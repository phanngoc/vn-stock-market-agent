# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of 2026-09-14

**RUN_DIR:** `log_run_2026-09-14_05-05-12`

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là khung ra quyết định mô phỏng cho mục đích nghiên cứu/giáo dục, tổng hợp từ tranh luận nội bộ 4 agent (A kỹ thuật, B news, C bò, D gấu) dựa trên mô hình định lượng có **edge YẾU (AUC ~0.53–0.55)** — chỉ nhỉnh hơn tung đồng xu một chút. Quyết định giao dịch thật thuộc về người dùng, cần tự thẩm định và chịu trách nhiệm rủi ro của mình.

## Nguyên tắc ra quyết định

Vì mô hình có edge yếu và chênh lệch điểm giữa các mã (0.53–0.58) nằm trong biên độ nhiễu thống kê, quyết định **ưu tiên bảo toàn vốn**. Khi lập luận bò (Agent C) và gấu (Agent D) có sức nặng tương đương cho một mã — tức không bên nào áp đảo rõ ràng — mặc định là **THEO DÕI**, không MUA. Chỉ những mã có luận điểm gấu áp đảo rõ ràng (kỹ thuật xấu + không có phản biện bò thuyết phục) mới bị xếp **TRÁNH**.

Không có mã nào trong 5 ứng viên đủ điều kiện **MUA** ở thời điểm này — xem lý do từng mã bên dưới.

---

## Bảng quyết định theo mã

| Mã | Quyết định | Độ tin cậy | Lý do quyết định |
|---|---|---|---|
| **VIC** | THEO DÕI | Thấp | Bò: điểm ensemble cao nhất + LNST +360,5% svck + catalyst FTSE large-cap 21/9. Gấu: vol_ratio 0.189 — **thấp nhất trong toàn bộ 30 mã**, mô hình con bất đồng mạnh (LSTM 0.807 kéo điểm lên trong khi GradBoost/XGBoost <0.45), vừa giảm -4,3% ngay trước tín hiệu, rủi ro bán ròng cơ cấu ETF frontier trước 21/9. Bò/gấu cân bằng nhưng bằng chứng thanh khoản yếu nhất nhóm là tín hiệu cụ thể, không thể bỏ qua → chờ xác nhận volume. |
| **GAS** | THEO DÕI | TB | Setup kỹ thuật tốt nhất nhóm (uptrend ổn định, RSI chưa quá mua, vol_ratio cao nhất — dù vẫn <1) + cổ tức tiền mặt 25% đang chi trả thực. Nhưng ĐHĐCĐ **bất thường** diễn ra đúng ngày phát tín hiệu (14/9) với nội dung hoàn toàn chưa biết, trong bối cảnh rủi ro pháp lý cơ cấu cổ đông (Nhà nước 96,8%+ phải thoái vốn) — rủi ro sự kiện nhị phân chưa định giá. Chờ công bố nội dung ĐHĐCĐ trước khi cân nhắc entry. |
| **VRE** | THEO DÕI | Thấp | Hỗ trợ tin tức mạnh nhất nhóm (KQKD tốt, cổ tức, chiến lược mở rộng, catalyst FTSE 21/9) nhưng chính Agent A ghi nhận **mâu thuẫn giữa nhãn mô hình (trend_up=True) và hình thái giá thực tế (MA50 vẫn dốc xuống)** — đây là dấu hiệu độ tin cậy tín hiệu có vấn đề, không chỉ là "rủi ro chấp nhận được". Thêm rủi ro tương quan với VIC (cùng hệ sinh thái Vingroup) nếu chọn cả hai. Cần xác nhận MA50 tạo đáy trước khi coi là actionable. |
| **GVR** | TRÁNH | Cao | Không được Agent C chọn vào danh sách bò. Kỹ thuật đang test lại MA50 sau 2 phiên giảm mạnh, chưa xác nhận giữ được hỗ trợ. Cộng thêm rủi ro pháp lý cơ cấu cổ đông thật (Nhà nước nắm 96,8%, nguy cơ hủy tư cách công ty đại chúng nếu không thoái vốn trong 1 năm) — rủi ro hệ thống, không phải tin đồn. Không có catalyst FTSE bù đắp. |
| **PNJ** | TRÁNH | Cao | Setup kỹ thuật yếu nhất nhóm theo chính Agent A: downtrend 6 tháng rõ ràng (77k→36k), giá dưới MA50 đang dốc xuống, TP đặt đúng tại kháng cự động (MA50) — dạng "bắt dao rơi" điển hình. KQKD cơ bản tốt (DT +79% svck) không đủ bù đắp rủi ro kỹ thuật khi biên lợi nhuận gộp toàn công ty đang giảm và không có catalyst FTSE. |

---

## Kế hoạch theo dõi (watch plan) cho các mã THEO DÕI

### VIC — Vingroup
- **Vùng theo dõi để cân nhắc entry:** 235.000–240.000đ, **chỉ giải ngân nếu** vol_ratio phục hồi rõ rệt (>0.5) và giá giữ vững trên vùng hỗ trợ 226–230k trong ít nhất 2-3 phiên.
- **TP (+8%):** 257.148đ · **SL (-5%):** 226.195đ · **Time-stop:** 25 phiên
- **Cỡ vị thế đề xuất nếu kích hoạt:** 2-3% danh mục (thận trọng, do thanh khoản yếu nhất nhóm)
- **Điều kiện huỷ luận điểm:** đóng cửa dưới 226.195đ; vol_ratio tiếp tục dưới 0.25 kèm tin xác nhận bán ròng cơ cấu ETF frontier lớn; tin tiêu cực mới về đợt phát hành trái phiếu quốc tế ~8.050 tỷ đồng.

### GAS — PV Gas
- **Vùng theo dõi:** 82.000–86.000đ, **chỉ giải ngân sau khi** có công bố nội dung ĐHĐCĐ bất thường 14/9/2026 và nội dung không mang tính tiêu cực (không liên quan xấu tới rủi ro tư cách công ty đại chúng).
- **TP (+8%):** 92.016đ · **SL (-5%):** 80.940đ · **Time-stop:** 25 phiên
- **Cỡ vị thế đề xuất nếu kích hoạt:** 2-3% danh mục
- **Điều kiện huỷ luận điểm:** đóng cửa dưới 80.940đ; nội dung ĐHĐCĐ bất thường tiêu cực (liên quan thoái vốn Nhà nước/tư cách công ty đại chúng); lưu ý ngày GDKHQ cổ tức 25% (đang chi trả 9/9-20/11) có thể gây điều chỉnh giá kỹ thuật — không tự động coi là gãy xu hướng nếu mức giảm khớp đúng tỷ lệ cổ tức.

### VRE — Vincom Retail
- **Vùng theo dõi:** 24.800–25.500đ, **chỉ giải ngân nếu** MA50 xác nhận ngừng dốc xuống/tạo đáy (không chỉ dựa vào nhãn mô hình trend_up) và giá giữ trên vùng hỗ trợ gần nhất trước 21/9/2026.
- **TP (+8%):** 27.378đ · **SL (-5%):** 24.082đ · **Time-stop:** 25 phiên
- **Cỡ vị thế đề xuất nếu kích hoạt:** 2% danh mục (thấp hơn VIC/GAS do độ tin cậy tín hiệu thấp nhất)
- **Điều kiện huỷ luận điểm:** đóng cửa dưới 24.082đ; MA50 tiếp tục dốc xuống rõ ràng qua 21/9 mà không có phản ứng tích cực từ dòng vốn FTSE; nếu đã nắm giữ VIC, không mở thêm VRE để tránh tập trung rủi ro cùng hệ sinh thái Vingroup.

---

## Mã tránh — không có kế hoạch giao dịch

- **GVR:** tránh cho tới khi (a) giá xác nhận giữ vững hỗ trợ MA50 qua ít nhất 3-5 phiên, và (b) có thông tin rõ ràng hơn về phương án xử lý rủi ro tư cách công ty đại chúng.
- **PNJ:** tránh cho tới khi giá đóng cửa vượt lại trên MA50 với volume xác nhận — hiện tại là "bắt dao rơi" trong downtrend chưa đảo chiều.

---

## Stance tổng danh mục

**Khẩu vị rủi ro chung: Thận trọng.**

Không mã nào trong 5 ứng viên hội tụ đủ cả 3 yếu tố (kỹ thuật xác nhận + catalyst tin tức rõ ràng + thanh khoản đủ mạnh) để MUA ngay. Ba mã (VIC, GAS, VRE) có luận điểm bò/gấu cân bằng — đáng theo dõi sát nhưng chưa đủ cơ sở giải ngân; hai mã (GVR, PNJ) có luận điểm gấu áp đảo rõ ràng nên tránh. Phân bổ gợi ý: giữ tỷ trọng tiền mặt cao, nếu tham gia thì tổng vị thế cho cả 3 mã theo dõi không vượt **6-8% danh mục** (2-3% mỗi mã), chỉ kích hoạt khi điều kiện xác nhận ở trên được đáp ứng.

## Cần theo dõi tuần tới

1. **14/9/2026 (hôm nay):** nội dung nghị quyết ĐHĐCĐ bất thường PV Gas (GAS) — quyết định trực tiếp tới việc GAS có nên chuyển từ THEO DÕI sang cân nhắc entry hay không.
2. **21/9/2026:** FTSE Russell chính thức nâng hạng VN lên Emerging Market thứ cấp — theo dõi phản ứng giá VIC (large-cap) và VRE (small-cap) quanh ngày hiệu lực, đặc biệt hoạt động cơ cấu ETF frontier cũ có thể gây bán ròng VIC trước ngày này.
3. **vol_ratio của VIC, GAS, VRE:** cần thấy dấu hiệu phục hồi trên 0.5 để coi thanh khoản đã xác nhận lại, hiện tất cả đều dưới 1 (yếu chung toàn nhóm 5 mã).
4. **Ngày GDKHQ cổ tức** của GAS (25%), VRE và PNJ (10% mỗi mã) — hiện "chưa kiểm chứng" cụ thể, cần cập nhật để tránh nhầm lẫn điều chỉnh giá kỹ thuật do chia cổ tức với tín hiệu gãy xu hướng.
5. **GVR/GAS:** tiến độ (nếu có) của Bộ Tài chính/Ủy ban Quản lý vốn về thoái vốn xuống dưới 90% — liên quan trực tiếp tới rủi ro hủy tư cách công ty đại chúng.

---
*Toàn bộ nội dung trên là kết quả của một khung tranh luận đa tác nhân mô phỏng, dựa trên dữ liệu và mô hình có edge thống kê YẾU. KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — không dùng để ra quyết định giao dịch thực tế mà không có thẩm định độc lập.*
