# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-08-28 02:25 · dữ liệu giá as-of **2026-08-27** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Hai ứng viên khả dĩ nhất (VIC, VRE) đều ở trạng thái bò≈gấu cân bằng, mô hình nền chỉ có edge yếu (AUC ~0,53-0,55), cộng rủi ro tương quan nhóm Vingroup và bất định vĩ mô (kỳ nghỉ lễ 2/9, Jackson Hole 27-29/8) khiến ưu tiên bảo toàn vốn hơn giải ngân mạnh.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 226000-230000 | 254,880 | 224,200 | 25 phiên | 2-3% |
| **VRE** | TB | 25500-26200 | 28,080 | 24,700 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PDR** | Cao | Rủi ro pha loãng cổ phiếu đã công bố cụ thể (~200 triệu cp dưới giá sổ sách) là headwind định lượng được, cộng kỹ thuật yếu (vol_ratio 0,76 dưới MA50) - nhịp hồi thiếu dòng tiền xác nhận. |
| **KDH** | Cao | Kỹ thuật yếu nhất nhóm (downtrend dai dẳng nhất, vol_ratio thấp nhất, dưới MA20/MA50), doanh thu lõi giảm gần 85% khiến chất lượng lợi nhuận công bố đáng ngờ - gần như bắt dao rơi điển hình. |
| **PNJ** | TB | Kỹ thuật yếu (dưới MA50 đang giảm, vol_ratio không xác nhận) và KQKD quý 2/2026 lỗ thật - hồi giá gần đây chủ yếu do tâm lý gỡ vướng pháp lý, chưa có bằng chứng nền tảng cải thiện. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Setup kỹ thuật + catalyst KQKD mạnh nhất nhóm, nhưng RSI cận 70 và khối lượng đỉnh lịch sử có thể là phân phối chứ không chỉ dòng tiền vào - chờ xác nhận thay vì mua đuổi.
  - *Huỷ luận điểm nếu:* Giá thủng MA20 kèm khối lượng lớn; RSI vượt 70 rồi đảo chiều giảm nhanh; nhóm Vingroup đồng loạt điều chỉnh mạnh.
- **VRE** — Tín hiệu cắt MA20/50 + catalyst cổ tức/Vincom Collection hợp lý nhưng còn mới, chưa kiểm chứng; catalyst tin tức thực ra đã cũ và tỷ lệ lấp đầy 88,1% là điểm yếu vận hành thật.
  - *Huỷ luận điểm nếu:* Giá rớt lại xuống dưới MA20/MA50 vừa cắt lên (bull trap); không có tin tức mới củng cố trong 2-3 tuần; VIC/nhóm Vingroup điều chỉnh mạnh kéo theo.

### 📅 Cần theo dõi tuần này
- VIC: diễn biến sau RSI 68,7 - lấp gap hay tiếp tục breakout kèm khối lượng
- VRE: giá có giữ được trên MA20/MA50 vừa cắt lên kèm khối lượng xác nhận không
- VN-Index kiểm định vùng kháng cự 1.800-1.810 điểm
- Hội nghị Jackson Hole 27-29/8/2026 - định hướng lãi suất Fed ảnh hưởng dòng vốn ngoại
- Kỳ nghỉ lễ Quốc khánh 2/9 (5 ngày) - thanh khoản có thể co lại
- FTSE Russell nâng hạng 21/9/2026 - danh sách 30 mã hưởng lợi cụ thể (chưa kiểm chứng VIC/VRE có nằm trong đó)
- PNJ: ĐHĐCĐ bất thường dự kiến tháng 10/2026 sau lỗ quý 2
- PDR: tiến độ phát hành ~200 triệu cổ phiếu giá dưới sổ sách
- Chính sách đất đai: Nghị định 281/2026/NĐ-CP hiệu lực 31/8/2026

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.352** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ 3/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, rủi ro cao hơn kèo momentum.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-08-28_02-05-58`. Chạy lại: skill `vn-swing-daily`.*
