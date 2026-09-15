# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-15 05:20 · dữ liệu giá as-of **2026-09-15** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Mô hình nền có edge yếu (AUC ~0.53-0.55) và base win-rate thấp hơn buy-and-hold trên tập kiểm định; bò và gấu cân bằng ở cả 3 mã có luận điểm mua nên ưu tiên bảo toàn vốn, không giải ngân mới.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 235000-242000 | 260,820 | 229,425 | 25 phiên | 0% (theo dõi, chờ xác nhận) |
| **VRE** | TB | 25300-25900 | 27,648 | 24,320 | 25 phiên | 0% (theo dõi, chờ xác nhận) |
| **GAS** | TB | 86000-89000 | 95,796 | 84,265 | 25 phiên | 0% (theo dõi, chờ xác nhận) |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Downtrend dốc dưới MA50 (bắt dao rơi) kèm lỗ ròng quý 2 kỷ lục và dự phòng 2.267 tỷ chưa dứt điểm. |
| **GVR** | Cao | Không có catalyst (ngoài rổ FTSE), kỹ thuật đi ngang yếu (RSI dưới 50, vol_ratio 0.15), thêm rủi ro pháp lý cổ đông nhỏ. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Catalyst FTSE Large Cap (21/9) và trend dài hạn đẹp, nhưng vol_ratio 0.10 thấp nhất nhóm và đã có phiên đảo chiều giảm >4,3% tại vùng kháng cự gần TP.
  - *Huỷ luận điểm nếu:* Tái lập giảm mạnh (>4%/phiên) quanh vùng 260k, hoặc dòng vốn ngoại không xác nhận sau 21/9 (dấu hiệu sell the news), hoặc tin xấu mới về đòn bẩy trái phiếu quốc tế.
- **VRE** — Tin tức/KQKD tốt nhất nhóm và catalyst FTSE Small Cap, nhưng kỹ thuật mới cắt lên MA50 (dễ whipsaw) và vol_ratio 0.23 chưa xác nhận dòng tiền.
  - *Huỷ luận điểm nếu:* Giá cắt xuống lại dưới MA50 kèm thanh khoản tăng, hoặc không phản ứng tích cực quanh sự kiện FTSE 21/9.
- **GAS** — Kỹ thuật/cơ bản tốt nhất nhóm (breakout, doanh thu +39% YoY) nhưng RSI 67 gần quá mua cộng dồn với giảm giá cơ học quanh ngày GDKHQ cổ tức trong đúng khung nắm giữ.
  - *Huỷ luận điểm nếu:* RSI vượt 70 rồi đảo chiều giảm mạnh, hoặc thêm công bố bất lợi về rủi ro công ty đại chúng.

### 📅 Cần theo dõi tuần này
- 21/9/2026: FTSE Russell nâng hạng có hiệu lực - theo dõi phản ứng giá VIC/VRE (buy the rumor sell the news hay không)
- ~23/9/2026 (ngày chính xác chưa kiểm chứng): GAS chốt danh sách cổ đông nhận cổ tức 25% tiền mặt - theo dõi điều chỉnh giá và RSI
- 26/10/2026: PNJ công bố BCTC quý 3/2026 - đánh giá lại tồn kho kim cương
- Diễn biến vol_ratio của VIC/VRE/GAS trong tuần tới
- Thời hạn khắc phục tình trạng không đủ điều kiện công ty đại chúng của GAS/GVR (chưa kiểm chứng mốc ngày)

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-15_05-01-59`. Chạy lại: skill `vn-swing-daily`.*
