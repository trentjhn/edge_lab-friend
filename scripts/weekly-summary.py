"""Weekly trade summary. Aggregates the week's entries.

Usage:
    python scripts/weekly-summary.py --week 2026-04-27   # Monday's date
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "journal" / "entries"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_entry(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fields[k.strip()] = v.strip()
    return fields


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--week", required=True, help="Monday's date in YYYY-MM-DD")
    args = p.parse_args()

    monday = dt.date.fromisoformat(args.week)
    sunday = monday + dt.timedelta(days=6)

    entries = []
    for path in ENTRIES_DIR.glob("*.md"):
        e = parse_entry(path)
        if not e or "date" not in e:
            continue
        try:
            entry_date = dt.date.fromisoformat(e["date"])
        except ValueError:
            continue
        if monday <= entry_date <= sunday:
            entries.append(e)

    if not entries:
        print(f"No entries between {monday} and {sunday}.")
        return

    wins = sum(1 for e in entries if e.get("outcome") == "win")
    losses = sum(1 for e in entries if e.get("outcome") == "loss")
    total_r = 0.0
    for e in entries:
        try:
            total_r += float(e.get("r", 0))
        except ValueError:
            pass

    setups = {}
    for e in entries:
        s = e.get("setup", "?")
        setups[s] = setups.get(s, 0) + 1

    print(f"=== Week of {monday} ===")
    print(f"Total trades:      {len(entries)}")
    print(f"Wins / Losses:     {wins} / {losses}")
    print(f"Win rate:          {(wins / len(entries) * 100):.1f}%")
    print(f"Net R:             {total_r:+.2f}")
    print(f"Avg R / trade:     {(total_r / len(entries)):+.2f}")
    print(f"Setup breakdown:   {setups}")


if __name__ == "__main__":
    main()
