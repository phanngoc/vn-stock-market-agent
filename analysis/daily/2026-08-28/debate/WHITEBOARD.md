# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-08-28)

*Board tạo lúc 2026-09-01 05:27:03. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.353** · buy&hold kỳ kiểm định **0.3146**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): VIC, PDR, KDH, PNJ, VRE
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **VIC** | RealEstate | 236,000 | 0.64 | 254,880 | 224,200 | 69 | ↑ trên MA50 |
| 2 | **PDR** | RealEstate | 12,400 | 0.59 | 13,392 | 11,780 | 49 | ↓ dưới MA50 |
| 3 | **KDH** | RealEstate | 18,200 | 0.59 | 19,656 | 17,290 | 49 | ↓ dưới MA50 |
| 4 | **PNJ** | Retail/Consumer | 42,100 | 0.57 | 45,468 | 39,995 | 57 | ↓ dưới MA50 |
| 5 | **VRE** | RealEstate | 26,100 | 0.57 | 28,188 | 24,795 | 59 | ↑ trên MA50 |

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

### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-09-01 05:30

| Mã | Trend (giá vs MA20/MA50) | RSI(14) | Vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **VIC** | ↑ trên MA50, MA20>MA50 (uptrend rõ) | 68.7 (gần vùng quá mua, chưa vượt 70) | 1.43 (sôi động) | **6.5** | Vừa có nến bứt phá lên ~242k rồi rút về 236k — có thể là chốt lời ngắn hạn sau sóng tăng mạnh từ vùng 210-220k; SL 224,200 nằm ngay dưới vùng hỗ trợ MA20/MA50 cũ, hợp lý; TP 254,880 là vùng giá chưa từng test (breakout), rủi ro "hụt hơi" nếu RSI chạm quá mua. |
| **VRE** | ↑ vừa cắt lên trên MA50 (uptrend mới hình thành) | 58.7 (trung tính, còn dư địa) | 1.44 (sôi động) | **6.5** | Setup sạch nhất về động lượng: chưa quá mua, khối lượng xác nhận đà tăng tốt. TP 28,188 có thể chạm vùng cản cũ tháng 6 (~27,000-28,000) trước khi lên tiếp — khả năng chốt lời sớm ở vùng này. SL 24,795 nằm dưới cả MA20 và MA50 hiện tại, hợp lý làm đáy bảo vệ. |
| **PNJ** | ↓ dưới MA50 (~44,000, đang đi ngang/giảm nhẹ), giá vừa hồi mạnh từ đáy 30k | 57.0 (trung tính) | 0.65 (èo uột, <1) | **4.0** | Hồi giá mạnh (30k→45k) nhưng KHÔNG có khối lượng xác nhận — tín hiệu yếu, nghi ngờ hồi kỹ thuật ngắn hạn trong downtrend lớn hơn là đảo chiều thật. TP 45,468 nằm sát ngay MA50 (~44,000) — dễ bị chặn lại tại đây trước khi đạt +8%. |
| **KDH** | ↓ dưới MA50 (MA50 đang giảm dốc từ 26k xuống ~19k) | 48.8 (trung tính) | 0.84 (dưới trung bình) | **3.5** | Downtrend rõ và kéo dài từ tháng 2; nhịp hồi cuối biểu đồ chỉ vừa chạm MA20, còn cách MA50 khá xa — dạng "bắt dao rơi" trong xu hướng giảm chưa xác nhận đảo chiều. Khối lượng dưới trung bình càng làm giảm độ tin cậy của nhịp hồi. |
| **PDR** | ↓ dưới MA50 (MA50 đang giảm dốc từ ~16.2k xuống ~13k) | 49.1 (trung tính) | 0.61 (èo uột nhất trong nhóm) | **3.5** | Tương tự KDH: downtrend dài từ tháng 3, nhịp hồi cuối chuỗi rất nhỏ và khối lượng thấp nhất trong 5 mã — cảnh báo "bắt dao rơi", chưa có xác nhận kỹ thuật đủ mạnh để coi là điểm vào tốt. |

**Nhận định chung:**
- Setup kỹ thuật đẹp nhất về mặt xu hướng + khối lượng: **VIC và VRE** — cả hai đều đã ở trên MA50 với vol_ratio >1.4 (dòng tiền chủ động tham gia), khác biệt với 3 mã còn lại vẫn nằm dưới MA50.
- Setup kỹ thuật yếu/rủi ro nhất: **PDR và KDH** — cùng mô-típ "hồi kỹ thuật trong downtrend dài" với khối lượng dưới trung bình (<0.85), chưa đủ cơ sở gọi là đảo chiều xu hướng.
- Rủi ro kỹ thuật lớn nhất trong nhóm top: VIC có RSI 68.7 sát ngưỡng quá mua sau một nến rút chân mạnh — dễ điều chỉnh ngắn hạn trước khi (nếu) tiếp tục lên.
- PNJ là trường hợp trung gian: giá hồi tốt nhưng khối lượng không xác nhận, và TP nằm sát vùng cản MA50 — chưa kiểm chứng được liệu đây là đảo chiều hay chỉ là hồi kỹ thuật.
- Toàn bộ đánh giá trên chỉ dựa vào số liệu RSI/trend/vol_ratio và biểu đồ nến trong signals_latest.csv + charts/, không xét tin tức hay định giá cơ bản. Cần nhấn mạnh: mô hình có edge yếu (AUC ~0.53-0.55), nên các điểm số kỹ thuật trên chỉ mang tính xác suất tương đối giữa các mã, không phải tín hiệu chắc chắn.

*Đây KHÔNG PHẢI khuyến nghị đầu tư.*

### 🅱️ Agent B — Phân tích News / Cơ bản · 2026-08-28 (as-of), viết lúc 2026-09-01

*Phạm vi: 5 mã ứng viên top-score từ pipeline (VIC, PDR, KDH, PNJ, VRE) + bối cảnh vĩ mô/ngành. Độc lập với phân tích kỹ thuật (Agent A). Không phải khuyến nghị đầu tư.*

---

#### VIC — Vingroup
- **KQKD nửa đầu 2026 (đã xảy ra, tích cực):** Doanh thu hợp nhất ~222.000 tỷ đồng, lợi nhuận sau thuế ~20.375 tỷ đồng nửa đầu năm; tổng tài sản vượt 1,3 triệu tỷ đồng, nợ phải trả >1,12 triệu tỷ đồng (đòn bẩy vẫn rất cao — cần lưu ý). Vinhomes (công ty con) ghi nhận doanh thu quy đổi 6 tháng đạt 134.200 tỷ đồng, gấp 3 lần cùng kỳ. Sắc thái: **tích cực** nhưng nợ vay lớn là rủi ro nền. [VnExpress](https://vnexpress.net/vingroup-len-ke-hoach-doanh-thu-ky-luc-450-000-ty-dong-5057422.html), [Thời báo Tài chính VN](https://thoibaotaichinhvietnam.vn/vingroup-dat-muc-tieu-but-pha-nam-2026-voi-loi-nhuan-sau-thue-35000-ty-dong-196175.html)
- **Sự kiện thương hiệu (đã xảy ra, trung tính/tích cực nhẹ):** 30/7/2026, Vingroup công bố "VinFast" là tên sân vận động 135.000 chỗ tại Khu đô thị Thể thao Quốc tế Hà Nội — mang tính PR/thương hiệu, không tác động trực tiếp KQKD. [Baomoi/Vingroup](https://baomoi.com/vingroup-tag10938.epi)
- **Catalyst FTSE (sắp xảy ra, tích cực, đã xác nhận):** VIC là 1 trong 3 mã Large Cap Việt Nam (cùng VCB, VHM) vào rổ FTSE Global Equity Index Series kỳ nâng hạng 9/2026, **và** thuộc nhóm 6 mã được thêm vào FTSE All-World. Hiệu lực **21/9/2026**. [Dân trí](https://dantri.com.vn/kinh-doanh/27-co-phieu-viet-nam-vao-ro-chi-so-moi-noi-cua-ftse-nang-hang-co-hieu-luc-tu-219-20260821192938821.htm), [Người Quan Sát](https://nguoiquansat.vn/ftse-russell-he-lo-lo-trinh-nang-hang-cua-viet-nam-ty-trong-co-phieu-se-tang-gap-10-lan-312710.html)
- **Rủi ro:** Đòn bẩy tài chính rất cao (nợ/tài sản ~86%); giá cổ phiếu đã tăng mạnh trước khi vào rổ FTSE (rủi ro "sell the news" quanh 21/9). Chưa kiểm chứng thêm tin pháp lý/trái phiếu cụ thể trong tuần cuối tháng 8.

#### PDR — Phát Đạt
- **Mua lại cổ phần Lotte Eco Smart City (đã xảy ra, tích cực):** 10/8/2026, PDR hoàn tất thanh toán 7.666 tỷ đồng để chính thức sở hữu 35% Lotte Properties HCMC (đơn vị triển khai dự án Lotte Eco Smart City Thủ Thiêm) — mở rộng quỹ đất dự án lớn. [Nguồn cần Vietstock/CafeF xác nhận thêm — tìm thấy qua tổng hợp search, **chưa kiểm chứng độc lập 100%**].
- **Chủ tịch đăng ký mua cổ phiếu (đã xảy ra, tích cực):** Chủ tịch Nguyễn Văn Đạt đăng ký mua 20 triệu cp PDR trong giai đoạn 31/7–29/8/2026 (tái cấu trúc sở hữu, mua khi giá thấp 3 năm). [Vietstock](https://vietstock.vn/2026/07/pdr-chu-tich-nguyen-van-dat-muon-mua-20-trieu-cp-khi-gia-thap-nhat-3-nam-739-1472096.htm), [CafeF](https://cafef.vn/tung-ban-co-phieu-de-hy-sinh-loi-ich-ca-nhan-chu-tich-phat-dat-nay-muon-mua-lai-20-trieu-co-phieu-pdr-188260728143638883.chn)
- **Pha loãng (rủi ro, đã xảy ra/đang triển khai):** ĐHĐCĐ 2026 thông qua kế hoạch phát hành ~200 triệu cp cho cổ đông hiện hữu (tỷ lệ 5:1, giá 10.000đ/cp thấp hơn thị giá) để huy động ~1.996 tỷ đồng, rót vào dự án Đà Nẵng Centre Point. Đã phát hành 2 lô trái phiếu ngày 26/3/2026 huy động 5.600 tỷ đồng. Sắc thái: **tiêu cực** về pha loãng/áp lực nợ, dù dùng cho dự án cụ thể. [Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/phat-dat-pdr-muon-huy-dong-gan-2000-ty-dong-tu-chao-ban-cho-co-dong-hien-huu-post387998.html)
- **Không thuộc danh sách 27 mã FTSE** nâng hạng (không thấy PDR trong danh sách công bố 21/8). Trung tính/không có catalyst FTSE trực tiếp.

#### KDH — Khang Điền
- **Mở bán dự án Gladia (đã xảy ra, tích cực mạnh):** Lễ mở bán 1/8/2026, hơn 90% sản phẩm giới thiệu đã có khách đặt cọc, tổng giá trị giao dịch gần 4.000 tỷ đồng. Phần cao tầng dự án Gladia (616 căn) dự kiến mở bán tiếp Q3/2026, khởi công Q1/2026, bàn giao Q4/2027. [Fili](https://fili.vn/2026/04/khang-dien-len-ke-hoach-lai-1500-ty-mo-ban-hon-600-can-ho-gladia-trong-quy-3-737-1422577.htm), [Vietstock](https://vietstock.vn/2026/01/tien-do-ban-hang-va-trien-khai-du-an-cua-kdh-737-1392501.htm)
- **Kế hoạch 2026 (đã công bố, trung tính/hơi tiêu cực):** Mục tiêu doanh thu 4.200 tỷ, LNST 1.500 tỷ — **giảm 10%/8%** so với 2025. Cổ tức 2025 chi trả tỷ lệ 10%. [Báo Đầu tư](https://baodautu.vn/nha-khang-dien-len-ke-hoach-lai-1500-ty-dong-trong-nam-2026-d558641.html)
- **Sạch nợ trái phiếu (đã xảy ra, tích cực):** ĐHĐCĐ 2026 công bố Khang Điền đã sạch nợ trái phiếu, không có kế hoạch phát hành vốn mới — giảm rủi ro tài chính. [Doanhnhan.baophapluat](https://doanhnhan.baophapluat.vn/dhdcd-khang-dien-kdh-2026-sach-no-trai-phieu-noi-khong-voi-phat-hanh-von-moi-va-muc-tieu-lai-1-500-ty-dong.html)
- **KDH không thuộc danh sách 27 mã FTSE** nâng hạng công bố 21/8.

#### PNJ — Vàng bạc đá quý Phú Nhuận
- **Lỗ kỷ lục quý II/2026 (đã xảy ra, tiêu cực mạnh — quan trọng):** Doanh thu thuần Q2 tăng 12% YoY đạt ~8.484 tỷ đồng nhưng **lỗ sau thuế gần 283 tỷ đồng** (cùng kỳ lãi 437 tỷ). Nguyên nhân: trích lập dự phòng ước tính ~865 tỷ đồng liên quan hoạt động mua lại kim cương, phát sinh sau làn sóng khách trả hàng vì bê bối buôn lậu liên quan cựu giám đốc P-Lab (bùng từ 3/7/2026). Lỗ thuần từ HĐKD 345,8 tỷ (cùng kỳ 2025 lãi 548 tỷ). Lũy kế 6 tháng vẫn lãi 1.184 tỷ (+6% YoY) nhờ Q1 tốt. [VnEconomy](https://vneconomy.vn/pnj-bao-lo-quy-2-do-trich-lap-du-phong-uoc-tinh-865-ty-dong.htm), [CafeF](https://cafef.vn/dieu-gi-khien-pnj-bao-lo-283-ty-trong-quy-2-2026-188260730202944666.chn), [Vietnambiz](https://vietnambiz.vn/pnj-lo-gan-283-ty-dong-quy-ii-trich-lap-hon-865-ty-sau-ap-luc-mua-lai-kim-cuong-202673020522995.htm)
- **Rủi ro uy tín thương hiệu (đang diễn ra, tiêu cực):** Bê bối buôn lậu liên quan cựu giám đốc P-Lab (đơn vị kiểm định) có thể tiếp tục ảnh hưởng niềm tin khách hàng trong các quý tới — **chưa kiểm chứng** liệu vấn đề đã xử lý dứt điểm hay còn kéo dài.
- **Giá vàng (bối cảnh, trung tính):** Giá vàng thế giới giảm cuối tháng 8 (SJC ~150,3 triệu/lượng, vàng thế giới quanh 4.567–4.608 USD/oz ngày 27-28/8/2026) sau khi đạt đỉnh giữa tháng — ảnh hưởng biên lợi nhuận vàng miếng/vàng 24K của PNJ nhưng doanh thu vàng 24K Q1 vẫn tăng 324,7% YoY. [Nongnghiepmoitruong](https://nongnghiepmoitruong.vn/bang-gia-vang-9999-24k-18k-sjc-doji-pnj-hom-nay-28-8-2026-d828493.html)
- **PNJ không thuộc danh sách 27 mã FTSE** nâng hạng.

#### VRE — Vincom Retail
- **Cổ tức tiền mặt (đã công bố, tích cực):** Lần đầu chia cổ tức sau 7 năm — 10% tiền mặt (1.000đ/cp), tổng ~2.272 tỷ đồng, dự kiến trả **Q3/2026** (cần theo dõi ngày GDKHQ cụ thể — **chưa kiểm chứng ngày chính xác**). Đánh dấu chuyển sang chu kỳ hoàn vốn cổ đông. [Báo Pháp luật VN](https://baophapluat.vn/dhdcd-vincom-retail-vre-2026-ke-hoach-lai-5-375-ty-dong-chot-chia-co-tuc-tien-mat-ty-le-10.html)
- **Khai trương TTTM mới (đã xảy ra, tích cực):** Vincom Plaza Đan Phượng (Hà Nội, 25.000 m²) khai trương tháng 8/2026, tỷ lệ lấp đầy ~93% trước khai trương — dự án trọng điểm Q3/2026.
- **KQKD nửa đầu 2026 (đã xảy ra, tích cực):** Khách đến TTTM tăng 13-15%, doanh số gian hàng chia sẻ doanh thu tăng 23-25% YoY. Kế hoạch cả năm: doanh thu 10.132 tỷ, LNST 5.375 tỷ (+16%/+15% YoY).
- **Catalyst FTSE (sắp xảy ra, tích cực, đã xác nhận):** VRE thuộc danh sách 27 mã Việt Nam vào rổ FTSE GEIS kỳ nâng hạng, nhóm Small Cap. Hiệu lực **21/9/2026**. [Dân trí](https://dantri.com.vn/kinh-doanh/27-co-phieu-viet-nam-vao-ro-chi-so-moi-noi-cua-ftse-nang-hang-co-hieu-luc-tu-219-20260821192938821.htm)

---

#### 📅 Sự kiện sắp tới (theo mã/ngành)
- **21/9/2026:** FTSE Russell chính thức phân bổ 27 mã CP Việt Nam vào rổ chỉ số mới nổi thứ cấp (GEIS), 6 mã lớn (gồm VIC) vào cả FTSE All-World — **VIC và VRE** trong danh sách candidate của hội đồng nằm trong nhóm hưởng lợi trực tiếp; PDR/KDH/PNJ **không** có trong danh sách 21/8 công bố.
- **Q3/2026:** VRE dự kiến trả cổ tức tiền mặt 10% (ngày cụ thể chưa kiểm chứng).
- **Q3/2026:** KDH mở bán tiếp phần cao tầng dự án Gladia (616 căn).
- Chưa xác định ngày GDKHQ cụ thể cho VIC/PDR/KDH/PNJ trong giai đoạn tới — cần cập nhật thêm gần ngày.

#### 🌐 Bối cảnh chung
- **Vĩ mô/ngành BĐS-tín dụng:** NHNN 2026 siết tốc độ tăng trưởng tín dụng BĐS của từng ngân hàng không vượt tốc độ tăng tín dụng chung của chính ngân hàng đó so với cuối 2025; ngân hàng vi phạm bị trừ room. Ngân hàng có xu hướng ưu tiên vốn cho dự án "pháp lý rõ ràng, nhu cầu ở thực" — có thể ảnh hưởng khác biệt giữa các chủ đầu tư (KDH được đánh giá pháp lý tốt/sạch nợ trái phiếu; PDR đang dùng phát hành cp+trái phiếu để cấp vốn dự án — rủi ro cao hơn). [Thời báo Tài chính VN](https://thoibaotaichinhvietnam.vn/tang-truong-tin-dung-2026-gioi-han-van-bat-dong-san-ngan-hang-vuot-rao-se-bi-tru-room-190385.html)
- **FTSE nâng hạng:** Xác nhận chính thức, hiệu lực 21/9/2026, ước tính ~1,33-1,45 tỷ USD vốn ETF/quỹ chỉ số phân bổ vào TTCK Việt Nam — dòng tiền định kỳ tập trung vào 27 mã trong danh sách (có VIC, VRE trong nhóm ứng viên của hội đồng). Cảnh báo từ báo chí: "đừng tưởng tiền tỷ đô đổ vào sau một đêm" — dòng vốn thực tế phân bổ dần theo lộ trình đến 9/2027. [Elibook](https://elibook.vn/2026/08/22/nang-hang-ftse-27-cai-ten-da-chot-nhung-dung-tuong-tien-ty-do-do-vao-sau-mot-dem/)
- **Giá vàng thế giới:** Biến động mạnh cuối tháng 8/2026 (đỉnh giữa tháng rồi điều chỉnh giảm ~49 USD/oz ngày 27/8), gắn với kỳ vọng lãi suất Fed (CME FedWatch: ~34% khả năng tăng lãi suất tháng 9, ~74% tháng 12 — số liệu này khá bất thường/cần kiểm chứng lại nguồn gốc, có thể model đã diễn giải sai chiều chính sách Fed).

---

#### 🏆 Xếp hạng theo hỗ trợ tin tức (mạnh → yếu)
1. **VRE** — cổ tức lần đầu sau 7 năm + KQKD tăng trưởng ổn định + catalyst FTSE xác nhận + TTTM mới khai trương. Tin tức đồng thuận tích cực, ít rủi ro tiêu cực rõ ràng.
2. **VIC** — KQKD kỷ lục + catalyst FTSE mạnh nhất (vào cả All-World), nhưng đòn bẩy tài chính rất cao là rủi ro nền cần lưu ý.
3. **KDH** — mở bán dự án thành công vượt kỳ vọng (90% booking) + sạch nợ trái phiếu, nhưng kế hoạch lợi nhuận 2026 tự đặt thấp hơn 2025 (tín hiệu thận trọng từ chính doanh nghiệp).
4. **PDR** — tín hiệu hỗn hợp: Chủ tịch mua vào + mở rộng dự án Lotte Thủ Thiêm (tích cực) nhưng đối trọng bởi pha loãng cổ phần lớn (200 triệu cp) + phát hành trái phiếu quy mô lớn (rủi ro tài chính).
5. **PNJ** — tin tức tiêu cực nổi bật nhất trong nhóm: lỗ kỷ lục Q2/2026 vì bê bối P-Lab + trích lập dự phòng lớn; rủi ro uy tín thương hiệu chưa rõ đã kết thúc hay chưa.

*Không phải khuyến nghị đầu tư. Đây là tổng hợp tin tức/bằng chứng cơ bản độc lập, phục vụ tranh luận nội bộ; mô hình định lượng có edge yếu (AUC ~0.53–0.55) nên tin tức chỉ nên dùng để bổ sung góc nhìn, không thay thế quản trị rủi ro (TP/SL/time-stop đã định trước).*



---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

### 🐂 Agent C — Tổng hợp hướng BÒ · 2026-09-01 05:45

*Trước khi vào luận điểm: mô hình định lượng có edge yếu (AUC ~0.53–0.55, theo cả Agent A và Agent B nhấn mạnh). Luận điểm bò dưới đây KHÔNG dựa vào score mô hình làm lý do chính — chỉ dùng score như bộ lọc sơ bộ, còn sức nặng thực sự đến từ sự **trùng khớp** giữa kỹ thuật (Agent A) và catalyst tin tức (Agent B).*

---

## 1. VRE — Vincom Retail (kèo bò rõ ràng nhất)

**Luận điểm mua:** Đây là mã hiếm hoi trong nhóm 5 ứng viên có sự đồng thuận đầy đủ giữa kỹ thuật và cơ bản. Theo Agent A, VRE "vừa cắt lên trên MA50 (uptrend mới hình thành)", RSI 58.7 — trung tính, còn dư địa tăng trước khi chạm vùng quá mua, và vol_ratio 1.44 cho thấy dòng tiền chủ động tham gia xác nhận đà tăng. Agent A gọi đây là "setup sạch nhất về động lượng" trong 5 mã. Agent B xếp VRE **hạng 1/5** về hỗ trợ tin tức, với "tin tức đồng thuận tích cực, ít rủi ro tiêu cực rõ ràng."

**Catalyst (theo Agent B):**
- Chia cổ tức tiền mặt 10% lần đầu sau 7 năm, dự kiến trả Q3/2026 — tín hiệu chuyển sang chu kỳ hoàn vốn cổ đông (ngày GDKHQ cụ thể chưa kiểm chứng).
- Vào rổ FTSE GEIS (nhóm Small Cap), hiệu lực 21/9/2026 — dòng vốn ETF/quỹ chỉ số sẽ phân bổ vào mã này theo lộ trình.
- KQKD nửa đầu 2026: khách đến TTTM tăng 13-15%, doanh số gian hàng chia sẻ doanh thu tăng 23-25% YoY; kế hoạch cả năm LNST +15% YoY.
- Khai trương Vincom Plaza Đan Phượng (8/2026, lấp đầy ~93% trước khai trương) — dự án mới đã có khách thuê, không phải kỳ vọng suông.

**Kịch bản giá tới TP:** Entry tham chiếu 26.100đ (giá 2026-08-28), TP 28.188đ (+8%). Theo Agent A, vùng cản cũ tháng 6 quanh 27.000-28.000đ có thể khiến giá chững lại trước khi chạm TP — đây là kịch bản hợp lý nhất: tăng dần, có thể nghỉ ở vùng cản cũ rồi bứt tiếp nhờ catalyst FTSE (21/9) và tin cổ tức làm chất xúc tác thứ hai đẩy giá qua vùng cản.

**Rủi ro & vì sao chịu được:** SL 24.795đ nằm dưới cả MA20 và MA50 hiện tại (theo Agent A) — nếu giá thủng ngưỡng này thì cấu trúc uptrend mới hình thành đã hỏng, cắt lỗ sớm và rõ ràng. Time-stop 25 ngày đủ để đón nhịp trước ngày hiệu lực FTSE 21/9. Rủi ro "vùng cản cũ chặn giá" đã được Agent A cảnh báo trước — nếu giá đi ngang quanh 27-28k thay vì bứt phá, đây là hành vi tích lũy bình thường trước catalyst, không phải tín hiệu hỏng setup, miễn SL chưa bị chạm.

---

## 2. VIC — Vingroup (kèo bò catalyst mạnh nhất, đi kèm rủi ro nền)

**Luận điểm mua:** Theo Agent A, VIC đang "trên MA50, MA20>MA50 (uptrend rõ)", vol_ratio 1.43 — cùng nhóm với VRE là 2 mã duy nhất có dòng tiền chủ động (vol_ratio >1.4) trong 5 ứng viên. Agent B xếp VIC hạng 2/5 về tin tức, với "KQKD kỷ lục + catalyst FTSE mạnh nhất."

**Catalyst (theo Agent B):**
- KQKD nửa đầu 2026: doanh thu hợp nhất ~222.000 tỷ đồng, LNST ~20.375 tỷ đồng; Vinhomes ghi nhận doanh thu quy đổi 6 tháng gấp 3 lần cùng kỳ — tăng trưởng thực, đã công bố, không phải kỳ vọng.
- Catalyst FTSE mạnh nhất nhóm: VIC không chỉ vào rổ FTSE GEIS (Large Cap, cùng VCB/VHM) mà còn thuộc nhóm 6 mã được thêm vào FTSE All-World — phạm vi dòng vốn thụ động lớn hơn VRE. Hiệu lực 21/9/2026.

**Kịch bản giá tới TP:** Entry 236.000đ, TP 254.880đ (+8%). Theo Agent A, giá "vừa có nến bứt phá lên ~242k rồi rút về 236k" — kịch bản hợp lý là đây là nhịp chốt lời ngắn hạn sau sóng tăng mạnh từ vùng 210-220k, tích lũy lại trước khi catalyst FTSE (21/9) kích hoạt dòng tiền mới đẩy giá lên vùng breakout 254.880đ (vùng giá chưa từng test).

**Rủi ro & vì sao chịu được:** Hai rủi ro rõ ràng đã có sẵn cơ chế bảo vệ. (1) RSI 68.7 gần vùng quá mua (theo Agent A) — nhưng SL 224.200đ nằm ngay dưới vùng hỗ trợ MA20/MA50 cũ, nghĩa là nếu đà tăng thực sự hụt hơi, hệ thống cắt lỗ trước khi thiệt hại lớn. (2) Đòn bẩy tài chính rất cao, nợ/tài sản ~86% (theo Agent B) — đây là rủi ro nền dài hạn, nhưng với time-stop 25 ngày, luận điểm bò ở đây không đặt cược vào sức khỏe tài chính dài hạn của VIC mà vào catalyst ngắn hạn có ngày cụ thể (21/9 FTSE), nằm gọn trong khung thời gian time-stop.

---

## 3. KDH — Khang Điền (kèo bò suy đoán, kỹ thuật chưa xác nhận — mức độ tự tin thấp hơn)

**Luận điểm mua:** Đây là mã có **tin tức cơ bản đáng chú ý nhất** trong nhóm còn lại nhưng **kỹ thuật chưa ủng hộ** — nêu ra để tranh luận, không phải kèo tự tin cao. Agent B xếp KDH hạng 3/5, ghi nhận: "mở bán dự án Gladia... hơn 90% sản phẩm giới thiệu đã có khách đặt cọc, tổng giá trị giao dịch gần 4.000 tỷ đồng" (1/8/2026) và "đã sạch nợ trái phiếu, không có kế hoạch phát hành vốn mới — giảm rủi ro tài chính" (theo ĐHĐCĐ 2026). Đây là 2 điểm tích cực có thật, đã xảy ra, không phải kỳ vọng.

**Catalyst:** Phần cao tầng dự án Gladia (616 căn) dự kiến mở bán tiếp Q3/2026 — nếu tỷ lệ hấp thụ tiếp tục cao như đợt mở bán đầu (90%), có thể là chất xúc tác dòng tiền/doanh thu ghi nhận trong các quý tới.

**Kịch bản giá tới TP:** Entry 18.200đ, TP 19.656đ (+8%). *Suy luận (chưa có xác nhận kỹ thuật):* nếu tin tức tích cực về Gladia lan tỏa rộng hơn ra thị trường, có thể kéo dòng tiền quay lại đủ để đẩy giá vượt MA20 rồi thử thách MA50.

**Rủi ro & vì sao chịu được — CẢNH BÁO RÕ:** Agent A xếp KDH vào nhóm "setup kỹ thuật yếu/rủi ro nhất" cùng PDR — downtrend rõ và kéo dài từ tháng 2, MA50 đang giảm dốc từ 26k xuống ~19k, nhịp hồi cuối biểu đồ "chỉ vừa chạm MA20... dạng bắt dao rơi trong xu hướng giảm chưa xác nhận đảo chiều", vol_ratio 0.84 (dưới trung bình) càng làm giảm độ tin cậy. Nói thẳng: tin tốt (Gladia, sạch nợ) **chưa được thị trường xác nhận bằng dòng tiền** — đây là lý do kèo này xếp thứ 3, không phải thứ 1. SL 17.290đ nằm dưới hỗ trợ hiện tại, và time-stop 25 ngày giới hạn thời gian chịu rủi ro nếu "bắt dao rơi" sai — nếu downtrend tiếp diễn, lệnh sẽ bị cắt hoặc hết hạn trước khi thiệt hại lan rộng.

---

## Phản biện trước (chuẩn bị cho Agent D)

- **"Score mô hình chỉ nhỉnh hơn tung đồng xu (AUC ~0.53-0.55)"** — Đúng, và vì vậy luận điểm bò ở đây không dựa vào score làm lý do chính. VIC/VRE được chọn vì **hai nguồn bằng chứng độc lập** (kỹ thuật của A + tin tức của B) cùng chỉ về một hướng, điều mà bản thân score không thể hiện được.
- **"VIC RSI gần quá mua, dễ điều chỉnh"** — Đã thừa nhận ở trên; đây chính là lý do SL đặt sát vùng hỗ trợ MA20/MA50, không phải lý do loại bỏ kèo.
- **"FTSE effective date 21/9 còn xa, sao biết giá phản ứng trước không sau"** — Đúng là chưa kiểm chứng được thời điểm chính xác thị trường "price in" catalyst này; time-stop 25 ngày từ 2026-08-28 rơi vào khoảng 2026-09-22, tức là bao trùm gần trọn giai đoạn tới ngày hiệu lực — nếu thị trường phản ứng sớm (trước ngày chính thức) thì vẫn nằm trong cửa sổ time-stop; nếu là hiện tượng "sell the news" sau 21/9 (rủi ro Agent B đã nêu cho VIC) thì đó là lý do chốt lời sớm, không phải lý do không vào lệnh.
- **"KDH downtrend rõ, sao vẫn đưa vào"** — Đưa vào có chủ đích ở mức độ tự tin thấp nhất trong 3 mã, nêu rõ kỹ thuật chưa xác nhận, để hội đồng cân nhắc — không phải khuyến nghị ngang hàng VIC/VRE.

---

**Kèo bò tự tin nhất: VRE** — mã duy nhất có sự đồng thuận đầy đủ giữa setup kỹ thuật sạch (uptrend mới, vol_ratio 1.44, RSI chưa quá mua) và chuỗi tin tức tích cực liên tiếp (cổ tức lần đầu sau 7 năm, FTSE, KQKD tăng trưởng, TTTM mới lấp đầy cao) — không có tín hiệu tiêu cực đáng kể nào được Agent A hoặc Agent B nêu ra cho mã này.

*Đây KHÔNG PHẢI khuyến nghị đầu tư. Luận điểm trên chỉ tổng hợp và khuếch đại các điểm tích cực đã có trong bằng chứng của Agent A và Agent B, phục vụ tranh luận nội bộ; mô hình định lượng có edge yếu (AUC ~0.53-0.55), quyết định cuối cần cân đối với phản biện của Agent D.*


---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

### 🐻 Agent D — Tổng hợp hướng GẤU + phản biện · 2026-09-01 06:00

*Vai trò: phản biện có cơ sở (devil's advocate), không bịa tin xấu. Nếu suy đoán sẽ ghi rõ "giả định"/"chưa kiểm chứng". Mục tiêu là stress-test luận điểm bò của Agent C, không phải bi quan cho có.*

---

## 0. Cảnh báo nền trước khi vào chi tiết: mô hình chỉ nhỉnh hơn tung đồng xu — và bản thân ensemble score đang "che" một sự bất đồng lớn

Agent C tự nhận "luận điểm bò không dựa vào score mô hình làm lý do chính". Nhưng nhìn vào breakdown 5 mô hình con trong `signals_latest.csv`, vấn đề còn nghiêm trọng hơn AUC 0.53–0.55 gợi ý:

| Mã | LogReg | RandomForest | GradBoost | XGBoost | LSTM | Score tổng |
|---|---|---|---|---|---|---|
| VIC | 0.685 | 0.665 | **0.504** | 0.554 | **0.816** | 0.645 |
| VRE | 0.585 | 0.527 | **0.403** | **0.439** | **0.875** | 0.566 |
| KDH | 0.514 | 0.604 | 0.513 | 0.575 | **0.740** | 0.589 |

Với **VRE — "kèo bò tự tin nhất" của Agent C** — 2/5 mô hình con (GradBoost 0.403, XGBoost 0.439) dự đoán xác suất đạt TP **thấp hơn 50%**, tức là *nghiêng về khả năng KHÔNG đạt TP*. Điểm tổng 0.566 chỉ "nhỉnh" vì LSTM cho ra 0.875 — một outlier cao bất thường so với 4 mô hình còn lại. Với VIC cũng tương tự: GradBoost gần như tung đồng xu (0.504), XGBoost chỉ 0.554. Nói cách khác, phần "đồng thuận" mà Agent C nhấn mạnh (kỹ thuật A + tin tức B cùng hướng) **không hề được phản ánh trong đồng thuận giữa các mô hình định lượng** — 2 trong 5 thuật toán tree-based đang nói ngược lại đúng lúc C chọn 2 mã này làm kèo tự tin nhất. Đây là lý do để hoài nghi thêm, không phải để bác bỏ hoàn toàn, nhưng cần nêu rõ cho Agent E.

---

## 1. Phản biện từng luận điểm của Agent C

### VRE
- **Agent C cho rằng** đây là "kèo bò rõ ràng nhất" nhờ đồng thuận kỹ thuật + tin tức. **Nhưng**: chính Agent A đã cảnh báo vùng cản cũ tháng 6 (27.000–28.000đ) gần như trùng khít với TP 28.188đ — nghĩa là gần như toàn bộ biên độ mục tiêu (+8%) nằm ngay trong hoặc sát vùng kháng cự đã từng chặn giá trước đây. Agent C thừa nhận rủi ro này nhưng gán nhãn "tích lũy bình thường trước catalyst" — đây là một *diễn giải lạc quan*, không phải sự thật đã kiểm chứng; kịch bản ngược lại (giá bị chặn hẳn tại 27–28k và quay đầu về MA20/MA50 rồi chạm SL) có xác suất tương đương và không được Agent C định lượng.
- **Agent C cho rằng** cổ tức tiền mặt 10% (lần đầu sau 7 năm) là chất xúc tác tích cực. **Nhưng** theo chính Agent B, "ngày GDKHQ cụ thể chưa kiểm chứng" — nếu ngày chốt quyền rơi ngoài time-stop 25 ngày (đến ~22/9), catalyst này có thể không kịp phát huy tác dụng trong khung thời gian của lệnh. Tỷ suất cổ tức tuyệt đối (1.000đ/26.100đ ≈ 3,8%) cũng không đủ lớn để một mình đẩy giá vượt kháng cự nếu không có dòng tiền khác hỗ trợ.
- **Agent C cho rằng** catalyst FTSE (hiệu lực 21/9) là điểm cộng lớn. **Nhưng** danh sách 27 mã đã công bố từ 21/8 — tức là **11 ngày trước thời điểm entry tham chiếu (28/8)** thị trường đã biết tin này. Rủi ro "price-in trước, bán ra sau ngày hiệu lực" (sell the news) mà chính Agent B cảnh báo cho VIC cũng áp dụng được cho VRE — Agent C chỉ né rủi ro này ở mục VIC mà không đề cập cho VRE, dù cùng một catalyst và cùng ngày hiệu lực.
- **Rủi ro thanh khoản/độ mới của tín hiệu:** vol_ratio 1.44 là một con số tại một thời điểm (28/8) — Agent A không xác nhận đây là xu hướng dòng tiền bền vững qua nhiều phiên hay chỉ một phiên đột biến. Agent C mặc định coi đây là "dòng tiền chủ động xác nhận đà tăng" nhưng đó là suy diễn, chưa có bằng chứng về tính liên tục.

### VIC
- **Agent C cho rằng** nến rút chân từ 242k về 236k là "chốt lời ngắn hạn... tích lũy lại trước catalyst". **Nhưng** đây là một trong hai cách diễn giải khả dĩ — cách còn lại là bắt đầu phân phối (distribution) sau một sóng tăng mạnh, đặc biệt khi RSI đã chạm 68,7 sát vùng quá mua. Agent A không khẳng định đây là tích lũy; Agent C đã chọn diễn giải có lợi cho luận điểm mua mà không nêu khả năng ngược lại.
- **Agent C cho rằng** SL 224.200đ "bảo vệ" nếu đà tăng hụt hơi. **Nhưng** đây là chấp nhận rủi ro giảm 5% để đổi lấy cơ hội tăng 8% vào một vùng giá "chưa từng test" (breakout) — tỷ lệ R:R khoảng 1:1,6 chỉ hấp dẫn *nếu* xác suất thành công đủ cao, mà như mục 0 đã nêu, 2/5 mô hình con gần như trung lập/tiêu cực về khả năng này.
- **Agent C cho rằng** đòn bẩy tài chính cao (nợ/tài sản ~86%) chỉ là "rủi ro nền dài hạn", không ảnh hưởng trong khung time-stop 25 ngày. **Nhưng** Agent B cũng nêu bối cảnh vĩ mô: NHNN đang siết tăng trưởng tín dụng bất động sản theo từng ngân hàng trong năm 2026. Một cổ phiếu có đòn bẩy cao trong chính giai đoạn ngành bị siết tín dụng dễ nhạy cảm hơn với tin tức chính sách/thanh khoản bất ngờ — rủi ro này có thể kích hoạt *trong* 25 ngày tới nếu có tin siết room tín dụng cụ thể, không nhất thiết phải đợi "dài hạn".
- **Điểm C không nhắc tới:** VIC đã tăng mạnh từ vùng 210-220k trước khi vào lệnh — nghĩa là phần lớn "tin tốt" KQKD nửa đầu năm 2026 (đã công bố) và triển vọng FTSE (đã biết từ 21/8) nhiều khả năng đã phần nào phản ánh vào giá. Mua ở gần đỉnh ngắn hạn (236k, cách đỉnh 242k chỉ 2,5%) sau một sóng tăng dài là rủi ro "mua đỉnh" cổ điển mà C không đề cập.

### KDH
- Agent C tự xếp đây là kèo "mức độ tự tin thấp hơn" — D đồng ý và **nhấn mạnh thêm**: theo dữ liệu gốc, `trend_up = False` cho KDH (cũng như PDR, PNJ) — tức bản thân pipeline định lượng đã gắn nhãn xu hướng giảm, không phải "trung tính chờ xác nhận" như cách diễn đạt của C. Đây là bắt dao rơi theo đúng nghĩa, được cả Agent A và dữ liệu thô xác nhận.
- Tin tốt Gladia (90% booking) là thật, nhưng đã xảy ra từ 1/8/2026 — gần 1 tháng trước entry (28/8) — nếu tin này đủ mạnh để đảo chiều dòng tiền, nhẽ ra đã phải thấy vol_ratio tăng lên; thực tế vol_ratio KDH chỉ 0,84 (dưới trung bình), nghĩa là thị trường đã có gần 1 tháng để phản ứng và **chưa phản ứng**. Đây là bằng chứng ngược lại khá mạnh mà Agent C không đối chiếu thời gian.

---

## 2. Rủi ro downside theo mã (tới SL hoặc xa hơn)

- **VIC:** RSI 68,7 sát quá mua sau sóng tăng mạnh → rủi ro điều chỉnh sâu nếu dòng tiền chốt lời lan rộng, đặc biệt nếu xảy ra "sell the news" quanh/sau 21/9 (rủi ro chính Agent B nêu). Đòn bẩy 86% nợ/tài sản kết hợp bối cảnh NHNN siết tín dụng BĐS là rủi ro hệ thống có thể kích hoạt bất ngờ. Biên độ giao dịch ±7%/phiên + T+2 (không bán được ngay khi vừa mua) khiến việc "thoát sớm" khi có tin xấu bất ngờ trong 1-2 phiên đầu gần như bất khả thi.
- **VRE:** Vùng kháng cự 27.000–28.000đ nằm sát TP — nếu bị chặn và có áp lực bán chung ngành BĐS (NHNN siết room tín dụng ảnh hưởng cả nhóm), giá có thể quay đầu nhanh về vùng SL 24.795đ (chỉ cách entry ~5%). Rủi ro cổ tức bị hoãn/GDKHQ ngoài time-stop.
- **KDH:** Downtrend dài từ tháng 2 (MA50 giảm từ 26k→19k) chưa có dấu hiệu đảo chiều theo khối lượng; nếu đợt mở bán cao tầng Gladia Q3/2026 không đạt tỷ lệ hấp thụ như đợt đầu, hoặc tín dụng BĐS bị siết ảnh hưởng tới tiến độ giải ngân của khách mua nhà, giá dễ tiếp tục giảm xuyên SL 17.290đ.
- **PDR (không được C đưa vào bò nhưng nằm trong top 5, cần nêu vì rủi ro cao):** Agent A xếp kỹ thuật yếu nhất nhóm (vol_ratio 0,61, downtrend dài từ tháng 3). Agent B nêu rủi ro pha loãng cổ phần lớn (200 triệu cp, giá phát hành thấp hơn thị giá) + phát hành trái phiếu 5.600 tỷ — áp lực pha loãng/nợ vay là rủi ro thực, đã xảy ra/đang triển khai, không phải suy đoán.
- **PNJ (ngoài phạm vi bò của C nhưng đáng lưu ý cho E):** lỗ kỷ lục quý II/2026 (-283 tỷ) do bê bối P-Lab là tin xấu mới, rủi ro uy tín thương hiệu "chưa kiểm chứng liệu đã xử lý dứt điểm" — nếu Agent E cân nhắc đa dạng hóa ngoài nhóm BĐS, cần biết rủi ro này chưa hết.
- **Rủi ro tập trung ngành (hệ thống, áp dụng chung):** 4/5 mã ứng viên top-score (VIC, PDR, KDH, VRE) đều thuộc nhóm BĐS. Nếu Agent E chọn cả VIC + VRE (kèo tự tin nhất của C) cùng lúc, đây **không phải hai vị thế độc lập** — cùng chịu chung rủi ro chính sách tín dụng BĐS, tâm lý ngành, và khối ngoại (nếu có bán ròng nhóm BĐS). Một tin chính sách bất lợi (VD: siết room tín dụng cụ thể một ngân hàng lớn cho vay BĐS) có thể khiến cả hai chạm SL gần như đồng thời.

---

## 3. Mã nên tránh / rủi ro nhất

1. **PDR** — kỹ thuật yếu nhất nhóm (theo Agent A: downtrend dài, vol_ratio 0,61 thấp nhất), cộng thêm rủi ro pha loãng cổ phần + phát hành trái phiếu lớn (theo Agent B) — hai lớp rủi ro kỹ thuật và cơ bản cùng tiêu cực, không có catalyst FTSE bù đắp.
2. **KDH** — downtrend xác nhận bởi cả kỹ thuật (`trend_up=False`) lẫn thời gian (tin tốt Gladia đã gần 1 tháng mà chưa kéo được dòng tiền) — dạng bắt dao rơi rủi ro cao, đúng như Agent C tự thừa nhận mức tin cậy thấp nhất.
3. **VIC** (thận trọng, không phải "tránh tuyệt đối" nhưng rủi ro downside lớn nhất trong 2 mã C tự tin nhất) — mua gần đỉnh ngắn hạn sau sóng tăng dài, RSI sát quá mua, đòn bẩy tài chính cao đúng lúc ngành bị siết tín dụng, và catalyst FTSE đã được biết trước 11 ngày (rủi ro sell-the-news do chính Agent B cảnh báo).

---

**Nhắc lại:** mô hình định lượng có edge yếu (AUC ~0.53–0.55) — chỉ nhỉnh hơn tung đồng xu một chút. Như phân tích ở mục 0, ngay cả trong 2 mã được Agent C chọn làm kèo tự tin nhất, một nửa số mô hình con trong ensemble (GradBoost, XGBoost) không đồng thuận với hướng mua. Sự "đồng thuận kỹ thuật + tin tức" mà Agent C nhấn mạnh là có thật ở tầng định tính, nhưng không nên diễn giải thành xác suất thắng cao — đây vẫn là các kèo xác suất mỏng, cần tuân thủ nghiêm ngặt SL/time-stop đã định sẵn, không nới lỏng dựa trên câu chuyện catalyst.

*Đây KHÔNG PHẢI khuyến nghị đầu tư. Toàn bộ nội dung trên là phản biện nội bộ phục vụ tranh luận, dựa trên dữ liệu và bằng chứng đã có trong whiteboard của Agent A/B/C — không bổ sung tin tức mới ngoài các nguồn đã trích dẫn.*


---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*

### 🎩 Agent E — Giám đốc Chiến lược · 2026-09-01 06:15

*KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — khung ra quyết định mô phỏng.*

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| **VRE** | THEO DÕI | TB | Đồng thuận kỹ thuật+tin tức tốt nhất nhóm, nhưng kháng cự 27-28k trùng sát TP + FTSE đã biết trước 11 ngày + ensemble chia rẽ → chờ xác nhận breakout thay vì mua đuổi. |
| **VIC** | THEO DÕI | TB | Catalyst FTSE mạnh nhất + KQKD kỷ lục, nhưng RSI sát quá mua, mua gần đỉnh ngắn hạn, đòn bẩy 86% giữa lúc siết tín dụng BĐS → chờ hồi về hỗ trợ. |
| **KDH** | TRÁNH | Cao | `trend_up=False` xác nhận downtrend; tin tốt Gladia đã gần 1 tháng mà vol_ratio vẫn dưới trung bình — thị trường chưa phản ứng, bắt dao rơi. |
| **PDR** | TRÁNH | Cao | Kỹ thuật yếu nhất nhóm + rủi ro pha loãng 200 triệu cp/phát hành trái phiếu lớn, không có catalyst bù đắp. |
| **PNJ** | TRÁNH | Cao | Lỗ kỷ lục Q2/2026 vì bê bối P-Lab, rủi ro uy tín chưa xử lý dứt điểm, kỹ thuật yếu không xác nhận nhịp hồi. |

**Stance danh mục: Thận trọng.** Mô hình có edge yếu (AUC ~0,53–0,55) và ngay 2 mã tốt nhất vẫn có 2/5 mô hình con nghiêng dưới 50%; 4/5 ứng viên cùng ngành BĐS là rủi ro tập trung. Không giải ngân mới ngay; nếu tham gia VIC/VRE chỉ ở size nhỏ (2-3% mỗi mã) và chờ xác nhận kỹ thuật thêm.

→ Chi tiết đầy đủ: `debate/DECISION.md`

