# Risk Management

## Per-Trade Risk

- **Dollar risk:** $200 - $300 per trade
- **Account %:** 1% - 2% of account (account size in `.env` as `ACCOUNT_SIZE`)
- **Default risk %:** 1.5% (mid-band)

The position sizer reads `ACCOUNT_SIZE` from `.env` and computes contract count from your stop distance.

## Stop Placement Rules

There are exactly two stop rules. Every trade uses one of them. Claude will refuse to size a trade until you specify which.

### Stop Rule 1 — FVG-near-sweep tight stop (SETUP-1)
- Stop is just past the sweep wick — the high (for shorts) or low (for longs) of the sweep candle, plus 1-2 ticks of buffer.
- This is the *tighter* of the two stops. Used when the FVG you're entering at is right next to the sweep.

### Stop Rule 2 — iFVG line stop (SETUP-2)
- Stop is exactly at the inversion line of the iFVG.
- For a bearish iFVG (former bullish FVG broken below): stop is just above the top of the iFVG zone.
- For a bullish iFVG (former bearish FVG broken above): stop is just below the bottom of the iFVG zone.

## Sizing Math

### Futures (ES, NQ, GC, SI)
Use `python scripts/position-sizer-futures.py --instrument X --entry X --stop X --account X --risk-pct X`.

Tick values:
- ES: $12.50 / tick (0.25 point increment)
- NQ: $5 / tick (0.25 point increment)
- GC: $10 / tick (0.10 point increment)
- SI: $25 / tick (0.005 point increment)

Formula: `contracts = floor((account × risk_pct/100) ÷ (stop_ticks × tick_value))`

If contracts comes out to 0, your stop is too wide for the account at your risk %. Either tighten the stop, take a smaller %, or skip the trade.

### Options (SPY, QQQ)
Use `python scripts/position-sizer-options.py --premium X --contracts X --account X`.

Max-loss assumption: full premium. Don't pretend stops on options work the way they do on shares.

If `% of account` > 5%, the script flags it. Don't override the flag.

## Targets

Minimum 1:2 RR. Never take a trade with target < 2R.

If the next opposing relevant level is closer than 2R, skip the trade or wait for a pullback that gives you a tighter entry.

## Trade Management

- At 1R: trail stop to break-even.
- At 2R: take half off, let the rest run with trail at 1R behind.
- Never widen a stop. Ever.
