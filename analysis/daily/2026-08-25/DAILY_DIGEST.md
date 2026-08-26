# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-08-26 10:12 · dữ liệu giá as-of **2026-08-25** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Edge mô hình ~coin-flip (AUC 0,53-0,55), rổ ứng viên tập trung ngành cực đoan (4 BĐS + 1 Chứng khoán = một cược vĩ mô), VN-Index áp sát kháng cự mạnh 1.800 và khối ngoại chưa ổn định. Ưu tiên bảo toàn vốn: giữ tiền mặt cao, không giải ngân trước xác nhận.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 210000-218000 | 241,704 | 212,610 | 25 phiên | 2-3% |
| **VRE** | TB | 25700-26200 | 27,540 | 24,225 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **KDH** | Cao | Bắt dao rơi kinh điển: kỹ thuật tệ nhất (3,5/10, downtrend, MA50 dốc xuống chặn ngay TP), lợi nhuận Q2 ảo từ thoái vốn, bán nhà -85%, dòng tiền KD 6 tháng âm >1.480 tỷ, không có catalyst FTSE. |
| **PDR** | Cao | Volume yếu nhất bảng (0,43), còn xa dưới MA50, TP nằm trên MA50 (phải phá kháng cự mới tới đích); chi 7.666 tỷ thương vụ Lotte gây áp lực dòng tiền, bán BĐS chỉ ~2 tỷ, ngoài rổ FTSE - thiếu catalyst ngắn hạn. |
| **VCI** | TB | Chỉ là beta thuần vào catalyst FTSE với nền cơ bản xấu nhất (tự doanh lỗ, thu nhập toàn diện âm 432 tỷ, mới đạt 29% kế hoạch); margin kỷ lục là rủi ro hệ thống nếu index bị chặn ở 1.800 gây giải chấp. Dưới MA50, 2 cây quyết định bearish. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Setup kỹ thuật đẹp nhất (trên MA50, vol>1) và catalyst FTSE Large Cap mạnh nhất, nhưng mua ở giá hiện tại là đuổi sau nhịp +60%/tháng và TP đụng kháng cự đỉnh cũ; chờ chỉnh về nền tích lũy thay vì đuổi.
  - *Huỷ luận điểm nếu:* Ngày GDKHQ phát hành cổ phiếu trả cổ tức/thưởng rơi trong khung 25 phiên (rủi ro pha loãng); mất nền MA50 (~213-215k) kèm volume bán lớn; VN-Index bị đẩy lùi mạnh khỏi 1.800.
- **VRE** — Cơ bản vững nhất nhóm (Q1 lãi kỷ lục, FTSE Small Cap, cổ tức tiền mặt 10%) nhưng đang dưới MA50 với volume yếu (0,71); chỉ vào khi đóng cửa vững trên MA50 kèm volume tăng.
  - *Huỷ luận điểm nếu:* Bị đẩy ngược xuống dưới MA20 sau khi test MA50 thất bại; volume tiếp tục èo uột (<1) khi tiếp cận kháng cự; GDKHQ cổ tức rơi bất lợi trong khung.

### 📅 Cần theo dõi tuần này
- VRE: đóng cửa vững trên MA50 (~25.700) kèm volume tăng = mốc xác nhận
- VIC: nhịp chỉnh về nền 210-218k; ngày GDKHQ phát hành cổ phiếu trả cổ tức/thưởng (HOSE/VSD - chưa kiểm chứng)
- VN-Index phản ứng tại kháng cự mạnh 1.800 (hiện ~1.768)
- Khối ngoại mua/bán ròng - dòng vốn chưa ổn định
- Mốc 21/9 FTSE hiệu lực đợt 1: cảnh giác kịch bản mua tin đồn bán sự thật
- VRE: ngày GDKHQ cổ tức tiền mặt 10% (chưa kiểm chứng)

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LSTM** · base win-rate **0.352** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ 4/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, rủi ro cao hơn kèo momentum.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-08-26_09-00-48`. Chạy lại: skill `vn-swing-daily`.*
