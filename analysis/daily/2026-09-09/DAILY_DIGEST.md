# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-09 05:11 · dữ liệu giá as-of **2026-09-09** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Không mã nào trong 5 ứng viên top-score hội tụ đủ bằng chứng bò áp đảo gấu; mô hình nền có AUC yếu (~0.53-0.55) nên ưu tiên bảo toàn vốn, đứng ngoài phần lớn.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 245000-250500 | 270,540 | 237,975 | 25 phiên | 0-3% |
| **GVR** | TB | 31500-32500 | 34,506 | 30,352 | 25 phiên | 0-3% |
| **VRE** | TB | 26000-26800 | 28,728 | 25,270 | 25 phiên | 0-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Kỹ thuật yếu nhất nhóm (downtrend chưa xác nhận dừng) cộng rủi ro pha loãng cụ thể đã công bố (chào bán 5:1 giá 10.000đ thấp hơn thị trường, tăng vốn điều lệ ~24%). |
| **PNJ** | Cao | Lỗ ròng Q2 lần đầu kể từ niêm yết, dự phòng lũy kế tăng gần gấp đôi công bố ban đầu, rủi ro bán cổ phiếu nội bộ từ gia đình Chủ tịch. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Trend tăng mạnh nhất nhóm, KQKD H1 tốt, nhưng RSI cận quá mua và vol_ratio thấp nhất nhóm (0.13) khiến động lượng đáng ngờ.
  - *Huỷ luận điểm nếu:* Giá thủng vùng 238k kèm khối lượng lớn quanh/sau đợt cơ cấu ETF (11-21/9), hoặc xác nhận bán ròng ETF gây áp lực kéo dài sau 21/9 -> chuyển sang TRÁNH.
- **GVR** — Setup breakout kỹ thuật sạch khỏi vùng tích lũy 28-40k, nhưng khối lượng yếu (0.30) khiến rủi ro breakout giả cao.
  - *Huỷ luận điểm nếu:* Tin chính thức cổ tức GVR thấp hơn nhiều so với đồn đoán 25% gây phản ứng giá tiêu cực, hoặc giá quay lại vùng tích lũy 28-30k -> chuyển sang TRÁNH.
- **VRE** — Tin tức cơ bản tốt nhất nhóm (KQKD cốt lõi +~20%), nhưng score mô hình tổng hợp thực ra thấp nhất nhóm và khối lượng còn yếu quanh MA50.
  - *Huỷ luận điểm nếu:* Giá thủng vùng 25.3-25.5k kèm khối lượng lớn, hoặc xác nhận cụ thể VRE bị bán ròng ETF quy mô đáng kể -> chuyển sang TRÁNH.

### 📅 Cần theo dõi tuần này
- 11/9/2026: MarketVector/STOXX công bố kết quả cơ cấu ETF quý 3 (ảnh hưởng VIC, khả năng VRE)
- 11-14/9/2026: PHR (công ty con GVR) GDKHQ/chốt quyền cổ tức tiền mặt 14%
- 21/9/2026: FTSE Russell chính thức nâng hạng Việt Nam + hiệu lực cơ cấu ETF quý 3 cùng ngày
- Dự kiến 21/10/2026: PNJ họp ĐHĐCĐ bất thường thông qua kế hoạch điều chỉnh sau lỗ Q2
- PDR: theo dõi tiến độ phê duyệt UBCKNN cho đợt chào bán 5:1 (chưa có ngày cụ thể)

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-09_04-51-25`. Chạy lại: skill `vn-swing-daily`.*
