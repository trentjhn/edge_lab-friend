# Level Criteria — What Counts as "Most Relevant"

Not every high or low matters. The framework only considers a level "most relevant" if it's one of these four types:

## 1. Closest 1H High/Low
The most recent untested or most recently respected 1H swing high/low. The closer in time, the more relevant.

## 2. Closest Daily High/Low
The most recent daily candle high or low. Always relevant during cash session — gets respected, swept, or broken with conviction.

## 3. Closest Session High/Low
The high or low of the current trading session (RTH or after-hours). Updates intraday. Especially relevant in the first 90 minutes of NY open.

## 4. News-Event Candle Wicks
Any wick from a high-impact news/data event:
- FOMC announcements (FOMC days)
- CPI / PPI / PCE releases
- NFP / employment data
- Presidential speeches with market relevance
- Major geopolitical headlines

These remain "most relevant" **regardless of how old** they are, until taken out cleanly. A November FOMC wick can still be live in March if no candle has closed past it.

## Ranking Rules

When multiple levels are clustered (within ~5 ticks on ES/NQ):

1. **News-event wicks beat everything else** — they have the longest persistence and the most institutional memory.
2. **Most-recent untested > most-recently-tested > older** — fresh levels have unfilled liquidity behind them.
3. **Higher timeframe beats lower** when in conflict — daily H/L beats 1H H/L beats session H/L.

## What Is NOT Relevant

- Random 5m wicks
- 1m highs/lows
- Indicator-derived levels (MAs, Bollinger Bands, Fib levels)
- Round numbers unless they coincide with one of the four types above

If a level doesn't match one of the four types, **it's not a level for trading purposes**. Don't draw it on your chart.

## Maintenance

- Update `levels/watchlist.md` weekly with current monthly/weekly opens and key levels.
- Active news-event wicks should be tracked in the "Active news-event wicks" section per instrument.
- Once a wick is taken out cleanly (1m close past it), remove it from active levels.
