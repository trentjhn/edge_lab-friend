"""Walk journal/entries/, parse YAML frontmatter, write journal/INDEX.md."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "journal" / "entries"
INDEX_PATH = ROOT / "journal" / "INDEX.md"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_entry(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    fields["_path"] = str(path.relative_to(ROOT))
    return fields


def main() -> None:
    if not ENTRIES_DIR.exists():
        ENTRIES_DIR.mkdir(parents=True, exist_ok=True)

    entries = sorted(
        (e for e in (parse_entry(p) for p in ENTRIES_DIR.glob("*.md")) if e),
        key=lambda e: e.get("date", ""),
        reverse=True,
    )

    lines = [
        "# Journal Index",
        "",
        "Built by `scripts/build-index.py`. Do not edit manually.",
        "",
        "| Date | Symbol | TF | Setup | Direction | R | Outcome | File |",
        "|------|--------|----|----|-----------|---|---------|------|",
    ]

    for e in entries:
        lines.append(
            f"| {e.get('date', '?')} | {e.get('symbol', '?')} | {e.get('timeframe', '?')} "
            f"| {e.get('setup', '?')} | {e.get('direction', '?')} | {e.get('r', '?')} "
            f"| {e.get('outcome', '?')} | [{Path(e['_path']).name}]({e['_path']}) |"
        )

    if not entries:
        lines.append("")
        lines.append("*No entries yet.*")

    INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {INDEX_PATH} — {len(entries)} entries.")


if __name__ == "__main__":
    main()
