#!/usr/bin/env python3
"""
Agent-driven Canva production: autofill brand template → export → posts/media/

Usage:
  python scripts/canva_produce.py --week 30 --brief strips-vs-pills
  python scripts/canva_produce.py --week 30 --brief strips-vs-pills --dry-run

Requires tools/canva.yaml (copy from tools/canva.example.yaml).
Without config, exits with instructions for browser-automation fallback.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
CANVA_API = "https://api.canva.com/rest/v1"
CANVA_TOKEN = f"{CANVA_API}/oauth/token"
CONFIG_PATH = ROOT / "tools" / "canva.yaml"


def load_config(*, required: bool = True) -> dict | None:
    if not CONFIG_PATH.exists():
        if not required:
            return None
        print(
            "Missing tools/canva.yaml - agent should use browser automation (workflows/canva-production.md Path B)\n"
            "Or copy tools/canva.example.yaml to tools/canva.yaml and complete OAuth setup."
        )
        sys.exit(2)
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def refresh_access_token(cfg: dict) -> str:
    import base64

    creds = base64.b64encode(
        f"{cfg['client_id']}:{cfg['client_secret']}".encode()
    ).decode()
    resp = requests.post(
        CANVA_TOKEN,
        headers={
            "Authorization": f"Basic {creds}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": cfg["refresh_token"],
        },
        timeout=30,
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"Canva token refresh failed ({resp.status_code}): {resp.text}")
    data = resp.json()
    token = data.get("access_token")
    if not token:
        raise RuntimeError(f"No access_token in response: {data}")
    return token


def api_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def load_brief(week: str, brief_id: str) -> dict:
    path = ROOT / "content" / f"week-{week}" / "canva-briefs.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    briefs = data.get("briefs", {})
    if brief_id not in briefs:
        raise KeyError(f"Brief '{brief_id}' not in {path}. Available: {list(briefs)}")
    return briefs[brief_id]


def build_autofill_data(brief: dict, field_map: dict) -> dict:
    """Map brief YAML to Canva autofill field payload."""
    data: dict = {}

    def get_nested(obj: dict, dotted: str):
        cur = obj
        for part in dotted.split("."):
            cur = cur[part]
        return cur

    for canva_field, brief_path in field_map.items():
        try:
            value = get_nested(brief, brief_path)
        except (KeyError, TypeError):
            continue
        if canva_field == "product_image" or brief_path.endswith("_url"):
            data[canva_field] = {"type": "image", "asset_id": value} if str(value).startswith("M") else {"type": "image", "url": value}
        else:
            data[canva_field] = {"type": "text", "text": str(value)}
    return data


def start_autofill(token: str, template_id: str, title: str, data: dict) -> str:
    resp = requests.post(
        f"{CANVA_API}/autofills",
        headers=api_headers(token),
        json={"brand_template_id": template_id, "title": title, "data": data},
        timeout=60,
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"Autofill start failed ({resp.status_code}): {resp.text}")
    job = resp.json().get("job", {})
    job_id = job.get("id")
    if not job_id:
        raise RuntimeError(f"No job id: {resp.json()}")
    return job_id


def poll_autofill(token: str, job_id: str, interval: int, timeout: int) -> str:
    deadline = time.time() + timeout
    while time.time() < deadline:
        resp = requests.get(
            f"{CANVA_API}/autofills/{job_id}",
            headers=api_headers(token),
            timeout=30,
        )
        resp.raise_for_status()
        job = resp.json().get("job", {})
        status = job.get("status")
        if status == "success":
            design = job.get("result", {}).get("design", {})
            design_id = design.get("id")
            if not design_id:
                raise RuntimeError(f"Autofill success but no design id: {job}")
            return design_id
        if status == "failed":
            raise RuntimeError(f"Autofill failed: {job.get('error', job)}")
        time.sleep(interval)
    raise TimeoutError(f"Autofill job {job_id} timed out after {timeout}s")


def start_export(token: str, design_id: str, fmt: str) -> str:
    format_body = {"type": fmt}
    if fmt == "mp4":
        format_body["quality"] = "horizontal_1080p"
    resp = requests.post(
        f"{CANVA_API}/exports",
        headers=api_headers(token),
        json={"design_id": design_id, "format": format_body},
        timeout=60,
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"Export start failed ({resp.status_code}): {resp.text}")
    job = resp.json().get("job", {})
    export_id = job.get("id")
    if not export_id:
        raise RuntimeError(f"No export job id: {resp.json()}")
    return export_id


def poll_export(token: str, export_id: str, interval: int, timeout: int) -> list[str]:
    deadline = time.time() + timeout
    while time.time() < deadline:
        resp = requests.get(
            f"{CANVA_API}/exports/{export_id}",
            headers=api_headers(token),
            timeout=30,
        )
        resp.raise_for_status()
        job = resp.json().get("job", {})
        status = job.get("status")
        if status == "success":
            urls = job.get("urls", []) or []
            if not urls:
                result = job.get("result", {})
                urls = result.get("urls", []) if isinstance(result, dict) else []
            return urls
        if status == "failed":
            raise RuntimeError(f"Export failed: {job.get('error', job)}")
        time.sleep(interval)
    raise TimeoutError(f"Export job {export_id} timed out after {timeout}s")


def download_file(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    dest.write_bytes(resp.content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Agent-driven Canva autofill + export")
    parser.add_argument("--week", required=True)
    parser.add_argument("--brief", required=True, help="Brief id from canva-briefs.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cfg = load_config(required=not args.dry_run)
    brief = load_brief(args.week, args.brief)

    if args.dry_run and cfg is None:
        output = ROOT / brief["output"]
        print(f"Dry-run (no canva.yaml): brief '{args.brief}'")
        print(f"  title: {brief.get('title', args.brief)}")
        print(f"  template_key: {brief.get('template_key')}")
        print(f"  export: {brief.get('export_format', 'mp4')} -> {output}")
        print(f"  slides: {list(brief.keys())}")
        print("Agent: use browser automation until tools/canva.yaml is configured.")
        return 0

    cfg = cfg or {}
    defaults = cfg.get("defaults", {})
    interval = int(defaults.get("poll_interval_seconds", 5))
    timeout = int(defaults.get("poll_timeout_seconds", 300))
    export_fmt = brief.get("export_format") or defaults.get("export_format", "mp4")

    template_key = brief.get("template_key", "carousel_1080x1350")
    template_id = cfg.get("brand_templates", {}).get(template_key, "")
    if not template_id:
        print(f"No brand_templates.{template_key} in canva.yaml")
        return 1

    field_map = cfg.get("field_map", {})
    autofill_data = build_autofill_data(brief, field_map)
    output = ROOT / brief["output"]

    if args.dry_run:
        print(f"Would autofill template {template_id}")
        print(f"  title: {brief.get('title', args.brief)}")
        print(f"  fields: {list(autofill_data.keys())}")
        print(f"  export: {export_fmt} -> {output}")
        return 0

    token = refresh_access_token(cfg)
    job_id = start_autofill(token, template_id, brief.get("title", args.brief), autofill_data)
    print(f"Autofill job: {job_id}")
    design_id = poll_autofill(token, job_id, interval, timeout)
    print(f"Design created: {design_id}")

    export_id = start_export(token, design_id, export_fmt)
    print(f"Export job: {export_id}")
    urls = poll_export(token, export_id, interval, timeout)
    if not urls:
        raise RuntimeError("Export succeeded but no download URLs")

    download_file(urls[0], output)
    print(f"Saved -> {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
