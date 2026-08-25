"""Technical-indicator feature engineering (pure pandas/numpy, no `ta` dep).

All features use information available up to and including day t, so pairing them
with forward-looking labels (labels.py) introduces no look-ahead bias.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _rsi(close: pd.Series, n: int = 14) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0.0)
    down = -delta.clip(upper=0.0)
    roll_up = up.ewm(alpha=1 / n, min_periods=n, adjust=False).mean()
    roll_down = down.ewm(alpha=1 / n, min_periods=n, adjust=False).mean()
    rs = roll_up / roll_down.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def _atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    h, l, c = df["high"], df["low"], df["close"]
    prev_c = c.shift(1)
    tr = pd.concat([(h - l), (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, min_periods=n, adjust=False).mean()


FEATURE_COLS = [
    "ret_5", "ret_10", "ret_20",
    "roc_20", "roc_60",
    "px_sma20", "px_sma50", "sma20_sma50",
    "rsi_14", "macd_hist", "bb_pctb", "bb_bw",
    "atr_pct", "vol_ratio", "stoch_k", "stoch_d",
    "dist_52w_high", "dist_52w_low",
]


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Given one symbol's OHLCV (sorted by date) return date+symbol+close+features."""
    df = df.sort_values("date").reset_index(drop=True).copy()
    c, h, l, v = df["close"], df["high"], df["low"], df["volume"]

    df["ret_5"] = c.pct_change(5)
    df["ret_10"] = c.pct_change(10)
    df["ret_20"] = c.pct_change(20)
    df["roc_20"] = c.pct_change(20)
    df["roc_60"] = c.pct_change(60)

    sma20 = c.rolling(20).mean()
    sma50 = c.rolling(50).mean()
    df["px_sma20"] = c / sma20 - 1
    df["px_sma50"] = c / sma50 - 1
    df["sma20_sma50"] = sma20 / sma50 - 1

    df["rsi_14"] = _rsi(c, 14)

    ema12 = c.ewm(span=12, adjust=False).mean()
    ema26 = c.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    macd_sig = macd.ewm(span=9, adjust=False).mean()
    df["macd_hist"] = (macd - macd_sig) / c  # normalized by price

    bb_mid = sma20
    bb_std = c.rolling(20).std()
    upper, lower = bb_mid + 2 * bb_std, bb_mid - 2 * bb_std
    df["bb_pctb"] = (c - lower) / (upper - lower).replace(0, np.nan)
    df["bb_bw"] = (upper - lower) / bb_mid.replace(0, np.nan)

    df["atr_pct"] = _atr(df, 14) / c

    df["vol_ratio"] = v / v.rolling(20).mean()

    ll = l.rolling(14).min()
    hh = h.rolling(14).max()
    stoch_k = 100 * (c - ll) / (hh - ll).replace(0, np.nan)
    df["stoch_k"] = stoch_k
    df["stoch_d"] = stoch_k.rolling(3).mean()

    df["dist_52w_high"] = c / c.rolling(252).max() - 1
    df["dist_52w_low"] = c / c.rolling(252).min() - 1

    keep = ["date", "symbol", "open", "high", "low", "close", "volume"] + FEATURE_COLS
    return df[keep]


if __name__ == "__main__":
    from .data import load_universe

    d = load_universe("2018-01-01", "2026-08-25", universe=["FPT"])
    f = build_features(d["FPT"]).dropna()
    print("feature rows:", len(f), "| cols:", FEATURE_COLS)
    print(f[["date", "close"] + FEATURE_COLS].tail(3).to_string())
