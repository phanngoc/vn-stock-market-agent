# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-08-26)

*Board tạo lúc 2026-08-26 05:27:36. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.352** · buy&hold kỳ kiểm định **0.302**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): KDH, PNJ, PDR, VIC, VRE
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **KDH** | RealEstate | 18,200 | 0.59 | 19,656 | 17,290 | 49 | ↓ dưới MA50 |
| 2 | **PNJ** | Retail/Consumer | 42,500 | 0.58 | 45,900 | 40,375 | 59 | ↓ dưới MA50 |
| 3 | **PDR** | RealEstate | 12,550 | 0.57 | 13,554 | 11,922 | 52 | ↓ dưới MA50 |
| 4 | **VIC** | RealEstate | 223,000 | 0.56 | 240,840 | 211,850 | 61 | ↑ trên MA50 |
| 5 | **VRE** | RealEstate | 25,250 | 0.55 | 27,270 | 23,987 | 52 | ↓ dưới MA50 |

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
