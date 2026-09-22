# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of 2026-09-22

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là khung ra quyết định mô phỏng từ một hội đồng agent tranh luận nội bộ, dựa trên mô hình có **edge rất yếu (AUC ~0,53–0,55)** — chỉ nhỉnh hơn tung đồng xu một chút. Quyết định đầu tư thật thuộc về người dùng, tự chịu trách nhiệm và tự thẩm định trước khi hành động.

## Tóm tắt điều hành

Cả 5 mã ứng viên (PNJ, VIC, GAS, VRE, GVR) đều có **vol_ratio < 1** — không mã nào có dòng tiền thật xác nhận tín hiệu. Kết hợp với edge mô hình yếu, hội đồng **ưu tiên bảo toàn vốn**: không có mã nào đủ điều kiện MUA ngay ở thời điểm này. 4/5 mã ở mức THEO DÕI (có luận điểm đáng chú ý nhưng thiếu xác nhận), 1 mã (PNJ) ở mức TRÁNH rõ ràng do bằng chứng tiêu cực áp đảo.

## Bảng quyết định theo mã

| Mã | Quyết định | Độ tin cậy | Lý do cân bằng bò/gấu |
|---|---|---|---|
| **PNJ** | TRÁNH | Cao | Bò không có luận điểm (Agent C tự loại). Gấu áp đảo: dưới MA50 sau downtrend 6 tháng, gia đình Chủ tịch đăng ký/đã bán 25 triệu cp (insider selling quy mô lớn), tin lợi nhuận giảm 38% sau soát xét chưa kiểm chứng. Score mô hình cao nhất (0,60) nhưng đây đúng dạng "bắt dao rơi" — score đi ngược thực tế cơ bản/kỹ thuật. |
| **VIC** | THEO DÕI | TB | Bò: trend đẹp nhất nhóm, FTSE Large Cap catalyst đã hiệu lực. Gấu: vol_ratio thấp nhất nhóm (0,091) sau khi giá đã tăng ~60%/tháng — rủi ro chốt lời/điều chỉnh sâu nếu không có dòng tiền thật đỡ giá; TP sát đỉnh cũ. Nghiêng về gấu do thiếu xác nhận volume ở mức tăng nóng — chưa đủ cơ sở MUA. |
| **GAS** | THEO DÕI | TB | Bò: KQKD 8 tháng vượt 129% kế hoạch lợi nhuận cả năm — catalyst cơ bản mạnh nhất nhóm. Gấu: GDKHQ cổ tức tiền mặt rơi đúng ngày as-of (22/9) tạo rủi ro thực thi cụ thể (entry/TP/SL trong signals_latest.csv có thể chưa phản ánh điều chỉnh giá cơ học ~2.500đ/cp); TP trùng đỉnh cũ tháng 8 là kháng cự thật; không có catalyst FTSE. Bò/gấu tương đối cân bằng → mặc định THEO DÕI, chờ giá ổn định sau GDKHQ. |
| **VRE** | THEO DÕI | TB | Kèo cân bằng nhất nhóm theo Agent C: KQKD đúng tiến độ, mở rộng TTTM rõ ràng, có FTSE Small Cap, không tìm thấy tin xấu đáng kể. Nhưng Agent D chỉ rõ: tín hiệu cắt lên MA50 còn non (vol_ratio 0,236, èo uột), TP trùng kháng cự cũ, "không tìm thấy tin xấu" là thiếu bằng chứng chứ không phải bằng chứng vắng rủi ro, và nhóm BĐS nhạy với lãi suất vay mua nhà cao (13–16%/năm). Bò/gấu gần như ngang nhau → THEO DÕI theo nguyên tắc bảo toàn vốn, dù đây là mã có luận điểm gần MUA nhất trong nhóm. |
| **GVR** | THEO DÕI | Thấp | Bò: lợi nhuận quý 2 tăng 58% svck (cao nhất 5 năm), R:R kỹ thuật cân đối nhất nhóm (TP/SL bám biên range 26k–40k). Gấu: tin trái chiều chưa kiểm chứng về kế hoạch lợi nhuận cả năm ("đi lùi" theo một nguồn), lợi nhuận quý 2 có thể đến từ khoản một lần (thanh lý gỗ cao su + đền bù đất, không lặp lại) — chất lượng lợi nhuận đáng ngờ; đây chỉ là cược dao động trong range chứ không phải breakout có cơ sở. Độ tin cậy thấp nhất nhóm do thông tin cơ bản mâu thuẫn chưa đối chiếu được. |

## Kế hoạch giao dịch chi tiết (mã THEO DÕI — chỉ kích hoạt khi điều kiện xác nhận xảy ra)

### VRE (ưu tiên theo dõi cao nhất trong nhóm)
- **Vùng entry (nếu xác nhận):** 25.000–25.500đ, **chỉ giải ngân khi vol_ratio vượt rõ rệt trên 1** (xác nhận dòng tiền thật cho cú cắt lên MA50), hoặc khi giá giữ vững trên 25.000đ qua ít nhất 3–5 phiên không hồi xuống dưới MA50.
- **Chốt lời (TP):** 27.000đ (+8%).
- **Cắt lỗ (SL):** 23.750đ (−5%).
- **Time-stop:** 25 phiên kể từ ngày kích hoạt (không phải từ hôm nay).
- **Cỡ vị thế đề xuất:** 0% hiện tại; tối đa 2–3% danh mục **chỉ khi** điều kiện volume xác nhận ở trên xảy ra.
- **Invalidation:** Giá đóng cửa dưới 24.000đ (phá lại vùng giằng co cũ) → huỷ luận điểm cắt lên MA50; hoặc xuất hiện tin xấu cụ thể (KQKD quý tới không đạt kế hoạch, dòng vốn FTSE thực tế thấp hơn nhiều ước tính 150–250 triệu USD).

### GAS
- **Vùng entry (nếu xác nhận):** chờ qua ngày GDKHQ 22–23/9/2026 để giá ổn định sau điều chỉnh cơ học (~−2.500đ/cp); quan sát vùng 82.000–85.000đ sau điều chỉnh, tránh vào lệnh ngay tại 85.200đ như signals_latest.csv ghi vì số này chưa loại trừ hiệu ứng cổ tức (**chưa kiểm chứng liệu mô hình đã tính đến**).
- **Chốt lời (TP):** 92.016đ theo signals_latest.csv (+8% từ entry gốc) — cần đối chiếu lại sau điều chỉnh giá, đây là kháng cự thật (đỉnh cũ tháng 8).
- **Cắt lỗ (SL):** 80.940đ theo signals_latest.csv (−5%) — cần đối chiếu lại sau điều chỉnh giá.
- **Time-stop:** 25 phiên kể từ ngày kích hoạt.
- **Cỡ vị thế đề xuất:** 0% hiện tại; tối đa 2% nếu giá vượt rõ vùng kháng cự đỉnh cũ ~92k kèm volume cải thiện.
- **Invalidation:** Giá không thể vượt kháng cự 92k sau vài lần thử; hoặc tin tức xác nhận tăng trưởng lợi nhuận chậm lại quý tới.

### VIC
- **Vùng entry (nếu xác nhận):** chờ pullback về vùng MA20 (~230.000–240.000đ) kèm volume tăng rõ rệt so với hiện tại (0,091), hoặc chờ tích luỹ đi ngang ổn định sau chuỗi tăng nóng.
- **Chốt lời (TP):** 259.200đ theo signals_latest.csv (+8%) — lưu ý sát đỉnh cũ ~265k, dư địa mỏng.
- **Cắt lỗ (SL):** 228.000đ theo signals_latest.csv (−5%).
- **Time-stop:** 25 phiên kể từ ngày kích hoạt.
- **Cỡ vị thế đề xuất:** 0% hiện tại; tối đa 2% nếu volume xác nhận.
- **Invalidation:** Xuất hiện phiên bán mạnh có volume cao (dấu hiệu chốt lời sau tăng 60%/tháng) → không tham gia; giá thủng MA20 kèm volume tăng theo hướng giảm.

### GVR
- **Vùng entry (nếu xác nhận):** vùng hỗ trợ dưới của range 30.700–32.350đ, chỉ khi có thông tin xác nhận (không phải "đi lùi") về kế hoạch lợi nhuận cả năm 2026.
- **Chốt lời (TP):** 34.938đ theo signals_latest.csv (+8%, bám biên trên range).
- **Cắt lỗ (SL):** 30.732đ theo signals_latest.csv (−5%, bám biên dưới range).
- **Time-stop:** 25 phiên kể từ ngày kích hoạt.
- **Cỡ vị thế đề xuất:** 0% hiện tại; tối đa 1–2% nếu tin trái chiều được làm rõ theo hướng tích cực.
- **Invalidation:** Xác nhận kế hoạch lợi nhuận 2026 "đi lùi" là chính xác → huỷ hoàn toàn luận điểm dựa trên quý 2 đột biến (khoản một lần từ thanh lý gỗ cao su/đền bù đất).

### PNJ — TRÁNH, không có kế hoạch giao dịch
Không đưa ra kế hoạch giao dịch do luận điểm mua không đủ cơ sở; theo dõi diễn biến bán ra của gia đình Chủ tịch và kết quả soát xét lợi nhuận trước khi xem xét lại.

## Stance tổng danh mục

**Thận trọng.** Lý do: (1) edge mô hình toàn hệ thống rất yếu (AUC ~0,53–0,55); (2) toàn bộ 5 mã ứng viên đều thiếu xác nhận dòng tiền (vol_ratio < 1); (3) rủi ro hệ thống: dư nợ margin toàn thị trường ước tính vượt 10 tỷ USD, lãi suất vay mua nhà thực tế cao (13–16%/năm) ảnh hưởng nhóm BĐS (VIC, VRE) chiếm 2/5 candidate. Phân bổ gợi ý: giữ tỷ trọng tiền mặt/quan sát cao, **không giải ngân mới** cho tới khi có xác nhận volume rõ ràng ở mã cụ thể; nếu buộc phải có một vị thế thăm dò, ưu tiên VRE (luận điểm cân bằng nhất) với cỡ vị thế nhỏ (2–3%) và kỷ luật cắt lỗ nghiêm ngặt.

## Cần theo dõi tuần tới

1. **GAS:** phản ứng giá quanh GDKHQ cổ tức 22/9/2026 và ĐKCC 23/9/2026 — xem điều chỉnh giá cơ học có bị hiểu nhầm thành tín hiệu bán hay không.
2. **VRE:** vol_ratio có vượt rõ rệt trên 1 để xác nhận cú cắt lên MA50 hay quay lại vùng giằng co 24k (false breakout).
3. **VIC/VRE:** dòng vốn ngoại thực tế từ hiệu lực phân bổ FTSE (21/9/2026) — Agriseco ước tính chỉ 150–250 triệu USD giai đoạn 9/2026–3/2027, cần xem có đúng kỳ vọng hay thấp hơn.
4. **PNJ:** tiến độ đăng ký/bán ra phần còn lại trong 25 triệu cp của gia đình Chủ tịch; xác nhận hay bác bỏ tin "lợi nhuận giảm 38% sau soát xét".
5. **GVR:** làm rõ thông tin trái chiều về kế hoạch lợi nhuận cả năm 2026 ("đi lùi" hay tăng trưởng).
6. **Toàn thị trường:** diễn biến VN-Index quanh 1.840 điểm và dư nợ margin (>10 tỷ USD) — rủi ro force-sell dây chuyền nếu điều chỉnh mạnh.

---
*Ghi chú phương pháp: Quyết định dựa trên tổng hợp whiteboard PHIÊN 1–3 (Agent A kỹ thuật, Agent B tin tức, Agent C bò, Agent D gấu) và signals_latest.csv. Các số liệu chưa kiểm chứng đầy đủ được giữ nguyên trạng thái "chưa kiểm chứng" theo đúng ghi nhận của Agent A/B, không tự suy diễn thêm.*

*Đây KHÔNG PHẢI khuyến nghị đầu tư.*
