# Playbook — SETUP-2: Inverse FVG Rejection

Step-by-step execution. Follow exactly.

## Step 1 — Identify the prior FVG

On 5m or 15m, find an FVG that has been **broken** — meaning price closed cleanly through it (not just wicked).

**Pass criteria:** A specific FVG zone you can mark, with confirmation it was broken (a candle closed past the FVG zone).
**Fail:** FVG that's only been wicked through, or no recent broken FVGs → wait.

## Step 2 — Confirm the inversion

Once broken, the FVG inverts polarity:
- A **broken bullish FVG** (price closed below it) now acts as **bearish resistance**.
- A **broken bearish FVG** (price closed above it) now acts as **bullish support**.

**Pass criteria:** Price has moved away from the broken FVG and is now drifting back toward it.
**Fail:** Price never returns to the FVG zone → no setup.

## Step 3 — Confirm HTF alignment

Check 1H/4H bias (per `timeframe-rules.md`). The setup direction (rejection away from the iFVG) must align with the HTF trend.

**Pass criteria:** HTF bias is in the direction of the rejection.
**Fail:** HTF says continuation through the iFVG → no trade.

## Step 4 — Watch for the retest

On 5m or 1m, wait for price to come back to the iFVG zone.

**Pass criteria:** Price wicks into the iFVG zone or touches the iFVG line.
**Fail:** Price stops short of the zone → no entry, but stay on watch.

## Step 5 — Entry trigger

Wait for a rejection candle close at the iFVG line.

- **Bearish iFVG (short setup):** 1m candle wicks up into the iFVG zone, closes back below the iFVG top.
- **Bullish iFVG (long setup):** 1m candle wicks down into the iFVG zone, closes back above the iFVG bottom.

Enter at market on the close of the rejection candle, OR set a limit at the iFVG line.

## Step 6 — Stop placement

**Stop Rule 2 (per `risk-management.md`):** Exactly at the iFVG line.
- **Bearish iFVG (short):** stop just above the top of the iFVG zone.
- **Bullish iFVG (long):** stop just below the bottom of the iFVG zone.

This is structural — if price closes through the iFVG, the setup is invalidated by definition (the inversion has been re-inverted).

## Step 7 — Sizing

Run `python scripts/position-sizer-futures.py --instrument <X> --entry <X> --stop <X> --account <ACCOUNT_SIZE> --risk-pct 1.5`.

iFVG stops are typically *wider* than SETUP-1 sweep-wick stops, so contract counts will be smaller. Don't compensate by increasing risk %.

## Step 8 — Target

Minimum 2R. First target = next opposing relevant level OR the opposite end of the FVG range that was originally broken.

## Step 9 — Trade management

- At 1R: trail stop to break-even.
- At 2R: take half off, trail remainder at 1R behind.
- 1m close past stop = exit immediately.

## Step 10 — Log it

`python tools/run.py log`.

## Common failure modes

- **Confusing a wick-through with a break.** A wick is not a break. The candle has to *close* through the FVG.
- **Trading every iFVG retest.** Filter by HTF bias. Only take rejections in the trending direction.
- **Stops too tight (inside the iFVG zone).** The stop is *at the iFVG line*, not inside it. Anywhere inside the zone is too tight.
- **Trading iFVGs during news.** Volatility spikes invalidate the inversion. Wait until volatility compresses.
