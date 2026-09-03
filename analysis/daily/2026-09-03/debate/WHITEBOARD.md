# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-09-03)

*Board tạo lúc 2026-09-03 04:49:57. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.354** · buy&hold kỳ kiểm định **0.2954**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): VIC, PNJ, PDR, KDH, VRE
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **VIC** | RealEstate | 236,300 | 0.63 | 255,204 | 224,485 | 69 | ↑ trên MA50 |
| 2 | **PNJ** | Retail/Consumer | 40,150 | 0.62 | 43,362 | 38,142 | 51 | ↓ dưới MA50 |
| 3 | **PDR** | RealEstate | 12,200 | 0.61 | 13,176 | 11,590 | 45 | ↓ dưới MA50 |
| 4 | **KDH** | RealEstate | 17,800 | 0.60 | 19,224 | 16,910 | 44 | ↓ dưới MA50 |
| 5 | **VRE** | RealEstate | 26,250 | 0.54 | 28,350 | 24,938 | 60 | ↑ trên MA50 |

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

### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-09-03 04:50

| Mã | Trend (giá vs MA20/MA50) | RSI(14) | vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **VIC** | ↑ trên MA50; vừa bứt lên khỏi vùng đi ngang 210–225k, giá 236,300 | 68.9 (sát vùng quá mua, chưa >70) | 0.41 (yếu, <1) | **6/10** | Breakout động lượng tốt nhưng KHÔNG có xác nhận khối lượng — rủi ro breakout giả. TP 255,204 nằm ở vùng giá chưa từng giao dịch trong biểu đồ (không có kháng cự rõ nhưng cũng chưa được kiểm chứng); SL 224,485 gần vùng hỗ trợ MA20 cũ — hợp lý. |
| **PNJ** | ↓ dưới MA50 (MA50 vẫn dốc xuống); giá đang hồi từ đáy ~32k lên 40,150 | 50.7 (trung tính) | 0.84 (yếu, gần 1) | **4/10** | Đây là hồi phục ngược xu hướng giảm dài (80k→30k), chưa xác nhận đảo chiều bằng MA. Khối lượng khá hơn nhóm còn lại nhưng vẫn <1. |
| **PDR** | ↓ dưới MA50 (MA50 dốc xuống); giá hồi nhẹ từ đáy ~11,500 lên 12,200 | 45.3 (trung tính) | 0.30 (rất yếu) | **3/10** | Xu hướng giảm rõ, hồi phục không có khối lượng xác nhận — dạng "bắt đáy" rủi ro cao chứ chưa hẳn "bắt dao rơi" (đã tạo đáy vài phiên). |
| **KDH** | ↓ dưới MA50 rõ rệt nhất nhóm; MA50 dốc xuống liên tục từ 03/26 | 44.1 (trung tính) | 0.62 (yếu) | **2.5/10** | Setup kỹ thuật yếu nhất: downtrend dài, chưa có dấu hiệu tạo đáy vững, giá mới nhích nhẹ khỏi 17,800. Cảnh báo "bắt dao rơi". |
| **VRE** | ↑ vừa vượt lại MA50 sau giai đoạn tạo đáy 07/26 | 59.8 (trung tính, thiên tăng) | 0.37 (rất yếu) | **5/10** | Trend vừa chuyển tăng nhưng khối lượng rất mỏng — độ tin cậy thấp. TP 28,350 trùng vùng kháng cự cũ tháng 06/26 (~28–29k), có thể gặp cản. |

**Nhận định chung:**
- Setup kỹ thuật tốt nhất về xu hướng: **VIC** (đang trên MA50, vừa breakout) — nhưng khối lượng yếu (0.41) là điểm trừ lớn, cần thận trọng với breakout giả.
- Setup kỹ thuật tệ nhất: **KDH** — downtrend dài và dốc nhất nhóm, dưới MA50 sâu, chưa có tín hiệu đảo chiều đáng tin.
- Rủi ro kỹ thuật lớn nhất chung của cả nhóm: **khối lượng (vol_ratio) đều dưới 1** ở cả 5 mã — không mã nào có xác nhận dòng tiền mạnh, làm giảm độ tin cậy của mọi setup breakout/hồi phục.
- PNJ, PDR, KDH đều là các mã đang dưới MA50 (3/5 ứng viên) — cần phân biệt rõ giữa "hồi kỹ thuật trong downtrend" (PNJ, PDR) và "bắt dao rơi" (KDH, downtrend còn dốc mạnh nhất).
- VRE là ca thú vị nhất về mặt chuyển trend (mới vượt MA50) nhưng chưa đủ khối lượng để khẳng định.
- Toàn bộ đánh giá trên chỉ dựa trên số liệu RSI/trend/vol_ratio trong signals_latest.csv và biểu đồ nến — chưa xét tin tức/định giá cơ bản.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Setup kỹ thuật chỉ phản ánh xác suất, không phải chắc chắn — mô hình có edge yếu (AUC ~0.53–0.55).

### 🅱️ Agent B — Phân tích News / Cơ bản · 2026-09-03 05:15

*Không phải khuyến nghị đầu tư. Độc lập với phân tích kỹ thuật (Agent A). Mỗi khẳng định kèm nguồn; nếu không kiểm chứng được sẽ ghi rõ.*

---

#### VIC — Vingroup

- KQKD H1/2026 rất mạnh: doanh thu thuần ~221.900 tỷ đồng (+70% YoY), lãi sau thuế >20.900 tỷ đồng (gấp 4,6 lần cùng kỳ), hoàn thành hơn nửa kế hoạch lợi nhuận cả năm. Sắc thái: **tích cực**. [Vốn hóa tăng 525.000 tỷ sau 8T2026 - CafeF](https://cafef.vn/vingroup-tang-gan-525000-ty-dong-von-hoa-sau-8t2026-phan-tang-them-con-lon-hon-ca-gia-tri-vietcombank-188260903000252913.chn)
- Cổ phiếu VIC tăng gần 60% trong 1 tháng qua, đưa Vingroup vào top 5 vốn hóa lớn nhất Đông Nam Á — mức tăng đã rất lớn, cần lưu ý rủi ro chốt lời sau sóng tăng mạnh. Sắc thái: **tích cực nhưng đã phản ánh nhiều vào giá** (chưa kiểm chứng mức độ "quá mua" cụ thể). [CafeF, 2026-09-03](https://cafef.vn/vingroup-tang-gan-525000-ty-dong-von-hoa-sau-8t2026-phan-tang-them-con-lon-hon-ca-gia-tri-vietcombank-188260903000252913.chn)
- VIC nằm trong danh sách ~30 mã dự kiến hút ròng vốn FTSE khi Việt Nam chính thức nâng hạng (hiệu lực 21/9/2026), ước tính dòng mua ròng dự phóng ~46,4 triệu USD cho riêng VIC (theo phân tích của MBS, **chưa phải số chính thức từ FTSE**). Sắc thái: **tích cực** (catalyst sắp tới). [Vietstock, 2026-08](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)
- Không tìm thấy tin về ngày GDKHQ/cổ tức cụ thể của VIC trong tháng 9/2026 — **chưa kiểm chứng**.

#### PNJ — Vàng bạc Đá quý Phú Nhuận

- Q1/2026: doanh thu thuần 17.245 tỷ đồng (+79% YoY), LNST 1.467 tỷ đồng (+116,5% YoY); bán lẻ tăng 21,7%. Sắc thái: **tích cực**. [congluan.vn](https://congluan.vn/doanh-thu-quy-1-2026-pnj-dat-17-245-ty-dong-10338985.html)
- H1/2026: doanh thu thuần 25.728 tỷ đồng (+49,4% YoY) nhưng LNST hợp nhất chỉ tăng nhẹ 6,2% (~1.184 tỷ đồng) — biên lợi nhuận bị co hẹp. Đáng chú ý: **Q2/2026 lỗ kỷ lục gần 283 tỷ đồng** dù doanh thu quý vẫn tăng, do biến động giá vàng/tồn kho tăng mạnh. Sắc thái: **tiêu cực/hỗn hợp** — đây là rủi ro cần cân nhắc dù cổ phiếu có score kỹ thuật cao. [Doanh Nhân VN qua Baomoi](https://baomoi.com/kqkd-cua-pnj-quy-ii-lo-ky-luc-gan-283-ty-nhung-6-thang-van-lai-1-184-ty-dong-hang-ton-kho-tang-manh-c55731400.epi)
- PNJ được cho là hưởng lợi dài hạn từ việc siết/kiểm tra thị trường vàng, có thể cải thiện biên lợi nhuận gộp nhờ đảm bảo nguồn nguyên liệu — nhưng đây là nhận định từ 1 nguồn phân tích (elibook.vn, 2026-05), **chưa kiểm chứng độc lập**. Sắc thái: **trung tính/tích cực dài hạn**. [elibook.vn](https://elibook.vn/2026/05/22/pnj-huong-loi-tu-viec-siet-va-kiem-tra-thi-truong-vang-bien-loi-nhuan-gop-duoc-cai-thien-sau-khi-dam-bao-nguon-nguyen-lieu-dau-vao.html/)
- PNJ **không có mặt** trong danh sách 30 mã dự kiến hút vốn FTSE nói trên. [Vietstock](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)

#### PDR — Phát Đạt

- Kế hoạch 2026: doanh thu 8.830 tỷ đồng, LNST 868 tỷ đồng (+69% YoY); mục tiêu 2026-2030 doanh thu lũy kế ~44.848 tỷ đồng. Sắc thái: **tích cực** (kỳ vọng tăng trưởng, nhưng là mục tiêu công ty tự đặt, chưa phải kết quả thực tế). [phatdat.com.vn](https://www.phatdat.com.vn/news/phat-dat-pdr-tang-toc-bung-hang-loat-du-an-don-luc-vao-tp-hcm/)
- **Rủi ro pha loãng đáng kể**: PDR có kế hoạch chào bán tối đa ~199,56 triệu cổ phiếu cho cổ đông hiện hữu (tỷ lệ 5:1, giá chào bán 10.000 đồng/cp) để huy động ~2.000 tỷ đồng đầu tư dự án Đà Nẵng/ven sông Hàn. Dòng tiền hoạt động kinh doanh 2025 vẫn âm gần 3.000 tỷ đồng. Sắc thái: **tiêu cực** — rủi ro pha loãng ngắn/trung hạn. [Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/phat-dat-pdr-muon-huy-dong-gan-2000-ty-dong-tu-chao-ban-cho-co-dong-hien-huu-post387998.html); [congluan.vn](https://congluan.vn/chu-tich-phat-dat-pdr-giai-thich-chuyen-ban-co-phieu-doanh-nghiep-len-ke-hoach-huy-dong-gan-2-000-ty-dong-10338480.html)
- Toàn ngành BĐS niêm yết dự kiến phát hành thêm ~48,2 tỷ cổ phiếu mới trong 2026 (+26% YoY, ~17,1% tổng số cổ phiếu lưu hành cuối 2025) — rủi ro pha loãng mang tính hệ thống cho nhóm BĐS, không riêng PDR. Sắc thái: **tiêu cực cho ngành**. [An Ninh Thủ Đô](https://anninhthudo.vn/rui-ro-pha-loang-khi-gan-482-ty-co-phieu-moi-du-kien-tung-ra-thi-truong-trong-nam-2026-post656401.antd)
- PDR **không có mặt** trong danh sách 30 mã FTSE dự phóng.

#### KDH — Khang Điền

- ĐHĐCĐ 2026: công ty tuyên bố **sạch nợ trái phiếu**, "nói không" với phát hành vốn mới (trừ khi có nhu cầu cấp thiết), duy trì cổ tức tiền mặt 10%. Sắc thái: **tích cực** — giảm rủi ro pha loãng/tài chính so với PDR. [doanhnhan.baophapluat.vn](https://doanhnhan.baophapluat.vn/dhdcd-khang-dien-kdh-2026-sach-no-trai-phieu-noi-khong-voi-phat-hanh-von-moi-va-muc-tieu-lai-1-500-ty-dong.html)
- Kế hoạch lãi 2026 ban đầu ~1.500 tỷ đồng, sau đó có thông tin điều chỉnh mục tiêu lên hơn 2.000 tỷ đồng (gấp đôi năm trước) — **chưa kiểm chứng chéo giữa các nguồn**, có thể là nhầm lẫn số liệu giữa các bài. Sắc thái: **tích cực nhưng cần xác minh thêm**.
- Catalyst sắp tới: dự án Gladia by the Waters (hợp tác Keppel) — phần cao tầng dự kiến **mở bán Q3/2026** (tức có thể trong tháng 9) nếu đủ điều kiện pháp lý. Sắc thái: **tích cực, đang chờ xác nhận thời điểm chính xác**. [Tổng hợp qua tìm kiếm — chưa có ngày cụ thể, chưa kiểm chứng]
- KDH nằm trong danh sách 30 mã dự kiến hút vốn FTSE. Sắc thái: **tích cực**. [Vietstock](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)
- KDH được vinh danh Top 50 Công ty đại chúng uy tín và hiệu quả 2026 (VIX50), công bố 2026-08-06. Sắc thái: **trung tính/tích cực nhẹ** (PR, ít tác động giá). [khangdien.com.vn](https://www.khangdien.com.vn/tap-doan-khang-dien-kdh-lan-thu-6-dat-top-50-cong-ty-dai-chung-uy-tin-va-hieu-qua-2026)

#### VRE — Vincom Retail

- Kế hoạch 2026: doanh thu 10.132 tỷ đồng, LNST 5.375 tỷ đồng (+16%/+15% YoY trên nền so sánh tương đương). Q1/2026 đạt ~25% kế hoạch doanh thu, ~30% kế hoạch lợi nhuận; khách tới TTTM +13-15%, doanh số khách thuê +23-25% YoY. Sắc thái: **tích cực**. [Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/vincom-retail-vre-dat-muc-tieu-doanh-thu-10132-ty-dong-nam-2026-post388253.html); [24hmoney](https://24hmoney.vn/news/vincom-retail-vre-bao-lai-hon-1-600-ty-dong-trong-quy-i-2026-c1a2777434.html)
- **Sự kiện đã xảy ra**: VRE đã chi trả cổ tức tiền mặt 10% (1.000đ/cp, ~2.272 tỷ đồng), GDKHQ 1/7/2026, đã thanh toán ~22/7/2026 — lần đầu chia cổ tức tiền mặt sau 7 năm. Đây là tin **đã phản ánh vào giá**, không còn là catalyst tương lai. Sắc thái: **tích cực (lịch sử)**. [24hmoney](https://24hmoney.vn/news/vincom-retail-chi-2-300-ty-dong-tien-mat-co-dong-lan-dau-nhan-qua-lon-sau-7-nam-c1a2795987.html)
- Chiến lược mới: ra mắt thương hiệu "Vincom Collection" (mô hình phố mua sắm ngoài trời gắn với đô thị Vinhomes), VRE thu phí hoa hồng thay vì đầu tư vốn trực tiếp — mục tiêu >30% tăng trưởng quy mô thương hiệu so với 2025. Sắc thái: **tích cực dài hạn**. [nguoiquansat.vn](https://nguoiquansat.vn/vincom-retail-vre-dat-muc-tieu-lai-hon-5-300-ty-dong-trong-nam-2026-281990.html)
- VRE nằm trong danh sách 30 mã dự kiến hút vốn FTSE. Sắc thái: **tích cực**. [Vietstock](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)

---

#### 📅 Sự kiện sắp tới (toàn thị trường, ảnh hưởng nhóm ứng viên)

- **21/9/2026**: FTSE Russell chính thức triển khai phân bổ cổ phiếu Việt Nam vào rổ chỉ số Thị trường Mới nổi Thứ cấp (Secondary Emerging Market), tỷ trọng ban đầu 10%, ước dòng vốn vào có thể đạt ~6 tỷ USD trong lộ trình đến 9/2027. Trong nhóm ứng viên, **VIC, VRE, KDH** đều có tên trong danh sách 30 mã dự phóng hưởng lợi; **PDR, PNJ không có tên**. [VnEconomy](https://vneconomy.vn/ftse-russell-xac-nhan-viet-nam-vuot-qua-ky-review-chinh-thuc-nang-hang-vao-thang-92026.htm); [Vietstock](https://vietstock.vn/2026/08/30-co-phieu-duoc-ky-vong-hut-manh-dong-tien-ftse-khi-viet-nam-nang-hang-3358-1475689.htm)
- **Q3/2026**: KDH dự kiến mở bán phần cao tầng dự án Gladia by the Waters — thời điểm cụ thể trong tháng 9 **chưa kiểm chứng**.
- Chưa tìm thấy ngày GDKHQ/họp ĐHĐCĐ bất thường cụ thể nào sắp tới cho VIC, PNJ, PDR trong tháng 9/2026 — **chưa kiểm chứng, cần theo dõi công bố HSX**.

#### 🌐 Bối cảnh chung

- **Nâng hạng thị trường** là câu chuyện vĩ mô lớn nhất hiện tại, chính thức có hiệu lực 21/9/2026 — nhóm cổ phiếu vốn hóa lớn (VIC, VHM, VRE, các ngân hàng, chứng khoán) được kỳ vọng hưởng lợi trực tiếp từ dòng vốn ETF/quỹ thụ động. Đây là catalyst mang tính vĩ mô, không đảm bảo tác động đồng đều lên từng mã. [nhandan.vn](https://nhandan.vn/ftse-russell-xac-nhan-lo-trinh-nang-hang-thi-truong-chung-khoan-viet-nam-len-thi-truong-moi-noi-thu-cap-vao-thang-92026-post953977.html)
- **Room tín dụng 2026**: NHNN đặt mục tiêu tăng trưởng tín dụng toàn hệ thống ~15%, một số ngân hàng ưu tiên được cấp room >30%; margin chứng khoán chỉ chiếm ~1,5% tổng dư nợ hệ thống, được đánh giá chưa gây rủi ro hệ thống. Sắc thái: **trung tính, không phải rủi ro cấp bách cho nhóm ứng viên hiện tại** (không có ngân hàng nào trong top 5). [vneconomy.vn](https://vneconomy.vn/ngan-hang-nao-duoc-cap-room-tin-dung-cao-nhat-nam-2026.htm)
- **Rủi ro pha loãng ngành BĐS**: toàn thị trường dự kiến có thêm ~48,2 tỷ cổ phiếu mới trong 2026 (+26% YoY), chủ yếu từ nhóm BĐS phát hành huy động vốn — đây là rủi ro mang tính hệ thống cần lưu ý khi đánh giá PDR (và ở mức độ thấp hơn, VHM/DXG dù không nằm trong top 5 hôm nay). [An Ninh Thủ Đô](https://anninhthudo.vn/rui-ro-pha-loang-khi-gan-482-ty-co-phieu-moi-du-kien-tung-ra-thi-truong-trong-nam-2026-post656401.antd)

---

#### 🏆 Xếp hạng theo hỗ trợ tin tức (mạnh → yếu)

1. **VIC** — KQKD H1 xuất sắc + catalyst FTSE 21/9 + đà tăng giá mạnh (nhưng đã tăng nhiều, rủi ro chốt lời).
2. **VRE** — KQKD đúng kế hoạch, catalyst FTSE, chiến lược mới rõ ràng; cổ tức đã trả (không còn là catalyst tương lai).
3. **KDH** — Tài chính lành mạnh (sạch nợ trái phiếu), có catalyst FTSE + dự án mở bán Q3, nhưng số liệu lợi nhuận giữa các nguồn chưa nhất quán.
4. **PDR** — Kế hoạch tăng trưởng tham vọng nhưng đi kèm rủi ro pha loãng cụ thể (~2.000 tỷ chào bán) và dòng tiền kinh doanh âm; không có catalyst FTSE.
5. **PNJ** — KQKD lẫn lộn: Q1 tốt nhưng Q2 lỗ kỷ lục do biến động giá vàng/tồn kho; không có catalyst FTSE.

*Đây KHÔNG PHẢI khuyến nghị đầu tư — chỉ là tổng hợp tin tức/cơ bản để hội đồng tranh luận tham khảo cùng phân tích kỹ thuật (Agent A). Edge mô hình định lượng hiện còn yếu (AUC ~0.53–0.55), tin tức trên không nên dùng để lấn át quản trị rủi ro (TP/SL/time-stop đã định).*



---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

### 🐂 Agent C — Tổng hợp hướng BÒ · 2026-09-03 05:35

*Không phải khuyến nghị đầu tư. Luận điểm dưới đây chỉ dùng lại bằng chứng đã có của Agent A (kỹ thuật) và Agent B (news/cơ bản) trên whiteboard — không thêm dữ kiện mới. Model đầu vào có edge yếu (AUC ~0.53–0.55), nên luận điểm bò phải đứng được nhờ catalyst + kỹ thuật, không chỉ vì con số score.*

---

#### 1. VIC — Vingroup (điểm tổng hợp cao nhất: score 0.6267, KT 6/10, xếp #1 theo news của Agent B)

**Luận điểm mua:**
Theo Agent A, VIC là setup kỹ thuật tốt nhất nhóm: giá đang ở trên MA50, vừa bứt hẳn ra khỏi vùng đi ngang 210–225k lên 236.300đ, RSI 68,9 — sát vùng quá mua nhưng **chưa vượt 70**, tức chưa chính thức bị dán nhãn quá mua theo ngưỡng kỹ thuật kinh điển. Đây là điểm khác biệt duy nhất trong nhóm 5 mã có xu hướng breakout rõ ràng thay vì "hồi trong downtrend" hay "bắt dao rơi".

**Catalyst (theo Agent B):**
- KQKD H1/2026 rất mạnh: doanh thu +70% YoY, lãi sau thuế gấp 4,6 lần cùng kỳ, đã hoàn thành hơn nửa kế hoạch lợi nhuận năm — đây là nền cơ bản thực, không phải kỳ vọng suông.
- VIC nằm trong danh sách ~30 mã dự kiến hút vốn FTSE khi Việt Nam chính thức nâng hạng (hiệu lực 21/9/2026), ước tính dòng mua ròng dự phóng ~46,4 triệu USD riêng cho VIC (theo MBS, Agent B ghi rõ chưa phải số chính thức) — đây là catalyst **sắp diễn ra**, chưa hết hạn, đúng trong khung time-stop 25 ngày của tín hiệu.
- Đà tăng ~60%/1 tháng đưa Vingroup vào top 5 vốn hóa Đông Nam Á — cho thấy dòng tiền thị trường đang thực sự chú ý tới mã này, không phải setup bị bỏ quên.

**Kịch bản giá tới TP:** Entry tham chiếu 236.300đ → TP 255.204đ (+8%), SL 224.485đ (-5,3%, quanh vùng hỗ trợ MA20 cũ theo Agent A), time-stop 25 ngày. Cửa sổ 25 ngày đủ để đón catalyst FTSE 21/9/2026 nằm gọn trong thời gian nắm giữ dự kiến — nếu dòng vốn nâng hạng thực sự chảy vào trước/quanh ngày hiệu lực, đây là chất xúc tác có mốc thời gian cụ thể, không phải catalyst mơ hồ.

**Rủi ro & vì sao chấp nhận được:**
Agent A cảnh báo đúng: vol_ratio chỉ 0,41 — breakout **không có xác nhận khối lượng**, và Agent B cũng lưu ý mức tăng 60%/tháng "đã phản ánh nhiều vào giá", rủi ro chốt lời sau sóng tăng mạnh. Đây là lo ngại có thật, không né tránh. Tuy vậy, cơ chế R:R của tín hiệu (TP +8% / SL -5,3%, tỷ lệ ~1,5:1) và time-stop 25 ngày đã được thiết kế để giới hạn thiệt hại nếu breakout là giả — nếu giá không giữ được trên vùng breakout và chạm SL, lệnh tự động cắt sớm thay vì để lỗ lan rộng. Nói cách khác, phần "khối lượng yếu" là rủi ro xác suất, còn khung R:R là cơ chế giới hạn hậu quả nếu xác suất đó thành hiện thực — hai việc khác nhau.

**Phản biện trước (đón đầu Agent D):**
- "RSI sát vùng quá mua" → đúng nhưng chưa vượt 70, và SL đã đặt dưới vùng breakout để xử lý đúng kịch bản này.
- "Vol_ratio 0,41 quá yếu, không đáng tin" → đây là điểm yếu thật, nhưng nó là rủi ro chung của **cả 5 mã** trong bảng (theo Agent A, không mã nào có vol_ratio ≥1), không phải điểm yếu riêng khiến VIC kém hấp dẫn hơn tương đối so với nhóm còn lại — trong khi VIC là mã duy nhất có cả trend tăng THẬT SỰ lẫn catalyst vĩ mô có mốc ngày cụ thể.
- "Giá đã tăng 60%/tháng, dễ đảo chiều" → đúng là rủi ro, nhưng đây chính là lý do time-stop 25 ngày và SL tồn tại — luận điểm bò không phủ nhận rủi ro này mà dựa vào cơ chế cắt lỗ để giới hạn nó.

---

#### 2. VRE — Vincom Retail (score 0.5384, KT 5/10, xếp #2 theo news của Agent B)

**Luận điểm mua:**
Theo Agent A, VRE "vừa vượt lại MA50 sau giai đoạn tạo đáy 07/26" — đây là 1 trong 2 mã duy nhất trong nhóm 5 (cùng VIC) có trend_up = True và giá trên MA50, tức đang trong giai đoạn chuyển pha từ giảm sang tăng chứ không phải hồi kỹ thuật trong downtrend như PNJ/PDR/KDH. RSI 59,8 — trung tính thiên tăng, còn nhiều dư địa trước khi chạm vùng quá mua.

**Catalyst (theo Agent B):**
- Kế hoạch 2026 đang đi đúng tiến độ: Q1/2026 đạt ~25% kế hoạch doanh thu, ~30% kế hoạch lợi nhuận — tín hiệu thực thi tốt hơn tỷ lệ thời gian đã trôi qua trong năm.
- Khách tới TTTM +13–15%, doanh số khách thuê +23–25% YoY — cho thấy động lực kinh doanh lõi (bán lẻ mặt bằng) đang cải thiện thực chất, không chỉ là con số kế toán.
- Nằm trong danh sách 30 mã dự phóng hưởng lợi từ dòng vốn FTSE 21/9/2026 — cùng catalyst vĩ mô với VIC, cùng nằm trong khung time-stop 25 ngày.
- Chiến lược mới "Vincom Collection" (mô hình thu phí hoa hồng thay vì đầu tư vốn trực tiếp) là câu chuyện tăng trưởng dài hạn ít thâm dụng vốn hơn — giảm rủi ro tài chính so với mô hình cũ.
- Công ty vừa chi trả cổ tức tiền mặt 10% lần đầu sau 7 năm — dù Agent B lưu ý đây là tin đã phản ánh vào giá (không phải catalyst tương lai), nó vẫn là tín hiệu về sức khỏe dòng tiền và mức độ thân thiện với cổ đông của ban lãnh đạo.

**Kịch bản giá tới TP:** Entry tham chiếu 26.250đ → TP 28.350đ (+8%), SL 24.938đ (-5%), time-stop 25 ngày. Agent A lưu ý TP trùng vùng kháng cự cũ tháng 06/26 (~28–29k) — tức đây không phải mức giá "vô định", mà là target ngay dưới một vùng cản đã từng có diễn biến giá thật, giúp đánh giá tính khả thi dễ hơn so với target đi vào "vùng chưa từng giao dịch" như của VIC.

**Rủi ro & vì sao chấp nhận được:**
Vol_ratio 0,37 — yếu nhất trong 2 mã bò chính, "độ tin cậy thấp" theo đúng nhận định của Agent A. Đây là rủi ro thật, không giảm nhẹ. Nhưng R:R của tín hiệu vẫn đối xứng (+8%/-5%, ~1,5:1), và việc TP nằm ngay dưới kháng cự cũ (thay vì vùng giá chưa kiểm chứng) khiến kịch bản "đạt TP" có cơ sở tham chiếu lịch sử cụ thể hơn — nếu giá không đủ lực vượt kháng cự, khả năng cao sẽ đi ngang/điều chỉnh nhẹ về SL trong biên độ đã định, chứ không phải một cú sập bất ngờ ngoài kịch bản.

**Phản biện trước (đón đầu Agent D):**
- "Khối lượng còn mỏng hơn cả VIC" → đúng, đây là điểm yếu lớn nhất của luận điểm VRE, thừa nhận thẳng thắn.
- "Cổ tức đã trả rồi, không còn là catalyst" → đồng ý với Agent B, không dùng cổ tức làm catalyst tương lai; catalyst thực sự ở đây là FTSE 21/9 + đà thực thi kế hoạch kinh doanh đúng tiến độ.

---

### Kèo bò tự tin nhất

Trong nhóm 5 mã, **VIC** là kèo bò có cơ sở vững nhất vì là mã duy nhất hội tụ đủ 3 yếu tố cùng lúc theo đúng bằng chứng của Agent A và Agent B: trend kỹ thuật tăng thật (breakout khỏi vùng đi ngang, trên MA50), KQKD nền tảng mạnh thực chất (lãi gấp 4,6 lần cùng kỳ), và catalyst vĩ mô có mốc thời gian rõ ràng (FTSE 21/9/2026) nằm trong khung time-stop 25 ngày — dù vẫn tồn tại rủi ro thật về khối lượng yếu (0,41) và mức tăng giá đã lớn, hai rủi ro này được giới hạn bởi cơ chế SL/time-stop sẵn có của tín hiệu.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Model có edge yếu (AUC ~0.53–0.55); luận điểm trên chỉ tổng hợp lại bằng chứng có thật từ Agent A/B để phục vụ tranh luận, không phải cơ sở để đặt lệnh.


---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

### 🐻 Agent D — Tổng hợp hướng GẤU + phản biện · 2026-09-03 06:00

*Đọc toàn bộ A (kỹ thuật), B (news/cơ bản), C (bò). Chỉ dùng lại dữ kiện đã có trên whiteboard — không bịa số/tin mới. Nếu suy đoán, ghi rõ "giả định". Mục tiêu: stress-test luận điểm bò, không phải bi quan cho có.*

---

## Phản biện Agent C

### 1. VIC

**C nói:** "RSI 68,9 sát vùng quá mua nhưng chưa vượt 70, tức chưa chính thức bị dán nhãn quá mua."
**D phản biện:** Đây là ngụy biện ranh giới cứng ("arbitrary threshold"). Ngưỡng 70 là quy ước, không phải ranh giới vật lý — cổ phiếu không biết nó đang ở 68,9 hay 71. Thực tế là VIC đã tăng **~60% trong 1 tháng** (theo Agent B) và RSI đang ở mức cực kỳ căng. "Chưa vượt 70" không làm giảm rủi ro đảo chiều, nó chỉ là cách đọc số học có lợi cho luận điểm mua.

**C nói:** "Vol_ratio 0,41 là rủi ro chung của cả 5 mã, không phải điểm yếu riêng của VIC."
**D phản biện:** Đây là ngụy biện "ai cũng vậy nên không sao" (relative-to-peers ≠ an toàn tuyệt đối). VIC là mã DUY NHẤT trong nhóm vừa có mức tăng giá parabol (+60%/tháng) VỪA có khối lượng xác nhận yếu (0,41). Một breakout mạnh mà không có dòng tiền đi kèm, trên nền giá đã tăng rất nóng, là dấu hiệu kinh điển của **climax/phân phối** (nhà đầu tư lớn xả hàng dần vào lực mua nhỏ lẻ đuổi giá), không hẳn là tích lũy để bứt phá bền vững. Vol_ratio yếu ở PNJ/PDR/KDH (đang hồi nhẹ, giá thấp) có ý nghĩa khác hẳn vol_ratio yếu ở VIC (đang breakout sau sóng tăng lớn) — gộp chung "cả nhóm đều vậy" để pha loãng rủi ro là so sánh khập khiễng.

**C nói:** Catalyst FTSE 21/9/2026 với dòng vốn ước ~46,4 triệu USD là chất xúc tác có mốc thời gian cụ thể nằm trong khung time-stop 25 ngày.
**D phản biện:** Agent B đã ghi rõ đây là **ước tính từ MBS, chưa phải số chính thức từ FTSE**. Rủi ro "buy the rumor, sell the news" là có thật và cụ thể ở đây: giá VIC tăng 60%/tháng trước ngày 21/9 rất có thể ĐÃ phản ánh phần lớn kỳ vọng nâng hạng + KQKD tốt. Time-stop 25 ngày từ 03/09 kết thúc khoảng đầu/giữa tháng 10 — nghĩa là lệnh vẫn có thể đang mở đúng lúc "tin ra là hết chuyện để kể" (sự kiện chính thức 21/9 qua đi), một kịch bản chốt lời hàng loạt hoàn toàn khả dĩ, không phải giả định xa vời.

**C nói:** R:R (+8%/−5,3%, ~1,5:1) và time-stop là "cơ chế giới hạn hậu quả" nên rủi ro vol_ratio yếu/giá đã tăng nhiều "chấp nhận được".
**D phản biện:** Cơ chế SL chỉ bảo vệ được nếu lệnh khớp đúng giá đặt. Với một mã vừa tăng 60%/tháng, biến động (volatility) thực tế đang rất cao; kết hợp biên độ dao động ±7%/phiên trên HOSE (giả định — cần xác nhận VIC niêm yết HOSE, nhưng đây là cơ chế thị trường phổ biến), một phiên giảm sàn/gap mạnh có thể khiến giá xuyên qua SL 224.485đ mà không khớp đúng mức, gây trượt giá (slippage) lớn hơn -5,3% danh nghĩa. Thêm nữa, cơ chế T+2 khiến nhà đầu tư mua hôm nay không thể bán ngay nếu phiên kế tiếp đảo chiều mạnh — "cơ chế cắt lỗ" trên giấy không tương đương bảo vệ thực tế trong kịch bản gap-down.

### 2. VRE

**C nói:** RSI 59,8 "còn nhiều dư địa trước khi chạm vùng quá mua."
**D phản biện:** "Còn dư địa" chỉ nghĩa là chưa bị RSI chặn lại, không phải bằng chứng cho việc giá sẽ tăng. Đây là lập luận thiếu — thiếu tín hiệu tiêu cực không đồng nghĩa có tín hiệu tích cực.

**C nói:** Vol_ratio 0,37 là "điểm yếu lớn nhất, thừa nhận thẳng thắn" nhưng vẫn xếp VRE là kèo bò #2.
**D phản biện:** Cần nói thẳng hơn: 0,37 là vol_ratio **yếu nhất trong toàn bộ 5 ứng viên** (yếu hơn cả VIC 0,41), đúng vào lúc giá "vừa vượt lại MA50" theo Agent A. Một cú vượt MA50 không có dòng tiền xác nhận là tín hiệu dễ thất bại kinh điển (bull trap) — xác suất giá tụt lại xuống dưới MA50 trong vài phiên tới là kịch bản hiện thực, không phải giả thuyết bi quan.

**C nói:** TP 28.350đ nằm ngay dưới kháng cự cũ tháng 06/26 (~28–29k) nên "có cơ sở tham chiếu lịch sử cụ thể hơn" so với VIC.
**D phản biện:** Đây chính xác là điều ngược lại với cách C diễn giải. Kháng cự cũ nghĩa là tại vùng giá đó **đã từng có lực bán đủ mạnh để chặn đà tăng trước đây**. Nếu dòng tiền hiện tại (vol_ratio 0,37) còn yếu hơn giai đoạn hình thành kháng cự đó, xác suất giá bị chặn lại TRƯỚC khi chạm TP là cao, không phải thấp như C ngụ ý.

**C nói:** Cổ tức 10% đã trả không dùng làm catalyst tương lai (đồng ý với B); catalyst thật là FTSE + đà thực thi kế hoạch kinh doanh.
**D phản biện:** Đồng ý phần cổ tức đã hết hạn. Nhưng cần nhấn thêm: "đà thực thi kế hoạch kinh doanh đúng tiến độ" là số liệu Q1/2026 (theo B) — đây là **tin cũ đã công bố cách đây nhiều tháng**, không phải catalyst mới sắp xảy ra trong 25 ngày tới. Sau khi loại cổ tức (đã qua) và tin Q1 (đã cũ), chất xúc tác thực sự còn lại của VRE trong khung thời gian nắm giữ chỉ còn FTSE — cùng một catalyst vĩ mô, không đảm bảo, mà cả VIC lẫn KDH cũng có. VRE không có catalyst riêng biệt nào mới để giải thích tại sao nó phải tăng giá *trong 25 ngày tới*.

---

## Rủi ro downside theo mã

- **VIC:** Rủi ro lớn nhất là mã đã tăng quá nóng (+60%/tháng) không có xác nhận khối lượng (0,41) — kịch bản downside: chốt lời hàng loạt sau/quanh ngày FTSE 21/9 ("sell the news"), đặc biệt vì giá đang ở vùng chưa từng giao dịch trước đây (theo Agent A) — nghĩa là KHÔNG có vùng hỗ trợ kỹ thuật nào phía trên SL nếu đảo chiều, việc giảm có thể diễn ra nhanh và sâu hơn kỳ vọng. Biên độ dao động theo phiên + T+2 khiến SL danh nghĩa (-5,3%) có thể không bảo vệ đủ trong kịch bản gap.
- **VRE:** Rủi ro chính là bull-trap — vượt MA50 không dòng tiền (vol_ratio 0,37, yếu nhất nhóm), dễ tụt lại dưới MA50; TP nằm ngay dưới kháng cự cũ có lực bán lịch sử. Ngoài ra VRE gắn với hệ sinh thái Vingroup/Vinhomes — nếu có tin xấu ảnh hưởng nhóm này (kể cả tin không liên quan trực tiếp tới VRE), tâm lý bán chéo trong "họ Vin" là rủi ro có thật dù chưa kiểm chứng cụ thể cho phiên tới.
- **PDR:** Theo Agent B, có kế hoạch chào bán ~199,56 triệu cổ phiếu (tỷ lệ 5:1) để huy động ~2.000 tỷ đồng, trong khi dòng tiền hoạt động kinh doanh 2025 âm gần 3.000 tỷ — đây là rủi ro pha loãng **đã xác nhận bằng kế hoạch cụ thể**, không phải suy đoán. Kết hợp kỹ thuật yếu (KT 3/10 theo Agent A — downtrend, hồi không khối lượng), đây là ca "hồi trong downtrend" rủi ro cao, không phải đảo chiều thật.
- **KDH:** Agent A đánh giá đây là setup kỹ thuật **yếu nhất nhóm (2,5/10)** — downtrend dài và dốc nhất, dưới MA50 sâu, cảnh báo rõ ràng "bắt dao rơi". Tin tốt (sạch nợ trái phiếu, catalyst FTSE, dự án Gladia) không đủ bù cho việc chưa có bất kỳ dấu hiệu tạo đáy kỹ thuật nào — mua ở đây là đặt cược vào việc tin tốt sẽ đảo ngược một xu hướng giảm đang còn rất dốc, chưa có bằng chứng giá phản ứng.
- **PNJ:** Q2/2026 lỗ kỷ lục ~283 tỷ đồng do biến động giá vàng/tồn kho (theo Agent B) trong khi cổ phiếu vẫn đang hồi trong downtrend dài hạn (80k→30k, KT 4/10). Đây là ca rõ nhất "kỹ thuật và cơ bản đều không ủng hộ" — hồi giá không có xác nhận đảo chiều MA, lợi nhuận quý gần nhất tệ.

**Rủi ro hệ thống/tập trung chung cho cả nhóm 5 mã:**
- 4/5 ứng viên (VIC, VRE, KDH, PDR) đều là bất động sản hoặc gắn trực tiếp với hệ sinh thái Vingroup/Vinhomes — đây không phải một danh mục đa dạng hóa, mà là một cược tập trung vào một ngành/một tập đoàn. Bất kỳ tin xấu vĩ mô nào về ngành BĐS (room tín dụng, pháp lý dự án, lãi suất) hoặc riêng về Vingroup có thể kéo giảm đồng thời nhiều mã trong nhóm.
- Toàn ngành BĐS niêm yết dự kiến phát hành thêm ~48,2 tỷ cổ phiếu mới năm 2026 (+26% YoY, theo Agent B) — rủi ro pha loãng mang tính hệ thống, có thể ảnh hưởng tâm lý cả nhóm BĐS kể cả các mã không trực tiếp phát hành (VIC, VRE, KDH).
- Cả 5/5 mã có vol_ratio < 1 (theo Agent A) — không mã nào có xác nhận dòng tiền mạnh. Đây là rủi ro nền tảng cho toàn bộ danh sách, không riêng mã nào.
- Margin/khối ngoại bán ròng cho riêng nhóm 5 mã này: **chưa kiểm chứng** — Agent B chỉ có dữ liệu margin ở cấp hệ thống ngân hàng (~1,5% tổng dư nợ, "chưa gây rủi ro hệ thống"), không phải dữ liệu margin chứng khoán/khối ngoại riêng cho VIC/PNJ/PDR/KDH/VRE. Không nên diễn giải "margin không phải rủi ro hệ thống chung" thành "margin không phải rủi ro cho nhóm mã cụ thể này".
- Biên độ dao động ±7% (HOSE) và cơ chế thanh toán T+2: đây là đặc điểm cấu trúc thị trường VN nói chung (không phải tin riêng của mã nào) — làm tăng rủi ro trượt giá khi chạm SL trong phiên biến động mạnh, và khóa vị thế 2 ngày làm việc sau khi mua, không thể phản ứng ngay nếu giá đảo chiều gấp.

---

## Mã nên tránh

1. **PDR — rủi ro cao nhất để tránh:** kỹ thuật yếu nhất trong nhóm ứng viên còn "hồi trong downtrend" (không phải KDH vì KDH thậm chí còn yếu hơn về kỹ thuật, nhưng PDR có thêm rủi ro pha loãng **đã xác nhận bằng kế hoạch cụ thể** — chào bán 5:1 huy động ~2.000 tỷ trong khi dòng tiền kinh doanh âm gần 3.000 tỷ). Đây là tổ hợp hiếm: kỹ thuật xấu + tin xấu cụ thể (không phải suy đoán) cùng lúc.
2. **KDH — tránh vì lý do kỹ thuật thuần túy:** setup yếu nhất nhóm theo Agent A (2,5/10), downtrend dốc nhất, chưa có dấu hiệu tạo đáy — bất kể tin tốt (sạch nợ, FTSE, dự án mới), mua ở đây là bắt dao rơi theo đúng cảnh báo của Agent A.
3. **VIC — rủi ro ẩn dưới vỏ bọc "kèo bò tự tin nhất":** đây là mã đông người đồng thuận nhất (Agent C xếp #1, KQKD tốt nhất, catalyst rõ nhất) — chính sự đồng thuận cao này là rủi ro: giao dịch quá đông (crowded trade) sau khi đã tăng 60%/tháng dễ bị đảo chiều mạnh khi có tín hiệu chốt lời đầu tiên, và vol_ratio thấp cho thấy chưa có dòng tiền tổ chức thực sự xác nhận, có thể phần lớn là dòng tiền cá nhân đuổi giá.

---

## Cảnh báo edge mô hình

Model dùng để xếp hạng 5 mã này có **AUC ~0,53–0,55** — chỉ nhỉnh hơn một chút so với việc tung đồng xu. Theo whiteboard, base win-rate của mô hình tốt nhất (LogReg) là 0,354 so với buy&hold 0,2954 trong kỳ kiểm định — cải thiện tuyệt đối chỉ ~6 điểm phần trăm, một biên độ rất mong manh và dễ bị nhiễu bởi phương sai mẫu nhỏ. Toàn bộ điểm số 0,61–0,63 phân biệt VIC/PNJ/PDR/KDH với nhau là chênh lệch rất nhỏ trên nền một mô hình có edge yếu — không nên đọc thứ hạng số score như một tín hiệu chắc chắn. Luận điểm bò của Agent C xây trên catalyst + kỹ thuật là cách tiếp cận đúng hướng (không dựa thuần vào score), nhưng các catalyst đưa ra (FTSE ước tính chưa chính thức, KQKD đã công bố từ trước) phần lớn đã hoặc có thể đã phản ánh vào giá — sự tự tin trong luận điểm C nên được chiết khấu thêm vì nền tảng dự đoán định lượng phía dưới vẫn rất yếu.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Toàn bộ nội dung trên là phản biện/stress-test luận điểm bò để phục vụ tranh luận, dựa trên dữ kiện đã có trên whiteboard — không phải cơ sở để đặt lệnh.


---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*

### 🎩 Agent E — Giám đốc Chiến lược · 2026-09-03 06:20

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| **VIC** | THEO DÕI | TB | Trend + KQKD mạnh nhưng vol_ratio 0,41 sau đà tăng 60%/tháng = rủi ro climax/phân phối thật; bò-gấu ngang cơ. |
| **VRE** | THEO DÕI | Thấp | Vừa vượt MA50 nhưng vol_ratio 0,37 yếu nhất nhóm — dấu hiệu bull-trap; TP sát kháng cự cũ có lực bán lịch sử. |
| **PDR** | TRÁNH | Cao | Kỹ thuật yếu (3/10) + rủi ro pha loãng đã xác nhận (chào bán 5:1 ~2.000 tỷ) trong khi dòng tiền kinh doanh âm. |
| **KDH** | TRÁNH | Cao | Setup kỹ thuật yếu nhất nhóm (2,5/10), downtrend dốc, chưa có dấu hiệu tạo đáy — bắt dao rơi. |
| **PNJ** | TRÁNH | TB | Hồi trong downtrend dài chưa xác nhận đảo chiều + Q2/2026 lỗ kỷ lục do biến động giá vàng/tồn kho. |

**Stance danh mục: Thận trọng.** Cả 5 mã đều vol_ratio < 1, 4/5 mã tập trung ngành BĐS/hệ sinh thái Vingroup, mô hình có edge yếu (AUC ~0,53–0,55) — ưu tiên bảo toàn vốn: chỉ THEO DÕI có điều kiện (size nhỏ 2–3%) với VIC/VRE khi có xác nhận khối lượng, tránh hoàn toàn PDR/KDH/PNJ ở thời điểm này.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Chi tiết đầy đủ tại `debate/DECISION.md`.

