# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-08 05:06 · dữ liệu giá as-of **2026-09-08** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Toàn bộ 5 mã ứng viên đều có vol_ratio dưới 1 (chưa xác nhận dòng tiền mạnh) và mô hình nền có edge yếu (AUC ~0.53-0.55); catalyst nâng hạng FTSE 21/9/2026 đáng theo dõi cho VIC/VRE nhưng chưa đủ để giải ngân ngay.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 235000-242000 | 261,036 | 229,615 | 25 phiên | 2-3% |
| **VRE** | TB | 25800-26500 | 28,458 | 25,032 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Downtrend rõ nhất nhóm (điểm kỹ thuật 3.5/10, thấp nhất), rủi ro pha loãng cụ thể và định lượng được (~2.000 tỷ phát hành + 34,1 triệu cp hoán đổi nợ), không có catalyst FTSE bù đắp. |
| **PNJ** | TB | Vẫn dưới MA50 trong downtrend dài (80k->30k từ tháng 3-7) - dạng bắt dao rơi; luận điểm mua phụ thuộc hoàn toàn vào KQKD quý 3/2026 chưa công bố, không có catalyst FTSE bù đắp. |
| **GVR** | TB | Không có xu hướng kỹ thuật rõ ràng (đi ngang nhiều tháng, chưa xác nhận breakout), kế hoạch lợi nhuận đi lùi năm tới, giá đã chạy trước mạnh trong quá khứ, không có catalyst FTSE. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Catalyst FTSE Large Cap 21/9/2026 định lượng, có ngày cụ thể, nhưng giá đã tăng ~60%/tháng và vol_ratio thấp nhất nhóm (0.21) chưa xác nhận dòng tiền.
  - *Huỷ luận điểm nếu:* Giá thủng MA20 kèm khối lượng lớn trước 21/9 (dấu hiệu sell-the-rumor sớm); hoặc xác nhận Vingroup/VinFast triển khai lại phát hành trái phiếu chuyển đổi pha loãng.
- **VRE** — Setup kỹ thuật tốt nhất nhóm (vol_ratio cao nhất, RSI còn dư địa) cộng catalyst kép FTSE Small Cap + cổ tức 10%, nhưng ngày GDKHQ cổ tức chưa xác định và TP nằm tại vùng kháng cự thực.
  - *Huỷ luận điểm nếu:* Giá thủng MA50 hoặc xuất hiện bán tháo diện rộng nhóm BĐS (tin xấu cụ thể về trái phiếu đáo hạn ngành) trước khi FTSE/cổ tức kịp phát huy tác dụng.

### 📅 Cần theo dõi tuần này
- 21/9/2026: FTSE Russell chính thức nâng hạng có hiệu lực - theo dõi phản ứng giá/khối lượng VIC, VRE quanh mốc này
- Vol_ratio cả nhóm cần vượt rõ trên 1.0 mới coi là xác nhận dòng tiền thật, hiện tất cả đều dưới 0.5
- Ngày GDKHQ cổ tức tiền mặt 10% của VRE (dự kiến quý 3/2026, ngày cụ thể chưa kiểm chứng)
- KQKD quý 3/2026 của VIC, VRE, PNJ - đặc biệt quan trọng với PNJ
- Diễn biến trái phiếu BĐS đáo hạn (~141.908 tỷ đồng nửa cuối 2026) - rủi ro hệ thống cho VIC, VRE, PDR, GVR
- Xác nhận việc Vingroup/VinFast có triển khai lại kế hoạch phát hành 5.000 tỷ trái phiếu chuyển đổi hay không

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-08_04-47-32`. Chạy lại: skill `vn-swing-daily`.*
