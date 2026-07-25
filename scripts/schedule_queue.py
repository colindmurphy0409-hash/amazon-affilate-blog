#!/usr/bin/env python3
"""
Schedule pending posts from posts/queue.yaml to Blotato.

Usage:
  python scripts/schedule_queue.py          # schedule all pending posts with videos present
  python scripts/schedule_queue.py --dry-run
  python scripts/schedule_queue.py --id day-01-energy

Claude Code workflow:
  1. Export videos to posts/media/day-XX.mp4
  2. Run this script (or ask Cursor to run it)
  3. Review queue in Blotato app
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from _lib import ROOT, blotato_request, load_api_key, upload_local_video

QUEUE_PATH = ROOT / "posts" / "queue.yaml"


def resolve_queue_path(explicit: str | None) -> Path:
    if explicit:
        p = Path(explicit)
        return p if p.is_absolute() else ROOT / p
    return QUEUE_PATH


def resolve_media(api_key: str, video_value: str) -> str:
    if video_value.startswith("http://") or video_value.startswith("https://"):
        return video_value

    path = (ROOT / "posts" / video_value).resolve()
    if not path.exists():
        path = (ROOT / video_value).resolve()
    if not path.exists():
        raise FileNotFoundError(f"Video not found: {video_value}")

    print(f"  Uploading {path.name}...")
    return upload_local_video(api_key, path)


def schedule_post(api_key: str, account_id: str, platform: str, text: str, media_url: str, use_next_free_slot: bool) -> str:
    body: dict = {
        "post": {
            "accountId": account_id,
            "content": {
                "text": text,
                "mediaUrls": [media_url],
                "platform": platform,
            },
            "target": {"targetType": platform},
        }
    }

    if platform == "tiktok":
        body["post"].update({
            "privacyLevel": "PUBLIC_TO_EVERYONE",
            "disabledComments": False,
            "disabledDuet": False,
            "disabledStitch": False,
            "isBrandedContent": False,
            "isYourBrand": True,
            "isAiGenerated": True,
            "mediaType": "reel",
        })
    elif platform == "instagram":
        body["post"]["mediaType"] = "reel"

    if use_next_free_slot:
        body["useNextFreeSlot"] = True

    result = blotato_request("POST", "/posts", api_key, json=body)
    return result.get("postSubmissionId") or result.get("id") or str(result)


def main() -> int:
    parser = argparse.ArgumentParser(description="Schedule Wellthlab posts via Blotato")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be scheduled")
    parser.add_argument("--id", help="Only schedule one queue item by id")
    parser.add_argument("--queue", help="Queue YAML path (default: posts/queue.yaml)")
    args = parser.parse_args()

    queue_path = resolve_queue_path(args.queue)
    if not queue_path.exists():
        print(f"Missing {queue_path}")
        return 1

    data = yaml.safe_load(queue_path.read_text(encoding="utf-8"))
    defaults = data.get("defaults", {})
    tiktok_id = defaults.get("tiktok_account_id", "48023")
    instagram_id = defaults.get("instagram_account_id", "55960")
    use_slot = defaults.get("use_next_free_slot", True)

    api_key = None if args.dry_run else load_api_key()
    posts = data.get("posts", [])
    changed = False
    scheduled_count = 0
    skipped = []

    for post in posts:
        if post.get("status") == "scheduled":
            continue
        if args.id and post.get("id") != args.id:
            continue
        if post.get("status") != "pending":
            continue

        post_id = post.get("id", "unknown")
        video = post.get("video", "")
        caption = (post.get("caption") or "").strip()
        platforms = post.get("platforms", [])

        if not video:
            skipped.append(f"{post_id}: no video path")
            continue

        try:
            if args.dry_run:
                media_url = video if video.startswith("http") else str((ROOT / "posts" / video))
                if not Path(media_url).exists() and not video.startswith("http"):
                    media_url = str((ROOT / video))
                if not video.startswith("http") and not Path(media_url).exists():
                    skipped.append(f"{post_id}: video file missing ({video})")
                    continue
            else:
                media_url = resolve_media(api_key, video)
        except FileNotFoundError as e:
            skipped.append(str(e))
            continue

        print(f"\n[{post_id}]")
        submissions = []

        for platform in platforms:
            account_id = tiktok_id if platform == "tiktok" else instagram_id
            print(f"  → {platform} ({'dry-run' if args.dry_run else 'scheduling'})")
            if args.dry_run:
                submissions.append({"platform": platform, "dry_run": True})
                continue
            sub_id = schedule_post(api_key, account_id, platform, caption, media_url, use_slot)
            submissions.append({"platform": platform, "submission_id": sub_id})
            print(f"    queued: {sub_id}")

        post["status"] = "scheduled"
        post["scheduled_at"] = datetime.now(timezone.utc).isoformat()
        post["blotato"] = submissions
        changed = True
        scheduled_count += 1

    if changed and not args.dry_run:
        queue_path.write_text(yaml.dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        print(f"\nUpdated {queue_path}")

    print(f"\nDone: {scheduled_count} scheduled, {len(skipped)} skipped")
    for s in skipped:
        print(f"  - {s}")

    if skipped and scheduled_count == 0:
        print("\nTip: Claude Code exports videos to posts/media/ then re-run.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
