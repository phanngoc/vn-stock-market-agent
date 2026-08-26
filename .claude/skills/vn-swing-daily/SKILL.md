---
name: vn-swing-daily
description: Chạy 1 phát ra 1 bản tin đầu tư swing hằng ngày cho TTCK Việt Nam. Gộp toàn bộ quy trình - pipeline ML (dữ liệu thật vnstock/VCI) + hội đồng 5 tác nhân tranh luận (A kỹ thuật, B news, C bò, D gấu, E giám đốc chiến lược) - thành MỘT lệnh, kết quả duy nhất là DAILY_DIGEST.md (MUA/THEO DÕI/TRÁNH + entry/TP/SL/time-stop). Dùng khi người dùng muốn "chạy 1 phát", "bản tin/khuyến nghị swing hằng ngày", "hôm nay nên vào mã nào".
---

# Skill: vn-swing-daily — Bản tin swing hằng ngày (chạy 1 phát)

Một lệnh → chạy hết → **một file kết quả để tham khảo đầu tư mỗi sáng**:
`DAILY_DIGEST.md` (khẩu vị danh mục + bảng **MUA / THEO DÕI / TRÁNH** với vùng vào, chốt lời +8%, cắt lỗ −5%, time-stop 25 phiên, cỡ vị thế, điều kiện huỷ luận điểm, việc cần theo dõi tuần này).

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Khung mô phỏng (ML + tranh luận đa tác nhân) trên dữ liệu quá khứ; edge mô hình yếu. Quyết định là của người dùng.

Skill này **kết hợp** [`vn-swing-analysis`](../vn-swing-analysis/SKILL.md) (pipeline ML) và [`vn-swing-debate`](../vn-swing-debate/SKILL.md) (hội đồng 5 agent) thành một chuỗi tự động.

## Cách chạy (ưu tiên: workflow)
Gọi Workflow bằng `scriptPath` tuyệt đối (không cần gõ lại kịch bản):
```
Workflow({ scriptPath: "/Users/ngocp/goterm-workspace/vn-stock-market-agent/.claude/workflows/vn-swing-daily.js" })
```
Workflow chạy nền và điều phối 5 giai đoạn (~6 agent, medium): **Pipeline → Evidence(A‖B) → Debate(C→D) → Decision(E) → Digest**. Khi xong, đọc `DAILY_DIGEST.md` ở `run_dir` trả về và trình bày cho người dùng.

## Các giai đoạn workflow làm gì
1. **Pipeline** — `python run_analysis.py` (dữ liệu thật vnstock/VCI → 18 chỉ báo → LogReg/RF/GBM/XGB/LSTM → backtest OOS → tín hiệu + charts) rồi `python debate/scaffold.py runs/latest` dựng whiteboard. Tạo run dir mới `runs/log_run_<ts>/`.
2. **Evidence** — Agent A (kỹ thuật, đọc signals+charts) và Agent B (news, WebSearch tin mới + link) chạy **song song**, mỗi agent ghi `debate/notes/<X>.md`.
3. **Debate** — Agent C (bò) đọc note A+B dựng luận điểm mua; Agent D (gấu) đọc A+B+C và **phản biện trực tiếp C** (tuần tự).
4. **Decision** — Agent E (CIO) đọc toàn bộ, ghi `DECISION.md` (đầy đủ) + `notes/E_cio.md` (tóm tắt) + `decision.json` (máy đọc).
5. **Digest** — `python debate/compile.py <run>` gộp note A→E vào `WHITEBOARD.md`; `python daily_digest.py <run>` render **`DAILY_DIGEST.md`** từ `decision.json` (fallback: top tín hiệu quant nếu thiếu); `python archive_daily.py <run>` copy TOÀN BỘ run vào `analysis/daily/<ngày>/`.

## Kết quả (lưu theo NGÀY — đây là thứ được commit)
```
analysis/daily/<YYYY-MM-DD>/
├── DAILY_DIGEST.md      ← ⭐ FILE ĐỂ ĐỌC MỖI SÁNG (MUA/THEO DÕI/TRÁNH)
├── REPORT.md            ← báo cáo ML đầy đủ
├── signals_latest.csv · model_metrics.csv · summary.json · backtest_trades_*.csv
├── charts/              ← biểu đồ nến (overview + từng mã)
└── debate/
    ├── WHITEBOARD.md     ← toàn bộ tranh luận (A→E, có tên agent)
    ├── DECISION.md       ← quyết định CIO đầy đủ
    ├── decision.json     ← quyết định máy đọc
    └── notes/            ← note riêng từng agent
```
`analysis/daily/LATEST_DIGEST.md` = con trỏ tới bản tin mới nhất. Vùng làm việc `analysis/runs/` bị gitignore.

## Chạy thủ công (không dùng Workflow) — dự phòng
Nếu không gọi Workflow: (1) chạy skill `vn-swing-analysis`; (2) chạy skill `vn-swing-debate` (A‖B → C → D → E) — nhưng cho C/D/E **đọc thẳng `debate/notes/*.md`** thay vì WHITEBOARD (whiteboard chỉ gộp ở cuối); (3) `cd analysis && python debate/compile.py runs/latest && python daily_digest.py runs/latest`.

## Chạy hằng ngày / tự động
- **Thủ công (tương tác)**: gọi lại Workflow như trên — có giao diện `/workflows` theo dõi.
- **Tự động (không tương tác)**: chạy `analysis/scripts/run_daily_ci.sh` — orchestrator path-relative dùng chung cho cả cron và CI. Nó KHÔNG dùng Workflow tool: pipeline (python) → 5 agent qua `claude -p --dangerously-skip-permissions` → compile → `daily_digest.py`. Degrade gracefully (LLM lỗi vẫn ra bản quant-only). Ghi kèm bản lịch sử vào `analysis/daily/<ngày>/` + `analysis/daily/LATEST_DIGEST.md`.
  - **GitHub Actions**: `.github/workflows/daily-swing.yml` (01:30 UTC = 08:30 VN, T2–T6, hoặc chạy tay). Cần secret **`ANTHROPIC_API_KEY`**; tuỳ chọn repo var `CLAUDE_MODEL`. Tự commit `analysis/results` + `analysis/daily` về repo.
  - **Cron cục bộ (macOS)**: `analysis/scripts/cron_daily_swing.sh` (gọi `run_daily_ci.sh`, log ở `analysis/runs/cron_logs/`). Cài: thêm dòng crontab `30 8 * * 1-5 .../cron_daily_swing.sh`.

## Nguyên tắc (áp cho mọi agent)
KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ · không bịa số/tin (B phải có link) · tôn trọng edge yếu → ưu tiên bảo toàn vốn, bò≈gấu thì "THEO DÕI" · nhiều mã dưới MA50 = rủi ro bắt đáy.
