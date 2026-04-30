"""Pull recent OHLCV via yfinance and write a snapshot to context/market-snapshot.md."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import pandas as pd
import yfinance as yf

TICKERS = {
    "ES=F": "ES (S&P futures)",
    "NQ=F": "NQ (Nasdaq futures)",
    "GC=F": "GC (Gold)",
    "SI=F": "SI (Silver)",
    "SPY": "SPY",
    "QQQ": "QQQ",
}

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_PATH = ROOT / "context" / "market-snapshot.md"


def ema(series: pd.Series, period: int) -> float:
    return series.ewm(span=period, adjust=False).mean().iloc[-1]


def rsi(series: pd.Series, period: int = 14) -> float:
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs)).iloc[-1] if loss.iloc[-1] != 0 else 100.0


def atr(df: pd.DataFrame, period: int = 14) -> float:
    high_low = df["High"] - df["Low"]
    high_close = (df["High"] - df["Close"].shift()).abs()
    low_close = (df["Low"] - df["Close"].shift()).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return tr.rolling(period).mean().iloc[-1]


def regime_tag(close: float, ema9: float, ema21: float, ema50: float, atr_now: float, atr_avg: float) -> str:
    if atr_now > 1.5 * atr_avg:
        return "volatile"
    if ema9 > ema21 > ema50 and close > ema9:
        return "trending_up"
    if ema9 < ema21 < ema50 and close < ema9:
        return "trending_down"
    return "ranging"


def fetch_one(ticker: str) -> dict | None:
    try:
        df = yf.Ticker(ticker).history(period="60d", interval="1d")
        if df.empty or len(df) < 50:
            return None
        close = df["Close"].iloc[-1]
        ema9 = ema(df["Close"], 9)
        ema21 = ema(df["Close"], 21)
        ema50 = ema(df["Close"], 50)
        rsi14 = rsi(df["Close"])
        atr14 = atr(df)
        atr_avg = atr(df.iloc[:-1]) if len(df) > 30 else atr14
        regime = regime_tag(close, ema9, ema21, ema50, atr14, atr_avg)
        return {
            "ticker": ticker,
            "close": close,
            "ema9": ema9,
            "ema21": ema21,
            "ema50": ema50,
            "rsi14": rsi14,
            "atr14": atr14,
            "regime": regime,
        }
    except Exception as exc:
        return {"ticker": ticker, "error": str(exc)}


def render(rows: list[dict]) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z").strip()
    lines = [
        "# Market Snapshot",
        "",
        f"**Generated:** {now}",
        "",
        "| Ticker | Close | EMA9 | EMA21 | EMA50 | RSI14 | ATR14 | Regime |",
        "|--------|------:|-----:|------:|------:|------:|------:|--------|",
    ]
    for row in rows:
        if "error" in row:
            lines.append(f"| {row['ticker']} | ERROR: {row['error']} | | | | | | |")
            continue
        lines.append(
            f"| {row['ticker']} | {row['close']:.2f} | {row['ema9']:.2f} | {row['ema21']:.2f} "
            f"| {row['ema50']:.2f} | {row['rsi14']:.1f} | {row['atr14']:.2f} | {row['regime']} |"
        )
    lines.append("")
    lines.append("Run `python tools/run.py refresh` to regenerate.")
    return "\n".join(lines)


def main() -> None:
    rows = [fetch_one(t) for t in TICKERS]
    rows = [r for r in rows if r is not None]
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(render(rows), encoding="utf-8")
    print(f"Wrote {SNAPSHOT_PATH} — {len(rows)} tickers.")


if __name__ == "__main__":
    main()
