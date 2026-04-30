# Valid Setup Criteria

Two named setups, one trigger. The trigger is always: price tags a relevant level (closest 1H/daily/session high or low, or a news-event candle wick that's still active). What happens at that level determines which setup you're in.

## SETUP-1: Sweep + FVG Continuation

**What it is:** Price runs the level via a liquidity sweep (takes out stops past the high or low), then prints a fair value gap (FVG) on the way back through. You enter on the FVG retest, in the direction *away* from the swept level (continuation through the level, not back to it).

**Required conditions:**
- [ ] A clearly defined relevant level (per `level-criteria.md`)
- [ ] A sweep through the level — visible on 5m or 1m as a wick or quick spike past the level followed by a reversal candle
- [ ] An FVG forms in the direction of the new move (3-candle imbalance, candle 1 high < candle 3 low for bull FVG, or vice versa)
- [ ] FVG is *near* the sweep (within a few ticks, same vicinity)
- [ ] HTF (4H/1H) bias is aligned with the new direction — see `timeframe-rules.md`
- [ ] Session is in your active hours — see `session-rules.md`

**Entry trigger:** Price retraces to the FVG, prints a rejection candle on 1m, you enter at the FVG midpoint or top edge (on long) / bottom edge (on short).

**Stop:** Tight, just past the sweep wick. Per `risk-management.md` stop rule #1.

**Target:** Minimum 2R. First target is the next opposing relevant level. If no level in range, use measured-move from the sweep depth.

**Regime validity:** Trending RTH, news-driven (carefully). Not valid in chop or low-volume Asian.

**Minimum confluence:** All 6 required conditions above.

---

## SETUP-2: Inverse FVG Rejection

**What it is:** A prior FVG was broken cleanly (price closed through it on whatever timeframe it formed). Once broken, that FVG inverts polarity — a former bullish FVG now acts as bearish resistance, and vice versa. You enter on the *retest* of the inverted FVG, fading away from it.

**Required conditions:**
- [ ] A prior FVG that is now broken (closed through, not just wicked through)
- [ ] Price has returned to retest the broken FVG zone
- [ ] Rejection candle prints on 1m or 5m at the iFVG line (close back into the zone, not through it)
- [ ] HTF (4H/1H) bias is aligned with the rejection direction
- [ ] Session is in your active hours

**Entry trigger:** Rejection candle close at the iFVG. Enter on the next 1m bar at market or limit at the iFVG line.

**Stop:** Exactly at the iFVG line — the level where the original FVG got inverted. Per `risk-management.md` stop rule #2.

**Target:** Minimum 2R. First target is the next opposing relevant level or the opposite end of the FVG range.

**Regime validity:** Trending RTH, chop (this setup actually works in chop better than SETUP-1). Not valid in news-driven volatility unless the iFVG is already established before the news.

**Minimum confluence:** All 5 required conditions above.

---

## What is NOT a setup

- A level test without a sweep → wait
- A sweep without an FVG forming → wait
- An FVG that printed far from the sweep (different price area) → not SETUP-1, possibly something else; don't force the trade
- A retest of an FVG that wasn't broken first → not SETUP-2
- HTF and LTF in conflict → no trade. Period. (See `timeframe-rules.md`.)
- Trading outside your hours → no trade. (See `session-rules.md`.)

If it doesn't match SETUP-1 or SETUP-2 criteria exactly, it's not your setup. Sit out.
