"""Futures position sizer for ES, NQ, GC, SI.

Usage:
    python scripts/position-sizer-futures.py --instrument ES --entry 5500.00 --stop 5495.00 --account 20000 --risk-pct 1.5
"""

from __future__ import annotations

import argparse
import math

TICK_VALUE = {  # USD per tick per contract
    "ES": 12.50,
    "NQ": 5.00,
    "GC": 10.00,
    "SI": 25.00,
}

TICK_SIZE = {  # price increment per tick
    "ES": 0.25,
    "NQ": 0.25,
    "GC": 0.10,
    "SI": 0.005,
}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--instrument", choices=list(TICK_VALUE), required=True)
    p.add_argument("--entry", type=float, required=True)
    p.add_argument("--stop", type=float, required=True)
    p.add_argument("--account", type=float, required=True)
    p.add_argument("--risk-pct", type=float, default=1.5, help="Default 1.5%%")
    args = p.parse_args()

    tick_value = TICK_VALUE[args.instrument]
    tick_size = TICK_SIZE[args.instrument]

    stop_distance_price = abs(args.entry - args.stop)
    stop_ticks = stop_distance_price / tick_size

    if stop_ticks < 1:
        print("ERROR: stop is closer than 1 tick to entry. Widen the stop or skip the trade.")
        return

    dollar_risk_target = args.account * (args.risk_pct / 100.0)
    risk_per_contract = stop_ticks * tick_value
    contracts = math.floor(dollar_risk_target / risk_per_contract)
    actual_risk = contracts * risk_per_contract

    print(f"Instrument:        {args.instrument}")
    print(f"Entry:             {args.entry}")
    print(f"Stop:              {args.stop}")
    print(f"Stop distance:     {stop_distance_price:.4f} ({stop_ticks:.1f} ticks)")
    print(f"Tick value:        ${tick_value:.2f} per contract")
    print(f"Risk per contract: ${risk_per_contract:.2f}")
    print(f"Account:           ${args.account:,.2f}")
    print(f"Risk %:            {args.risk_pct}%  → ${dollar_risk_target:,.2f}")
    print(f"Contracts:         {contracts}")
    print(f"Actual $ at risk:  ${actual_risk:,.2f}")

    if contracts == 0:
        print("\n⚠️  WARNING: 0 contracts — stop too wide for account at this risk%.")
        print("   Either tighten stop, increase risk%, or skip the trade.")
    elif actual_risk > dollar_risk_target * 1.05:
        print("\n⚠️  Actual risk exceeds target by >5%. Consider 1 fewer contract.")


if __name__ == "__main__":
    main()
