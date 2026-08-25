"""Build a pooled cross-sectional panel: features + triple-barrier labels for all symbols."""
from __future__ import annotations

import pandas as pd

from .data import SECTOR, load_universe
from .features import FEATURE_COLS, build_features
from .labels import triple_barrier


def build_panel(start: str, end: str, tp=0.08, sl=0.05, horizon=25, universe=None) -> pd.DataFrame:
    data = load_universe(start, end, universe=universe)
    frames = []
    for sym, ohlcv in data.items():
        feat = build_features(ohlcv)
        lab = triple_barrier(ohlcv, tp=tp, sl=sl, horizon=horizon)
        merged = feat.merge(
            lab[["date", "label", "fwd_ret", "hold_days", "exit_reason"]], on="date", how="left"
        )
        merged["sector"] = SECTOR.get(sym, "Other")
        frames.append(merged)
    panel = pd.concat(frames, ignore_index=True)
    panel = panel.sort_values(["date", "symbol"]).reset_index(drop=True)
    return panel


def split_train_test(panel: pd.DataFrame, test_start: str):
    """Chronological split. Train rows must have a known label (not right-censored)."""
    feat_ok = panel.dropna(subset=FEATURE_COLS)
    labeled = feat_ok.dropna(subset=["label"])
    train = labeled[labeled["date"] < test_start].copy()
    test = labeled[labeled["date"] >= test_start].copy()
    return train, test


def latest_unlabeled(panel: pd.DataFrame) -> pd.DataFrame:
    """Most recent row per symbol that has complete features (for live scoring)."""
    feat_ok = panel.dropna(subset=FEATURE_COLS)
    idx = feat_ok.groupby("symbol")["date"].idxmax()
    return feat_ok.loc[idx].sort_values("symbol").reset_index(drop=True)


if __name__ == "__main__":
    p = build_panel("2018-01-01", "2026-08-25", universe=["FPT", "HPG", "VCB", "MWG", "SSI"])
    tr, te = split_train_test(p, "2025-01-01")
    print(f"panel={len(p)}  train={len(tr)}  test={len(te)}")
    print("train win rate:", round(tr["label"].mean(), 3), "| test win rate:", round(te["label"].mean(), 3))
    print("latest rows:\n", latest_unlabeled(p)[["date", "symbol", "close"]].to_string())
