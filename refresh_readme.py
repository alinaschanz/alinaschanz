#!/usr/bin/env python3
"""rewrite the live block of README.md from public data: the gasweek daily dataset and the site feed.

runs in the profile repository's workflow once a day; standard library only, no keys.
everything between the two marker comments is replaced, the rest of the file is untouched.
"""
from __future__ import annotations

import csv
import io
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

DAILY = "https://raw.githubusercontent.com/alinaschanz/gasweek/main/data/daily.csv"
FEED = "https://alinaschanz.life/feed.xml"
START, END = "<!-- live:start -->", "<!-- live:end -->"
UA = {"User-Agent": "alinaschanz-profile-refresh/1.0"}


def get(url: str, timeout: float = 30.0) -> str:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read().decode("utf-8")


def gwei(v: float) -> str:
    return f"{v:.3f}" if v < 1 else f"{v:.2f}" if v < 10 else f"{v:.1f}"


def gas_lines() -> list[str]:
    rows = list(csv.DictReader(io.StringIO(get(DAILY))))
    if not rows:
        return []
    last = rows[-1]
    week = rows[-7:]
    medians = [float(r["median_gwei"]) for r in week]
    cheapest = int(last["cheapest_hour_utc"])
    priciest = int(last["priciest_hour_utc"])
    return [
        f"- base fee on {last['date_utc']}: median {gwei(float(last['median_gwei']))} gwei, "
        f"p90 {gwei(float(last['p90_gwei']))}, cheapest hour {cheapest:02d}:00 utc, priciest {priciest:02d}:00 utc",
        f"- last {len(week)} day{'s' if len(week) != 1 else ''}: medians from {gwei(min(medians))} to {gwei(max(medians))} gwei "
        f"([the dataset](https://github.com/alinaschanz/gasweek/blob/main/data/daily.csv))",
    ]


def note_lines() -> list[str]:
    root = ET.fromstring(get(FEED))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entries = root.findall("a:entry", ns)
    if not entries:
        return []
    e = entries[0]
    title = (e.findtext("a:title", default="", namespaces=ns) or "").strip()
    link = e.find("a:link", ns)
    href = link.get("href") if link is not None else "https://alinaschanz.life/notes/"
    updated = (e.findtext("a:updated", default="", namespaces=ns) or "")[:10]
    return [f"- latest note: [{title}]({href}) ({updated})"]


def main() -> int:
    readme = Path(__file__).with_name("README.md")
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print("no live markers in README.md", file=sys.stderr)
        return 1
    lines: list[str] = []
    for fn in (gas_lines, note_lines):
        try:
            lines += fn()
        except Exception as exc:  # noqa: BLE001 - one source down must not blank the block
            print(f"{fn.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M utc")
    block = "\n".join([START, *lines, f"<sub>refreshed {stamp} by [refresh_readme.py](refresh_readme.py)</sub>", END])
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, text, count=1, flags=re.S)
    if new != text:
        readme.write_text(new, encoding="utf-8", newline="\n")
        print("README.md updated")
    else:
        print("README.md unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
