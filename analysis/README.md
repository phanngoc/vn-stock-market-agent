# analysis/ — ML swing-opportunity pipeline (dữ liệu thật)

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Công cụ nghiên cứu/giáo dục. Hiệu suất quá khứ không đảm bảo tương lai.

Pipeline machine-learning tìm cơ hội **swing (lướt sóng)** trên TTCK Việt Nam, dùng **dữ liệu giá thật** lấy qua [`vnstock`](https://github.com/thinh-vu/vnstock) (nguồn VCI/Vietcap). Kết quả đầy đủ: [`results/REPORT.md`](results/REPORT.md).

## Kết quả chính (out-of-sample 2025-01 → 2026-08, đọc kèm hạn chế)

- Thử 5 thuật toán: **Logistic Regression, Random Forest, Gradient Boosting, XGBoost, LSTM (PyTorch)**.
- **Sức dự báo yếu nhưng thực:** AUC ~0.53–0.55 (>0.5). Sau phí, chỉ **LogReg / XGBoost / LSTM** có kỳ vọng dương/hoà mỗi lệnh; cây (RF/GBM) âm.
- Lọc "top 20% tín hiệu tự tin nhất" nâng **win-rate ~0.38 → ~0.41**, vượt breakeven 0.385 (R:R = 8:5).
- **Cảnh báo trung thực:** trong giai đoạn kiểm định (thị trường tăng), **buy & hold ~+35%** — edge của mô hình là *lọc + quản trị rủi ro*, không phải "đánh bại thị trường". Xem mục Hạn chế trong REPORT.

## Cách "sóng" được định nghĩa (triple-barrier)

Vào tại giá đóng cửa; trong tối đa **25 phiên (~5 tuần)**: **chốt lời +8%** (WIN nếu chạm trước) / **cắt lỗ −5%** / hết giờ thì thoát theo giá. Đây vừa là *nhãn ML* vừa là *quy tắc giao dịch* — nên tín hiệu trả lời được "vào mã nào, chốt/cắt ở đâu, giữ bao lâu".

## Chạy

```bash
pip install -r requirements.txt          # vnstock, torch, sklearn, xgboost, pandas, matplotlib
cd analysis && python run_analysis.py    # lần đầu tải dữ liệu (~1 phút) rồi train + backtest + tín hiệu
```

Đầu ra ghi vào [`results/`](results/): `REPORT.md`, `signals_latest.csv`, `model_metrics.csv`,
`backtest_trades_*.csv`, `summary.json`, và 3 biểu đồ PNG (equity, so sánh mô hình, feature importance).

```bash
python plot_signals.py   # vẽ biểu đồ NẾN có điểm MUA + ranh giới chốt lời/cắt lỗ + time-stop
```
Biểu đồ nến ghi vào [`results/charts/`](results/charts/): `overview_top6.png`, `<TICKER>_setup.png` (setup từng mã), `<TICKER>_history.png` (các điểm vào backtest, ▲ xanh=thắng/đỏ=thua).

## Cấu trúc code (`vn_swing/`)

| Module | Vai trò |
|---|---|
| `data.py` | Lấy & cache OHLCV ngày (VCI), vũ trụ 38 mã VN30-heavy |
| `features.py` | 18 chỉ báo kỹ thuật (RSI, MACD, Bollinger, ATR, Stoch, MA, momentum…) thuần pandas |
| `labels.py` | Nhãn triple-barrier (TP/SL/time-stop) + lợi nhuận thực hiện theo quy tắc |
| `dataset.py` | Gộp panel đa mã, tách train/test theo thời gian, lấy hàng mới nhất để chấm live |
| `models.py` | LogReg / RandomForest / GradientBoosting / XGBoost |
| `lstm.py` | LSTM (PyTorch) trên chuỗi 20 phiên, chuẩn hoá bằng thống kê train (không rò rỉ) |
| `backtest.py` | Backtest theo sự kiện, đặt cược cố định, chỉ số win-rate/kỳ vọng/Sharpe/DD + phí |
| `../run_analysis.py` | Orchestrator: chạy tất cả, tự ghi REPORT.md bằng số liệu thật |

## Chống rò rỉ (no look-ahead)

- Feature chỉ dùng thông tin tới ngày *t*; nhãn dùng tương lai *t+1…t+H*; tách train/test theo mốc thời gian.
- LSTM chuẩn hoá bằng mean/std của **train**. Tín hiệu live retrain trên dữ liệu đã có nhãn (resolve ≤ 2026-07-21) rồi mới chấm bar 2026-08-25.

## Điều CHƯA mô phỏng (giới hạn thực tế)

Biên độ trần/sàn ±7% HOSE, T+2 (không bán cùng ngày), khe hở giá & trượt giá khi bán tháo, thanh khoản hạn chế mã nhỏ, thuế cổ tức, giới hạn margin/call. Tham số TP/SL/horizon do người đặt → rủi ro overfitting; **cập nhật lại hàng tuần** và kết hợp phân tích cơ bản ([`../docs/03`](../docs/03-phuong-phap-phan-tich-co-ban.md)) + rủi ro ([`../docs/05`](../docs/05-rui-ro-va-nguon-du-lieu.md)).
