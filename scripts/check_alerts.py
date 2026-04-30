"""Check pending watchlist setups against current prices via yfinance."""

from __future__ import annotations

import re
from pathlib import Path

import yfinance as yf

ROOT = Path(__file__).resolve().parent.parent
PENDING_PATH = ROOT / "context" / "pending-setups.md"

ROW_RE = re.compile(r"^\|\s*([A-Z=\-^]+)\s*\|.*?\|\s*([\d.]+)\s*\|", re.MULTILINE)
TICKER_MAP = {
    "ES": "ES=F",
    "NQ": "NQ=F",
    "GC": "GC=F",
    "SI": "SI=F",
}


def fetch_price(ticker: str) -> float | None:
    yf_ticker = TICKER_MAP.get(ticker, ticker)
    try:
        info = yf.Ticker(yf_ticker).fast_info
        return float(info.last_price)
    except Exception:
        return None


def main() -> None:
    if not PENDING_PATH.exists():
        print("No pending setups file.")
        return

    text = PENDING_PATH.read_text(encoding="utf-8")
    rows = ROW_RE.findall(text)
    if not rows:
        print("No watchlist entries.")
        return

    print(f"Checking {len(rows)} watchlist entries...\n")
    alerts = []
    for symbol, target_str in rows:
        target = float(target_str)
        current = fetch_price(symbol)
        if current is None:
            print(f"  {symbol}: price fetch failed")
            continue
        pct_dist = abs(current - target) / target * 100
        marker = " 🔔" if pct_dist <= 1.0 else ""
        print(f"  {symbol}: ${current:.2f} (target ${target:.2f}, {pct_dist:.2f}% away){marker}")
        if pct_dist <= 1.0:
            alerts.append((symbol, current, target, pct_dist))

    if alerts:
        print("\n=== ALERTS (within 1%) ===")
        for symbol, current, target, pct_dist in alerts:
            print(f"  🔔 {symbol}: ${current:.2f} → ${target:.2f} ({pct_dist:.2f}% away)")
    else:
        print("\nNo alerts.")


if __name__ == "__main__":
    main()
