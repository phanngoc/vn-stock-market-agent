# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of 2026-09-23

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là khung ra quyết định mô phỏng phục vụ nghiên cứu/giáo dục, dựa trên tranh luận nội bộ của các agent A/B/C/D. Quyết định đầu tư thật thuộc về người dùng, tự chịu trách nhiệm rủi ro. Mô hình định lượng nền tảng có **edge yếu (AUC ~0.53–0.55)** — chỉ nhỉnh hơn tung đồng xu một chút; mọi điểm số/thứ hạng trong báo cáo mang tính xác suất thấp, không chắc chắn. Số liệu tin tức/BCTC nào ghi "chưa kiểm chứng" thì KHÔNG được coi là sự thật đã xác nhận.

## 0. Bối cảnh ra quyết định

- Mô hình tốt nhất OOS: LogReg, base win-rate 0.356 ~ buy&hold kỳ kiểm định 0.3563 → **hầu như không có edge dự báo thật sự**, chốt lời +8%/cắt lỗ −5%/time-stop 25 phiên là khung quản trị rủi ro cố định, không phải "dự báo thắng".
- **Toàn bộ 5 mã ứng viên (PNJ, GAS, VIC, VRE, GVR) đều có vol_ratio < 1** (0.16–0.54) — không mã nào có xác nhận dòng tiền/thanh khoản cho xu hướng giá quan sát được. Đây là rủi ro chung, không riêng mã nào.
- Bối cảnh vĩ mô theo Agent B: thanh khoản khớp lệnh toàn thị trường phiên 22/9 giảm 23,4% (chỉ ~65% trung bình) trong khi VN-Index vẫn tăng nhờ nhóm trụ; **margin tăng +12,1% (5 phiên)/+13,32% (20 phiên)** — tổ hợp đòn bẩy cao + thanh khoản mỏng là rủi ro cổ điển nếu thị trường điều chỉnh, có thể khiến lệnh cắt lỗ "nhảy cóc" qua ngưỡng −5% dự kiến.
- Bò (Agent C) và Gấu (Agent D) đưa ra bằng chứng có sức nặng gần tương đương ở GAS/VIC/VRE — không mã nào có luận điểm bò áp đảo tuyệt đối luận điểm gấu. Theo nguyên tắc bảo toàn vốn khi bò≈gấu, quyết định mặc định là **THEO DÕI**, không MUA bừa.

## 1. Bảng quyết định theo mã

| Mã | Quyết định | Độ tin cậy | Lý do quyết định |
|---|---|---|---|
| **GAS** | THEO DÕI | TB | Bò mạnh nhất nhóm (KQKD vượt 129% kế hoạch, cổ tức tiền mặt 25% xác nhận, kỹ thuật đẹp nhất) nhưng vol_ratio chỉ 0.29 và giá tham chiếu điều chỉnh kỹ thuật đúng ngày 23/9 (ex-date) — cần đợi xác nhận thanh khoản trước khi vào thật. |
| **VIC** | THEO DÕI | TB | Catalyst FTSE xác nhận + lực kéo chỉ số là có thật, nhưng vol_ratio thấp nhất toàn bảng (0.16) gợi ý rủi ro "mua theo tin đồn, bán theo tin chính thức" (giá đã +79% từ đáy trước khi tin có hiệu lực), cộng đính chính BCTC chưa rõ mức độ trọng yếu và đòn bẩy trái phiếu VinFast 10.000 tỷ chưa định lượng được — chưa đủ cơ sở để MUA. |
| **VRE** | THEO DÕI | Thấp | Định giá rẻ (P/B ~1,3x so với TB 8 năm ~1,9x) và không có tin xấu là điểm cộng, nhưng chính Agent C thừa nhận đây là "suy luận thuần túy", MA20/50 mới hội tụ chưa breakout xác nhận, vol_ratio 0.20 — mua ở đây gần với đoán đáy, cần chờ xác nhận kỹ thuật rõ hơn. |
| **GVR** | THEO DÕI | Thấp | Rủi ro pháp lý cũ (nguy cơ huỷ tư cách đại chúng) đã được hoá giải là tin tích cực, nhưng không có catalyst mới cụ thể trong tháng 9, giá đang tích luỹ đi ngang hơn là breakout, thiếu bằng chứng cả bò lẫn gấu đủ mạnh để nghiêng hẳn về một phía — bằng chứng quá mỏng để hành động. |
| **PNJ** | TRÁNH | Cao | Rủi ro tin tức nghiêm trọng nhất nhóm: gia đình Chủ tịch đã bán ròng 25 triệu cổ phiếu (thu ~259 tỷ từ riêng 7 triệu cp), dùng tiền cho chính công ty vay, cộng nghi vấn lợi nhuận giảm 38% sau soát xét (**chưa kiểm chứng đầy đủ qua BCTC chính thức**) — kết hợp kỹ thuật vẫn dưới MA50 trong downtrend dài hạn. Dù có score mô hình cao nhất (0.5693), đây chính là ví dụ điển hình tin tức tiêu cực có thể vô hiệu hoá tín hiệu mô hình yếu. |

## 2. Kế hoạch giao dịch (chỉ áp dụng nếu điều kiện xác nhận xảy ra — hiện tại là THEO DÕI, chưa giải ngân)

### GAS — THEO DÕI (TB)
- **Vùng entry theo dõi:** 85.700–87.000đ, **chỉ cân nhắc giải ngân thật nếu vol_ratio phục hồi rõ (ước lượng >0.5) trong 3–5 phiên sau ngày GDKHQ 23/9/2026** và giá giữ được trên MA20.
- **Chốt lời (+8%):** 92.880đ (lưu ý: sát vùng kháng cự đỉnh cũ tháng 4-5 ~95k — dư địa lời có thể hẹp hơn 8% nếu kháng cự giữ).
- **Cắt lỗ (−5%):** 81.700đ.
- **Time-stop:** 25 phiên (~5 tuần).
- **Cỡ vị thế đề xuất (nếu kích hoạt):** 2–3% danh mục — thận trọng do rủi ro thanh khoản chưa xác nhận.
- **Điều kiện huỷ luận điểm:** vol_ratio không cải thiện sau ex-date, hoặc giá thủng 81.700đ, hoặc xuất hiện tin xấu bất ngờ về hoạt động kinh doanh/giá dầu khí.

### VIC — THEO DÕI (TB)
- **Vùng entry theo dõi:** 238.000–243.000đ, **chỉ cân nhắc nếu**: (1) thanh khoản cải thiện rõ so với mức 0.16 hiện tại, (2) không có thông tin xấu mới từ đợt đính chính BCTC soát xét, (3) giá không có dấu hiệu "sell-the-news" (giảm mạnh kèm khối lượng lớn) ngay sau đợt nâng hạng FTSE có hiệu lực 21/9.
- **Chốt lời (+8%):** 260.712đ (sát đỉnh gần nhất ~265k — dư địa hẹp).
- **Cắt lỗ (−5%):** 229.330đ (lưu ý biên độ tuyệt đối lớn ~12.000đ/cp, rủi ro gap qua SL trong phiên biến động ±7%).
- **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu kích hoạt):** 2–3% danh mục.
- **Điều kiện huỷ luận điểm:** đính chính BCTC hé lộ vấn đề trọng yếu, giá giảm mạnh kèm thanh khoản tăng ngay sau 21-23/9 (dấu hiệu sell-the-news), hoặc tin xấu mới về đòn bẩy nhóm Vingroup/VinFast.

### VRE — THEO DÕI (Thấp)
- **Vùng entry theo dõi:** 24.800–25.500đ, **chỉ cân nhắc nếu** MA20 cắt lên MA50 rõ ràng kèm vol_ratio tăng vượt mức hiện tại (0.20), xác nhận breakout thay vì "chạm rồi lùi".
- **Chốt lời (+8%):** 27.162đ (trùng vùng kháng cự đỉnh tháng 8 — cần khối lượng để vượt qua).
- **Cắt lỗ (−5%):** 23.892đ.
- **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu kích hoạt):** 2% danh mục — độ tin cậy thấp nên cỡ vị thế nhỏ hơn GAS/VIC.
- **Điều kiện huỷ luận điểm:** giá quay lại dưới đáy gần nhất của vùng tích luỹ, hoặc không có xác nhận breakout trong 1–2 tuần tới.

### GVR — THEO DÕI (Thấp)
- **Vùng entry theo dõi:** 31.800–32.600đ, **chỉ cân nhắc nếu** xuất hiện catalyst cụ thể mới (KQKD quý, tin tức xác nhận) và giá breakout khỏi vùng tích luỹ 31–34k kèm khối lượng tăng.
- **Chốt lời (+8%):** 34.992đ (sát biên trên vùng dao động gần đây — dư địa hẹp).
- **Cắt lỗ (−5%):** 30.780đ.
- **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu kích hoạt):** 2% danh mục.
- **Điều kiện huỷ luận điểm:** không có catalyst/KQKD mới trong 4 tuần tới và giá phá vỡ đáy vùng tích luỹ (dưới ~31k).

### PNJ — TRÁNH
- Không lập kế hoạch giao dịch. Chỉ xem xét lại nếu: BCTC quý 3 chính thức (dự kiến 26/10/2026) phủ nhận rõ ràng nghi vấn lợi nhuận giảm 38%, VÀ giá phục hồi rõ ràng lên trên MA50 với khối lượng xác nhận.

## 3. Stance tổng danh mục

**Thận trọng (Cautious).** Không có mã nào trong nhóm ứng viên đủ điều kiện MUA ngay lúc này: mô hình định lượng có edge yếu, toàn bộ 5 mã đều thiếu xác nhận thanh khoản (vol_ratio <1), và bối cảnh vĩ mô cho thấy thanh khoản thị trường suy yếu trong khi margin tăng — tổ hợp rủi ro cổ điển trước một đợt điều chỉnh. Ưu tiên bảo toàn vốn: giữ tỷ trọng tiền mặt cao, chỉ giải ngân nhỏ (2–3%/mã) và có điều kiện rõ ràng khi các mã THEO DÕI có xác nhận thêm (thanh khoản, tin tức, kỹ thuật). Tuyệt đối tránh PNJ do rủi ro tin tức nội bộ cụ thể và đã được xác thực một phần (giao dịch bán của người liên quan là sự kiện đã xảy ra).

## 4. Cần theo dõi tuần tới

- **GAS**: diễn biến vol_ratio và giá tham chiếu ngay sau ngày GDKHQ cổ tức 23/9/2026 (hôm nay) — đây là phép thử trực tiếp cho luận điểm bò/gấu.
- **VIC**: nội dung cụ thể của đính chính BCTC hợp nhất soát xét (công bố 4/9, chưa rõ mức độ trọng yếu); phản ứng giá/thanh khoản trong 1–2 tuần sau ngày nâng hạng FTSE chính thức có hiệu lực (21/9) để phân biệt "dòng vốn thật" hay "sell-the-news"; tiến độ phát hành 10.000 tỷ trái phiếu cho VinFast vay.
- **VRE**: xác nhận MA20/50 cắt lên kèm khối lượng tăng; kiểm chứng lại số liệu KQKD 9 tháng (80,6% kế hoạch) qua BCTC chính thức — nguồn hiện tại chưa xác định rõ.
- **GVR**: KQKD quý gần nhất (chưa có dữ liệu trong phạm vi tìm kiếm) và bất kỳ catalyst cụ thể mới nào.
- **PNJ**: BCTC quý 3 dự kiến 26/10/2026 — kiểm chứng nghi vấn lợi nhuận giảm 38% sau soát xét.
- **Toàn thị trường**: xu hướng thanh khoản khớp lệnh (đang suy yếu) và tốc độ tăng margin — nếu cả hai tiếp tục cùng chiều (margin tăng, thanh khoản giảm), rủi ro điều chỉnh mạnh tăng lên, cần siết chặt kỷ luật cắt lỗ hơn nữa cho mọi vị thế đang mở.
