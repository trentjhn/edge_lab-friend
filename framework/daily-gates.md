# Daily Gates — Hard Stops

You have two daily gates. They are non-negotiable. Claude enforces them.

## Rules

**Gate 1 — Dollar floor:** down $500 on the session → done.
**Gate 2 — Consecutive losers:** 3 in a row → done.

**Whichever hits first stops trading for the day.**

## Why these exist

3-consecutive-losers catches *tilt*. Tilt almost always shows up as "I just took 3 dumb trades to make it back." If you stop after the 3rd, you don't take the 4th-7th dumb trades that turn a bad day into a wreck.

The $500 floor catches the *one big bad trade* — the rare day where a single trade goes 2R+ against you immediately and you don't even get to the 3-in-a-row gate. $500 is roughly 2R at full size. Step away.

## Claude enforcement protocol

Claude tracks session P&L and consecutive losers from `context/portfolio-state.md`. After every closed trade, the file gets updated.

Threshold responses:

- **Down $300 (warning):** "$300 down — 2 more losers or $200 more loss = done. Stay disciplined."
- **Down $500 OR 3rd consecutive loser:** "Daily gate hit. Stop trading. Close the terminal."

If you push back ("just one more"), Claude repeats the message verbatim. No discussion.

## What "stop trading" means

- No new entries
- Manage open positions only (let stops/targets play out, don't re-enter on closes)
- Close Claude when flat
- Do not open another session today

## Resetting

The gate resets at next session start. Claude reads `context/portfolio-state.md` — if the timestamp is from a prior day, P&L and consecutive-losers reset to 0.

## What this gate is NOT

It is not a profit target. There is no upper gate. If you're up money and your setups are good, keep trading until the session window closes (per `session-rules.md`).
