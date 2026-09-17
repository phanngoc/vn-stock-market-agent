# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-17 05:18 · dữ liệu giá as-of **2026-09-17** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Volume dưới trung bình ở cả 5 mã ứng viên, mô hình nền AUC ~0.53-0.55 (edge yếu), khối ngoại đang bán ròng ngay trước sự kiện nâng hạng FTSE 21/9 -> ưu tiên bảo toàn vốn, không mở vị thế MUA mới.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VRE** | TB | 24800-25500 | 27,972 | 24,605 | 25 phiên | 2-3% |
| **GVR** | TB | 31500-32500 | 34,992 | 30,780 | 25 phiên | 2-3% |
| **GAS** | Thấp | 85500-87500 | 95,688 | 84,170 | 25 phiên | 2% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Dưới MA50 đang giảm (bắt dao rơi), volume 0.19 cực thấp, lợi nhuận sau kiểm toán giảm ~38-40%. |
| **VIC** | TB | Xu hướng giá đẹp nhất nhóm và catalyst FTSE lớn nhất (ước tính ~46.4 triệu USD mua ròng), nhưng đây mới là dự báo chưa xảy ra. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VRE** — KQKD vượt tiến độ kế hoạch (80.6% lợi nhuận năm sau 9 tháng), nằm trong nhóm hưởng lợi FTSE, SL có biên an toàn dưới vùng tích lũy tháng 8 - nhưng volume 0.41 chưa xác nhận bứt phá.
  - *Huỷ luận điểm nếu:* Khối ngoại tiếp tục bán ròng mạnh quanh 21/9 (kịch bản sell-the-news); giá thủng 24.000 kèm volume tăng (phân phối, không phải tích lũy).
- **GVR** — Setup kỹ thuật đồng thuận nhất nhóm (MA20 cắt lên MA50, volume tương đối tốt nhất dù vẫn dưới 1, lợi nhuận 5 tháng +30% YoY đã công bố).
  - *Huỷ luận điểm nếu:* Ban lãnh đạo tự đặt kế hoạch lợi nhuận 2026 giảm (~-2.9% YoY) và không có catalyst ngắn hạn trong khung 25 phiên; giá thủng đáy 30.300 hoặc volume tụt lại sẽ vô hiệu luận điểm.
- **GAS** — Catalyst cổ tức GDKHQ 22/9 (25%) là dữ kiện thật, KQKD 8 tháng vượt xa kế hoạch năm.
  - *Huỷ luận điểm nếu:* RSI 63 quá mua, SL sát MA20 dễ bị quét khi test lại; không có luận điểm bò riêng được xây dựng cho mã này - nếu GDKHQ 22/9 qua đi mà giá không phản ứng tích cực, rút lui.

### 📅 Cần theo dõi tuần này
- 21/9/2026: FTSE Russell chính thức nâng hạng - theo dõi dòng vốn ngoại thực tế (mua/bán ròng) tại VIC, VRE
- 22/9/2026: GDKHQ cổ tức tiền mặt GAS (25%) - theo dõi phản ứng giá quanh MA20 (~85k)
- 10/9-9/10/2026: khối lượng bán ra thực tế từ gia đình Chủ tịch PNJ (25 triệu cổ phiếu)
- Ngày GDKHQ cổ tức 10% của VRE - chưa kiểm chứng, cần công bố chính thức từ HOSE
- Xu hướng mua/bán ròng khối ngoại toàn thị trường (hiện bán ròng ~2.200 tỷ từ đầu tháng 9)
- Volume ratio của VIC - cần phục hồi rõ rệt (>1) trước khi xem xét lại luận điểm TRÁNH
- Thanh khoản toàn thị trường (hiện ~17.156 tỷ/phiên)

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-17_05-00-45`. Chạy lại: skill `vn-swing-daily`.*
