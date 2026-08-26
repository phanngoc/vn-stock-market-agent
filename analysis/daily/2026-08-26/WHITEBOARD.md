# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-08-26)

*Board tạo lúc 2026-08-26 07:13:56. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.352** · buy&hold kỳ kiểm định **0.302**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): KDH, PNJ, PDR, VIC, VRE
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **KDH** | RealEstate | 18,200 | 0.59 | 19,656 | 17,290 | 49 | ↓ dưới MA50 |
| 2 | **PNJ** | Retail/Consumer | 42,500 | 0.58 | 45,900 | 40,375 | 59 | ↓ dưới MA50 |
| 3 | **PDR** | RealEstate | 12,550 | 0.57 | 13,554 | 11,922 | 52 | ↓ dưới MA50 |
| 4 | **VIC** | RealEstate | 223,000 | 0.56 | 240,840 | 211,850 | 61 | ↑ trên MA50 |
| 5 | **VRE** | RealEstate | 25,250 | 0.55 | 27,270 | 23,987 | 52 | ↓ dưới MA50 |

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

### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-08-26 07:20

| Mã | Trend (vs MA20/MA50) | RSI(14) | Vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **VIC** | ↑ trên MA20 & MA50, đang breakout khỏi vùng đi ngang 200–230k (4 tháng) | 61.1 (trung tính, gần vùng mua nhiều) | 0.55 | **7/10** | Setup sạch nhất: xu hướng chính là tăng, giá vừa vượt kháng cự ngắn hạn ~220k; nhưng khối lượng bùng nổ vẫn <1 (chưa xác nhận mạnh) |
| **PDR** | ↓ dưới MA50 nhưng MA50 đang đi ngang/phẳng dần; giá đang tạo đáy quanh 11.8–13k | 52.3 (trung tính) | 0.17 | **5/10** | SL (11,922) sát đáy gần nhất (~11.8–12k) → hợp lý về R:R; nhưng vol_ratio rất thấp — bật giá gần đây thiếu xác nhận khối lượng |
| **VRE** | ↓ dưới MA50, đang trong downtrend từ đỉnh tháng 4 (~36k); MA50 bắt đầu đi ngang | 52.5 (trung tính) | 0.23 | **4/10** | Đang hồi trong xu hướng giảm dài hơn, chưa có tín hiệu đảo chiều rõ; khối lượng èo uột |
| **PNJ** | ↓ dưới MA50; downtrend dốc mạnh Feb→Jul (80k→~30k), rồi bật mạnh gần đây lên 42.5k | 59.1 (trung tính, thiên hồi phục) | 0.41 | **4/10** | Bật giá rất mạnh (~+40% từ đáy) nhưng vẫn dưới MA50 đang giảm dốc — rủi ro "dead-cat bounce" cao, khối lượng xác nhận yếu |
| **KDH** | ↓ dưới cả MA20 & MA50, downtrend liên tục từ 28k (Feb) → 17.3k đáy gần nhất | 49.1 (trung tính) | 0.36 | **3/10** | ⚠️ Setup giống "bắt dao rơi": mới bật 2 phiên từ đáy, MA50 vẫn dốc xuống rõ, chưa có xác nhận đảo chiều; khối lượng thấp |

**Xếp hạng kỹ thuật (cao → thấp):** VIC (7) > PDR (5) > PNJ ≈ VRE (4) > KDH (3)

- Setup kỹ thuật đẹp nhất về mặt kỹ thuật thuần túy: **VIC** — mã duy nhất trong top-5 nằm trên cả MA20/MA50, đang breakout khỏi vùng tích lũy dài; nhưng RSI 61 đã gần vùng nhạy cảm và khối lượng xác nhận vẫn dưới trung bình (0.55).
- Rủi ro kỹ thuật lớn nhất: **KDH** — toàn bộ 4 mã còn lại (KDH, PNJ, PDR, VRE) đều đang ở dưới MA50 trong xu hướng giảm trung hạn; KDH là trường hợp rõ nhất của việc mua khi giá vẫn đang giảm mạnh ("bắt dao rơi"), độ tin cậy của cú bật hiện tại chưa được khối lượng xác nhận.
- Điểm chung đáng chú ý: **cả 5/5 mã đều có vol_ratio < 1** (khối lượng dưới trung bình) — không mã nào có xác nhận dòng tiền mạnh cho tín hiệu mua tại thời điểm này; đây là điểm yếu kỹ thuật xuyên suốt toàn bộ danh sách.
- TP +8%/SL −5% nhìn chung khớp tương đối với biên độ dao động gần đây của các mã (đặc biệt PDR, KDH có SL gần vùng đáy kỹ thuật gần nhất), nhưng đây là quy tắc cố định của hệ thống, không phải được suy ra riêng từ từng biểu đồ — mức hỗ trợ/kháng cự chính xác hơn (theo phiên/theo tuần) **chưa kiểm chứng** do chỉ có ảnh biểu đồ tổng quan.
- Không mã nào trong top-5 đang ở vùng quá mua (RSI>70) hay quá bán (RSI<30) — RSI toàn bộ nằm ở vùng trung tính, không cho tín hiệu động lượng mạnh theo hướng nào.
- Nhắc lại: mô hình có edge yếu (AUC ~0.53–0.55), các điểm số kỹ thuật ở trên là đánh giá xác suất, không phải chắc chắn.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**

### 🅱️ Agent B — Phân tích News / Cơ bản · 2026-08-26 07:30

*Lưu ý: đây KHÔNG PHẢI khuyến nghị đầu tư — chỉ tổng hợp tin tức/catalyst độc lập với biểu đồ kỹ thuật. Mô hình quant nền có edge YẾU (AUC ~0.53–0.55), tin tức dưới đây chỉ bổ sung góc nhìn, không thay quản trị rủi ro.*

---

## KDH — Nhà Khang Điền (RealEstate)

- **KQKD 2025 vượt kế hoạch**: lợi nhuận 2025 đạt hơn 1.633 tỷ đồng, vượt 63% kế hoạch; công ty đặt mục tiêu lãi 1.500 tỷ đồng (một số nguồn nêu >2.000 tỷ, tăng gấp đôi) cho 2026 → **tích cực**, nhưng con số mục tiêu 2026 giữa các nguồn không khớp nhau, cần kiểm chứng thêm. ([Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/khang-dien-kdh-loi-nhuan-2025-vuot-63-ke-hoach-dat-hon-1633-ty-dong-mo-rong-tang-truong-trong-2026-post384618.html), [Báo Đầu tư](https://baodautu.vn/nha-khang-dien-len-ke-hoach-lai-1500-ty-dong-trong-nam-2026-d558641.html))
- **Sạch nợ trái phiếu, không phát hành vốn mới trong 2026** → giảm rủi ro pha loãng/nợ vay, **tích cực** cho tâm lý nhà đầu tư. ([Doanh nhân Pháp luật](https://doanhnhan.baophapluat.vn/dhdcd-khang-dien-kdh-2026-sach-no-trai-phieu-noi-khong-voi-phat-hanh-von-moi-va-muc-tieu-lai-1-500-ty-dong.html))
- **Triển khai đồng loạt 4 dự án tại TP.HCM** (>150ha, ~6.000 căn hộ + hơn 1.000 nhà thấp tầng + ~60ha đất công nghiệp) trong 2026-2027, vừa khởi công phần cao tầng dự án Gladia by the Waters (>600 căn, bàn giao dự kiến Q4/2027) → **tích cực** dài hạn nhưng chưa phải catalyst ngắn hạn cho khung swing 5 tuần. ([Doanh nhân Pháp luật](https://doanhnhan.baophapluat.vn/dhdcd-khang-dien-kdh-2026-sach-no-trai-phieu-noi-khong-voi-phat-hanh-von-moi-va-muc-tieu-lai-1-500-ty-dong.html))
- Cổ tức 2026 dự kiến giữ mức 10% — **trung tính**. Ngày chốt quyền ĐHĐCĐ 2026 đã qua (đầu năm), không phải catalyst hiện tại.

## PNJ — Vàng bạc Đá quý Phú Nhuận (Retail/Consumer)

- **6 tháng đầu 2026**: doanh thu 25.729 tỷ đồng (+49,4% YoY), lãi sau thuế 1.256 tỷ đồng (+6,3% YoY) → tăng trưởng doanh thu mạnh nhưng lợi nhuận tăng chậm hơn nhiều → **hỗn hợp/trung tính**. ([Thương hiệu Công luận](https://thuonghieucongluan.com.vn/pnj-dat-doanh-thu-25-729-ty-dong-trong-6-thang-dau-nam-2026-a328728.html))
- **Q2/2026 lỗ 283 tỷ đồng** dù doanh thu +12% YoY, do trích lập dự phòng theo nguyên tắc thận trọng (liên quan biến động giá vàng) → **tiêu cực**, cần xem chi tiết vì đây là khoản mục bất thường lớn so với lãi Q1. ([Baomoi/Thương Gia](https://baomoi.com/pnj-duy-tri-da-tang-truong-trong-nua-dau-nam-2026-c55730106.epi))
- **Q1/2026**: doanh thu 17.245 tỷ (+79% YoY), lãi sau thuế 1.467 tỷ (+116,5% YoY) → quý đầu rất mạnh, tương phản với quý 2 lỗ → **hỗn hợp**. ([Công luận](https://congluan.vn/doanh-thu-quy-1-2026-pnj-dat-17-245-ty-dong-10338985.html))
- Mục tiêu cả năm 2026: lãi sau thuế 3.409 tỷ (kỷ lục, +21% YoY), doanh thu 48.660 tỷ (+37%) — bán lẻ trang sức 6 tháng +13,6% YoY nhờ khách mới/cũ và omni-channel → **tích cực** về triển vọng dài hạn nhưng khoản lỗ Q2 là rủi ro cần theo dõi báo cáo tài chính chi tiết (chưa kiểm chứng nguyên nhân cụ thể). ([Vietstock](https://vietstock.vn/2026/04/pnj-dat-muc-tieu-loi-nhuan-lap-dinh-moi-737-1421473.htm))

## PDR — Bất động sản Phát Đạt (RealEstate)

- **Chủ tịch Nguyễn Văn Đạt đăng ký mua 20 triệu cổ phiếu** trong giai đoạn 31/7–29/8/2026 khi giá "thấp nhất 3 năm" → **tích cực** mạnh, tín hiệu lãnh đạo tin tưởng và đúng cửa sổ giao dịch hiện tại (vẫn đang trong giai đoạn mua, sát as-of date 26/8/2026) — đáng chú ý là **catalyst gần nhất** cho mã này. ([Vietstock](https://vietstock.vn/2026/07/pdr-chu-tich-nguyen-van-dat-muon-mua-20-trieu-cp-khi-gia-thap-nhat-3-nam-739-1472096.htm))
- **Kế hoạch phát hành ~200 triệu cổ phiếu** cho cổ đông hiện hữu (tỷ lệ 5:1, giá 15.780đ/cp), huy động gần 2.000 tỷ đồng → **tiêu cực** (rủi ro pha loãng đáng kể, ~20% số cổ phiếu lưu hành hiện tại), cần theo dõi ngày GDKHQ chưa công bố cụ thể. ([Doanh nhân Pháp luật](https://doanhnhan.baophapluat.vn/phat-dat-pdr-du-kien-phat-hanh-gan-200-trieu-co-phieu-don-luc-cho-du-an-da-nang-va-tp-hcm.html), [Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/phat-dat-pdr-muon-huy-dong-gan-2000-ty-dong-tu-chao-ban-cho-co-dong-hien-huu-post387998.html))
- **Phát hành trái phiếu thành công 5.600 tỷ đồng** (26/3/2026) → tăng đòn bẩy, **trung tính/tiêu cực nhẹ** tùy mục đích sử dụng vốn.
- Kế hoạch 2026: thu ~1.900 tỷ từ chuyển nhượng dự án, tập trung TP.HCM và Đồng Nai, không mở rộng tỉnh mới; phân bổ ~1.550 tỷ cho dự án Đà Nẵng Centre Point (gồm 921 tỷ mua lại cổ phần dự kiến Q2/2026, 629 tỷ góp vốn xây dựng Q3/2026) → **trung tính**, chiến lược thận trọng hơn. ([Vietstock](https://vietstock.vn/2026/01/phat-dat-du-kien-nam-2026-thu-19-ngan-ty-tu-chuyen-nhuong-du-an-tap-trung-dau-tu-o-tphcm-va-dong-nai-737-1397290.htm))
- Đang lấy ý kiến cổ đông về thương vụ mua vốn góp tại Lotte Properties HCMC (chưa rõ chi tiết/kết quả) — **chưa kiểm chứng**, cần theo dõi thêm.

## VIC — Vingroup (RealEstate)

- **Vinpearl thoái ~5,2 triệu cổ phiếu VIC** (16/4/2026), giảm sở hữu từ ~90 triệu xuống ~85 triệu cp (từ 1,16% xuống ~1,1% vốn điều lệ), thu về ước ~984 tỷ đồng → **trung tính/tiêu cực nhẹ** (giao dịch nội bộ nhóm, quy mô nhỏ so với vốn hóa VIC, nhưng là dạng thoái vốn cần lưu ý). ([DNSE](https://www.dnse.com.vn/senses/tin-tuc/vinpearl-thoai-hon-5-trieu-co-phieu-tai-vingroup-35217602))
- **VinFast dự kiến thoái vốn mảng sản xuất** tại Việt Nam, hoàn tất giao dịch trong Q3/2026 sau khi được cổ đông/chủ nợ thông qua, để dồn lực cho R&D → tin liên quan hệ sinh thái Vingroup, **trung tính**, tác động trực tiếp đến VIC chưa rõ ràng (chưa kiểm chứng mức độ ảnh hưởng đến định giá VIC). ([Vietstock](https://vietstock.vn/2026/05/vinfast-muon-thoai-von-mang-san-xuat-de-don-luc-vao-nghien-cuu-phat-trien-xe-737-1441951.htm))
- Không tìm thấy tin tức cụ thể mới trong tháng 8/2026 riêng cho VIC (KQKD Q2, sự kiện lớn) qua tìm kiếm — **chưa kiểm chứng/không thấy tin đáng chú ý** ở thời điểm hiện tại ngoài các mục trên.

## VRE — Vincom Retail (RealEstate)

- **Kế hoạch 2026**: doanh thu 10.132 tỷ đồng (+16%), lãi sau thuế 5.375 tỷ đồng (+15%) so với 2025 (loại trừ thu nhập bất thường) → **tích cực**. ([Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/vincom-retail-vre-dat-muc-tieu-doanh-thu-10132-ty-dong-nam-2026-post388253.html))
- **Cổ tức tiền mặt 10% (1.000đ/cp)**, tổng chi ~2.272 tỷ đồng, dự kiến chi trả **Q3/2026** → **catalyst gần** (ex-date cụ thể chưa công bố trong kết quả tìm kiếm — cần theo dõi thông báo GDKHQ chính thức). ([Báo Pháp luật VN](https://baophapluat.vn/dhdcd-vincom-retail-vre-2026-ke-hoach-lai-5-375-ty-dong-chot-chia-co-tuc-tien-mat-ty-le-10.html))
- **Q1/2026**: doanh thu đạt 25%, lãi đạt ~30% kế hoạch năm; lượt khách đến TTTM +13-15%, doanh thu shared-space +23-25% YoY → **tích cực**, khởi đầu năm tốt. ([Người quan sát](https://nguoiquansat.vn/vincom-retail-vre-dat-muc-tieu-lai-hon-5-300-ty-dong-trong-nam-2026-281990.html))
- **Ra mắt thương hiệu Vincom Collection** (mô hình phố mua sắm ngoài trời, hợp tác với các khu đô thị Vinhomes, VRE hưởng hoa hồng không cần vốn đầu tư trực tiếp) → **tích cực** dài hạn, mô hình vốn nhẹ. Tỷ lệ lấp đầy bình quân 88%, còn ~12% diện tích sàn để khai thác thêm doanh thu.

---

## 📅 Sự kiện sắp tới

- **21/9/2026**: FTSE Russell chính thức nâng hạng TTCK Việt Nam lên Thị trường Mới nổi Thứ cấp (Secondary Emerging Market) — xác nhận chính thức từ kỳ rà soát giữa kỳ 8/4/2026; dòng vốn ngoại phân bổ theo lộ trình nhiều đợt, bắt đầu tháng 9/2026, hoàn tất trong 2027 → **catalyst vĩ mô tích cực mạnh cho toàn thị trường**, đặc biệt nhóm vốn hóa lớn/bluechip (VIC, VRE có thể hưởng lợi dòng vốn ETF/quỹ mô phỏng chỉ số mới nổi). ([VnEconomy](https://vneconomy.vn/ftse-russell-xac-nhan-viet-nam-vuot-qua-ky-review-chinh-thuc-nang-hang-vao-thang-92026.htm), [Doanh nhân Pháp luật](https://doanhnhan.baophapluat.vn/chinh-thuc-ftse-russell-xac-nhan-nang-hang-chung-khoan-viet-nam-len-thi-truong-moi-noi-tu-thang-9-2026.html))
- **PDR — cửa sổ mua cổ phiếu của Chủ tịch**: 31/7–29/8/2026 (đang diễn ra, còn ~3 phiên tính đến as-of 26/8/2026).
- **VRE — cổ tức tiền mặt 10%**: chi trả dự kiến Q3/2026, ngày GDKHQ cụ thể chưa xác định — cần theo dõi thông báo chính thức từ HOSE.
- **24/8/2026**: Quốc hội dự kiến xem xét/thông qua Luật Phát triển đô thị → liên quan gián tiếp đến toàn ngành bất động sản (KDH, PDR, VIC, VRE), tác động cụ thể đến từng mã **chưa kiểm chứng**. ([Vietstock](https://vietstock.vn/2026/08/luat-phat-trien-do-thi-du-kien-duoc-quoc-hoi-thong-qua-ngay-trong-thang-8-761-1480553.htm))

## 🌐 Bối cảnh chung (vĩ mô/ngành)

- **VN-Index** đang thử thách vùng 1.775–1.810 điểm (kịch bản VNDirect: dao động 1.720–1.800 trong tháng 8), nhưng **thanh khoản không theo kịp đà tăng** — khối lượng giảm ~10,3% so với tuần trước và thấp hơn ~9% so với trung bình 20 tuần (phiên 19/8/2026) → **cảnh báo**: đà tăng thiếu sự xác nhận của dòng tiền, rủi ro giằng co/điều chỉnh ngắn hạn. ([Vietstock](https://vietstock.vn/2026/08/nhip-dap-thi-truong-1908-vn-index-giang-co-trong-boi-canh-thanh-khoan-sut-giam-1636-1482473.htm), [Tiền Phong](https://tienphong.vn/vn-index-truoc-cua-ai-1800-diem-dong-tien-co-du-suc-duy-tri-post1866466.tpo))
- **Dư nợ margin** tăng 26,7 nghìn tỷ đồng (+6% so với quý trước), khiến thị trường nhạy cảm hơn trong các đợt điều chỉnh mạnh (như tháng 7/2026); sau đợt bán tháo, một phần đòn bẩy đã được giải phóng, có thể giảm áp lực force-sell trong 1-2 tháng tới → **trung tính**, cần theo dõi.
- **Bất động sản TP.HCM**: hơn 400 dự án đã được tháo gỡ pháp lý dứt điểm; TP.HCM đặt mục tiêu giải quyết 28 "siêu dự án" khó nhất trong năm 2026 → **tích cực** cho nhóm BĐS nói chung (KDH, PDR, VIC, VRE đều liên quan TP.HCM) nhưng một số dự án lớn của doanh nghiệp khác (QCG, Vạn Phúc...) vẫn vướng — mức độ hưởng lợi cụ thể cho từng mã trong danh sách **chưa kiểm chứng** riêng lẻ. ([Tuổi Trẻ](https://tuoitre.vn/tp-hcm-quyet-tam-dut-diem-28-sieu-du-an-bat-dong-san-kho-nhat-trong-nam-2026-20260602085339228.htm))
- **FTSE nâng hạng** (21/9/2026) là catalyst vĩ mô lớn nhất trong khung thời gian gần với time-stop 25 phiên (~5 tuần) của mô hình — nằm gọn trong cửa sổ swing hiện tại.

## 🏆 Xếp hạng theo hỗ trợ tin tức (mạnh → yếu)

1. **PDR** — catalyst rõ nhất và đang diễn ra (Chủ tịch mua 20 triệu cp, cửa sổ đến 29/8/2026), nhưng đi kèm rủi ro pha loãng từ kế hoạch phát hành ~200 triệu cp → tin tức hỗn hợp nhưng có tín hiệu insider tích cực gần nhất.
2. **VRE** — kế hoạch tăng trưởng 2 chữ số, cổ tức tiền mặt sắp chi trả Q3/2026, mô hình Vincom Collection vốn nhẹ, hưởng lợi tiềm năng từ nâng hạng FTSE.
3. **KDH** — nền tảng cơ bản vững (sạch nợ trái phiếu, lãi 2025 vượt kế hoạch), nhưng thiếu catalyst ngắn hạn cụ thể trong khung 5 tuần.
4. **VIC** — hưởng lợi tiềm năng từ nâng hạng FTSE (cổ phiếu vốn hóa lớn) nhưng không có tin tức cụ thể mới trong tháng 8/2026 qua tìm kiếm; giao dịch thoái vốn nội bộ Vinpearl/VinFast là nhiễu, không phải catalyst trực tiếp.
5. **PNJ** — tin tức hỗn hợp rõ rệt nhất: doanh thu tăng mạnh nhưng Q2/2026 lỗ do trích lập dự phòng — cần thêm thông tin để đánh giá, đây là mã có rủi ro tin tức cụ thể nhất trong nhóm.

*(Ghi chú: PNJ không nằm trong top 5 candidate theo bảng WHITEBOARD gốc — đã bổ sung vì có trong signals_latest.csv hạng #2. Xếp hạng trên chỉ phản ánh sắc thái tin tức/cơ bản, KHÔNG PHẢI khuyến nghị đầu tư.)*



---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

### 🐂 Agent C — Tổng hợp hướng BÒ · 2026-08-26 07:45

*Lưu ý: mô hình nền có edge YẾU (AUC ~0.53–0.55) — các luận điểm dưới đây không dựa vào score như bằng chứng chính, mà tìm cách kết hợp kỹ thuật (Agent A) + catalyst thật (Agent B) để có case chắc hơn score đơn thuần. Đây KHÔNG PHẢI khuyến nghị đầu tư.*

---

## 1. VIC — Vingroup

**Luận điểm mua:** Đây là setup kỹ thuật sạch nhất trong toàn bộ danh sách. Theo Agent A, VIC là **mã duy nhất trong top-5 nằm trên cả MA20 và MA50**, đang breakout khỏi vùng tích lũy đi ngang kéo dài 4 tháng (200–230k), điểm kỹ thuật 7/10 — cao nhất nhóm. RSI 61.1 vẫn ở vùng trung tính, chưa quá mua, còn dư địa tăng trước khi chạm vùng nhạy cảm (>70). Về vĩ mô, Agent B nêu **FTSE Russell chính thức nâng hạng TTCK Việt Nam lên Thị trường Mới nổi Thứ cấp từ 21/9/2026**, và dòng vốn ETF/quỹ mô phỏng chỉ số mới nổi có xu hướng ưu tiên nhóm vốn hóa lớn/bluechip — VIC là một trong những mã được B liệt kê là có thể hưởng lợi tiềm năng từ dòng vốn này.

**Catalyst:** FTSE nâng hạng (21/9/2026) rơi đúng vào khung time-stop 25 phiên (~5 tuần) của mô hình — Agent B đã ghi rõ điểm trùng khớp này. Đây là catalyst vĩ mô có thật, đã được xác nhận chính thức (không phải tin đồn), khác với các catalyst công ty đơn lẻ dễ bị nhiễu.

**Kịch bản giá tới TP (+8%, 240,840đ):** Giá đang breakout khỏi vùng đi ngang 200–230k sau 4 tháng tích lũy — về mặt kỹ thuật cổ điển, breakout khỏi nền tích lũy dài thường có dư địa dịch chuyển tương ứng với biên độ vùng tích lũy trước đó (~30k, tức hơn 8% từ vùng kháng cự ~220k). Nếu dòng tiền ngoại bắt đầu giải ngân trước ngày chính thức 21/9 (thị trường thường phản ánh trước sự kiện đã biết), VIC — cổ phiếu vốn hóa lớn nhất nhóm bất động sản — có thể là một trong những mã hưởng lợi sớm.

**Rủi ro & vì sao chịu được:** Agent A lưu ý khối lượng xác nhận vẫn yếu (vol_ratio 0.55, dưới 1 như toàn bộ nhóm), và RSI đã gần vùng nhạy cảm. Tuy nhiên: (1) SL tại 211,850đ (-5%) nằm dưới vùng breakout, nếu giá quay lại vùng tích lũy cũ thì cắt lỗ sớm, giới hạn thiệt hại; (2) time-stop 25 phiên đảm bảo không giữ vị thế "chết" quá lâu nếu breakout thất bại; (3) tin Vinpearl thoái ~5,2 triệu cp và VinFast dự kiến thoái vốn sản xuất — Agent B đánh giá đây là **"trung tính/tiêu cực nhẹ", quy mô nhỏ so với vốn hóa VIC** — không đủ sức nặng để phủ nhận setup kỹ thuật + catalyst vĩ mô.

---

## 2. PDR — Bất động sản Phát Đạt

**Luận điểm mua:** Catalyst tin tức mạnh nhất và **đang diễn ra ngay tại thời điểm phân tích**: Agent B xác nhận **Chủ tịch Nguyễn Văn Đạt đăng ký mua 20 triệu cổ phiếu** trong giai đoạn 31/7–29/8/2026 khi giá "thấp nhất 3 năm" — tính đến as-of date 26/8/2026, cửa sổ mua còn khoảng 3 phiên. Đây là tín hiệu insider tin tưởng vào giá hiện tại, và trùng khớp với việc Agent A ghi nhận giá đang **tạo đáy quanh 11.8–13k** với RSI trung tính (52.3), chưa quá bán nhưng cũng chưa đảo chiều rõ.

**Catalyst:** Chủ tịch mua cổ phiếu ở "giá thấp nhất 3 năm" ngay trong cửa sổ hiện tại — hiếm khi có sự trùng khớp thời gian rõ như vậy giữa giao dịch nội bộ và thời điểm phân tích swing.

**Kịch bản giá tới TP (+8%, 13,554đ):** Agent A ghi nhận SL hệ thống (11,922đ) nằm sát vùng đáy kỹ thuật gần nhất (~11.8–12k) — tức R:R được neo theo vùng hỗ trợ thật, không phải con số tùy ý. Nếu lực mua từ Chủ tịch (khối lượng 20 triệu cp là đáng kể) tạo hiệu ứng tâm lý kéo dòng tiền vào, việc test lại vùng kháng cự gần (13k+) trong 25 phiên là kịch bản hợp lý về mặt thời gian.

**Rủi ro & vì sao chịu được:** Rủi ro pha loãng rõ ràng — Agent B nêu kế hoạch phát hành ~200 triệu cổ phiếu (tỷ lệ 5:1, ~20% lượng lưu hành) và vol_ratio rất thấp (0.17, thấp nhất nhóm) cho thấy bật giá thiếu xác nhận dòng tiền. Vì sao vẫn chấp nhận được: (1) SL đã bám sát đáy kỹ thuật, mức lỗ tối đa nếu sai là có kiểm soát và không xa; (2) ngày GDKHQ của đợt phát hành **chưa công bố cụ thể** (theo B) — nghĩa là rủi ro pha loãng chưa chắc rơi vào đúng khung 5 tuần này; (3) hành động mua thực tế bằng tiền thật của Chủ tịch là tín hiệu mạnh hơn một kế hoạch phát hành chưa có ngày chốt.

---

## 3. VRE — Vincom Retail

**Luận điểm mua:** Đây là case "cơ bản tốt, kỹ thuật yếu hơn" — thành thật mà nói, Agent A xếp VRE thấp nhất về kỹ thuật thuần túy (4/10, đang trong downtrend từ đỉnh tháng 4). Nhưng Agent B cho thấy nền tảng cơ bản và catalyft gần vượt trội: kế hoạch 2026 tăng trưởng 2 chữ số (doanh thu +16%, lãi +15%), **Q1/2026 đã đạt ~25% doanh thu và ~30% lợi nhuận kế hoạch năm** — khởi đầu năm rất tốt, và mô hình "Vincom Collection" mới ra mắt không cần vốn đầu tư trực tiếp (vốn nhẹ, hưởng hoa hồng).

**Catalyst:** (1) **Cổ tức tiền mặt 10% (1.000đ/cp), dự kiến chi trả Q3/2026** — rơi vào đúng khung thời gian phân tích hiện tại (dù ngày GDKHQ cụ thể B ghi rõ là **chưa công bố**, cần theo dõi); (2) tiềm năng hưởng lợi dòng vốn ETF từ nâng hạng FTSE (21/9/2026), tương tự VIC, do VRE cũng là bluechip vốn hóa lớn trong rổ chỉ số.

**Kịch bản giá tới TP (+8%, 27,270đ):** MA50 theo Agent A "bắt đầu đi ngang" — dấu hiệu đà giảm có thể chững lại. Nếu thông tin GDKHQ cổ tức được công bố trong 25 phiên tới, đây có thể là chất xúc tác ngắn hạn kéo dòng tiền quan tâm trở lại trước ngày chốt quyền — kịch bản này là suy luận logic thông thường (tin cổ tức thường thu hút chú ý trước ex-date), chưa phải sự kiện đã xảy ra.

**Rủi ro & vì sao chịu được:** Rủi ro kỹ thuật lớn nhất trong 3 mã — vẫn dưới MA50, "đang hồi trong xu hướng giảm dài hơn, chưa có tín hiệu đảo chiều rõ" (Agent A), vol_ratio chỉ 0.23. Đây là case yếu nhất về setup giá, chấp nhận được chỉ vì: (1) SL 23,987đ (-5%) giới hạn rủi ro rõ ràng; (2) nền cơ bản Q1/2026 đã thực sự vượt kế hoạch (không phải kỳ vọng suông); (3) hai catalyst (cổ tức + FTSE) độc lập với kỹ thuật, nên dù giá chưa xác nhận đảo chiều, có cơ sở thật để theo dõi trong thời gian chờ.

---

## Phản biện trước (chuẩn bị cho Agent D)

- **"Cả 5 mã đều vol_ratio <1, không có dòng tiền xác nhận"** — đúng, đây là điểm yếu chung toàn danh sách (Agent A nêu rõ). Phản hồi: với VIC, vol_ratio 0.55 là *cao nhất* trong nhóm và đi kèm breakout kỹ thuật + catalyst vĩ mô đã xác nhận (không phải tin đồn) — hai lớp bằng chứng độc lập bù đắp phần nào cho thiếu khối lượng.
- **"Score mô hình chỉ nhỉnh hơn 0.5 một chút, AUC yếu"** — đúng, và đây là lý do case bò của cả 3 mã trên **không dựa vào score** làm luận cứ chính, mà dựa vào catalyst tin tức xác nhận (insider buying của PDR, sự kiện FTSE đã công bố chính thức, KQKD Q1 vượt kế hoạch của VRE) — những dữ kiện độc lập với model.
- **"PDR có rủi ro pha loãng ~20%"** — thật, đã nêu ở trên; điểm mấu chốt là ngày GDKHQ chưa công bố, nên rủi ro này chưa chắc kích hoạt trong khung 5 tuần.
- **"VIC có tin thoái vốn nội bộ (Vinpearl, VinFast)"** — Agent B tự đánh giá là quy mô nhỏ, "trung tính/tiêu cực nhẹ", không phải catalyst tiêu cực mạnh.

---

**Kèo bò tự tin nhất: VIC** — vì đây là mã duy nhất hội tụ đủ 3 yếu tố độc lập cùng chiều: kỹ thuật tốt nhất nhóm (breakout xác nhận, điểm 7/10), chưa quá mua (RSI 61), và catalyst vĩ mô đã được xác nhận chính thức (FTSE nâng hạng 21/9/2026) rơi đúng khung time-stop — trong khi PDR và VRE mỗi mã chỉ có 1-2 chân đứng vững, còn lại phải dựa vào suy luận hoặc thông tin chưa kiểm chứng.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**


---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

### 🐻 Agent D — Tổng hợp hướng GẤU + phản biện · 2026-08-26 07:55

*Nhắc lại ngay từ đầu: mô hình nền có edge YẾU — AUC ~0.53–0.55, score cao nhất trong top-10 (KDH 0.5924) chỉ nhỉnh hơn coin-flip một chút. Toàn bộ phần dưới là stress-test cho luận điểm bò của Agent C, KHÔNG PHẢI khuyến nghị bán/tránh chắc chắn.*

---

## Phản biện Agent C (từng mã)

### 1. VIC

- **Agent C cho rằng** vol_ratio 0.55 là "cao nhất nhóm" nên bù đắp phần nào cho thiếu khối lượng. Nhưng 0.55 vẫn là **dưới 1** — tức khối lượng vẫn *dưới trung bình* tại đúng thời điểm giá phá vỡ vùng tích lũy 4 tháng. Một breakout kỹ thuật "sách vở" cần vol_ratio rõ ràng >1 (lý tưởng >1.5) để xác nhận dòng tiền thật sự nhập cuộc — "cao nhất trong một nhóm toàn số liệu yếu" không biến nó thành tín hiệu mạnh, chỉ là "người lùn cao nhất". Agent A cũng đã tự ghi "khối lượng bùng nổ vẫn <1 (chưa xác nhận mạnh)" — C trích câu này nhưng vẫn quy đổi thành "hai lớp bằng chứng độc lập bù đắp" — đây là suy luận lạc quan, không phải bằng chứng thêm.
- **Agent C cho rằng** RSI 61.1 "còn dư địa tăng trước khi chạm vùng nhạy cảm >70". Nhưng chính Agent A ghi RSI 61.1 là "trung tính, **gần vùng mua nhiều**" — tức A đã cảnh báo sẵn, C chỉ chọn nửa câu tích cực.
- **Agent C dùng catalyst FTSE nâng hạng (21/9/2026) làm chân đứng chính**, nhưng đây là catalyst **vĩ mô, đã công bố chính thức từ 8/4/2026** — thị trường có gần 5 tháng để phản ánh trước. Nếu "dòng vốn ngoại giải ngân trước ngày chính thức" như C giả định, thì phần lớn khả năng đã **nằm trong giá** rồi — điều này thậm chí làm yếu đi kịch bản breakout: giá vừa phá đỉnh 4 tháng nhưng khối lượng dưới trung bình có thể là dấu hiệu "sell-the-news" tiềm ẩn hơn là dòng tiền mới. C không xét khả năng này.
- **Agent C dismiss tin Vinpearl thoái ~5,2 triệu cp và VinFast thoái vốn sản xuất** là "quy mô nhỏ, trung tính/tiêu cực nhẹ" theo đánh giá của B. Nhưng đây là **hai giao dịch thoái vốn nội bộ trong cùng hệ sinh thái Vingroup diễn ra gần nhau** — dù quy mô riêng lẻ nhỏ, một chuỗi hành động thoái vốn từ các công ty liên quan tại đúng vùng giá cao (breakout) đáng để đặt câu hỏi về niềm tin nội bộ, thay vì gạt bỏ hoàn toàn. **Giả định**: chưa đủ dữ liệu kết luận đây là tín hiệu tiêu cực mạnh, nhưng cũng không nên bị coi là "nhiễu" hoàn toàn như C làm.
- Rủi ro thực thi: VIC giá 223.000đ — SL −5% (211.850đ) tương ứng mức lỗ tuyệt đối lớn nhất nhóm; với biên độ ±7%/phiên của HOSE, một phiên giảm sàn có thể gap thẳng qua vùng SL trước khi lệnh khớp.

### 2. PDR

- **Agent C dùng "Chủ tịch đăng ký mua 20 triệu cp" làm catalyst chính**. Cần lưu ý: đây là **đăng ký mua**, chưa có xác nhận đã mua đủ/mua xong (nguồn B chỉ nêu giai đoạn đăng ký 31/7–29/8/2026) — lãnh đạo đăng ký mua nhưng không thực hiện hết khối lượng đăng ký không phải hiếm ở TTCK VN. **Chưa kiểm chứng** đã khớp bao nhiêu % khối lượng đăng ký tính đến 26/8/2026.
- Mua ở "giá thấp nhất 3 năm" cũng có thể đọc theo hướng ngược lại: giá đã giảm liên tục 3 năm phản ánh **suy giảm nền tảng dài hạn thực sự** (đòn bẩy cao, phát hành trái phiếu 5.600 tỷ 26/3/2026, kế hoạch pha loãng ~20%) — insider mua giá thấp không đảm bảo đảo chiều ngắn hạn trong khung 5 tuần, nhất là khi vol_ratio là **thấp nhất toàn nhóm (0.17)** — thị trường nói chung chưa "tin" theo Chủ tịch.
- **Agent C cho rằng** rủi ro pha loãng "chưa chắc kích hoạt trong khung 5 tuần" vì ngày GDKHQ chưa công bố. Đây là ngụy biện im lặng (absence of evidence ≠ evidence of absence): kế hoạch phát hành ~200 triệu cp đã được công bố và **có thể chốt ngày GDKHQ bất cứ lúc nào** trong 25 phiên tới; thị trường thường bắt đầu "pha loãng kỳ vọng" vào giá ngay khi có tin kế hoạch, không cần đợi ngày GDKHQ chính thức — điều này giới hạn trần tăng giá bất kể catalyst insider-buying.
- trend_up = **False** theo signals_latest.csv, MA50 mới chỉ "đi ngang/phẳng dần" (Agent A) — chưa phải xác nhận đảo chiều, chỉ là chưa tệ thêm.

### 3. VRE

- **Agent C tự thừa nhận đây là case kỹ thuật yếu nhất** (4/10, thấp nhất nhóm 5 mã của A) và cố gắng bù bằng cơ bản/catalyst. Nhưng đây chính là vấn đề cấu trúc: một lệnh **swing 5 tuần** cần giá phản ứng đúng hướng *trong ngắn hạn*, trong khi luận điểm của C dựa vào KQKD quý và kế hoạch năm — những yếu tố vốn đã được thị trường biết và định giá dần, không phải catalyst giật giá tức thời. "Cơ bản tốt" không tự động thắng được xu hướng giá đang giảm.
- **Catalyst cổ tức tiền mặt 10% (1.000đ/cp)** mà C dùng làm điểm tựa: (1) ngày GDKHQ **chưa công bố** — có thể rơi ngoài khung 25 phiên hoặc không hề rơi vào khung này; (2) về mặt cơ chế, vào ngày GDKHQ giá tham chiếu **bị điều chỉnh giảm đúng bằng số cổ tức** — nếu ex-date rơi trong 25 phiên, đây thực chất là một lực cản kỹ thuật lên giá (giá bị "reset" xuống), không phải lực đẩy tăng như C ngụ ý; cổ tức tiền mặt hấp dẫn nhà đầu tư dài hạn/nắm giữ, không phải catalyst đẩy giá ngắn hạn cho swing trade.
- FTSE nâng hạng: B ghi "VRE **có thể** hưởng lợi" — chưa xác nhận VRE nằm trong rổ được các quỹ mô phỏng mua trực tiếp đợt đầu (tháng 9/2026); đây là suy luận gián tiếp, C trình bày gần như chắc chắn hơn mức B thực sự xác nhận.
- vol_ratio 0.23, vẫn dưới MA50, "đang hồi trong xu hướng giảm dài hơn, chưa có tín hiệu đảo chiều rõ" (Agent A) — đây là mô tả gần với "bắt dao rơi" hơn là đảo chiều xác nhận.

---

## Rủi ro downside theo mã (kịch bản tới SL hoặc xa hơn)

- **VIC**: nếu breakout thất bại (khối lượng không theo kịp, dòng vốn FTSE đã priced-in trước), giá có thể quay lại vùng tích lũy 200–230k, chạm SL 211.850đ (−5%); do biến động vĩ mô hoặc tin xấu bất ngờ từ hệ sinh thái Vingroup (thoái vốn thêm, VinFast), rủi ro gap giảm mạnh vượt SL trong phiên biến động ±7% là có thật, đặc biệt khi vol_ratio hiện tại còn thấp nghĩa là thanh khoản để thoát hàng ở đúng giá SL cũng không chắc chắn.
- **PDR**: nếu công bố ngày GDKHQ phát hành 200 triệu cp trong 25 phiên tới, áp lực pha loãng + tâm lý bán trước ngày chốt quyền có thể đẩy giá xuyên SL 11.922đ; đòn bẩy từ đợt phát hành trái phiếu 5.600 tỷ cũng làm công ty nhạy cảm hơn với biến động lãi suất/thanh khoản hệ thống. Đây là mã có vol_ratio thấp nhất — thanh khoản thoát hàng khi thị trường xấu là rủi ro riêng.
- **VRE**: nếu downtrend từ đỉnh tháng 4 tiếp diễn (chưa có xác nhận đảo chiều thật), giá dễ chạm SL 23.987đ trước khi bất kỳ catalyst nào (cổ tức, FTSE) kịp phát huy tác dụng trong khung 25 phiên.
- **Rủi ro hệ thống chung cho cả 3 mã**: **VIC, PDR, VRE (và cả KDH trong top-5 gốc) đều thuộc nhóm ngành RealEstate** theo signals_latest.csv — đây là rủi ro tập trung ngành nghiêm trọng mà Agent C không đề cập khi xây dựng "kèo bò tự tin nhất". Nếu có tin xấu vĩ mô riêng cho ngành bất động sản (thắt chặt tín dụng, kết quả không thuận lợi của Luật Phát triển đô thị dự kiến thông qua 24/8/2026 — B ghi rõ "tác động cụ thể chưa kiểm chứng"), cả 3 mã có thể giảm đồng loạt, tương quan cao, không có tác dụng phân tán rủi ro dù chọn 3 mã "khác nhau".
- **Rủi ro thanh khoản thị trường chung**: B ghi nhận khối lượng toàn thị trường (phiên 19/8/2026) giảm ~10,3% so với tuần trước, thấp hơn ~9% so với TB 20 tuần, trong khi VN-Index đang thử vùng cản 1.775–1.810 — đúng như cảnh báo của B "đà tăng thiếu xác nhận dòng tiền, rủi ro giằng co/điều chỉnh ngắn hạn". Điều này khớp với vol_ratio thấp ở cấp độ từng mã — không phải vấn đề riêng của từng cổ phiếu mà là đặc điểm chung của thị trường hiện tại.
- **Rủi ro margin**: dư nợ margin tăng 26,7 nghìn tỷ (+6% so với quý trước) khiến thị trường nhạy cảm hơn trong các đợt điều chỉnh mạnh — nếu VN-Index đảo chiều tại vùng cản 1.775–1.810, áp lực force-sell có thể khuếch đại đà giảm ở các mã đang mua đuổi theo breakout yếu như VIC.
- **Rủi ro T+2**: nếu tin xấu xuất hiện ngay sau khi mua (đặc biệt PDR — đang chờ tin GDKHQ phát hành có thể ra bất cứ lúc nào), nhà đầu tư bị kẹp hàng T+2 không thể bán ngay để cắt lỗ sớm hơn giá mở cửa phiên kế tiếp.

---

## Mã nên tránh / rủi ro nhất

1. **KDH** — không nằm trong lựa chọn của C nhưng đáng nêu lại: điểm kỹ thuật thấp nhất nhóm gốc (3/10), Agent A gọi thẳng đây là setup "bắt dao rơi" — dưới cả MA20 & MA50, downtrend liên tục, khối lượng thấp, mới bật 2 phiên chưa xác nhận. Cơ bản tốt (lãi 2025 vượt 63% kế hoạch, sạch nợ trái phiếu) theo B nhưng B tự ghi "thiếu catalyst ngắn hạn cụ thể trong khung 5 tuần" — cơ bản tốt dài hạn không cứu được setup giá xấu ngắn hạn.
2. **PDR** — dù có catalyst insider-buying hấp dẫn nhất theo B, đây vẫn là mã có **vol_ratio thấp nhất toàn nhóm 10 mã (0.17)** và rủi ro pha loãng ~20% treo lơ lửng không rõ thời điểm — kết hợp "thanh khoản yếu nhất + rủi ro pha loãng lớn nhất" khiến đây là kèo có biên độ bất định cao nhất nếu tin xấu (GDKHQ phát hành) ra trước tin tốt (Chủ tịch hoàn tất mua).
3. **PNJ** (ngoài top-5 whiteboard gốc nhưng rank #2 theo score) — B nêu rõ đây là mã có **tin xấu cụ thể nhất, đã xảy ra**: Q2/2026 lỗ 283 tỷ dù doanh thu +12% YoY, tương phản mạnh với Q1 lãi 1.467 tỷ; nguyên nhân trích lập dự phòng do biến động giá vàng **chưa được B kiểm chứng chi tiết**. Đây là rủi ro "đã biết nhưng chưa hiểu rõ" — nguy hiểm hơn rủi ro suy đoán vì có thể lặp lại ở Q3 nếu giá vàng tiếp tục biến động.
4. **VRE** — về bản chất là mua một mã đang trong downtrend kỹ thuật (thấp điểm nhất trong 3 lựa chọn của C) chỉ dựa trên catalyst cơ bản/cổ tức chưa có ngày cụ thể — mismatch giữa khung thời gian swing (5 tuần) và bản chất chậm của các catalyst được nêu.

---

**Nhắc lại edge mô hình:** AUC ~0.53–0.55 nghĩa là mô hình chỉ nhỉnh hơn tung đồng xu một chút; ngay cả điểm số cao nhất trong toàn bộ danh sách 10 mã (KDH 0.5924) cũng không đủ để coi là tín hiệu đáng tin cậy độc lập. Toàn bộ lập luận bò của Agent C — dù có logic và dựa trên tin tức thật — vẫn xây trên nền một mô hình xác suất yếu, cộng thêm khối lượng xác nhận dưới trung bình ở toàn bộ 5 mã. Không nên diễn giải các catalyst tin tức là "chắc thắng"; chúng chỉ là xác suất bổ sung, không phải bảo chứng.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**


---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*

### 🎩 Agent E — Giám đốc Chiến lược · 2026-08-26 08:10

*KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — khung ra quyết định mô phỏng. Edge mô hình yếu (AUC ~0.53–0.55), ưu tiên bảo toàn vốn.*

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| **VIC** | THEO DÕI | TB | Kỹ thuật tốt nhất nhóm (breakout, trend_up) nhưng vol_ratio vẫn <1 và catalyst FTSE có thể đã phần nào priced-in — bò/gấu cân bằng. |
| **PDR** | THEO DÕI | TB | Insider-buying thật nhưng đối trọng bởi vol_ratio thấp nhất nhóm + rủi ro pha loãng ~20% chưa rõ thời điểm — bò/gấu cân bằng. |
| **VRE** | TRÁNH | TB | Kỹ thuật yếu nhất trong 3 mã bò chọn; catalyst cổ tức thực chất là lực cản kỹ thuật ở ngày GDKHQ, lợi ích FTSE chưa chắc — gấu thắng thế. |
| **PNJ** | TRÁNH | TB | Không có luận điểm bò; tin xấu cụ thể đã xảy ra (lỗ Q2/2026) chưa giải thích rõ + kỹ thuật yếu (rủi ro dead-cat bounce). |
| **KDH** | TRÁNH | Cao | Kỹ thuật thấp nhất nhóm ("bắt dao rơi"), không có luận điểm bò; cơ bản tốt nhưng thiếu catalyst ngắn hạn trong khung 5 tuần. |

**Stance danh mục: Thận trọng.** Toàn bộ 5/5 mã ứng viên có vol_ratio <1 (không xác nhận dòng tiền), 3/5 mã cùng ngành RealEstate (rủi ro tập trung), thanh khoản thị trường chung đang giảm khi VN-Index thử vùng cản 1.775–1.810. Không mở vị thế mới ngay; tối đa ~5% danh mục dự phòng cho VIC/PDR nếu có xác nhận thêm trong tuần tới, còn lại giữ tiền mặt.

Chi tiết đầy đủ: [`DECISION.md`](../DECISION.md)

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.**

