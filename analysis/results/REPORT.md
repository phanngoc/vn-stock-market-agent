# Kết quả phân tích cơ hội swing — TTCK Việt Nam

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả thực nghiệm của một pipeline machine-learning trên dữ liệu quá khứ. Hiệu suất quá khứ **không** đảm bảo tương lai. Mô hình có thể sai; đừng giao dịch chỉ dựa vào file này.

*Sinh tự động bởi [`run_analysis.py`](../run_analysis.py) — mọi số liệu là kết quả tính thật, out-of-sample. Dữ liệu giá tới 2026-08-25 (vnstock/VCI).*

## 1. Thiết lập

- **Vũ trụ cổ phiếu:** 38 mã thanh khoản (VN30-heavy, nhiều ngành).
- **Dữ liệu:** giá ngày 2019-01-03 → 2026-08-25 (sau khi bỏ ~1 năm đầu để 'làm nóng' chỉ báo); huấn luyện < 2025-01-01, **kiểm định out-of-sample ≥ 2025-01-01**.
- **Lưu ý nhãn:** nhãn triple-barrier cần 25 phiên tương lai để 'chốt', nên backtest OOS chỉ tính được tới **2026-07-21**; ~25 phiên gần nhất (tới 2026-08-25) được **chấm điểm live** ở mục 3 nhưng chưa thể backtest.
- **Định nghĩa 'sóng' (triple-barrier):** vào tại giá đóng cửa; **chốt lời +8%**, **cắt lỗ −5%**, **time-stop 25 phiên (~35 ngày lịch, ~5 tuần)**. Nhãn WIN = chạm chốt lời trước cắt lỗ.
- **Chi phí giao dịch:** 0.3%/vòng (phí+thuế+trượt giá). **Quy tắc vào lệnh:** chỉ giao dịch **top 20% tín hiệu tự tin nhất** mỗi mô hình.
- **Mô hình thử:** Logistic Regression, Random Forest, Gradient Boosting, XGBoost, **LSTM (PyTorch)**.

## 2. So sánh mô hình (out-of-sample)

| Mô hình | AUC | Win-rate | Avg net/trade | Kỳ vọng (R) | Σ P&L (cược cố định) | Max DD | #lệnh |
|---|---|---|---|---|---|---|---|
| **LSTM** | 0.5327 | 0.4055 | 0.40% | 0.08 | 203.11% | -162.88% | 508 |
| LogReg | 0.5549 | 0.4091 | 0.20% | 0.039 | 125.95% | -313.67% | 638 |
| XGBoost | 0.5354 | 0.3936 | 0.03% | 0.006 | 18.49% | -289.41% | 653 |
| GradBoost | 0.535 | 0.3846 | -0.16% | -0.032 | -98.91% | -391.04% | 611 |
| RandomForest | 0.5374 | 0.3822 | -0.22% | -0.044 | -134.50% | -476.27% | 607 |

- **Base win-rate** (vào mọi phiên, không lọc) trên tập kiểm định: **0.352** (breakeven ≈ 0.385 do R:R = 8:5).
- **Buy & hold** trung bình các mã trong kỳ kiểm định: **35.32%** (tham chiếu, không phải cùng cơ sở rủi ro).
- **Mô hình tốt nhất out-of-sample: `LSTM`** (chọn theo avg net/trade với #lệnh ≥ 20).
- AUC quanh 0.5 nghĩa là sức dự báo yếu — hãy đọc mục *Hạn chế*. Ảnh: [`equity_curve.png`](equity_curve.png), [`model_comparison.png`](model_comparison.png), [`feature_importance.png`](feature_importance.png).

## 3. Tín hiệu swing hiện tại (as-of 2026-08-25)

Điểm `score` = trung bình xác suất WIN của các mô hình (đã retrain trên **toàn bộ** dữ liệu có nhãn). Xếp hạng 38 mã; dưới đây **top 10**. Giá đơn vị VND.

| # | Mã | Ngành | Giá | Score | Chốt lời (+8%) | Cắt lỗ (−5%) | RSI | Trend | Vol× |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **VRE** | RealEstate | 25,500 | 0.5949 | 27,540 | 24,225 | 54 | ↓ dưới MA50 | 0.71 |
| 2 | **VIC** | RealEstate | 223,800 | 0.587 | 241,704 | 212,610 | 61 | ↑ trên MA50 | 1.11 |
| 3 | **KDH** | RealEstate | 18,200 | 0.5586 | 19,656 | 17,290 | 49 | ↓ dưới MA50 | 0.53 |
| 4 | **PDR** | RealEstate | 12,700 | 0.5435 | 13,716 | 12,065 | 55 | ↓ dưới MA50 | 0.43 |
| 5 | **VCI** | Securities | 22,400 | 0.5393 | 24,192 | 21,280 | 56 | ↓ dưới MA50 | 0.84 |
| 6 | **DXG** | RealEstate | 11,750 | 0.5347 | 12,690 | 11,162 | 58 | ↑ trên MA50 | 0.30 |
| 7 | **PLX** | Energy | 37,500 | 0.5058 | 40,500 | 35,625 | 59 | ↑ trên MA50 | 0.76 |
| 8 | **GAS** | Energy | 82,800 | 0.505 | 89,424 | 78,660 | 61 | ↑ trên MA50 | 0.80 |
| 9 | **GVR** | Materials | 31,850 | 0.5016 | 34,398 | 30,258 | 58 | ↑ trên MA50 | 0.37 |
| 10 | **DGC** | Materials | 44,250 | 0.4989 | 47,790 | 42,038 | 58 | ↑ trên MA50 | 0.67 |

**Cách đọc / kế hoạch giao dịch (rule-based):**
- **Thời gian vào hàng:** các mã score cao ở trên, ưu tiên mã *trên MA50* (xu hướng lên) và RSI chưa quá nóng (<70). Vào ở phiên kế tiếp, hoặc chờ nhịp chỉnh về vùng MA20 để giá vào tốt hơn.
- **Thời gian ra hàng (chốt lời):** thoát khi **chạm +8%** (mục tiêu chốt lời), hoặc **cắt lỗ tại −5%**, hoặc **hết 25 phiên (~5 tuần)** thì thoát theo giá thị trường. Trong backtest, thời gian giữ trung bình ≈ 8.9 phiên.
- **Khung 3 tháng:** với time-stop ~5 tuần, một mã có thể cho **2–3 nhịp sóng** trong 3 tháng tới (từ 2026-08-25 đến ~2026-11-25). Danh sách nên **cập nhật lại hàng tuần** khi có dữ liệu mới.
- Bảng máy đọc: [`signals_latest.csv`](signals_latest.csv). Backtest chi tiết: [`backtest_trades_LSTM.csv`](backtest_trades_LSTM.csv), so sánh: [`model_metrics.csv`](model_metrics.csv).

## 4. Hạn chế & cảnh báo (đọc kỹ)

- **Sức dự báo có giới hạn:** giá cổ phiếu gần ngẫu nhiên ngắn hạn; AUC thường chỉ nhỉnh hơn 0.5. Lợi thế (nếu có) đến từ *lọc xác suất* + quản trị rủi ro (R:R, time-stop), không phải 'tiên tri'.
- **Chưa mô phỏng đầy đủ thực tế:** chưa tính biên độ trần/sàn ±7% (HOSE), thanh khoản/khe hở giá, trượt giá lớn khi bán tháo, T+2 (không bán ngay trong ngày), thuế cổ tức, hay giới hạn margin/call.
- **Rủi ro overfitting & regime change:** tham số TP/SL/horizon do người đặt; thị trường 2025–2026 (nâng hạng FTSE, KRX, margin kỷ lục) có thể đổi 'chế độ' làm mô hình quá khứ mất hiệu lực.
- **Không xét cơ bản/định giá/tin tức** — thuần kỹ thuật. Hãy kết hợp khung phân tích cơ bản ([`../docs/03`](../docs/03-phuong-phap-phan-tich-co-ban.md)) và bản đồ rủi ro ([`../docs/05`](../docs/05-rui-ro-va-nguon-du-lieu.md)).
- **Đây là công cụ nghiên cứu/giáo dục.** Quyết định đầu tư là của bạn; cân nhắc tư vấn chuyên môn được cấp phép.

*Chạy lại: `cd analysis && python run_analysis.py`. Tạo lúc dữ liệu 2026-08-25.*
