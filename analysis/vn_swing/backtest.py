"""Event-driven backtest of the swing signal on out-of-sample test rows.

Rule: scan test dates in order. When a model's prob >= threshold for a symbol and
that symbol has no open position, ENTER at that day's close and realize the
triple-barrier outcome (`fwd_ret` over `hold_days`) already computed in labels.py.
Costs (fees+slippage, round-trip) are subtracted from each trade.

Metrics reported are realized, out-of-sample, and directly comparable across models.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def classification_metrics(y_true, prob, thr=0.5) -> dict:
    from sklearn.metrics import accuracy_score, precision_score, roc_auc_score

    pred = (prob >= thr).astype(int)
    out = {"auc": float("nan"), "acc": float("nan"), "precision_signal": float("nan"), "n_signals": int(pred.sum())}
    try:
        out["auc"] = round(roc_auc_score(y_true, prob), 4)
    except Exception:
        pass
    out["acc"] = round(accuracy_score(y_true, pred), 4)
    if pred.sum() > 0:
        out["precision_signal"] = round(precision_score(y_true, pred, zero_division=0), 4)
    return out


def backtest(test_df: pd.DataFrame, prob: np.ndarray, threshold: float, cost=0.003) -> dict:
    """test_df must have date,symbol,close,fwd_ret,hold_days,label aligned to `prob`."""
    d = test_df.copy().reset_index(drop=True)
    d["prob"] = prob
    d = d.sort_values(["date", "symbol"]).reset_index(drop=True)

    open_until: dict[str, pd.Timestamp] = {}
    trades = []
    for _, r in d.iterrows():
        if r["prob"] < threshold:
            continue
        sym, day = r["symbol"], r["date"]
        if sym in open_until and day <= open_until[sym]:
            continue  # already in a position for this symbol
        # approximate exit date by trading-day offset within this symbol's row stream
        exit_day = day + pd.Timedelta(days=int(r["hold_days"]) * 7 / 5 + 1)
        open_until[sym] = exit_day
        net = float(r["fwd_ret"]) - cost
        trades.append({
            "date": day, "symbol": sym, "prob": round(float(r["prob"]), 4),
            "entry": float(r["close"]), "gross_ret": round(float(r["fwd_ret"]), 4),
            "net_ret": round(net, 4), "hold_days": int(r["hold_days"]),
            "win": int(r["label"]), "exit_reason": r.get("exit_reason", ""),
        })

    if not trades:
        return {"n_trades": 0, "summary": {}, "trades": pd.DataFrame()}

    tr = pd.DataFrame(trades)
    rets = tr["net_ret"].to_numpy()
    wins = tr["win"].to_numpy()
    # Fixed-bet cumulative P&L: each signal gets the SAME notional, profits banked
    # (NOT full-capital compounding) -> avoids the reinvestment blow-up artifact and
    # is a fair signal-quality proxy. Equity = 1 + cumulative sum of per-trade returns.
    equity = 1.0 + np.cumsum(rets)
    peak = np.maximum.accumulate(equity)
    max_dd = float((equity - peak).min())  # additive drawdown (units of 1 position)
    avg = float(rets.mean())
    sharpe_per_trade = avg / (rets.std() + 1e-9)
    summary = {
        "n_trades": int(len(tr)),
        "win_rate": round(float(wins.mean()), 4),
        "avg_net_ret": round(avg, 4),
        "median_net_ret": round(float(np.median(rets)), 4),
        "total_pnl_fixed": round(float(rets.sum()), 4),  # Σ net returns, fixed bet
        "sharpe_per_trade": round(float(sharpe_per_trade), 3),
        "max_dd_fixed": round(max_dd, 4),
        "expectancy_R": round(avg / 0.05, 3),  # in units of the 5% initial risk
        "avg_hold_days": round(float(tr["hold_days"].mean()), 1),
    }
    return {"n_trades": len(tr), "summary": summary, "trades": tr, "equity": equity}
