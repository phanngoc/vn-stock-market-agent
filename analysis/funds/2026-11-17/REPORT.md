# Cá mập quỹ đang làm gì? Có copy trade được không? (17/11/2026)

Nội dung giáo dục, không phải khuyến nghị đầu tư.

## 1. Quỹ lớn đang làm gì (tin công bố, 10–11/2026)

| Ngày GD | Quỹ | Mã | Hành động | Sở hữu |
|---|---|---|---|---|
| 04/11, 06–12/11 | Dragon Capital | DXG | Mua ~5 tr cp (04/11) rồi mua ròng ~17,45 tr cp (06–12/11) | 4,96% → 6,19% (78,5 tr cp), trở lại cổ đông lớn |
| 11/11 (CBTT 16/11) | Dragon Capital | TCH | Mua ròng 1,38 tr cp (~19 tỷ) | 4,91% → 5,04%, trở lại cổ đông lớn sau 5 tháng |
| 22/10 | VinaCapital (Liva) | KDC | Bán 1,9 tr cp | 5,2% → 4,5%, rời cổ đông lớn |
| 20/10 | PYN Elite | DSE | Bán 1 tr cp | 8,2% → ~8% |
| 21/10 | HD Capital | AAS | Mua 2 tr cp | 4,4% → 5,2% |
| 02–06/11 | Các quỹ ETF | — | Bị rút ròng ~369 tỷ | — |

Danh mục chậm (factsheet VEIL – quỹ lớn nhất của Dragon, 30/09/2026): ngân hàng 39,5%, bất động sản 19,9%, bán lẻ 10,6%. Top 10: VIC 11,2% · MWG 7,2% · BID 6,5% · VCB 6,4% · VPB 5,5% · TCB 4,6% · VHM 4,5% · CTG 3,7% · HPG 3,6% · MBB 3,3%. P/E danh mục 9,8x FY26.
VCBF-BCF top 5 (09/10): MBB 9,66% · MWG 6,05% · MSN 5,98% · CTG 5,61% · HPG 5,43%.

## 2. Bằng chứng: chính các quỹ đang thua chỉ số

| Quỹ | YTD 2026 | VN-Index cùng kỳ | 5 năm |
|---|---|---|---|
| VEIL NAV (USD, 30/09) | −8,8% | +2,0% | −3,6% vs VNI +26,1% |
| PYN Elite (31/10) | −14,68% | — | — |

VEIL đã mua lại 24,2% số chứng chỉ quỹ từ đầu năm → **phải bán cổ phiếu để có tiền trả**. Một lệnh bán của quỹ không chắc là quỹ thấy cổ phiếu xấu.

## 3. Kiểm chứng: làm theo 11 giao dịch đã công bố thì được gì

Mua/bán theo **giá đóng cửa ngày tin được công bố** (thường chậm 2 phiên so với ngày quỹ giao dịch). Lợi nhuận so với VN-Index. Với lệnh bán, "làm theo" là tránh mã đó, nên vượt chỉ số âm = quỹ đúng. Script: `analysis/scripts/fund_event_study.py`, số liệu: `event_study.csv`.

| Quỹ | Mã | Chiều | Ngày công bố | Quỹ đi trước (%) | +20 phiên vs VNI | Tới 17/11 vs VNI | Quỹ đúng? |
|---|---|---|---|---|---|---|---|
| Dragon (VEIL) | DPG | MUA | 08/01 | +1,8 | +23,9 | −7,2 | ✗ |
| Dragon | MWG | BÁN | 11/02 | +2,9 | −4,3 | −14,6 | ✓ |
| Dragon | PNJ | MUA | 12/02 | +5,0 | +3,3 | **−76,7** | ✗ |
| Dragon | TCH | BÁN | 17/06 | +1,7 | −7,8 | −0,7 | ✓ (sát hoà) |
| Dragon | DXG | BÁN | 16/07 | −0,8 | −8,9 | −5,1 | ✓ |
| Dragon | FRT | BÁN | 17/07 | −1,1 | +31,1 | **+33,0** | ✗ |
| Dragon | PNJ | BÁN | 20/07 | +0,2 | −10,8 | −63,5 | ✓ (bán sau vụ P-Lab 03/07) |
| PYN | DSE | BÁN | 22/10 | +1,8 | – | +1,9 | ✗ (mới 18 phiên) |
| VinaCapital | KDC | BÁN | 26/10 | −0,6 | – | +1,1 | ✗ (mới 16 phiên) |
| Dragon | DXG | MUA | 06/11 | +4,3 | – | +0,4 | – (mới 7 phiên) |
| Dragon | TCH | MUA | 13/11 | −0,7 | – | −1,7 | – (mới 2 phiên) |

Đọc bảng:
- Lệnh **mua** có đủ thời gian kiểm chứng: 0/2 thắng (DPG đi lên rồi về dưới chỉ số; PNJ mất 77% so với VN-Index vì vụ kim cương P-Lab).
- Lệnh **bán** có đủ thời gian kiểm chứng: 4/5 đúng, nhưng lệnh bán PNJ đến *sau* khi giá đã sập. Quỹ phản ứng theo tin, không đoán trước được tin.
- Cột "quỹ đi trước": người làm theo trung bình vào chậm ~1–2% so với giá quỹ được hưởng (DXG: 4,3%).
- Mẫu chỉ có 11 sự kiện, chọn theo tin báo đưa, thiếu phí và thuế. **Không đủ để kết luận thống kê.** Chỉ đủ để nói: làm theo quỹ không phải công thức thắng.

## 4. Vì sao copy trade theo quỹ khó

1. **Chỉ thấy một lát cắt**: quỹ chỉ phải công bố khi vượt hoặc rơi qua mốc 5% hoặc thay đổi 1%. Tức là thấy một phiên trong cả đợt gom kéo dài nhiều tuần.
2. **Trễ**: công bố sau 2–7 ngày. Factsheet tháng ra sau 2–6 tuần.
3. **Lý do khác bạn**: quỹ bán để trả tiền rút vốn/mua lại chứng chỉ (VEIL −24%), cơ cấu theo chỉ số ETF, giới hạn tỷ trọng.
4. **Tầm nhìn khác**: quỹ cầm nhiều năm, chịu được −30%. Người xem nhỏ lẻ thường cắt lỗ −7–10%.
5. **Quỹ có thể sai** và đang thua chỉ số (mục 2).

## 5. Đề xuất cho kênh: "Theo dấu cá mập" thay vì "copy trade"

- Hằng tuần: bảng giao dịch cổ đông lớn của Dragon, VinaCapital, PYN, các ETF (nguồn: CBTT HOSE/HNX, chuyên mục "Chuyển động quỹ đầu tư" của Vietstock).
- **Bảng thành tích công khai**: mỗi giao dịch được ghi lại, sau 20 và 60 phiên tự chấm đúng/sai (chạy lại script này). Đây là thứ phân biệt kênh với các kênh hô "cá mập gom hàng".
- Mỗi tuần một câu hỏi giáo dục: "Quỹ mua TCH lúc 13.600, giá nào là sai?" (điểm cắt lỗ, tỷ trọng) thay vì "mua theo ngay".
- Pháp lý: tại VN, tư vấn đầu tư chứng khoán cần giấy phép. Nội dung miễn phí, mang tính giáo dục, có disclaimer thì an toàn hơn so với gửi tín hiệu mua/bán, nhất là tín hiệu thu phí.

## Nguồn
- vietnambiz 17/11/2026 – Dragon Capital trở lại vị thế cổ đông lớn tại TCH sau 5 tháng
- mekongasean – Sau DXG, Dragon Capital tiếp tục nâng sở hữu…; vietstock 11/2026 – Dragon mua 5 tr cp DXG
- vietstock 01/11/2026 – Chuyển động quỹ đầu tư: VinaCapital rời ghế cổ đông lớn KDC
- vietstock 11/2026 – PYN Elite lỗ gần 15% từ đầu năm; VnEconomy – ETF rút ròng
- vietnamfinance 18/07/2026 (DXG, FRT); thitruongtaichinhtiente 15/02 & 25/02/2026 (MWG, KDH, DPG, PNJ); baodautu (PNJ 07/2026)
- VEIL Factsheet 09/2026 (cdn.dragoncapital.com); VCBF-BCF danh mục 09/10/2026
- Giá: vnstock/VCI (đã điều chỉnh), cập nhật tới 17/11/2026
