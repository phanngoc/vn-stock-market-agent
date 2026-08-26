"""Render ONE daily morning brief (DAILY_DIGEST.md) from a run.

Reads the structured decision written by Agent E (`debate/decision.json`) plus the
quant signals (`signals_latest.csv`) and model summary (`summary.json`), and renders
a single, consistently-formatted file the user reads each morning:
what to BUY / WATCH / AVOID, entry / take-profit / stop / time-stop, sizing,
invalidation, what to watch this week — with the standing risk disclaimer.

If `decision.json` is missing (debate not run), it falls back to the top quant
signals so the digest is still produced, clearly flagged as "quant only".

Usage: python daily_digest.py [run_dir]        (default: runs/latest)
"""
from __future__ import annotations

import glob
import json
import os
import sys
from datetime import datetime

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")

DEC_ORDER = {"MUA": 0, "THEO DÕI": 1, "THEO DOI": 1, "TRÁNH": 2, "TRANH": 2}
DEC_ICON = {"MUA": "✅ MUA", "THEO DÕI": "👀 THEO DÕI", "TRÁNH": "⛔ TRÁNH"}


def _latest_run() -> str | None:
    link = os.path.join(RUNS, "latest")
    if os.path.islink(link):
        return os.path.realpath(link)
    subs = sorted(glob.glob(os.path.join(RUNS, "log_run_*")))
    return subs[-1] if subs else None


def _vnd(x) -> str:
    try:
        return f"{int(round(float(x))):,}"
    except (TypeError, ValueError):
        return str(x) if x not in (None, "") else "—"


def _load(run_dir: str):
    sig = pd.read_csv(os.path.join(run_dir, "signals_latest.csv"))
    summ, dec = {}, None
    try:
        summ = json.load(open(os.path.join(run_dir, "summary.json")))
    except Exception:
        pass
    dpath = os.path.join(run_dir, "debate", "decision.json")
    if os.path.isfile(dpath):
        try:
            dec = json.load(open(dpath, encoding="utf-8"))
        except Exception:
            dec = None
    return sig, summ, dec


def render(run_dir: str) -> str:
    sig, summ, dec = _load(run_dir)
    asof = str(sig["date"].iloc[0]) if len(sig) else "?"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    best = summ.get("best_model", "?")
    base_wr = summ.get("base_win_rate", "?")
    has_debate = dec is not None

    m = []
    m.append(f"# 📈 Bản tin swing hằng ngày — TTCK Việt Nam\n")
    m.append(f"*Tạo lúc {now} · dữ liệu giá as-of **{asof}** (vnstock/VCI) · "
             f"{'hội đồng 5 tác nhân đã tranh luận' if has_debate else 'CHỈ tín hiệu quant (chưa tranh luận)'}.*\n")
    m.append("> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** "
             "Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, "
             "edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.\n")

    if has_debate:
        stance = dec.get("portfolio_stance", "—")
        note = dec.get("stance_note", "")
        m.append(f"## 🎩 Khẩu vị danh mục hôm nay: **{stance}**")
        if note:
            m.append(f"{note}\n")
        picks = sorted(
            dec.get("picks", []),
            key=lambda p: (DEC_ORDER.get(str(p.get("decision", "")).upper(), 3),
                           str(p.get("confidence", ""))),
        )
        # bucketed one-line tables
        for want in ("MUA", "THEO DÕI", "TRÁNH"):
            bucket = [p for p in picks if str(p.get("decision", "")).upper().replace("DOI", "DÕI")
                      .replace("TRANH", "TRÁNH") == want]
            if not bucket:
                continue
            m.append(f"\n### {DEC_ICON[want]}")
            if want == "TRÁNH":
                m.append("| Mã | Độ tin cậy | Lý do |")
                m.append("|---|---|---|")
                for p in bucket:
                    m.append(f"| **{p.get('symbol','?')}** | {p.get('confidence','—')} | "
                             f"{p.get('thesis','—')} |")
            else:
                m.append("| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |")
                m.append("|---|---|---|---|---|---|---|")
                for p in bucket:
                    m.append(f"| **{p.get('symbol','?')}** | {p.get('confidence','—')} | "
                             f"{p.get('entry_zone_vnd','—')} | {_vnd(p.get('tp_vnd'))} | "
                             f"{_vnd(p.get('sl_vnd'))} | {p.get('time_stop_days','25')} phiên | "
                             f"{p.get('size_pct','—')} |")
        # per-pick detail for actionable ones
        actionable = [p for p in picks if str(p.get("decision", "")).upper() != "TRÁNH"]
        if actionable:
            m.append("\n### 📋 Chi tiết luận điểm & điều kiện huỷ")
            for p in actionable:
                m.append(f"- **{p.get('symbol','?')}** — {p.get('thesis','')}")
                inv = p.get("invalidation")
                if inv:
                    m.append(f"  - *Huỷ luận điểm nếu:* {inv}")
        watch = dec.get("watch_this_week") or []
        if watch:
            m.append("\n### 📅 Cần theo dõi tuần này")
            for w in watch:
                m.append(f"- {w}")
    else:
        top = sig.head(5)
        m.append("## 🔢 Top tín hiệu quant (chưa qua hội đồng tranh luận)\n")
        m.append("| # | Mã | Ngành | Giá | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |")
        m.append("|---|---|---|---|---|---|---|---|---|")
        for _, r in top.iterrows():
            trend = "↑ trên MA50" if r["trend_up"] else "↓ dưới MA50"
            m.append(f"| {int(r['rank'])} | **{r['symbol']}** | {r['sector']} | {_vnd(r['price_vnd'])} | "
                     f"{r['score']:.2f} | {_vnd(r['tp_price_vnd'])} | {_vnd(r['sl_price_vnd'])} | "
                     f"{r['rsi_14']:.0f} | {trend} |")
        m.append("\n*Chạy skill `vn-swing-daily` để có quyết định của hội đồng đầu tư (MUA/THEO DÕI/TRÁNH).*")

    n_down = int((~sig.head(5)["trend_up"]).sum())
    m.append("\n---\n### 🧭 Bối cảnh & cảnh báo")
    m.append(f"- Mô hình tốt nhất OOS: **{best}** · base win-rate **{base_wr}** · "
             f"quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.")
    if n_down >= 3:
        m.append(f"- ⚠️ {n_down}/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, "
                 f"rủi ro cao hơn kèo momentum.")
    m.append("- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.")
    m.append("\n### 🔗 Xem thêm")
    m.append("- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)")
    if has_debate:
        m.append("- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · "
                 "quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)")
    m.append("- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)")
    m.append(f"\n*Nguồn: run `{os.path.basename(run_dir)}`. Chạy lại: skill `vn-swing-daily`.*\n")

    text = "\n".join(m)
    out = os.path.join(run_dir, "DAILY_DIGEST.md")
    open(out, "w", encoding="utf-8").write(text)
    # Lưu theo ngày (analysis/daily/<ngày>/) do archive_daily.py xử lý sau bước này.
    print("wrote", out)
    return out


if __name__ == "__main__":
    rd = sys.argv[1] if len(sys.argv) > 1 else _latest_run()
    if not rd or not os.path.isdir(rd):
        print("No run dir. Run `python run_analysis.py` first.")
        raise SystemExit(1)
    render(rd)
