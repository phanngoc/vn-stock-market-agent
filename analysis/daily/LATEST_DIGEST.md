# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-02 05:04 · dữ liệu giá as-of **2026-08-28** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Mô hình có edge yếu (AUC ~0.53-0.55) và cả 5 mã ứng viên đều có ít nhất một rủi ro chưa hóa giải (dữ liệu giá chưa kiểm chứng, downtrend kỹ thuật, pha loãng, rủi ro pháp lý, hoặc quy mô dòng vốn catalyst chưa xác nhận); ưu tiên bảo toàn vốn, không MUA mã nào lúc này, chỉ theo dõi 2 mã có setup tốt nhất chờ xác nhận thêm.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VRE** | TB | 25800-26100 (chờ xác nhận giữ trên MA50 kèm volume >1 trước khi vào) | 28,188 | 24,795 | 25 phiên | 0% hiện tại, tối đa 2-3% nếu có xác nhận |
| **VIC** | Thấp | chưa vào lệnh - cần xác minh giá thực tế trước (chênh lệch ~205,000-208,500 vs 236,000 theo signals) | 254,880 | 224,200 | 25 phiên | 0% hiện tại |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Rủi ro pháp lý/uy tín nghiêm trọng và mới xảy ra (vụ án hình sự tại công ty con, giá mất ~50% từ đỉnh, bị loạt CTCK siết margin) chưa được hóa giải; phiên hồi kỹ thuật gần đây nhiều khả năng là bull trap trong bối cảnh thanh khoản bị siết, không phải xác nhận ổn định nền tảng. |
| **PDR** | TB | Dưới MA50 với MA50 còn dốc xuống, volume yếu nhất nhóm (0.61) — đúng mẫu 'bắt dao rơi'; tín hiệu nội bộ Chủ tịch đăng ký mua tích cực nhưng bị át bởi rủi ro pha loãng cụ thể từ đợt phát hành 5:1 (~199.56 triệu cổ phiếu). |
| **KDH** | TB | Dưới MA50 với MA50 còn dốc xuống, volume dưới trung bình (0.84) — chưa có xác nhận kỹ thuật đảo chiều dù tin tức dự án (Gladia Heights, quỹ đất Mả Lạng/Chợ Gà-Gạo) tích cực; thêm rủi ro cung chưa kiểm chứng từ khả năng VinaCapital thoái vốn. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VRE** — Setup kỹ thuật sạch nhất nhóm (RSI còn dư địa, mới cắt lên MA50, volume xác nhận) cộng catalyst FTSE GEIS đã công bố chính thức (hiệu lực 21/9/2026); nhưng quy mô dòng vốn Small Cap thực tế chưa được xác nhận và catalyst có thể đã một phần phản ánh vào giá — bò và gấu cân bằng nên chưa đủ cơ sở MUA ngay, cần thêm xác nhận.
  - *Huỷ luận điểm nếu:* Giá thủng MA50 kèm volume lớn (dead-cat bounce thất bại); hoặc gần ngày 21/9/2026 mà không có dấu hiệu dòng vốn ETF thực tế đổ vào — cho thấy catalyst đã bị 'sell the news'.
- **VIC** — Điểm mô hình cao nhất nhóm và trend/volume tốt theo A, nhưng RSI 68.7 sát quá mua, TP đòi phá đỉnh 6 tháng, và có chênh lệch dữ liệu giá chưa kiểm chứng giữa signals_latest.csv và nguồn tin — rủi ro vận hành đủ lớn để không hành động cho tới khi xác minh.
  - *Huỷ luận điểm nếu:* Nếu xác minh giá thực tế lệch đáng kể so với 236,000đ thì toàn bộ entry/TP/SL trong bảng tín hiệu vô hiệu, cần tính lại; nếu RSI xác nhận phân kỳ giảm hoặc giá thủng MA20 thì loại bỏ luận điểm mua.

### 📅 Cần theo dõi tuần này
- VIC: xác minh giá giao dịch thực tế hiện nay — signals_latest.csv ghi 236,000đ (28/8) nhưng nguồn Simplize cho thấy vùng 205,000-208,500đ giữa/cuối tháng 8; không dùng entry/TP/SL của VIC cho tới khi đối chiếu xong
- VRE: theo dõi việc giá có giữ được trên MA50 kèm volume >1 khi tiến gần ngày FTSE GEIS hiệu lực phân bổ 21/9/2026, và tìm thêm thông tin quy mô dòng vốn ETF cụ thể phân bổ vào nhóm Small Cap
- PDR: kết quả đăng ký mua 20 triệu cổ phiếu của Chủ tịch Nguyễn Văn Đạt (đăng ký kết thúc 29/8/2026) — đã mua thực tế bao nhiêu, và tiến độ đợt phát hành 5:1 ~199.56 triệu cổ phiếu
- KDH: xác nhận hoặc bác bỏ thông tin VinaCapital tiếp tục thoái vốn xuống dưới 7%
- PNJ: diễn biến vụ án hình sự liên quan P-Lab và động thái các CTCK về margin PNJ — có nới lại hay siết thêm
- Toàn thị trường: dư nợ margin đang ở mức kỷ lục (~435,000 tỷ đồng cuối Q2/2026) — theo dõi rủi ro margin call diện rộng có thể khiến giá gap qua các mức SL đã tính

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.353** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ 3/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, rủi ro cao hơn kèo momentum.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-02_04-43-40`. Chạy lại: skill `vn-swing-daily`.*
