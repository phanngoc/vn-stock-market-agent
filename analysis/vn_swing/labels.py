"""Triple-barrier labeling for swing trades (López de Prado style).

Entry at close[t]. Looking forward up to H trading days:
  - WIN  (label=1): the high touches the take-profit barrier (+TP) BEFORE the
    low touches the stop-loss barrier (-SL).
  - LOSS (label=0): stop-loss touched first, OR time runs out below TP.
When a single daily bar spans both barriers we assume the stop is hit first
(conservative / worst-case).

This makes the ML target and the trade rule identical: "enter now; take profit at
+TP; cut at -SL; force-exit after H days". The realized return `fwd_ret` is what a
mechanical trader would actually have booked under that rule.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def triple_barrier(df: pd.DataFrame, tp: float = 0.08, sl: float = 0.05, horizon: int = 25) -> pd.DataFrame:
    """Add label / fwd_ret / hold_days / exit_reason columns. df has open/high/low/close sorted by date."""
    df = df.sort_values("date").reset_index(drop=True).copy()
    close = df["close"].to_numpy(float)
    high = df["high"].to_numpy(float)
    low = df["low"].to_numpy(float)
    n = len(df)

    label = np.full(n, np.nan)
    fwd_ret = np.full(n, np.nan)
    hold = np.full(n, np.nan)
    reason = np.array([""] * n, dtype=object)

    for t in range(n):
        end = t + horizon
        if end >= n:  # right-censored: not enough future bars
            continue
        entry = close[t]
        tp_px = entry * (1 + tp)
        sl_px = entry * (1 - sl)
        outcome = None
        for k in range(t + 1, end + 1):
            hit_sl = low[k] <= sl_px
            hit_tp = high[k] >= tp_px
            if hit_sl and hit_tp:  # worst-case: stop first
                outcome = (0, -sl, k - t, "sl(same-bar)")
                break
            if hit_sl:
                outcome = (0, -sl, k - t, "sl")
                break
            if hit_tp:
                outcome = (1, tp, k - t, "tp")
                break
        if outcome is None:  # timed out
            realized = close[end] / entry - 1
            outcome = (1 if realized >= tp else 0, realized, horizon, "time")
        label[t], fwd_ret[t], hold[t], reason[t] = outcome

    df["label"] = label
    df["fwd_ret"] = fwd_ret
    df["hold_days"] = hold
    df["exit_reason"] = reason
    return df


if __name__ == "__main__":
    from .data import load_universe

    d = load_universe("2018-01-01", "2026-08-25", universe=["FPT"])
    lab = triple_barrier(d["FPT"]).dropna(subset=["label"])
    print("labeled rows:", len(lab))
    print("win rate (base):", round(lab["label"].mean(), 3))
    print(lab["exit_reason"].value_counts().to_string())
    print("avg realized ret per trade (base rule):", round(lab["fwd_ret"].mean(), 4))
