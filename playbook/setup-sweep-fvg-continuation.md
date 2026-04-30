# Playbook — SETUP-1: Sweep + FVG Continuation

Step-by-step execution. Follow exactly. If a step fails the criteria, abort the trade.

## Step 1 — Identify the level (HTF)

On 1H or 4H, find the closest relevant high/low (per `framework/level-criteria.md`).

**Pass criteria:** A specific level you can name + price (e.g., "ES 5505, closest 1H high, untested").
**Fail:** Multiple ambiguous levels in a cluster, or no clean level near current price → wait.

## Step 2 — Watch for the sweep (5m or 1m)

Wait for price to spike past the level (taking out resting stops) and immediately reverse.

**Pass criteria:** A wick or sharp candle that pierces the level and closes back through. Volume should be elevated on the sweep candle.
**Fail:** Price grinds through the level without a sweep wick, or sweeps and continues in the original direction → not your setup.

## Step 3 — Wait for the FVG to print

After the sweep reverses, watch for a 3-candle imbalance (FVG) on 5m. Bull FVG: candle 1 high < candle 3 low. Bear FVG: candle 1 low > candle 3 high.

**Pass criteria:** FVG forms within 1-3 candles of the sweep, in the direction of the new move.
**Fail:** No FVG forms, or the FVG is far from the sweep (different price area) → no setup.

## Step 4 — Drop to 1m for execution

Watch the 1m as price retraces toward the FVG.

**Pass criteria:** Price approaches the FVG zone. You're ready to enter.
**Fail:** Price doesn't pull back to the FVG (continuation without retracement) → missed entry, don't chase.

## Step 5 — Entry trigger

When price reaches the FVG, watch for a rejection candle on 1m.

- **Long:** 1m candle wicks into the FVG and closes back above the FVG top (or midpoint, if you're more aggressive).
- **Short:** 1m candle wicks into the FVG and closes back below the FVG bottom (or midpoint).

Enter at market on the close of the rejection candle, OR set a limit at the FVG midpoint.

## Step 6 — Stop placement

**Stop Rule 1 (per `risk-management.md`):** Tight, just past the sweep wick. 1-2 ticks of buffer beyond the sweep high (for shorts) or sweep low (for longs).

## Step 7 — Sizing

Run `python scripts/position-sizer-futures.py --instrument <ES|NQ|GC|SI> --entry <X> --stop <X> --account <ACCOUNT_SIZE> --risk-pct 1.5`.

If contracts == 0, your stop is too wide. Skip or tighten.

## Step 8 — Target

Minimum 2R. First target = next opposing relevant level.

## Step 9 — Trade management

- At 1R: trail stop to break-even.
- At 2R: take half off, trail remainder at 1R behind.
- 1m close past stop = exit immediately.

## Step 10 — Log it

After the trade closes (win or loss): `python tools/run.py log`.

## Common failure modes

- **Entering before the FVG fully prints.** Wait for the third candle to close.
- **Entering on the sweep itself instead of waiting for the retest.** That's a different (and worse) setup.
- **Stops too wide because "I want to give it room."** Tight stop is the entire edge of this setup.
- **Trading SETUP-1 in chop regime.** Continuation rarely materializes. Use SETUP-2 in chop.
