# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-04 04:59 · dữ liệu giá as-of **2026-09-04** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Không mã nào đạt đồng thuận đủ mạnh giữa kỹ thuật, tin tức và rủi ro để MUA; nhóm ứng viên tập trung cao vào BĐS và mô hình nền có AUC chỉ ~0.53-0.55 nên ưu tiên bảo toàn vốn.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 241300-248000 | 274,320 | 241,300 | 25 phiên | 2-3% |
| **VRE** | TB | 25800-26700 | 28,836 | 25,365 | 25 phiên | 3-4% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Kỹ thuật tệ nhất nhóm (volume 0.34 thấp nhất, dưới MA50) cộng rủi ro pha loãng định lượng lớn (~233,7 triệu cp mới, ước tính hơn 23% cổ phiếu lưu hành) chưa rõ thời điểm chốt quyền. |
| **GVR** | TB | Hội tụ 3 tín hiệu tiêu cực đồng thời: volume rất yếu (0.36) không xác nhận breakout MA50, guidance nội bộ hạ LNST 2026 -7%, và model split (GradBoost/XGBoost dưới 0.5) không có catalyst ngắn hạn bù lại. |
| **PNJ** | TB | Dưới MA50 trong downtrend dài (85k→39k, mất ~54% từ đỉnh tháng 2) chưa xác nhận đảo chiều; KQKD Q1 mạnh là tin cũ, không đủ đảo ngược trend giá. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Catalyst FTSE GEIS (21/9) và KQKD đột biến là thật, nhưng RSI 77 quá mua và volume không xác nhận cú tăng vọt khiến entry hiện tại rủi ro cao.
  - *Huỷ luận điểm nếu:* RSI tiếp tục trên 75 kèm volume không cải thiện; giá giảm mạnh (>3%/1-2 phiên) quanh 21/9 (dấu hiệu sell-the-news); tin xấu đảo ngược catalyst FTSE.
- **VRE** — Kỹ thuật tốt nhất nhóm (RSI chưa quá mua, volume xác nhận) và catalyst cổ tức 10% lần đầu sau 7 năm, nhưng ngày GDKHQ chưa kiểm chứng và model-disagreement (GradBoost/XGBoost dưới 0.5) cần theo dõi thêm.
  - *Huỷ luận điểm nếu:* Giá thủng lại MA50 kèm volume yếu; không có công bố ngày GDKHQ trong vài tuần tới; model score tổng hợp giảm sâu hơn.

### 📅 Cần theo dõi tuần này
- 21/9/2026: FTSE Russell chính thức nâng hạng, VIC hưởng lợi trực tiếp - theo dõi rủi ro sell-the-news quanh mốc này
- Ngày GDKHQ cổ tức tiền mặt 10% của VRE (chưa công bố cụ thể) - xác nhận qua VSD/HOSE
- Thời điểm chốt quyền chào bán cổ phiếu 5:1 của PDR (pha loãng ~23%+) - theo dõi công bố HOSE
- Diễn biến VN-Index quanh vùng 1.800-1.830 điểm và dòng vốn khối ngoại

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.355** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-04_04-42-31`. Chạy lại: skill `vn-swing-daily`.*
