"""Shallow-clone (or update) every `clone: true` repo from resources.yml into resources/.

Usage:
  uv run python scripts/fetch_resources.py              # clone / pull all
  uv run python scripts/fetch_resources.py --dry-run    # just list what would happen
  uv run python scripts/fetch_resources.py --only hacktricks sigma   # name substring filter

resources/ is git-ignored. Clones are --depth 1 to stay small.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from _resources import ROOT, load

DEST = ROOT / "resources"


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", nargs="*", default=[], help="case-insensitive name substrings")
    args = ap.parse_args()

    _, resources = load()
    todo = [r for r in resources if r.get("clone")]
    if args.only:
        wanted = [w.lower() for w in args.only]
        todo = [r for r in todo if any(w in r["name"].lower() for w in wanted)]

    failures = 0
    for r in todo:
        target = DEST / r["category"] / slug(r["name"])
        if target.exists():
            cmd = ["git", "-C", str(target), "pull", "--ff-only", "--depth", "1"]
            action = "update"
        else:
            cmd = ["git", "clone", "--depth", "1", "--single-branch", r["repo"], str(target)]
            action = "clone"
        print(f"[{action}] {r['name']} -> {target.relative_to(ROOT)}")
        if args.dry_run:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if subprocess.run(cmd, check=False).returncode != 0:
            failures += 1
            print(f"  !! failed: {r['name']}")
    print(f"{len(todo)} repos, {failures} failed{' (dry run)' if args.dry_run else ''}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
