# 🧑‍⚖️ WHITEBOARD — Tranh luận đa tác nhân về cơ hội swing (as-of 2026-09-14)

*Board tạo lúc 2026-09-14 05:13:23. Đây là bảng chung: **mỗi agent viết ý kiến của mình lên đây, ai cũng đọc được**, mỗi khối
ý kiến ghi rõ tên agent. Không phải khuyến nghị đầu tư.*

## 📌 Bối cảnh (do quant pipeline sinh ra)
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · buy&hold kỳ kiểm định **0.3938**.
- Quy tắc "sóng": vào tại giá đóng cửa → **chốt lời +8% / cắt lỗ −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ Edge mô hình YẾU (AUC ~0.53–0.55). Tranh luận này để *bổ sung* góc nhìn kỹ thuật + tin tức, không thay quản trị rủi ro.

## 🎯 Ứng viên tranh luận (top 5 theo score): VIC, PNJ, VRE, GVR, GAS
| # | Mã | Ngành | Giá (VND) | Score | Chốt lời +8% | Cắt lỗ −5% | RSI | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | **VIC** | RealEstate | 238,100 | 0.58 | 257,148 | 226,195 | 57 | ↑ trên MA50 |
| 2 | **PNJ** | Retail/Consumer | 36,550 | 0.57 | 39,474 | 34,722 | 40 | ↓ dưới MA50 |
| 3 | **VRE** | RealEstate | 25,350 | 0.55 | 27,378 | 24,082 | 48 | ↑ trên MA50 |
| 4 | **GVR** | Materials | 30,550 | 0.54 | 32,994 | 29,022 | 45 | ↑ trên MA50 |
| 5 | **GAS** | Energy | 85,200 | 0.54 | 92,016 | 80,940 | 61 | ↑ trên MA50 |

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

### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-09-14 05:14

| Mã | Trend (MA20/50) | RSI(14) | vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **GAS** | ↑ trên MA50, giá bám sát MA20 | 60.7 (trung tính, gần vùng mua quá) | 0.615 (yếu, nhưng cao nhất nhóm) | **6/10** | Uptrend rõ nhất nhóm, đang consolidating quanh 82-87k sát đỉnh cũ (~95k tháng 5). TP +8% (92,016) chưa gặp kháng cự rõ trên chart gần đây, SL (80,940) trùng vùng MA20/50 hỗ trợ — R:R hợp lý. Volume vẫn dưới trung bình dù cao nhất nhóm. |
| **VIC** | ↑ trên MA50 nhưng đang pullback 3 phiên gần nhất từ đỉnh ~265k | 57.2 (trung tính) | 0.189 (**rất yếu**) | **5.5/10** | Uptrend trung hạn mạnh (từ ~145k → 260k) nhưng entry rơi đúng nhịp điều chỉnh sau khi giá đã chạy xa MA20. Volume cực thấp → tín hiệu thiếu xác nhận dòng tiền. SL (226,195) gần vùng đi ngang cũ 220-226k, hợp lý; nhưng nếu pullback tiếp diễn, dễ chạm SL trước khi hồi. |
| **GVR** | ↑ trên MA50, vừa bật từ đáy nhưng 2 phiên gần nhất giảm mạnh về sát MA50 | 45.1 (trung tính) | 0.339 (yếu) | **5/10** | Giá đang test lại hỗ trợ MA50 (~30-31k) sau nhịp tăng ngắn từ 28k lên 34k — chưa rõ giữ được hỗ trợ hay không. TP (32,994) trùng vùng đỉnh gần nhất (kháng cự), SL (29,022) dưới hỗ trợ MA50 — R:R chấp nhận được nhưng setup chưa xác nhận. |
| **VRE** | ↑ theo nhãn trend_up nhưng MA50 đang cắt xuống dần, giá nằm sát/dưới MA50 | 47.7 (trung tính) | 0.390 (yếu) | **4.5/10** | Chart cho thấy giá đi ngang/giằng co quanh MA50 sau downtrend từ đỉnh 36k (tháng 5) — chưa có xác nhận breakout rõ ràng, MA50 vẫn dốc xuống. Volume yếu. |
| **PNJ** | ↓ dưới MA50, MA50 dốc xuống rõ | 40.2 (trung tính-yếu) | 0.491 (yếu) | **3/10** | Downtrend rõ 6 tháng (77k → 36k), giá vừa bật nhẹ từ đáy nhưng vẫn dưới MA50 đang giảm — dạng "bắt dao rơi" tiềm ẩn. TP +8% (39,474) rơi đúng vùng MA50 đang là kháng cự động → dễ bị chặn trước khi đạt mục tiêu. Setup kỹ thuật yếu nhất nhóm. |

**Nhận định chung (thuần kỹ thuật, không xét tin tức/định giá):**
- Setup kỹ thuật tốt nhất nhóm là **GAS**: xu hướng tăng ổn định nhất, RSI chưa quá mua, volume (dù vẫn yếu) cao nhất trong 5 mã.
- Setup tệ nhất là **PNJ**: đang dưới MA50 trong downtrend dài hạn, mục tiêu chốt lời trùng kháng cự động (MA50) — rủi ro kỹ thuật cao nhất là "bắt dao rơi".
- Rủi ro kỹ thuật lớn nhất chung của cả nhóm: **vol_ratio < 1 ở tất cả 5 mã** — không mã nào có xác nhận dòng tiền mạnh, nghĩa là các tín hiệu breakout/pullback đều thiếu sự đồng thuận của khối lượng.
- **VIC** và **GVR** đều đang trong nhịp điều chỉnh ngắn hạn ngay tại điểm vào lệnh — chưa rõ đã tạo đáy hay chưa, cần theo dõi thêm 1-2 phiên tới (dữ liệu hiện tại chưa đủ để khẳng định, "chưa kiểm chứng").
- **VRE** là setup mơ hồ nhất: nhãn trend_up=True nhưng hình thái giá cho thấy MA50 vẫn đang dốc xuống — mâu thuẫn giữa nhãn và quan sát trực quan trên chart.
- Toàn bộ đánh giá trên là **xác suất**, dựa trên mô hình có edge yếu (AUC ~0.53-0.55); không nên xem là chắc chắn.

KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — chỉ là phân tích kỹ thuật độc lập, không xét tin tức/định giá cơ bản.

### 🅱️ Agent B — Phân tích News / Cơ bản · 2026-09-14 09:30

## VIC — Vingroup

- KQKD 6 tháng đầu năm 2026: lợi nhuận sau thuế gần 20.905 tỷ đồng, tăng 360,5% svck; đã đạt ~60% kế hoạch lợi nhuận cả năm (kế hoạch 2026: DT 485.000 tỷ, LNST 35.000 tỷ). **Tích cực.** ([cafef.vn](https://cafef.vn/chuyen-gi-vua-xay-ra-voi-co-phieu-vingroup-188260907154438857.chn))
- Phiên 7/9/2026: VIC đảo chiều giảm hơn 4,3%, đóng cửa 245.000đ/cp sau chuỗi tăng ~30% kể từ giữa tháng 8 — áp lực chốt lời kỹ thuật, không phải tin xấu cơ bản. So với đầu năm vẫn +44%. **Trung tính/thận trọng ngắn hạn.** ([cafef.vn](https://cafef.vn/chuyen-gi-vua-xay-ra-voi-co-phieu-vingroup-188260907154438857.chn))
- Giữa tháng 8/2026: Vingroup thông qua kế hoạch phát hành trái phiếu quốc tế tới 455 tỷ won Hàn Quốc (~8.050 tỷ đồng) — cần theo dõi rủi ro pha loãng/đòn bẩy nợ. **Trung tính, cần theo dõi.** ([Investing.com](https://vn.investing.com/news/stock-market-news/vic-co-the-bi-ban-rong-hon-1500-ty-dong-trong-dot-co-cau-etf-thang-9-2707619))
- VIC nằm trong danh sách 27 mã được FTSE đưa vào rổ FTSE Global Equity Index Series đợt nâng hạng 21/9/2026, thuộc nhóm large-cap và cũng được thêm trực tiếp vào FTSE All-World — dòng vốn thụ động có thể đổ vào. Tuy nhiên cũng có báo cáo VIC có thể bị **bán ròng hơn 1.500 tỷ đồng** trong đợt cơ cấu ETF quý 3/2026 (MSCI/FTSE frontier cũ) trước khi hiệu lực nâng hạng. Hai chiều tác động đan xen — **hỗn hợp, chưa rõ chiều ròng**. ([Investing.com](https://vn.investing.com/news/stock-market-news/vic-co-the-bi-ban-rong-hon-1500-ty-dong-trong-dot-co-cau-etf-thang-9-2707619), [Dân trí](https://dantri.com.vn/kinh-doanh/27-co-phieu-viet-nam-vao-ro-chi-so-moi-noi-cua-ftse-nang-hang-co-hieu-luc-tu-219-20260821192938821.htm))

## PNJ — Vàng bạc Đá quý Phú Nhuận

- KQKD Q1/2026: doanh thu thuần 17.245 tỷ đồng (+79% svck), vượt ~27% kỳ vọng của VDSC. Mảng vàng 24K/vàng miếng tăng trưởng đột biến; biên lãi gộp mảng bán lẻ trang sức cải thiện lên 31,5% dù biên gộp toàn công ty giảm (22%→18,2%) do tỷ trọng vàng miếng tăng. **Tích cực nhưng có yếu tố pha loãng biên lợi nhuận.** ([Vietstock](https://finance.vietstock.vn/bao-cao-phan-tich/20335/pnj-bao-cao-cap-nhat-kqkd-q12026.htm), [Elibook](https://elibook.vn/2026/05/22/pnj-huong-loi-tu-viec-siet-va-kiem-tra-thi-truong-vang-bien-loi-nhuan-gop-duoc-cai-thien-sau-khi-dam-bao-nguon-nguyen-lieu-dau-vao.html/))
- Hai công ty chứng khoán (VDSC, Vietcap) đưa khuyến nghị MUA với giá mục tiêu lần lượt 90.400đ và 88.900đ/cp (báo cáo tháng 5-7/2026) — **lưu ý đây là quan điểm của CTCK, không phải khuyến nghị của Agent B**. **Tích cực (theo nguồn thứ ba).** ([VDSC](https://vdsc.com.vn/data/api/app/file-storage/8c93e350-5ab8-4576-92d0-08de8de9e4f5/PNJ_Company%20Report_2026_VIE.pdf))
- Kế hoạch cổ tức tiền mặt tỷ lệ 10% cho Quý 3/2026 — ngày GDKHQ cụ thể **chưa kiểm chứng** (không tìm thấy công bố chính thức về ngày chốt quyền). **Trung tính.** ([Elibook](https://elibook.vn/2026/05/22/pnj-huong-loi-tu-viec-siet-va-kiem-tra-thi-truong-vang-bien-loi-nhuan-gop-duoc-cai-thien-sau-khi-dam-bao-nguon-nguyen-lieu-dau-vao.html/))
- PNJ **không xuất hiện** trong danh sách 27 mã FTSE công bố đợt nâng hạng 21/9/2026 → không có catalyst dòng vốn ETF thụ động trực tiếp. **Trung tính/hơi tiêu cực (thiếu catalyst).** ([Vietstock](https://vietstock.vn/2026/09/126-co-phieu-viet-nam-roi-ftse-frontier-sau-khi-duoc-nang-hang-3358-1488491.htm))

## VRE — Vincom Retail

- ĐHĐCĐ 2026: kế hoạch lãi ~5.375 tỷ đồng (+15% svck), doanh thu 10.132 tỷ đồng (+16%); Q1/2026 đã đạt ~30% kế hoạch lợi nhuận, lãi hơn 1.600 tỷ đồng; doanh thu hợp nhất điều chỉnh Q1 tăng 20,7% svck, khách đến TTTM tăng 13-15%. **Tích cực.** ([Tin nhanh chứng khoán](https://www.tinnhanhchungkhoan.vn/vincom-retail-vre-dat-muc-tieu-doanh-thu-10132-ty-dong-nam-2026-post388253.html), [24hmoney](https://24hmoney.vn/news/vincom-retail-vre-bao-lai-hon-1-600-ty-dong-trong-quy-i-2026-c1a2777434.html))
- Cổ tức tiền mặt 10% (1.000đ/cp), tổng chi ~2.272 tỷ đồng, dự kiến thanh toán Quý 3/2026 — ngày GDKHQ cụ thể **chưa kiểm chứng**. **Tích cực (dòng tiền cổ đông) nhưng thiếu ngày chốt cụ thể.** ([baophapluat.vn](https://baophapluat.vn/dhdcd-vincom-retail-vre-2026-ke-hoach-lai-5-375-ty-dong-chot-chia-co-tuc-tien-mat-ty-le-10.html))
- Chiến lược mới: ra mắt thương hiệu "Vincom Collection" (mô hình phố mua sắm ngoài trời gắn với đô thị Vinhomes) theo cơ chế nhận hoa hồng từ chủ đầu tư thay vì tự bỏ vốn — mở rộng quy mô mà không tăng nợ/vốn đầu tư nhiều. Tỷ lệ lấp đầy hệ thống TTTM ~88%, còn ~12% dư địa khai thác. **Tích cực.** ([baodautu.vn](https://baodautu.vn/vincom-retail-dat-muc-tieu-tro-thanh-nha-phat-trien-va-quan-ly-bat-dong-san-ban-le-hang-dau-chau-a-d576238.html))
- VRE nằm trong danh sách 27 mã FTSE đợt nâng hạng 21/9/2026, thuộc nhóm small-cap (theo phân loại FTSE cho khu vực APAC ex-Nhật/Trung) — có thể hưởng dòng vốn ETF thụ động khi hiệu lực từ 21/9/2026. **Tích cực (catalyst gần).** ([Dân trí](https://dantri.com.vn/kinh-doanh/27-co-phieu-viet-nam-vao-ro-chi-so-moi-noi-cua-ftse-nang-hang-co-hieu-luc-tu-219-20260821192938821.htm))

## GVR — Tập đoàn Công nghiệp Cao su Việt Nam

- KQKD Q1/2026: doanh thu ~8.845 tỷ đồng (+56% svck), LNST hơn 2.500 tỷ đồng (+85% svck) — mức lợi nhuận cao nhất gần 5 năm; mủ cao su đóng góp 84% doanh thu; thu nhập khác (thanh lý cây, bồi thường đất phục vụ KCN) tăng hơn 270%. **Tích cực.** ([24hmoney](https://24hmoney.vn/news/co-phieu-gvr-duy-tri-da-tang-tu-mang-nao-trong-nam-2026-c1a2698968.html))
- ĐHĐCĐ (tháng 6/2026): giá cao su dự báo tiếp tục tăng 5-10% trong năm 2026; nhiều khu công nghiệp bắt đầu triển khai đầu tư từ Q3 — câu chuyện chuyển đổi đất cao su sang đất công nghiệp là động lực dài hạn thay đổi cơ cấu lợi nhuận. **Tích cực (dài hạn).** ([Vietstock](https://vietstock.vn/2026/06/dhdcd-gvr-gia-cao-su-con-tang-trien-khai-dau-tu-nhieu-khu-cong-nghiep-tu-quy-3-737-1455245.htm))
- **Rủi ro pháp lý cơ cấu cổ đông**: Bộ Tài chính nắm 96,8% vốn GVR; theo Luật Chứng khoán sửa đổi (hiệu lực 01/01/2025), công ty đại chúng phải có tối thiểu 10% cổ phiếu biểu quyết do ≥100 NĐT nhỏ lẻ nắm giữ. Nếu không khắc phục trong 1 năm (Nhà nước không thoái vốn xuống dưới 90%), GVR có thể bị buộc **hủy tư cách công ty đại chúng**. **Tiêu cực/rủi ro đáng chú ý**, cùng rủi ro pha loãng-điều tra sai phạm được nêu trong báo cáo tháng 3/2026 (Elibook) — **chưa kiểm chứng chi tiết vụ điều tra**. ([Elibook](https://elibook.vn/2026/03/16/gvr-co-phieu-chu-ky-hang-hoa-hap-dan-khi-cao-su-tang-nho-xung-dot-my-iran-ap-luc-rui-ro-sau-dieu-tra-sai-pham-vao-thang-2-2026.html/))
- GVR **không có tên** trong danh sách 27 mã FTSE công bố đợt nâng hạng 21/9/2026 → không có catalyst dòng vốn ETF thụ động trực tiếp từ sự kiện này. **Trung tính (thiếu catalyst gần).**

## GAS — PV Gas (Tổng Công ty Khí Việt Nam)

- KQKD 6 tháng đầu năm 2026: doanh thu ~81.270 tỷ đồng (+46% svck), LNST 9.025 tỷ đồng (+19% svck); kế hoạch cả năm DT 142.000 tỷ, LNTT ~11.200 tỷ, LNST ~9.000 tỷ đồng — 6 tháng đã gần đạt kế hoạch năm. **Tích cực.** ([Báo Pháp luật VN](https://baophapluat.vn/nam-2026-pv-gas-dat-ke-hoach-doanh-thu-khoang-142-000-ty-dong-loi-nhuan-truoc-thue-khoang-11-200-ty-dong.html))
- Cổ tức tiền mặt 2025 tỷ lệ 25% (2.500đ/cp), tổng chi ~6.032 tỷ đồng, **thời gian chi trả 9/9/2026 – 20/11/2026** — sự kiện dòng tiền cổ đông đang diễn ra. **Tích cực.** ([cafef.vn](https://cafef.vn/pv-gas-sap-chi-hon-6000-ty-dong-tra-co-tuc-nam-2025-188260910150319815.chn))
- **Rủi ro cơ cấu cổ đông tương tự GVR**: PV Gas không đáp ứng điều kiện công ty đại chúng (thiếu tỷ lệ cổ phiếu biểu quyết do NĐT nhỏ lẻ nắm giữ theo Luật Chứng khoán sửa đổi); công ty cam kết có 1 năm để khắc phục. **Rủi ro pháp lý/cơ cấu, cần theo dõi.** ([baomoi.com/VnEconomy](https://baomoi.com/pv-gas-co-1-nam-de-dap-ung-dieu-kien-cong-ty-dai-chung-c55961221.epi))
- **Sự kiện sắp tới quan trọng**: ĐHĐCĐ bất thường dự kiến tổ chức **14/9/2026** (trực tuyến, bỏ phiếu điện tử) — đúng ngày as-of của báo cáo này, nội dung nghị quyết **chưa kiểm chứng** tại thời điểm viết. ([danviet.vn](https://danviet.vn/dhdcd-nam-2026-pv-gas-lap-ky-luc-doanh-thu-tuong-duong-11-gdp-ca-nuoc-san-sang-buoc-vao-chu-ky-tang-truong-moi-d1429236.html))
- GAS **không có tên** trong danh sách 27 mã FTSE công bố đợt nâng hạng 21/9/2026. **Trung tính (thiếu catalyst gần từ FTSE).**

## 📅 Sự kiện sắp tới (toàn cảnh)

- **21/9/2026**: FTSE Russell chính thức nâng hạng Việt Nam từ Thị trường Cận biên lên Thị trường Mới nổi thứ cấp (Secondary Emerging Market), triển khai theo 4 giai đoạn tới tháng 9/2027; giai đoạn đầu tỷ trọng cổ phiếu VN vào rổ FTSE EM khoảng 10%. Danh sách 27 mã được đưa vào gồm: VCB, VIC, VHM, BID, HPG, VPB, FPT, GEX, HDB, HCM, MCH, MSN, NVL, SHB, STB, SSB, SSI, TCX, VNM, VCI, VJC, MSB, **VRE**, VPL, VIX, VND, VCK. Trong nhóm 5 ứng viên tranh luận, chỉ **VIC** và **VRE** có tên trực tiếp; PNJ, GVR, GAS không có. ([cafef.vn](https://cafef.vn/chinh-thuc-cong-bo-danh-sach-co-phieu-viet-nam-lot-ftse-global-equity-index-series-188260821182038611.chn), [Dân trí](https://dantri.com.vn/kinh-doanh/27-co-phieu-viet-nam-vao-ro-chi-so-moi-noi-cua-ftse-nang-hang-co-hieu-luc-tu-219-20260821192938821.htm))
- **14/9/2026**: ĐHĐCĐ bất thường PV Gas (GAS) — nội dung chưa kiểm chứng, cần theo dõi công bố sau đại hội.
- **9/9 – 20/11/2026**: PV Gas (GAS) chi trả cổ tức tiền mặt 25% cho năm 2025.
- Quý 3/2026: VRE và PNJ dự kiến chi trả cổ tức tiền mặt tỷ lệ 10% — ngày GDKHQ chính xác **chưa kiểm chứng** cho cả hai mã.
- Sau 1 năm kể từ thời điểm không đáp ứng điều kiện công ty đại chúng (mốc cụ thể chưa kiểm chứng rõ ràng), cả **GVR** và **GAS** đối diện nguy cơ phải nộp hồ sơ hủy tư cách công ty đại chúng nếu Nhà nước (Bộ Tài chính/Ủy ban Quản lý vốn) không thoái vốn xuống dưới 90% — đây là rủi ro cơ cấu mang tính hệ thống cho cả hai mã, không phải tin đồn.

## 🌐 Bối cảnh chung (vĩ mô/ngành)

- Sự kiện lớn nhất chi phối toàn thị trường hiện tại là **nâng hạng FTSE có hiệu lực 21/9/2026**, ước tính thu hút dòng vốn ETF thụ động đáng kể (ước ~1,5 tỷ USD theo một số nguồn), nhưng đi kèm là hoạt động cơ cấu ETF cũ (frontier) có thể gây bán ròng ở một số mã lớn như VIC trong ngắn hạn trước ngày hiệu lực.
- Nhóm **bất động sản** (VIC, VRE, PDR, DXG, KDH, VHM, NLG) hưởng lợi từ KQKD Vingroup/Vinhomes/Vincom Retail tích cực nửa đầu 2026, nhưng cần theo dõi thêm các yếu tố pháp lý dự án và trái phiếu đáo hạn từng doanh nghiệp — **chưa kiểm chứng chi tiết** cho từng mã ngoài VIC/VRE ở trên trong phạm vi tìm kiếm lần này.
- Nhóm doanh nghiệp nhà nước sở hữu chi phối cao (**GVR, GAS**) đối diện rủi ro pháp lý chung về điều kiện duy trì tư cách công ty đại chúng theo Luật Chứng khoán sửa đổi — đây là rủi ro mang tính hệ thống, không phải đặc thù từng doanh nghiệp.
- Không tìm thấy tin tức đáng chú ý về thay đổi room tín dụng ngân hàng hoặc thanh khoản/margin chứng khoán mới trong phạm vi tìm kiếm lần này liên quan trực tiếp đến 5 mã ứng viên — **chưa kiểm chứng**.

## 🏆 Xếp hạng theo hỗ trợ tin tức (mạnh → yếu)

1. **VRE** — KQKD tích cực, cổ tức tiền mặt, chiến lược mở rộng mới, có tên trong danh sách FTSE 21/9 (nhóm small-cap) → catalyst gần nhất rõ ràng nhất.
2. **VIC** — KQKD rất mạnh, có tên trong FTSE large-cap, nhưng có nhiễu ngắn hạn (chốt lời, khả năng bán ròng cơ cấu ETF cũ) và rủi ro phát hành trái phiếu cần theo dõi.
3. **GAS** — KQKD tốt, đang chi trả cổ tức 25% (dòng tiền thực), nhưng có rủi ro cơ cấu cổ đông/công ty đại chúng và không có catalyst FTSE.
4. **PNJ** — KQKD rất mạnh, được CTCK khuyến nghị tích cực, nhưng biên lợi nhuận gộp toàn công ty giảm và không có catalyst FTSE.
5. **GVR** — KQKD tốt và câu chuyện chuyển đổi đất dài hạn hấp dẫn, nhưng rủi ro pháp lý cơ cấu cổ đông (nguy cơ hủy tư cách công ty đại chúng) là yếu tố tiêu cực đáng chú ý nhất trong nhóm 5 mã.

---
*Đây KHÔNG PHẢI là khuyến nghị đầu tư. Toàn bộ thông tin trên tổng hợp từ các nguồn báo chí/công bố công khai tại thời điểm tìm kiếm (14/9/2026); một số chi tiết (ngày GDKHQ cụ thể, nội dung ĐHĐCĐ bất thường GAS) chưa kiểm chứng đầy đủ và có thể thay đổi. Edge mô hình định lượng đi kèm còn YẾU (AUC ~0.53–0.55) — thông tin news/cơ bản ở đây chỉ mang tính bổ sung góc nhìn, không thay thế quản trị rủi ro.*



---

# 🗣️ PHIÊN 2 — LUẬN ĐIỂM BÒ (Agent C)

### 🐂 Agent C — Tổng hợp hướng BÒ · 2026-09-14 05:20

**Lưu ý mở đầu:** Toàn bộ mô hình chấm điểm có edge **YẾU** (AUC ~0.53–0.55, theo cả Agent A và Agent B nhắc lại) — luận điểm dưới đây không dựa vào score đơn thuần mà phải đứng được nhờ sự **hội tụ** giữa kỹ thuật (Agent A) và catalyst tin tức/cơ bản (Agent B). Chọn 3 mã có luận điểm mua thuyết phục nhất: **VIC, GAS, VRE**.

---

## 1. VIC — Vingroup

**Luận điểm mua:**
Theo Agent A, VIC có điểm mô hình cao nhất nhóm ứng viên (score 0.5776, xác suất LogReg 0.62 — signals_latest.csv) và **uptrend trung hạn mạnh nhất về biên độ** (từ ~145k lên đỉnh ~265k). Theo Agent B, KQKD 6 tháng đầu năm 2026 gây ấn tượng mạnh: LNST gần 20.905 tỷ đồng, **tăng 360,5% svck**, đã đạt ~60% kế hoạch lợi nhuận cả năm — đây là tăng trưởng lợi nhuận thực, có công bố, không phải suy đoán.

**Catalyst:**
Agent B xác nhận VIC nằm trong danh sách 27 mã được FTSE đưa vào rổ FTSE Global Equity Index Series (nhóm large-cap) khi Việt Nam chính thức nâng hạng hiệu lực **21/9/2026** — dòng vốn ETF thụ động có thể đổ vào một mã large-cap ngay trước/trong giai đoạn đó. Đây là catalyst có ngày cụ thể, không phải tin đồn.

**Kịch bản giá tới TP (+8%, 257.148đ):**
Agent A ghi nhận VIC đang pullback 3 phiên gần nhất từ đỉnh ~265k sau chuỗi tăng ~30% kể từ giữa tháng 8 (theo B, đây là "áp lực chốt lời kỹ thuật, không phải tin xấu cơ bản"). *Suy luận của Agent C:* nếu KQKD nền tảng vẫn tích cực và catalyst FTSE đến gần, nhịp điều chỉnh hiện tại có thể là vùng tích lũy lại trước khi dòng tiền thụ động và tâm lý nâng hạng hỗ trợ giá tiến về vùng đỉnh cũ và xa hơn. SL (226.195đ) trùng vùng đi ngang cũ 220-226k mà Agent A xác định là hỗ trợ hợp lý — R:R được bảo vệ bởi vùng giá đã kiểm chứng trong quá khứ.

**Rủi ro & vì sao chấp nhận được:**
- Agent A ghi nhận vol_ratio cực thấp (0.189) — dòng tiền xác nhận yếu. *Phản biện trước:* volume thấp trong nhịp điều chỉnh sau một đợt tăng mạnh không hiếm gặp và không tự động nghĩa là đảo chiều; time-stop 25 ngày giới hạn thời gian chịu rủi ro nếu tín hiệu không được xác nhận thêm.
- Agent B nêu khả năng **bán ròng hơn 1.500 tỷ đồng** trong đợt cơ cấu ETF cũ (frontier) trước ngày hiệu lực nâng hạng — đây là rủi ro dòng tiền ngắn hạn có thật, xảy ra *trước* khi dòng vốn mới từ FTSE EM chảy vào. SL đặt dưới vùng hỗ trợ đã giúp giới hạn thiệt hại nếu áp lực bán này kéo giá xuống thêm.
- Kế hoạch phát hành trái phiếu quốc tế ~8.050 tỷ đồng (Agent B) — rủi ro pha loãng/đòn bẩy cần theo dõi, nhưng là kế hoạch huy động vốn cho tăng trưởng, chưa phải sự kiện tiêu cực đã xảy ra.

---

## 2. GAS — PV Gas

**Luận điểm mua:**
Agent A xếp GAS là **setup kỹ thuật tốt nhất nhóm**: xu hướng tăng ổn định nhất, RSI 60.7 chưa vào vùng quá mua, và vol_ratio (0.615) tuy vẫn dưới 1 nhưng **cao nhất trong 5 mã** — nghĩa là dòng tiền, dù chưa mạnh, đồng thuận tốt hơn các mã khác. Agent B xác nhận nền cơ bản vững: doanh thu 6 tháng đầu năm ~81.270 tỷ đồng (+46% svck), LNST 9.025 tỷ đồng (+19% svck), gần đạt kế hoạch năm.

**Catalyst:**
Agent B nêu GAS đang trong giai đoạn **chi trả cổ tức tiền mặt 25%** (tổng ~6.032 tỷ đồng), thời gian chi trả 9/9–20/11/2026 — đây là dòng tiền cổ đông thực đang diễn ra ngay lúc này, không phải kế hoạch xa. Ngoài ra, ĐHĐCĐ bất thường diễn ra đúng ngày 14/9/2026 (hôm nay) — nội dung "chưa kiểm chứng" theo Agent B, nên đây là một sự kiện cần theo dõi chứ chưa thể tính là catalyst tích cực chắc chắn.

**Kịch bản giá tới TP (+8%, 92.016đ):**
Theo Agent A, giá đang consolidating quanh 82-87k, và mục tiêu TP "chưa gặp kháng cự rõ trên chart gần đây" trước khi tới vùng đỉnh cũ ~95k (tháng 5). Với uptrend rõ nhất nhóm theo A, đây là mã có đường đi tới TP sạch nhất về mặt kỹ thuật trong 5 ứng viên.

**Rủi ro & vì sao chấp nhận được:**
- Cả A và B đều lưu ý vol_ratio dưới 1 ở toàn bộ nhóm — GAS không ngoại lệ, dù đỡ yếu nhất. *Phản biện trước:* SL (80.940đ) trùng đúng vùng hỗ trợ MA20/50 mà Agent A xác định, nên nếu volume yếu khiến giá không giữ được xu hướng, hệ thống sẽ cắt lỗ sớm tại vùng đã biết trước, không phải chờ đến khi mất kiểm soát.
- Agent B nêu rủi ro pháp lý cơ cấu cổ đông (nguy cơ mất tư cách công ty đại chúng nếu Nhà nước không thoái vốn dưới 90% trong 1 năm) — đây là rủi ro dài hạn/mang tính hệ thống, không phải sự kiện tức thời trong khung thời gian time-stop 25 ngày của tín hiệu này.
- Không có catalyst FTSE — bù lại bằng catalyst cổ tức đang chi trả thực tế, là dòng tiền có thể xác minh (đã công bố ngày chi trả cụ thể).

---

## 3. VRE — Vincom Retail

**Luận điểm mua:**
Theo Agent B, VRE có **hỗ trợ tin tức mạnh nhất nhóm** (được B xếp hạng #1): KQKD tích cực (kế hoạch lãi ~5.375 tỷ đồng +15% svck, Q1/2026 đã đạt ~30% kế hoạch, khách đến TTTM tăng 13-15%), cổ tức tiền mặt 10% dự kiến Quý 3/2026, và chiến lược mở rộng "Vincom Collection" theo mô hình nhận hoa hồng — mở rộng quy mô mà không tăng nợ/vốn đầu tư nhiều (tỷ lệ lấp đầy hiện ~88%, còn dư địa ~12%).

**Catalyst:**
VRE có tên trong danh sách 27 mã FTSE nâng hạng hiệu lực 21/9/2026 (nhóm small-cap theo B) — cùng với VIC, đây là 1 trong 2 mã ứng viên duy nhất có catalyst dòng vốn thụ động trực tiếp từ sự kiện nâng hạng lớn nhất thị trường hiện tại.

**Kịch bản giá tới TP (+8%, 27.378đ):**
*Suy luận của Agent C:* nếu catalyst FTSE (21/9) và cổ tức Quý 3 hội tụ trong cùng khung thời gian time-stop (25 ngày kể từ 14/9), đây có thể là chất xúc tác đủ để kéo giá dù kỹ thuật chưa xác nhận breakout rõ ràng.

**Rủi ro & vì sao chấp nhận được:**
- Agent A đánh giá đây là setup kỹ thuật **mơ hồ nhất nhóm**: nhãn trend_up=True nhưng MA50 quan sát trên chart vẫn đang dốc xuống — mâu thuẫn giữa nhãn mô hình và hình thái giá thực tế. Đây là điểm yếu thật, không né tránh.
- *Phản biện trước:* SL (24.082đ) và time-stop 25 ngày giới hạn rủi ro nếu setup không xác nhận; đồng thời catalyst FTSE có ngày cụ thể (21/9) nằm gọn trong khung 25 ngày time-stop, nên nếu dòng vốn thụ động thực sự xuất hiện, tín hiệu có thời gian đủ để phản ánh trước khi bị cắt.
- Ngày GDKHQ cổ tức cụ thể "chưa kiểm chứng" theo Agent B — không tính đây là catalyst có ngày chắc chắn, chỉ là yếu tố hỗ trợ chung.

---

## Kèo bò tự tin nhất

Trong 3 mã trên, **VIC** là kèo bò tự tin nhất: đây là mã duy nhất hội tụ đồng thời điểm mô hình cao nhất nhóm (Agent A/signals), tăng trưởng lợi nhuận đột biến có công bố chính thức (+360,5% svck theo Agent B), và catalyst dòng vốn thụ động FTSE có ngày hiệu lực cụ thể (21/9/2026) — dù vẫn phải thừa nhận rủi ro thật từ volume yếu và áp lực bán cơ cấu ETF ngắn hạn.

---
*KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — đây là tổng hợp luận điểm MUA mang tính tranh luận nội bộ (phe Bò) dựa hoàn toàn trên bằng chứng của Agent A và Agent B, đi kèm mô hình định lượng có edge còn YẾU (AUC ~0.53–0.55). Không dùng để ra quyết định giao dịch trực tiếp.*


---

# 🗣️ PHIÊN 3 — LUẬN ĐIỂM GẤU + PHẢN BIỆN (Agent D)

### 🐻 Agent D — Tổng hợp hướng GẤU + phản biện · 2026-09-14 09:50

**Khung tham chiếu:** Toàn bộ mô hình có edge **YẾU** (AUC ~0.53–0.55) — chênh lệch điểm số 0.53–0.58 giữa các mã gần như nằm trong biên độ nhiễu thống kê, không phải khác biệt có ý nghĩa. Mọi lập luận "mã X có điểm cao nhất" dưới đây cần được đọc với tinh thần đó.

---

## Phản biện Agent C

### 1. VIC

- **Agent C cho rằng** VIC là "kèo bò tự tin nhất" vì điểm mô hình cao nhất nhóm (0.5776) và tăng trưởng LNST +360,5% svck. **Nhưng**: điểm ensemble 0.5776 che giấu sự **bất đồng nghiêm trọng giữa các mô hình con** — theo signals_latest.csv, p_LSTM = 0.807 (rất cao) trong khi p_GradBoost chỉ 0.4435 và p_XGBoost chỉ 0.4283, tức **2/4 mô hình cây cho xác suất dưới 0.45 (thiên về không mua)**. Một outlier (LSTM) đang kéo điểm tổng hợp lên; nếu bỏ LSTM ra, VIC không còn là mã dẫn đầu. Đây là dấu hiệu overfitting/model disagreement, không phải sự đồng thuận mạnh.
- **Agent C cho rằng** volume thấp (vol_ratio 0.189) "không hiếm gặp sau nhịp tăng mạnh, không tự động là đảo chiều". **Nhưng**: 0.189 không chỉ là "thấp" — đây là **vol_ratio thấp nhất trong toàn bộ 30 mã của signals_latest.csv**, thấp hơn cả FRT (0.198), STB (0.213). Kết hợp với việc giá vừa giảm hơn 4,3% trong 1 phiên (7/9) ngay sau chuỗi tăng 30%, đây là hình thái **kiệt sức/chốt lời hàng loạt với thanh khoản cạn**, không phải "tích lũy lại" như Agent C suy diễn — và chính C cũng tự thừa nhận đây là "suy luận của Agent C" chứ không phải bằng chứng.
- **Agent C thừa nhận rủi ro** bán ròng >1.500 tỷ đồng từ cơ cấu ETF frontier cũ nhưng cho rằng SL sẽ bảo vệ. **Nhưng** Agent B nói rõ đây là tác động "**hỗn hợp, chưa rõ chiều ròng**" — nếu đợt bán ròng này rơi vào đúng những ngày trước 21/9 (tức nằm gọn trong 1 tuần đầu của time-stop 25 ngày), rủi ro là giá bị ép xuống **trước khi** dòng vốn EM mới kịp vào, đúng lúc thanh khoản đã yếu nhất nhóm — xác suất chạm SL (226.195đ) sớm là có thật, không chỉ là kịch bản xấu ở biên.
- **Agent C nêu** kế hoạch phát hành trái phiếu quốc tế ~8.050 tỷ đồng chỉ là "kế hoạch huy động vốn tăng trưởng, chưa tiêu cực". **Nhưng** việc một công ty vừa báo lãi kỷ lục vẫn cần huy động thêm nợ ngoại tệ quy mô lớn đặt câu hỏi về áp lực dòng tiền/đòn bẩy đi kèm mở rộng — đây là rủi ro pha loãng/lãi suất cần theo dõi, không nên bị gạt sang một bên chỉ vì "chưa xảy ra".
- Catalyst FTSE 21/9 đã được công bố từ 21/8/2026 — gần 1 tháng trước — nên khả năng thị trường đã phản ánh một phần vào đà tăng +30% từ giữa tháng 8 trước khi đảo chiều giảm 4,3%. Đây có dáng dấp kinh điển của "buy the rumor, sell the news", điều Agent C không đề cập.

### 2. GAS

- **Agent C cho rằng** vol_ratio 0.615 "cao nhất nhóm" nghĩa là dòng tiền đồng thuận tốt hơn. **Nhưng** 0.615 vẫn là **dưới 1** — tức khối lượng chỉ bằng 61,5% trung bình; "cao nhất trong nhóm 5 mã tệ" không đồng nghĩa với xác nhận dòng tiền thực sự, đây chính là điều Agent A tự nhận định ("không mã nào có xác nhận dòng tiền mạnh").
- **Agent C cho rằng** ĐHĐCĐ bất thường ngày 14/9 chỉ là "sự kiện cần theo dõi" trung tính. **Nhưng** đây là một AGM **bất thường** (không phải thường niên) diễn ra đúng ngày phát tín hiệu, nội dung hoàn toàn chưa biết — trong bối cảnh Agent B đã chỉ ra GAS đối diện rủi ro pháp lý cơ cấu cổ đông (Nhà nước nắm >90%, phải thoái vốn hoặc mất tư cách công ty đại chúng), một AGM bất thường đúng lúc này hoàn toàn có thể là nơi bàn về chính vấn đề đó. Đây là rủi ro sự kiện nhị phân chưa định giá, không nên coi là trung tính.
- **Agent C tách rủi ro pháp lý cơ cấu cổ đông ra khỏi khung thời gian 25 ngày** ("dài hạn, ngoài time-stop"). **Nhưng** AGM bất thường hôm nay có thể là đúng thời điểm rủi ro này được đưa ra bàn — tức cửa sổ rủi ro và cửa sổ giao dịch trùng nhau, không tách biệt như C giả định.
- Giá đang consolidate quanh 82-87k, sát vùng đỉnh cũ ~95k (tháng 5) — đây cũng có thể là vùng phân phối/kháng cự dài hạn thay vì "đường tới TP sạch" như C mô tả; RSI 60,7 đã ở vùng "gần mua quá" theo chính ghi chú của Agent A.
- Cổ tức 25% "dòng tiền thực" nhưng ngày GDKHQ không được nêu rõ trong ghi chú B — nếu rơi vào giai đoạn nắm giữ, giá sẽ **điều chỉnh kỹ thuật giảm đúng bằng tỷ lệ cổ tức** vào ngày giao dịch không hưởng quyền, có thể bị hiểu nhầm là gãy xu hướng hoặc kích hoạt cắt lỗ giả.

### 3. VRE

- **Agent C tự thừa nhận** đây là setup kỹ thuật "mơ hồ nhất nhóm" (nhãn trend_up=True nhưng MA50 quan sát trên chart vẫn dốc xuống) nhưng vẫn xếp VRE vào top 3 bò nhờ tin tức. **Phản biện**: mâu thuẫn giữa nhãn mô hình và hình thái giá thực tế là dấu hiệu **độ tin cậy của nhãn/tín hiệu có vấn đề** — nếu nhãn trend_up bị sai, toàn bộ cấu trúc TP/SL tính theo % từ giá hiện tại (dựa trên giả định xu hướng tăng) cũng mất cơ sở, không chỉ đơn thuần là "rủi ro chấp nhận được nhờ SL".
- **Agent C tự dùng ngôn ngữ giả định**: "nếu... hội tụ... đây CÓ THỂ là chất xúc tác đủ" — đây là suy đoán có điều kiện, không phải bằng chứng, nhưng vẫn được đưa vào phần "kịch bản giá tới TP" như một luận điểm chính.
- vol_ratio chỉ 0.390 — yếu, thấp hơn cả GAS và GVR trong nhóm 5 mã.
- Ngày GDKHQ cổ tức 10% "chưa kiểm chứng" (theo B) — rủi ro điều chỉnh giá kỹ thuật giống GAS nếu rơi vào thời gian nắm giữ.
- VRE thuộc nhóm FTSE **small-cap**, không phải large-cap như VIC — quy mô dòng vốn thụ động đổ vào nhóm small-cap trong đợt nâng hạng thường nhỏ hơn đáng kể so với kỳ vọng thị trường đặt vào nhóm large-cap; catalyst có thể yếu hơn C ngụ ý khi đặt VRE ngang hàng VIC.
- **Rủi ro tương quan chưa được Agent C nhắc tới**: VRE và VIC đều thuộc hệ sinh thái Vingroup (bất động sản/bán lẻ liên quan Vinhomes-Vingroup). Nếu chọn cả 2 mã này cùng lúc (2/3 mã bò của C), danh mục mất tính phân tán — một tin xấu riêng của nhóm Vingroup (ví dụ liên quan trái phiếu, pháp lý dự án) có thể kéo cả hai xuống đồng thời, khuếch đại rủi ro thay vì giảm.

---

## Rủi ro downside theo mã

- **VIC**: SL 226.195đ (~-5% từ 238.100đ). Kịch bản xấu: bán ròng cơ cấu ETF frontier cũ (đã nêu trong B, "có thể" >1.500 tỷ) trùng thời điểm thanh khoản thấp nhất thị trường (vol_ratio 0.189 — thấp nhất 30 mã) → giá dễ trượt qua vùng hỗ trợ 226-220k nhanh mà không có lực đỡ từ dòng tiền, đặc biệt nếu tâm lý "sell the news" hậu công bố FTSE (đã biết từ 21/8) tiếp diễn sau cú giảm 4,3% ngày 7/9. Rủi ro pha loãng từ phát hành trái phiếu quốc tế là yếu tố trung hạn cần theo dõi thêm, chưa phản ánh vào giá.
- **GAS**: SL 80.940đ. Kịch bản xấu: nội dung ĐHĐCĐ bất thường 14/9 (chưa biết) liên quan đến rủi ro thoái vốn Nhà nước/tư cách công ty đại chúng gây bất ngờ tiêu cực; hoặc giá chạm vùng kháng cự đỉnh cũ ~95k rồi bị bán ra do RSI đã gần vùng quá mua (60,7) kết hợp volume yếu nhất nhóm (dù "cao nhất" trong 5 mã, vẫn <1).
- **VRE**: SL 24.082đ. Kịch bản xấu: MA50 tiếp tục dốc xuống (đúng như quan sát thực tế của Agent A, trái với nhãn mô hình) khiến giá phá xuống dưới SL trước khi catalyst FTSE (21/9, thuộc nhóm small-cap, tác động nhỏ hơn) kịp phát huy; vol_ratio 0.390 không đủ xác nhận bất kỳ đảo chiều nào.
- **GVR** (không được C chọn nhưng nằm trong nhóm 5 ứng viên A/B phân tích): giá đang test lại hỗ trợ MA50 sau 2 phiên giảm mạnh, chưa xác nhận giữ được; đồng thời mang cùng rủi ro pháp lý cơ cấu cổ đông như GAS (Nhà nước giữ 96,8%) — rủi ro kép kỹ thuật + pháp lý.
- **PNJ** (không được C chọn): downtrend 6 tháng rõ ràng (77k→36k), giá dưới MA50 đang giảm, TP trùng đúng kháng cự động MA50 — theo chính Agent A đây là "bắt dao rơi" và là setup kỹ thuật yếu nhất nhóm; không có catalyst FTSE.

## Mã nên tránh

- **Tránh nhất về kỹ thuật thuần túy**: **PNJ** — downtrend dài hạn chưa đảo chiều, giá dưới MA50 dốc xuống, TP đặt ngay tại kháng cự động; đây là kiểu "bắt dao rơi" theo đúng nhận định của Agent A.
- **Tránh do rủi ro pháp lý/cơ cấu chưa được định giá rõ**: **GVR** — kỹ thuật chưa xác nhận giữ hỗ trợ MA50 + rủi ro mất tư cách công ty đại chúng (Nhà nước nắm 96,8%, phải thoái vốn dưới 90% trong 1 năm) là rủi ro hệ thống thật, không phải tin đồn.
- **Trong 3 mã Agent C chọn, rủi ro cao nhất là VIC** — dù điểm ensemble cao nhất, thanh khoản là thấp nhất toàn bộ 30 mã trong danh sách, mô hình con bất đồng mạnh (LSTM cao bất thường so với 3 mô hình còn lại), và vừa có phiên giảm -4,3% ngay trước thời điểm phát tín hiệu — đặc điểm của một nhịp "xả hàng" hơn là "tích lũy".

---

## Nhắc lại giới hạn mô hình

Toàn bộ điểm số, xác suất và xếp hạng trên dựa trên mô hình có **AUC ~0.53–0.55** — chỉ nhỉnh hơn tung đồng xu một chút. Sự khác biệt điểm giữa VIC (0.5776) và GAS (0.5352) hay VRE (0.5474) không đủ lớn để coi là tín hiệu đáng tin cậy; đồng thời các mô hình con (LogReg, RandomForest, GradBoost, XGBoost, LSTM) thường xuyên bất đồng nhau ở biên độ lớn (ví dụ LSTM luôn cho xác suất 0,76–0,88 trong khi GradBoost/XGBoost chỉ 0,27–0,46 cho cùng các mã) — đây là dấu hiệu mô hình LSTM có thể bị lệch/overfit và đang kéo điểm tổng hợp lên một cách không tương xứng với các mô hình khác. Không nên xem bất kỳ luận điểm bò nào ở trên là chắc chắn.

---

*KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — đây là tổng hợp luận điểm GẤU/phản biện mang tính tranh luận nội bộ, dùng để stress-test luận điểm bò của Agent C cho Agent E tham khảo, không dùng để ra quyết định giao dịch trực tiếp.*


---

# 🗣️ PHIÊN 4 — QUYẾT ĐỊNH (Agent E)

*(Tóm tắt; chi tiết đầy đủ ở [`DECISION.md`](DECISION.md).)*

### 🎩 Agent E — Giám đốc Chiến lược · 2026-09-14 10:15

Không có mã nào đủ điều kiện MUA. Bò (C) và gấu (D) cân bằng ở VIC/GAS/VRE (mỗi mã có catalyst tin tức thật nhưng cũng có rủi ro cụ thể chưa giải quyết) → mặc định THEO DÕI theo nguyên tắc bảo toàn vốn. GVR và PNJ có luận điểm gấu áp đảo rõ ràng (rủi ro pháp lý cơ cấu cổ đông / downtrend kỹ thuật xác nhận) → TRÁNH.

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| VIC | THEO DÕI | Thấp | Điểm mô hình cao nhất + KQKD mạnh, nhưng vol_ratio thấp nhất toàn bộ 30 mã và mô hình con bất đồng mạnh (LSTM outlier) — chờ volume xác nhận. |
| GAS | THEO DÕI | TB | Setup kỹ thuật tốt nhất nhóm + cổ tức thực đang chi trả, nhưng ĐHĐCĐ bất thường đúng ngày tín hiệu chưa rõ nội dung — chờ công bố. |
| VRE | THEO DÕI | Thấp | Hỗ trợ tin tức tốt nhất + catalyst FTSE, nhưng nhãn trend_up mâu thuẫn với MA50 quan sát thực tế trên chart — chờ xác nhận đáy kỹ thuật. |
| GVR | TRÁNH | Cao | Kỹ thuật chưa xác nhận giữ MA50 + rủi ro pháp lý hủy tư cách công ty đại chúng thật (Nhà nước nắm 96,8%). |
| PNJ | TRÁNH | Cao | Downtrend 6 tháng chưa đảo chiều, giá dưới MA50 dốc xuống, TP trùng kháng cự động — "bắt dao rơi" theo chính Agent A. |

**Stance danh mục:** Thận trọng. Không mã nào hội tụ đủ kỹ thuật + catalyst + thanh khoản để giải ngân ngay; giữ tỷ trọng tiền mặt cao, tổng vị thế 3 mã theo dõi (nếu kích hoạt) không vượt 6-8% danh mục.

Chi tiết đầy đủ: `debate/DECISION.md`.

KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.

