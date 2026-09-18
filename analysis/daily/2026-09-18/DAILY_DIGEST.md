# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-18 05:11 · dữ liệu giá as-of **2026-09-18** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Edge mô hình yếu (AUC ~0.53-0.55), 4/5 mã ứng viên có vol_ratio dưới 0.5 (thiếu xác nhận dòng tiền), thị trường sắp qua giai đoạn biến động cao quanh sự kiện nâng hạng FTSE và cơ cấu ETF ngoại (18-21/9/2026) - ưu tiên bảo toàn vốn, đứng ngoài quan sát thay vì giải ngân ngay.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 235000-242600 | 262,008 | 230,470 | 25 phiên | 0% hiện tại, tối đa 2-3% nếu xác nhận |
| **VRE** | TB | 25500-26500 | 28,242 | 24,842 | 25 phiên | 0% hiện tại, tối đa 2-3% nếu xác nhận |
| **GAS** | TB | 85000-88000 | 94,824 | 83,410 | 25 phiên | 0% hiện tại, tối đa 2-3% nếu xác nhận |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Setup kỹ thuật xấu nhất nhóm (dưới MA50, xu hướng giảm dài hạn) và rủi ro tin tức cao nhất (khủng hoảng tháng 7 chưa qua hẳn, ĐHĐCĐ bất thường tháng 10 là ẩn số); score mô hình cao nhất không bù được bối cảnh định tính xấu. |
| **GVR** | TB | Không có luận điểm mua nào đủ mạnh; công ty tự đặt kế hoạch lợi nhuận 2026 đi lùi là tín hiệu thận trọng nội bộ không bị phản bác, không có catalyst nâng hạng. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Xu hướng tăng rõ nhất nhóm và catalyst FTSE Large Cap có ngày hiệu lực cụ thể (21/9), nhưng khả năng đã phản ánh phần lớn vào giá sau khi tăng ~60%/tháng, cộng case đảo chiều thực tế 7/9 và vol_ratio yếu nhất toàn thị trường khiến bò/gấu cân bằng.
  - *Huỷ luận điểm nếu:* Tái diễn phiên đảo chiều mạnh kiểu 7/9 không kèm cải thiện thanh khoản; giá đóng cửa dưới SL 230470đ; hoặc sau 21/9 giá không giữ được đà tăng dù dòng vốn cơ cấu đã vào.
- **VRE** — Catalyst kép (FTSE Small Cap + VNSI/Top50) và tích lũy hội tụ MA hợp lý, nhưng thanh khoản vẫn yếu và rủi ro tương quan ngành BĐS với VIC khiến chưa đủ cơ sở mua ngay.
  - *Huỷ luận điểm nếu:* Giá thủng vùng hội tụ MA và SL 24842đ; nhóm BĐS bị bán tháo đồng loạt quanh 21/9; hoặc vol_ratio không cải thiện sau ngày cơ cấu ETF.
- **GAS** — Setup kỹ thuật tốt nhất nhóm và KQKD vượt xa kế hoạch (130% LNST), nhưng tin tốt có thể đã phản ánh vào giá và khối lượng co lại chưa xác nhận dòng tiền mới.
  - *Huỷ luận điểm nếu:* Giá thủng SL 83410đ; điều chỉnh kéo dài dưới MA20 không có volume xác nhận hồi phục; hoặc dòng tiền thị trường tiếp tục bỏ qua GAS quá 2 tuần.

### 📅 Cần theo dõi tuần này
- Diễn biến giá/thanh khoản VIC, VRE quanh ngày hoàn tất cơ cấu ETF (18/9) và hiệu lực nâng hạng FTSE (21/9) - xác nhận dòng tiền mới thực sự vào hay kịch bản bán theo tin thật
- Vol_ratio của VIC/VRE/GAS có vượt rõ rệt lên trên 0.5 hay tiếp tục èo uột
- GAS: giá có giữ vững trên MA20 sau nhịp điều chỉnh hay tiếp tục co hẹp khối lượng
- PNJ: thông tin cụ thể về ĐHĐCĐ bất thường dự kiến tháng 10/2026 (ngày họp, nội dung điều chỉnh kế hoạch)
- Dòng vốn ngoại mua/bán ròng thực tế quanh mốc nâng hạng so với kỳ vọng 6-8 tỷ USD

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.356** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-18_04-52-47`. Chạy lại: skill `vn-swing-daily`.*
