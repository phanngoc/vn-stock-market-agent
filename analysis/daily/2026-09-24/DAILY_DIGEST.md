# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-24 05:16 · dữ liệu giá as-of **2026-09-24** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Không mã nào đạt ngưỡng MUA vì 3 mã bò tốt nhất (GAS, GVR, VIC) đều bị phản biện đủ mạnh để hạ xuống THEO DÕI; mô hình quant chỉ có edge yếu (AUC ~0.53-0.55) nên ưu tiên bảo toàn vốn.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **GAS** | TB | 83500-85000 | 90,936 | 79,990 | 25 phiên | 2-3% |
| **GVR** | TB | 32500-33500 | 35,640 | 31,350 | 25 phiên | 2-3% |
| **VIC** | Thấp | 228000-232000 | 248,940 | 218,975 | 25 phiên | 1-2% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Downtrend dưới cả MA20/MA50 chưa xác nhận đảo chiều, LNST quý 2 âm do trích lập dự phòng, rủi ro thương hiệu chưa kiểm chứng mức độ. |
| **KDH** | Cao | Rủi ro rõ rệt nhất nhóm: downtrend sâu chưa xác nhận đáy, nợ vay/vốn chủ 83%, tồn kho ~29.500 tỷ, vướng văn bản UBCKNN chưa rõ hậu quả. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **GAS** — KQKD vượt kế hoạch và cổ tức 25% có nguồn thật, nhưng đây là tin đã cũ và đã phản ánh vào giá; volume entry yếu (0.34) chưa xác nhận lực mua.
  - *Huỷ luận điểm nếu:* Tin 'vướng tiêu chuẩn công ty đại chúng' được xác nhận nghiêm trọng, hoặc giá thủng MA50 kèm khối lượng lớn.
- **GVR** — Setup kỹ thuật đẹp nhất nhóm (vol_ratio 1.44 duy nhất >1, MA50 ngóc lên) nhưng vol_ratio không phân biệt được mua/bán và giá vẫn trong downtrend dài hạn -30% từ đỉnh.
  - *Huỷ luận điểm nếu:* Giá phá đáy vừa tạo (dưới 31.000đ) hoặc xuất hiện thêm phiên khối lượng lớn kèm giá giảm.
- **VIC** — Hưởng lợi câu chuyện nâng hạng FTSE có nguồn xác thực nhưng giá đã tăng +11,4%/tháng trước entry, vol_ratio yếu nhất toàn nhóm 5 mã (0.23) — rủi ro 'sell the news'.
  - *Huỷ luận điểm nếu:* Giá thủng MA50 rõ rệt, hoặc có thêm thông tin xấu về nhân sự cấp cao/pháp lý.

### 📅 Cần theo dõi tuần này
- GAS: xác minh nội dung tin 'vướng tiêu chuẩn công ty đại chúng' (chưa kiểm chứng); theo dõi vol_ratio có vượt 1 không
- GVR: theo dõi khối lượng để phân biệt tích lũy vs phân phối; xác nhận nguyên nhân gốc đợt giảm từ đỉnh 46.500đ
- VIC: theo dõi tiến độ giải ngân dòng vốn ngoại theo lộ trình FTSE (giai đoạn 1 chỉ 10%); theo dõi thêm lý do miễn nhiệm Phó Tổng Giám đốc
- KDH: theo dõi phản hồi/hậu quả từ văn bản UBCKNN số 9074, 9075 (14/9/2026)
- Toàn thị trường: dòng vốn ngoại sau ngày FTSE Russell nâng hạng có hiệu lực (21/9/2026)

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.356** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-24_05-01-06`. Chạy lại: skill `vn-swing-daily`.*
