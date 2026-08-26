"""End-to-end swing-opportunity analysis for the VN stock market.

Pipeline: real data (vnstock/VCI) -> technical features -> triple-barrier labels
-> train LogReg / RandomForest / GradientBoosting / XGBoost / LSTM -> out-of-sample
backtest -> current swing signals (entry / take-profit / stop / time-stop).

Writes everything under analysis/results/. All numbers in the report are produced
here from real, out-of-sample computation — nothing is hand-typed.

NOT INVESTMENT ADVICE. Educational / research use only.
"""
from __future__ import annotations

import json
import os
import shutil
import warnings
from datetime import datetime

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from vn_swing.backtest import backtest, classification_metrics  # noqa: E402
from vn_swing.dataset import build_panel, latest_unlabeled, split_train_test  # noqa: E402
from vn_swing.features import FEATURE_COLS  # noqa: E402
from vn_swing.lstm import train_lstm  # noqa: E402
from vn_swing.models import build_models  # noqa: E402
import plot_signals  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")       # latest-snapshot mirror (keeps stable README links)
RUNS = os.path.join(HERE, "runs")         # per-run archive: runs/log_run_<ts>/
os.makedirs(RES, exist_ok=True)
os.makedirs(RUNS, exist_ok=True)


def _make_run_dir():
    ts = datetime.now().strftime("log_run_%Y-%m-%d_%H-%M-%S")
    d = os.path.join(RUNS, ts)
    os.makedirs(os.path.join(d, "charts"), exist_ok=True)
    return d, ts


def _publish_latest(run_dir, ts):
    """Mirror the run into results/ (latest snapshot) and update runs/latest symlink."""
    if os.path.isdir(RES):
        shutil.rmtree(RES)
    shutil.copytree(run_dir, RES)
    link = os.path.join(RUNS, "latest")
    try:
        if os.path.islink(link) or os.path.exists(link):
            os.remove(link)
        os.symlink(ts, link)
    except OSError:
        pass

# ---- config ----
# END = hôm nay (động) để bản tin hằng ngày lấy giá tới phiên gần nhất.
# Đặt biến môi trường VN_END=YYYY-MM-DD để ghim ngày (tái lập kết quả cũ).
START = "2018-01-01"
END = os.environ.get("VN_END") or datetime.now().strftime("%Y-%m-%d")
TEST_START = "2025-01-01"          # out-of-sample period
TP, SL, HORIZON = 0.08, 0.05, 25   # +8% / -5% / 25 trading days (~5 weeks)
COST = 0.003                        # round-trip fees+slippage
TRADE_PCTILE = 80                   # trade only the top 20% most-confident signals
LSTM_L, LSTM_EPOCHS = 20, 12


def fmt_vnd(x_thousand):
    return f"{int(round(x_thousand*1000)):,}"


def main():
    RUN_DIR, RUN_TS = _make_run_dir()
    print("== Run dir:", RUN_DIR, "==")
    print("== 1. Build panel (real data via vnstock/VCI) ==")
    panel = build_panel(START, END, tp=TP, sl=SL, horizon=HORIZON)
    train, test = split_train_test(panel, TEST_START)
    print(f"panel={len(panel)} train={len(train)} test={len(test)} "
          f"| base win-rate train={train['label'].mean():.3f} test={test['label'].mean():.3f}")

    Xtr, ytr = train[FEATURE_COLS].to_numpy(), train["label"].to_numpy().astype(int)
    Xte = test[FEATURE_COLS].to_numpy()
    yte = test["label"].to_numpy().astype(int)

    rows = []
    per_model = {}

    print("\n== 2. Classical models ==")
    models = build_models()
    for name, model in models.items():
        model.fit(Xtr, ytr)
        prob = model.predict_proba(Xte)[:, 1]
        thr = float(np.percentile(prob, TRADE_PCTILE))
        cm = classification_metrics(yte, prob, thr)
        bt = backtest(test, prob, thr, cost=COST)
        s = bt["summary"]
        per_model[name] = {"prob": prob, "thr": thr, "bt": bt, "cm": cm}
        rows.append({
            "model": name, "auc": cm["auc"], "test_acc": cm["acc"],
            "signal_precision": cm["precision_signal"], **s,
        })
        print(f"  {name:13} AUC={cm['auc']}  n_trades={s.get('n_trades',0)}  "
              f"win={s.get('win_rate')}  avg_net={s.get('avg_net_ret')}  "
              f"totalPnL={s.get('total_pnl_fixed')}  maxDD={s.get('max_dd_fixed')}")

    print("\n== 3. LSTM (PyTorch) ==")
    feat_ok = panel.dropna(subset=FEATURE_COLS).copy()
    try:
        lstm_test, lstm_latest = train_lstm(feat_ok, TEST_START, L=LSTM_L, epochs=LSTM_EPOCHS)
        merged = test.merge(lstm_test, on=["symbol", "date"], how="inner")
        prob = merged["prob"].to_numpy()
        thr = float(np.percentile(prob, TRADE_PCTILE))
        cm = classification_metrics(merged["label"].astype(int), prob, thr)
        bt = backtest(merged, prob, thr, cost=COST)
        s = bt["summary"]
        per_model["LSTM"] = {"prob": prob, "thr": thr, "bt": bt, "cm": cm, "latest": lstm_latest}
        rows.append({"model": "LSTM", "auc": cm["auc"], "test_acc": cm["acc"],
                     "signal_precision": cm["precision_signal"], **s})
        print(f"  {'LSTM':13} AUC={cm['auc']}  n_trades={s.get('n_trades',0)}  "
              f"win={s.get('win_rate')}  avg_net={s.get('avg_net_ret')}  totalPnL={s.get('total_pnl_fixed')}")
    except Exception as e:  # noqa: BLE001
        print("  LSTM skipped:", e)
        lstm_latest = None

    metrics = pd.DataFrame(rows).sort_values("avg_net_ret", ascending=False)
    metrics.to_csv(os.path.join(RUN_DIR, "model_metrics.csv"), index=False)

    # buy-and-hold benchmark over the test window (equal-weight universe)
    bh = _buy_hold_benchmark(test)

    # ---- pick best model by out-of-sample expectancy (needs enough trades) ----
    elig = metrics[metrics["n_trades"] >= 20]
    best_name = (elig.iloc[0]["model"] if len(elig) else metrics.iloc[0]["model"])
    print(f"\n== Best out-of-sample model: {best_name} ==")

    # save best model's backtested trades + equity curve
    best_bt = per_model[best_name]["bt"]
    if len(best_bt.get("trades", [])):
        best_bt["trades"].to_csv(os.path.join(RUN_DIR, f"backtest_trades_{best_name}.csv"), index=False)
    _plot_equity(per_model, best_name, bh, RUN_DIR)
    _plot_model_comparison(metrics, RUN_DIR)
    _plot_feature_importance(models, RUN_DIR)

    print("\n== 4. Current swing signals (retrained on ALL labeled data) ==")
    signals = _current_signals(panel, models, lstm_latest)
    signals.to_csv(os.path.join(RUN_DIR, "signals_latest.csv"), index=False)
    print(signals.head(12).to_string(index=False))

    _write_report(metrics, per_model, best_name, bh, signals, train, test, RUN_DIR)

    print("\n== 5. Candlestick charts ==")
    try:
        plot_signals.generate(RUN_DIR)
    except Exception as e:  # noqa: BLE001
        print("  charts skipped:", e)

    _publish_latest(RUN_DIR, RUN_TS)
    print("\nRun dir :", RUN_DIR)
    print("Latest  :", RES, "(mirror)")


def _buy_hold_benchmark(test: pd.DataFrame) -> dict:
    """Equal-weight average of each symbol's return over the test window."""
    rets = []
    for _, sub in test.groupby("symbol"):
        sub = sub.sort_values("date")
        if len(sub) > 1:
            rets.append(sub["close"].iloc[-1] / sub["close"].iloc[0] - 1)
    if not rets:
        return {"avg_symbol_return": float("nan"), "n": 0}
    return {"avg_symbol_return": round(float(np.mean(rets)), 4), "n": len(rets)}


def _current_signals(panel, models, lstm_latest) -> pd.DataFrame:
    """Retrain classical models on ALL labeled rows; score the latest row per symbol."""
    feat_ok = panel.dropna(subset=FEATURE_COLS)
    labeled = feat_ok.dropna(subset=["label"])
    X_all = labeled[FEATURE_COLS].to_numpy()
    y_all = labeled["label"].to_numpy().astype(int)

    latest = latest_unlabeled(panel)
    Xl = latest[FEATURE_COLS].to_numpy()

    prob_cols = {}
    for name, model in models.items():
        model.fit(X_all, y_all)
        prob_cols[name] = model.predict_proba(Xl)[:, 1]
    ens = np.mean([prob_cols[m] for m in prob_cols], axis=0)

    out = latest[["symbol", "sector", "date", "close", "rsi_14", "px_sma50", "vol_ratio"]].copy()
    for name in prob_cols:
        out[f"p_{name}"] = np.round(prob_cols[name], 4)
    if lstm_latest is not None:
        out = out.merge(lstm_latest.rename(columns={"prob": "p_LSTM"})[["symbol", "p_LSTM"]],
                        on="symbol", how="left")
        ens = np.mean([out[c].to_numpy() for c in out.columns if c.startswith("p_")], axis=0)
    out["score"] = np.round(ens, 4)

    out["price_vnd"] = (out["close"] * 1000).round().astype(int)
    out["tp_price_vnd"] = (out["close"] * (1 + TP) * 1000).round().astype(int)
    out["sl_price_vnd"] = (out["close"] * (1 - SL) * 1000).round().astype(int)
    out["time_stop_days"] = HORIZON
    out["trend_up"] = out["px_sma50"] > 0  # price above 50-day average
    out = out.sort_values("score", ascending=False).reset_index(drop=True)
    out["rank"] = out.index + 1
    return out[["rank", "symbol", "sector", "date", "price_vnd", "score",
                *[c for c in out.columns if c.startswith("p_")],
                "tp_price_vnd", "sl_price_vnd", "time_stop_days", "rsi_14", "trend_up", "vol_ratio"]]


def _plot_equity(per_model, best_name, bh, res):
    plt.figure(figsize=(9, 5))
    for name, d in per_model.items():
        eq = d["bt"].get("equity")
        if eq is not None and len(eq):
            plt.plot(np.arange(1, len(eq) + 1), eq, label=f"{name} (n={len(eq)})",
                     lw=2 if name == best_name else 1, alpha=1 if name == best_name else 0.6)
    plt.axhline(1.0, color="k", ls="--", lw=0.8)
    plt.title(f"Out-of-sample cumulative P&L — fixed bet (1 + Σ net returns per trade)\n"
              f"TP+{int(TP*100)}%/SL-{int(SL*100)}%/{HORIZON}d, cost {COST*100:.1f}%RT — "
              f"buy&hold avg {bh['avg_symbol_return']*100:.1f}% (diff. risk basis)")
    plt.xlabel("trade # (chronological)"); plt.ylabel("1 + Σ returns (units of one position)"); plt.legend(fontsize=8)
    plt.tight_layout(); plt.savefig(os.path.join(res, "equity_curve.png"), dpi=110); plt.close()


def _plot_model_comparison(metrics, res):
    m = metrics.sort_values("auc", ascending=True)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))
    ax[0].barh(m["model"], m["auc"], color="#3b82f6"); ax[0].axvline(0.5, color="k", ls="--", lw=0.8)
    ax[0].set_title("ROC-AUC (out-of-sample)"); ax[0].set_xlim(0.4, max(0.6, m["auc"].max() + 0.03))
    m2 = metrics.sort_values("avg_net_ret", ascending=True)
    colors = ["#16a34a" if v > 0 else "#dc2626" for v in m2["avg_net_ret"]]
    ax[1].barh(m2["model"], m2["avg_net_ret"] * 100, color=colors); ax[1].axvline(0, color="k", lw=0.8)
    ax[1].set_title("Avg net return / trade (%)")
    plt.tight_layout(); plt.savefig(os.path.join(res, "model_comparison.png"), dpi=110); plt.close()


def _plot_feature_importance(models, res):
    for name in ("RandomForest", "XGBoost", "GradBoost"):
        m = models.get(name)
        if m is not None and hasattr(m, "feature_importances_"):
            imp = pd.Series(m.feature_importances_, index=FEATURE_COLS).sort_values()
            plt.figure(figsize=(7, 6)); imp.plot(kind="barh", color="#8b5cf6")
            plt.title(f"Feature importance — {name}"); plt.tight_layout()
            plt.savefig(os.path.join(res, "feature_importance.png"), dpi=110); plt.close()
            return


def _write_report(metrics, per_model, best_name, bh, signals, train, test, out_dir):
    top = signals.head(10)
    horizon_cal = int(round(HORIZON * 7 / 5))
    asof = signals["date"].max().date()      # latest available bar -> live signals as-of
    label_asof = test["date"].max().date()   # last date whose triple-barrier label resolved
    md = []
    md.append("# Kết quả phân tích cơ hội swing — TTCK Việt Nam\n")
    md.append("> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** "
              "Đây là kết quả thực nghiệm của một pipeline machine-learning trên dữ liệu quá khứ. "
              "Hiệu suất quá khứ **không** đảm bảo tương lai. Mô hình có thể sai; đừng giao dịch chỉ dựa vào file này.\n")
    md.append(f"*Sinh tự động bởi [`run_analysis.py`](../run_analysis.py) — mọi số liệu là kết quả tính thật, out-of-sample. "
              f"Dữ liệu giá tới {asof} (vnstock/VCI).*\n")

    md.append("## 1. Thiết lập\n")
    md.append(f"- **Vũ trụ cổ phiếu:** {test['symbol'].nunique()} mã thanh khoản (VN30-heavy, nhiều ngành).")
    md.append(f"- **Dữ liệu:** giá ngày {train['date'].min().date()} → {asof} (sau khi bỏ ~1 năm đầu để 'làm nóng' chỉ báo); "
              f"huấn luyện < {TEST_START}, **kiểm định out-of-sample ≥ {TEST_START}**.")
    md.append(f"- **Lưu ý nhãn:** nhãn triple-barrier cần {HORIZON} phiên tương lai để 'chốt', nên backtest OOS chỉ tính "
              f"được tới **{label_asof}**; ~{HORIZON} phiên gần nhất (tới {asof}) được **chấm điểm live** ở mục 3 nhưng "
              f"chưa thể backtest.")
    md.append(f"- **Định nghĩa 'sóng' (triple-barrier):** vào tại giá đóng cửa; **chốt lời +{int(TP*100)}%**, "
              f"**cắt lỗ −{int(SL*100)}%**, **time-stop {HORIZON} phiên (~{horizon_cal} ngày lịch, ~{HORIZON//5} tuần)**. "
              f"Nhãn WIN = chạm chốt lời trước cắt lỗ.")
    md.append(f"- **Chi phí giao dịch:** {COST*100:.1f}%/vòng (phí+thuế+trượt giá). "
              f"**Quy tắc vào lệnh:** chỉ giao dịch **top {100-TRADE_PCTILE}% tín hiệu tự tin nhất** mỗi mô hình.")
    md.append(f"- **Mô hình thử:** Logistic Regression, Random Forest, Gradient Boosting, XGBoost, **LSTM (PyTorch)**.\n")

    md.append("## 2. So sánh mô hình (out-of-sample)\n")
    md.append("| Mô hình | AUC | Win-rate | Avg net/trade | Kỳ vọng (R) | Σ P&L (cược cố định) | Max DD | #lệnh |")
    md.append("|---|---|---|---|---|---|---|---|")
    for _, r in metrics.iterrows():
        md.append(f"| {'**'+r['model']+'**' if r['model']==best_name else r['model']} | {r['auc']} | "
                  f"{r.get('win_rate','—')} | {_pct(r.get('avg_net_ret'))} | {r.get('expectancy_R','—')} | "
                  f"{_pct(r.get('total_pnl_fixed'))} | {_pct(r.get('max_dd_fixed'))} | {int(r.get('n_trades',0))} |")
    base_wr = round(float(test['label'].mean()), 3)
    md.append(f"\n- **Base win-rate** (vào mọi phiên, không lọc) trên tập kiểm định: **{base_wr}** "
              f"(breakeven ≈ {round(SL/(TP+SL),3)} do R:R = {int(TP*100)}:{int(SL*100)}).")
    md.append(f"- **Buy & hold** trung bình các mã trong kỳ kiểm định: **{_pct(bh['avg_symbol_return'])}** "
              f"(tham chiếu, không phải cùng cơ sở rủi ro).")
    md.append(f"- **Mô hình tốt nhất out-of-sample: `{best_name}`** (chọn theo avg net/trade với #lệnh ≥ 20).")
    md.append("- AUC quanh 0.5 nghĩa là sức dự báo yếu — hãy đọc mục *Hạn chế*. Ảnh: "
              "[`equity_curve.png`](equity_curve.png), [`model_comparison.png`](model_comparison.png), "
              "[`feature_importance.png`](feature_importance.png).\n")

    md.append(f"## 3. Tín hiệu swing hiện tại (as-of {asof})\n")
    md.append(f"Điểm `score` = trung bình xác suất WIN của các mô hình (đã retrain trên **toàn bộ** dữ liệu có nhãn). "
              f"Xếp hạng {len(signals)} mã; dưới đây **top 10**. Giá đơn vị VND.\n")
    md.append("| # | Mã | Ngành | Giá | Score | Chốt lời (+8%) | Cắt lỗ (−5%) | RSI | Trend | Vol× |")
    md.append("|---|---|---|---|---|---|---|---|---|---|")
    for _, r in top.iterrows():
        trend = "↑ trên MA50" if r["trend_up"] else "↓ dưới MA50"
        md.append(f"| {r['rank']} | **{r['symbol']}** | {r['sector']} | {r['price_vnd']:,} | "
                  f"{r['score']} | {r['tp_price_vnd']:,} | {r['sl_price_vnd']:,} | "
                  f"{r['rsi_14']:.0f} | {trend} | {r['vol_ratio']:.2f} |")
    end_date = asof
    md.append(f"\n**Cách đọc / kế hoạch giao dịch (rule-based):**")
    md.append(f"- **Thời gian vào hàng:** các mã score cao ở trên, ưu tiên mã *trên MA50* (xu hướng lên) và "
              f"RSI chưa quá nóng (<70). Vào ở phiên kế tiếp, hoặc chờ nhịp chỉnh về vùng MA20 để giá vào tốt hơn.")
    md.append(f"- **Thời gian ra hàng (chốt lời):** thoát khi **chạm +{int(TP*100)}%** (mục tiêu chốt lời), "
              f"hoặc **cắt lỗ tại −{int(SL*100)}%**, hoặc **hết {HORIZON} phiên (~{HORIZON//5} tuần)** thì thoát theo giá thị trường. "
              f"Trong backtest, thời gian giữ trung bình ≈ {per_model[best_name]['bt']['summary'].get('avg_hold_days','?')} phiên.")
    md.append(f"- **Khung 3 tháng:** với time-stop ~{HORIZON//5} tuần, một mã có thể cho **2–3 nhịp sóng** trong 3 tháng tới "
              f"(từ {end_date} đến ~{_add_months(end_date,3)}). Danh sách nên **cập nhật lại hàng tuần** khi có dữ liệu mới.")
    n_down = int((~top["trend_up"]).sum())
    if n_down >= len(top) / 2:
        md.append(f"- **Bối cảnh (quan trọng):** {n_down}/{len(top)} mã trong top đang **dưới MA50** (xu hướng giảm) → "
                  f"phần lớn là kèo **hồi kỹ thuật / bắt đáy** (mean-reversion), rủi ro cao hơn kèo momentum. "
                  f"Ai ngại 'bắt dao rơi' nên ưu tiên mã *trên MA50* hoặc chờ nến xác nhận đảo chiều.")
    md.append(f"- Bảng máy đọc: [`signals_latest.csv`](signals_latest.csv). Backtest chi tiết: "
              f"[`backtest_trades_{best_name}.csv`](backtest_trades_{best_name}.csv), so sánh: [`model_metrics.csv`](model_metrics.csv).\n")

    top6 = list(signals.head(6)["symbol"])
    top1 = top6[0]
    md.append("## 4. Biểu đồ nến (dễ nhìn giao dịch)\n")
    md.append("Tạo/cập nhật bằng `python plot_signals.py` (matplotlib thuần). Mỗi chart gồm: nến OHLC, MA20/MA50, "
              "**▲ điểm MUA**, ranh giới **chốt lời +8% (xanh nét đứt)** / **cắt lỗ −5% (đỏ nét đứt)**, và vạch "
              "**time-stop 25 phiên** — nhìn phát thấy ngay vào ở đâu, chốt/cắt ở đâu.\n")
    md.append("![Tổng quan top 6](charts/overview_top6.png)\n")
    md.append("*Tổng quan top 6 tín hiệu.* Chart từng mã: "
              + ", ".join(f"[`{s}`](charts/{s}_setup.png)" for s in top6) + ".")
    md.append(f"\n**Quy tắc chạy thật trong quá khứ** — {top1}: mỗi ▲ là một điểm mô hình từng ra tín hiệu "
              f"(**xanh = thắng**, chạm +{int(TP*100)}% trước; **đỏ = thua**), theo đúng luật TP/SL/time-stop:")
    md.append(f"![{top1} history](charts/{top1}_history.png)\n")

    md.append("## 5. Hạn chế & cảnh báo (đọc kỹ)\n")
    md.append("- **Sức dự báo có giới hạn:** giá cổ phiếu gần ngẫu nhiên ngắn hạn; AUC thường chỉ nhỉnh hơn 0.5. "
              "Lợi thế (nếu có) đến từ *lọc xác suất* + quản trị rủi ro (R:R, time-stop), không phải 'tiên tri'.")
    md.append("- **Chưa mô phỏng đầy đủ thực tế:** chưa tính biên độ trần/sàn ±7% (HOSE), thanh khoản/khe hở giá, "
              "trượt giá lớn khi bán tháo, T+2 (không bán ngay trong ngày), thuế cổ tức, hay giới hạn margin/call.")
    md.append("- **Rủi ro overfitting & regime change:** tham số TP/SL/horizon do người đặt; thị trường 2025–2026 "
              "(nâng hạng FTSE, KRX, margin kỷ lục) có thể đổi 'chế độ' làm mô hình quá khứ mất hiệu lực.")
    md.append("- **Không xét cơ bản/định giá/tin tức** — thuần kỹ thuật. Hãy kết hợp khung phân tích cơ bản "
              "([`../docs/03`](../docs/03-phuong-phap-phan-tich-co-ban.md)) và bản đồ rủi ro "
              "([`../docs/05`](../docs/05-rui-ro-va-nguon-du-lieu.md)).")
    md.append("- **Đây là công cụ nghiên cứu/giáo dục.** Quyết định đầu tư là của bạn; cân nhắc tư vấn chuyên môn được cấp phép.\n")
    md.append(f"*Chạy lại: `cd analysis && python run_analysis.py`. Tạo lúc dữ liệu {end_date}.*")

    with open(os.path.join(out_dir, "REPORT.md"), "w") as f:
        f.write("\n".join(md) + "\n")

    # small machine-readable summary
    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump({"best_model": best_name, "base_win_rate": base_wr,
                   "buy_hold_avg": bh["avg_symbol_return"],
                   "metrics": metrics.to_dict(orient="records"),
                   "top_signals": top[["symbol", "score", "price_vnd"]].to_dict(orient="records")}, f,
                  ensure_ascii=False, indent=2, default=str)


def _pct(x):
    try:
        return f"{float(x)*100:.2f}%"
    except Exception:
        return "—"


def _add_months(d, n):
    from datetime import date
    m = d.month - 1 + n
    return date(d.year + m // 12, m % 12 + 1, min(d.day, 28))


if __name__ == "__main__":
    main()
