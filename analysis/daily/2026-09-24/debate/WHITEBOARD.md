# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-09-24)

*Board tạo lúc 2026-09-24 05:07:29. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.356** · buy&hold kỳ kiểm định **0.3591**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): GAS, PNJ, VIC, KDH, GVR
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **GAS** | Energy | 84,200 | 0.55 | 90,936 | 79,990 | 51 | ↑ trên MA50 |
| 2 | **PNJ** | Retail/Consumer | 34,100 | 0.54 | 36,828 | 32,395 | 34 | ↓ dưới MA50 |
| 3 | **VIC** | RealEstate | 230,500 | 0.52 | 248,940 | 218,975 | 47 | ↑ trên MA50 |
| 4 | **KDH** | RealEstate | 15,700 | 0.48 | 16,956 | 14,915 | 33 | ↓ dưới MA50 |
| 5 | **GVR** | Materials | 33,000 | 0.47 | 35,640 | 31,350 | 61 | ↑ trên MA50 |

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

### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-09-24 12:08

| Mã | Trend (giá vs MA20/MA50) | RSI(14) | Vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **GVR** | ↑ trên MA20 & MA50, MA50 vừa tạo đáy và đang ngóc lên sau downtrend 05→07 | 61.2 (trung tính, ngả hưng phấn, chưa quá mua) | 1.44 (>1, cao nhất nhóm) | **7/10** | Hồi phục có xác nhận khối lượng tốt nhất nhóm; entry 33,000 nằm dưới vùng cản cũ 34.5–36k (đỉnh đi ngang T5–T6) → TP +8% (35,640) khớp vùng cản này, hợp lý nhưng không dễ vượt ngay. |
| **GAS** | ↑ trên MA50, vừa điều chỉnh từ đỉnh gần nhất (~93k) về 84,200 | 51.2 (trung tính) | 0.34 (èo uột) | **6/10** | Xu hướng tăng rõ nhưng cú giảm/entry hiện tại không có khối lượng xác nhận; TP +8% (90,936) nằm sát đỉnh cũ gần nhất → có thể gặp cản. SL (79,990) gần MA50, hợp lý về mặt hỗ trợ. |
| **VIC** | ↑ trên MA50, đang pullback từ đỉnh 265k về 230,500 | 47.5 (trung tính) | 0.23 (yếu nhất nhóm) | **5.5/10** | Trend tăng tốt nhưng pullback gần như không khối lượng — chưa rõ là nghỉ ngơi hay đảo chiều. TP +8% (248,940) đúng vùng đỉnh gần nhất; SL (218,975) dưới MA50, hợp lý. |
| **PNJ** | ↓ dưới MA20 & MA50, MA50 vẫn dốc xuống dù giá đang đi ngang 34–38k vài tuần gần đây | 33.7 (gần quá bán nhưng chưa xác nhận) | 0.60 (<1, yếu) | **3.5/10** | Downtrend dài (từ ~76k về 34k) chưa có tín hiệu đảo chiều kỹ thuật rõ ràng (không phân kỳ RSI rõ, không có khối lượng đột biến) — mua ở đây gần giống "bắt dao rơi" nhẹ, dù giá đã bớt rơi mạnh. TP +8% (36,828) trùng vùng đỉnh đi ngang gần đây, khả thi nếu có hồi kỹ thuật. |
| **KDH** | ↓ dưới MA20 & MA50 rõ rệt, MA50 dốc xuống liên tục 6 tháng | 33.1 (gần quá bán, chưa xác nhận đảo chiều) | 0.32 (èo uột) | **2.5/10** | Cảnh báo **bắt dao rơi**: downtrend rất bền (từ ~27k về 15.7k), chưa có nến/khối lượng xác nhận tạo đáy. Setup kỹ thuật yếu nhất nhóm. |

**Xếp hạng kỹ thuật (giảm dần):** GVR > GAS > VIC > PNJ > KDH

- **Setup đẹp nhất về kỹ thuật:** GVR — trend đảo chiều tăng có xác nhận khối lượng (vol_ratio 1.44 duy nhất >1 trong nhóm), RSI còn dư địa trước vùng quá mua.
- **Setup tệ nhất / rủi ro kỹ thuật lớn nhất:** KDH — downtrend kéo dài dưới cả MA20/MA50, RSI gần quá bán nhưng chưa có dấu hiệu đảo chiều nào (nến/khối lượng) → nguy cơ "bắt dao rơi" cao nhất.
- GAS và VIC đều đang uptrend nhưng cú pullback hiện tại **không có khối lượng xác nhận** (vol_ratio 0.34 và 0.23) — cần thận trọng vì thiếu áp lực mua rõ ràng ở entry.
- PNJ: RSI thấp (33.7) gợi ý có thể sắp quá bán nhưng vẫn nằm dưới MA50 đang dốc xuống — chưa đủ bằng chứng kỹ thuật để gọi là đáy, chỉ là "có thể đang tạo nền".
- Toàn bộ TP +8%/SL −5% đều rơi vào vùng hỗ trợ/kháng cự gần đúng vị trí kỹ thuật hợp lý (đỉnh/đáy gần nhất hoặc MA50) đối với cả 5 mã — không mã nào có TP/SL đặt "vô lý" so với cấu trúc giá.
- Toàn bộ vol_ratio dưới 1 ngoại trừ GVR — nhìn chung khối lượng nhóm ứng viên top-5 khá yếu, cần tôn trọng edge mô hình yếu (AUC ~0.53–0.55): các điểm trên chỉ là xác suất, không phải tín hiệu chắc chắn.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**

### 🅱️ Agent B — Phân tích News / Cơ bản · 2026-09-24 05:20

*Ghi chú: mô hình quant có edge YẾU (AUC ~0.53–0.55), 5 mã dưới đây chỉ là ứng viên top-score để tranh luận, không phải khuyến nghị mua. Toàn bộ nội dung dưới đây KHÔNG PHẢI khuyến nghị đầu tư.*

---

#### GAS (PV GAS — Energy)
- **KQKD tích cực**: lợi nhuận 8 tháng đầu 2026 đạt hơn 14.500 tỷ đồng, vượt kế hoạch cả năm 29-30%; doanh thu lập đỉnh mới. Sắc thái: **tích cực**. [Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/pv-gas-gas-loi-nhuan-8-thang-dat-hon-14500-ty-dong-chot-quyen-co-tuc-25-va-bau-bo-sung-3-thanh-vien-hdqt-post397608.html), [MekongASEAN](https://mekongasean.vn/doanh-thu-lap-dinh-moi-pv-gas-du-kien-chia-co-tuc-25-bang-tien-mat-55331.html)
- **Cổ tức 25% tiền mặt (2.500đ/CP)**: ngày GDKHQ đã qua là **22/9/2026**, ngày thanh toán dự kiến **20/11/2026**, tổng chi ~6.032 tỷ đồng, PVN (cổ đông lớn) nhận ~5.777 tỷ. Vì ex-date đã qua trước ngày phân tích (24/9), giá tham chiếu hiện tại đã điều chỉnh giảm theo cổ tức — cần đối chiếu với dữ liệu giá trong signals_latest.csv (không tự suy diễn tác động cụ thể lên giá). Sắc thái: **trung tính/tích cực** (dòng tiền cổ tức lớn nhưng đã phản ánh vào giá). [DNSE](https://www.dnse.com.vn/senses/tin-tuc/pv-gas-chot-ngay-tra-co-tuc-pvn-du-kien-nhan-gan-5800-ty-dong-35286573), [Vietstock lịch cổ tức](https://vietstock.vn/2026/09/co-tuc-tuan-21-2509-noi-bat-khoan-co-tuc-6-ngan-ty-cua-pv-gas-738-1494029.htm)
- **Rủi ro tin tức — cần kiểm chứng thêm**: có bài báo tựa đề "PV GAS sắp trả hơn 6.000 tỷ đồng cổ tức **giữa lúc vướng tiêu chuẩn công ty đại chúng**" — tiêu đề gợi ý vấn đề tuân thủ/tiêu chuẩn công ty đại chúng, nhưng tôi **chưa kiểm chứng được nội dung chi tiết** của vấn đề này (chỉ thấy tiêu đề qua kết quả tìm kiếm, chưa đọc được toàn văn). Ghi nhận là **rủi ro chưa kiểm chứng, cần Agent E hoặc người dùng tự tra cứu thêm** trước khi coi là yếu tố quyết định. [CafeF](https://cafef.vn/pv-gas-sap-tra-hon-6000-ty-dong-co-tuc-giua-luc-vuong-tieu-chuan-cong-ty-dai-chung-188260909151438803.chn)
- **Chiến lược dài hạn**: mục tiêu doanh thu 205.000-250.000 tỷ đồng vào 2030, mở rộng LNG và năng lượng tái tạo — thông tin định hướng, không phải catalyst ngắn hạn. Sắc thái: **trung tính (dài hạn)**.

#### PNJ (Vàng bạc đá quý Phú Nhuận — Retail/Consumer)
- **KQKD lẫn lộn**: 6 tháng đầu 2026 doanh thu thuần 25.729 tỷ đồng (+49,4% YoY), LNST 1.256 tỷ đồng (+6,3% YoY) — tăng trưởng doanh thu mạnh. Nhưng **riêng quý 2/2026 lỗ sau thuế 283 tỷ đồng** do chủ động trích lập dự phòng (có nguồn ghi ước tính trích lập ~865 tỷ đồng, cần đối chiếu số liệu chính thức). Sắc thái: **hỗn hợp** (doanh thu tốt nhưng lợi nhuận quý 2 âm vì dự phòng). [Thanh Niên](https://thanhnien.vn/pnj-duy-tri-da-tang-truong-quy-2-12-doanh-thu-6-thang-dat-25729-ti-dong-185260731083355808.htm), [VnEconomy](https://vneconomy.vn/pnj-bao-lo-quy-2-do-trich-lap-du-phong-uoc-tinh-865-ty-dong.htm), [Nhịp cầu đầu tư](https://nhipcaudautu.vn/su-kien-doanh-nghiep/doanh-thu-quy-ii-tang-12-pnj-tiep-tuc-mo-rong-tep-khach-hang-3365501/)
- **Rủi ro nền**: có bài phân tích nhắc tới "cái giá phải trả từ biến cố kim cương" — liên quan sự cố trước đây về kim cương nhân tạo trà trộn, ảnh hưởng đến niềm tin thương hiệu. **Chưa kiểm chứng mức độ ảnh hưởng hiện tại** (bài không có ngày cụ thể rõ ràng trong kết quả tìm kiếm). Sắc thái: **tiêu cực (rủi ro thương hiệu, cần kiểm chứng thêm)**. [TheLeader](https://theleader.vn/pnj-va-cai-gia-phai-tra-tu-bien-co-kim-cuong-d47102.html)
- **Mảng lõi vẫn tốt**: doanh thu trang sức bán lẻ 6 tháng +13,6% YoY nhờ khách hàng mới lẫn hiện hữu. Sắc thái: **tích cực**.
- Không tìm được tin tức/catalyst mới đáng chú ý nào khác trong khoảng thời gian gần nhất (giữa-cuối tháng 9/2026) — "chưa kiểm chứng thêm".

#### VIC (Vingroup — Real Estate)
- **Thay đổi nhân sự cấp cao**: Nghị quyết HĐQT số 31/2026 ngày 09/9/2026 miễn nhiệm bà Mai Hương Nội khỏi vị trí Phó Tổng Giám đốc sau gần 14 năm gắn bó (lý do cá nhân theo công bố). Sau miễn nhiệm, bà không còn là người nội bộ của Vingroup. Đây là thay đổi nhân sự cấp cao nhưng không có dấu hiệu liên quan sai phạm/pháp lý trong các nguồn đã đọc. Sắc thái: **trung tính/hơi tiêu cực** (mất nhân sự kỳ cựu, nhưng lý do "cá nhân" — cần kiểm chứng thêm động cơ thực sự). [Vietstock](https://vietstock.vn/2026/09/vingroup-mien-nhiem-ba-mai-huong-noi-khoi-vi-tri-pho-tong-giam-doc-sau-14-nam-214-1490705.htm), [Dân Trí](https://dantri.com.vn/kinh-doanh/vingroup-mien-nhiem-mot-nu-tuong-sau-20-nam-gan-bo-20260909202615309.htm)
- **Dòng tiền lớn**: có nguồn (chưa kiểm chứng độc lập, dạng tin "dòng tiền cá mập") cho biết khối ngoại và tự doanh gom mạnh VIC ngày 10/9/2026. Đây là loại tin **suy đoán dòng tiền, không phải công bố chính thức** — ghi nhận "chưa kiểm chứng" và cần thận trọng.
- **Diễn biến giá**: theo dữ liệu thị trường, VIC tăng khoảng 11,4% trong tháng 9/2026 (tính đến ~21/9), đây là dữ liệu giá chứ không phải catalyst cụ thể.
- Không tìm thấy KQKD quý gần nhất hay tin lớn về dự án/pháp lý mới trong phạm vi tìm kiếm này — "chưa kiểm chứng thêm", khuyến nghị tra cứu báo cáo tài chính quý 2/2026 của VIC riêng nếu cần độ tin cậy cao hơn.

#### KDH (Nhà Khang Điền — Real Estate)
- **Rủi ro tài chính đáng chú ý**: tính đến cuối tháng 6/2026, dư nợ vay toàn hệ thống đạt 16.659 tỷ đồng (tăng thêm hơn 6.500 tỷ chỉ trong nửa đầu năm), tỷ lệ nợ vay/vốn chủ sở hữu lên tới 83%; tồn kho gần 29.500 tỷ đồng. Sắc thái: **tiêu cực rõ rệt** (đòn bẩy tài chính tăng nhanh, tồn kho lớn — rủi ro thanh khoản BĐS). [Thương Trường](https://thuongtruong.com.vn/news/nha-khang-dien-kdh-no-vay-vuot16600-ty-dong-ton-kho-gan-29500-ty-giua-luc-co-phieu-giam-manh-169594.html), [Doanh Nhân Pháp Luật](https://doanhnhan.baophapluat.vn/hang-ton-kho-va-no-vay-tang-vot-nha-khang-dien-kdh-chat-vat-tim-luc-do-gia-co-phieu.html)
- **Giá cổ phiếu chạm đáy nhiều năm**: phiên 17/9/2026 đóng cửa 15.600đ, xuyên thủng vùng đáy thiết lập trong khủng hoảng trái phiếu 2022, thấp nhất 6 năm. Sắc thái: **tiêu cực** (xác nhận xu hướng giảm mạnh, phù hợp với RSI thấp 33 và trend "dưới MA50" trong signals_latest.csv).
- **Vướng quy định phát hành trái phiếu**: nhận văn bản số 9074, 9075 từ UBCKNN ngày 14/9/2026 liên quan tuân thủ quy định chào bán trái phiếu doanh nghiệp. **Chưa kiểm chứng được nội dung/mức độ nghiêm trọng cụ thể** của văn bản này — cần đọc công bố gốc trên HOSE/UBCKNN để đánh giá đầy đủ. Sắc thái: **tiêu cực tiềm ẩn (chưa kiểm chứng đầy đủ)**.
- → KDH là mã có **rủi ro tin tức/cơ bản rõ rệt nhất** trong nhóm 5 mã, dù giá đã chiết khấu sâu (có thể hấp dẫn về định giá kỹ thuật nhưng nền tảng cơ bản đang xấu đi).

#### GVR (Tập đoàn Công nghiệp Cao su Việt Nam — Materials)
- **Động lực tăng trưởng 2026**: lợi nhuận tích cực chủ yếu nhờ giá cao su tăng mạnh, cộng thêm thanh lý gỗ cao su và thu nhập bồi thường đất chuyển đổi sang đất khu công nghiệp; mảng KCN dự kiến doanh thu 344 tỷ đồng (+6%) nhờ giá thuê đất tăng. Sắc thái: **tích cực (nhưng nguồn không ghi rõ ngày công bố, cần kiểm chứng tính thời sự)**. [Finhay](https://www.finhay.com.vn/en/co-phieu-gvr), [24HMoney](https://24hmoney.vn/news/co-phieu-gvr-duy-tri-da-tang-tu-mang-nao-trong-nam-2026-c1a2698968.html)
- **Tín hiệu giao dịch cần thận trọng**: có ghi nhận "dấu hiệu phân phối từ tổ chức" vào các ngày 20, 23, 24/8 và 16/9/2026 — đây là quan sát dòng tiền/giao dịch, **chưa kiểm chứng nguồn gốc số liệu**, nên xem là tín hiệu kỹ thuật hơn là tin cơ bản xác thực. Sắc thái: **tiêu cực nhẹ (chưa kiểm chứng)**.
- Giá đã giảm đáng kể so với đỉnh lịch sử 46.500đ (04/3/2026) về vùng ~31.000-33.000đ — không tìm được lý do sụt giảm cụ thể qua tin tức, "chưa kiểm chứng thêm".
- Không tìm thấy catalyst ngắn hạn cụ thể (KQKD quý, ĐHĐCĐ, ex-date) trong phạm vi tìm kiếm này.

---

### 📅 Sự kiện sắp tới (toàn nhóm)
- **GAS**: thanh toán cổ tức tiền mặt 25% dự kiến **20/11/2026** (ex-date đã qua 22/9/2026).
- **KDH**: cần theo dõi phản hồi/động thái tiếp theo sau văn bản UBCKNN số 9074, 9075 (14/9/2026) — **chưa có thông tin về hậu quả cụ thể, chưa kiểm chứng**.
- Không có thông tin xác thực về ĐHĐCĐ bất thường, phát hành thêm, hay thoái vốn sắp tới cho VIC, PNJ, GVR trong phạm vi tìm kiếm này.

### 🌏 Bối cảnh chung (vĩ mô/ngành)
- **Sự kiện lớn nhất tháng 9/2026**: FTSE Russell chính thức nâng hạng TTCK Việt Nam từ Frontier Market lên **Secondary Emerging Market**, có hiệu lực từ **21/9/2026**, phân bổ theo lộ trình 4 giai đoạn (10% → 30% → 65% → 100%) hoàn tất vào 9/2027. Cơ sở pháp lý: Thông tư 08/2026/TT-BTC đảm bảo nhà đầu tư nước ngoài tiếp cận qua công ty chứng khoán toàn cầu. Đây là catalyst vĩ mô **tích cực mạnh** cho toàn thị trường, đặc biệt nhóm vốn hóa lớn dễ lọt rổ ETF (VIC, GAS thuộc nhóm này có khả năng hưởng lợi dòng vốn ngoại nhiều hơn PNJ/KDH/GVR vốn hóa nhỏ hơn). [VnEconomy](https://vneconomy.vn/ftse-russell-xac-nhan-viet-nam-vuot-qua-ky-review-chinh-thuc-nang-hang-vao-thang-92026), [Báo Chính phủ](https://baochinhphu.vn/chinh-thuc-xac-nhan-lo-trinh-nang-hang-thi-truong-chung-khoan-viet-nam-102260407214555354.htm), [SGGP](https://www.sggp.org.vn/chung-khoan-thang-9-tam-diem-nang-hang-va-ky-vong-don-dong-von-ngoai-post869745.html)
- Ngành BĐS (VIC, KDH) đang trong giai đoạn phân hóa mạnh: nhóm lớn (VIC) được đỡ bởi kỳ vọng dòng vốn ngoại + tin tức nâng hạng, trong khi nhóm vừa (KDH) đối mặt áp lực nợ vay và tồn kho cao — không nên gộp chung nhận định ngành cho cả hai mã.
- Ngành năng lượng (GAS) hưởng lợi từ KQKD vượt kế hoạch, nhưng cần theo dõi thêm về vấn đề "tiêu chuẩn công ty đại chúng" chưa kiểm chứng nêu trên.

### 🏆 Xếp hạng theo mức hỗ trợ tin tức (mạnh → yếu)
1. **GAS** — KQKD vượt kế hoạch rõ rệt, cổ tức tiền mặt lớn, hưởng lợi câu chuyện nâng hạng; điểm trừ nhỏ là tin "vướng tiêu chuẩn công ty đại chúng" chưa kiểm chứng.
2. **VIC** — hưởng lợi câu chuyện nâng hạng FTSE (vốn hóa lớn), giá tăng tốt trong tháng, nhưng có thay đổi nhân sự cấp cao và thiếu KQKD mới để xác nhận.
3. **PNJ** — doanh thu và mảng lõi tăng trưởng tốt, nhưng lợi nhuận quý 2 âm vì trích lập dự phòng + rủi ro thương hiệu chưa kiểm chứng rõ mức độ.
4. **GVR** — có câu chuyện giá cao su/đất KCN tích cực nhưng thiếu catalyst gần đây, có tín hiệu phân phối chưa kiểm chứng.
5. **KDH** — tin tức cơ bản tiêu cực rõ rệt nhất: nợ vay tăng vọt, tồn kho cao, giá chạm đáy nhiều năm, vướng vấn đề UBCKNN chưa rõ mức độ.

---
*Ghi chú cuối: Đây KHÔNG PHẢI là khuyến nghị đầu tư. Toàn bộ đánh giá dựa trên tin tức công khai tìm được tại thời điểm 2026-09-24; các mục ghi "chưa kiểm chứng" cần được xác minh thêm trước khi dùng để ra quyết định.*



---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

### 🐂 Agent C — Tổng hợp hướng BÒ · 2026-09-24 13:00

*Lưu ý trước: mô hình quant có edge YẾU (AUC ~0.53–0.55) — mọi score/xếp hạng bên dưới là xác suất mờ, không phải tín hiệu chắc chắn. Luận điểm bò dưới đây cố tình đứng vững nhờ **catalyst + kỹ thuật thật**, không dựa vào score model.*

Chọn 3 mã có cơ hội bò tốt nhất trong nhóm 5 mã đã tranh luận: **GAS, GVR, VIC**.

---

#### 1. GAS (PV GAS) — kèo có nền tảng cơ bản rõ ràng nhất

**Luận điểm mua:** Theo Agent A, GAS đang ↑ trên MA50, RSI 51.2 trung tính (còn dư địa), điểm kỹ thuật 6/10 — xu hướng tăng vẫn nguyên vẹn dù đang pullback. Theo Agent B, đây là mã có nền tảng tin tức **mạnh nhất nhóm**: lợi nhuận 8 tháng đầu 2026 hơn 14.500 tỷ đồng, **vượt kế hoạch cả năm 29-30%**, doanh thu lập đỉnh mới — đây là con số thật, có nguồn (Tin nhanh chứng khoán, MekongASEAN). Thêm vào đó, cổ tức tiền mặt 25% (2.500đ/CP) đã công bố ngày thanh toán dự kiến 20/11/2026 — dòng tiền cổ tức lớn (~6.032 tỷ đồng) là bằng chứng sức khỏe tài chính tốt.

**Catalyst:** (1) KQKD vượt kế hoạch — Agent B xác nhận có nguồn. (2) Cổ tức tiền mặt 25% sắp chi trả. (3) Agent B ghi nhận GAS thuộc nhóm vốn hóa lớn dễ hưởng lợi dòng vốn ngoại từ sự kiện **FTSE Russell nâng hạng TTCK Việt Nam lên Secondary Emerging Market (hiệu lực 21/9/2026)** — đây là catalyst vĩ mô tích cực mạnh cho toàn thị trường, và GAS được B xếp vào nhóm hưởng lợi nhiều hơn nhờ vốn hóa lớn.

**Kịch bản giá tới TP:** Entry 84.200đ → TP +8% = 90.936đ. Theo Agent A, vùng TP này "nằm sát đỉnh cũ gần nhất" (~93k) — nghĩa là chỉ cần giá hồi lại gần đỉnh gần nhất (chưa cần phá đỉnh) là chạm TP, một kịch bản kỹ thuật hợp lý trong xu hướng tăng còn nguyên.

**Rủi ro & vì sao chịu được:** Agent A lưu ý vol_ratio 0.34 (yếu) — pullback hiện tại thiếu xác nhận khối lượng. Nhưng SL 79.990đ được đặt ngay sát MA50 — nếu xu hướng tăng thật sự gãy, lệnh cắt lỗ sẽ kích hoạt sớm với mức lỗ giới hạn ~5%, còn time-stop 25 ngày giới hạn thời gian chờ. Rủi ro tin "vướng tiêu chuẩn công ty đại chúng" mà Agent B nêu là **chưa kiểm chứng nội dung** — không nên coi là yếu tố phủ định catalyst KQKD/cổ tức đã có nguồn xác thực.

---

#### 2. GVR (Tập đoàn Cao su VN) — kèo kỹ thuật đẹp nhất, có xác nhận dòng tiền thật

**Luận điểm mua:** Theo Agent A, GVR là mã **duy nhất trong nhóm 5 mã có vol_ratio > 1 (1.44)** — nghĩa là khối lượng mua vào entry cao hơn trung bình, xác nhận lực cầu thật sự đứng sau đà hồi phục, chứ không phải hồi giá suông. MA50 "vừa tạo đáy và đang ngóc lên sau downtrend" — dấu hiệu đảo chiều kỹ thuật rõ nhất nhóm, điểm kỹ thuật cao nhất (7/10). RSI 61.2 mới ngả hưng phấn, chưa quá mua — còn dư địa tăng trước khi vào vùng rủi ro đảo chiều.

**Catalyst:** Theo Agent B, động lực 2026 của GVR đến từ giá cao su tăng mạnh, thanh lý gỗ cao su, và thu nhập bồi thường đất chuyển đổi sang đất khu công nghiệp (mảng KCN dự kiến doanh thu +6%) — đây là câu chuyện lợi nhuận thật dù B tự lưu ý "nguồn không ghi rõ ngày công bố, cần kiểm chứng tính thời sự".

**Kịch bản giá tới TP:** Entry 33.000đ → TP +8% = 35.640đ. Theo Agent A, vùng này khớp đúng vùng cản cũ 34.500–36.000đ (đỉnh đi ngang T5–T6) — hợp lý về cấu trúc giá, dù A cũng lưu ý "không dễ vượt ngay", tức đây là mục tiêu thực tế chứ không viển vông.

**Rủi ro & vì sao chịu được:** Agent B có ghi nhận "dấu hiệu phân phối từ tổ chức" vào 20,23,24/8 và 16/9 — nhưng chính B tự đánh giá đây là **"chưa kiểm chứng nguồn gốc số liệu"**. Ngược lại, bằng chứng vol_ratio 1.44 từ Agent A là số liệu thật lấy trực tiếp từ signals_latest.csv, mạnh hơn về độ tin cậy so với tin đồn phân phối chưa kiểm chứng. SL 31.350đ (dưới đáy vừa tạo) + time-stop 25 ngày giới hạn rủi ro nếu kịch bản đảo chiều không thành.

---

#### 3. VIC (Vingroup) — kèo hưởng lợi trực tiếp từ câu chuyện vĩ mô lớn nhất năm

**Luận điểm mua:** Theo Agent A, VIC ↑ trên MA50, RSI 47.5 trung tính, điểm kỹ thuật 5.5/10 — đang trong nhịp pullback của một xu hướng tăng. Theo Agent B, VIC thuộc nhóm vốn hóa lớn được xếp vào diện **hưởng lợi trực tiếp** từ sự kiện FTSE Russell nâng hạng TTCK Việt Nam lên Secondary Emerging Market (hiệu lực 21/9/2026, lộ trình phân bổ 4 giai đoạn tới 9/2027) — đây là catalyst vĩ mô có nguồn xác thực (VnEconomy, Báo Chính phủ, SGGP), không phải suy đoán. Bằng chứng giá đã phản ánh phần nào: theo B, VIC tăng khoảng 11,4% trong tháng 9/2026 (tính đến ~21/9) — đây là dữ liệu giá thật, cho thấy dòng tiền đã bắt đầu vào trước khi hiệu lực nâng hạng chính thức.

**Catalyst:** Nâng hạng thị trường (FTSE) — dòng vốn ngoại thụ động dự kiến đổ vào nhóm vốn hóa lớn như VIC theo lộ trình đã công bố chính thức.

**Kịch bản giá tới TP:** Entry 230.500đ → TP +8% = 248.940đ. Theo Agent A, vùng này "đúng vùng đỉnh gần nhất" (~265k là đỉnh trước đó, TP nằm giữa đường pullback và đỉnh cũ) — hợp lý nếu dòng vốn ngoại từ câu chuyện nâng hạng tiếp tục vào.

**Rủi ro & vì sao chịu được:** Agent A lưu ý vol_ratio 0.23 (yếu nhất nhóm) trong nhịp pullback — chưa rõ là nghỉ ngơi hay đảo chiều. Agent B cũng nêu miễn nhiệm một Phó Tổng Giám đốc sau 14 năm gắn bó, nhưng chính B đánh giá đây là thay đổi nhân sự **"không có dấu hiệu liên quan sai phạm/pháp lý"**, lý do công bố là "cá nhân" — mức độ nghiêm trọng thấp hơn nhiều so với một catalyst vĩ mô tích cực mạnh (nâng hạng) đang tác động lên toàn nhóm vốn hóa lớn. SL 218.975đ dưới MA50 + time-stop 25 ngày bảo vệ nếu nhịp pullback biến thành đảo chiều thật.

---

### Phản biện trước (chuẩn bị cho Agent D — gấu)

- **"Volume yếu ở entry (GAS, VIC) là dấu hiệu xấu"** → Đúng là vol_ratio dưới 1, nhưng đây là đặc điểm chung của *toàn bộ nhóm ứng viên top-5* trừ GVR (Agent A ghi nhận). Volume yếu trong một nhịp pullback của xu hướng tăng không tự động nghĩa là đảo chiều — SL + time-stop 25 ngày đã được thiết kế để giới hạn thiệt hại nếu giả thuyết sai.
- **"GVR có tín hiệu phân phối tổ chức"** → Chính Agent B tự gắn nhãn tin này là "chưa kiểm chứng nguồn gốc số liệu". Bằng chứng vol_ratio 1.44 (số liệu thật từ signals_latest.csv) về mặt độ tin cậy mạnh hơn một tin đồn chưa xác thực.
- **"KDH, PNJ có TP/SL tương tự nhưng nền tảng xấu hơn nhiều"** → Đúng, và vì vậy 2 mã này **không** được chọn vào danh sách bò ở đây — chọn lọc dựa trên cả kỹ thuật lẫn catalyst thật, không chọn đại trà theo score.
- **"Score model cho GAS/GVR/VIC không phải cao nhất tuyệt đối và AUC chỉ ~0.53-0.55"** → Thừa nhận đúng: đây là lý do luận điểm bò ở đây dựa vào catalyst tin tức có nguồn thật (KQKD, cổ tức, nâng hạng thị trường) và bằng chứng khối lượng thật (GVR), chứ không dựa vào con số score đơn thuần.

### Kèo bò tự tin nhất

Nếu phải chọn một: **GAS** — vì đây là mã duy nhất trong nhóm có *đồng thời* KQKD vượt kế hoạch đã xác nhận nguồn, cổ tức tiền mặt lớn đã công bố lịch chi trả, xu hướng kỹ thuật tăng còn nguyên trên MA50, và nằm trong nhóm hưởng lợi câu chuyện nâng hạng thị trường — dù volume entry yếu, TP/SL/time-stop đã có cấu trúc bảo vệ hợp lý.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**


---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

### 🐻 Agent D — Tổng hợp hướng GẤU + phản biện · 2026-09-24 14:30

*Lưu ý: mô hình quant có edge YẾU (AUC ~0.53–0.55) — gần như ngang xu (0.5). Score chỉ là xác suất mờ, cả luận điểm bò lẫn gấu dưới đây đều đứng trên nền một mô hình gần như không tách biệt được tín hiệu khỏi nhiễu. Bất kỳ ai — kể cả Agent C — tự tin quá mức vào bộ 5 mã này đều đang đánh giá thấp rủi ro nền.*

---

## Phản biện Agent C (từng luận điểm)

### 1. GAS — "kèo có nền tảng cơ bản rõ ràng nhất"

- **Agent C cho rằng** KQKD vượt kế hoạch 29-30% + cổ tức 25% là bằng chứng sức khỏe tài chính tốt, **nhưng** chính Agent B đã chỉ rõ: ngày GDKHQ cổ tức **đã qua (22/9/2026)**, tức thị trường **đã định giá xong** phần cổ tức này vào giá tham chiếu trước ngày phân tích (24/9). Đây không phải catalyst tương lai — nó là tin cũ đã phản ánh vào giá. KQKD 8 tháng cũng vậy: là tin quá khứ (đã công bố), không phải sự kiện sắp xảy ra có thể đẩy giá tiếp trong 25 ngày time-stop.
- **Agent C cho rằng** rủi ro "vướng tiêu chuẩn công ty đại chúng" không nên phủ định catalyst đã xác thực, **nhưng** đây là ngụy biện chọn lọc: một tiêu đề báo chí nêu đích danh GAS "vướng tiêu chuẩn công ty đại chúng" ngay **giữa lúc chi trả hơn 6.000 tỷ cổ tức** là tín hiệu bất thường đáng ngờ (tại sao báo lại đặt cạnh nhau hai sự kiện này?) — Agent B tự nhận "chưa kiểm chứng nội dung", nghĩa là chúng ta **không biết mức độ nghiêm trọng**, có thể là vấn đề tuân thủ tỷ lệ cổ đông đại chúng ảnh hưởng đến thanh khoản/niêm yết. Bỏ qua một rủi ro chưa rõ ràng chỉ vì nó "chưa kiểm chứng" cũng nguy hiểm như tin vào một catalyst khi chưa kiểm chứng đầy đủ.
- **Agent C thừa nhận** vol_ratio 0.34 là yếu nhưng biện minh bằng SL sát MA50. Về mặt kỹ thuật thuần túy theo Agent A: đây là entry **không có xác nhận dòng tiền** — nếu pullback là khởi đầu của một downtrend chứ không phải nghỉ ngơi, ta sẽ vào lệnh đúng lúc mô hình đang bẫy false positive (AUC 0.55 nghĩa là gần 45% khả năng tín hiệu này là nhiễu).
- **Kịch bản downside GAS:** TP 90.936đ nằm sát đỉnh cũ ~93k — nghĩa là để đạt TP, giá phải gần như retest đỉnh, một ngưỡng khó nếu không có catalyst mới thực sự (mà catalyst hiện có đã "cũ"). Nếu tin "vướng tiêu chuẩn công ty đại chúng" xấu hơn dự kiến, hoặc dòng vốn ngoại FTSE chậm giải ngân theo lộ trình 4 giai đoạn (giai đoạn đầu chỉ 10%, không phải dòng tiền lớn ngay lập tức), giá có thể trôi về SL 79.990đ (khoảng −5% từ entry).

### 2. GVR — "kèo kỹ thuật đẹp nhất, có xác nhận dòng tiền thật"

- **Agent C cho rằng** vol_ratio 1.44 là "số liệu thật từ signals_latest.csv" nên đáng tin hơn tin đồn phân phối tổ chức, **nhưng** đây là ngộ nhận về bản chất dữ liệu: vol_ratio là **con số thống kê mô tả** (khối lượng hôm nay so với trung bình), nó không phân biệt được khối lượng đó đến từ **lực mua tổ chức thật** hay chính là khối lượng phân phối/bán ra mà Agent B ghi nhận (tin phân phối xảy ra các ngày 20, 23, 24/8 và 16/9 — tức là các phiên khối lượng cao trước đó). Nói cách khác, vol_ratio cao **không loại trừ** khả năng đó là khối lượng bán ra (phân phối), nó chỉ nói "có giao dịch nhiều hơn bình thường" — chiều nào (mua ròng hay bán ròng) thì signals_latest.csv không thể hiện. Agent C đã quy đổi một chỉ số trung tính thành "bằng chứng lực mua" một cách vội vàng.
- **Agent C dẫn** MA50 "vừa tạo đáy và đang ngóc lên" như tín hiệu đảo chiều tích cực, **nhưng** chính Agent A ghi rõ đây là hồi phục "sau downtrend 05→07" — nghĩa là GVR vẫn đang trong xu hướng giảm dài hạn (giá đã rơi từ đỉnh lịch sử 46.500đ về 31.000-33.000đ, theo Agent B — mất khoảng 30%). Một MA50 "ngóc lên" sau một downtrend sâu chưa đủ để khẳng định đảo chiều — đây vẫn có thể là một đợt hồi kỹ thuật (dead-cat bounce) trong xu hướng giảm lớn hơn.
- **Agent B tự thừa nhận** không tìm được lý do cụ thể cho việc GVR giảm từ đỉnh 46.500đ — Agent C bỏ qua chi tiết này. Nếu thị trường bán GVR mạnh suốt từ tháng 3 vì lý do cơ bản nào đó (giá cao su đảo chiều? định giá lại KCN?) mà chúng ta chưa biết, thì một tuần hồi giá không đủ để đảo ngược nguyên nhân gốc.
- **Kịch bản downside GVR:** đây là mã điểm KT cao nhất nhưng **điểm score model thấp nhất trong 3 mã bò của C (0.467)** — thấp hơn cả KDH (0.4825) và PNJ (0.5359) theo signals_latest.csv. Nếu tín hiệu phân phối tổ chức (dù chưa kiểm chứng) là thật, GVR có thể quay đầu giảm nhanh về SL 31.350đ khi lực bán từ nhà đầu tư tổ chức lớn hơn lực mua cá nhân đang đẩy giá hồi.

### 3. VIC — "kèo hưởng lợi trực tiếp từ câu chuyện vĩ mô lớn nhất năm"

- **Agent C cho rằng** giá tăng 11,4% trong tháng 9 là "dòng tiền đã bắt đầu vào trước khi hiệu lực nâng hạng chính thức", **nhưng** đây có thể đọc theo hướng ngược lại: nếu tin nâng hạng FTSE (công bố chính thức, hiệu lực 21/9) đã được thị trường "front-run" và giá đã chạy trước +11,4%, thì phần lớn "juice" của catalyst **đã được ăn hết trước khi Agent E ra quyết định** ở entry 230.500đ (vốn đã pullback từ đỉnh 265k). Mua sau khi tin đã lan rộng và giá đã tăng mạnh là rủi ro kinh điển "buy the rumor, và tin đã ra" — phần còn lại của game chỉ còn hy vọng vào lộ trình giải ngân ETF, mà giai đoạn đầu chỉ chiếm 10% tổng phân bổ (theo B), tức dòng vốn thực tế đổ vào ngắn hạn có thể rất nhỏ giọt, không đủ sức đẩy giá thêm 8%.
- **Agent C giảm nhẹ** việc miễn nhiệm Phó Tổng Giám đốc 14 năm bằng lý do "cá nhân, không sai phạm", **nhưng** Agent B tự đặt câu hỏi "cần kiểm chứng thêm động cơ thực sự" — một nhân sự cấp cao rời đi đột ngột sau gần 14 năm gắn bó, đúng lúc công bố "lý do cá nhân", là mô-tip thường xuất hiện trước khi có thông tin xấu hơn lộ diện (dù chỉ là khả năng, chưa kiểm chứng). Kết hợp với vol_ratio 0.23 — **yếu nhất trong toàn bộ nhóm 5 mã** — nghĩa là không có dòng tiền xác nhận nào đứng sau đợt pullback, cả từ phía mua lẫn thanh khoản chung.
- **Kịch bản downside VIC:** đây là mã có TP xa nhất về giá trị tuyệt đối (248.940đ, cách entry +18.440đ) nhưng động lực chính (nâng hạng) là tin đã biết trước, effect có thể đã "sell the news" khi dòng vốn thực chưa về kịp (lộ trình kéo dài tới 9/2027). Nếu thị trường chung điều chỉnh, VIC vốn hóa lớn thường bị rút vốn đầu tiên khi khối ngoại chốt lời ngắn hạn — rủi ro trôi về SL 218.975đ hoàn toàn hiện thực.

### Phản biện điểm chung của C: "SL + time-stop 25 ngày đã bảo vệ đủ rủi ro"

- Đây là lập luận **đúng nhưng không đủ**: SL −5% giới hạn lỗ mỗi lệnh, nhưng không giải quyết vấn đề **xác suất thắng**. Với AUC 0.53–0.55, tỷ lệ tín hiệu đúng chỉ nhỉnh hơn tung đồng xu một chút. Nếu cả 3 mã bò của C đều dựa trên setup có vol_ratio dưới 1 (GAS 0.34, VIC 0.23 — chỉ GVR trên 1), tức 2/3 kèo bò thiếu xác nhận dòng tiền vào đúng lúc mua — SL bảo vệ vốn nhưng không bảo vệ **kỳ vọng lợi nhuận**, vì nếu tỷ lệ thắng thực tế gần 50%, risk/reward 8%/5% (R:R ~1.6) chỉ hòa vốn hoặc lãi mỏng sau chi phí giao dịch, chưa kể trượt giá.

---

## Rủi ro downside theo mã (tới SL hoặc xa hơn)

| Mã | Rủi ro downside cụ thể | Ghi chú |
|---|---|---|
| **GAS** | Catalyst (KQKD, cổ tức) đã phản ánh vào giá; tin "vướng tiêu chuẩn công ty đại chúng" chưa kiểm chứng có thể xấu hơn dự kiến; vol_ratio 0.34 không xác nhận lực mua ở entry | Nếu tin xấu lộ diện, giá có thể xuyên SL 79.990đ nhanh vì thiếu lực đỡ khối lượng |
| **GVR** | Tín hiệu phân phối tổ chức (dù chưa kiểm chứng) trùng thời điểm với vol_ratio cao — không loại trừ khả năng chính vol_ratio 1.44 là khối lượng bán; vẫn trong downtrend dài hạn từ đỉnh 46.500đ (-30%), điểm score model thấp nhất nhóm bò (0.467) | Rủi ro "dead-cat bounce" trong xu hướng giảm lớn hơn chưa rõ nguyên nhân gốc |
| **VIC** | Catalyst nâng hạng có thể đã bị "ăn" vào giá (+11,4% trong tháng); vol_ratio 0.23 yếu nhất nhóm 5 mã — không có xác nhận dòng tiền; thay đổi nhân sự cấp cao chưa rõ động cơ thực; lộ trình giải ngân ETF chỉ 10% giai đoạn đầu | Rủi ro "sell the news" khi dòng vốn thực chưa kịp về |
| **PNJ** (không thuộc danh sách bò của C nhưng đáng lưu ý rủi ro hệ thống) | Downtrend dài dưới MA50, RSI 33.7 gần quá bán nhưng chưa xác nhận đáy — mua ở đây là "bắt dao rơi nhẹ" theo Agent A; thêm rủi ro thương hiệu "biến cố kim cương" chưa kiểm chứng mức độ hiện tại | Agent C đã loại mã này khỏi danh sách bò — hợp lý |
| **KDH** (loại khỏi bò, nhưng để đối chiếu rủi ro hệ thống ngành BĐS) | Nợ vay/vốn chủ 83%, tồn kho ~29.500 tỷ, vướng văn bản UBCKNN chưa rõ mức độ — rủi ro thanh khoản BĐS rõ rệt nhất nhóm; downtrend dưới cả MA20/MA50 chưa có xác nhận đảo chiều | Xác nhận nhận định của cả A và B: đây là setup "bắt dao rơi" nguy hiểm nhất |

**Rủi ro hệ thống chung cần cân nhắc (giả định — chưa kiểm chứng cụ thể trong whiteboard):**
- Toàn bộ nhóm cổ phiếu vốn hóa lớn (VIC, GAS) đang neo theo một câu chuyện vĩ mô (nâng hạng FTSE) — nếu dòng vốn ngoại thực tế giải ngân chậm hơn kỳ vọng thị trường trong giai đoạn đầu (10%), có thể xảy ra điều chỉnh thất vọng ("sell on fact") trên diện rộng, kéo theo cả nhóm large-cap.
- Biên độ giao dịch ±7% (HOSE) và cơ chế T+2 có thể khiến nhà đầu tư kẹp hàng nếu giá giảm sàn liên tiếp — rủi ro này áp dụng chung cho mọi mã, không riêng nhóm C chọn.
- Ngành BĐS (VIC, KDH) đang phân hóa mạnh theo Agent B — nếu tâm lý thị trường quay sang thận trọng với BĐS nói chung (vì rủi ro nợ vay như KDH), VIC dù vốn hóa lớn cũng khó tránh hoàn toàn hiệu ứng lây (giả định, chưa kiểm chứng mức độ tương quan thực tế giữa VIC và KDH).

---

## Mã nên tránh

1. **KDH** — rủi ro rõ rệt nhất theo cả A (kỹ thuật) và B (cơ bản): downtrend chưa xác nhận đáy, nợ vay/tồn kho tăng vọt, vướng UBCKNN chưa rõ hậu quả. Đây là "bắt dao rơi" điển hình.
2. **PNJ** — tương tự KDH ở mặt kỹ thuật (dưới MA50, chưa xác nhận đảo chiều), thêm rủi ro thương hiệu và lợi nhuận quý 2 âm chưa được giải thích đầy đủ.
3. **VIC** (trong nhóm C chọn, mã rủi ro nhất) — vol_ratio thấp nhất nhóm 5 mã (0.23), catalyst có khả năng đã phản ánh vào giá, nhân sự cấp cao rời đi chưa rõ lý do thực.

---

## Nhắc lại edge mô hình

AUC ~0.53–0.55 nghĩa là mô hình chỉ nhỉnh hơn phỏng đoán ngẫu nhiên một chút. Toàn bộ xếp hạng bull/bear ở đây — kể cả của tôi — đều xây trên một tập tín hiệu kỹ thuật + tin tức có chất lượng tốt hơn score model, nhưng **không có gì đảm bảo chắc chắn**. Agent E nên coi cả luận điểm bò và gấu này là hai kịch bản xác suất, không phải dự báo chắc chắn, và ưu tiên kỷ luật SL/time-stop hơn là niềm tin vào bất kỳ câu chuyện nào ở trên.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**


---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*

### 🎩 Agent E — Giám đốc Chiến lược · 2026-09-24 15:30

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| **GAS** | THEO DÕI | TB | Catalyst KQKD/cổ tức có nguồn nhưng đã cũ (D: đã phản ánh vào giá), volume entry yếu — bò/gấu cân bằng. |
| **GVR** | THEO DÕI | TB | Kỹ thuật đẹp nhất nhóm nhưng D lật lại vol_ratio không phân biệt mua/bán, vẫn trong downtrend dài hạn -30%. |
| **VIC** | THEO DÕI | Thấp | Catalyst nâng hạng FTSE thật nhưng có thể đã "ăn" vào giá (+11,4%/tháng), vol_ratio yếu nhất nhóm 5 mã. |
| **PNJ** | TRÁNH | Cao | Downtrend dưới MA20/MA50 chưa đảo chiều, LNST quý 2 âm, rủi ro thương hiệu chưa kiểm chứng — không nằm trong danh sách bò. |
| **KDH** | TRÁNH | Cao | Rủi ro rõ nhất nhóm: downtrend sâu, nợ vay/vốn chủ 83%, tồn kho lớn, vướng UBCKNN chưa rõ hậu quả — cả A/B/D đồng thuận tránh. |

**Stance danh mục:** Thận trọng. Không mã nào đạt ngưỡng MUA — cả 3 mã bò tốt nhất bị phản biện đủ mạnh để hạ xuống THEO DÕI, tôn trọng edge mô hình yếu (AUC ~0.53–0.55) và ưu tiên bảo toàn vốn. Chi tiết đầy đủ tại [`DECISION.md`](../DECISION.md).

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**

