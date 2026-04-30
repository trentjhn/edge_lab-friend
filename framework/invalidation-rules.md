# Invalidation Rules

A trade is invalidated when **the 1m candle closes past your stop**.

## Hard Rules

1. **1m close past stop = out.** Not "the wick doesn't count." Not "give it room." Closed past = out, immediately, at market.
2. **No widening stops.** Ever. If the trade needs a wider stop than your original plan, the original plan was wrong. Take the loss. Re-evaluate.
3. **No averaging down.** No second-entry "to lower my cost basis." If the first entry stopped, that thesis is dead.
4. **No re-entering the same setup until structure shifts.** If you got stopped on a SETUP-1 long, you cannot take another SETUP-1 long at the same level until either:
   - A market structure shift (MSS) confirms a new direction, or
   - A break of structure (BOS) validates the original direction with new evidence (a fresh sweep, a fresh FVG).

## After Invalidation

1. Update `context/portfolio-state.md`:
   - Increment consecutive-losers counter
   - Update session P&L
2. Tell Claude "I got stopped on [setup]" — it will check if any daily gate triggers.
3. Take 5 minutes off the chart. Walk away from the desk.
4. Re-read the setup criteria for whatever you're considering next. Don't enter on muscle memory.

## Common Invalidation Mistakes

- **"It's just a wick."** A wick that closes past your stop counts. The candle close is the close.
- **"The stop was too tight."** Your stop was right at trade time. The market disagreed. The market is right.
- **"I'll wait for the next 1m to confirm."** No. The close already happened. You're rationalizing.

## When Stops Don't Apply

Options on SPY/QQQ. There is no in-trade stop on options the way there is on futures. Your max-loss is the full premium, baked in at entry. If the trade goes against you, you can:

- Sell to close at any time (taking partial loss before full premium loss)
- Let it expire (losing full premium)

Treat options entry size as your invalidation. If max premium loss > $300, the position was sized wrong.
