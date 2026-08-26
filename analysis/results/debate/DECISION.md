# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of 2026-08-26

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là khung ra quyết định mô phỏng dựa trên tranh luận đa tác nhân (Agent A/B/C/D), phục vụ mục đích nghiên cứu/giáo dục. Quyết định đầu tư thật là của người dùng, tự chịu trách nhiệm và tự thẩm định thêm trước khi hành động. Mô hình nền có **edge YẾU (AUC ~0.53–0.55)** — score cao nhất trong top-10 (KDH 0.5924) chỉ nhỉnh hơn tung đồng xu một chút.

## Nguyên tắc ra quyết định
- Ưu tiên **bảo toàn vốn** trên lợi nhuận kỳ vọng, vì edge mô hình yếu và toàn bộ 5/5 mã ứng viên đều có `vol_ratio < 1` (không có xác nhận dòng tiền mạnh).
- Khi luận điểm bò (Agent C) và gấu (Agent D) **cân bằng** cho một mã → mặc định **THEO DÕI**, không MUA bừa.
- Khi luận điểm gấu **áp đảo** (không có phản bác hợp lý, hoặc catalyst bò dựa trên suy luận yếu / tin chưa xác nhận) → **TRÁNH**.
- 3/5 mã ứng viên (KDH, PDR, VIC, VRE — trừ PNJ) đều thuộc **nhóm ngành RealEstate** → rủi ro tập trung ngành có thật, đã được Agent D nêu rõ và không bị bác bỏ.

---

## Bảng quyết định theo mã

| Mã | Quyết định | Độ tin cậy | Lý do quyết định |
|---|---|---|---|
| **VIC** | 🟡 THEO DÕI | TB | Setup kỹ thuật tốt nhất nhóm (breakout, trend_up=True, 7/10) nhưng khối lượng xác nhận vẫn <1 (0.55) và catalyst FTSE đã công bố từ 5 tháng trước nên có thể đã phần nào phản ánh vào giá (rủi ro "sell-the-news") — bò/gấu cân bằng. |
| **PDR** | 🟡 THEO DÕI | TB | Catalyst insider-buying (Chủ tịch mua 20tr cp) là tín hiệu thật và đang diễn ra, nhưng đối trọng bởi vol_ratio thấp nhất nhóm (0.17), rủi ro pha loãng ~20% chưa rõ thời điểm, và mua đăng ký chưa xác nhận đã khớp hết — bò/gấu cân bằng, nghiêng nhẹ về rủi ro. |
| **VRE** | 🔴 TRÁNH | TB | Kỹ thuật yếu nhất trong 3 mã được Agent C chọn (4/10, vẫn dưới MA50, chưa đảo chiều rõ); catalyst cổ tức mà C dùng làm điểm tựa thực chất là lực cản kỹ thuật khi tới ngày GDKHQ (giá tham chiếu bị điều chỉnh giảm đúng số cổ tức), và lợi ích từ FTSE với VRE chỉ là "có thể" (B), không chắc chắn — gấu thắng thế. |
| **PNJ** | 🔴 TRÁNH | TB | Không có luận điểm bò được xây dựng (Agent C không chọn); tin xấu **cụ thể, đã xảy ra** (lỗ 283 tỷ đồng Q2/2026) chưa được giải thích rõ nguyên nhân, cộng với kỹ thuật yếu (4/10, rủi ro "dead-cat bounce" sau nhịp hồi +40%) — gấu thắng thế rõ. |
| **KDH** | 🔴 TRÁNH | Cao | Kỹ thuật thấp nhất nhóm (3/10) — Agent A gọi thẳng đây là "bắt dao rơi": dưới cả MA20/MA50, mới bật 2 phiên, khối lượng thấp, MA50 vẫn dốc xuống. Cơ bản công ty tốt (lãi 2025 vượt 63% KH, sạch nợ) nhưng chính Agent B xác nhận **thiếu catalyst ngắn hạn cụ thể trong khung 5 tuần** — không có luận điểm bò nào được xây dựng cho mã này. |

---

## Kế hoạch giao dịch (chỉ áp dụng cho THEO DÕI — chưa vào lệnh)

### VIC — THEO DÕI (TB)
- **Vùng theo dõi/entry điều kiện:** 218,000–223,000đ, **chỉ xem xét vào lệnh nếu `vol_ratio` vượt rõ trên 1.0** (xác nhận dòng tiền vào breakout) trong 1–2 phiên tới, và giá giữ được trên vùng kháng cự cũ ~220k (không rơi lại vùng tích lũy 200–215k).
- **Chốt lời (+8%):** 240,840đ | **Cắt lỗ (−5%):** 211,850đ | **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu điều kiện xác nhận đạt):** 2–3% danh mục (thận trọng, do edge mô hình yếu).
- **Điều kiện huỷ luận điểm:** vol_ratio tiếp tục dưới 0.6 trong >3 phiên tới (breakout không được dòng tiền xác nhận); xuất hiện thêm tin thoái vốn/tiêu cực khác từ nhóm Vingroup; giá đóng cửa dưới 211,850đ.

### PDR — THEO DÕI (TB)
- **Vùng theo dõi/entry điều kiện:** 12,300–12,600đ, **chỉ xem xét vào lệnh nếu** có xác nhận Chủ tịch đã mua xong/mua thêm cổ phiếu (công bố kết quả giao dịch trước/sau hạn 29/8/2026) **và** chưa có thông báo ngày GDKHQ của đợt phát hành 200 triệu cp.
- **Chốt lời (+8%):** 13,554đ | **Cắt lỗ (−5%):** 11,922đ | **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu điều kiện xác nhận đạt):** 1.5–2.5% danh mục (thận trọng hơn VIC do vol_ratio thấp nhất nhóm và rủi ro pha loãng).
- **Điều kiện huỷ luận điểm:** công bố ngày GDKHQ chốt quyền mua cổ phiếu 5:1 trong thời gian tới; Chủ tịch không hoàn tất mua theo đăng ký; giá xuyên SL 11,922đ.

---

## Mã TRÁNH — không có kế hoạch vào lệnh (entry_zone/size = 0%)
VRE, PNJ, KDH: không đưa ra vùng entry. Sẽ xem xét lại nếu có thay đổi cụ thể ở phần "cần theo dõi" bên dưới.

---

## Stance tổng danh mục

**Khẩu vị rủi ro chung: Thận trọng (Cautious).**

Lý do: (1) mô hình nền có edge yếu, không mã nào có xác nhận khối lượng mạnh (`vol_ratio` toàn bộ top-5 <1); (2) 3/5 mã ứng viên cùng thuộc ngành RealEstate → rủi ro tập trung ngành nếu có tin xấu vĩ mô (thắt chặt tín dụng, kết quả Luật Phát triển đô thị); (3) bối cảnh thị trường chung: thanh khoản VN-Index giảm ~10% khi chỉ số thử vùng cản 1.775–1.810, dư nợ margin tăng 6% so với quý trước — cả hai làm tăng rủi ro giằng co/điều chỉnh ngắn hạn cho bất kỳ vị thế mới nào.

**Phân bổ gợi ý:** không mở vị thế mới ngay; giữ tối đa ~5% danh mục "dự phòng theo dõi" cho VIC + PDR nếu điều kiện xác nhận đạt trong tuần tới (xem điều kiện ở trên), phần còn lại giữ tiền mặt/chờ tín hiệu rõ hơn.

---

## Cần theo dõi tuần tới

1. **VIC:** `vol_ratio` có vượt 1.0 không (xác nhận breakout); phản ứng giá quanh vùng 220–230k; tin tức mới (nếu có) về dòng vốn ETF trước ngày FTSE nâng hạng chính thức 21/9/2026.
2. **PDR:** kết quả cuối cùng đợt đăng ký mua 20 triệu cp của Chủ tịch (hạn 29/8/2026, còn ~3 phiên); tin về ngày GDKHQ của đợt phát hành 200 triệu cổ phiếu (5:1).
3. **VRE:** thông báo ngày GDKHQ cổ tức tiền mặt 10% (dự kiến Q3/2026) — lưu ý đây là lực cản kỹ thuật khi đến ngày, không phải lực đẩy.
4. **Ngành BĐS chung:** kết quả cụ thể của Luật Phát triển đô thị (Quốc hội dự kiến thông qua 24/8/2026) — tác động đến KDH/PDR/VIC/VRE hiện **chưa kiểm chứng**.
5. **Thị trường chung:** VN-Index có vượt dứt điểm vùng cản 1.775–1.810 kèm thanh khoản cải thiện hay không; diễn biến dư nợ margin.
6. **PNJ (ngoài watchlist mua):** theo dõi báo cáo tài chính chi tiết Q2/2026 để hiểu rõ nguyên nhân khoản lỗ 283 tỷ — hiện **chưa kiểm chứng** cụ thể.

---

*Ghi chú cuối: toàn bộ quyết định trên dựa trên tranh luận mô phỏng giữa các agent AI, sử dụng dữ liệu và tin tức có thể chưa đầy đủ/chưa kiểm chứng hết. **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.***
