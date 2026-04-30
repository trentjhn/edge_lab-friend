# Regime Definitions — Intraday

Four regimes. Setup validity differs per regime.

## Trending RTH

**What it looks like:** Clean directional move with EMA9/21/50 stack aligned (9 > 21 > 50 in uptrend, inverted in downtrend). HH/HL pattern intact on 5m and 15m. ATR is normal-to-elevated but not blowing out.

**Setups valid:** SETUP-1 (sweep + FVG continuation) is the bread-and-butter here. SETUP-2 (iFVG rejection) also works as a fade against the trend at major levels.

**How to identify on the snapshot:** `python tools/run.py refresh` outputs a regime tag per ticker. Trending RTH = `trending_up` or `trending_down`.

## Chop

**What it looks like:** EMAs flat or oscillating. Price drifts between two horizontal levels. ATR low. No clean HH or LL — instead price equal-highs and equal-lows.

**Setups valid:** SETUP-2 (iFVG rejection) — iFVGs form frequently in chop and play very cleanly. SETUP-1 mostly fails in chop because the "continuation" never materializes.

**Snapshot tag:** `ranging`.

## News-Driven

**What it looks like:** Sudden volatility expansion around a scheduled (FOMC, CPI, NFP) or unscheduled (geopolitical headline, Fed speak, presidential statement) event. ATR spikes. Levels get violated cleanly or get absorbed dramatically.

**Setups valid:** SETUP-1 *after* the volatility compresses (post-event sweep + FVG off the news wick). Avoid trading the spike itself. SETUP-2 only if the iFVG was established *before* the news.

**Snapshot tag:** `volatile` (when ATR > 1.5x recent average).

## Low-Volume Asian

**What it looks like:** Thin liquidity. Price slow-grinds with occasional sharp wicks that don't follow through. Common on GC/SI overnight.

**Setups valid:** SETUP-2 with caution — iFVG retests can play but get faked frequently. SETUP-1 is unreliable here; the sweep often fails to follow through.

**Snapshot tag:** `low_volume` (volume < 0.7x recent average).

## Regime Conflict

If 1H regime is trending but 5m regime is chop → wait. Either let the 5m sort itself out into a new trend, or let the 1H regime shift into chop. Don't force a setup across regime conflicts.
