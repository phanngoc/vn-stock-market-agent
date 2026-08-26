"""Scaffold a multi-agent DEBATE whiteboard for a given run.

Creates <run_dir>/debate/WHITEBOARD.md (the shared board every agent writes on),
an empty notes/ dir (each agent's individual sticky note), and DECISION.md.

The 5 agents (see .claude/skills/vn-swing-debate):
  🅰️ Agent A — Phân tích Kỹ thuật
  🅱️ Agent B — Phân tích News / Cơ bản
  🐂 Agent C — Tổng hợp hướng BÒ (bull)
  🐻 Agent D — Tổng hợp hướng GẤU (bear)
  🎩 Agent E — Giám đốc Chiến lược Đầu tư (quyết định cuối)

Usage: python debate/scaffold.py [run_dir]   (default: runs/latest)
"""
from __future__ import annotations

import glob
import json
import os
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "..", "runs")


def _latest_run():
    link = os.path.join(RUNS, "latest")
    if os.path.islink(link):
        return os.path.realpath(link)
    subs = sorted(glob.glob(os.path.join(RUNS, "log_run_*")))
    return subs[-1] if subs else None


def scaffold(run_dir: str, top_n: int = 5) -> str:
    import pandas as pd

    deb = os.path.join(run_dir, "debate")
    os.makedirs(os.path.join(deb, "notes"), exist_ok=True)
    sig = pd.read_csv(os.path.join(run_dir, "signals_latest.csv")).head(top_n)
    try:
        summ = json.load(open(os.path.join(run_dir, "summary.json")))
    except Exception:
        summ = {}
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    asof = str(sig["date"].iloc[0]) if len(sig) else "?"

    rows = ["| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |",
            "|---|---|---|---|---|---|---|---|---|"]
    for _, r in sig.iterrows():
        trend = "↑ trên MA50" if r["trend_up"] else "↓ dưới MA50"
        rows.append(f"| {int(r['rank'])} | **{r['symbol']}** | {r['sector']} | {int(r['price_vnd']):,} | "
                    f"{r['score']:.2f} | {int(r['tp_price_vnd']):,} | {int(r['sl_price_vnd']):,} | "
                    f"{r['rsi_14']:.0f} | {trend} |")
    table = "\n".join(rows)
    tickers = ", ".join(sig["symbol"])

    wb = f"""# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of {asof})

*Board tạo lúc {ts}. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **{summ.get('best_model','?')}** · base win-rate **{summ.get('base_win_rate','?')}** · buy&hold kỳ kiểm định **{summ.get('buy_hold_avg','?')}**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top {top_n} theo score): {tickers}
{table}

## 👥 Roster & thứ tự
1. 🅰️ **Agent A — Kỹ thuật** và 🅱️ **Agent B — News/Cơ bản** viết bằng chứng độc lập (song song).
2. 🐂 **Agent C — BÒ** đọc A+B, dựng luận điểm mua mạnh nhất.
3. 🐻 **Agent D — GẤU** đọc A+B+C, dựng luận điểm bán/tránh và **phản biện trực tiếp C**.
4. 🎩 **Agent E — Giám đốc Chiến lược** đọc toàn bộ, ra **quyết định cuối** (xem `DECISION.md`).

## ✍️ Quy ước viết
- Mỗi ý kiến bắt đầu bằng tiêu đề: `### <emoji> Agent X — <vai trò> · <thời gian>`.
- Trích nguồn/số liệu khi có (RSI, giá, tin + link). Nói thẳng độ không chắc chắn.
- Được phép trích tên agent khác để phản biện: "Agent C cho rằng… nhưng…".

---

# 🗣️ PHIÊN 1 — BẰNG CHỨNG (Agent A & B)

*(A và B điền khối của mình vào đây / hoặc ghi ở `notes/` rồi orchestrator gộp lên.)*

---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*
"""
    open(os.path.join(deb, "WHITEBOARD.md"), "w").write(wb)
    open(os.path.join(deb, "DECISION.md"), "w").write(
        f"# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of {asof}\n\n*Chờ Agent E (Giám đốc Chiến lược) điền.*\n"
        "\n> ⚠️ KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.\n")
    print("scaffolded debate ->", deb)
    return deb


if __name__ == "__main__":
    rd = sys.argv[1] if len(sys.argv) > 1 else _latest_run()
    if not rd or not os.path.isdir(rd):
        print("No run dir. Run `python run_analysis.py` first."); raise SystemExit(1)
    scaffold(rd)
