# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of 2026-08-28

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là khung ra quyết định mô phỏng phục vụ nghiên cứu/giáo dục dựa trên mô hình quant có **edge yếu (AUC ~0.53–0.55)** kết hợp phân tích kỹ thuật + tin tức + tranh luận đa tác nhân. Quyết định đầu tư thật là trách nhiệm của người dùng, sau khi tự thẩm định và chịu rủi ro của chính mình.

*Giám đốc Chiến lược (Agent E) tổng hợp toàn bộ whiteboard: bằng chứng Agent A (kỹ thuật) + Agent B (news/cơ bản), luận điểm bò Agent C, phản biện gấu Agent D, và dữ liệu `signals_latest.csv`.*

---

## Nguyên tắc ra quyết định

1. **Bảo toàn vốn là ưu tiên số 1.** Mô hình nền chỉ nhỉnh hơn tung đồng xu (AUC ~0.53–0.55); các model con trong ensemble (`GradBoost`, `XGBoost`) đều **không đồng thuận** với điểm tổng ở cả 5 mã ứng viên — điểm số bị kéo lên chủ yếu bởi một model LSTM lạc quan bất thường. Không nên đọc điểm tổng hợp như một xác suất đáng tin.
2. **Khi lập luận bò và gấu cân bằng nhau → mặc định THEO DÕI**, không MUA để "cho chắc". Chỉ MUA khi bằng chứng kỹ thuật + tin tức + rủi ro đã được cân đối rõ ràng nghiêng về một phía và không bị phản biện hợp lý nào của Agent D làm lung lay.
3. **Mã dưới MA50 (PDR, KDH, PNJ theo Agent A) mang rủi ro "bắt dao rơi" cao hơn** — cần bằng chứng tin tức/kỹ thuật mạnh hơn hẳn để bù đắp; trong phiên này, không mã nào dưới MA50 hội đủ điều kiện đó sau khi cân bằng phản biện của Agent D.
4. **4/5 mã ứng viên cùng ngành RealEstate (VIC, PDR, KDH, VRE)** — rủi ro chính sách room tín dụng BĐS 2026 (Agent B) là rủi ro hệ thống dùng chung, làm giảm tác dụng đa dạng hóa nếu chọn nhiều hơn 1 mã nhóm này.

---

## Bảng quyết định theo mã

| Mã | Quyết định | Độ tin cậy | Lý do quyết định |
|---|---|---|---|
| **VIC** | 🟡 THEO DÕI | TB | KQKD xuất sắc (+73% DT, LNST x4.5) và trend kỹ thuật tốt, nhưng **catalyst đã phản ánh vào giá** (mua sau khi lập ATH), RSI 68,7 sát quá mua, **không có catalyst mới** trong suốt 25 phiên nắm giữ (KQKD quý tới 30/10 nằm ngoài time-stop), và model con GradBoost gần như tung đồng xu (0.5043). Bò≈gấu → theo dõi chờ nhịp điều chỉnh rõ ràng hơn thay vì đuổi giá đỉnh lịch sử. |
| **PDR** | 🔴 TRÁNH | Cao | Dưới MA50, RSI trung tính không xác nhận đảo chiều, volume yếu (0.61) — không có dòng tiền xác nhận. Tin Chủ tịch mua vào 20 triệu cp là tích cực nhưng bị lấn át bởi giá giảm 40,6%/năm, phát ngôn tiêu cực tại ĐHĐCĐ, và áp lực dòng tiền ra lớn (7.666 tỷ cho thương vụ Lotte). Đồng thuận A+B+C+D đều xếp đây là kèo yếu nhất/rủi ro nhất. |
| **KDH** | 🔴 TRÁNH | Cao | Dưới MA50, volume dưới trung bình, không có tín hiệu kỹ thuật đảo chiều. Dòng tiền kinh doanh âm 634 tỷ và rủi ro bị loại khỏi rổ VNDiamond (dù "chưa kiểm chứng đầy đủ") là các cờ đỏ chưa được bù đắp đủ bởi tin mở rộng quỹ dự án. |
| **PNJ** | 🔴 TRÁNH | TB | Điểm kỹ thuật yếu nhất nhóm (4.0/10, dưới MA50, volume 0.65). Catalyst minh oan pháp lý + Vanguard mua vào là tin thật và tích cực, nhưng **giá tham chiếu hiện tại (42.100đ) đã cao hơn ~5,5% so với đỉnh phiên tăng trần** (39.900đ ngày 21/8) — phần lớn phần thưởng của catalyst nhiều khả năng đã được hấp thụ trước khi vào lệnh. SL nằm sát một vùng hỗ trợ chỉ mang tính tâm lý, chưa được kỹ thuật xác nhận; dư âm rủi ro pháp lý liên đới (công ty giám định con) chưa đóng hẳn. Khi kỹ thuật và tin tức mâu thuẫn ở khung thời gian ngắn (25 phiên), ưu tiên tín hiệu dòng tiền (kỹ thuật) hơn tin tức đã công khai. |
| **VRE** | 🟡 THEO DÕI | TB | Setup kỹ thuật tốt nhất nhóm (7.0/10, trên MA50, volume 1.44, RSI còn dư địa) + catalyst cụ thể hiếm gặp (cổ tức tiền mặt 10% lần đầu sau 7 năm) + tài chính lành mạnh. Nhưng biến động cực đoan hai chiều (tuần +11,21%/tháng −13,83%/năm −12,75%) khiến nhịp tăng tuần qua có thể là hồi kỹ thuật ngắn chưa xác nhận đảo chiều bền vững; 2/5 model con (GradBoost 0.40, XGBoost 0.44) dự báo dưới 50% — ensemble không đồng thuận. Đây là kèo cân bằng nhất giữa bò và gấu trong nhóm → theo dõi thêm 1 nhịp xác nhận trước khi giải ngân.

---

## Kế hoạch giao dịch (áp dụng cho VIC, VRE — mã THEO DÕI, chỉ kích hoạt nếu điều kiện xác nhận thêm xuất hiện; PDR/KDH/PNJ: TRÁNH, không có kế hoạch vào lệnh)

### VIC (THEO DÕI)
- **Vùng entry đề xuất nếu xác nhận thêm:** 228.000–233.000đ (ưu tiên chờ nhịp điều chỉnh nhả bớt RSI khỏi vùng 68–70, không đuổi mua tại đỉnh lịch sử 236.000đ).
- **Chốt lời +8%:** 254.880đ (tính trên giá tham chiếu 236.000đ, theo `signals_latest.csv`).
- **Cắt lỗ −5%:** 224.200đ.
- **Time-stop:** 25 phiên (~5 tuần).
- **Cỡ vị thế đề xuất:** 2–3% danh mục (thận trọng do RSI cận biên quá mua + rủi ro tập trung vì VIC chiếm >20% vốn hóa HoSE).
- **Điều kiện hủy luận điểm (invalidation):** giá đóng cửa dưới MA50 hoặc dưới 224.200đ trước khi vào lệnh; RSI không hạ nhiệt mà tiếp tục leo qua 72–75 kèm volume giảm dần (dấu hiệu đuối sức); xuất hiện tin tiêu cực bất ngờ (pháp lý/quản trị) làm gãy câu chuyện KQKD.

### VRE (THEO DÕI)
- **Vùng entry đề xuất nếu xác nhận thêm:** 25.500–26.100đ (vùng giá hiện tại; chờ 1–2 phiên xác nhận giữ trên MA50 sau nhịp tăng mạnh tuần qua, tránh mua đuổi ngay sau phiên +11,21%/tuần).
- **Chốt lời +8%:** 28.188đ (trên giá tham chiếu 26.100đ).
- **Cắt lỗ −5%:** 24.795đ.
- **Time-stop:** 25 phiên (~5 tuần).
- **Cỡ vị thế đề xuất:** 2–3% danh mục (thận trọng do biến động lịch sử cực đoan + ensemble model không đồng thuận).
- **Điều kiện hủy luận điểm (invalidation):** giá đóng cửa rơi lại dưới MA50 hoặc dưới 24.795đ; nhịp tăng tuần qua thoái lui >50% trong vài phiên tới (dấu hiệu dead-cat bounce như Agent D cảnh báo); tin tức xấu mới về ngành bán lẻ/BĐS thương mại hoặc room tín dụng ảnh hưởng trực tiếp đến VRE.

### PDR, KDH, PNJ — TRÁNH
- Không đề xuất vùng entry / cỡ vị thế (0%).
- Mức TP/SL trong `decision.json` chỉ mang tính **tham chiếu thông tin** (lấy nguyên từ `signals_latest.csv`), không phải kế hoạch giao dịch đang khuyến nghị.
- **Điều kiện để xem xét lại:** PDR/KDH cần giá đóng cửa vượt lại MA50 kèm volume >1 và không còn tin tiêu cực mới về dòng tiền/room tín dụng; PNJ cần volume xác nhận vượt MA50 và kết luận cuối cùng (không còn tố tụng phát sinh) về vụ án liên đới.

---

## Stance tổng danh mục

**Thận trọng.** 3/5 mã ứng viên (PDR, KDH, PNJ) bị loại vì thiếu xác nhận kỹ thuật và/hoặc rủi ro tin tức/dòng tiền chưa được bù đắp đủ. 2 mã còn lại (VIC, VRE) có luận điểm bò tương đối mạnh nhưng đều bị phản biện hợp lý của Agent D làm cân bằng lại (catalyst đã phản ánh vào giá, RSI cận biên, ensemble model không đồng thuận, biến động lịch sử cực đoan) — chưa đủ để chuyển từ THEO DÕI sang MUA. Toàn bộ 4/5 mã ứng viên cùng ngành RealEstate khiến rủi ro chính sách room tín dụng BĐS 2026 là rủi ro hệ thống chung, không nên xem các vị thế này là độc lập/đa dạng hóa lẫn nhau. **Phân bổ gợi ý lúc này: giữ tỷ trọng tiền mặt cao; nếu có giải ngân, giới hạn tổng exposure vào nhóm RealEstate/BĐS (VIC + VRE nếu xác nhận) ở mức thận trọng (tổng ≤5% danh mục), không giải ngân vào PDR/KDH/PNJ ở thời điểm này.**

---

## Cần theo dõi tuần tới

1. **VIC:** phản ứng giá quanh vùng 228.000–236.000đ; RSI có hạ nhiệt về dưới 65 không; tín hiệu chốt lời sau ATH có lan rộng ra nhóm vốn hóa lớn không.
2. **VRE:** độ bền của nhịp tăng tuần qua (+11,21%) — có giữ trên MA50 hay thoái lui mạnh (dấu hiệu dead-cat bounce).
3. **FTSE Russell nâng hạng:** hiệu lực từ 21/9/2026, giai đoạn giải ngân đầu tiên (10% trong tổng ~1,5 tỷ USD) — theo dõi dòng vốn ETF thụ động có thực sự chảy vào nhóm vốn hóa lớn (VIC, VRE) hay không.
4. **KDH:** thông báo chính thức (nếu có) về khả năng bị loại khỏi rổ VNDiamond kỳ review Q2/2026.
5. **PNJ:** diễn biến tố tụng vụ kim cương liên quan công ty giám định con; nội dung họp ĐHĐCĐ bất thường dự kiến tháng 10/2026.
6. **Chính sách room tín dụng BĐS 2026:** văn bản/tín hiệu tiếp theo từ NHNN có thể ảnh hưởng đồng thời cả nhóm RealEstate (VIC, PDR, KDH, VRE).

---

*Đây KHÔNG PHẢI khuyến nghị đầu tư. Mô hình quant nền có edge yếu (AUC ~0.53–0.55); mọi quyết định trên là khung phân tích mô phỏng dựa trên tranh luận đa tác nhân, không thay thế cho thẩm định độc lập và quản trị rủi ro cá nhân.*
