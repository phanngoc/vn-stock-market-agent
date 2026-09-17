# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-09-17)

*Board tạo lúc 2026-09-17 05:07:10. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · buy&hold kỳ kiểm định **0.3963**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): PNJ, VRE, VIC, GVR, GAS
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **PNJ** | Retail/Consumer | 36,600 | 0.62 | 39,528 | 34,770 | 42 | ↓ dưới MA50 |
| 2 | **VRE** | RealEstate | 25,900 | 0.57 | 27,972 | 24,605 | 53 | ↑ trên MA50 |
| 3 | **VIC** | RealEstate | 242,400 | 0.57 | 261,792 | 230,280 | 61 | ↑ trên MA50 |
| 4 | **GVR** | Materials | 32,400 | 0.53 | 34,992 | 30,780 | 57 | ↑ trên MA50 |
| 5 | **GAS** | Energy | 88,600 | 0.49 | 95,688 | 84,170 | 63 | ↑ trên MA50 |

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

### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-09-17 05:10

| Mã | Trend | RSI(14) | Vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **PNJ** | ↓ dưới MA50 (giảm mạnh 03/26→08/26, từ ~77k còn ~35k, mới chớm đi ngang) | 42 (trung tính, không quá bán) | 0.19 (rất èo uột) | **3/10** | Cảnh báo **bắt dao rơi**: giá dưới cả MA20/MA50, MA50 vẫn đang dốc xuống. TP 39,528 trùng vùng MA50 đang giảm → kháng cự ngay trên đầu, khó đạt nếu xu hướng giảm chưa xác nhận đảo chiều. Volume cực thấp → không có dòng tiền xác nhận đáy. |
| **VRE** | ↑ trên MA50 nhưng đang test lại MA20/MA50 hội tụ (đi ngang sau nhịp giảm) | 53 (trung tính) | 0.41 (dưới 1, yếu) | **5/10** | TP 27,972 gần vùng đỉnh cũ tháng 6 (~28,000) — hợp lý về kháng cự. SL 24,605 nằm dưới vùng tích lũy tháng 8 (~24,000–25,000) — có biên an toàn. Volume yếu nên chưa có xác nhận bứt phá. |
| **VIC** | ↑ trên MA50, vừa pullback từ đỉnh gần nhất (~265k) về ~242k | 61 (nghiêng quá mua, chưa cực đoan) | 0.14 (thấp nhất nhóm — rất mỏng) | **5/10** | Uptrend rõ nhất về giá nhưng volume quá thấp khiến độ tin cậy giảm. TP 261,792 nằm sát đỉnh cũ vừa tạo (~265k) → phải phá kháng cự gần mới đạt được. SL 230,280 khá xa MA50 (~222k) — nếu điều chỉnh sâu có thể dính SL trước khi chạm vùng hỗ trợ MA50 thật sự. |
| **GVR** | ↑ trên MA50, vừa tạo đáy quanh 30k (07–08/26) rồi hồi phục, MA20 cắt lên MA50 | 57 (trung tính, nghiêng tích cực) | 0.44 (yếu nhưng cao nhất trong 5 mã) | **6/10** | Setup kỹ thuật đồng thuận nhất nhóm: nền giá rõ, MA20/50 bắt đầu ủng hộ xu hướng lên. TP 34,992 trùng vùng đỉnh swing tháng 9 (~34,000–34,200) — kháng cự gần, khả thi nhưng không nhiều dư địa. SL 30,780 sát đáy gần nhất (~30,300) — hợp lý. |
| **GAS** | ↑ trên MA50, vừa có nhịp tăng mạnh (65k→93k) rồi điều chỉnh về 88.6k | 63 (nghiêng quá mua) | 0.45 (dưới 1 nhưng cao nhất trong 5 mã) | **5/10** | TP 95,688 chỉ nhỉnh hơn đỉnh vừa lập (~93,500) — khả thi nếu tiếp diễn nhưng RSI đã cao, rủi ro đuổi giá. SL 84,170 nằm dưới MA20 (~85k) và trên MA50 (~78k) — có đệm nhưng nếu test lại MA20 dễ dính SL sớm. |

**Nhận định chung (thuần kỹ thuật, không xét tin tức/định giá):**
- Setup kỹ thuật ổn nhất nhóm: **GVR** — xu hướng tăng đang hình thành từ đáy rõ ràng, TP/SL bám sát vùng kháng cự/hỗ trợ hợp lý, dù volume vẫn dưới 1.
- Setup kỹ thuật rủi ro nhất nhóm: **PNJ** — mặc dù có score mô hình cao nhất (0.62), đây là mẫu hình "bắt dao rơi" kinh điển: dưới MA50 đang giảm, volume cực thấp (0.19), TP vướng ngay kháng cự MA50 động.
- **VIC** có xu hướng giá đẹp nhất về mặt hình dạng nhưng volume mỏng nhất nhóm (0.14) — cần thận trọng vì thiếu xác nhận dòng tiền, SL đặt khá xa vùng hỗ trợ cấu trúc thực (MA50).
- **VRE** và **GAS** ở mức trung bình: VRE đang tích lũy chờ tín hiệu bứt phá; GAS đã tăng nóng và RSI tiệm cận vùng quá mua nên rủi ro đuổi giá cao hơn.
- Rủi ro kỹ thuật lớn nhất toàn nhóm: **volume nhìn chung yếu ở cả 5 mã** (đều <1, tức thấp hơn trung bình 20 phiên) — điều này làm giảm độ tin cậy của mọi tín hiệu xu hướng, kể cả với các mã có điểm mô hình cao.
- Toàn bộ đánh giá dựa trên xác suất từ dữ liệu giá/khối lượng, mô hình có edge yếu (AUC ~0.53–0.55) — không phải khuyến nghị đầu tư.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**

### 🅱️ Agent B — Phân tích News / Cơ bản · 2026-09-17 05:20

## PNJ (Vàng bạc Đá quý Phú Nhuận) — Retail/Consumer
- **Tiêu cực/rủi ro:** Hai con gái của Chủ tịch HĐQT Cao Thị Ngọc Dung đăng ký bán tổng cộng 25 triệu cổ phiếu PNJ trong khoảng 10/9–9/10/2026 (ước thu >1.000 tỷ đồng), mục đích hỗ trợ vốn lưu động cho công ty. Đây là giai đoạn bán **đang diễn ra ngay lúc as-of (17/9)** → áp lực cung cổ phiếu từ nội bộ. [Investing.com/Vietstock](https://vn.investing.com/news/stock-market-news/pnj-giai-trinh-loi-nhuan-giam-38-sau-soat-xet-gia-dinh-chu-tich-dang-ky-ban-25-trieu-cp-ho-tro-von-cho-cong-ty-2706586)
- **Tiêu cực (đã xảy ra, cần kiểm chứng thêm về mốc thời gian):** Lợi nhuận sau kiểm toán/soát xét giảm mạnh so với báo cáo tự lập (giảm ~38–40% so cùng kỳ) do trích lập dự phòng hàng đổi trả và biên lợi nhuận mảng vàng 24K thấp hơn. [Investing.com/Vietstock](https://vn.investing.com/news/stock-market-news/pnj-giai-trinh-loi-nhuan-giam-38-sau-soat-xet-gia-dinh-chu-tich-dang-ky-ban-25-trieu-cp-ho-tro-von-cho-cong-ty-2706586); [24h.com.vn](https://www.24h.com.vn/kinh-doanh/loi-nhuan-6-thang-giam-gan-40-pnj-noi-gi-c161a1792285.html)
- **Trung tính/tích cực nhẹ (chưa kiểm chứng đầy đủ về kỳ báo cáo):** Một số nguồn cho biết KQKD quý gần nhất doanh thu thuần ~7.130 tỷ đồng (+3% YoY), lãi trước thuế 318 tỷ (+2%), biên lợi nhuận gộp cải thiện lên 17,5%. **Lưu ý:** thông tin này có thể không khớp thời điểm với tin lợi nhuận giảm 38% ở trên — chưa xác định rõ đây là quý nào, cần kiểm chứng chéo trước khi dùng. [DNSE](https://www.dnse.com.vn/senses/tin-tuc/bien-loi-nhuan-gop-cua-pnj-co-the-cham-24-nam-2026-35185238)
- **Tích cực:** Cuối tháng 8/2026, cổ phiếu PNJ tăng trần với lực mua >10 triệu cp sau khi Công an Thanh Hóa xác nhận hồ sơ nhập khẩu kim cương của PNJ đầy đủ, hợp pháp — gỡ bỏ nghi vấn pháp lý trước đó. [Vietstock](https://vietstock.vn/2026/08/du-mua-hang-trieu-co-phieu-pnj-sau-thong-tin-moi-tu-cong-an-thanh-hoa-830-1483514.htm); [VnEconomy](https://vneconomy.vn/pnj-bat-ngo-dao-chieu-ngoan-muc-co-phieu-kich-tran-sau-chuoi-ngay-boc-hoi-gan-mot-nua-gia-tri.htm)
- **Không nằm trong** danh sách 30 mã được kỳ vọng hút dòng tiền FTSE khi nâng hạng 21/9. [Vietstock](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)

## VRE (Vincom Retail) — RealEstate
- **Tích cực:** ĐHĐCĐ 2026 thông qua kế hoạch lãi ~5.375 tỷ đồng, doanh thu hợp nhất mục tiêu 10.132 tỷ đồng (+16% YoY); chốt chia cổ tức tiền mặt tỷ lệ 10% (1.000đ/cp, tổng ~2.272 tỷ đồng). [Baomoi/Báo Pháp luật VN](https://baomoi.com/dhdcd-vincom-retail-vre-2026-ke-hoach-lai-5-375-ty-dong-chot-chia-co-tuc-tien-mat-ty-le-10-c55006411.epi); [TNCK](https://www.tinnhanhchungkhoan.vn/vincom-retail-vre-dat-muc-tieu-doanh-thu-10132-ty-dong-nam-2026-post388253.html)
- **Tích cực:** Lũy kế 9 tháng, doanh thu 6.525 tỷ đồng (đạt 68,5% kế hoạch năm), lãi sau thuế 3.787 tỷ đồng (đạt 80,6% kế hoạch năm) — vượt tiến độ. [Nguoiquansat](https://nguoiquansat.vn/vincom-retail-vre-dat-muc-tieu-lai-hon-5-300-ty-dong-trong-nam-2026-281990.html)
- **Tích cực (catalyst vĩ mô):** VRE **có tên trong danh sách 30 mã được kỳ vọng hút dòng vốn FTSE** khi Việt Nam chính thức nâng hạng từ 21/9/2026. [Vietstock](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)
- **Chưa kiểm chứng:** ngày GDKHQ cụ thể cho đợt cổ tức tiền mặt 10% — không tìm được thông báo chốt ngày chính xác qua tìm kiếm, cần theo dõi công bố HOSE.

## VIC (Vingroup) — RealEstate
- **Tích cực mạnh:** Cổ phiếu VIC lập đỉnh lịch sử ~260.000đ/cp phiên 4/9/2026; riêng nửa đầu tháng 9 đóng góp ~102 điểm cho đà tăng VN-Index, vượt trội các mã khác. [DNSE](https://www.dnse.com.vn/senses/tin-tuc/vic-lap-ky-luc-moi-nhom-tai-chinh-gay-ap-luc-cho-thi-truong-35282269)
- **Tích cực:** Vốn hóa VIC tăng ~60% trong 1 tháng, đưa Vingroup vào top 5 công ty vốn hóa lớn nhất Đông Nam Á. Kế hoạch 2026: doanh thu mục tiêu 450.000 tỷ đồng (+36% YoY). [Báo Pháp luật VN](https://doanhnhan.baophapluat.vn/vingroup-vic-lan-dau-vuot-moc-von-hoa-2-trieu-ty-dong-co-phieu-tang-manh-30-sau-hai-tuan.html)
- **Tích cực (catalyst vĩ mô):** VIC nằm trong danh sách 30 mã hưởng lợi dòng tiền FTSE; theo MBS ước tính VIC là mã được **mua ròng nhiều nhất (~46,4 triệu USD)** trong đợt nâng hạng 21/9/2026. [Vietstock](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)
- **Rủi ro/trung tính cần lưu ý:** Vingroup tiếp tục thế chấp tài sản để vay nợ hỗ trợ VinFast (báo cáo đầu tháng 9/2026) — rủi ro đòn bẩy tài chính nhóm liên quan tăng dù không trực tiếp tại VIC. [RFA Tiếng Việt](https://www.rfa.org/vietnamese/trong-nuoc/2026/09/03/vinfast-vingroup-xe-hoi-vay-no/) — nguồn quốc tế, cần đối chiếu thêm với công bố chính thức.
- Sau chuỗi tăng rất mạnh (+60%/tháng, đỉnh lịch sử), cổ phiếu tiềm ẩn rủi ro chốt lời/điều chỉnh kỹ thuật — đây là quan sát trung tính, không phải khuyến nghị.

## GVR (Tập đoàn Công nghiệp Cao su VN) — Materials
- **Tích cực:** Lợi nhuận trước thuế 5 tháng đầu 2026 gần 3.900 tỷ đồng, tăng >30% YoY nhờ giá mủ cao su tăng. [DNSE](https://www.dnse.com.vn/senses/tin-tuc/dhdcd-gvr-loi-nhuan-5-thang-tang-hon-30-du-bao-co-the-thieu-hut-2-trieu-tan-cao-su-toi-2030-35237612)
- **Tích cực (dài hạn):** ĐHĐCĐ dự báo thị trường có thể thiếu hụt ~2 triệu tấn cao su đến năm 2030 — hỗ trợ giá bán. Công ty đẩy mạnh chuyển đổi đất cao su sang khu công nghiệp xanh (quỹ đất ~400.000ha). [DNSE](https://www.dnse.com.vn/senses/tin-tuc/dhdcd-gvr-loi-nhuan-5-thang-tang-hon-30-du-bao-co-the-thieu-hut-2-trieu-tan-cao-su-toi-2030-35237612); [Tuổi Trẻ](https://tuoitre.vn/tap-doan-cao-su-lai-gan-7-000-ti-dong-pho-thu-tuong-yeu-cau-nang-hieu-qua-quy-dat-400-000-ha-2026022717155029.htm)
- **Trung tính/thận trọng:** Kế hoạch lợi nhuận cả năm 2026 GVR tự đặt ra lại **giảm nhẹ** (~6.902 tỷ đồng, -2,9% YoY) dù giá cao su thuận lợi — ban lãnh đạo thận trọng. [Vietstock](https://vietstock.vn/2026/05/bat-chap-gia-cao-su-tang-ong-lon-gvr-van-than-trong-ve-ke-hoach-2026-737-1447348.htm)
- **Rủi ro pháp lý/cơ cấu:** Bộ Tài chính nắm ~96,8% vốn điều lệ GVR; quá trình chuyển đổi đất cao su sang khu công nghiệp có thể **chậm tiến độ pháp lý**; phương án tái cơ cấu vốn nhà nước còn chờ quyết định thay thế QĐ 22/2021. [Nguoiquansat](https://nguoiquansat.vn/doanh-nghiep-vn30-nam-quy-dat-400-000ha-nhan-chi-dao-tai-co-cau-tu-chinh-phu-co-phieu-tang-63-sau-hai-thang-276703.html)
- **Không nằm trong** danh sách 30 mã hưởng lợi trực tiếp từ FTSE (theo nguồn đã tra cứu).

## GAS (PV GAS / Tổng Công ty Khí Việt Nam) — Energy
- **Tích cực (catalyst sắp xảy ra):** PV GAS chốt **ngày GDKHQ nhận cổ tức là 22/9/2026**, tỷ lệ 25% (2.500đ/cp), ngày thanh toán dự kiến 20/11/2026; PVN (cổ đông lớn giữ 95,76%) dự kiến nhận ~5.776,7 tỷ đồng. [DNSE](https://www.dnse.com.vn/senses/tin-tuc/pv-gas-chot-ngay-tra-co-tuc-pvn-du-kien-nhan-gan-5800-ty-dong-35286573)
- **Trung tính (đã xảy ra 14/9/2026):** ĐHĐCĐ bất thường bầu lại nhân sự lãnh đạo nhiệm kỳ 2026–2031 — ông Bùi Minh Tiến làm Chủ tịch HĐQT, ông Dương Trí Hội làm Tổng Giám đốc. Thay đổi lãnh đạo mới, chưa rõ tác động dài hạn. [Thời báo Tài chính VN](https://thoibaotaichinhvietnam.vn/pv-gas-kien-toan-nhan-su-lanh-dao-cho-nhiem-ky-2026-2031-203822.html)
- **Tích cực:** 8 tháng đầu 2026, doanh thu hợp nhất >108.100 tỷ đồng, lãi trước thuế >14.500 tỷ đồng (129% kế hoạch năm), lãi sau thuế ~11.700 tỷ đồng (130% kế hoạch năm) — vượt xa kế hoạch năm dù mới qua 8 tháng. [PVGas.com.vn](https://www.pvgas.com.vn/bai-viet/pv-gas-6-thang-dau-nam-2026-hoan-thanh-ke-hoach-loi-nhuan-va-nop-ngan-sach-cho-ca-nam-duy-tri-nguon-cung-khi-dam-bao-an-ninh-nang-luong-quoc-gia)
- **Trung tính:** Dự báo giá LPG tháng 9/2026 theo Saudi Aramco giữ ổn định ~630 USD/tấn, không đổi so với tháng 8 — không có cú hích giá đầu vào/đầu ra rõ rệt.
- **Không nằm trong** danh sách 30 mã hưởng lợi trực tiếp từ FTSE (theo nguồn đã tra cứu).

## 📅 Sự kiện sắp tới (toàn thị trường + từng mã)
- **21/9/2026:** FTSE Russell chính thức áp dụng nâng hạng Việt Nam lên Thị trường Mới nổi Thứ cấp (Secondary Emerging), phân bổ theo 4 giai đoạn đến 9/2027. Ước tính ~140–150 triệu USD giải ngân giai đoạn đầu (~10% tổng dòng vốn dự kiến ~1,5 tỷ USD trong 1 năm). Danh mục 30 mã hưởng lợi chính gồm VIC, VRE (trong top 5 candidate của mô hình) nhưng **không gồm PNJ, GVR, GAS**. [VnEconomy](https://vneconomy.vn/ftse-russell-xac-nhan-viet-nam-vuot-qua-ky-review-chinh-thuc-nang-hang-vao-thang-92026.htm); [Vietstock](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)
- **22/9/2026:** GDKHQ cổ tức tiền mặt GAS (tỷ lệ 25%). [DNSE](https://www.dnse.com.vn/senses/tin-tuc/pv-gas-chot-ngay-tra-co-tuc-pvn-du-kien-nhan-gan-5800-ty-dong-35286573)
- **10/9 – 9/10/2026:** Giai đoạn bán 25 triệu cổ phiếu PNJ của gia đình Chủ tịch — đang diễn ra, cần theo dõi khối lượng khớp lệnh thực tế mỗi phiên.
- VRE: chưa xác định được ngày GDKHQ cổ tức 10% cụ thể — "chưa kiểm chứng", cần theo dõi công bố HOSE.

## 🌐 Bối cảnh chung (vĩ mô/ngành)
- VN-Index cuối tháng gần nhất tăng nhẹ (+0,21%) lên vùng ~1.342 điểm, nhưng **thanh khoản thấp** (~17.156 tỷ đồng/phiên) — thị trường giằng co, tâm lý thận trọng trước mốc nâng hạng. [Doanhnhan.baophapluat.vn](https://doanhnhan.baophapluat.vn/chung-khoan-309-giang-co-voi-thanh-khoan-thap-vn-index-ket-thuc-thang-9-kha-em-dem-43492.html)
- **Khối ngoại bán ròng**: từ đầu tháng 9 đến nay bán ròng gần 2.200 tỷ đồng trên HoSE, tập trung ở HPG — dòng vốn ngoại chưa thực sự vào trước ngày nâng hạng chính thức (21/9). [DNSE](https://www.dnse.com.vn/senses/tin-tuc/khoi-ngoai-mua-rong-nha-dau-tu-co-the-tich-luy-co-phieu-35286677)
- **Margin toàn thị trường** được dự báo tăng mạnh (khoảng +40% trong 2026), phản ánh kỳ vọng dòng tiền nội + đòn bẩy cao hơn quanh giai đoạn nâng hạng — cần lưu ý rủi ro biến động mạnh hơn bình thường khi thị trường có cú sốc.
- Ngành BĐS bán lẻ (VRE) và tập đoàn đa ngành (VIC) được xem là nhóm hưởng lợi trực tiếp/rõ ràng nhất từ dòng vốn FTSE trong đợt nâng hạng 21/9; ngành năng lượng (GAS), vật liệu/cao su (GVR), bán lẻ trang sức (PNJ) không nằm trong nhóm 30 mã được nêu tên nhưng vẫn có thể hưởng lợi gián tiếp qua tâm lý thị trường chung.

## 🏆 Xếp hạng theo hỗ trợ tin tức (mạnh → yếu)
1. **VIC** — đỉnh lịch sử, top hưởng lợi FTSE (~46,4 triệu USD mua ròng ước tính), tăng trưởng doanh thu kế hoạch mạnh; rủi ro là đã tăng rất nóng (+60%/tháng) nên cần cẩn trọng chốt lời kỹ thuật.
2. **VRE** — KQKD vượt tiến độ kế hoạch, cổ tức tiền mặt đã chốt, nằm trong nhóm hưởng lợi FTSE; tin tức đồng thuận tích cực, ít điểm trừ rõ ràng.
3. **GAS** — catalyst cổ tức GDKHQ 22/9 rõ ràng, KQKD 8 tháng vượt kế hoạch mạnh; nhưng không có lực đẩy FTSE và giá LPG đi ngang.
4. **GVR** — hưởng lợi giá cao su và câu chuyện đất KCN dài hạn, nhưng kế hoạch lợi nhuận 2026 tự đặt giảm nhẹ + rủi ro pháp lý/tái cơ cấu vốn nhà nước chưa rõ ràng.
5. **PNJ** — nhiều tin trái chiều: lợi nhuận sau kiểm toán từng giảm mạnh, insider (gia đình Chủ tịch) đang bán 25 triệu cổ phiếu ngay trong giai đoạn hiện tại — áp lực cung ngắn hạn rõ nhất trong nhóm 5 mã.

---
*Lưu ý: Đây KHÔNG PHẢI khuyến nghị đầu tư — chỉ là tổng hợp tin tức/bối cảnh phục vụ tranh luận nội bộ. Một số chi tiết (đặc biệt về kỳ báo cáo tài chính PNJ và ngày GDKHQ cổ tức VRE) chưa được kiểm chứng chéo đầy đủ, cần xác minh thêm trước khi sử dụng.*



---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

### 🐂 Agent C — Tổng hợp hướng BÒ · 2026-09-17 05:30

**Lưu ý mở đầu:** Toàn bộ luận điểm dưới đây dựa **hoàn toàn** vào bằng chứng Agent A (kỹ thuật) và Agent B (news) đã ghi trên whiteboard. Mô hình có edge yếu (AUC ~0.53–0.55) nên score không phải căn cứ chính — luận điểm bò phải đứng vững nhờ setup kỹ thuật + catalyst tin tức thực tế, không chỉ vì con số xác suất.

---

## 1) VRE (Vincom Retail) — kèo cân bằng nhất

**Luận điểm mua:** Theo Agent A, VRE đang ở trên MA50 và test lại vùng hội tụ MA20/MA50 sau nhịp giảm — RSI 53 trung tính, chưa quá mua, còn dư địa tăng. SL 24.605 nằm dưới vùng tích lũy tháng 8 (~24.000–25.000), tức Agent A xác nhận "có biên an toàn". Về nền tảng, Agent B nêu: ĐHĐCĐ 2026 thông qua kế hoạch lãi ~5.375 tỷ đồng, doanh thu mục tiêu 10.132 tỷ đồng (+16% YoY); lũy kế 9 tháng đã đạt 68,5% kế hoạch doanh thu và **80,6% kế hoạch lợi nhuận cả năm** — vượt tiến độ rõ rệt, không phải kỳ vọng suông.

**Catalyst:** Theo Agent B, VRE nằm trong danh sách 30 mã được kỳ vọng hút dòng vốn FTSE khi Việt Nam chính thức nâng hạng ngày 21/9/2026 — sự kiện này rơi đúng trong khung time-stop 25 ngày của tín hiệu. Ngoài ra công ty đã chốt chia cổ tức tiền mặt tỷ lệ 10% (dù ngày GDKHQ cụ thể "chưa kiểm chứng" theo Agent B).

**Kịch bản tới TP:** TP 27.972 (+8%) trùng vùng đỉnh cũ tháng 6 (~28.000) — theo Agent A đây là kháng cự hợp lý chứ không phải vùng trống giá. Nếu dòng vốn FTSE thực sự giải ngân quanh 21/9 như Agent B mô tả (ước ~140-150 triệu USD giai đoạn đầu, VRE thuộc nhóm hưởng lợi), thanh khoản hiện đang yếu (vol_ratio 0.41) có cơ hội cải thiện để hỗ trợ giá test lại vùng đỉnh cũ.

**Rủi ro & vì sao chịu được:** Agent A ghi nhận volume vẫn yếu (dưới 1), chưa có xác nhận bứt phá — đây là rủi ro thật, không né tránh. Nhưng SL đặt dưới vùng tích lũy đã được kiểm chứng (không phải SL tùy tiện), và time-stop 25 ngày đủ dài để chứng kiến sự kiện FTSE 21/9 diễn ra — nếu catalyst không kích hoạt dòng tiền, time-stop sẽ cắt lỗ có kỷ luật thay vì để lệnh "chết dí".

---

## 2) VIC (Vingroup) — kèo động lượng mạnh nhất nhưng cần thận trọng volume

**Luận điểm mua:** Theo Agent A, VIC có "xu hướng giá đẹp nhất về mặt hình dạng" trong nhóm 5 mã — trên MA50, vừa pullback lành mạnh từ đỉnh ~265k về 242k, RSI 61 (nghiêng quá mua nhưng chưa cực đoan). Theo Agent B, đây là mã có tin tức hỗ trợ mạnh nhất nhóm: lập đỉnh lịch sử ~260.000đ/cp phiên 4/9, vốn hóa tăng ~60% trong 1 tháng đưa Vingroup vào top 5 vốn hóa lớn nhất Đông Nam Á, kế hoạch doanh thu 2026 mục tiêu 450.000 tỷ đồng (+36% YoY).

**Catalyst:** Agent B dẫn ước tính của MBS: VIC là mã được **mua ròng nhiều nhất (~46,4 triệu USD)** trong đợt nâng hạng FTSE 21/9/2026 — lớn nhất trong toàn bộ danh sách 30 mã hưởng lợi. Đây là catalyst định lượng cụ thể nhất trong toàn bộ bằng chứng B thu thập được cho nhóm 5 mã.

**Kịch bản tới TP:** TP 261.792 chỉ cách đỉnh cũ ~265k một khoảng ngắn — nếu dòng vốn FTSE ~46,4 triệu USD như MBS ước tính thực sự giải ngân quanh 21/9 (nằm trong time-stop 25 ngày), lực cầu mới có thể đủ để phá lại vùng đỉnh vừa tạo, vốn dĩ không phải kháng cự xa lạ mà là mức giá VIC vừa đạt được cách đây vài phiên.

**Rủi ro & vì sao chịu được (phản biện trước cho Agent D):**
- Agent A cảnh báo volume mỏng nhất nhóm (0.14) — độ tin cậy xu hướng thấp. *Suy luận (chưa có trên whiteboard, ghi rõ là suy luận):* thanh khoản có thể cải thiện gần ngày nâng hạng khi dòng vốn ngoại thực sự vào, nhưng đây là kỳ vọng, không phải dữ kiện đã xảy ra.
- Agent A cũng lưu ý SL 230.280 khá xa MA50 thật (~222k) — nếu điều chỉnh sâu có thể dính SL trước khi chạm hỗ trợ cấu trúc. Đây là điểm yếu thật của setup, không phải rủi ro tưởng tượng.
- Agent B nêu rủi ro Vingroup tiếp tục thế chấp tài sản hỗ trợ VinFast — nhưng tự nhận đây là nguồn quốc tế, "cần đối chiếu thêm", nên không cường điệu.
- Sau chuỗi tăng +60%/tháng, rủi ro chốt lời là có thật (Agent B tự nêu) — nhưng pullback hiện tại (265k→242k) có thể đọc là nhịp xả bớt trước khi đón catalyst 21/9, chứ chưa phải đảo chiều xu hướng (Agent A vẫn xác nhận giá trên MA50).

---

## 3) GVR (Tập đoàn Cao su VN) — kèo kỹ thuật đồng thuận nhất

**Luận điểm mua:** Theo Agent A, đây là "setup kỹ thuật đồng thuận nhất nhóm": MA20 vừa cắt lên MA50, nền giá tạo đáy rõ ràng quanh 30k rồi hồi phục, RSI 57 nghiêng tích cực nhưng chưa quá mua. Vol_ratio 0,44 tuy vẫn dưới 1 nhưng **cao nhất trong 5 mã** — tương đối tốt nhất về xác nhận dòng tiền so với các ứng viên còn lại.

**Catalyst:** Theo Agent B, lợi nhuận trước thuế 5 tháng đầu 2026 gần 3.900 tỷ đồng, tăng hơn 30% YoY nhờ giá mủ cao su tăng — đây là kết quả đã công bố, không phải kỳ vọng. Dài hạn, ĐHĐCĐ dự báo thị trường có thể thiếu hụt ~2 triệu tấn cao su đến 2030, hỗ trợ giá bán; công ty còn câu chuyện chuyển đổi ~400.000ha đất cao su sang khu công nghiệp xanh.

**Kịch bản tới TP:** TP 34.992 trùng vùng đỉnh swing tháng 9 (~34.000–34.200) theo Agent A — kháng cự gần, không đòi hỏi giá phải phá vỡ vùng chưa từng thấy. SL 30.780 sát đáy gần nhất (~30.300), theo Agent A là mức "hợp lý".

**Rủi ro & vì sao chịu được:** Agent B tự nêu hai điểm trừ: (1) GVR đặt kế hoạch lợi nhuận cả năm 2026 giảm nhẹ (~-2,9% YoY) dù giá cao su thuận lợi — ban lãnh đạo thận trọng; (2) rủi ro pháp lý/tái cơ cấu vốn nhà nước (Bộ Tài chính nắm ~96,8% vốn) có thể khiến tiến độ chuyển đổi đất chậm. Đây là rủi ro trung- dài hạn về câu chuyện tăng trưởng, không trực tiếp phủ nhận setup kỹ thuật ngắn hạn (TP/SL trong 25 ngày dựa trên vùng giá gần, không phụ thuộc vào việc đất KCN có chuyển đổi thành công hay không). GVR cũng không nằm trong nhóm 30 mã hưởng lợi FTSE trực tiếp (Agent B) — nghĩa là đây là kèo dựa vào cơ bản ngành + kỹ thuật, không có catalyst vĩ mô ngày 21/9 như VIC/VRE.

---

## Kèo bò tự tin nhất

Trong 3 kèo trên, **VRE** là kèo có sự đồng thuận cao nhất giữa kỹ thuật (SL có biên an toàn theo Agent A) và tin tức (KQKD vượt tiến độ kế hoạch rõ ràng + cổ tức đã chốt + nằm trong nhóm hưởng lợi FTSE theo Agent B), trong khi VIC có catalyst định lượng lớn nhất nhưng volume mỏng nhất nhóm khiến rủi ro kỹ thuật cao hơn.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**


---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

### 🐻 Agent D — Tổng hợp hướng GẤU + phản biện · 2026-09-17 05:40

**Nhắc lại nền tảng:** Toàn bộ mô hình chấm điểm dựa trên các classifier có **AUC ~0.53–0.55** — nhỉnh hơn tung đồng xu (0.50) không nhiều. Score 0.62 của PNJ hay 0.57 của VRE **không phải xác suất thắng thực sự**, chỉ là thứ hạng tương đối trong một mô hình gần như không có edge. Agent C xây toàn bộ lập luận "kèo tự tin nhất" trên nền một mô hình mà chính C cũng thừa nhận là yếu — cần giữ mức độ tự tin ở mức thấp cho cả 3 kèo, không riêng gì kèo bị coi là yếu nhất.

---

## Phản biện Agent C — từng luận điểm

### 1) VRE — "kèo cân bằng nhất / tự tin nhất"

- **Agent C cho rằng** SL 24.605 "có biên an toàn" vì nằm dưới vùng tích lũy tháng 8. Nhưng chính Agent A gọi volume là "yếu" (0.41, dưới 1) và ghi rõ **"chưa có xác nhận bứt phá"**. Một SL nằm dưới vùng tích lũy chỉ có ý nghĩa nếu vùng tích lũy đó được xác nhận bằng dòng tiền — ở đây dòng tiền vẫn mỏng, nên "biên an toàn" thực chất là biên an toàn *về giá*, không phải biên an toàn *về xác suất giữ được vùng đó* nếu áp lực bán xuất hiện.
- **Agent C cho rằng** KQKD "vượt tiến độ" (68,5% doanh thu, 80,6% lợi nhuận kế hoạch năm sau 9 tháng) là bằng chứng nền tảng vững. Đây là tin cũ (kết quả đã công bố từ trước), thị trường đã có thời gian phản ánh vào giá — **không phải catalyst mới** để đẩy giá lên trong 25 ngày tới. Growth tốt trong quá khứ không tự động chuyển thành breakout kỹ thuật sắp tới.
- **Agent C dựa nhiều vào catalyst FTSE 21/9.** Nhưng đây là **sự kiện đã được biết trước và bàn tán rộng rãi** suốt nhiều tháng (không phải thông tin bất ngờ) — theo lý thuyết thị trường hiệu quả, phần lớn dòng vốn "thông minh" thường giải ngân trước ngày chính thức, không phải sau. Agent B còn ghi rõ: **"dòng vốn ngoại chưa thực sự vào trước ngày nâng hạng chính thức"** và **khối ngoại đang bán ròng gần 2.200 tỷ đồng từ đầu tháng 9** trên HoSE — tức dòng tiền ngoại hiện tại đang là lực bán, không phải lực mua, ngay trước sự kiện mà Agent C kỳ vọng sẽ là catalyst tăng giá. Nếu FTSE là "buy the rumor, sell the news", VRE hoàn toàn có thể giảm ngay sau 21/9 khi tin đã ra hết.
- **Agent C bỏ sót:** ngày GDKHQ cổ tức 10% của VRE **"chưa kiểm chứng"** theo chính Agent B — nghĩa là catalyst cổ tức này có thể không rơi vào khung 25 ngày time-stop, làm giảm giá trị của luận điểm "cổ tức đã chốt" mà C nêu.

### 2) VIC — "động lượng mạnh nhất"

- **Agent C tự thừa nhận** volume mỏng nhất nhóm (0.14) là "điểm yếu thật của setup" và SL xa MA50 thật — nhưng vẫn xếp đây là kèo có catalyst tốt. Đây chính là mẫu hình rủi ro cổ điển: **giá tăng không có xác nhận khối lượng**. Vol_ratio 0.14 nghĩa là thanh khoản chỉ bằng ~14% mức trung bình — với một cổ phiếu vừa tăng nóng +60%/tháng, thanh khoản cạn kiệt ở vùng cao thường là dấu hiệu **thiếu người mua mới, chỉ còn người cũ giữ hàng** — dễ đảo chiều mạnh khi có tin xấu hoặc chốt lời hàng loạt.
- **Agent C viện dẫn** con số "mua ròng ~46,4 triệu USD" (ước tính của MBS, chưa xảy ra) như bằng chứng chắc chắn. Đây là **con số dự báo/ước tính**, không phải dữ liệu đã xảy ra — rủi ro sai lệch giữa ước tính và thực tế giải ngân là có thật, đặc biệt khi khối ngoại đang bán ròng ngay lúc này theo Agent B.
- **Agent C giảm nhẹ rủi ro đòn bẩy VinFast** bằng cách gọi nguồn RFA là "quốc tế, cần đối chiếu thêm". Nhưng đây vẫn là rủi ro **có thật trên whiteboard**, không phải bịa — việc thế chấp tài sản tập đoàn để hỗ trợ VinFast, nếu đúng, là rủi ro cấu trúc vốn có thể ảnh hưởng tâm lý nhà đầu tư với cả nhóm Vingroup, bất kể xác suất xảy ra sự cố ngay trong 25 ngày.
- **Rủi ro downside cụ thể:** VIC đã tăng từ đáy lên đỉnh lịch sử ~265k rồi pullback về 242k. Agent A gọi đây là "pullback lành mạnh" nhưng RSI 61 vẫn nghiêng quá mua. Với volume cạn (0.14), một nhịp bán tháo chốt lời sau chuỗi tăng nóng hoàn toàn có thể xuyên thủng MA50 thật (~222k) **trước khi chạm SL 230.280** — tức SL đặt xa hơn hỗ trợ cấu trúc, y như Agent A đã cảnh báo, khiến lệnh có thể lỗ sâu hơn kỳ vọng nếu trượt giá (đặc biệt nếu biên độ ±7%/phiên bị chạm và không khớp được ở giá SL mong muốn).

### 3) GVR — "kỹ thuật đồng thuận nhất"

- **Agent C cho rằng** đây là kèo ít phụ thuộc catalyst vĩ mô nên "an toàn" hơn. Nhưng ngược lại, đây cũng là kèo **không có động lực bên ngoài nào thúc đẩy dòng tiền mới** trong 25 ngày tới — không FTSE, không tin tức mới nổi bật ngoài KQKD 5 tháng đã cũ. Vol_ratio 0,44 tuy cao nhất nhóm 5 mã nhưng **vẫn dưới 1**, tức vẫn là thanh khoản dưới trung bình — "tốt nhất trong nhóm yếu" không đồng nghĩa với "đủ tốt".
- **Agent C tự nêu nhưng giảm nhẹ** hai rủi ro cơ bản quan trọng: (1) chính ban lãnh đạo GVR đặt kế hoạch lợi nhuận **giảm** cho 2026 dù giá cao su thuận lợi — đây là tín hiệu thận trọng từ chính nội bộ doanh nghiệp, thường đáng tin hơn các dự báo bên ngoài; (2) rủi ro tái cơ cấu vốn nhà nước (Bộ Tài chính giữ 96,8%) — nhóm cổ phiếu nhà nước sở hữu chi phối thường có thanh khoản thấp và biến động chính sách bất ngờ (thoái vốn, sáp nhập) có thể tạo biến động giá không liên quan đến yếu tố kỹ thuật/kinh doanh.
- Câu chuyện "thiếu hụt cao su đến 2030" là **catalyst dài hạn (nhiều năm)**, hoàn toàn không tương thích với khung thời gian time-stop 25 ngày của tín hiệu — dùng câu chuyện dài hạn để biện minh cho một lệnh ngắn hạn là **đánh tráo khung thời gian**, một lỗi lập luận cần lưu ý.

---

## Rủi ro downside theo mã (kịch bản tới SL hoặc xa hơn)

- **PNJ:** Không nằm trong danh sách kèo bò của C nhưng cần nhắc: đây là ví dụ rõ nhất của "bắt dao rơi" — dưới MA50 đang giảm, volume 0.19 cực thấp, và theo Agent B, **gia đình Chủ tịch đang bán 25 triệu cổ phiếu ngay trong giai đoạn hiện tại (10/9–9/10)** — áp lực cung nội bộ trùng khớp thời gian với toàn bộ khung time-stop 25 ngày. Kết hợp với lợi nhuận sau kiểm toán giảm ~38-40%, đây là mã rủi ro downside rõ ràng nhất nhóm 5 mã.
- **VRE:** Nếu FTSE là "sell the news" và khối ngoại tiếp tục bán ròng như xu hướng đầu tháng 9, giá có thể giảm về lại vùng 24.000 hoặc thủng SL 24.605 mà không cần tin xấu riêng của VRE — chỉ cần tâm lý thị trường chung xấu đi khi thanh khoản toàn thị trường đang thấp (~17.156 tỷ/phiên, theo Agent B).
- **VIC:** Rủi ro lớn nhất là **gap-down** sau chuỗi tăng nóng — với biên độ ±7%/phiên của HOSE, nếu có phiên bán tháo mạnh (chốt lời sau đỉnh lịch sử, hoặc tin xấu về đòn bẩy VinFast lan rộng), giá có thể nhảy qua vùng SL 230.280 mà không khớp được lệnh ở đúng giá đó, đặc biệt khi volume hiện tại (0.14) cho thấy thanh khoản hai chiều đều mỏng.
- **GVR:** Rủi ro thấp hơn về biến động ngắn hạn nhưng dễ đi ngang/giảm nhẹ nếu không có dòng tiền mới — TP 34.992 nằm ngay tại kháng cự vùng đỉnh tháng 9, nếu không phá được sẽ tạo mô hình "double top" ngắn hạn, dễ kích hoạt bán ra.
- **GAS:** RSI 63 (quá mua), vừa tăng mạnh 65k→93k rồi điều chỉnh — SL 84.170 khá sát MA20, dễ bị quét nếu có nhịp test lại MA20 trước khi tiếp diễn (nếu có).

## Rủi ro hệ thống toàn thị trường (áp dụng mọi mã)

- Thanh khoản toàn thị trường thấp (~17.156 tỷ đồng/phiên) — thị trường giằng co, dễ bị chi phối bởi dòng tiền nhỏ/lớn bất thường quanh sự kiện nâng hạng.
- Khối ngoại đang **bán ròng** (~2.200 tỷ đồng từ đầu tháng 9), trái ngược với kỳ vọng "dòng vốn ngoại đổ vào trước nâng hạng" mà nhiều luận điểm bò dựa vào.
- Margin toàn thị trường được dự báo tăng mạnh (+40% năm 2026, theo Agent B) — đòn bẩy cao hơn đồng nghĩa biến động mạnh hơn khi có cú sốc, rủi ro call margin dây chuyền nếu thị trường điều chỉnh sau sự kiện 21/9 ("sell the news").
- Nhóm cổ phiếu được thảo luận tập trung nhiều vào BĐS/bán lẻ (VRE, VIC, PDR, NLG, KDH, VHM, DXG đều xuất hiện trong top signals) — rủi ro tập trung ngành nếu có cú sốc lãi suất/tín dụng bất động sản.
- Biên độ dao động ±7%/phiên của HOSE khiến SL lý thuyết có thể không khớp được ở đúng giá trong phiên biến động mạnh (gap risk), đặc biệt với các mã volume mỏng như VIC, PNJ.
- T+2: không thể cắt lỗ ngay trong phiên mua nếu giá giảm mạnh ngày đầu (đối với NĐT cá nhân theo cơ chế thông thường) — rủi ro kẹp hàng ngắn hạn.

## Mã nên tránh

- **Tránh nhất: PNJ** — hội tụ đủ mọi tín hiệu xấu: dưới MA50 đang giảm (bắt dao rơi), volume cực thấp (0.19), lợi nhuận kiểm toán giảm ~38-40%, và áp lực bán insider 25 triệu cổ phiếu đang diễn ra ngay trong khung thời gian nắm giữ.
- **Thận trọng: VIC** — dù có câu chuyện tin tức tốt nhất, volume mỏng nhất nhóm (0.14) + đã tăng nóng +60%/tháng + SL đặt xa vùng hỗ trợ cấu trúc thật là tổ hợp rủi ro kỹ thuật cao, bất kể catalyst FTSE có xảy ra hay không.
- **VRE và GVR** rủi ro thấp hơn tương đối trong nhóm nhưng đều có chung điểm yếu nền tảng: volume dưới 1 (chưa xác nhận dòng tiền) và toàn bộ mô hình chấm điểm nền là AUC ~0.53-0.55 — biên độ sai số của mọi con số score/TP/SL cần được hiểu là **tương đối, không chắc chắn**.

## Cảnh báo chung

Agent C xây dựng lập luận khá chặt chẽ và tự phản biện trước một số điểm (đáng ghi nhận), nhưng cách trình bày "kèo tự tin nhất" cho VRE/VIC dễ tạo cảm giác chắc chắn hơn thực tế. Với AUC ~0.53-0.55, khoảng 45-47% khả năng mô hình xếp hạng sai ngay cả trên dữ liệu huấn luyện — tự tin thái quá (overconfidence) vào bất kỳ kèo nào trong nhóm 5 mã này là rủi ro nhận thức lớn nhất, độc lập với chất lượng lập luận kỹ thuật/tin tức.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**


---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*

### 🎩 Agent E — Giám đốc Chiến lược · 2026-09-17 05:50

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| PNJ | TRÁNH | Cao | Dưới MA50 giảm + volume 0,19 cực thấp + insider bán 25 triệu cp đúng khung nắm giữ + lợi nhuận kiểm toán giảm ~38–40%. |
| VRE | THEO DÕI | TB | Bò/gấu cân sức: KQKD vượt tiến độ & SL hợp lý >< catalyst FTSE có rủi ro "sell the news" + volume chưa xác nhận. |
| VIC | TRÁNH | TB | Volume mỏng nhất nhóm (0,14) + SL lệch khỏi hỗ trợ MA50 thật + tăng nóng +60%/tháng → gấu thắng thế dù catalyst FTSE lớn nhất (nhưng mới là ước tính). |
| GVR | THEO DÕI | TB | Kỹ thuật đồng thuận nhất nhóm nhưng thiếu catalyst ngắn hạn trong 25 phiên; nội bộ tự hạ kế hoạch lợi nhuận. |
| GAS | THEO DÕI | Thấp | Catalyst cổ tức 22/9 thật nhưng RSI quá mua, SL sát MA20, không có luận điểm bò riêng. |

**Stance danh mục: Thận trọng.** Toàn bộ 5 mã đều volume dưới trung bình, mô hình nền AUC ~0,53–0,55 (edge yếu), khối ngoại đang bán ròng ngay trước sự kiện FTSE 21/9 — không mở vị thế MUA mới, chỉ THEO DÕI có điều kiện với cỡ vị thế nhỏ (2–3%/mã), ưu tiên bảo toàn vốn.

Chi tiết đầy đủ: xem `debate/DECISION.md`.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**

