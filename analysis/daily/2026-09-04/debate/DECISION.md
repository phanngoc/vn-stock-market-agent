# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of 2026-09-04

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là khung ra quyết định mô phỏng cho mục đích nghiên cứu/giáo dục, tổng hợp từ tranh luận nội bộ của các agent (kỹ thuật, tin tức, bò, gấu). Mọi con số TP/SL/entry chỉ là tham chiếu dựa trên `signals_latest.csv` và các quy tắc quản trị rủi ro cố định (+8%/-5%/25 phiên), KHÔNG phải dự báo giá. Quyết định giao dịch thật thuộc về người dùng, sau khi tự kiểm chứng dữ liệu và cân nhắc khả năng chịu rủi ro của mình. Mô hình định lượng nền có **AUC ~0.53–0.55** — gần mức ngẫu nhiên, không đủ mạnh để làm cơ sở duy nhất cho bất kỳ quyết định nào.

## Tóm tắt quan điểm hội đồng

Agent A (kỹ thuật) xếp hạng đẹp→xấu: VRE > VIC > GVR > PNJ > PDR. Agent B (tin tức) xếp theo hỗ trợ tin: VIC > VRE > PNJ > GVR > PDR. Agent C (bò) chọn VIC, VRE, GVR làm kèo bò, tự tin nhất ở VIC. Agent D (gấu) phản biện mạnh cả ba: VIC là "đuổi giá ở đỉnh" (RSI 77, volume không xác nhận, khả năng "sell the news" quanh mốc FTSE 21/9 đã priced-in); VRE có model-disagreement rõ (GradBoost/XGBoost < 0.5, chỉ LSTM > 0.5 kéo điểm); GVR hội tụ 3 tín hiệu tiêu cực (volume thấp, guidance nội bộ giảm LNST, model split) nên nên xếp vào TRÁNH chứ không phải dự phòng. D cũng nêu rủi ro pha loãng định lượng lớn ở PDR (~23%+ cổ phiếu mới) và downtrend dài chưa đảo chiều ở PNJ.

Nguyên tắc bảo toàn vốn được ưu tiên: khi bò và gấu có luận điểm ngang nhau (bò có catalyst thật nhưng gấu chỉ ra rủi ro cụ thể tương đương hoặc lớn hơn), quyết định mặc định là **THEO DÕI**, không MUA. Với mô hình có AUC chỉ 0.53-0.55, độ tin cậy "Cao" hầu như không nên gán cho bất kỳ mã nào trong nhóm này trừ khi cả kỹ thuật + tin tức + rủi ro đều đồng thuận rõ.

## Bảng quyết định

| Mã | Quyết định | Độ tin cậy | Lý do quyết định |
|---|---|---|---|
| **VIC** | THEO DÕI | TB | Catalyst FTSE GEIS (21/9) + KQKD đột biến là thật, nhưng RSI 77 quá mua, volume không xác nhận cú tăng vọt, và tin đã công bố 2 tuần trước (rủi ro priced-in/"sell the news") — D chỉ ra time-stop 25 ngày trùng đúng qua mốc sự kiện, rủi ro entry theo thời điểm quá cao để MUA ngay. |
| **VRE** | THEO DÕI | TB | Kỹ thuật tốt nhất nhóm (6.5/10, volume xác nhận, RSI chưa quá mua) và catalyst cổ tức 10% lần đầu sau 7 năm là điểm cộng thật, nhưng ngày GDKHQ "chưa kiểm chứng" nên không thể dùng làm mốc giao dịch, và D chỉ ra model-disagreement (GradBoost/XGBoost <0.5) đáng cảnh báo — bò/gấu cân bằng, chưa đủ độ tin cậy để MUA. |
| **GVR** | TRÁNH | TB | C tự xếp đây là kèo "yếu, chỉ tham khảo"; D chỉ ra hội tụ 3 tín hiệu tiêu cực đồng thời (volume 0.36 thấp thứ nhì nhóm, guidance nội bộ hạ LNST 2026 -7%, model split GradBoost/XGBoost <0.5) không có catalyst ngắn hạn bù lại trong khung time-stop 25 ngày — đồng ý với D, không nên xem là dự phòng. |
| **PNJ** | TRÁNH | TB | Kỹ thuật xấu thứ nhì nhóm — dưới MA50, downtrend dài (85k→39k, mất ~54% từ đỉnh), chưa xác nhận đảo chiều. KQKD Q1 mạnh nhưng là tin cũ (đã qua 2 quý), không đủ để đảo ngược một downtrend kéo dài — mua ở đây là bắt dao rơi thuần túy. |
| **PDR** | TRÁNH | Cao | Kỹ thuật tệ nhất nhóm (volume 0.34 thấp nhất, dưới MA50) CỘNG rủi ro pha loãng định lượng lớn và cụ thể (~233,7 triệu cp mới ≈ >23% cổ phiếu lưu hành, thời điểm chốt quyền chưa xác định) — tổ hợp kỹ thuật xấu + rủi ro tin tức cụ thể, đủ rõ để tránh với độ tin cậy cao. |

**Không có mã nào đạt mức "MUA"** trong phiên này — không mã nào có sự đồng thuận đủ mạnh giữa kỹ thuật, tin tức, VÀ rủi ro (mô hình định lượng) để vượt ngưỡng bảo toàn vốn.

## Kế hoạch giao dịch (cho các mã THEO DÕI — chỉ để tham khảo nếu điều kiện cải thiện)

### VIC (giá hiện tại 254.000đ)
- **Vùng entry theo dõi:** chỉ xem xét sau khi giá điều chỉnh và ổn định lại trên MA20/MA50 với RSI hạ về vùng trung tính (<65), HOẶC sau khi mốc 21/9 FTSE đã qua và phản ứng giá rõ ràng (không "sell the news").
- **TP:** 274.320đ (+8%) · **SL:** 241.300đ (-5%) · **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu vào):** 2-3% danh mục (giảm so với chuẩn do rủi ro thời điểm cao).
- **Điều kiện huỷ luận điểm:** RSI tiếp tục >75 kèm volume không cải thiện; giá giảm mạnh (>3% trong 1-2 phiên) quanh/trước 21/9 (dấu hiệu sell-the-news); hoặc bất kỳ tin xấu bất ngờ nào làm đảo ngược catalyst FTSE.

### VRE (giá hiện tại 26.700đ)
- **Vùng entry theo dõi:** chờ xác nhận thêm 3-5 phiên giữ vững trên MA50 với volume duy trì ≥0.8, và/hoặc chờ ngày GDKHQ cổ tức được công bố chính thức (kiểm chứng qua VSD/HOSE).
- **TP:** 28.836đ (+8%) · **SL:** 25.365đ (-5%) · **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất (nếu vào):** 3-4% danh mục.
- **Điều kiện huỷ luận điểm:** giá thủng lại MA50 kèm volume yếu; model score tổng hợp giảm sâu hơn (đặc biệt nếu GradBoost/XGBoost tiếp tục <0.4); không có công bố ngày GDKHQ trong vài tuần tới làm mất catalyst chính.

## Stance tổng danh mục

**Thận trọng.** Thị trường đang ở trạng thái hưng phấn (VN-Index đã vượt 1.800 điểm, vốn hóa VIC lập kỷ lục), nhưng nhóm 5 mã ứng viên có tỷ trọng BĐS cao (VIC, VRE, PDR — 3/5 mã), tạo rủi ro tập trung ngành nếu tâm lý BĐS đảo chiều. Mô hình định lượng có AUC chỉ 0.53-0.55 — gần ngẫu nhiên — nên không đủ cơ sở để tích cực giải ngân. Phân bổ gợi ý: giữ tỷ trọng tiền mặt cao (≥60-70%), chỉ xem xét mở vị thế nhỏ (2-4% mỗi mã) cho VIC/VRE nếu điều kiện huỷ luận điểm ở trên không xảy ra và có xác nhận thêm; PNJ, PDR, GVR nên tránh hoàn toàn trong giai đoạn này.

## Cần theo dõi tuần tới

- **21/9/2026** — FTSE Russell chính thức nâng hạng VN, VIC là 1 trong 3 mã vốn hóa lớn hưởng lợi trực tiếp; theo dõi phản ứng giá quanh/sau mốc này (rủi ro "sell the news").
- **Ngày GDKHQ cổ tức VRE** (dự kiến chi trả Q3/2026, ngày cụ thể chưa công bố) — cần xác nhận qua VSD/HOSE trước khi coi đây là catalyst có thể giao dịch.
- **PDR** — thời điểm chốt quyền chào bán cổ phiếu 5:1 (pha loãng ~23%+) chưa xác nhận; theo dõi công bố HOSE để tránh bị bất ngờ.
- **GVR** — tiến độ pháp lý các dự án KCN trên đất cao su (không nằm trong khung time-stop 25 ngày, chỉ theo dõi dài hạn).
- **Diễn biến khối ngoại** và biến động VN-Index quanh vùng 1.800-1.830 — rủi ro điều chỉnh chung tăng khi thị trường hưng phấn.
