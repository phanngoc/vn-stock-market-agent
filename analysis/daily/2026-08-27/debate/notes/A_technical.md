### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-08-28 02:15

**Nguồn số liệu**: `signals_latest.csv` (RSI-14, trend vs MA50, vol_ratio, TP/SL) + chart `<TICKER>_setup.png` (nến, MA20/MA50) cho 5 mã ứng viên top theo score. Không dùng tin tức/định giá cơ bản.

| Mã | Trend (vs MA50) | RSI-14 | Vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **VIC** | ↑ trên MA50 | 68.7 (cận quá mua) | 1.49 (sôi động) | **7/10** | Vừa breakout tăng mạnh bằng 1 nến gap lớn vượt vùng đỉnh cũ ~225–230k, khối lượng xác nhận tốt, nhưng nến vào lệnh đã giãn xa MA20 → mua đuổi sau gap, RSI gần 70 nên dư địa trước khi "quá mua" không còn nhiều, rủi ro điều chỉnh ngắn hạn để lấp gap. |
| **VRE** | ↑ trên MA50 (mới cắt lên) | 58.0 (trung tính, còn dư địa) | 1.37 (sôi động) | **6.5/10** | Giá vừa cắt lên lại MA20/MA50 đang đi ngang sau downtrend từ đỉnh tháng 4 (~36k → đáy ~24k), khối lượng ủng hộ, RSI chưa quá mua nên dư địa tốt hơn VIC. Nhưng đây là tín hiệu đảo chiều **mới hình thành**, chưa phải xu hướng tăng đã xác lập — độ tin cậy thấp hơn VIC. |
| **PNJ** | ↓ dưới MA50 | 56.5 (trung tính) | 0.98 (~trung bình, không xác nhận) | **3.5/10** | Downtrend sâu và kéo dài (80k → ~30k từ đầu năm), giá đang hồi phục dưới MA50 vẫn đang dốc xuống rõ. Khối lượng không có gì đột biến để xác nhận đảo chiều → giống nhịp hồi trong downtrend hơn là đảo chiều thật, cảnh báo "bắt dao rơi". |
| **PDR** | ↓ dưới MA50 | 54.2 (trung tính) | 0.76 (èo uột) | **3.5/10** | Downtrend rõ từ ~17k xuống đáy ~11.4k, mới nhích lên nhưng vẫn dưới MA50 đang giảm; vol_ratio <1 cho thấy nhịp hồi thiếu dòng tiền xác nhận. Rủi ro kỹ thuật là hồi kỹ thuật ngắn trong xu hướng giảm. |
| **KDH** | ↓ dưới MA50 | 51.4 (trung tính, sát 50) | 0.68 (èo uột nhất nhóm) | **2.5/10** | Downtrend đều đặn và dai dẳng nhất nhóm (28k → 18k xuyên suốt Feb–Aug), giá vẫn nằm dưới cả MA20 lẫn MA50 đang dốc xuống, khối lượng yếu nhất → setup kỹ thuật yếu nhất trong 5 mã, gần như "bắt dao rơi" điển hình. |

**Nhận định chung**
- Setup kỹ thuật đẹp nhất nhóm: **VIC** (uptrend + volume xác nhận mạnh nhất) nhưng đi kèm rủi ro mua đuổi vì RSI đã cận 70 và nến vào lệnh giãn xa MA20 sau gap tăng lớn.
- **VRE** là ứng viên đáng chú ý thứ hai — vừa cắt lên MA50 với khối lượng tốt và RSI còn dư địa hơn VIC, nhưng tín hiệu đảo chiều còn mới, chưa được kiểm chứng qua thời gian.
- **PNJ, PDR, KDH** đều đang ở dưới MA50 trong xu hướng giảm trung/dài hạn, khối lượng hồi phục yếu (đặc biệt PDR và KDH có vol_ratio <0.8) → rủi ro kỹ thuật lớn nhất nhóm là "bắt dao rơi", nhịp hồi kỹ thuật không có xác nhận dòng tiền.
- Rủi ro kỹ thuật lớn nhất toàn nhóm: **KDH** — downtrend dai dẳng nhất, khối lượng èo uột nhất, chưa có dấu hiệu tạo đáy rõ ràng.
- Về TP (+8%)/SL (−5%) so với vùng hỗ trợ/kháng cự cụ thể: chỉ đối chiếu được bằng mắt qua chart, **chưa kiểm chứng định lượng** (không có dữ liệu vùng S/R tính toán sẵn trong signals_latest.csv). Với VRE, vùng chốt lời 28,080 gần trùng vùng kháng cự cũ tháng 6 (~28–29k) — hợp lý. Với PNJ, vùng chốt lời 45,252 nằm ngay dưới MA50 đang giảm (~45k) nên có thể gặp cản kỹ thuật trước khi đạt TP.
- Lưu ý bắt buộc: mô hình có edge yếu (AUC ~0.53–0.55), các nhận định trên chỉ mang tính xác suất tương đối giữa các mã, không phải tín hiệu chắc chắn.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ** — chỉ là phân tích kỹ thuật độc lập, phục vụ tranh luận nội bộ hội đồng.

Đã ghi vào: `/home/runner/work/vn-stock-market-agent/vn-stock-market-agent/analysis/runs/log_run_2026-08-28_02-05-58/debate/notes/A_technical.md`
