# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-08-31 06:04 · dữ liệu giá as-of **2026-08-28** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Mô hình nền edge yếu (AUC ~0.53-0.55) và ensemble không đồng thuận ở cả 5 mã ứng viên; 4/5 mã cùng ngành RealEstate chịu chung rủi ro chính sách room tín dụng BĐS 2026, nên ưu tiên bảo toàn vốn thay vì giải ngân dàn trải.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 228000-233000 | 254,880 | 224,200 | 25 phiên | 2-3% |
| **VRE** | TB | 25500-26100 | 28,188 | 24,795 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Dưới MA50, RSI trung tính không xác nhận đảo chiều, volume yếu (0,61); tin Chủ tịch mua vào bị lấn át bởi giá giảm 40,6%/năm và áp lực dòng tiền ra lớn từ thương vụ Lotte. |
| **KDH** | Cao | Dưới MA50, volume dưới trung bình, dòng tiền kinh doanh âm 634 tỷ và rủi ro bị loại khỏi rổ VNDiamond chưa được bù đắp đủ bởi tin mở rộng quỹ dự án. |
| **PNJ** | TB | Kỹ thuật yếu nhất nhóm (4,0/10, dưới MA50, volume 0,65); catalyst minh oan pháp lý đã phần lớn phản ánh vào giá (giá hiện tại cao hơn ~5,5% so với đỉnh phiên tăng trần). |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — KQKD 6T2026 vượt trội (+73% DT, LNST x4,5) và trend kỹ thuật xác nhận trên MA50, nhưng catalyst đã phản ánh vào giá (mua sau ATH) và RSI 68,7 cận quá mua.
  - *Huỷ luận điểm nếu:* Giá đóng cửa xuống dưới MA50 hoặc dưới 224.200đ; RSI tiếp tục leo qua 72-75 kèm volume giảm; xuất hiện tin pháp lý/quản trị tiêu cực bất ngờ.
- **VRE** — Setup kỹ thuật tốt nhất nhóm (7,0/10, trên MA50, volume 1,44) và cổ tức tiền mặt hiếm gặp sau 7 năm, nhưng biến động lịch sử cực đoan và 2/5 model con dự báo dưới 50% cho thấy ensemble không đồng thuận.
  - *Huỷ luận điểm nếu:* Giá đóng cửa rơi lại dưới MA50 hoặc dưới 24.795đ; nhịp tăng tuần qua thoái lui >50% trong vài phiên tới; tin xấu mới về ngành bán lẻ/BĐS thương mại hoặc room tín dụng.

### 📅 Cần theo dõi tuần này
- VIC: phản ứng giá vùng 228.000-236.000đ và RSI có hạ nhiệt dưới 65 không
- VRE: nhịp tăng tuần qua (+11,21%) có giữ trên MA50 hay thoái lui mạnh (dead-cat bounce)
- FTSE Russell nâng hạng hiệu lực 21/9/2026 - giai đoạn giải ngân đầu tiên của dòng vốn ETF thụ động
- KDH: thông báo chính thức về khả năng bị loại khỏi rổ VNDiamond kỳ review Q2/2026
- PNJ: diễn biến tố tụng vụ kim cương liên đới công ty giám định con; nội dung họp ĐHĐCĐ bất thường dự kiến tháng 10/2026
- Chính sách room tín dụng bất động sản 2026: văn bản/tín hiệu tiếp theo từ NHNN

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.353** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ 3/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, rủi ro cao hơn kèo momentum.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-08-31_05-45-16`. Chạy lại: skill `vn-swing-daily`.*
