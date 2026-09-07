# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-07 05:11 · dữ liệu giá as-of **2026-09-07** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Bò/gấu ở VRE và VIC ngang nhau, mô hình có edge yếu (AUC ~0.53-0.55), 3/5 mã cùng ngành BĐS (rủi ro tương quan cao), margin bị siết và thanh khoản chung thận trọng nên ưu tiên bảo toàn vốn, chỉ theo dõi thay vì giải ngân đầy đủ.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VRE** | TB | 26800-27400 | 29,268 | 25,745 | 25 phiên | 2-3% |
| **VIC** | TB | 218000-225000 | 269,352 | 236,930 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Dưới MA50 trong downtrend dài hạn, cộng rủi ro pha loãng cụ thể đã xác nhận (~2.000 tỷ đồng chào bán cổ đông hiện hữu) và rủi ro nợ chuyển đổi thành cổ phần từ nhiều đối tác. |
| **PNJ** | Cao | Giá dưới cả MA20 và MA50 trong downtrend dài hạn, khối lượng èo uột không xác nhận đảo chiều - rủi ro bắt dao rơi bất chấp KQKD cơ bản rất mạnh (+116% svck). |
| **GVR** | TB | Kỹ thuật trung tính không xác nhận khối lượng (vol_ratio 0.24); ban lãnh đạo tự hạ dự phóng LNST 2026 (-7%) dù giá cao su thuận lợi, câu chuyện KCN là dài hạn ngoài khung time-stop 25 phiên. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VRE** — Setup kỹ thuật tốt nhất nhóm (vol_ratio 1.24 duy nhất xác nhận) cộng catalyst FTSE Small Cap + cổ tức 10%, nhưng ensemble mô hình con chia rẽ (p_GradBoost/p_XGBoost <0.5) và kháng cự 28-29k từng thất bại nhiều lần.
  - *Huỷ luận điểm nếu:* Vol_ratio quay về dưới 1 kèm giá thủng MA20/50 hội tụ (~25.300-25.500), GDKHQ cổ tức rơi đúng lúc giá test kháng cự, hoặc xác nhận tiêu cực cụ thể từ tin ba lớp game tài chính họ Vin.
- **VIC** — Catalyst FTSE Large Cap rõ ràng nhất nhóm (hiệu lực 21/9/2026) và KQKD kỷ lục, nhưng RSI 70.2 quá mua cộng volume thấp nhất nhóm (0.21) và rủi ro sell-the-news quanh ngày cơ cấu ETF khiến nên chờ pullback thay vì mua đuổi.
  - *Huỷ luận điểm nếu:* Giá thủng MA20/50 (~218-220k) trước khi hồi phục, diễn biến sell-the-news rõ rệt quanh 18-21/9, xác nhận tiêu cực cụ thể về cấu trúc tài chính họ Vin, hoặc tín hiệu NHNN siết room tín dụng BĐS ảnh hưởng cụ thể tới VIC.

### 📅 Cần theo dõi tuần này
- FTSE Russell: danh mục 27 mã đã chốt 7/9/2026, cơ cấu ETF hoàn tất sau phiên 18/9/2026, hiệu lực chính thức 21/9/2026 - theo dõi phản ứng giá VIC/VRE quanh các mốc này (rủi ro buy-the-rumor-sell-the-news)
- VRE: vol_ratio có duy trì >1 thêm các phiên tới không, và phản ứng giá tại vùng kháng cự 28.000-29.000 VND
- VIC: RSI có hạ nhiệt dưới 70 kèm giữ vững trên MA20/50 (~218-220k) hay bị thủng trước ngày 21/9
- Nội dung chi tiết bài viết ba lớp game tài chính họ Vin (VIC-VHM-VRE-VPL) khi fetch được - hiện chưa kiểm chứng (lỗi 403)
- Diễn biến margin/thanh khoản chung HoSE (đã cắt margin một số mã do lỗ bán niên)
- Tiến độ chính sách NHNN về room tín dụng BĐS 2026 - ảnh hưởng nhóm VIC/VRE/PDR

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.356** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-07_04-52-12`. Chạy lại: skill `vn-swing-daily`.*
