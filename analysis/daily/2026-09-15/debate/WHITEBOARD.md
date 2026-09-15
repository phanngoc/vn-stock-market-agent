# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-09-15)

*Board tạo lúc 2026-09-15 05:09:09. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · buy&hold kỳ kiểm định **0.3824**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): PNJ, VIC, VRE, GVR, GAS
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **PNJ** | Retail/Consumer | 36,750 | 0.58 | 39,690 | 34,912 | 42 | ↓ dưới MA50 |
| 2 | **VIC** | RealEstate | 241,500 | 0.58 | 260,820 | 229,425 | 60 | ↑ trên MA50 |
| 3 | **VRE** | RealEstate | 25,600 | 0.56 | 27,648 | 24,320 | 50 | ↑ trên MA50 |
| 4 | **GVR** | Materials | 30,350 | 0.54 | 32,778 | 28,832 | 44 | ↑ trên MA50 |
| 5 | **GAS** | Energy | 88,700 | 0.51 | 95,796 | 84,265 | 67 | ↑ trên MA50 |

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

### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-09-15 05:12

| Mã | Trend (giá vs MA20/MA50) | RSI(14) | vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **GAS** | ↑ trên MA50, breakout rõ từ đáy 65k (07/26) lên 88.7k, MA20/MA50 dốc lên | 67.1 (gần vùng quá mua, chưa vượt 70) | 0.76 (cao nhất nhóm, vẫn <1) | **6.5** | Setup kỹ thuật tốt nhất nhóm: xu hướng rõ + khối lượng đỡ hơn hẳn 4 mã còn lại. Rủi ro: RSI sát 70, có thể điều chỉnh trước khi chạm TP. |
| **VIC** | ↑ trên MA50, uptrend dài hạn từ 3/26, vừa tạo đỉnh mới ~266k rồi lùi về 241.5k | 60.2 (trung tính-tích cực) | 0.10 (rất thấp) | **6.0** | Trend đẹp nhưng khối lượng cực yếu → đợt tăng gần đây chưa được xác nhận bởi dòng tiền. TP +8% (260,820) trùng vùng đỉnh cũ — có thể là kháng cự. |
| **VRE** | ↑ trên MA50 nhưng mới cắt lên gần đây; nhìn dài hạn vẫn đang hồi phục sau downtrend từ đỉnh 36k (5/26) về đáy 21.5k (8/26) | 49.8 (trung tính) | 0.23 (thấp) | **5.0** | Tín hiệu "trên MA50" còn non, dạng hồi kỹ thuật trong xu hướng giảm dài hơn là uptrend chắc chắn. TP/SL bám sát vùng dao động gần nhất, hợp lý về mặt R:R nhưng chưa có xác nhận xu hướng mạnh. |
| **GVR** | ↑ trên MA50 nhưng giá đang đi ngang ngay tại vùng giao cắt MA20/MA50 (30-33k), sau downtrend 5/26→8/26 | 43.9 (dưới 50, động lượng yếu) | 0.15 (thấp) | **4.5** | Giá lình xình sát MA, chưa có xu hướng rõ, khối lượng èo uột. Setup mang tính "chờ xác nhận" hơn là vào lệnh ngay. |
| **PNJ** | ↓ dưới MA50, downtrend rất dốc từ ~80k (3/26) về 36.75k (9/26) | 42.0 (trung tính, không quá bán dù giảm sâu) | 0.33 (thấp, nhưng cao hơn VIC/VRE/GVR) | **3.0** | Cảnh báo rõ "bắt dao rơi": giá cách xa MA50 phía dưới, MA50 vẫn dốc xuống mạnh trên chart. RSI chưa quá bán nên chưa có tín hiệu đảo chiều chắc chắn — rủi ro kỹ thuật lớn nhất nhóm. |

**Nhận định chung:**
- Setup kỹ thuật tốt nhất nhóm (thuần túy góc nhìn trend/RSI/volume): **GAS**, nhờ xu hướng tăng rõ ràng và volume tương đối tốt hơn (dù vẫn <1, tức chưa thực sự "sôi động").
- Setup tệ nhất, rủi ro kỹ thuật cao nhất: **PNJ** — đang trong downtrend dài dưới MA50, đúng dạng "bắt dao rơi" mà mô hình cảnh báo, dù RSI chưa cho tín hiệu quá bán rõ ràng.
- **VIC** có xu hướng dài hạn đẹp nhất về hình thái giá nhưng vol_ratio 0.10 là điểm trừ lớn — đợt tăng gần nhất thiếu xác nhận dòng tiền, và vùng chốt lời +8% trùng đỉnh cũ nên khả năng gặp kháng cự.
- **VRE** và **GVR** đều là các mã mới hồi phục sau downtrend, "trên MA50" mang tính kỹ thuật ngắn hạn hơn là xu hướng vững; khối lượng cả hai đều thấp.
- Toàn bộ 5 mã đều có vol_ratio < 1 (khối lượng dưới trung bình) — nhóm chưa có mã nào cho tín hiệu dòng tiền mạnh xác nhận theo đúng nghĩa "sôi động".
- Chưa kiểm chứng: vùng hỗ trợ/kháng cự cụ thể (số liệu S/R chính xác) chỉ ước lượng bằng mắt từ chart, không có số liệu định lượng trong signals_latest.csv.

KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — chỉ là góc nhìn kỹ thuật độc lập, mô hình có edge yếu (AUC ~0.53–0.55), cần kết hợp với các agent khác và quản trị rủi ro.

### 🅱️ Agent B — Phân tích News / Cơ bản · 2026-09-15 05:20

## PNJ (Retail/Consumer)
- Q2/2026 lỗ ròng 283 tỷ đồng — quý lỗ đầu tiên trong lịch sử niêm yết, dù doanh thu thuần vẫn tăng 11,9% YoY lên 8.484 tỷ đồng; lợi nhuận 6 tháng đầu năm bị điều chỉnh giảm 35% YoY còn 729 tỷ đồng. **Tiêu cực.** [VnEconomy](https://vneconomy.vn/pnj-bat-ngo-dao-chieu-ngoan-muc-co-phieu-kich-tran-sau-chuoi-ngay-boc-hoi-gan-mot-nua-gia-tri.htm), [Elibook](https://elibook.vn/2026/09/08/pnj-trang-an-vu-kim-cuong-nhung-hoa-don-du-phong-thi-chua-xong-va-cuoc-thay-mau-co-dong-van-dang-tiep-dien/)
- Nguyên nhân lỗ: toàn bộ đến từ dự phòng cho làn sóng khách trả lại kim cương sau sự cố "P-Lab", lũy kế dự phòng tới 3/9/2026 đã lên 2.267 tỷ đồng. **Tiêu cực**, rủi ro chưa chấm dứt (theo Elibook, "vụ kim cương" đã trắng án pháp lý nhưng khoản dự phòng kế toán chưa xử lý xong). [Elibook](https://elibook.vn/2026/09/08/pnj-trang-an-vu-kim-cuong-nhung-hoa-don-du-phong-thi-chua-xong-va-cuoc-thay-mau-co-dong-van-dang-tiep-dien/)
- Công ty vẫn giữ nguyên mục tiêu cả năm 2026: doanh thu 48.660 tỷ, LNST 3.409 tỷ đồng — tín hiệu ban lãnh đạo tự tin phục hồi nửa cuối năm. **Trung tính/hơi tích cực** (chưa kiểm chứng khả năng đạt được). [VnEconomy](https://vneconomy.vn/pnj-bat-ngo-dao-chieu-ngoan-muc-co-phieu-kich-tran-sau-chuoi-ngay-boc-hoi-gan-mot-nua-gia-tri.htm)
- Đầu tháng 8/2026: dư mua hàng triệu cổ phiếu sau thông tin mới từ Công an Thanh Hóa liên quan vụ việc — chi tiết cụ thể **chưa kiểm chứng** đầy đủ trong lần tra cứu này. [Vietstock](https://vietstock.vn/2026/08/du-mua-hang-trieu-co-phieu-pnj-sau-thong-tin-moi-tu-cong-an-thanh-hoa-830-1483514.htm)

## VIC (RealEstate — Vingroup)
- Đầu tháng 9/2026, giá cổ phiếu đảo chiều mạnh: tăng gần 30% trong chưa đầy 3 tuần lên đỉnh mới, sau đó có phiên đảo chiều giảm hơn 4,3% (đóng cửa 245.000đ) từ mức tăng gần 3,5% đầu phiên. **Trung tính** (biến động 2 chiều, không phải xu hướng 1 chiều). [CafeF](https://cafef.vn/chuyen-gi-vua-xay-ra-voi-co-phieu-vingroup-188260907154438857.chn)
- Sau 6 tháng đầu năm 2026, Vingroup đạt ~46% kế hoạch doanh thu và ~60% kế hoạch lợi nhuận cả năm (kế hoạch: doanh thu 485.000 tỷ, LNST 35.000 tỷ). Lợi nhuận vượt tiến độ nhưng doanh thu còn chậm. **Hỗn hợp, thiên tích cực về lợi nhuận.** [Fireant](https://web.fireant.vn/ma-chung-khoan/VIC)
- Giữa tháng 8/2026: được thông qua phát hành trái phiếu quốc tế tối đa 455 tỷ won Hàn Quốc (~8.050 tỷ đồng) — tăng đòn bẩy tài chính cho mở rộng. **Trung tính/hơi tiêu cực** (rủi ro nợ). [Fireant](https://web.fireant.vn/ma-chung-khoan/VIC)
- Ngày 10/9/2026: khối ngoại và tự doanh mua ròng tích cực VIC (cùng FPT), trong khi bán ròng VHM — dòng tiền đang phân hóa nội bộ nhóm Vin. **Tích cực ngắn hạn cho VIC.** [CafeF](https://cafef.vn/chuyen-gi-vua-xay-ra-voi-co-phieu-vingroup-188260907154438857.chn)
- **Catalyst xác nhận**: VIC nằm trong nhóm 3 mã Large Cap được FTSE Russell thêm vào rổ chỉ số đợt nâng hạng, hiệu lực từ 21/9/2026. **Tích cực** — dòng vốn ngoại thụ động dự kiến đổ vào. [Người Quan Sát](https://nguoiquansat.vn/chinh-thuc-lo-dien-danh-muc-cac-ma-ftse-se-mua-tu-thang-9-2026-goi-ten-vic-vhm-vcb-hpg-311887.html)

## VRE (RealEstate — Vincom Retail)
- 9 tháng đầu năm 2026: doanh thu 6.525 tỷ đồng (đạt 68,5% kế hoạch năm), LNST 3.787 tỷ đồng (đạt 80,6% kế hoạch năm) — tiến độ lợi nhuận vượt kế hoạch. **Tích cực.** [Vietstock/DNSE](https://www.dnse.com.vn/senses/tin-tuc/mo-hinh-moi-giup-vincom-retail-hut-khach-co-phieu-vre-con-hap-dan-35234874)
- MBS dự báo cả năm 2026: doanh thu 9.181 tỷ, LNST 5.454 tỷ; nếu loại trừ khoản lợi nhuận bất thường từ thoái vốn năm 2025, lợi nhuận cốt lõi 2026 thực chất tăng trưởng ~20%. **Tích cực** (tăng trưởng thực chất, không chỉ so sánh danh nghĩa). [MBS Research PDF](https://www.mbs.com.vn/files/uploads/2026/02/VRE_BCPT_20260209.pdf)
- Mô hình bán lẻ mới giúp thu hút khách thuê/khách hàng, hỗ trợ định giá. **Tích cực.** [DNSE](https://www.dnse.com.vn/senses/tin-tuc/mo-hinh-moi-giup-vincom-retail-hut-khach-co-phieu-vre-con-hap-dan-35234874)
- **Catalyst xác nhận**: VRE nằm trong nhóm cổ phiếu Small Cap được FTSE thêm vào rổ chỉ số, hiệu lực 21/9/2026. **Tích cực.** [Người Quan Sát](https://nguoiquansat.vn/chinh-thuc-lo-dien-danh-muc-cac-ma-ftse-se-mua-tu-thang-9-2026-goi-ten-vic-vhm-vcb-hpg-311887.html)

## GVR (Materials — Tập đoàn Cao su VN)
- Q1/2026 lợi nhuận tăng đáng kể; MBS từng khuyến nghị trung lập (neutral) với giá mục tiêu 36.100đ (báo cáo cũ hơn, có thể không còn cập nhật). **Trung tính.** [Finhay](https://www.finhay.com.vn/en/co-phieu-gvr)
- Tháng 7/2026: Phó Tổng Giám đốc Trần Thanh Phụng nghỉ hưu — thay đổi nhân sự cấp cao. **Trung tính.** [Baomoi](https://baomoi.com/tap-doan-cong-nghiep-cao-su-viet-nam-gvr-tag13252.epi)
- Rủi ro pháp lý: Bộ Tài chính sở hữu 96,8% GVR; theo Luật Chứng khoán sửa đổi (hiệu lực 1/1/2025), công ty đại chúng phải có ≥10% cổ phần biểu quyết do ít nhất 100 cổ đông nhỏ nắm giữ, nếu không sẽ bị hủy niêm yết bắt buộc sau 1 năm. Tỷ lệ cổ đông nhỏ của GVR hiện có nguy cơ không đạt ngưỡng này — mốc thời hạn cụ thể **chưa kiểm chứng** trong lần tra cứu này. **Tiêu cực/rủi ro cần theo dõi.** [Finhay](https://www.finhay.com.vn/en/co-phieu-gvr)
- **Xác nhận KHÔNG có trong danh sách 27 mã Large/Mid/Small Cap của FTSE đợt nâng hạng 9/2026** (chưa rõ có nằm trong 90 mã Micro Cap hay không). Do đó GVR không có catalyst dòng vốn FTSE trực tiếp như VIC/VRE. **Trung tính/hơi tiêu cực so sánh tương đối.** [Người Quan Sát](https://nguoiquansat.vn/chinh-thuc-lo-dien-danh-muc-cac-ma-ftse-se-mua-tu-thang-9-2026-goi-ten-vic-vhm-vcb-hpg-311887.html)

## GAS (Energy — PV GAS)
- Ngày 14/9/2026, ĐHĐCĐ bất thường bầu Chủ tịch mới (ông Bùi Minh Tiến), Tổng Giám đốc mới (ông Dương Trí Hối) và thành viên HĐQT mới (ông Nguyễn Tuấn Anh) — cải tổ nhân sự cấp cao đồng loạt. **Trung tính** (chưa rõ tác động dài hạn). [Tiền Phong](https://tienphong.vn/pv-gas-co-chu-tich-va-tong-giam-doc-moi-post1876422.tpo)
- PV GAS công bố **không còn đáp ứng điều kiện công ty đại chúng**: cổ phần biểu quyết do cổ đông không phải cổ đông lớn nắm giữ chỉ ~102 triệu cổ phần, tương đương 4,24% tổng số cổ phần biểu quyết (dưới ngưỡng luật định). **Tiêu cực** — rủi ro pháp lý/quản trị tương tự GVR. [Người Quan Sát](https://nguoiquansat.vn/pv-gas-cong-bo-thong-tin-bat-thuong-lien-quan-so-tien-6-000-ty-dong-315134.html), [Smartly](https://smartly.vn/tin-tuc/pv-gas-co-24743-co-dong-nhung-van-khong-du-dieu-kien-cong-ty-dai-chung)
- Chi trả cổ tức tiền mặt 2025 tỷ lệ 25% (2.500đ/cp), tổng ~6.032 tỷ đồng, thanh toán từ 9/9 đến 20/11/2026. **Tích cực** (dòng tiền cổ đông), nhưng giá tham chiếu sẽ điều chỉnh giảm quanh ngày GDKHQ. [CafeF](https://cafef.vn/pv-gas-sap-chi-hon-6000-ty-dong-tra-co-tuc-nam-2025-188260910150319815.chn)
- 7 tháng đầu 2026: doanh thu hợp nhất hơn 95.300 tỷ đồng (+39% YoY), lợi nhuận trước thuế hơn 12.600 tỷ đồng (+20% YoY) — nền tảng kinh doanh vững. **Tích cực.** [CafeF](https://cafef.vn/mot-dai-gia-dau-khi-choi-lon-tra-hon-6000-ty-dong-tien-co-tuc-188260909152106874.chn)
- Không nằm trong danh sách 27 mã FTSE Large/Mid/Small Cap đợt 9/2026. **Trung tính/thiếu catalyst dòng vốn ngoại.** [Người Quan Sát](https://nguoiquansat.vn/chinh-thuc-lo-dien-danh-muc-cac-ma-ftse-se-mua-tu-thang-9-2026-goi-ten-vic-vhm-vcb-hpg-311887.html)

## Sự kiện sắp tới
- **21/9/2026**: FTSE Russell chính thức triển khai nâng hạng TTCK Việt Nam từ Cận biên lên Mới nổi Thứ cấp, phân bổ theo lộ trình 4 đợt đến 9/2027, ước tính ~150 triệu USD đợt đầu. VIC (Large Cap) và VRE (Small Cap) nằm trong danh sách được mua; GVR, GAS, PNJ **không** nằm trong nhóm 27 mã Large/Mid/Small. [VnEconomy](https://vneconomy.vn/ftse-russell-xac-nhan-viet-nam-vuot-qua-ky-review-chinh-thuc-nang-hang-vao-thang-92026.htm), [Người Quan Sát](https://nguoiquansat.vn/chinh-thuc-lo-dien-danh-muc-cac-ma-ftse-se-mua-tu-thang-9-2026-goi-ten-vic-vhm-vcb-hpg-311887.html)
- **~23/9/2026**: GAS dự kiến chốt danh sách cổ đông nhận cổ tức 25% tiền mặt (ngày GDKHQ sẽ trước đó vài ngày làm việc — ngày chính xác **chưa kiểm chứng**). [CafeF](https://cafef.vn/pv-gas-sap-chi-hon-6000-ty-dong-tra-co-tuc-nam-2025-188260910150319815.chn)
- **26/10/2026**: PNJ dự kiến công bố BCTC quý 3/2026 — sẽ đánh giá lại đầy đủ giá trị thu hồi thực tế của kim cương tồn kho, có thể ảnh hưởng mạnh đến lợi nhuận công bố. [VnEconomy](https://vneconomy.vn/pnj-bat-ngo-dao-chieu-ngoan-muc-co-phieu-kich-tran-sau-chuoi-ngay-boc-hoi-gan-mot-nua-gia-tri.htm)
- **Cuối năm 2026**: VRE dự kiến khai trương phố thương mại J-Town tại Tuyên Quang. [DNSE](https://www.dnse.com.vn/senses/tin-tuc/mo-hinh-moi-giup-vincom-retail-hut-khach-co-phieu-vre-con-hap-dan-35234874)
- GVR/GAS: thời hạn cụ thể để khắc phục tình trạng "không đủ điều kiện công ty đại chúng" trước nguy cơ hủy niêm yết bắt buộc — **chưa kiểm chứng** mốc ngày chính xác, cần theo dõi thêm công bố chính thức.

## Bối cảnh chung
- Sự kiện vĩ mô lớn nhất hiện tại là việc FTSE Russell chính thức nâng hạng TTCK Việt Nam lên Thị trường Mới nổi Thứ cấp, có hiệu lực từ 21/9/2026 — được xem là cột mốc lịch sử, kỳ vọng thu hút dòng vốn ngoại lớn trong nhiều năm tới. Nhóm cổ phiếu lọt rổ (trong đó có VIC, VRE) được cho là hưởng lợi trực tiếp từ dòng vốn thụ động; nhóm không lọt rổ (GVR, GAS, PNJ) không có catalyst này. [VnEconomy](https://vneconomy.vn/ftse-russell-xac-nhan-viet-nam-vuot-qua-ky-review-chinh-thuc-nang-hang-vao-thang-92026.htm)
- Nhóm doanh nghiệp nhà nước/cổ phần hóa (GVR, GAS) đang đối mặt rủi ro pháp lý chung về tỷ lệ cổ đông nhỏ tối thiểu theo Luật Chứng khoán sửa đổi — có thể ảnh hưởng đến thanh khoản/tâm lý nhà đầu tư nếu không xử lý kịp thời.
- Ngành bán lẻ trang sức (PNJ) đang trong giai đoạn xử lý hậu quả sự cố chất lượng sản phẩm (P-Lab), tạo ra khoản lỗ kế toán bất thường quý 2/2026; cần chờ BCTC quý 3 để đánh giá mức độ dứt điểm của rủi ro.
- Dòng tiền khối ngoại/tự doanh đang phân hóa trong nhóm cổ phiếu lớn (mua VIC/FPT, bán VHM) — cho thấy thị trường đang tái cơ cấu danh mục quanh sự kiện nâng hạng, không phải xu hướng mua/bán đồng loạt.

## Xếp hạng theo hỗ trợ tin tức (mạnh → yếu)
1. **VRE** — KQKD 9 tháng vượt tiến độ kế hoạch, tăng trưởng lợi nhuận cốt lõi thực chất ~20%, có catalyst FTSE (Small Cap) và mở dự án mới, không có rủi ro pháp lý nổi bật.
2. **VIC** — Có catalyst FTSE (Large Cap, dòng vốn ngoại lớn nhất nhóm), lợi nhuận vượt tiến độ kế hoạch, nhưng biến động giá 2 chiều mạnh và tăng đòn bẩy nợ vay quốc tế.
3. **GAS** — Nền tảng kinh doanh rất mạnh (doanh thu +39%, lợi nhuận +20%) và cổ tức tiền mặt cao, nhưng vướng rủi ro pháp lý "công ty đại chúng" và không có catalyst dòng vốn FTSE.
4. **GVR** — Thiếu tin tức tích cực rõ ràng gần đây, không có catalyst FTSE, mang rủi ro pháp lý cổ đông nhỏ/nguy cơ hủy niêm yết tương tự GAS nhưng ít thông tin cập nhật hơn.
5. **PNJ** — Tin tức tiêu cực nổi bật nhất trong nhóm: lỗ ròng quý 2 kỷ lục do dự phòng vụ P-Lab, lợi nhuận 6 tháng giảm 35% YoY; rủi ro chưa dứt điểm, chờ BCTC quý 3 (26/10/2026).

*Đây KHÔNG PHẢI khuyến nghị đầu tư — chỉ là tổng hợp tin tức/bối cảnh cơ bản để hội đồng tranh luận tham khảo. Mô hình ML nền có edge yếu (AUC ~0.53–0.55), tin tức trên không thay thế quản trị rủi ro.*



---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

### 🐂 Agent C — Tổng hợp hướng BÒ · 2026-09-15 05:32

Ghi chú trước khi vào luận điểm: mô hình nền có **edge yếu (AUC ~0.53–0.55)** — điểm số (`score`) không phải căn cứ đủ mạnh để mua một mình. Luận điểm bò dưới đây chỉ dựng trên 3 mã có **đồng thời** kỹ thuật (Agent A) và catalyst/tin tức thật (Agent B) ủng hộ; PNJ và GVR bị loại vì Agent B xếp hạng "hỗ trợ tin tức yếu nhất nhóm" và không có điểm tích cực đủ rõ để chống lại rủi ro đã nêu.

---

## 1) VIC

**Luận điểm mua:** Theo Agent A, VIC có "xu hướng dài hạn đẹp nhất về hình thái giá" (uptrend từ 3/26, RSI 60.2 trung tính-tích cực, điểm KT 6.0/10 — cao thứ nhì nhóm 5 mã). Theo Agent B, VIC là 1 trong 3 mã Large Cap được FTSE Russell chính thức đưa vào rổ nâng hạng, hiệu lực từ 21/9/2026 — dòng vốn ngoại thụ động dự kiến đổ vào. Đáng chú ý, Agent B ghi nhận ngày 10/9/2026 khối ngoại và tự doanh **đã mua ròng tích cực VIC** trước khi catalyst chính thức có hiệu lực — dòng tiền có vẻ đi trước sự kiện. Về cơ bản, lũy kế 6 tháng đầu năm Vingroup đạt ~60% kế hoạch lợi nhuận cả năm (vượt tiến độ so với ~46% kế hoạch doanh thu), theo Agent B.

**Catalyst:** FTSE Large Cap có hiệu lực 21/9/2026 (rơi trong vòng time-stop 25 ngày của mô hình) + tín hiệu mua ròng khối ngoại/tự doanh xác nhận trước sự kiện (Agent B).

**Kịch bản giá tới TP +8% (260.820đ, giá hiện tại 241.500đ):** Theo Agent A, VIC vừa tạo đỉnh mới ~266k đầu tháng 9/2026 rồi mới lùi về vùng hiện tại — nghĩa là vùng TP +8% nằm **dưới** mức giá thị trường đã từng thực sự giao dịch gần đây, không phải một đỉnh chưa từng được kiểm định (suy luận logic từ dữ liệu A, không phải dữ kiện mới). Catalyst FTSE rơi đúng trong khung thời gian nắm giữ.

**Rủi ro & vì sao chịu được:** Agent A cảnh báo vol_ratio chỉ 0.10 (thấp nhất nhóm) — đợt tăng gần đây "chưa được xác nhận bởi dòng tiền", và vùng TP trùng đỉnh cũ có thể là kháng cự. Đây là rủi ro thật, không phủ nhận. Nhưng vì giá đã từng chạm vùng ~266k, kháng cự ở đây là vùng đã có thanh khoản thực tế trước đó chứ không phải đỉnh hoàn toàn mới. SL ở 229.425đ (khoảng -5% từ giá hiện tại) và time-stop 25 ngày giới hạn thiệt hại nếu catalyst FTSE không tạo đủ lực đẩy. Rủi ro đòn bẩy từ phát hành trái phiếu quốc tế (theo Agent B) là rủi ro cấu trúc dài hạn, nằm ngoài khung thời gian swing 25 ngày.

---

## 2) VRE

**Luận điểm mua:** Agent B xếp VRE là mã có **hỗ trợ tin tức mạnh nhất nhóm 5 mã**: doanh thu 9 tháng đầu năm đạt 68,5% kế hoạch, LNST đạt 80,6% kế hoạch — tiến độ lợi nhuận vượt kế hoạch rõ rệt; MBS ước tính nếu loại trừ khoản lợi nhuận bất thường từ thoái vốn 2025, tăng trưởng lợi nhuận cốt lõi 2026 thực chất ~20%. VRE cũng nằm trong rổ FTSE Small Cap nâng hạng, hiệu lực 21/9/2026 — cùng nhóm catalyst dòng vốn ngoại như VIC. Về kỹ thuật, Agent A ghi nhận giá vừa cắt lên trên MA50, RSI 49.8 hoàn toàn trung tính — còn nhiều dư địa trước khi vào vùng quá mua, khác với GAS đã gần sát 70.

**Catalyst:** FTSE Small Cap hiệu lực 21/9/2026 + KQKD vượt kế hoạch + mô hình bán lẻ mới hỗ trợ thu hút khách thuê (Agent B), không có rủi ro pháp lý/đòn bẩy nào được Agent B nêu cho VRE (khác với VIC, GAS, GVR).

**Kịch bản giá tới TP +8% (27.648đ, giá hiện tại 25.600đ):** RSI 49.8 (trung tính, theo A) để lại nhiều dư địa tăng hơn trước khi chạm vùng quá mua, so với các mã còn lại trong nhóm. Việc giá "mới cắt lên MA50" kết hợp catalyst FTSE trong đúng 6 ngày tới có thể là chất xúc tác đủ để duy trì đà tăng thay vì đảo chiều ngay.

**Rủi ro & vì sao chịu được:** Agent A thẳng thắn cảnh báo đây là dạng "hồi kỹ thuật trong xu hướng giảm dài hơn là uptrend chắc chắn", vol_ratio 0.23 thấp — tín hiệu kỹ thuật còn non, không phủ nhận. Nhưng bù lại, VRE là mã DUY NHẤT trong nhóm 5 vừa có catalyst FTSE xác nhận, vừa có KQKD cơ bản vượt kế hoạch theo Agent B, mà không kèm cảnh báo rủi ro pháp lý/đòn bẩy nào (khác VIC — nợ vay quốc tế; khác GAS/GVR — rủi ro công ty đại chúng). SL ở 24.320đ (~-5%) và time-stop 25 ngày giới hạn thiệt hại nếu đà hồi kỹ thuật thất bại.

---

## 3) GAS

**Luận điểm mua:** Agent A chấm GAS là "setup kỹ thuật tốt nhất nhóm" (6.5/10) — breakout rõ từ đáy 65k (7/26) lên 88.7k, MA20/MA50 dốc lên, vol_ratio 0.76 **cao nhất nhóm 5 mã** (dù vẫn dưới 1). Agent B ghi nhận nền tảng kinh doanh 7 tháng đầu 2026 rất mạnh: doanh thu hợp nhất +39% YoY, lợi nhuận trước thuế +20% YoY, cộng với cổ tức tiền mặt 25% (2.500đ/cp, tổng ~6.032 tỷ đồng) đang chi trả từ 9/9 đến 20/11/2026.

**Catalyst:** Kết quả kinh doanh tăng trưởng mạnh + dòng tiền cổ tức tiền mặt lớn đang chi trả trong đúng giai đoạn nắm giữ (Agent B).

**Kịch bản giá tới TP +8% (95.796đ, giá hiện tại 88.700đ):** Với vol_ratio cao nhất nhóm và xu hướng breakout được Agent A xác nhận rõ ràng, đây là mã có tín hiệu dòng tiền tương đối tốt nhất trong 5 mã (dù về số tuyệt đối vẫn <1, chưa phải "sôi động" thực sự).

**Rủi ro & vì sao chịu được:** RSI 67.1 gần vùng quá mua (theo A) — rủi ro điều chỉnh trước khi chạm TP là có thật, thừa nhận thẳng. Agent B cũng nêu rủi ro pháp lý: GAS công bố không còn đáp ứng điều kiện công ty đại chúng, và GAS không nằm trong rổ FTSE đợt này — đây là điểm yếu thật, không có catalyst dòng vốn ngoại bù đắp. Cơ chế bảo vệ: SL ở 84.265đ (~-5%) và time-stop 25 ngày giới hạn thiệt hại nếu RSI cao dẫn đến điều chỉnh sớm; cổ tức tiền mặt chi trả trong đúng giai đoạn nắm giữ phần nào bù đắp dòng tiền nếu giá điều chỉnh ngắn hạn quanh ngày GDKHQ (dù giá tham chiếu sẽ giảm tương ứng theo thông lệ chia cổ tức, như Agent B lưu ý).

---

## Phản biện trước (chuẩn bị cho Agent D)

- "Vol_ratio cả nhóm đều <1" (Agent A) — đúng, không mã nào có dòng tiền "sôi động" theo đúng nghĩa; nhưng GAS (0.76) và VRE tương đối khá hơn VIC (0.10) trong nhóm, và catalyst FTSE (VIC, VRE) là yếu tố ngoại lực có thể kéo dòng tiền vào bất kể vol_ratio quá khứ.
- "Model AUC yếu 0.53–0.55" — đúng, nên luận điểm bò ở đây dựa vào catalyst tin tức (FTSE, KQKD, cổ tức) + kỹ thuật cụ thể của A, không dựa vào score mô hình làm căn cứ chính.
- "VIC/VRE mới cắt lên MA50, chưa chắc bền" (Agent A) — thừa nhận, đây là lý do SL/time-stop tồn tại; luận điểm bò không phủ nhận rủi ro này mà dựa vào catalyst FTSE có mốc thời gian cụ thể (21/9) để tạo xác suất thành công cao hơn trong khung 25 ngày.

---

**Kèo bò tự tin nhất:** VRE — hội tụ đồng thời catalyst FTSE xác nhận và KQKD cơ bản vượt kế hoạch thực chất (theo Agent B), mà không vướng rủi ro pháp lý/đòn bẩy nào như VIC (nợ vay quốc tế) hay GAS (rủi ro công ty đại chúng), dù kỹ thuật mới chỉ vừa xác nhận và cần SL/time-stop bảo vệ chặt.

KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — đây là luận điểm một chiều (phe bò) để phục vụ tranh luận nội bộ, mô hình nền có edge yếu (AUC ~0.53–0.55), cần đối chiếu với Agent D (gấu) và quyết định cuối của Agent E trước khi coi là bất kỳ dạng khuyến nghị nào.


---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

### 🐻 Agent D — Tổng hợp hướng GẤU + phản biện · 2026-09-15 05:45

Ghi chú mở đầu: nhắc lại bối cảnh whiteboard — mô hình tốt nhất OOS (LogReg) có **base win-rate 0.357, THẤP HƠN buy&hold kỳ kiểm định (0.3824)**. Nói cách khác, trên chính tập dữ liệu kiểm định, "ngồi im mua giữ" còn thắng nhiều hơn tín hiệu mô hình. Đây là điểm mấu chốt bị Agent C bỏ qua khi liên tục nhấn mạnh catalyst tin tức "bù" cho score yếu — score yếu không chỉ là "không đủ mạnh để mua một mình" như C thừa nhận, mà thực chất là **âm** so với baseline thụ động.

---

## Phản biện Agent C

### VIC
- **Agent C cho rằng** vùng kháng cự TP +8% (260.820đ) "đã có thanh khoản thực tế trước đó" (từng chạm ~266k) nên dễ vượt hơn một đỉnh hoàn toàn mới. **Nhưng** chính diễn biến đó — giá chạm ~266k rồi bị bán mạnh, có phiên đảo chiều giảm hơn 4,3% ngay trong ngày (theo Agent B) — là bằng chứng CUNG áp đảo tại vùng đó gần đây, không phải tín hiệu trung lập. Với vol_ratio chỉ 0.10 (thấp nhất nhóm 5 mã, theo Agent A), khi giá quay lại thử vùng 260k, lực cầu nhiều khả năng còn yếu hơn lần thất bại gần nhất.
- **Agent C cho rằng** dòng vốn ngoại/tự doanh mua ròng ngày 10/9 là dấu hiệu "dòng tiền đi trước sự kiện" ủng hộ giá. **Nhưng** danh mục FTSE thường được thị trường biết trước ngày hiệu lực khá lâu — nếu dòng tiền đã mua trước, rất có thể phần lớn kỳ vọng nâng hạng đã được phản ánh vào giá trước 21/9, tạo rủi ro kinh điển "buy the rumor, sell the news": đúng lúc catalyst chính thức có hiệu lực (nằm giữa khung time-stop 25 phiên) lại là lúc lực bán chốt lời xuất hiện, giống hệt mẫu hình giảm hơn 4,3%/phiên vừa xảy ra ở đỉnh 266k.
- **Agent C gạt** rủi ro đòn bẩy từ phát hành trái phiếu quốc tế 455 tỷ won (~8.050 tỷ đồng) là "rủi ro cấu trúc dài hạn, ngoài khung 25 ngày". **Nhưng** thị trường thường định giá lại rủi ro pha loãng/chi phí lãi vay ngay khi có tin liên quan (kể cả tin phát hành trong tương lai), không đợi đến khi trái phiếu thực sự giải ngân — đây là rủi ro tâm lý có thể kích hoạt bất cứ lúc nào trong 25 ngày nắm giữ, không thể loại trừ khỏi khung thời gian một cách chắc chắn.
- Bổ sung: VIC vừa cho thấy biên độ dao động một phiên >4,3% (theo B) — với SL đặt ở -5% (229.425đ), chỉ cần 1-2 phiên biến động mạnh theo chiều bất lợi là có thể chạm SL, bất kể xu hướng dài hạn "đẹp" theo A.

### VRE
- **Agent C chọn VRE là "kèo bò tự tin nhất"**, dựa trên hội tụ catalyst FTSE + KQKD vượt kế hoạch, không vướng rủi ro pháp lý/đòn bẩy. **Nhưng** chính Agent A đã cảnh báo thẳng đây là "hồi kỹ thuật trong xu hướng giảm dài hơn là uptrend chắc chắn" — nhìn dài hạn, VRE vẫn đang phục hồi từ đáy 21,5k (8/26) sau khi giảm từ đỉnh 36k (5/26), tức đã mất ~40% trước khi hồi về 25.600đ hiện tại. "Mới cắt lên MA50" là dạng tín hiệu dễ bị whipsaw (cắt lên rồi cắt xuống lại) nhất trong các loại tín hiệu kỹ thuật, không phải xác nhận xu hướng.
- **Agent C dùng RSI 49,8 "trung tính" như một điểm cộng** (còn dư địa tăng). **Nhưng** RSI trung tính cũng có thể đọc theo hướng ngược lại: sau một nhịp hồi, giá chưa tạo đủ động lượng để RSI vượt hẳn lên vùng tích cực (>55-60) — nghĩa là lực mua chưa đủ thuyết phục để khẳng định xu hướng giảm dài hạn đã đảo chiều.
- **Agent C nhấn mạnh** VRE là mã Small Cap FTSE, "không rủi ro pháp lý/đòn bẩy nào" — nhưng đây là lập luận từ *sự vắng mặt* của tin xấu, không phải bằng chứng về sức mạnh dòng tiền. vol_ratio của VRE chỉ 0.23 — vẫn rất thấp; danh mục Small Cap trong đợt nâng hạng thường nhận phân bổ vốn thụ động nhỏ hơn nhiều so với Large Cap (VIC), nên kỳ vọng "dòng vốn ngoại kéo giá" cho VRE cần được chiết khấu so với VIC, chứ không nghiễm nhiên là "chắc ăn hơn".
- Catalyst FTSE cho VRE và VIC là **cùng một sự kiện** (hiệu lực 21/9/2026) — nếu đây là kiểu "sell the news" như phân tích ở trên, hai trong ba mã bò của Agent C (VIC, VRE) sẽ thất bại đồng thời, không phải hai cơ hội độc lập. Danh mục bò của C có rủi ro tập trung catalyst mà C không nêu.

### GAS
- **Agent C xếp GAS là "setup kỹ thuật tốt nhất nhóm"** dựa trên breakout rõ + vol_ratio cao nhất nhóm (0,76). **Nhưng** chính Agent A cũng ghi rõ RSI 67,1 "gần vùng quá mua" sau khi giá đã tăng từ đáy 65k lên 88.700đ — tức đã tăng khoảng +36% trong một nhịp. Mua đuổi ở gần vùng quá mua sau một đợt tăng mạnh như vậy là rủi ro thực, và vol_ratio 0,76 dù cao nhất nhóm vẫn **dưới 1**, nghĩa là khối lượng vẫn dưới trung bình — không đủ để coi là xác nhận dòng tiền mạnh, chỉ là "đỡ tệ nhất" trong một nhóm toàn yếu.
- **Agent C thừa nhận** rủi ro pháp lý "công ty đại chúng" của GAS (chỉ ~4,24% cổ phần biểu quyết do cổ đông nhỏ nắm giữ, dưới ngưỡng luật định) là "điểm yếu thật, không có catalyst bù đắp", nhưng vẫn xếp GAS ngang hàng VIC/VRE trong luận điểm mua. Đây là rủi ro quản trị/pháp lý có thể ảnh hưởng tâm lý nhà đầu tư bất kỳ lúc nào nếu có thêm công bố bất lợi (theo Agent B, GVR/PV GAS đối mặt nguy cơ hủy niêm yết bắt buộc nếu không khắc phục — mốc thời hạn cụ thể "chưa kiểm chứng").
- **Agent C coi cổ tức tiền mặt 25% là yếu tố "bù đắp dòng tiền"** nếu giá điều chỉnh quanh ngày GDKHQ. **Nhưng** đây thực chất là một đợt giảm giá tham chiếu **cơ học chắc chắn sẽ xảy ra** trong đúng khung nắm giữ 25 ngày (GDKHQ ước quanh 23/9, theo B — ngày chính xác "chưa kiểm chứng"), không phải rủi ro xác suất — nó tự động kéo giá xuống một khoảng tương ứng cổ tức (2.500đ/cp, ~2,8% giá hiện tại) ngay khi RSI đang ở vùng nhạy cảm gần quá mua, làm tăng khả năng chạm SL sớm nếu đà tăng chững lại đúng lúc.
- GAS không nằm trong rổ FTSE — thiếu hẳn "tấm đệm" dòng vốn ngoại thụ động mà VIC/VRE có, trong khi lại cộng thêm rủi ro pháp lý riêng. Đây là mã có **risk-adjusted case yếu nhất trong 3 mã bò của C**, dù kỹ thuật thuần túy (theo A) là đẹp nhất nhóm.

---

## Rủi ro downside theo mã

- **PNJ**: rủi ro rõ nhất và đã hiện thực hóa — lỗ ròng quý 2 kỷ lục (283 tỷ), dự phòng lũy kế 2.267 tỷ đồng cho vụ "P-Lab" chưa xử lý dứt điểm (theo B), giá đang dưới MA50 trong downtrend dốc (từ ~80k về 36.750đ, theo A) — đúng mẫu hình "bắt dao rơi" mà cả A lẫn C đều loại khỏi rổ mua. BCTC Q3 (26/10/2026) sẽ đánh giá lại tồn kho kim cương, có thể phát sinh thêm biến động mạnh hai chiều. Nếu giá tiếp tục giảm về sát/dưới SL mô hình (34.912đ, khoảng -5%), rủi ro trượt giá (gap down) khi có tin xấu là có thật.
- **GVR**: không có catalyst tích cực rõ ràng (không thuộc rổ FTSE), giá đi ngang sát vùng giao cắt MA20/MA50 sau downtrend, RSI dưới 50, vol_ratio thấp (0,15) — đúng như A/C đã loại. Thêm rủi ro pháp lý cổ đông nhỏ tương tự GAS.
- **VIC**: biến động một phiên >4,3% đã xảy ra gần đây; nếu vùng 260k tái lập vai trò kháng cự, kịch bản quay đầu về sát/dưới SL (229.425đ) trong khung 25 ngày là hoàn toàn khả dĩ, đặc biệt nếu FTSE là "sell the news".
- **VRE**: nếu nhịp hồi kỹ thuật thất bại (giống các lần hồi trước trong downtrend 5/26→8/26), giá có thể cắt xuống lại dưới MA50 nhanh, chạm SL 24.320đ; vol_ratio 0,23 không đủ xác nhận dòng tiền bền vững.
- **GAS**: rủi ro điều chỉnh kỹ thuật từ vùng gần quá mua (RSI 67) cộng dồn với giảm giá cơ học quanh ngày GDKHQ cổ tức — hai lực giảm giá trùng thời điểm trong cùng khung nắm giữ.
- **Rủi ro hệ thống chung** (chưa kiểm chứng số liệu cụ thể trong lần tra cứu này, nêu để lưu ý): biên độ dao động ±7% của HOSE có thể khuếch đại biến động hai chiều trong một phiên; rủi ro margin call/giải chấp trên diện rộng nếu thị trường điều chỉnh quanh sự kiện FTSE; cơ chế T+2 khiến nhà đầu tư có thể "kẹp hàng" 2 ngày không bán được nếu giá giảm ngay sau khi khớp lệnh. Đây là rủi ro cấu trúc thị trường, áp dụng cho cả 5 mã, không riêng mã nào.

## Mã nên tránh

1. **PNJ — rủi ro cao nhất, nên tránh rõ ràng nhất**: cả A (downtrend dưới MA50, "bắt dao rơi") và B (lỗ kỷ lục, dự phòng chưa dứt điểm, chờ BCTC Q3) đều chỉ ra rủi ro cụ thể, không phải suy đoán.
2. **GVR — tránh vì thiếu catalyst và setup kỹ thuật yếu**: không có điểm mạnh nào đủ rõ để bù rủi ro pháp lý cổ đông nhỏ.
3. Trong 3 mã Agent C chọn mua, nếu buộc phải xếp hạng rủi ro thấp→cao theo phản biện trên: **GAS rủi ro-điều chỉnh-kỹ thuật cao nhất trong ngắn hạn** (RSI gần quá mua + giảm giá cơ học do cổ tức trùng thời điểm), còn **VIC và VRE cùng phụ thuộc một catalyst duy nhất (FTSE 21/9)** nên rủi ro của hai mã này có tương quan cao, không nên coi là hai lựa chọn độc lập giảm thiểu rủi ro danh mục.

## Nhắc lại giới hạn mô hình

Mô hình nền có **edge yếu (AUC ~0,53–0,55)**, và quan trọng hơn: base win-rate của mô hình tốt nhất (LogReg, 0,357) **thấp hơn** buy&hold trên tập kiểm định (0,3824). Toàn bộ luận điểm bò của Agent C — dù có catalyst tin tức thật — vẫn được dựng trên nền một mô hình dự báo có xác suất đúng thấp hơn việc không làm gì cả. Catalyst tin tức (FTSE, KQKD, cổ tức) là có thật và đáng cân nhắc, nhưng không nên diễn giải thành "xác suất thành công cao hơn" theo cách Agent C ngụ ý — đó là tự tin thái quá dựa trên một edge thống kê rất mỏng, dễ bị nhiễu bởi biến động ngắn hạn của từng mã.

---

KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — đây là luận điểm một chiều (phe gấu) nhằm stress-test luận điểm bò của Agent C để Agent E ra quyết định cuối cùng, không phải khuyến nghị mua/bán bất kỳ mã nào; các suy đoán về diễn biến giá tương lai (vd. "sell the news") được ghi rõ là giả định logic, không phải dữ kiện đã xảy ra.


---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*

### 🎩 Agent E — Giám đốc Chiến lược · 2026-09-15 06:00

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| **VRE** | THEO DÕI | TB | Tin tức tốt nhất nhóm + catalyst FTSE, nhưng kỹ thuật mới cắt MA50 và vol_ratio thấp — chưa đủ xác nhận để vào lệnh. |
| **VIC** | THEO DÕI | TB | Catalyst FTSE thật nhưng vol_ratio 0.10 + đã có phiên đảo chiều >4,3% tại vùng TP — rủi ro "sell the news", tương quan catalyst với VRE. |
| **GAS** | THEO DÕI | TB | Kỹ thuật/cơ bản tốt nhất nhóm nhưng RSI gần quá mua + giảm giá cơ học do cổ tức trùng khung nắm giữ, không có catalyst FTSE bù đắp. |
| **GVR** | TRÁNH | Cao | Không catalyst, kỹ thuật yếu, rủi ro pháp lý cổ đông nhỏ. |
| **PNJ** | TRÁNH | Cao | Downtrend dốc dưới MA50, lỗ kỷ lục quý 2, dự phòng chưa dứt điểm. |

**Stance danh mục: Thận trọng.** Mô hình nền có edge yếu và base win-rate thấp hơn buy-and-hold trên tập kiểm định; bò và gấu cân bằng nhau ở cả 3 mã có luận điểm mua (VIC/VRE/GAS) nên mặc định THEO DÕI thay vì MUA, ưu tiên bảo toàn vốn. Không giải ngân mới nhóm này ở thời điểm hiện tại; chỉ xem xét vào lệnh nhỏ (2–3%/mã) nếu có xác nhận dòng tiền/giá sau sự kiện FTSE 21/9/2026.

Chi tiết đầy đủ: `debate/DECISION.md`.

KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.

