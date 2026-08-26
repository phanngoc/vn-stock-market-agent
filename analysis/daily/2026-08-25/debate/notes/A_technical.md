### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-08-26 09:05

*Chỉ dùng số trong `signals_latest.csv` (RSI_14, trend_up, vol_ratio) + đọc 5 chart `*_setup.png`. Độc lập với tin tức. Setup KT là xác suất, không phải chắc chắn (edge mô hình yếu, AUC ~0.53–0.55).*

## Bảng chấm điểm kỹ thuật (top 5 ứng viên)

| Mã | Giá (VND) | Trend (vs MA50) | RSI_14 | vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|---|
| **VIC** | 223,800 | ↑ trên MA50 | 61.5 | **1.11** | **7.5** | Setup đẹp nhất: uptrend, nến xanh mạnh bứt khỏi vùng tích lũy 210–222, là mã DUY NHẤT có volume xác nhận (>1). RSI 61 thiên mua nhưng chưa quá mua. SL 212,610 nằm sát cụm MA20/MA50 (~213–215k) → hỗ trợ tốt nhưng dễ bị quét (whipsaw). TP 241,704 trùng đỉnh 06/26 (~242k) → kháng cự thật. |
| **VRE** | 25,500 | ↓ dưới MA50 | 54.4 | 0.71 | 5.5 | Hồi phục từ đáy 07/26 (~21k), giá đang test MA50 (~25.7k) ngay tại đây, MA20 bẻ lên. RSI 54 trung tính. Volume 0.71 (yếu, chưa xác nhận). Đang gặp kháng cự MA50 → cần đóng cửa trên MA50 mới xác nhận. |
| **VCI** | 22,400 | ↓ dưới MA50 | 55.6 | 0.84 | 5.0 | Hồi từ đáy 07/26 (~18k), giá trên MA20 (~21.4k) nhưng dưới/sát MA50 (~22.6k). RSI 56 trung tính. Volume 0.84 (yếu). TP 24,192 vướng cụm kháng cự 06/26 (~24–25k). Kịch bản tương tự VRE nhưng cấu trúc trend hơi yếu hơn. |
| **PDR** | 12,700 | ↓ dưới MA50 | 55.3 | 0.43 | 4.0 | Đáy 07/26 (~11k) đang xây nền, giá vừa vượt MA20 (~12k) nhưng còn xa dưới MA50 (~13.1k). RSI 55. Volume 0.43 — YẾU NHẤT nhóm, gần như èo uột. TP 13,716 nằm TRÊN MA50 → phải phá MA50 mới tới đích. |
| **KDH** | 18,200 | ↓ dưới MA50 | 49.1 | 0.53 | 3.5 | Setup tệ nhất: downtrend dài từ ~28k → ~16.5k, MA50 (~19.4k) vẫn dốc xuống. RSI 49 thấp nhất nhóm. Volume 0.53 yếu. TP 19,656 bị chặn ngay tại MA50 → dư địa lên bị "trần" bởi kháng cự động. Rủi ro bắt dao rơi. |

## Nhận định chung (dựa trên số)

- **Setup đẹp nhất về mặt KT: VIC.** Là mã duy nhất còn trên MA50 (uptrend) VÀ là mã duy nhất có `vol_ratio > 1` (1.11 → volume xác nhận). Các mã còn lại đều dưới MA50 và volume < 1.
- **Rủi ro kỹ thuật lớn nhất — thiếu volume xác nhận:** 4/5 ứng viên (VRE, KDH, PDR, VCI) có `vol_ratio < 1`, PDR (0.43) và KDH (0.53) đặc biệt èo uột → mọi nhịp hồi thiếu dòng tiền, tín hiệu yếu.
- **Cảnh báo "bắt dao rơi":** KDH và PDR còn nằm trong cấu trúc downtrend rõ (dưới MA50, MA50 dốc xuống); tuy đã xây nền ~1 tháng nhưng chưa có tín hiệu đảo chiều bằng volume. Với 2 mã này, TP +8% lại rơi vào/ trên vùng MA50 → kháng cự chặn ngay dư địa lời.
- **VRE & VCI là "canh test MA50":** cả hai đang hồi lên và test MA50 từ dưới. Đây là vùng quyết định — nếu đóng cửa vững trên MA50 kèm volume tăng thì setup cải thiện; nếu không, dễ bị đẩy ngược xuống MA20.
- **Về khung TP/SL chung:** biên SL −5% của nhiều mã (VIC, VRE, VCI) rơi sát cụm MA20/MA50 → hợp lý theo S/R nhưng dễ bị quét khi biến động; TP +8% của VIC/VRE trùng đỉnh cũ (kháng cự thật), của KDH/PDR bị MA50 chặn trước.

> ⚠️ Đây KHÔNG PHẢI khuyến nghị đầu tư. Chỉ là đánh giá setup kỹ thuật (xác suất, edge mô hình yếu); không bàn tin tức/định giá cơ bản. Các mức MA20/MA50 đọc ước lượng từ chart — "chưa kiểm chứng" bằng số tuyệt đối.
