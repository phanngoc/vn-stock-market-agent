---
name: vn-swing-analysis
description: Chạy pipeline ML tìm cơ hội swing (lướt sóng) trên TTCK Việt Nam từ dữ liệu giá thật (vnstock/VCI). Sinh tín hiệu vào/chốt/cắt + biểu đồ nến, ghi vào runs/log_run_<timestamp>/. Dùng khi cần cập nhật tín hiệu swing, backtest mô hình, hoặc lấy dữ liệu đầu vào cho skill vn-swing-debate.
---

# Skill: vn-swing-analysis

Pipeline machine-learning tìm cơ hội **swing** (chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên) trên ~38 mã VN30-heavy, dùng dữ liệu giá thật qua `vnstock` (nguồn VCI). **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**

## Khi nào dùng
- Người dùng muốn "tìm cơ hội swing / lướt sóng", "cập nhật tín hiệu", "chạy lại mô hình", "backtest".
- Cần `signals_latest.csv` làm đầu vào cho skill **vn-swing-debate**.

## Cách chạy
```bash
cd analysis
pip install -r requirements.txt          # lần đầu: vnstock, torch, sklearn, xgboost, pandas, matplotlib
python run_analysis.py                    # fetch (cache) -> features -> 5 mô hình -> backtest OOS -> tín hiệu -> charts
```
Một lần chạy tự làm hết: LogReg, RandomForest, GradientBoosting, XGBoost, LSTM (PyTorch) → backtest out-of-sample → tín hiệu hiện tại → biểu đồ nến.

## Kết quả ghi ở đâu (QUAN TRỌNG — cấu trúc log theo run)
Mỗi lần chạy tạo **một folder riêng để tracking**:
```
analysis/runs/log_run_<YYYY-MM-DD_HH-MM-SS>/
├── REPORT.md                 # báo cáo đầy đủ (tự sinh, số liệu thật)
├── signals_latest.csv        # tín hiệu hiện tại (mã, giá, TP/SL, score, RSI, trend)
├── model_metrics.csv         # so sánh 5 mô hình (AUC, win-rate, avg net/trade…)
├── backtest_trades_<best>.csv
├── summary.json
├── equity_curve.png, model_comparison.png, feature_importance.png
└── charts/                   # overview_top6.png, <TICKER>_setup.png, <TICKER>_history.png
```
- `analysis/runs/latest` = symlink tới run mới nhất.
- `analysis/results/` = **bản mirror của run mới nhất** (giữ link ổn định trong README/REPORT).
- `analysis/runs/` bị gitignore (log cục bộ); chỉ commit run làm ví dụ khi cần.

## Vẽ lại biểu đồ nến cho một run
```bash
python plot_signals.py [run_dir]         # mặc định: runs/latest
```

## Tinh chỉnh (trong run_analysis.py, khối `# ---- config ----`)
`START/END`, `TEST_START` (mốc OOS), `TP/SL/HORIZON` (định nghĩa sóng), `COST` (phí), `TRADE_PCTILE` (lọc top-% tín hiệu), `LSTM_L/LSTM_EPOCHS`. Universe & sector map ở `vn_swing/data.py`.

## Diễn giải trung thực
- AUC ~0.53–0.55 = edge YẾU (đúng bản chất dự báo giá ngắn hạn). Lợi thế đến từ *lọc xác suất + kỷ luật R:R/time-stop*, không phải "tiên tri".
- Trong kỳ thị trường tăng, buy&hold có thể vượt chiến lược. Đọc mục *Hạn chế* trong REPORT.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Cập nhật lại hàng tuần.
