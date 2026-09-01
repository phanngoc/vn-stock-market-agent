# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-01 05:39 · dữ liệu giá as-of **2026-08-28** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Mô hình định lượng có edge yếu (AUC ~0.53-0.55) và ngay trong 2 mã setup tốt nhất, 2/5 mô hình con vẫn nghiêng dưới 50%; 4/5 mã ứng viên cùng ngành Bất động sản là rủi ro tập trung, nên không giải ngân mới ngay, ưu tiên bảo toàn vốn và chờ xác nhận thêm.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 224000-230000 | 254,880 | 224,200 | 25 phiên | 2-3% |
| **VRE** | TB | 25800-26500 | 28,188 | 24,795 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Kỹ thuật yếu nhất nhóm (downtrend dài từ tháng 3, vol_ratio 0.61 thấp nhất) cộng rủi ro pha loãng ~200 triệu cổ phiếu và phát hành trái phiếu 5.600 tỷ đồng đang triển khai, không có catalyst bù đắp. |
| **KDH** | Cao | Downtrend xác nhận bởi cả nhãn định lượng (trend_up=False) lẫn thời gian: tin tốt Gladia (90% booking) đã gần 1 tháng mà vol_ratio vẫn dưới trung bình (0.84) - thị trường chưa phản ứng bằng dòng tiền, dạng bắt dao rơi. |
| **PNJ** | Cao | Lỗ kỷ lục quý II/2026 (gần 283 tỷ đồng) do trích lập dự phòng liên quan bê bối P-Lab, rủi ro uy tín thương hiệu chưa rõ đã xử lý dứt điểm; kỹ thuật dưới MA50 với khối lượng yếu (0.65) không xác nhận nhịp hồi giá. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Catalyst FTSE mạnh nhất nhóm (GEIS + All-World) và KQKD kỷ lục là điểm cộng thực, nhưng RSI sát quá mua và mua gần đỉnh ngắn hạn (236k, cách đỉnh 242k chỉ 2.5%) cộng đòn bẩy 86% nợ/tài sản giữa lúc NHNN siết tín dụng BĐS khiến chưa đủ cơ sở mua đuổi ngay.
  - *Huỷ luận điểm nếu:* Giá thủng SL 224.200đ; hoặc có tin cụ thể về siết room tín dụng ảnh hưởng trực tiếp nhóm Vingroup; hoặc dấu hiệu sell-the-news rõ rệt quanh/sau ngày FTSE hiệu lực 21/9.
- **VRE** — Setup kỹ thuật + tin tức đồng thuận tốt nhất nhóm (uptrend mới, vol xác nhận, cổ tức lần đầu sau 7 năm, FTSE 21/9), nhưng vùng kháng cự 27.000-28.000đ trùng sát TP và catalyst FTSE đã biết trước 11 ngày (rủi ro sell-the-news) khiến chưa đủ tin cậy để vào full vị thế ngay.
  - *Huỷ luận điểm nếu:* Giá thủng SL 24.795đ trước khi vượt được vùng cản 27-28k; hoặc tiếp cận kháng cự mà không có xác nhận khối lượng; hoặc GDKHQ cổ tức xác nhận rơi ngoài time-stop mà giá không có động lực khác.

### 📅 Cần theo dõi tuần này
- VRE: giá có vượt dứt khoát vùng cản 27.000-28.000đ kèm khối lượng xác nhận hay bị chặn lại
- VIC: giá có giữ vững trên vùng hỗ trợ MA20/MA50 hay tiếp tục điều chỉnh từ đỉnh ngắn hạn 242.000đ, RSI có hạ nhiệt khỏi vùng quá mua
- Chính sách NHNN siết tăng trưởng tín dụng bất động sản theo từng ngân hàng - nếu cụ thể hoá sẽ ảnh hưởng cả nhóm VIC/VRE/KDH/PDR
- Ngày GDKHQ cổ tức tiền mặt 10% của VRE (hiện chưa kiểm chứng)
- KDH: tỷ lệ hấp thụ đợt mở bán phần cao tầng Gladia Q3/2026 và diễn biến vol_ratio
- PNJ: diễn biến tiếp theo của bê bối P-Lab và rủi ro trích lập/uy tín thương hiệu
- Phản ứng giá VIC/VRE quanh và sau ngày FTSE hiệu lực 21/9/2026 (rủi ro sell-the-news)

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.353** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ 3/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, rủi ro cao hơn kèo momentum.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-01_05-18-44`. Chạy lại: skill `vn-swing-daily`.*
