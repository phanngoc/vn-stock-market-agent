# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-08-26 05:27 · dữ liệu giá as-of **2026-08-26** (vnstock/VCI) · CHỈ tín hiệu quant (chưa tranh luận).*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🔢 Top tín hiệu quant (chưa qua hội đồng tranh luận)

| # | Mã | Ngành | Giá | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **KDH** | RealEstate | 18,200 | 0.59 | 19,656 | 17,290 | 49 | ↓ dưới MA50 |
| 2 | **PNJ** | Retail/Consumer | 42,500 | 0.58 | 45,900 | 40,375 | 59 | ↓ dưới MA50 |
| 3 | **PDR** | RealEstate | 12,550 | 0.57 | 13,554 | 11,922 | 52 | ↓ dưới MA50 |
| 4 | **VIC** | RealEstate | 223,000 | 0.56 | 240,840 | 211,850 | 61 | ↑ trên MA50 |
| 5 | **VRE** | RealEstate | 25,250 | 0.55 | 27,270 | 23,987 | 52 | ↓ dưới MA50 |

*Chạy skill `vn-swing-daily` để có quyết định của hội đồng đầu tư (MUA/THEO DÕI/TRÁNH).*

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.352** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ 4/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, rủi ro cao hơn kèo momentum.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-08-26_05-19-18`. Chạy lại: skill `vn-swing-daily`.*
