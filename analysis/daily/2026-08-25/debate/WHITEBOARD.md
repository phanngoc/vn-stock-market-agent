# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-08-25)

*Board tạo lúc 2026-08-26 09:04:29. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LSTM** · base win-rate **0.352** · buy&hold kỳ kiểm định **0.3532**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): VRE, VIC, KDH, PDR, VCI
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **VRE** | RealEstate | 25,500 | 0.59 | 27,540 | 24,225 | 54 | ↓ dưới MA50 |
| 2 | **VIC** | RealEstate | 223,800 | 0.59 | 241,704 | 212,610 | 61 | ↑ trên MA50 |
| 3 | **KDH** | RealEstate | 18,200 | 0.56 | 19,656 | 17,290 | 49 | ↓ dưới MA50 |
| 4 | **PDR** | RealEstate | 12,700 | 0.54 | 13,716 | 12,065 | 55 | ↓ dưới MA50 |
| 5 | **VCI** | Securities | 22,400 | 0.54 | 24,192 | 21,280 | 56 | ↓ dưới MA50 |

## 👥 Roster & thứ tự
1. 🅰️ **Agent A — Kỹ thuật** và 🅱️ **Agent B — News/Cơ bản** viết bằng chứng độc lập (song song).
2. 🐂 **Agent C — BÒ** đọc A+B, dựng luận điểm mua mạnh nhất.
3. 🐻 **Agent D — GẤU** đọc A+B+C, dựng luận điểm bán/tránh và **phản biện trực tiếp C**.
4. 🎩 **Agent E — Giám đốc Chiến lược** đọc toàn bộ, ra **quyết định cuối** (xem `DECISION.md`).

## ✍️ Quy ước viết
- Mỗi ý kiến bắt đầu bằng tiêu đề: `### <emoji> Agent X — <vai trò> · <thời gian>`.
- Trích nguồn/số liệu khi có (RSI, giá, tin + link). Nói thẳng độ không chắc chắn.
- Được phép trích tên agent khác để phản biện: "Agent C cho rằng… nhưng…".

---

# 🗣️ PHIÊN 1 — BẰNG CHỨNG (Agent A & B)

*(A và B điền khối của mình vào đây / hoặc ghi ở `notes/` rồi orchestrator gộp lên.)*

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

### 🅱️ Agent B — Phân tích News / Cơ bản · 2026-08-26 09:15

*Dữ liệu as-of 2026-08-25. Ứng viên top 5: VRE, VIC, KDH, PDR, VCI (4 BĐS + 1 Chứng khoán). Mỗi khẳng định kèm link nguồn; phân biệt rõ **[ĐÃ XẢY RA]** vs **[KỲ VỌNG]**. Không tìm thấy tin → ghi "chưa kiểm chứng".*

---

## 🏬 VRE — Vincom Retail (BĐS bán lẻ)
- **[ĐÃ XẢY RA] Tích cực** — Lọt rổ nâng hạng FTSE (nhóm Small Cap) trong danh sách 27 mã công bố 21/8/2026 → hưởng lợi dòng vốn thụ động khi có hiệu lực 21/9. Nguồn: https://elibook.vn/2026/08/22/nang-hang-ftse-27-cai-ten-da-chot-nhung-dung-tuong-tien-ty-do-do-vao-sau-mot-dem/
- **[ĐÃ XẢY RA] Tích cực** — Q1/2026 lãi >1.600 tỷ (kỷ lục), doanh thu đạt ~25% & lợi nhuận ~30% kế hoạch năm; lượng khách và doanh thu khách thuê tăng 13–25% cùng kỳ. Nguồn: https://nguoiquansat.vn/dhdcd-vincom-retail-vre-he-lo-ket-qua-kinh-doanh-an-tuong-lai-hon-1-600-ty-dong-quy-i-2026-287786.html
- **[KỲ VỌNG] Tích cực** — Kế hoạch 2026: doanh thu 10.132 tỷ (+16%), LNST 5.375 tỷ (+15%), chốt **cổ tức tiền mặt 10%**; đẩy dòng sản phẩm Vincom Collection. Nguồn: https://baophapluat.vn/dhdcd-vincom-retail-vre-2026-ke-hoach-lai-5-375-ty-dong-chot-chia-co-tuc-tien-mat-ty-le-10.html · https://www.tinnhanhchungkhoan.vn/vincom-retail-vre-dat-muc-tieu-doanh-thu-10132-ty-dong-nam-2026-post388253.html
- *Lưu ý:* ngày GDKHQ cụ thể của cổ tức tiền mặt 10% — chưa kiểm chứng (cần xem công bố sàn).

## 🏙️ VIC — Tập đoàn Vingroup (BĐS/đa ngành)
- **[ĐÃ XẢY RA] Tích cực** — Lọt rổ FTSE nhóm **Large Cap** (cùng VCB, VHM) — mã hưởng lợi lớn nhất từ dòng vốn nâng hạng. Nguồn: https://elibook.vn/2026/08/22/nang-hang-ftse-27-cai-ten-da-chot-nhung-dung-tuong-tien-ty-do-do-vao-sau-mot-dem/
- **[ĐÃ XẢY RA] Trung tính→thận trọng** — Cổ phiếu VIC tăng ~60% trong 1 tháng, đưa Vingroup vào top 5 vốn hóa Đông Nam Á (giá ~205.000đ ngày 21/8). Đà tăng nóng → rủi ro định giá/chốt lời. Nguồn: https://vnexpress.net/tag/vic-5697
- **[KỲ VỌNG] Tích cực** — Kế hoạch doanh thu 2026 ~450.000 tỷ (+~36%); hệ sinh thái vận hành ~12 đại dự án hạ tầng/BĐS. Nguồn: https://finance.vietstock.vn/vic/tin-tuc-su-kien.htm
- **[ĐÃ XẢY RA] Tiêu cực (pha loãng)** — Kế hoạch phát hành cổ phiếu trả cổ tức/thưởng tỷ lệ lớn (nguồn nêu 12,5% cổ phiếu; tin tháng 7 nêu thưởng ~3,85 tỷ cp tỷ lệ 1:1) → giá tham chiếu sẽ bị điều chỉnh; **ngày GDKHQ chính xác chưa kiểm chứng**. Nguồn: https://doanhnhan.baophapluat.vn/vingroup-vic-chot-quyen-phat-hanh-co-phieu-tra-co-tuc-125-42241.html
- *Rủi ro:* Q2/2026 có nghĩa vụ >36.600 tỷ tiền thuê/thuế đất với Nhà nước; áp lực dòng tiền cho GPMB các dự án. (theinvestor/RFA — coi là tham khảo, cần đối chiếu công bố chính thức). Nguồn: https://finance.vietstock.vn/vic/tin-tuc-su-kien.htm

## 🏗️ KDH — Nhà Khang Điền (BĐS)
- **[ĐÃ XẢY RA] Trung tính (chất lượng lợi nhuận thấp)** — Q2/2026 LNST kỷ lục ~750 tỷ (gấp ~4 lần cùng kỳ) NHƯNG chủ yếu từ **doanh thu tài chính đột biến** (thoái 2% vốn Bình Trưng New ~68 tỷ, hạch toán đánh giá lại), KHÔNG từ bán nhà; **doanh thu bán hàng -85%**, dòng tiền KD 6 tháng **âm >1.480 tỷ**. Nguồn: https://vietstock.vn/2026/07/khang-dien-lap-ky-luc-loi-nhuan-bang-mot-thuong-vu-thoai-von-737-1474200.htm · https://elibook.vn/2026/08/05/khoan-lai-tai-chinh-dot-bien-cua-kdh-trong-quy-2-tu-dau-ra
- **[ĐÃ XẢY RA] Tích cực** — ĐHĐCĐ 2026: đã **sạch nợ trái phiếu**, "nói không" với phát hành vốn mới → giảm rủi ro pha loãng & rủi ro trái phiếu. Nguồn: https://doanhnhan.baophapluat.vn/dhdcd-khang-dien-kdh-2026-sach-no-trai-phieu-noi-khong-voi-phat-hanh-von-moi-va-muc-tieu-lai-1-500-ty-dong.html
- **[KỲ VỌNG] Tích cực** — Kế hoạch 2026: doanh thu 4.200 tỷ, LNST 1.500 tỷ (+43,5%); động lực chính là dự án Gladia by the Waters (hợp tác Keppel). Nguồn: https://baodautu.vn/nha-khang-dien-len-ke-hoach-lai-1500-ty-dong-trong-nam-2026-d558641.html
- **[ĐÃ XẢY RA] Trung tính** — **KHÔNG** có tên trong danh sách 27 mã FTSE (không có catalyst nâng hạng trực tiếp). Nguồn: https://elibook.vn/2026/08/22/nang-hang-ftse-27-cai-ten-da-chot-nhung-dung-tuong-tien-ty-do-do-vao-sau-mot-dem/

## 🏢 PDR — Phát Đạt (BĐS)
- **[ĐÃ XẢY RA] Trung tính→tiêu cực (dòng tiền)** — 10/8/2026 hoàn tất thanh toán **7.666 tỷ** để nhận 35% Lotte Properties HCMC (dự án Lotte Eco Smart City Thủ Thiêm) → chi tiền lớn, tăng đòn bẩy/áp lực dòng tiền ngắn hạn. Nguồn: https://nguoiquansat.vn/phat-dat-pdr-bao-doanh-thu-quy-ii-2026-tang-169-307577.html
- **[ĐÃ XẢY RA] Trung tính (chất lượng doanh thu)** — Q2/2026 doanh thu +169% nhưng chủ yếu từ mảng dịch vụ; doanh thu **bán bất động sản chỉ ~2 tỷ** (bán hàng ế ẩm). Nguồn: https://nguoiquansat.vn/phat-dat-pdr-bao-doanh-thu-quy-ii-2026-tang-169-307577.html
- **[KỲ VỌNG] Tích cực (dài hạn)** — Công bố chiến lược 2026–2030: doanh thu ~44.848 tỷ (~1,5 tỷ USD), LNST ~11.812 tỷ; kế hoạch doanh thu 2026 ~3.541 tỷ. Bài báo nêu công bố trong bối cảnh **thị giá giảm sâu**. Nguồn: https://doanhnhan.baophapluat.vn/phat-dat-pdr-cong-bo-chien-luoc-lai-12000-ty-dong-giai-doan-toi-khi-thi-gia-co-phieu-giam-sau-89734.html · https://mekongasean.vn/phat-dat-dat-muc-tieu-doanh-thu-45000-ty-do-ng-giai-doan-2026-2030-49743.html
- **[ĐÃ XẢY RA] Trung tính** — **KHÔNG** có trong rổ FTSE 27 mã (không có catalyst nâng hạng). Nguồn: https://elibook.vn/2026/08/22/nang-hang-ftse-27-cai-ten-da-chot-nhung-dung-tuong-tien-ty-do-do-vao-sau-mot-dem/

## 📈 VCI — Chứng khoán Vietcap (Securities)
- **[ĐÃ XẢY RA] Tích cực** — Lọt rổ FTSE nhóm Small Cap → nhóm chứng khoán nói chung hưởng lợi kép (vừa là mã trong rổ, vừa hưởng thanh khoản tăng khi vốn ngoại vào). Nguồn: https://elibook.vn/2026/08/22/nang-hang-ftse-27-cai-ten-da-chot-nhung-dung-tuong-tien-ty-do-do-vao-sau-mot-dem/
- **[ĐÃ XẢY RA] Tiêu cực** — 6 tháng 2026 mới đạt **~29% kế hoạch lợi nhuận năm**; **tự doanh báo lỗ**, thu nhập toàn diện **âm 432 tỷ** do danh mục AFS giảm giá → chất lượng lợi nhuận kém, rủi ro nếu thị trường điều chỉnh. Nguồn: https://doanhnghiephoinhap.vn/vietcap-moi-hoan-thanh-29-ke-hoach-loi-nhuan-sau-nua-nam-143926.html · https://doanhnhan.baophapluat.vn/tu-doanh-bao-lo-chung-khoan-vietcap-vci-chat-vat-voi-muc-tieu-loi-nhuan-nam.html
- **[ĐÃ XẢY RA] Tích cực** — Dư nợ margin kỷ lục ~16.646 tỷ (thu lãi margin +80% cùng kỳ); mảng IB dự kiến tăng ~40% doanh thu (đang tư vấn thương vụ 400–500 triệu USD). Nguồn: https://24hmoney.vn/news/vci-diem-roi-loi-nhuan-tu-sieu-thuong-vu-ipo-2026-c30a2773698.html
- **[KỲ VỌNG] Tích cực** — Kế hoạch 2026: tổng doanh thu 6.525 tỷ, LNTT 2.300 tỷ (+41%). Nguồn: https://doanhnhan.baophapluat.vn/dhdcd-2026-chung-khoan-vietcap-vci-chot-muc-tieu-lai-2-300-ty-dong-lo-dien-nhom-co-dong-nam-giu-30-von-dieu-le.html

---

## 📅 Sự kiện sắp tới (catalyst)
- **21/9/2026 — FTSE nâng hạng có hiệu lực (đợt phân bổ đầu tiên).** Lộ trình 4 đợt (T9/2026 → T9/2027, tỷ lệ 10%/20%/35%/35%); kỳ vọng ~5–8 tỷ USD tổng vốn (active+passive), riêng vốn thụ động ~1,45–1,5 tỷ USD. **Đây là KỲ VỌNG dòng tiền, không phải đã giải ngân** — dòng vốn vào từ từ theo đợt, không "một đêm". Nguồn: https://vn.investing.com/news/stock-market-news/ftse-nang-hang-27-co-phieu-viet-nam-co-the-hut-145-ty-usd-von-thu-dong-2697865 · https://elibook.vn/2026/08/22/nang-hang-ftse-27-cai-ten-da-chot-nhung-dung-tuong-tien-ty-do-do-vao-sau-mot-dem/
- **VIC — GDKHQ phát hành cổ phiếu trả cổ tức/thưởng:** kế hoạch có, ngày chính xác **chưa kiểm chứng** (theo dõi công bố HOSE/VSD). Nguồn: https://doanhnhan.baophapluat.vn/vingroup-vic-chot-quyen-phat-hanh-co-phieu-tra-co-tuc-125-42241.html
- **VRE — GDKHQ cổ tức tiền mặt 10%:** ngày cụ thể **chưa kiểm chứng**. Nguồn: https://baophapluat.vn/dhdcd-vincom-retail-vre-2026-ke-hoach-lai-5-375-ty-dong-chot-chia-co-tuc-tien-mat-ty-le-10.html
- KDH/PDR: chưa thấy GDKHQ/sự kiện lịch cụ thể trong vài tuần tới — chưa kiểm chứng.

## 🌐 Bối cảnh chung (vĩ mô/ngành)
- **Thị trường:** Cuối tháng 8/2026 VN-Index quanh **1.768 điểm**, dòng tiền trở lại, kỳ vọng thử lại vùng **1.800**. Ngày 25/8 tăng nhưng phân hóa cao & gặp kháng cự mạnh. Nguồn: https://thoibaotaichinhvietnam.vn/chung-khoan-tuan-cuoi-thang-8-2026-dong-tien-tro-lai-vn-index-se-tai-thu-suc-moc-1-800-diem-202776.html · https://baomoi.com/chung-khoan-hom-nay-25-8-2026-vn-index-tang-diem-muc-do-phan-hoa-cao-c55910841.epi
- **Khối ngoại — biến động 2 chiều:** Tuần 10–14/8 bán ròng >2.100 tỷ (VN-Index -38,98đ); nhưng 21/8 quay lại mua ròng, VN-Index +33,38đ (+1,95%). Dòng ngoại chưa ổn định. Nguồn: https://baomoi.com/chung-khoan-tuan-10-14-8-vn-index-roi-38-98-diem-khoi-ngoai-ban-rong-hon-2-100-ty-dong-c55840442.epi · https://vietstock.vn/2026/08/nhip-dap-thi-truong-2108-khoi-ngoai-quay-lai-mua-rong-vn-index-but-pha-cung-thanh-khoan-hoi-phuc-1636-1483481.htm
- **Chủ đề dẫn dắt:** Câu chuyện nâng hạng FTSE (21/9) đang là catalyst chính, ưu tiên VN30/vốn hóa lớn thanh khoản cao. Nhóm **chứng khoán** hưởng lợi gián tiếp từ thanh khoản/margin tăng; nhóm **BĐS** phân hóa mạnh theo pháp lý dự án & chất lượng dòng tiền.

---

## 🏁 Xếp hạng theo HỖ TRỢ TIN TỨC (mạnh → yếu)
1. **VIC** — Catalyst mạnh nhất: FTSE Large Cap + đà tăng + kế hoạch lớn. *Đối trọng:* đã tăng ~60%/tháng (rủi ro định giá) + sự kiện pha loãng cổ phiếu sắp tới.
2. **VRE** — FTSE Small Cap + KQKD Q1 kỷ lục + cổ tức tiền mặt 10%; cơ bản vững, ít tin xấu.
3. **VCI** — Trong rổ FTSE + margin/IB tăng, NHƯNG tự doanh lỗ & mới đạt 29% kế hoạch → tin tức hai chiều.
4. **KDH** — Sạch nợ trái phiếu (tốt) nhưng lợi nhuận Q2 "ảo" (từ thoái vốn), bán nhà -85%, dòng tiền âm; không có catalyst FTSE.
5. **PDR** — Chi 7.666 tỷ thương vụ Lotte (áp lực dòng tiền), bán hàng ~2 tỷ, thị giá giảm sâu; câu chuyện dài hạn nhưng thiếu catalyst ngắn hạn & ngoài rổ FTSE.

> ⚠️ **Đây KHÔNG PHẢI khuyến nghị đầu tư.** Bản ghi chỉ tổng hợp tin tức/cơ bản kèm nguồn để hội đồng tham chiếu; edge mô hình định lượng yếu (AUC ~0,53–0,55). Các số liệu KQKD chưa đối chiếu BCTC gốc; catalyst nâng hạng là **kỳ vọng dòng vốn**, giải ngân theo lộ trình chứ chưa xảy ra toàn bộ. Mục nào ghi "chưa kiểm chứng" cần xác minh thêm ở công bố HOSE/VSD.



---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

### 🐂 Agent C — Tổng hợp hướng BÒ · 2026-08-26 09:25

*Dữ liệu as-of 2026-08-25. Luận điểm MUA được dựng CHỈ từ điểm tích cực CÓ THẬT trong note Agent A (kỹ thuật) và Agent B (news). Không thêm dữ kiện mới ngoài whiteboard; suy luận logic được ghi rõ. Thừa nhận edge mô hình yếu (AUC ~0,53–0,55) → luận điểm bò đứng nhờ catalyst + kỹ thuật, KHÔNG chỉ nhờ score.*

---

## 🏙️ VIC — Vingroup (giá 223.800 · score 0,587 · rank 2)

**Luận điểm mua (setup + catalyst):**
Đây là kèo có sự đồng thuận HAI CHIỀU rõ nhất — kỹ thuật lẫn tin tức cùng chỉ về một hướng.
- **Kỹ thuật (Theo Agent A):** VIC được chấm **7,5/10 — setup đẹp nhất nhóm**, và là mã **DUY NHẤT** đồng thời (1) còn trên MA50 (uptrend thực sự) và (2) có `vol_ratio > 1` (1,11 → volume xác nhận, trong khi 4 mã còn lại đều <1). Agent A mô tả "nến xanh mạnh bứt khỏi vùng tích lũy 210–222". RSI 61,5 "thiên mua nhưng chưa quá mua" → còn dư địa trước vùng quá mua.
- **Catalyst (Agent B nêu tin):** VIC lọt rổ **FTSE nhóm Large Cap** [ĐÃ XẢY RA, công bố 21/8/2026] và được Agent B xếp **hạng 1 về hỗ trợ tin tức**, mô tả là "mã hưởng lợi lớn nhất từ dòng vốn nâng hạng". Kèm kế hoạch doanh thu 2026 ~450.000 tỷ (+~36%) [KỲ VỌNG].

**Kịch bản giá tới TP +8%:** 223.800 → **TP 241.704** (khớp CSV). Agent A xác nhận TP này "trùng đỉnh 06/26 (~242k) → kháng cự thật" — nghĩa là mục tiêu bám đúng mốc S/R có thật, không phải con số bịa. Với volume đã xác nhận + catalyst FTSE làm chất xúc tác dòng tiền, việc test lại đỉnh cũ là kịch bản hợp lý (suy luận). R:R ≈ 1,6 (lời 17.904 / lỗ 11.190).

**Rủi ro & vì sao chịu được:** Lo ngại lớn nhất (Agent B) là VIC đã **tăng ~60%/tháng** (rủi ro định giá) và có **sự kiện phát hành cổ phiếu trả cổ tức/thưởng** gây pha loãng. Phản biện: (a) SL −5% ở 212.610 nằm sát cụm MA20/MA50 (~213–215k) — theo Agent A là "hỗ trợ tốt", nên nếu điều chỉnh giá về vùng hỗ trợ động là điểm thoát kỷ luật; (b) time-stop 25 ngày cắt sớm nếu đà tăng hụt hơi; (c) ngày GDKHQ pha loãng **chưa kiểm chứng** — chưa phải rủi ro tức thời trong khung swing, và giá tham chiếu điều chỉnh không đồng nghĩa mất vốn nếu canh trước lịch chốt quyền.

---

## 🏬 VRE — Vincom Retail (giá 25.500 · score 0,5949 · rank 1)

**Luận điểm mua (setup + catalyst):**
Đây là kèo "chất lượng cơ bản + score cao nhất" — an toàn về nội tại nhất trong nhóm.
- **Score mô hình cao nhất bảng (0,5949)** và p_LSTM rất cao (0,845) — dù edge tổng thể yếu, VRE vẫn là mã được ensemble ưu tiên số 1 (dùng làm tie-breaker, không phải trụ chính).
- **Catalyst & cơ bản (Agent B nêu tin):** Agent B xếp VRE **hạng 2 hỗ trợ tin tức**, đánh giá "cơ bản vững, ít tin xấu". Cụ thể: lọt rổ **FTSE Small Cap** [ĐÃ XẢY RA]; **Q1/2026 lãi kỷ lục >1.600 tỷ** (đạt ~25% doanh thu & ~30% lợi nhuận kế hoạch năm ngay quý đầu; khách thuê +13–25%) [ĐÃ XẢY RA]; kế hoạch 2026 doanh thu +16%, LNST +15% và **chốt cổ tức tiền mặt 10%** [KỲ VỌNG]. Đây là mã có **nhiều điểm tích cực [ĐÃ XẢY RA] nhất**, ít phụ thuộc kỳ vọng suông.
- **Kỹ thuật (Theo Agent A):** 5,5/10 — "hồi phục từ đáy 07/26 (~21k)", "MA20 bẻ lên", đang test MA50 (~25,7k) ngay tại giá hiện tại. Đây là điểm quyết định: một phiên đóng cửa vững trên MA50 kèm volume tăng sẽ kích hoạt xác nhận setup (Agent A).

**Kịch bản giá tới TP +8%:** 25.500 → **TP 27.540** (khớp CSV). Kịch bản bò: catalyst FTSE (hiệu lực 21/9) + KQKD kỷ lục làm chất xúc tác giúp giá đóng cửa vượt MA50, mở đường lên vùng TP (suy luận dựa trên setup "test MA50" của Agent A). R:R ≈ 1,6.

**Rủi ro & vì sao chịu được:** Điểm yếu KT là **volume 0,71 (yếu, chưa xác nhận)** và giá đang vướng kháng cự MA50 (Agent A). Phản biện: (a) khác với KDH/PDR, VRE có nền cơ bản [ĐÃ XẢY RA] chống lưng nên nhịp hồi có "lý do", không phải bắt dao rơi thuần kỹ thuật; (b) SL −5% ở 24.225 nằm dưới vùng hỗ trợ đang hình thành → khung R:R rõ ràng; (c) nếu không đóng cửa được trên MA50, time-stop 25 ngày và SL bảo vệ vốn — chi phí thử sai được giới hạn.

---

## 📈 VCI — Chứng khoán Vietcap (giá 22.400 · score 0,5393 · rank 5)

**Luận điểm mua (setup + catalyst):** Kèo "ăn theo chủ đề nâng hạng" — đòn bẩy gián tiếp mạnh nhất vào catalyst FTSE.
- **Catalyst kép (Agent B nêu tin):** VCI vừa **lọt rổ FTSE Small Cap** [ĐÃ XẢY RA], vừa thuộc nhóm **chứng khoán hưởng lợi kép** (là mã trong rổ + hưởng thanh khoản/margin tăng khi vốn ngoại vào). Agent B ghi nhận **dư nợ margin kỷ lục ~16.646 tỷ (lãi margin +80% cùng kỳ)** và **mảng IB dự kiến +40% doanh thu** (đang tư vấn thương vụ 400–500 triệu USD) [ĐÃ XẢY RA]; kế hoạch 2026 LNTT +41% [KỲ VỌNG].
- **Kỹ thuật (Theo Agent A):** 5,0/10 — "hồi từ đáy 07/26 (~18k), giá trên MA20 (~21,4k)", cấu trúc hồi phục tương tự VRE.
- **Tín hiệu mô hình:** p_LSTM rất cao (0,878) — cao nhất nhóm ứng viên (ghi nhận, không phải trụ chính vì edge yếu).

**Kịch bản giá tới TP +8%:** 22.400 → **TP 24.192** (khớp CSV). Kịch bản bò: nếu VN-Index thử lại vùng 1.800 (bối cảnh Agent B nêu) và thanh khoản tăng theo dòng vốn FTSE, nhóm chứng khoán/margin là bên hưởng lợi trực tiếp → VCI có dư địa lên TP (suy luận). R:R ≈ 1,6.

**Rủi ro & vì sao chịu được:** Tin tức HAI CHIỀU — Agent B nêu **tự doanh báo lỗ, thu nhập toàn diện âm 432 tỷ, mới đạt ~29% kế hoạch lợi nhuận nửa năm**, và Agent A lưu ý giá "dưới/sát MA50 (~22,6k)" với volume 0,84 yếu. Phản biện trung thực: đây là kèo rủi ro cao hơn VIC/VRE, nên vị thế nhỏ hơn; SL −5% (21.280) và time-stop 25 ngày là lớp bảo vệ; luận điểm bò VCI chủ yếu là **beta vào catalyst nâng hạng**, không dựa vào chất lượng lợi nhuận quý gần nhất.

---

## 🎯 Phản biện trước các lo ngại chung (chuẩn bị cho Agent D gấu)

- **"Volume 4/5 mã <1, thiếu xác nhận" (Agent A):** Đúng — nhưng VIC (1,11) đã có xác nhận, và VRE/VCI đang ở đúng điểm test MA50, nơi volume có thể bùng khi catalyst FTSE (21/9) đến gần. Ta MUA khi có tín hiệu vượt MA50 kèm volume, không MUA mù.
- **"Catalyst FTSE là kỳ vọng, không phải đã giải ngân" (Agent B):** Ghi nhận — dòng vốn vào theo 4 đợt (10/20/35/35%), không "một đêm". Nhưng thị trường thường chạy trước kỳ vọng; khung swing 25 ngày đủ để bắt nhịp định giá lại trước mốc hiệu lực 21/9 (suy luận).
- **"Edge mô hình yếu (AUC 0,53–0,55)":** Thừa nhận hoàn toàn. Vì thế cả 3 kèo đều KHÔNG dựa vào score làm trụ chính, mà dựa vào catalyst [ĐÃ XẢY RA] + setup S/R có thật; R:R ~1,6 và time-stop là cơ chế sống sót khi mô hình sai.
- **"Khối ngoại biến động 2 chiều" (Agent B):** Đúng (tuần 10–14/8 bán ròng >2.100 tỷ). Nhưng 21/8 đã quay lại mua ròng (+1,95%); xu hướng chủ đề nâng hạng ưu tiên vốn hóa lớn thanh khoản cao → củng cố luận điểm VIC.

---

## 🏁 Kèo bò tự tin nhất

**VIC** — là ứng viên DUY NHẤT hội tụ cả ba: setup kỹ thuật đẹp nhất (Agent A: 7,5/10, uptrend + volume xác nhận), catalyst tin tức mạnh nhất (Agent B: hạng 1, FTSE Large Cap [ĐÃ XẢY RA]), và TP bám đúng mốc kháng cự thật — nên luận điểm mua đứng vững mà không cần dựa vào edge mô hình.

> ⚠️ **Đây KHÔNG PHẢI khuyến nghị đầu tư.** Bản ghi chỉ khuếch đại điểm tích cực có thật từ note A/B để hội đồng phản biện; edge mô hình yếu, catalyst nâng hạng là kỳ vọng dòng vốn (giải ngân theo lộ trình), các mốc MA/GDKHQ nhiều chỗ "chưa kiểm chứng". Cần đối chiếu công bố HOSE/VSD trước mọi quyết định.


---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

### 🐻 Agent D — Tổng hợp hướng GẤU + phản biện · 2026-08-26 09:35

*Dữ liệu as-of 2026-08-25. Nhiệm vụ: stress-test luận điểm bò của Agent C bằng rủi ro CÓ THẬT trong note A+B + logic. Không bịa tin xấu; suy đoán ghi rõ "giả định". Đây KHÔNG PHẢI khuyến nghị đầu tư.*

---

## 🎯 Phản biện Agent C (đối chiếu từng điểm)

### 🏙️ VIC — kèo "tự tin nhất" của C, nhưng là bẫy mua đuổi

- **Agent C cho rằng** "đồng thuận hai chiều rõ nhất, setup đẹp nhất, mua khi có xác nhận volume." **Nhưng** cả hai chân của luận điểm đều đã cũ tin: chính Agent B ghi **VIC đã tăng ~60% trong 1 tháng [ĐÃ XẢY RA]** và catalyst FTSE Large Cap **công bố 21/8** — nghĩa là mua ở giá 223.800 với RSI 61,5 là **mua ĐUỔI sau nhịp +60%, sau khi tin đã ra**. Đây là mua đỉnh xác nhận, không phải mua nền.
- **"Volume xác nhận (1,11)":** vol_ratio 1,11 chỉ nhỉnh hơn 1 một chút — **một cây nến mạnh**, chưa phải tích lũy dòng tiền bền. Sau +60%, nến xanh volume cao cũng có thể là **phân phối đỉnh** (giả định — không xác định được bên mua/bán từ vol_ratio đơn thuần).
- **"TP 241.704 trùng đỉnh cũ = mục tiêu bám S/R thật":** Agent A gọi đúng đây là **kháng cự thật**. Điều đó chống lại C: mục tiêu +8% đâm thẳng vào vùng bị chặn có thật → dư địa lời hẹp và xác suất bị đẩy ngược (rejection) cao. R:R 1,6 tính trên giả định TP đạt sạch — không tính chi phí "test đỉnh rồi rớt".
- **Rủi ro pha loãng mà C gạt đi:** Agent B nêu **[ĐÃ XẢY RA] kế hoạch phát hành cổ phiếu trả cổ tức/thưởng tỷ lệ lớn** (nguồn nêu 12,5%; tin T7 nêu thưởng ~3,85 tỷ cp tỷ lệ 1:1). C nói "GDKHQ chưa kiểm chứng nên chưa phải rủi ro tức thời" — **ngược logic**: chính vì **không biết ngày chốt quyền** mà vị thế swing giữ tới 25 ngày có nguy cơ **kẹp đúng ngày GDKHQ trong khung**. Giá tham chiếu điều chỉnh mạnh + tâm lý pha loãng 1:1 có thể tạo áp lực bán. Cộng thêm B lưu ý **Q2/2026 nghĩa vụ >36.600 tỷ tiền thuê/thuế đất** (tham khảo, cần đối chiếu) → áp lực dòng tiền. Đây là mã **nhiều tin tiêu cực cụ thể nhất**, không phải "chịu được rủi ro".
- **SL sát cụm MA20/MA50:** chính Agent A cảnh báo vùng này **"dễ bị quét (whipsaw)"** — C lại coi đó là ưu điểm. SL nằm ngay vùng dày lệnh = dễ bị đạp thủng rồi bật, cắt lỗ oan.

### 🏬 VRE — mua NGAY DƯỚI kháng cự, chưa hề có xác nhận

- **Agent C cho rằng** "chất lượng cơ bản + score cao nhất, an toàn nội tại nhất." **Nhưng** kỹ thuật nói khác: **trend_up = False (dưới MA50)**, và Agent A ghi rõ **"đang gặp kháng cự MA50 → CẦN đóng cửa trên MA50 mới xác nhận."** Luận điểm bò VRE **tự thừa nhận điều kiện chưa xảy ra** — tức là mua bây giờ = mua vào kháng cự, **trước** xác nhận, với **vol_ratio 0,71 (yếu nhất trong 3 kèo của C)**. Đây đúng nghĩa "canh test MA50" nhưng test từ **phía dưới**, xác suất bị đẩy ngược về MA20 là kịch bản A nêu thẳng.
- **"Score cao nhất bảng (0,5949) + p_LSTM 0,845":** với **AUC ~0,53–0,55**, khoảng cách score rank 1 (0,5949) và rank 5 (0,5393) **nằm trong nhiễu**. Tệ hơn, nội bộ ensemble **bất đồng**: p_GradBoost 0,4878 và p_XGBoost 0,5508 — hai cây quyết định gần/hụt 0,5, chỉ mình **LSTM (0,845) kéo score lên**. Một tín hiệu bị một mô hình chi phối, các mô hình khác không đồng thuận → độ tin cậy thấp, không phải "ensemble ưu tiên".
- **"KQKD Q1 kỷ lục + FTSE Small Cap = catalyst":** cả hai đều **[ĐÃ XẢY RA] và đã công khai** → **đã phản ánh vào giá**. Dòng vốn thụ động FTSE cho **nhóm Small Cap còn nhỏ hơn nhiều** so với Large Cap; tổng passive ~1,45–1,5 tỷ USD (B) chia cho 27 mã và ưu tiên vốn hóa lớn → phần rơi vào VRE là **không đáng kể** so với thanh khoản mã.
- **Cổ tức tiền mặt 10%:** GDKHQ **chưa kiểm chứng** → cùng rủi ro kẹp ngày chốt quyền trong khung 25 ngày (giả định: 10% cổ tức trên mệnh giá 10.000 ≈ 1.000đ/cp, ~4% giá tham chiếu — cần đối chiếu công bố sàn).

### 📈 VCI — beta thuần vào catalyst, nền cơ bản xấu nhất, dính rủi ro hệ thống

- **Agent C cho rằng** "đòn bẩy gián tiếp mạnh nhất vào FTSE, hưởng lợi kép." **Nhưng** C tự thừa nhận đây là **beta thuần vào catalyst, không dựa chất lượng lợi nhuận** — nghĩa là nếu FTSE là "sell the news" hoặc VN-Index quay đầu, VCI **không có sàn cơ bản đỡ**. Agent B nêu tin xấu **[ĐÃ XẢY RA] rõ ràng**: **tự doanh báo lỗ, thu nhập toàn diện âm 432 tỷ (danh mục AFS giảm giá), mới đạt ~29% kế hoạch nửa năm** → đây là mã **chất lượng lợi nhuận kém nhất** trong 3 kèo.
- **"Margin kỷ lục ~16.646 tỷ = hưởng lợi":** đây là con dao hai lưỡi và thực chất là **cờ đỏ rủi ro hệ thống**. AFS đã âm 432 tỷ chứng minh **P&L của VCI cực nhạy khi thị trường giảm**. Nếu VN-Index bị chặn ở vùng 1.800 (B: phiên 25/8 "phân hóa cao, gặp kháng cự mạnh") → **giải chấp margin → bán tháo → nhóm chứng khoán beta cao như VCI lãnh đủ trước tiên**. C dùng margin để bênh, nhưng margin cao là lý do để SỢ, không phải để mua.
- **Kỹ thuật yếu nhất trong 3:** trend_up False, dưới/sát MA50 (~22,6k), vol_ratio 0,84, A chấm 5,0 "cấu trúc trend hơi yếu hơn VRE." Ensemble score thấp nhất nhóm C (0,5393, rank 5), **p_GradBoost 0,403 và p_XGBoost 0,394 — cả hai cây quyết định BEARISH rõ**, chỉ LSTM (0,878) kéo lên. Đây là tín hiệu **mâu thuẫn nội bộ nặng nhất**.

---

## 📉 Rủi ro downside theo mã (kịch bản chạm/thủng SL −5%)

| Mã | Chốt chặn kỹ thuật (A) | Kịch bản gấu | SL −5% có an toàn? |
|---|---|---|---|
| **VIC** | Trên MA50 nhưng +60%/tháng, RSI 61,5 | Chốt lời sau nhịp nóng + pha loãng GDKHQ → mean-reversion. SL 212.610 sát MA20/MA50 = vùng **whipsaw** (A) | Dễ bị quét rồi bật → cắt lỗ oan; nếu GDKHQ/tin sốc gây sàn thì gap qua SL |
| **VRE** | **Dưới MA50**, kháng cự ngay đầu, vol 0,71 | Không đóng cửa nổi trên MA50 → đẩy ngược về MA20 (A). SL 24.225 | Trung bình — nhưng vào lệnh trước xác nhận = xác suất chạm SL cao |
| **VCI** | **Dưới MA50**, vol 0,84, tự doanh lỗ | Index rej-1.800 → giải chấp margin → chứng khoán beta cao rơi mạnh. SL 21.280 | Rủi ro nhất: có thể xuyên SL nếu deleveraging toàn thị trường |

**Rủi ro hệ thống áp lên CẢ 5 mã (C chưa cân đủ):**
- **Tập trung ngành cực đoan:** 4/5 ứng viên là **BĐS (VRE, VIC, KDH, PDR)** + 1 chứng khoán (VCI). Đây thực chất là **MỘT cược vĩ mô** (BĐS + chứng khoán, cùng nhạy lãi suất/thanh khoản). Không có phân tán — một cú sốc vĩ mô (lãi suất, tín dụng, ngoại bán ròng) đánh **đồng loạt**.
- **Biên độ ±7% + T+2:** SL −5% **không đảm bảo khớp**. Một phiên sàn (−7%) trắng bên mua → SL trượt sâu hơn −5% rất nhiều. Hàng mua về T+2 mới bán được → **kẹp hàng** khi có gap-down trong 1–2 phiên đầu. R:R 1,6 mà C dùng là **R:R lý thuyết**, thực tế downside có đuôi dày hơn.
- **Khối ngoại 2 chiều:** B ghi tuần 10–14/8 **bán ròng >2.100 tỷ**; dòng ngoại chưa ổn định. Dòng passive FTSE là **tái cơ cấu một lần**, không phải mua bền — dễ "mua tin đồn, bán sự thật" quanh mốc hiệu lực 21/9.
- **Timing xấu:** VN-Index ~1.768 áp sát **kháng cự mạnh 1.800** (B). Mua nhóm beta cao khi index ở kháng cự = nếu index bị đẩy lùi, mọi mã rơi theo.

---

## 🚫 Mã nên TRÁNH / rủi ro nhất

1. **KDH — tránh rõ nhất (bắt dao rơi kinh điển).** A chấm **3,5/10 (tệ nhất)**: downtrend dài ~28k→16,5k, **MA50 vẫn dốc xuống**, vol_ratio 0,53, TP 19.656 **bị MA50 chặn ngay** → dư địa lời "trần". B: lợi nhuận Q2 "ảo" từ **thoái vốn**, **bán nhà −85%**, **dòng tiền KD 6 tháng âm >1.480 tỷ**, **KHÔNG có catalyst FTSE**. Không có gì đỡ ngoài "sạch nợ trái phiếu".
2. **PDR — tránh.** vol_ratio **0,43 (yếu nhất bảng)**, còn xa dưới MA50, TP 13.716 nằm **trên** MA50 (phải phá kháng cự mới tới đích). B: chi **7.666 tỷ** thương vụ Lotte → áp lực dòng tiền; **bán BĐS chỉ ~2 tỷ**; ngoài rổ FTSE. Câu chuyện dài hạn nhưng thiếu catalyst ngắn hạn.
3. **VCI — rủi ro nhất trong 3 kèo của C** (lý do ở mục phản biện: cơ bản xấu nhất + dưới MA50 + beta margin + 2 cây quyết định bearish).
4. **VIC — bất đối xứng downside lớn nhất** dù setup KT đẹp: mua sau +60% + rủi ro pha loãng cụ thể = phần thưởng hẹp (TP đụng kháng cự thật), rủi ro đuôi rộng.

---

## ⚠️ Nhắc lại edge mô hình yếu (AUC ~0,53–0,55)

- AUC 0,53–0,55 chỉ **nhỉnh hơn tung đồng xu (0,50)**. Chênh lệch score giữa các ứng viên (0,5949 → 0,5393) **nằm trong biên nhiễu** → không nên coi rank là thứ tự ưu tiên đáng tin.
- Nội bộ ensemble **bất đồng ở đúng các kèo bò**: VRE (GradBoost 0,49; XGB 0,55), VCI (GradBoost 0,40; XGB 0,39) — score được **LSTM đơn lẻ kéo lên**. Tín hiệu bị một mô hình chi phối là tín hiệu **mong manh**.
- C thừa nhận "không dựa score, dựa catalyst" — nhưng catalyst chủ lực (FTSE) lại là thứ **dễ đã-vào-giá nhất** (VIC đã +60%, tin công bố 21/8). Khi cả score yếu **và** catalyst có thể đã phản ánh → luận điểm bò mất chân đỡ.
- **Kết luận gấu:** nếu buộc phải hành động, kỷ luật hơn là **chờ VRE/VCI đóng cửa vững TRÊN MA50 kèm volume thật** (điều kiện A nêu) thay vì mua trước xác nhận; VIC nên **chờ nhịp chỉnh về nền** thay vì đuổi giá; **tránh KDH/PDR**. Không mã nào đáng "all-in" khi edge ~coin-flip + tập trung ngành + rủi ro margin/±7%/T+2.

> ⚠️ **Đây KHÔNG PHẢI khuyến nghị đầu tư.** Bản ghi chỉ phản biện để hội đồng (Agent E) cân nhắc downside; mọi rủi ro nêu đều lấy từ note A/B, không bịa tin xấu. Các mốc MA, ngày GDKHQ nhiều chỗ "chưa kiểm chứng" — cần đối chiếu công bố HOSE/VSD trước mọi quyết định.


---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*

### 🎩 Agent E — Giám đốc Chiến lược · 2026-08-26 10:10

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| **VIC** | THEO DÕI | TB | Setup KT đẹp nhất + FTSE Large Cap, nhưng đuổi giá sau +60%/tháng & TP đụng kháng cự thật + rủi ro pha loãng → chờ chỉnh về nền. |
| **VRE** | THEO DÕI | TB | Cơ bản vững nhất, nhưng dưới MA50 & vol 0,71 yếu → chỉ mua khi đóng cửa vững trên MA50 kèm volume. |
| **VCI** | TRÁNH | TB | Beta thuần FTSE, cơ bản xấu nhất (tự doanh lỗ, âm 432 tỷ) + margin = rủi ro hệ thống nếu index rej 1.800. |
| **KDH** | TRÁNH | Cao | Bắt dao rơi: KT tệ nhất (downtrend, MA50 chặn TP), lợi nhuận Q2 "ảo", bán nhà −85%, dòng tiền âm, không catalyst. |
| **PDR** | TRÁNH | Cao | Vol yếu nhất (0,43), xa dưới MA50, TP trên MA50; chi 7.666 tỷ Lotte áp lực dòng tiền, ngoài rổ FTSE. |

**Stance danh mục: THẬN TRỌNG.** Edge mô hình ~coin-flip (AUC 0,53–0,55), rổ tập trung ngành cực đoan (4 BĐS + 1 CK = một cược vĩ mô), VN-Index áp sát kháng cự 1.800 → giữ tiền mặt cao, không giải ngân trước xác nhận; 0 MUA · 2 THEO DÕI · 3 TRÁNH. ⚠️ KHÔNG phải khuyến nghị đầu tư.

