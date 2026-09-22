# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-22 05:25 · dữ liệu giá as-of **2026-09-22** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Toàn bộ 5 mã ứng viên đều có vol_ratio dưới 1 (chưa xác nhận dòng tiền) và mô hình có edge rất yếu (AUC ~0.53-0.55), nên ưu tiên bảo toàn vốn thay vì giải ngân mới.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 230000-240000 | 259,200 | 228,000 | 25 phiên | 0-2% |
| **GAS** | TB | 82000-85200 | 92,016 | 80,940 | 25 phiên | 0-2% |
| **VRE** | TB | 25000-25500 | 27,000 | 23,750 | 25 phiên | 0-3% |
| **GVR** | Thấp | 30700-32350 | 34,938 | 30,732 | 25 phiên | 0-1% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Insider bán 25 triệu cp (gia đình Chủ tịch) và giá vẫn dưới MA50 sau downtrend 6 tháng, không có luận điểm bò đủ mạnh để đối trọng dù score mô hình cao nhất nhóm. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Trend kỹ thuật đẹp nhất nhóm và có catalyst FTSE Large Cap, nhưng vol_ratio thấp nhất nhóm (0.091) sau khi giá đã tăng khoảng 60%/tháng nên rủi ro điều chỉnh cao, chưa đủ cơ sở MUA.
  - *Huỷ luận điểm nếu:* Xuất hiện phiên bán mạnh có volume cao (chốt lời) hoặc giá thủng MA20 kèm volume tăng theo hướng giảm.
- **GAS** — KQKD 8 tháng vượt 129% kế hoạch lợi nhuận cả năm là catalyst cơ bản mạnh nhất nhóm, nhưng GDKHQ cổ tức tiền mặt đúng ngày as-of tạo rủi ro thực thi cụ thể cho entry/TP/SL và TP trùng kháng cự đỉnh cũ tháng 8.
  - *Huỷ luận điểm nếu:* Giá không vượt được kháng cự ~92.000đ sau vài lần thử, hoặc tin tức xác nhận tăng trưởng lợi nhuận chậm lại quý tới.
- **VRE** — Kèo cân bằng nhất nhóm: KQKD đúng tiến độ, FTSE Small Cap, không có tin xấu đáng kể; nhưng cú cắt lên MA50 còn non và thiếu xác nhận volume (vol_ratio 0.236), TP trùng kháng cự cũ nên chưa đủ cơ sở MUA ngay.
  - *Huỷ luận điểm nếu:* Giá đóng cửa dưới 24.000đ (phá lại vùng giằng co cũ) hoặc KQKD quý tới không đạt kế hoạch.
- **GVR** — Lợi nhuận quý 2 tăng 58% svck (cao nhất 5 năm) và R:R kỹ thuật cân đối nhất nhóm, nhưng có thể đến từ khoản một lần (thanh lý gỗ cao su, đền bù đất) và thông tin kế hoạch lợi nhuận cả năm còn trái chiều chưa kiểm chứng.
  - *Huỷ luận điểm nếu:* Xác nhận kế hoạch lợi nhuận 2026 đi lùi là chính xác, hoặc giá phá vỡ đáy range 26.000đ.

### 📅 Cần theo dõi tuần này
- GAS: phản ứng giá quanh GDKHQ cổ tức tiền mặt 22/9/2026 và ĐKCC 23/9/2026, xem điều chỉnh giá cơ học ~2.500đ/cp có bị hiểu nhầm thành tín hiệu bán
- VRE: vol_ratio có vượt rõ rệt trên 1 để xác nhận cú cắt lên MA50, hay quay lại vùng giằng co 24.000đ (false breakout)
- VIC/VRE: dòng vốn ngoại thực tế từ hiệu lực phân bổ FTSE 21/9/2026 so với ước tính 150-250 triệu USD của Agriseco
- PNJ: tiến độ bán ra phần còn lại trong 25 triệu cp của gia đình Chủ tịch, và xác nhận/bác bỏ tin lợi nhuận giảm 38% sau soát xét (chưa kiểm chứng)
- GVR: làm rõ thông tin trái chiều về kế hoạch lợi nhuận cả năm 2026 (đi lùi hay tăng trưởng)
- Toàn thị trường: VN-Index quanh 1.840 điểm và dư nợ margin ước tính vượt 10 tỷ USD

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.356** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-22_05-07-25`. Chạy lại: skill `vn-swing-daily`.*
