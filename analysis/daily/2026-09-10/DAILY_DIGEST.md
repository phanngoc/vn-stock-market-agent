# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-10 05:10 · dữ liệu giá as-of **2026-09-10** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Không mã nào hội tụ đủ trend + volume xác nhận + catalyst chắc chắn để đạt ngưỡng MUA; toàn bộ 5 ứng viên có vol_ratio dưới 1 và mô hình có edge yếu (AUC ~0.53-0.55) nên ưu tiên bảo toàn vốn, chỉ thăm dò nhỏ ở mã THEO DÕI.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 246000-251000 | 269,136 | 236,740 | 25 phiên | 0-2% |
| **VRE** | TB | 25800-26500 | 28,242 | 24,842 | 25 phiên | 0-2% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Rủi ro pha loãng cụ thể (chào bán 5:1, tăng vốn thêm ~2.393 tỷ đồng), áp lực trả nợ trái phiếu, lùm xùm quản trị chưa giải quyết, kỹ thuật vẫn dưới MA50 đang giảm - bắt dao rơi rõ nhất nhóm. |
| **GVR** | TB | Chính phe bò thừa nhận không có catalyst ngắn hạn rõ ràng trong khung 25 phiên, ban lãnh đạo tự nhận thận trọng dù giá cao su tăng, và volume chưa xác nhận breakout (0.230). |
| **PNJ** | TB | Điểm mô hình cao nhất nhóm và tin tức cơ bản tích cực (KQKD mạnh, rủi ro pháp lý cũ đang gỡ), nhưng giá vẫn dưới cả MA20/MA50 với MA50 đang dốc xuống - mâu thuẫn model-vs-giá lớn nhất, chưa xác nhận đảo chiều kỹ thuật. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Uptrend rõ trên MA20/50 với catalyst FTSE cụ thể (21/9/2026) và KQKD nửa năm +360%, nhưng vol_ratio thấp nhất toàn nhóm (0.099) và RSI cận quá mua (67.2) khiến rủi ro phân phối/sell-the-news chưa thể loại trừ.
  - *Huỷ luận điểm nếu:* Giá đóng cửa dưới MA50 hoặc dưới vùng SL 236.740đ; xuất hiện thêm phiên khối lượng lớn kèm giảm mạnh cho thấy phân phối tiếp diễn; dòng vốn FTSE không giải ngân như kỳ vọng quanh 21/9/2026.
- **VRE** — Vừa lấy lại MA50 với vol_ratio tốt nhất nhóm (dù vẫn dưới 1) và kế hoạch lợi nhuận/doanh thu 2 chữ số, nhưng dữ liệu cổ tức mâu thuẫn giữa các nguồn và rủi ro lây lan tâm lý từ hệ sinh thái Vingroup/ngành BĐS làm giảm độ tin cậy.
  - *Huỷ luận điểm nếu:* Giá đóng cửa dưới MA50 hoặc dưới vùng SL 24.842đ; thông tin cổ tức xác nhận tiêu cực hơn kỳ vọng; áp lực bán lan rộng trong nhóm BĐS do làn sóng phát hành tăng vốn.

### 📅 Cần theo dõi tuần này
- 21/9/2026: FTSE Russell nâng hạng chính thức, dòng vốn thụ động dự kiến giải ngân - theo dõi phản ứng giá/volume VIC (rủi ro sell-the-news vì danh sách đã công bố từ 21/8)
- Volume xác nhận: cần ít nhất 1 phiên vol_ratio >1 ở VIC hoặc VRE để coi là dòng tiền thực sự quay lại
- Thông tin cổ tức VRE: làm rõ mâu thuẫn giữa hai nguồn tin (đã thông qua cổ tức 10% vs không chia cổ tức) qua nghị quyết ĐHĐCĐ chính thức
- Diễn biến chào bán cổ phiếu 5:1 của PDR (giá bán, tiến độ) - nguồn rủi ro pha loãng cụ thể nhất nhóm
- MA50 của PNJ: theo dõi liệu giá có xác nhận đảo chiều (đóng cửa vượt MA50 kèm volume) hay tiếp tục giảm

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-10_04-52-48`. Chạy lại: skill `vn-swing-daily`.*
