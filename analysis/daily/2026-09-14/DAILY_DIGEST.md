# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-14 05:24 · dữ liệu giá as-of **2026-09-14** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Không mã nào trong 5 ứng viên hội tụ đủ kỹ thuật xác nhận, catalyst rõ ràng và thanh khoản mạnh để MUA ngay; mô hình có edge yếu (AUC ~0.53-0.55) nên ưu tiên bảo toàn vốn và chờ xác nhận thêm.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **GAS** | TB | 82000-86000 | 92,016 | 80,940 | 25 phiên | 2-3% |
| **VIC** | Thấp | 235000-240000 | 257,148 | 226,195 | 25 phiên | 2-3% |
| **VRE** | Thấp | 24800-25500 | 27,378 | 24,082 | 25 phiên | 2% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **GVR** | Cao | Kỹ thuật đang test lại hỗ trợ MA50 sau 2 phiên giảm mạnh, chưa xác nhận giữ được, cộng rủi ro pháp lý cơ cấu cổ đông thật (Nhà nước nắm 96,8%, nguy cơ hủy tư cách công ty đại chúng nếu không thoái vốn trong 1 năm) và không có catalyst FTSE bù đắp. |
| **PNJ** | Cao | Setup kỹ thuật yếu nhất nhóm - downtrend 6 tháng rõ ràng (77k về 36k), giá dưới MA50 đang dốc xuống, TP đặt đúng tại kháng cự động MA50 - dạng bắt dao rơi; KQKD cơ bản tốt không đủ bù đắp rủi ro kỹ thuật và biên lợi nhuận gộp toàn công ty đang giảm. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **GAS** — Setup kỹ thuật tốt nhất nhóm (uptrend ổn định, RSI chưa quá mua, vol_ratio cao nhất dù vẫn dưới 1) cộng cổ tức tiền mặt 25% đang chi trả thực, nhưng ĐHĐCĐ bất thường đúng ngày tín hiệu có nội dung chưa biết trong bối cảnh rủi ro pháp lý cơ cấu cổ đông.
  - *Huỷ luận điểm nếu:* Đóng cửa dưới SL 80.940đ; nội dung ĐHĐCĐ bất thường 14/9 tiêu cực liên quan thoái vốn Nhà nước/tư cách công ty đại chúng.
- **VIC** — Điểm mô hình cao nhất nhóm và KQKD 6T2026 tăng đột biến (+360,5% svck) cùng catalyst FTSE large-cap 21/9, nhưng vol_ratio 0.189 là thấp nhất trong toàn bộ 30 mã và mô hình con bất đồng mạnh (LSTM outlier kéo điểm lên) nên chưa đủ cơ sở giải ngân.
  - *Huỷ luận điểm nếu:* Đóng cửa dưới SL 226.195đ; vol_ratio tiếp tục dưới 0.25 kèm xác nhận bán ròng lớn từ cơ cấu ETF frontier cũ; tin tiêu cực mới về đợt phát hành trái phiếu quốc tế ~8.050 tỷ đồng.
- **VRE** — Hỗ trợ tin tức mạnh nhất nhóm (KQKD tốt, cổ tức, chiến lược mở rộng Vincom Collection) và catalyst FTSE small-cap 21/9, nhưng nhãn mô hình trend_up mâu thuẫn với MA50 quan sát thực tế vẫn đang dốc xuống - độ tin cậy tín hiệu thấp.
  - *Huỷ luận điểm nếu:* Đóng cửa dưới SL 24.082đ; MA50 tiếp tục dốc xuống rõ ràng qua 21/9 mà không có phản ứng tích cực từ dòng vốn FTSE; tránh cộng dồn với VIC do cùng hệ sinh thái Vingroup.

### 📅 Cần theo dõi tuần này
- 14/9/2026: nội dung nghị quyết ĐHĐCĐ bất thường PV Gas (GAS) - quyết định việc có nâng cấp THEO DÕI lên entry hay không
- 21/9/2026: FTSE Russell nâng hạng VN có hiệu lực - theo dõi phản ứng giá VIC (large-cap) và VRE (small-cap), và rủi ro bán ròng cơ cấu ETF frontier cũ trước ngày này
- vol_ratio của VIC, GAS, VRE cần phục hồi trên 0.5 để coi thanh khoản đã xác nhận lại
- Ngày GDKHQ cổ tức của GAS (25%), VRE và PNJ (10%) - hiện chưa kiểm chứng cụ thể, cần cập nhật để tránh nhầm điều chỉnh giá do chia cổ tức với gãy xu hướng
- Tiến độ thoái vốn Nhà nước xuống dưới 90% tại GVR/GAS liên quan rủi ro hủy tư cách công ty đại chúng

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-14_05-05-12`. Chạy lại: skill `vn-swing-daily`.*
