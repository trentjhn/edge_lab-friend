"""Historical open price lookup via yfinance.

Usage:
    python scripts/lookup_price.py --ticker ES=F --period 2026
    python scripts/lookup_price.py --ticker NQ=F --period 2026-Q1
    python scripts/lookup_price.py --ticker SPY  --period 2026-04
"""

from __future__ import annotations

import argparse
import datetime as dt
import re

import yfinance as yf

YEAR_RE = re.compile(r"^(\d{4})$")
QUARTER_RE = re.compile(r"^(\d{4})-Q([1-4])$")
MONTH_RE = re.compile(r"^(\d{4})-(\d{2})$")


def first_trading_day(target: dt.date) -> dt.date:
    """yfinance returns whatever's available; we try to fetch a window starting from `target`."""
    return target


def parse_period(period: str) -> dt.date:
    if (m := YEAR_RE.match(period)):
        return dt.date(int(m.group(1)), 1, 1)
    if (m := QUARTER_RE.match(period)):
        year, q = int(m.group(1)), int(m.group(2))
        month = (q - 1) * 3 + 1
        return dt.date(year, month, 1)
    if (m := MONTH_RE.match(period)):
        return dt.date(int(m.group(1)), int(m.group(2)), 1)
    raise ValueError(f"Bad period: {period}. Use YYYY, YYYY-QN, or YYYY-MM.")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", required=True)
    p.add_argument("--period", required=True, help="YYYY | YYYY-QN | YYYY-MM")
    args = p.parse_args()

    target = parse_period(args.period)
    end = target + dt.timedelta(days=10)

    df = yf.Ticker(args.ticker).history(start=target.isoformat(), end=end.isoformat(), interval="1d")
    if df.empty:
        print(f"No data for {args.ticker} starting {target}.")
        return

    first = df.iloc[0]
    print(f"{args.ticker} — {args.period} open:")
    print(f"  Date:  {df.index[0].date()}")
    print(f"  Open:  {first['Open']:.2f}")
    print(f"  Close: {first['Close']:.2f}")


if __name__ == "__main__":
    main()
