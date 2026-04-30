"""Options position sizer for SPY/QQQ. Treats max-loss as full premium.

Usage:
    python scripts/position-sizer-options.py --premium 2.45 --contracts 5 --account 20000
"""

from __future__ import annotations

import argparse


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--premium", type=float, required=True, help="Per-contract premium (e.g., 2.45)")
    p.add_argument("--contracts", type=int, required=True)
    p.add_argument("--account", type=float, required=True)
    args = p.parse_args()

    cost_per_contract = args.premium * 100  # 100 shares per contract
    total_cost = cost_per_contract * args.contracts
    pct_account = (total_cost / args.account) * 100

    print(f"Premium:        ${args.premium:.2f}")
    print(f"Contracts:      {args.contracts}")
    print(f"Cost / ctr:     ${cost_per_contract:.2f}")
    print(f"Total cost:     ${total_cost:,.2f}")
    print(f"% of account:   {pct_account:.2f}%")
    print(f"Max loss:       ${total_cost:,.2f} (full premium assumption)")

    if pct_account > 5:
        print("\n⚠️  WARNING: position is >5% of account. Cut contracts.")
    elif pct_account > 2:
        print("\n⚠️  >2% of account at risk — verify this is intended size.")


if __name__ == "__main__":
    main()
