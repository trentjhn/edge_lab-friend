"""Cross-platform command runner. Subcommands: refresh, log, check, weekly, lookup."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


def run_script(name: str, *extra: str) -> int:
    cmd = [sys.executable, str(SCRIPTS / name), *extra]
    return subprocess.run(cmd).returncode


def main() -> None:
    p = argparse.ArgumentParser(prog="run")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("refresh", help="Pull market data + rebuild journal index.")
    sub.add_parser("log", help="Log a trade interactively.")
    sub.add_parser("check", help="Check watchlist alerts against current prices.")

    weekly = sub.add_parser("weekly", help="Weekly trade summary.")
    weekly.add_argument("--week", required=True)

    lookup = sub.add_parser("lookup", help="Historical open price lookup.")
    lookup.add_argument("--ticker", required=True)
    lookup.add_argument("--period", required=True)

    args = p.parse_args()

    if args.cmd == "refresh":
        rc = run_script("fetch_market_state.py")
        if rc == 0:
            run_script("build-index.py")
    elif args.cmd == "log":
        run_script("log-trade.py")
    elif args.cmd == "check":
        run_script("check_alerts.py")
    elif args.cmd == "weekly":
        run_script("weekly-summary.py", "--week", args.week)
    elif args.cmd == "lookup":
        run_script("lookup_price.py", "--ticker", args.ticker, "--period", args.period)


if __name__ == "__main__":
    main()
