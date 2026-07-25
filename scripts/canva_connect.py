#!/usr/bin/env python3
"""
Canva Connect OAuth setup for Wellthlab agents.

Usage:
  # 1. Create integration at https://www.canva.com/developers/integrations
  # 2. Set redirect URL: http://127.0.0.1:3001/oauth/redirect
  # 3. Run:
  python scripts/canva_connect.py connect --client-id YOUR_ID --client-secret YOUR_SECRET

  python scripts/canva_connect.py test
  python scripts/canva_connect.py list-templates
  python scripts/canva_connect.py list-dataset TEMPLATE_ID
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import secrets
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "tools" / "canva.yaml"
EXAMPLE_PATH = ROOT / "tools" / "canva.example.yaml"

CANVA_AUTH = "https://www.canva.com/api/oauth/authorize"
CANVA_TOKEN = "https://api.canva.com/rest/v1/oauth/token"
CANVA_API = "https://api.canva.com/rest/v1"

REDIRECT_URI = "http://127.0.0.1:3001/oauth/redirect"
SCOPES = " ".join([
    "design:content:read",
    "design:content:write",
    "design:meta:read",
    "asset:read",
    "asset:write",
    "brandtemplate:meta:read",
    "brandtemplate:content:read",
    "profile:read",
])


def pkce_pair() -> tuple[str, str]:
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode()).digest()
    ).rstrip(b"=").decode()
    return verifier, challenge


def basic_auth_header(client_id: str, client_secret: str) -> dict[str, str]:
    creds = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    return {"Authorization": f"Basic {creds}"}


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
    if EXAMPLE_PATH.exists():
        return yaml.safe_load(EXAMPLE_PATH.read_text(encoding="utf-8")) or {}
    return {}


def save_config(cfg: dict) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(yaml.dump(cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Saved {CONFIG_PATH}")


def exchange_code(client_id: str, client_secret: str, code: str, code_verifier: str) -> dict:
    resp = requests.post(
        CANVA_TOKEN,
        headers={
            **basic_auth_header(client_id, client_secret),
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": code,
            "code_verifier": code_verifier,
            "redirect_uri": REDIRECT_URI,
        },
        timeout=30,
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"Token exchange failed ({resp.status_code}): {resp.text}")
    return resp.json()


def refresh_access_token(cfg: dict) -> str:
    resp = requests.post(
        CANVA_TOKEN,
        headers={
            **basic_auth_header(cfg["client_id"], cfg["client_secret"]),
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": cfg["refresh_token"],
        },
        timeout=30,
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"Token refresh failed ({resp.status_code}): {resp.text}")
    data = resp.json()
    if data.get("refresh_token"):
        cfg["refresh_token"] = data["refresh_token"]
        save_config(cfg)
    return data["access_token"]


def cmd_connect(client_id: str, client_secret: str) -> int:
    code_verifier, code_challenge = pkce_pair()
    state = secrets.token_urlsafe(32)

    params = {
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "scope": SCOPES,
        "response_type": "code",
        "client_id": client_id,
        "state": state,
        "redirect_uri": REDIRECT_URI,
    }
    auth_url = f"{CANVA_AUTH}?{urlencode(params)}"

    result: dict[str, str] = {}
    done = threading.Event()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            return

        def do_GET(self):
            parsed = urlparse(self.path)
            if parsed.path != "/oauth/redirect":
                self.send_response(404)
                self.end_headers()
                return
            qs = parse_qs(parsed.query)
            if qs.get("state", [""])[0] != state:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"State mismatch")
                return
            if "error" in qs:
                result["error"] = qs["error"][0]
            else:
                result["code"] = qs.get("code", [""])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<html><body><h1>Canva connected!</h1>"
                b"<p>You can close this tab and return to Cursor.</p></body></html>"
            )
            done.set()

    server = HTTPServer(("127.0.0.1", 3001), Handler)
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()

    print("\nOpening Canva authorization in your browser...")
    print(f"If it does not open, visit:\n{auth_url}\n")
    webbrowser.open(auth_url)

    done.wait(timeout=300)
    server.server_close()

    if result.get("error"):
        print(f"Authorization error: {result['error']}")
        return 1
    if not result.get("code"):
        print("Timed out waiting for authorization (5 min). Try again.")
        return 1

    tokens = exchange_code(client_id, client_secret, result["code"], code_verifier)
    cfg = load_config()
    cfg["client_id"] = client_id
    cfg["client_secret"] = client_secret
    cfg["refresh_token"] = tokens["refresh_token"]
    cfg.setdefault("redirect_uri", REDIRECT_URI)
    example = yaml.safe_load(EXAMPLE_PATH.read_text(encoding="utf-8")) if EXAMPLE_PATH.exists() else {}
    cfg.setdefault("brand_templates", example.get("brand_templates", {}))
    cfg.setdefault("field_map", example.get("field_map", {}))
    cfg.setdefault("defaults", example.get("defaults", {}))
    save_config(cfg)

    print("Canva connected successfully.")
    print(f"Scopes: {tokens.get('scope', 'unknown')}")
    print("\nNext: python scripts/canva_connect.py list-templates")
    print("Then paste template IDs into tools/canva.yaml under brand_templates.")
    return 0


def cmd_test() -> int:
    cfg = load_config()
    if not cfg.get("refresh_token"):
        print("Not connected. Run: python scripts/canva_connect.py connect --client-id ... --client-secret ...")
        return 1
    token = refresh_access_token(cfg)
    resp = requests.get(
        f"{CANVA_API}/users/me/profile",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    if resp.status_code >= 400:
        print(f"API test failed ({resp.status_code}): {resp.text}")
        return 1
    profile = resp.json()
    print("Canva connection OK.")
    print(json.dumps(profile, indent=2)[:500])
    return 0


def cmd_list_templates() -> int:
    cfg = load_config()
    if not cfg.get("refresh_token"):
        print("Not connected.")
        return 1
    token = refresh_access_token(cfg)
    resp = requests.get(
        f"{CANVA_API}/brand-templates",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    if resp.status_code >= 400:
        print(f"List templates failed ({resp.status_code}): {resp.text}")
        if resp.status_code == 403:
            print("\nBrand templates require Canva Enterprise. Use a Private integration on Enterprise,")
            print("or agents will use browser automation + standard designs until then.")
        return 1
    data = resp.json()
    items = data.get("items", [])
    if not items:
        print("No brand templates found. Create one in Canva with autofill fields.")
        return 0
    print(f"Found {len(items)} brand template(s):\n")
    for item in items:
        print(f"  ID: {item.get('id')}")
        print(f"  Title: {item.get('title')}")
        print()
    print("Copy IDs into tools/canva.yaml -> brand_templates.carousel_1080x1350")
    return 0


def cmd_list_dataset(template_id: str) -> int:
    cfg = load_config()
    token = refresh_access_token(cfg)
    resp = requests.get(
        f"{CANVA_API}/brand-templates/{template_id}/dataset",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    if resp.status_code >= 400:
        print(f"Dataset failed ({resp.status_code}): {resp.text}")
        return 1
    print(json.dumps(resp.json(), indent=2))
    print("\nMap field names above to field_map in tools/canva.yaml")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Canva Connect setup for Wellthlab")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_connect = sub.add_parser("connect", help="OAuth PKCE flow")
    p_connect.add_argument("--client-id", required=True)
    p_connect.add_argument("--client-secret", required=True)

    sub.add_parser("test", help="Verify saved credentials")
    sub.add_parser("list-templates", help="List brand templates (Enterprise)")
    p_ds = sub.add_parser("list-dataset", help="Show autofill fields for a template")
    p_ds.add_argument("template_id")

    args = parser.parse_args()

    if args.cmd == "connect":
        return cmd_connect(args.client_id, args.client_secret)
    if args.cmd == "test":
        return cmd_test()
    if args.cmd == "list-templates":
        return cmd_list_templates()
    if args.cmd == "list-dataset":
        return cmd_list_dataset(args.template_id)
    return 1


if __name__ == "__main__":
    sys.exit(main())
