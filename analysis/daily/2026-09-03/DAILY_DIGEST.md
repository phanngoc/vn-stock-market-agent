# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-03 05:00 · dữ liệu giá as-of **2026-09-03** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Cả 5 mã ứng viên đều có vol_ratio dưới 1 và 4/5 mã tập trung vào bất động sản/hệ sinh thái Vingroup; mô hình định lượng nền có edge yếu (AUC ~0.53-0.55) nên ưu tiên bảo toàn vốn hơn là giải ngân đầy đủ.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 224500-230000 | 255,204 | 224,485 | 25 phiên | 2-3% |
| **VRE** | Thấp | 25800-26250 | 28,350 | 24,938 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Kỹ thuật yếu nhất nhóm sau KDH (3/10), hồi không khối lượng trong downtrend, cộng rủi ro pha loãng đã xác nhận bằng kế hoạch chào bán 5:1 (~2.000 tỷ đồng) trong khi dòng tiền kinh doanh 2025 âm gần 3.000 tỷ. |
| **KDH** | Cao | Setup kỹ thuật yếu nhất trong toàn bộ nhóm ứng viên (2.5/10), downtrend còn dốc, chưa có dấu hiệu tạo đáy - tin cơ bản tốt (sạch nợ trái phiếu, catalyst FTSE) chưa đủ để đảo ngược xu hướng giảm. |
| **PNJ** | TB | Hồi trong downtrend dài (80k→30k) chưa xác nhận đảo chiều bằng MA, trong khi Q2/2026 lỗ kỷ lục ~283 tỷ đồng do biến động giá vàng/tồn kho - kỹ thuật và cơ bản đều không ủng hộ. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Breakout trên MA50 với KQKD H1/2026 rất mạnh và catalyst FTSE 21/9 có mốc ngày cụ thể, nhưng khối lượng breakout yếu (vol_ratio 0.41) sau đà tăng 60%/tháng là rủi ro climax/phân phối thật - chưa đủ cơ sở giải ngân đầy đủ.
  - *Huỷ luận điểm nếu:* Vol_ratio tiếp tục dưới 0.5 khi giá đi ngang/giảm sau breakout; giá thủng 224.485đ; qua ngày FTSE 21/9 mà không có phản ứng giá tích cực (sell-the-news hiện thực).
- **VRE** — Vừa vượt lại MA50 sau tạo đáy với KQKD đúng tiến độ và catalyst FTSE, nhưng vol_ratio 0.37 yếu nhất nhóm 5 mã ngay tại điểm vượt là tín hiệu bull-trap cổ điển, và TP nằm sát vùng kháng cự cũ có lực bán lịch sử.
  - *Huỷ luận điểm nếu:* Giá tụt lại xuống dưới MA50; vol_ratio không cải thiện trong 5-7 phiên tới; tin xấu từ hệ sinh thái Vingroup/Vinhomes gây bán chéo tâm lý.

### 📅 Cần theo dõi tuần này
- VIC: vol_ratio có vượt 1.0 để xác nhận breakout thật hay tiếp tục yếu (rủi ro phân phối)
- VIC: phản ứng giá quanh/sau ngày FTSE Russell nâng hạng có hiệu lực 21/9/2026
- VRE: giá có giữ vững trên MA50 (~26.000đ) hay tụt lại (bull-trap)
- VRE: diễn biến khi tiệm cận vùng kháng cự cũ 28.000-29.000đ
- PDR: tiến độ/giá chào bán cổ phiếu 5:1 (~10.000đ/cp, huy động ~2.000 tỷ đồng)
- KDH: dấu hiệu tạo đáy kỹ thuật (chưa xuất hiện) và thời điểm mở bán dự án Gladia by the Waters (Q3/2026, chưa kiểm chứng ngày cụ thể)
- PNJ: KQKD Q3/2026 sơ bộ, biến động giá vàng/tồn kho có ảnh hưởng biên lợi nhuận
- Toàn thị trường: ngày GDKHQ/họp ĐHĐCĐ bất thường tháng 9/2026 cho VIC/PNJ/PDR - chưa kiểm chứng

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.354** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ 3/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, rủi ro cao hơn kèo momentum.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-03_04-42-12`. Chạy lại: skill `vn-swing-daily`.*
