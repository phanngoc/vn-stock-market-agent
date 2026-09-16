# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of 2026-09-16

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là khung ra quyết định mô phỏng của một hội đồng tác nhân AI tranh luận nội bộ (kỹ thuật, tin tức, bò, gấu, CIO), dựa trên dữ liệu và bằng chứng đã ghi trên whiteboard. Quyết định đầu tư thật thuộc về người dùng, sau khi tự thẩm định. Mô hình định lượng nền có **edge yếu (AUC ~0.53–0.55)** — chỉ nhỉnh hơn tung đồng xu một chút, không đủ để xác nhận xác suất thắng cao cho bất kỳ mã nào.

## Nguyên tắc ra quyết định phiên này

Ưu tiên **bảo toàn vốn**. Khi lập luận bò (Agent C) và gấu (Agent D) cân bằng nhau — tức phản biện của D không bị bác bỏ rõ ràng bằng bằng chứng mới, chỉ là góc nhìn khác trên cùng dữ kiện — mặc định là **THEO DÕI**, không MUA. Chỉ xếp **MUA** khi bằng chứng kỹ thuật + tin tức + cơ bản đồng thuận mạnh và các phản biện gấu bị bằng chứng cụ thể làm suy yếu rõ.

Sau khi cân đối toàn bộ whiteboard: **không có mã nào trong 5 mã ứng viên đạt ngưỡng MUA phiên này.** Bò và gấu tranh luận cân bằng ở VIC và GVR (điểm mạnh có thật nhưng rủi ro cũng có thật, chưa bên nào áp đảo); ở PNJ, VRE, GAS, cán cân nghiêng về gấu.

---

## Bảng quyết định

| Mã | Quyết định | Độ tin cậy | Lý do quyết định |
|---|---|---|---|
| **VIC** | THEO DÕI | TB | Catalyst FTSE (21/9) + KQKD tăng 360,5% là thật, nhưng vol_ratio 0.12 (thấp nhất nhóm) và phiên giảm 4,3% do chốt lời cho thấy khả năng "buy the rumor, sell the news" — D chỉ ra hợp lý, C chưa bác bỏ được bằng volume xác nhận. |
| **GVR** | THEO DÕI | TB | Kỹ thuật cân bằng nhất (volume 1.34 cao nhất, SL sát hỗ trợ), nhưng D chỉ ra vùng giao MA20/MA50 là vùng cân bằng cung-cầu dễ bị "quét" SL, giá cao su thế giới đang giằng co, KQKD Q2/Q3 chưa kiểm chứng. |
| **GAS** | TRÁNH | TB | Chính Agent C đã tự hạ GAS xuống "kèo phụ có điều kiện"; RSI 71 quá mua nhất nhóm, giá tham chiếu gần như chắc chắn giảm kỹ thuật quanh GDKHQ 22/9 (~2,7%), TP sát kháng cự đỉnh lịch sử 95–102k, cộng rủi ro thủ tục công ty đại chúng. |
| **VRE** | TRÁNH | TB | A xếp kỹ thuật 4.5/10, giá đang chạm đúng vùng kháng cự MA50 từng bị từ chối (tháng 6–7) với volume hồi phục yếu (0.21); B xác nhận không có catalyst mới sắp tới (tin tốt đều đã cũ); C không chọn làm kèo bò. |
| **PNJ** | TRÁNH | Cao | Kỹ thuật thấp nhất nhóm (3/10), downtrend dài hạn từ ~78k chưa bị phá, volume phục hồi quá yếu (0.26) để tin đảo chiều — giống "bắt dao rơi"; cộng overhang cung cụ thể (người nhà Chủ tịch đăng ký bán "nghìn tỷ đồng", quy mô/thời điểm chưa kiểm chứng). Cả A và D đồng thuận đây là mã rủi ro nhất nhóm. |

---

## Kế hoạch giao dịch (chỉ áp dụng cho mã THEO DÕI — mang tính khung tham chiếu, KHÔNG phải lệnh mua ngay)

### VIC — THEO DÕI
- **Vùng theo dõi/entry tham khảo:** 238.000–244.000đ (quanh giá hiện tại 242.900đ; ưu tiên chờ nhịp điều chỉnh thêm hoặc xác nhận volume tăng trước khi vào, không mua đuổi).
- **Chốt lời +8%:** 262.332đ (theo TP trong signals_latest.csv, tính từ entry 242.900đ).
- **Cắt lỗ −5%:** 230.755đ.
- **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu giải ngân):** 2–3% danh mục — nhỏ, vì volume xác nhận còn yếu.
- **Điều kiện huỷ luận điểm (invalidation):** Volume không cải thiện quanh/sau ngày 21/9 (không có dấu hiệu dòng vốn ngoại thực chảy vào) dù giá vẫn giữ; hoặc giá thủng lại vùng 230k trước time-stop; hoặc xuất hiện tin xấu cụ thể về tín dụng BĐS/pha loãng từ đợt phát hành trái phiếu quốc tế.

### GVR — THEO DÕI
- **Vùng theo dõi/entry tham khảo:** 31.800–32.500đ (quanh giá hiện tại 32.250đ, đúng vùng giao MA20/MA50 mà cả A và D đều lưu ý là vùng cân bằng — chờ giá giữ vững trên vùng này thêm 1–2 phiên trước khi coi là xác nhận).
- **Chốt lời +8%:** 34.830đ.
- **Cắt lỗ −5%:** 30.638đ (sát hỗ trợ MA50 thực tế theo Agent A).
- **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu giải ngân):** 2–3% danh mục — thận trọng vì SL gần, dễ bị quét theo cảnh báo của D.
- **Điều kiện huỷ luận điểm (invalidation):** Giá đóng cửa thủng rõ ràng dưới MA50 (không chỉ chạm SL kỹ thuật mà mất xu hướng); giá cao su thế giới tiếp tục giảm rõ rệt (không chỉ giằng co); hoặc KQKD Q2/Q3 công bố cho thấy đà tăng trưởng 56%/85% svck của Q1 không duy trì được.

*(GAS, VRE, PNJ: TRÁNH — không lập kế hoạch giao dịch; `entry_zone_vnd` để trống, `size_pct` = 0% trong decision.json.)*

---

## Stance tổng danh mục

**Thận trọng.** 3/5 mã ứng viên bị xếp TRÁNH, 2/5 chỉ ở mức THEO DÕI — không mã nào đạt MUA phiên này. Edge mô hình định lượng yếu (AUC ~0.53–0.55) đồng nghĩa điểm số (score, p_LogReg...) trong signals_latest.csv không đủ để tự nó là căn cứ mua; toàn bộ lập luận bò của C đều dựa vào catalyst tin tức + kỹ thuật, và phản biện của D cho thấy cả hai catalyst mạnh nhất nhóm (FTSE với VIC, cổ tức với GAS) đều có rủi ro bị hiểu sai chiều tác động giá ngắn hạn (priced-in / giảm giá tham chiếu kỹ thuật). Phân bổ gợi ý: giữ tỷ trọng tiền mặt cao, nếu tham gia thì giới hạn VIC + GVR ở mức nhỏ (2–3% mỗi mã, tổng ≤5–6% danh mục) và chờ xác nhận thêm trước khi tăng tỷ trọng.

## Cần theo dõi tuần tới

1. **21/9/2026** — FTSE Russell chính thức phân bổ dòng vốn (nâng hạng Secondary Emerging Market): theo dõi volume thực tế của VIC quanh ngày này để xác nhận (hoặc bác bỏ) luận điểm dòng vốn ngoại của Agent C.
2. **22–23/9/2026** — GAS chốt quyền cổ tức tiền mặt 25% (GDKHQ 22/9): quan sát mức điều chỉnh giá tham chiếu và phản ứng giá sau đó để đánh giá lại GAS cho phiên tới.
3. **VRE** — vùng kháng cự MA50 cũ ~25.700–26.000đ: cần volume tăng rõ rệt để phá vùng này, nếu không khả năng bị từ chối lần nữa (như tháng 6–7) là cao.
4. **PNJ** — theo dõi tin cụ thể về khối lượng/thời điểm bán ra của người nhà Chủ tịch HĐQT (hiện "chưa kiểm chứng" quy mô); đây là overhang cung có thể xác nhận hoặc phủ định trong tuần tới.
5. **GVR** — chờ công bố KQKD Q2/Q3 2026 và diễn biến giá cao su thế giới (SHFE/TOCOM) để xác nhận đà tăng trưởng lợi nhuận có tiếp diễn hay không.

---

*Quyết định trên tổng hợp từ tranh luận nội bộ của Agent A (kỹ thuật), Agent B (tin tức/cơ bản), Agent C (bò), Agent D (gấu). Toàn bộ số liệu giá/TP/SL lấy từ `signals_latest.csv` (as-of 2026-09-16). Các điểm suy luận chưa có dữ liệu định lượng xác nhận đều được ghi rõ là "chưa kiểm chứng" trong các note tương ứng.*

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**
