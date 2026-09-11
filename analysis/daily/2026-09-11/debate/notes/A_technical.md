### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-09-11 11:57

| Mã | Trend (vs MA50) | RSI(14) | Vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| PNJ | ↓ dưới MA50 | 44.3 (trung tính) | 0.34 (èo uột) | **3/10** | Dưới MA50 nhưng RSI không quá bán (không phải đáy rõ) → giống "bắt dao rơi" nhẹ; volume rất yếu không xác nhận đảo chiều. |
| VIC | ↑ trên MA50 | 66.2 (gần quá mua) | 0.13 (rất yếu) | **4/10** | Xu hướng tăng nhưng RSI sát ngưỡng 70 + volume cực yếu (0.13) → phân kỳ giá/khối lượng, rủi ro đuối đà. |
| GVR | ↑ trên MA50 | 51.4 (trung tính) | 0.37 (yếu) | **6/10** | Setup cân bằng nhất: uptrend rõ, RSI còn nhiều dư địa trước khi quá mua, dù volume vẫn dưới trung bình. |
| VRE | ↑ trên MA50 | 52.1 (trung tính) | 0.29 (yếu) | **5.5/10** | Tương tự GVR nhưng volume yếu hơn → tín hiệu kém chắc chắn hơn một chút. |
| GAS | ↑ trên MA50 | 62.0 (tiến gần quá mua) | 0.38 (yếu) | **5/10** | Uptrend nhưng RSI đã khá cao, dư địa tăng hẹp hơn GVR/VRE; volume cũng dưới 1. |

Ghi chú TP/SL: cả 5 mã đều áp dụng công thức chuẩn +8%/−5% (không lệch theo mã); chưa kiểm chứng vùng hỗ trợ/kháng cự cụ thể từ chart (chỉ đọc số liệu CSV, chưa xem ảnh nến chi tiết) nên không khẳng định +8%/−5% có khớp với S/R thực tế hay không.

- **Setup kỹ thuật tốt nhất (tương đối): GVR** — uptrend + RSI trung tính (51) còn dư địa, dù volume vẫn dưới 1.
- **Setup kỹ thuật yếu nhất: PNJ** — dưới MA50 (downtrend) dù có score mô hình cao nhất (0.62); rủi ro "bắt dao rơi" nếu vào lúc này.
- **Rủi ro kỹ thuật lớn nhất chung: volume yếu trên toàn bộ top 5** (vol_ratio 0.13–0.38, đều <1) → không mã nào có dòng tiền xác nhận mạnh, tín hiệu kỹ thuật nói chung thiếu độ tin cậy.
- **VIC** đáng chú ý vì RSI gần vùng quá mua (66) trong khi volume lại thấp nhất nhóm (0.13) — phân kỳ giá/khối lượng, cảnh báo đà tăng có thể yếu dần.
- Toàn bộ đánh giá trên chỉ dựa trên chỉ báo trong signals_latest.csv (RSI, trend, vol_ratio); chưa xem chi tiết biểu đồ nến/MA20 để xác nhận vùng hỗ trợ-kháng cự cụ thể.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ** — chỉ là góc nhìn kỹ thuật thuần túy, độc lập với tin tức/định giá; mô hình có edge yếu (AUC ~0.53–0.55), setup kỹ thuật ở đây mang tính xác suất, không phải chắc chắn.
