"""Candlestick charts for the current swing signals — with BUY marker + take-profit
/ stop-loss boundaries + time-stop zone, so a trade is readable at a glance.

Reads <run_dir>/signals_latest.csv and the cached prices; writes into <run_dir>/charts/.
Candlesticks drawn by hand (matplotlib only — no mplfinance needed).

NOT INVESTMENT ADVICE. Educational / research use only.
"""
from __future__ import annotations

import glob
import os
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

from vn_swing.data import load_universe  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")

TP, SL, HORIZON = 0.08, 0.05, 25
LOOKBACK = 130
UP, DOWN = "#16a34a", "#dc2626"
MA20C, MA50C = "#f59e0b", "#3b82f6"


def _candles(ax, df, x0=0):
    for i, (_, r) in enumerate(df.iterrows()):
        x = x0 + i
        up = r["close"] >= r["open"]
        color = UP if up else DOWN
        ax.vlines(x, r["low"], r["high"], color=color, linewidth=0.8, zorder=2)
        lo, hi = (r["open"], r["close"]) if up else (r["close"], r["open"])
        h = max(hi - lo, (df["high"].max() - df["low"].min()) * 0.0008)
        ax.add_patch(Rectangle((x - 0.3, lo), 0.6, h, facecolor=color,
                               edgecolor=color, linewidth=0.5, zorder=3))


def _date_ticks(ax, dates, n_total, step=21):
    idx = list(range(0, len(dates), step))
    ax.set_xticks(idx)
    ax.set_xticklabels([dates[i].strftime("%m/%y") for i in idx], fontsize=8)
    ax.set_xlim(-1, n_total + 1)


def plot_setup(ax, sym, ohlcv, sig_row):
    df = ohlcv.sort_values("date").tail(LOOKBACK).reset_index(drop=True).copy()
    for c in ("open", "high", "low", "close"):
        df[c] = df[c] * 1000
    ma20 = df["close"].rolling(20).mean()
    ma50 = df["close"].rolling(50).mean()
    n = len(df)
    entry_i = n - 1
    entry = float(sig_row["price_vnd"]); tp = float(sig_row["tp_price_vnd"]); sl = float(sig_row["sl_price_vnd"])

    _candles(ax, df)
    ax.plot(range(n), ma20, color=MA20C, lw=1.1, label="MA20", zorder=1)
    ax.plot(range(n), ma50, color=MA50C, lw=1.1, label="MA50", zorder=1)

    xend = entry_i + HORIZON
    ax.axvspan(entry_i, xend, color="#94a3b8", alpha=0.10, zorder=0)
    ax.hlines(tp, entry_i, xend, color=UP, lw=1.6, ls="--", zorder=4)
    ax.hlines(sl, entry_i, xend, color=DOWN, lw=1.6, ls="--", zorder=4)
    ax.hlines(entry, entry_i, xend, color="#111827", lw=0.9, ls=":", zorder=4)
    ax.axvline(xend, color="#6b7280", lw=1.0, ls="-.", zorder=4)

    ax.scatter([entry_i], [df["low"].iloc[-1] * 0.99], marker="^", s=140, color="#111827", zorder=6)
    ax.annotate("MUA", (entry_i, df["low"].iloc[-1] * 0.985), ha="center", va="top", fontsize=8, fontweight="bold")

    ax.text(xend + 0.5, tp, f"  Chốt lời +{int(TP*100)}%\n  {tp:,.0f}", color=UP, fontsize=8, va="center", fontweight="bold")
    ax.text(xend + 0.5, sl, f"  Cắt lỗ −{int(SL*100)}%\n  {sl:,.0f}", color=DOWN, fontsize=8, va="center", fontweight="bold")
    ax.text(xend + 0.5, entry, f"  Entry {entry:,.0f}", color="#111827", fontsize=7.5, va="center")
    ax.text(xend, df["high"].max(), f"time-stop\n{HORIZON} phiên", color="#6b7280", fontsize=7, ha="center", va="bottom")

    trend = "↑ trên MA50" if sig_row["trend_up"] else "↓ dưới MA50"
    ax.set_title(f"{sym}  ·  score {sig_row['score']:.2f}  ·  RSI {sig_row['rsi_14']:.0f}  ·  {trend}", fontsize=10, fontweight="bold")
    _date_ticks(ax, list(df["date"]), xend + 8)
    ax.grid(alpha=0.15); ax.legend(loc="upper left", fontsize=7); ax.set_ylabel("VND")


def plot_history(sym, ohlcv, trades_csv, charts_dir):
    if not os.path.exists(trades_csv):
        return None
    tr = pd.read_csv(trades_csv, parse_dates=["date"])
    tr = tr[tr["symbol"] == sym]
    if tr.empty:
        return None
    df = ohlcv.sort_values("date").reset_index(drop=True).copy()
    df = df[df["date"] >= tr["date"].min() - pd.Timedelta(days=20)].reset_index(drop=True)
    for c in ("open", "high", "low", "close"):
        df[c] = df[c] * 1000
    dmap = {d: i for i, d in enumerate(df["date"])}
    fig, ax = plt.subplots(figsize=(12, 5))
    _candles(ax, df)
    ax.plot(range(len(df)), df["close"].rolling(20).mean(), color=MA20C, lw=1, label="MA20")
    for _, t in tr.iterrows():
        if t["date"] in dmap:
            x = dmap[t["date"]]; c = UP if t["win"] == 1 else DOWN
            ax.scatter([x], [df.loc[x, "low"] * 0.985], marker="^", s=70, color=c, zorder=6)
    n_win = int((tr["win"] == 1).sum())
    ax.set_title(f"{sym} — {len(tr)} tín hiệu backtest (▲ xanh=thắng {n_win}, đỏ=thua {len(tr)-n_win}) "
                 f"| net TB {tr['net_ret'].mean()*100:.2f}%/lệnh", fontsize=10, fontweight="bold")
    _date_ticks(ax, list(df["date"]), len(df), step=42)
    ax.grid(alpha=0.15); ax.legend(fontsize=8); ax.set_ylabel("VND")
    out = os.path.join(charts_dir, f"{sym}_history.png")
    plt.tight_layout(); plt.savefig(out, dpi=120); plt.close()
    return out


def generate(run_dir: str, top_n: int = 6, asof: str = "2026-08-25"):
    """Render candlestick charts into <run_dir>/charts from <run_dir>/signals_latest.csv."""
    charts = os.path.join(run_dir, "charts")
    os.makedirs(charts, exist_ok=True)
    sig = pd.read_csv(os.path.join(run_dir, "signals_latest.csv"))
    top = sig.head(top_n)
    syms = list(top["symbol"])
    data = load_universe("2018-01-01", asof, universe=syms, use_cache=True)

    for _, row in top.iterrows():
        if row["symbol"] not in data:
            continue
        fig, ax = plt.subplots(figsize=(11, 5.5))
        plot_setup(ax, row["symbol"], data[row["symbol"]], row)
        plt.tight_layout(); plt.savefig(os.path.join(charts, f"{row['symbol']}_setup.png"), dpi=120); plt.close()

    fig, axes = plt.subplots(2, 3, figsize=(20, 11))
    for ax, (_, row) in zip(axes.ravel(), top.iterrows()):
        if row["symbol"] in data:
            plot_setup(ax, row["symbol"], data[row["symbol"]], row)
    fig.suptitle(f"Tín hiệu swing TTCK Việt Nam — as-of {asof}  ·  MUA + chốt lời (+8%) / cắt lỗ (−5%) / time-stop 25 phiên\n"
                 "KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — nến & ranh giới để dễ hình dung giao dịch", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96]); plt.savefig(os.path.join(charts, "overview_top6.png"), dpi=110); plt.close()

    top1 = syms[0]
    for cand in (os.path.join(run_dir, "backtest_trades_LSTM.csv"),
                 *glob.glob(os.path.join(run_dir, "backtest_trades_*.csv"))):
        if os.path.exists(cand):
            plot_history(top1, data.get(top1, pd.DataFrame()), cand, charts)
            break
    print(f"  charts -> {charts}")


def _latest_run():
    link = os.path.join(RUNS, "latest")
    if os.path.islink(link):
        return os.path.join(RUNS, os.readlink(link))
    subs = sorted(glob.glob(os.path.join(RUNS, "log_run_*")))
    return subs[-1] if subs else None


if __name__ == "__main__":
    import sys

    rd = sys.argv[1] if len(sys.argv) > 1 else _latest_run()
    if not rd or not os.path.isdir(rd):
        print("No run dir found. Run `python run_analysis.py` first."); raise SystemExit(1)
    generate(rd)
