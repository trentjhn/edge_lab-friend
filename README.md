# edge_lab — Personal Day Trading Analyst

A folder of Markdown files that describe how you trade. Claude reads them and stress-tests every trade against your own rules.

## What's where

- `CLAUDE.md` — Claude's instructions. Loaded automatically every session.
- `framework/` — Your trading rules. Setup criteria, risk, daily gates, timeframes.
- `playbook/` — Step-by-step execution for each named setup.
- `levels/` — Price reference points (macro opens, watchlist).
- `context/` — Live state (macro outlook, pending setups, market snapshot, portfolio).
- `journal/` — Trade entries + auto-generated index.
- `scripts/` — Python automation (data fetch, position sizing, journal logging).
- `tools/run.py` — Cross-platform command runner.

## Daily commands

| What | Command |
|---|---|
| Open Claude in this folder | `claude` |
| Refresh market data | `python tools/run.py refresh` |
| Log a trade | `python tools/run.py log` |
| Check watchlist alerts | `python tools/run.py check` |
| Weekly review | `python tools/run.py weekly --week YYYY-MM-DD` |
| End session | Type "good night" to Claude |

## First-time setup

```
pip install -r requirements.txt
cp .env.example .env       # then edit .env with your account size (Windows: copy .env.example .env)
python tools/run.py refresh
claude
```

## First Claude session — paste this exact prompt

When Claude opens, copy-paste this entire block as your first message:

```text
I just cloned and installed edge_lab. You are my personal day-trading analyst.

1. Read CLAUDE.md fully — it's your instructions.
2. Read every file in framework/ to learn my rules (2 named ICT setups, daily gates, session hours, level criteria, risk math).
3. Read both files in playbook/ — those are the step-by-step execution guides for SETUP-1 (Sweep + FVG continuation) and SETUP-2 (Inverse FVG rejection).
4. Read context/market-snapshot.md to see what tools/run.py refresh just pulled.

Then run this exact sequence:

A. Print a 3-line summary of what you understood about my framework.
B. Ask me 3 confirmation questions:
   - SETUP-1 = sweep + FVG continuation, stop tight past sweep wick — yes?
   - Daily gate = down $500 OR 3 consecutive losers, whichever first — yes?
   - Hours = 6:30-10 AM PT primary, 3pm/5pm PT occasional — yes?
C. After I confirm all three, ask me my current bias on ES, NQ, gold/silver, SPY/QQQ — one sentence each. Write the answers to context/macro-outlook.md and update the timestamp.
D. Then prompt me to fill levels/macro-levels.md and levels/watchlist.md by asking which instruments I want to start tracking actively.
E. Once levels are populated, mark the system live: "edge_lab is live. Try saying 'I'm watching ES at [level] for a sweep+FVG continuation' to add a watchlist entry."

Output style: concise, direct, no walls of text, brief insights only when useful, one question at a time. Match this style every response.
```

That's it. Claude takes over from there.
