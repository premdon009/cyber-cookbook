"""Check every URL in resources.yml and every external link in docs/**/*.md.

Usage:  uv run python scripts/check_links.py [--only-resources] [--workers 16]

Exit 1 only on hard failures (404/410, DNS / connection errors). Sites that block
bots (401/403/429/503 and similar) are reported as WARN so you can check them by hand.
"""

from __future__ import annotations

import argparse
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from _resources import ROOT, load

UA = "Mozilla/5.0 (X11; Linux x86_64) cyber-cookbook-linkcheck/1.0"
HARD = {404, 410}
LINK_RE = re.compile(r"\]\((https?://[^)\s]+)\)|<(https?://[^>\s]+)>")


def collect(only_resources: bool) -> dict[str, set[str]]:
    urls: dict[str, set[str]] = {}
    _, resources = load()
    for r in resources:
        for key in ("url", "repo"):
            if r.get(key):
                urls.setdefault(r[key].split("#")[0], set()).add(f"resources.yml: {r['name']}")
    if not only_resources:
        for md in (ROOT / "docs").rglob("*.md"):
            if md.parent.name in ("resources", "note-templates"):  # generated / placeholders
                continue
            for m in LINK_RE.finditer(md.read_text(encoding="utf-8")):
                url = (m.group(1) or m.group(2)).split("#")[0]
                urls.setdefault(url, set()).add(str(md.relative_to(ROOT)))
    return urls


def probe(url: str) -> tuple[str, str]:
    ctx = ssl.create_default_context()
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
                final = resp.geturl()
                note = f" -> {final}" if final.rstrip("/") != url.rstrip("/") else ""
                return "OK", f"{resp.status}{note}"
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (400, 403, 404, 405, 429, 501):
                continue  # many servers mishandle HEAD; retry with GET
            return ("FAIL" if e.code in HARD else "WARN"), str(e.code)
        except Exception as e:  # DNS, TLS, timeout, connection reset
            if method == "HEAD":
                continue
            if "timed out" in str(e) or isinstance(e, TimeoutError):
                return "WARN", "timeout"  # often network/geo blocking, not a dead site
            return "FAIL", type(e).__name__ + ": " + str(e)[:80]
    return "FAIL", "unreachable"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-resources", action="store_true")
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()

    urls = collect(args.only_resources)
    with ThreadPoolExecutor(args.workers) as pool:
        results = dict(zip(urls, pool.map(probe, urls)))

    counts = {"OK": 0, "WARN": 0, "FAIL": 0}
    for url in sorted(urls):
        status, detail = results[url]
        counts[status] += 1
        if status != "OK" or "->" in detail:
            where = ", ".join(sorted(urls[url]))
            print(f"{status:4} {detail:>8}  {url}  [{where}]")
    print(f"\n{len(urls)} URLs: {counts['OK']} ok, {counts['WARN']} warn, {counts['FAIL']} fail")
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
