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
cp .env.example .env       # then edit .env with your account size
python tools/run.py refresh
claude
```

In your first Claude session, it'll ask you to confirm setups + capture your current bias for ES, NQ, gold/silver, SPY/QQQ.
