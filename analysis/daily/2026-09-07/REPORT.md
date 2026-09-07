# Kết quả phân tích cơ hội swing — TTCK Việt Nam

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả thực nghiệm của một pipeline machine-learning trên dữ liệu quá khứ. Hiệu suất quá khứ **không** đảm bảo tương lai. Mô hình có thể sai; đừng giao dịch chỉ dựa vào file này.

*Sinh tự động bởi [`run_analysis.py`](../run_analysis.py) — mọi số liệu là kết quả tính thật, out-of-sample. Dữ liệu giá tới 2026-09-07 (vnstock/VCI).*

## 1. Thiết lập

- **Vũ trụ cổ phiếu:** 38 mã thanh khoản (VN30-heavy, nhiều ngành).
- **Dữ liệu:** giá ngày 2018-08-02 → 2026-09-07 (sau khi bỏ ~1 năm đầu để 'làm nóng' chỉ báo); huấn luyện < 2025-01-01, **kiểm định out-of-sample ≥ 2025-01-01**.
- **Lưu ý nhãn:** nhãn triple-barrier cần 25 phiên tương lai để 'chốt', nên backtest OOS chỉ tính được tới **2026-07-29**; ~25 phiên gần nhất (tới 2026-09-07) được **chấm điểm live** ở mục 3 nhưng chưa thể backtest.
- **Định nghĩa 'sóng' (triple-barrier):** vào tại giá đóng cửa; **chốt lời +8%**, **cắt lỗ −5%**, **time-stop 25 phiên (~35 ngày lịch, ~5 tuần)**. Nhãn WIN = chạm chốt lời trước cắt lỗ.
- **Chi phí giao dịch:** 0.3%/vòng (phí+thuế+trượt giá). **Quy tắc vào lệnh:** chỉ giao dịch **top 20% tín hiệu tự tin nhất** mỗi mô hình.
- **Mô hình thử:** Logistic Regression, Random Forest, Gradient Boosting, XGBoost, **LSTM (PyTorch)**.

## 2. So sánh mô hình (out-of-sample)

| Mô hình | AUC | Win-rate | Avg net/trade | Kỳ vọng (R) | Σ P&L (cược cố định) | Max DD | #lệnh |
|---|---|---|---|---|---|---|---|
| **LogReg** | 0.5484 | 0.4141 | 0.28% | 0.056 | 181.09% | -275.59% | 652 |
| XGBoost | 0.533 | 0.4091 | 0.24% | 0.048 | 157.83% | -213.46% | 660 |
| LSTM | 0.5187 | 0.395 | 0.19% | 0.038 | 99.33% | -324.71% | 524 |
| RandomForest | 0.537 | 0.3958 | -0.05% | -0.009 | -28.93% | -392.98% | 624 |
| GradBoost | 0.5348 | 0.3838 | -0.15% | -0.029 | -95.33% | -454.45% | 654 |

- **Base win-rate** (vào mọi phiên, không lọc) trên tập kiểm định: **0.356** (breakeven ≈ 0.385 do R:R = 8:5).
- **Buy & hold** trung bình các mã trong kỳ kiểm định: **33.37%** (tham chiếu, không phải cùng cơ sở rủi ro).
- **Mô hình tốt nhất out-of-sample: `LogReg`** (chọn theo avg net/trade với #lệnh ≥ 20).
- AUC quanh 0.5 nghĩa là sức dự báo yếu — hãy đọc mục *Hạn chế*. Ảnh: [`equity_curve.png`](equity_curve.png), [`model_comparison.png`](model_comparison.png), [`feature_importance.png`](feature_importance.png).

## 3. Tín hiệu swing hiện tại (as-of 2026-09-07)

Điểm `score` = trung bình xác suất WIN của các mô hình (đã retrain trên **toàn bộ** dữ liệu có nhãn). Xếp hạng 38 mã; dưới đây **top 10**. Giá đơn vị VND.

| # | Mã | Ngành | Giá | Score | Chốt lời (+8%) | Cắt lỗ (−5%) | RSI | Trend | Vol× |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **PNJ** | Retail/Consumer | 38,550 | 0.6558 | 41,634 | 36,622 | 46 | ↓ dưới MA50 | 0.48 |
| 2 | **VIC** | RealEstate | 249,400 | 0.6474 | 269,352 | 236,930 | 70 | ↑ trên MA50 | 0.21 |
| 3 | **PDR** | RealEstate | 12,000 | 0.5906 | 12,960 | 11,400 | 42 | ↓ dưới MA50 | 0.27 |
| 4 | **VRE** | RealEstate | 27,100 | 0.5469 | 29,268 | 25,745 | 66 | ↑ trên MA50 | 1.24 |
| 5 | **GVR** | Materials | 31,850 | 0.5435 | 34,398 | 30,258 | 54 | ↑ trên MA50 | 0.24 |
| 6 | **KDH** | RealEstate | 17,250 | 0.5052 | 18,630 | 16,388 | 39 | ↓ dưới MA50 | 0.43 |
| 7 | **GAS** | Energy | 83,800 | 0.5005 | 90,504 | 79,610 | 62 | ↑ trên MA50 | 0.28 |
| 8 | **VCI** | Securities | 21,700 | 0.4986 | 23,436 | 20,615 | 47 | ↓ dưới MA50 | 0.60 |
| 9 | **BID** | Bank | 36,350 | 0.4921 | 39,258 | 34,532 | 50 | ↓ dưới MA50 | 0.33 |
| 10 | **SSI** | Securities | 20,900 | 0.4899 | 22,572 | 19,855 | 56 | ↑ trên MA50 | 0.32 |

**Cách đọc / kế hoạch giao dịch (rule-based):**
- **Thời gian vào hàng:** các mã score cao ở trên, ưu tiên mã *trên MA50* (xu hướng lên) và RSI chưa quá nóng (<70). Vào ở phiên kế tiếp, hoặc chờ nhịp chỉnh về vùng MA20 để giá vào tốt hơn.
- **Thời gian ra hàng (chốt lời):** thoát khi **chạm +8%** (mục tiêu chốt lời), hoặc **cắt lỗ tại −5%**, hoặc **hết 25 phiên (~5 tuần)** thì thoát theo giá thị trường. Trong backtest, thời gian giữ trung bình ≈ 6.5 phiên.
- **Khung 3 tháng:** với time-stop ~5 tuần, một mã có thể cho **2–3 nhịp sóng** trong 3 tháng tới (từ 2026-09-07 đến ~2026-12-07). Danh sách nên **cập nhật lại hàng tuần** khi có dữ liệu mới.
- **Bối cảnh (quan trọng):** 5/10 mã trong top đang **dưới MA50** (xu hướng giảm) → phần lớn là kèo **hồi kỹ thuật / bắt đáy** (mean-reversion), rủi ro cao hơn kèo momentum. Ai ngại 'bắt dao rơi' nên ưu tiên mã *trên MA50* hoặc chờ nến xác nhận đảo chiều.
- Bảng máy đọc: [`signals_latest.csv`](signals_latest.csv). Backtest chi tiết: [`backtest_trades_LogReg.csv`](backtest_trades_LogReg.csv), so sánh: [`model_metrics.csv`](model_metrics.csv).

## 4. Biểu đồ nến (dễ nhìn giao dịch)

Tạo/cập nhật bằng `python plot_signals.py` (matplotlib thuần). Mỗi chart gồm: nến OHLC, MA20/MA50, **▲ điểm MUA**, ranh giới **chốt lời +8% (xanh nét đứt)** / **cắt lỗ −5% (đỏ nét đứt)**, và vạch **time-stop 25 phiên** — nhìn phát thấy ngay vào ở đâu, chốt/cắt ở đâu.

![Tổng quan top 6](charts/overview_top6.png)

*Tổng quan top 6 tín hiệu.* Chart từng mã: [`PNJ`](charts/PNJ_setup.png), [`VIC`](charts/VIC_setup.png), [`PDR`](charts/PDR_setup.png), [`VRE`](charts/VRE_setup.png), [`GVR`](charts/GVR_setup.png), [`KDH`](charts/KDH_setup.png).

**Quy tắc chạy thật trong quá khứ** — PNJ: mỗi ▲ là một điểm mô hình từng ra tín hiệu (**xanh = thắng**, chạm +8% trước; **đỏ = thua**), theo đúng luật TP/SL/time-stop:
![PNJ history](charts/PNJ_history.png)

## 5. Hạn chế & cảnh báo (đọc kỹ)

- **Sức dự báo có giới hạn:** giá cổ phiếu gần ngẫu nhiên ngắn hạn; AUC thường chỉ nhỉnh hơn 0.5. Lợi thế (nếu có) đến từ *lọc xác suất* + quản trị rủi ro (R:R, time-stop), không phải 'tiên tri'.
- **Chưa mô phỏng đầy đủ thực tế:** chưa tính biên độ trần/sàn ±7% (HOSE), thanh khoản/khe hở giá, trượt giá lớn khi bán tháo, T+2 (không bán ngay trong ngày), thuế cổ tức, hay giới hạn margin/call.
- **Rủi ro overfitting & regime change:** tham số TP/SL/horizon do người đặt; thị trường 2025–2026 (nâng hạng FTSE, KRX, margin kỷ lục) có thể đổi 'chế độ' làm mô hình quá khứ mất hiệu lực.
- **Không xét cơ bản/định giá/tin tức** — thuần kỹ thuật. Hãy kết hợp khung phân tích cơ bản ([`../docs/03`](../docs/03-phuong-phap-phan-tich-co-ban.md)) và bản đồ rủi ro ([`../docs/05`](../docs/05-rui-ro-va-nguon-du-lieu.md)).
- **Đây là công cụ nghiên cứu/giáo dục.** Quyết định đầu tư là của bạn; cân nhắc tư vấn chuyên môn được cấp phép.

*Chạy lại: `cd analysis && python run_analysis.py`. Tạo lúc dữ liệu 2026-09-07.*
