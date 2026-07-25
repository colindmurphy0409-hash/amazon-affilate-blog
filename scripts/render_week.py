#!/usr/bin/env python3
"""Batch-render Remotion compositions from content/week-XX/remotion-props.json."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "video"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Wellthlab Remotion week batch")
    parser.add_argument("--week", required=True, help="ISO week number, e.g. 30")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    props_path = ROOT / "content" / f"week-{args.week}" / "remotion-props.json"
    if not props_path.exists():
        print(f"Missing {props_path}")
        return 1

    data = json.loads(props_path.read_text(encoding="utf-8"))
    compositions = data.get("compositions", [])
    if not compositions:
        print("No compositions in props file")
        return 1

    for item in compositions:
        comp_id = item["id"]
        output = ROOT / item["output"]
        props = item.get("props", {})
        output.parent.mkdir(parents=True, exist_ok=True)

        props_json = json.dumps(props)
        cmd = [
            "npx",
            "remotion",
            "render",
            comp_id,
            str(output),
            f"--props={props_json}",
        ]
        print(f"Rendering {comp_id} -> {output}")
        if args.dry_run:
            print(f"  dry-run: {' '.join(cmd)}")
            continue

        result = subprocess.run(cmd, cwd=VIDEO_DIR, shell=True)
        if result.returncode != 0:
            print(f"Failed rendering {comp_id}")
            return result.returncode

    print(f"Done: {len(compositions)} composition(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
