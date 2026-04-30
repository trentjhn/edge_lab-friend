"""Interactive trade logger. Prompts for fields, writes journal/entries/<date>-<symbol>-<tf>.md."""

from __future__ import annotations

import datetime as dt
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "journal" / "entries"
TEMPLATE_PATH = ROOT / "journal" / "template.md"


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    answer = input(f"{prompt}{suffix}: ").strip()
    return answer or default


def main() -> None:
    today = dt.date.today().isoformat()

    print("=== Log a trade ===\n")
    date = ask("Date", today)
    symbol = ask("Symbol (ES, NQ, GC, SI, SPY, QQQ)").upper()
    instrument = ask("Instrument (futures/options)", "futures")
    timeframe = ask("Timeframe (1m/5m/15m)", "5m")
    setup = ask("Setup (SETUP-1 / SETUP-2)").upper().replace(" ", "-")
    direction = ask("Direction (long/short)").lower()

    entry_time = ask("Entry time (HH:MM PT)")
    exit_time = ask("Exit time (HH:MM PT)")
    entry_price = ask("Entry price")
    stop = ask("Stop")
    target = ask("Target")
    exit_price = ask("Exit price")
    mae = ask("MAE (max adverse excursion in $ or R)")
    mfe = ask("MFE (max favorable excursion in $ or R)")
    r = ask("R outcome (e.g., 1.8 or -1)")
    pnl = ask("$ P&L")
    outcome = ask("Outcome (win/loss/breakeven)").lower()

    level = ask("Level being tested (e.g., 'closest 1H high at 5505')")
    sweep = ask("Sweep details (where, on what TF)")
    fvg = ask("FVG details (price range, TF)")
    stop_rule = ask("Stop rule (FVG-near-sweep tight stop / iFVG line stop)")

    worked = ask("What worked")
    didnt = ask("What didn't")
    emotion = ask("Emotional state (1 sentence)")
    obeyed = ask("Did this obey the framework? (yes/no — and why)")

    filename = f"{date}-{symbol}-{timeframe}.md"
    path = ENTRIES_DIR / filename
    ENTRIES_DIR.mkdir(parents=True, exist_ok=True)

    body = f"""---
date: {date}
symbol: {symbol}
instrument: {instrument}
timeframe: {timeframe}
setup: {setup}
direction: {direction}
r: {r}
outcome: {outcome}
---

# {date} — {symbol} {timeframe} — {setup}

## Trade Mechanics
- **Entry time:** {entry_time}
- **Exit time:** {exit_time}
- **Entry price:** {entry_price}
- **Stop:** {stop}
- **Target:** {target}
- **Exit price:** {exit_price}
- **MAE:** {mae}
- **MFE:** {mfe}
- **R:** {r}
- **$ P&L:** {pnl}

## Setup Notes
- **Level being tested:** {level}
- **Sweep details:** {sweep}
- **FVG details:** {fvg}
- **Stop rule applied:** {stop_rule}

## Reflection
- **What worked:** {worked}
- **What didn't:** {didnt}
- **Emotional state:** {emotion}
- **Did this trade obey the framework?** {obeyed}
"""

    path.write_text(body, encoding="utf-8")
    print(f"\nWrote {path.relative_to(ROOT)}")

    print("Rebuilding journal index...")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build-index.py")], check=False)


if __name__ == "__main__":
    main()
