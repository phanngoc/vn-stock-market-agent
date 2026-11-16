# Hội đồng đầu tư — tuần 16/11/2026 (brief chung cho 3 agent)

**Câu hỏi của owner:** chọn 10 cổ phiếu tiềm năng cho 3 tháng tới (17/11/2026 → ~16/02/2027), đánh giá cả
**kỹ thuật** lẫn **giá trị**; Bò và Gấu phản biện nhau; Giám đốc đầu tư (CIO) ra hướng hành động
với mục tiêu owner đặt ra: **lãi 120% trong 3 tháng**.

## Bằng chứng (đọc hết trước khi viết)
Thư mục: `analysis/weekly/2026-11-16/`
| File | Nội dung |
|---|---|
| `01_news_radar.md` | Radar tin tuần 09–13/11: VN-Index, khối ngoại, ngành, vĩ mô, lịch sự kiện, nhận định CTCK, 13 mã được khuyến nghị (có nguồn). Mục 8 = độ tin cậy. |
| `evidence_table.csv` | 38 mã universe: giá đóng 13/11, % 1T/3T/1N, cách đỉnh 52 tuần, trên/dưới MA20/50/200, RSI14, KL20/KL60, ATR%, P/E, P/E trung vị 5 năm, P/B, ROE, nợ/vốn, NPL, tăng trưởng LN TTM so cùng kỳ, + điểm mô hình ML (score, p_*). |
| `evidence_extra.csv` | 7 mã ngoài universe từ radar (GMD, HVN, PHR, PVS, VLB, TCX, VIX): kỹ thuật + giá trị, không có điểm ML. |
| `../../runs/latest/` | Run ML (dữ liệu tới 13/11): `REPORT.md`, `model_metrics.csv`, `signals_latest.csv`, `charts/*.png` (biểu đồ nến). |

## Lưu ý dữ liệu (bắt buộc tôn trọng)
- Giá tính bằng **nghìn đồng** (50.10 = 50.100đ). Chỉ số cơ bản là **TTM tới Q3/2026** (Vietcap IQ).
- `ttm_profit_yoy` suy ra từ vốn hoá/PE — có thể méo khi có lãi bất thường (VIC, VHM, POW, PHR, VLB ROE 71% …). Đánh dấu "cần kiểm chứng" thay vì tin mù.
- Mô hình ML có edge **yếu** (AUC ~0.53, win-rate ~39%, kỳ vọng ~+0.04R/lệnh). Điểm ML chỉ là một phiếu, không phải tiên tri.
- Giá mục tiêu CTCK lấy qua nguồn thứ cấp (Việt Báo dẫn MBS) — ghi rõ khi trích.
- Không bịa số. Cần thêm tin cho mã nào thì dùng WebSearch và ghi link + ngày.

## Quy ước viết
- Tiếng Việt, ngắn gọn, có bảng. Mỗi khối mở đầu `### <emoji> <Tên agent> — <vai trò>`.
- Mỗi luận điểm kèm con số + nguồn (file nào / link nào).
- Cuối mỗi file: *Không phải khuyến nghị đầu tư.*
