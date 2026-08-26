# 🎩 QUYẾT ĐỊNH CUỐI — Hội đồng Đầu tư Swing TTCK Việt Nam

**Người phân xử:** Agent E — Giám đốc Chiến lược Đầu tư (CIO)
**Thời điểm ra quyết định:** 2026-08-26 10:10 · **Dữ liệu as-of:** 2026-08-25
**Ứng viên (top 5):** VIC, VRE, VCI, KDH, PDR (4 BĐS + 1 Chứng khoán)

> ⚠️ **ĐÂY KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là **khung ra quyết định mô phỏng** của một hội đồng tranh luận có kỷ luật rủi ro. Mọi quyết định thực tế là của người dùng. Edge mô hình định lượng **yếu (AUC ~0,53–0,55 — chỉ nhỉnh hơn tung đồng xu)**; catalyst nâng hạng FTSE là **kỳ vọng dòng vốn** giải ngân theo lộ trình (chưa xảy ra toàn bộ); nhiều mốc MA/ngày GDKHQ **"chưa kiểm chứng"** — cần đối chiếu công bố HOSE/VSD. Ưu tiên cao nhất: **BẢO TOÀN VỐN**.

---

## 1. Bảng quyết định theo mã

| Mã | Quyết định | Độ tin cậy | Giá (VND) | TP +8% | SL −5% | Lý do quyết định (1–2 câu) |
|---|---|---|---|---|---|---|
| **VIC** | THEO DÕI | TB | 223.800 | 241.704 | 212.610 | Setup KT đẹp nhất + catalyst FTSE Large Cap mạnh nhất, NHƯNG mua ở đây là **đuổi giá sau nhịp +60%/tháng** (RSI 61,5) và TP đâm thẳng kháng cự đỉnh cũ (dư địa hẹp) + rủi ro pha loãng GDKHQ chưa rõ ngày → chờ chỉnh về nền, không đuổi. |
| **VRE** | THEO DÕI | TB | 25.500 | 27.540 | 24.225 | Cơ bản vững nhất nhóm (Q1 lãi kỷ lục, FTSE Small Cap, cổ tức tiền mặt 10%) NHƯNG **dưới MA50, chưa xác nhận** (vol 0,71 yếu); chỉ mua khi đóng cửa vững trên MA50 kèm volume. |
| **VCI** | TRÁNH | TB | 22.400 | 24.192 | 21.280 | Chỉ là **beta thuần vào FTSE**, nền cơ bản xấu nhất (tự doanh lỗ, thu nhập toàn diện âm 432 tỷ, mới đạt 29% KH); margin kỷ lục = **rủi ro hệ thống** nếu index bị chặn ở 1.800 → giải chấp. Dưới MA50, 2 cây quyết định bearish. |
| **KDH** | TRÁNH | Cao | 18.200 | 19.656 | 17.290 | **Bắt dao rơi kinh điển**: KT tệ nhất (3,5/10, downtrend, MA50 dốc xuống, TP bị MA50 chặn), lợi nhuận Q2 "ảo" từ thoái vốn, bán nhà −85%, dòng tiền KD âm >1.480 tỷ, không catalyst FTSE. |
| **PDR** | TRÁNH | Cao | 12.700 | 13.716 | 12.065 | Volume yếu nhất bảng (0,43), xa dưới MA50, TP nằm **trên** MA50; chi 7.666 tỷ thương vụ Lotte gây áp lực dòng tiền, bán BĐS chỉ ~2 tỷ, ngoài rổ FTSE — thiếu catalyst ngắn hạn. |

**Tóm tắt: 0 MUA · 2 THEO DÕI (VIC, VRE) · 3 TRÁNH (VCI, KDH, PDR).**

---

## 2. Cân đối bò (C) vs gấu (D) — vì sao mặc định THEO DÕI, không MUA

- **Điểm C thuyết phục:** VIC hội tụ setup KT đẹp nhất (Agent A: 7,5/10, mã duy nhất trên MA50 + vol>1) và catalyst tin tức mạnh nhất (Agent B: hạng 1, FTSE Large Cap). VRE có nền cơ bản [ĐÃ XẢY RA] chắc nhất, không phải bắt dao rơi thuần kỹ thuật.
- **Điểm D làm suy yếu (quyết định):**
  1. **Edge ~coin-flip:** Chênh score rank 1→5 (0,5949→0,5393) **nằm trong nhiễu**; các kèo bò đều bị **LSTM đơn lẻ kéo lên** trong khi GradBoost/XGBoost gần hoặc dưới 0,5 (VCI thậm chí bearish rõ) → không dùng rank làm thứ tự ưu tiên đáng tin.
  2. **Catalyst FTSE dễ đã-vào-giá:** VIC đã +60%/tháng, tin công bố 21/8; passive ~1,45–1,5 tỷ USD chia 27 mã, ưu tiên vốn hóa lớn → phần rơi vào Small Cap (VRE/VCI) không đáng kể. Rủi ro "mua tin đồn, bán sự thật" quanh mốc 21/9.
  3. **Vào lệnh TRƯỚC xác nhận:** VRE/VCI **dưới MA50**, Agent A nói thẳng "cần đóng cửa trên MA50 mới xác nhận" — mua bây giờ = mua vào kháng cự.
  4. **Rủi ro hệ thống C chưa cân đủ:** tập trung ngành cực đoan (4 BĐS + 1 CK = một cược vĩ mô cùng nhạy lãi suất/thanh khoản); VN-Index ~1.768 áp sát kháng cự mạnh 1.800; biên ±7% + T+2 khiến **SL −5% không đảm bảo khớp** (gap-down có đuôi dày hơn R:R 1,6 lý thuyết).
- **Phân xử:** Với VIC và VRE, bò ≈ gấu (mỗi bên có lý lẽ CÓ THẬT) → theo nguyên tắc bảo toàn vốn, **mặc định THEO DÕI + chờ xác nhận**, không MUA trước tín hiệu. Với VCI/KDH/PDR, cán cân nghiêng gấu rõ (cơ bản xấu và/hoặc KT downtrend) → **TRÁNH**.

---

## 3. Kế hoạch giao dịch (chỉ cho 2 mã THEO DÕI — kích hoạt KHI đủ điều kiện)

### VIC — THEO DÕI (TB)
- **Điều kiện kích hoạt:** KHÔNG đuổi giá ở vùng hiện tại. Chỉ cân nhắc khi giá **chỉnh về nền tích lũy 210–218k** (cụm MA20/MA50) rồi giữ vững, HOẶC breakout dứt khoát qua đỉnh cũ ~242k kèm volume.
- **Vùng entry đề xuất:** 210.000–218.000 (mua khi chỉnh về hỗ trợ, không đuổi).
- **Chốt lời (+8%):** 241.704 · **Cắt lỗ (−5%):** 212.610 · **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất:** 2–3% danh mục (thận trọng — mã beta cao, sau nhịp nóng).
- **Điều kiện huỷ luận điểm (invalidation):** Công bố **ngày GDKHQ phát hành cổ phiếu trả cổ tức/thưởng rơi vào khung 25 phiên** (rủi ro kẹp pha loãng); hoặc mất nền MA50 (~213–215k) kèm volume bán lớn; hoặc VN-Index bị đẩy lùi mạnh khỏi 1.800.

### VRE — THEO DÕI (TB)
- **Điều kiện kích hoạt:** **Đóng cửa vững TRÊN MA50 (~25.700) kèm volume tăng (vol_ratio > 1)** — đúng điều kiện Agent A nêu. Chưa xác nhận thì chưa vào.
- **Vùng entry đề xuất:** 25.700–26.200 (sau khi xác nhận vượt MA50).
- **Chốt lời (+8%):** 27.540 · **Cắt lỗ (−5%):** 24.225 · **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất:** 2–3% danh mục (thận trọng).
- **Điều kiện huỷ luận điểm (invalidation):** Bị đẩy ngược xuống dưới MA20 sau khi test MA50 thất bại; volume tiếp tục èo uột (<1) khi tiếp cận kháng cự; hoặc GDKHQ cổ tức tiền mặt 10% (chưa kiểm chứng ngày) rơi bất lợi trong khung.

> Với VCI/KDH/PDR (TRÁNH): không lập kế hoạch vào lệnh; giữ TP/SL trong bảng chỉ để tham chiếu.

---

## 4. Stance tổng danh mục

**Khẩu vị rủi ro: THẬN TRỌNG.**

- **Lý do:** (1) edge mô hình ~coin-flip → không có lợi thế thống kê đáng tin; (2) rổ ứng viên **tập trung ngành cực đoan** (4 BĐS + 1 CK) = thực chất một cược vĩ mô, không phân tán; (3) VN-Index áp sát **kháng cự mạnh 1.800**, khối ngoại chưa ổn định (tuần 10–14/8 bán ròng >2.100 tỷ); (4) catalyst FTSE nhiều khả năng đã phản ánh phần lớn vào nhóm dẫn dắt.
- **Phân bổ gợi ý:** **Giữ tỷ trọng tiền mặt cao** ở giai đoạn này. Không giải ngân trước khi có xác nhận. Nếu điều kiện kích hoạt xuất hiện, tổng tỷ trọng cho nhóm này **không quá ~5–6% danh mục** (2–3% mỗi mã VIC/VRE), tránh cộng dồn rủi ro cùng một cược vĩ mô. Ưu tiên chờ tín hiệu vượt MA50 + volume + phản ứng của index tại 1.800.

---

## 5. Cần theo dõi tuần tới (sự kiện / mức giá)

- **VRE:** đóng cửa vững **trên MA50 (~25.700)** kèm volume tăng — mốc xác nhận quyết định.
- **VIC:** nhịp **chỉnh về nền 210–218k**; đặc biệt **ngày GDKHQ phát hành cổ phiếu trả cổ tức/thưởng** (theo dõi công bố HOSE/VSD — hiện "chưa kiểm chứng").
- **VN-Index:** phản ứng tại **kháng cự mạnh 1.800** (hiện ~1.768) — bị đẩy lùi hay vượt quyết định rủi ro toàn nhóm beta cao.
- **Khối ngoại:** mua/bán ròng — dòng vốn chưa ổn định, cần xu hướng mua ròng bền để củng cố.
- **Mốc 21/9 (FTSE hiệu lực đợt 1):** cảnh giác kịch bản "mua tin đồn, bán sự thật" khi tin đã ra và giá đã chạy trước.
- **VRE cổ tức tiền mặt 10%:** ngày GDKHQ (chưa kiểm chứng) — theo dõi công bố sàn.

---

*Ghi chú tính nhất quán: quyết định trên bám sát bằng chứng whiteboard PHIÊN 1–3. Không bác bỏ luận điểm bò của C mà đặt điều kiện xác nhận trước khi hành động — phản ánh cán cân bò/gấu ngang bằng ở VIC/VRE và cán cân nghiêng gấu ở VCI/KDH/PDR. Không MUA nào được kích hoạt ở thời điểm này do ưu tiên bảo toàn vốn khi edge yếu + rủi ro hệ thống hiện hữu.*
