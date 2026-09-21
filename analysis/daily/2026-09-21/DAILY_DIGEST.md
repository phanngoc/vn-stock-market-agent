# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-21 05:23 · dữ liệu giá as-of **2026-09-21** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Edge mô hình yếu (AUC ~0.53-0.55) và toàn bộ 5 mã ứng viên đều vol_ratio dưới 1 (0.15-0.33) khiến tín hiệu kỹ thuật kém tin cậy; ưu tiên bảo toàn vốn, chỉ theo dõi thay vì giải ngân mạnh.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VRE** | TB | 24800-25400 | 27,162 | 23,892 | 25 phiên | 2-3% |
| **GVR** | TB | 31800-32500 | 34,668 | 30,495 | 25 phiên | 2% |
| **GAS** | TB | 86000-87500 | 96,228 | 84,645 | 25 phiên | 2% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Score mô hình cao nhất nhóm nhưng đang dưới MA50 với vol_ratio thấp nhất nhóm (0.16) — đúng dạng bắt dao rơi, kỹ thuật tệ nhất nhóm. |
| **VIC** | TB | Không được chọn làm kèo bò; vol_ratio thấp nhất nhóm cùng PNJ (0.15) và có tin điều chỉnh BCTC hợp nhất giữa niên độ chưa kiểm chứng mức độ trọng yếu. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VRE** — Setup kỹ thuật cân bằng nhất nhóm (trend tăng, RSI trung tính) và catalyst tăng trưởng 2026 + cổ tức 10%, nhưng vol_ratio 0.33 vẫn là thanh khoản yếu và catalyst đã công bố từ trước nên có thể đã phần nào phản ánh vào giá.
  - *Huỷ luận điểm nếu:* Vol_ratio không cải thiện lên gần 1.0 trong 5-7 phiên; giá thủng vùng 24.000d; VN-Index mất vùng hỗ trợ 1.760-1.780 điểm.
- **GVR** — Setup kỹ thuật ổn (trend tăng, RSI chưa quá mua) và câu chuyện chuyển đổi đất KCN dài hạn tích cực, nhưng tự thừa nhận thiếu catalyst ngắn hạn trong khung 25 phiên.
  - *Huỷ luận điểm nếu:* Giá đi ngang không tiến triển 10-15 phiên đầu mà không có tin tiến độ KCN/GPMB mới; RSI giảm dưới 45 kèm mất trend tăng.
- **GAS** — KQKD 8 tháng vượt 129% kế hoạch năm là nền tảng mạnh nhất nhóm, nhưng GDKHQ cổ tức rơi đúng ngày mai (22/9) gây điều chỉnh giá cơ học và RSI 63 là cao nhất nhóm, dư địa tăng hẹp nhất.
  - *Huỷ luận điểm nếu:* Giá không lấp khoảng điều chỉnh cổ tức trong 3-5 phiên sau 22/9; RSI tiếp tục neo trên 65-70 mà không hạ nhiệt.

### 📅 Cần theo dõi tuần này
- GAS: phiên GDKHQ cổ tức 22/9/2026 (2.500d/CP) - theo doi gia co lap lai khoang dieu chinh co hoc hay khong
- Dong von nang hang FTSE Russell hieu luc tu 21/9/2026, giai ngan theo 4 giai doan - theo doi dong tien khoi ngoai vao nhom von hoa lon, can trong hieu ung sell the news
- VN-Index: vung ho tro 1.760-1.780 diem va rui ro he thong tu margin toan thi truong tiep tuc phinh to
- Vol_ratio cua VRE/GVR/GAS can cai thien ro ret len gan 1.0 truoc khi can nhac giai ngan them
- VIC: cho lam ro noi dung dieu chinh BCTC hop nhat giua nien do cong bo 4/9/2026 (chua kiem chung muc do trong yeu)
- PNJ: cho KQKD quy 3/2026 (chua cong bo) de danh gia lai ky vong bien loi nhuan gop 2026
- Ngay GDKHQ co the co tuc tien mat 10% cua VRE - chua xac dinh duoc, can theo doi cong bo HOSE

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.356** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-21_05-06-22`. Chạy lại: skill `vn-swing-daily`.*
