---
name: vn-swing-debate
description: Chạy một phiên TRANH LUẬN đa tác nhân (5 agent) để ra quyết định đầu tư swing cho TTCK Việt Nam. Agent A (kỹ thuật) + B (news) đưa bằng chứng; C (bò) + D (gấu) tranh luận; E (giám đốc chiến lược) ra quyết định cuối. Các agent giao tiếp qua whiteboard .md có ghi tên. Dùng sau khi có signals_latest.csv từ skill vn-swing-analysis.
---

# Skill: vn-swing-debate — Hội đồng đầu tư đa tác nhân

Một "hội đồng đầu tư" gồm 5 agent tranh luận qua **whiteboard markdown** (bảng chung, ai cũng đọc được, mỗi ý kiến ghi rõ tên agent) để ra **quyết định swing cuối cùng**. **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**

## Roster (vai trò → template prompt)
| Agent | Vai trò | Prompt |
|---|---|---|
| 🅰️ A | Phân tích **Kỹ thuật** (chart, RSI, MACD, MA, S/R, khối lượng) | [`agents/A_technical.md`](agents/A_technical.md) |
| 🅱️ B | Phân tích **News / Cơ bản** (tin, catalyst, sự kiện — dùng WebSearch) | [`agents/B_news.md`](agents/B_news.md) |
| 🐂 C | Tổng hợp hướng **BÒ** (bull case mạnh nhất) | [`agents/C_bull.md`](agents/C_bull.md) |
| 🐻 D | Tổng hợp hướng **GẤU** (bear case + phản biện C) | [`agents/D_bear.md`](agents/D_bear.md) |
| 🎩 E | **Giám đốc Chiến lược Đầu tư** — quyết định cuối | [`agents/E_cio.md`](agents/E_cio.md) |

## Điều kiện tiên quyết
Cần một run của **vn-swing-analysis** (có `signals_latest.csv`). Nếu chưa có: chạy skill đó trước.

## Quy trình (orchestrator = agent chính điều phối)

1. **Scaffold whiteboard** cho run mới nhất:
   ```bash
   cd analysis && python debate/scaffold.py    # tạo runs/latest/debate/{WHITEBOARD.md, notes/, DECISION.md}
   ```
   Lấy đường dẫn tuyệt đối `DEB=<abs path>/runs/latest/debate`.

2. **PHIÊN 1 — Bằng chứng (song song):** dùng Agent tool chạy **A và B đồng thời** (một message, 2 tool-use).
   - A dùng prompt `agents/A_technical.md`; đọc `signals_latest.csv` + `charts/*_setup.png` của run; ghi ra `$DEB/notes/A_technical.md`.
   - B dùng prompt `agents/B_news.md`; **WebSearch** tin mới (thời điểm hiện tại) cho các mã top + vĩ mô; ghi ra `$DEB/notes/B_news.md`.
   - Orchestrator **gộp** A+B vào `WHITEBOARD.md` mục "PHIÊN 1".

3. **PHIÊN 2 — Bò (C):** chạy Agent C với prompt `agents/C_bull.md`; C **đọc `WHITEBOARD.md`** (đã có A+B); ghi `$DEB/notes/C_bull.md`. Gộp vào "PHIÊN 2".

4. **PHIÊN 3 — Gấu (D):** chạy Agent D với prompt `agents/D_bear.md`; D **đọc `WHITEBOARD.md`** (A+B+C) và **phản biện trực tiếp C**; ghi `$DEB/notes/D_bear.md`. Gộp vào "PHIÊN 3".
   - *(Tuỳ chọn: thêm vòng C phản biện D để tranh luận sâu hơn — lặp bước 3/4.)*

5. **PHIÊN 4 — Quyết định (E):** chạy Agent E với prompt `agents/E_cio.md`; E **đọc toàn bộ `WHITEBOARD.md`**; ghi:
   - `$DEB/DECISION.md` — quyết định đầy đủ theo từng mã: **MUA / THEO DÕI / TRÁNH**, độ tin cậy, entry/TP/SL/time-stop, sizing, điều kiện huỷ luận điểm (invalidation), và stance tổng danh mục.
   - khối tóm tắt vào `WHITEBOARD.md` mục "PHIÊN 4".

## Quy ước whiteboard (bắt buộc)
- Mỗi khối bắt đầu: `### <emoji> Agent X — <vai trò> · <thời gian>` → **luôn ghi tên agent**.
- Trích số liệu/nguồn khi có; nêu rõ độ không chắc chắn; được phép trích tên agent khác để phản biện.
- Ghi vào `notes/<X>.md` để tránh tranh chấp ghi đồng thời; orchestrator gộp lên `WHITEBOARD.md` theo thứ tự.

## Nguyên tắc an toàn (áp cho MỌI agent)
- **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ** — mọi output kèm dòng disclaimer.
- Không bịa số/tin; nếu không chắc, nói "chưa kiểm chứng". Agent B phải trích link nguồn.
- Tôn trọng edge yếu của mô hình (AUC ~0.53–0.55): quyết định phải dựa nhiều vào **quản trị rủi ro**, không phải "chắc thắng".

## Kết quả
`runs/<run>/debate/WHITEBOARD.md` (toàn bộ tranh luận) + `DECISION.md` (quyết định của Giám đốc Chiến lược). Được archive theo ngày vào `analysis/daily/<ngày>/debate/` (bởi `archive_daily.py`) — đây là bản được commit.
