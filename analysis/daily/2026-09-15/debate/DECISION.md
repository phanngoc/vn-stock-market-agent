# 🎩 QUYẾT ĐỊNH ĐẦU TƯ CUỐI CÙNG — as-of 2026-09-15

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.** Đây là khung ra quyết định mô phỏng của một hội đồng tác nhân AI tranh luận nội bộ, dựa trên dữ liệu và tin tức có thể sai/thiếu/lỗi thời. Mô hình nền có **edge yếu (AUC ~0.53–0.55)**; quan trọng hơn, base win-rate của mô hình tốt nhất trên tập kiểm định (LogReg, 0.357) **thấp hơn** buy-and-hold cùng kỳ (0.3824) — nghĩa là bản thân tín hiệu mô hình, xét thuần túy về xác suất thắng lịch sử, kém hơn việc không làm gì. Quyết định đầu tư thật thuộc về người dùng, tự chịu trách nhiệm rủi ro.

## Tóm tắt quyết định theo mã

| Mã | Quyết định | Độ tin cậy | Lý do 1 dòng |
|---|---|---|---|
| **VRE** | THEO DÕI | TB | Hội tụ tin tức mạnh nhất nhóm (KQKD vượt kế hoạch, catalyst FTSE Small Cap) nhưng kỹ thuật mới cắt lên MA50 — dạng tín hiệu dễ whipsaw, chưa đủ xác nhận dòng tiền (vol_ratio 0.23) để giải ngân ngay. |
| **VIC** | THEO DÕI | TB | Catalyst FTSE Large Cap thật, nhưng vol_ratio 0.10 thấp nhất nhóm + đã có phiên đảo chiều giảm >4,3% tại vùng TP — rủi ro "buy the rumor, sell the news" và rủi ro trùng lặp catalyst với VRE (không độc lập). |
| **GAS** | THEO DÕI | TB | Nền cơ bản/kỹ thuật tốt nhất nhóm, nhưng RSI 67 gần quá mua cộng dồn với giảm giá cơ học quanh ngày GDKHQ cổ tức (~23/9) đúng trong khung nắm giữ — hai lực ép giá cùng lúc, không có catalyst FTSE bù đắp. |
| **GVR** | TRÁNH | Cao | Không catalyst (ngoài rổ FTSE), kỹ thuật đi ngang yếu (RSI <50, vol_ratio 0.15), thêm rủi ro pháp lý cổ đông nhỏ — không có điểm mạnh nào đủ bù rủi ro. |
| **PNJ** | TRÁNH | Cao | Downtrend dốc dưới MA50 ("bắt dao rơi"), lỗ ròng quý 2 kỷ lục + dự phòng 2.267 tỷ chưa dứt điểm, chờ BCTC Q3 (26/10) có thể biến động mạnh thêm. |

**Ghi chú nguyên tắc áp dụng:** với cả 3 mã VRE/VIC/GAS, luận điểm bò (Agent C) và phản biện gấu (Agent D) đều có sức nặng tương đương — mỗi mã đều có ít nhất một rủi ro cụ thể, có cơ sở dữ liệu/tin tức thật (không phải suy đoán) đủ để phủ nhận việc vào lệnh ngay. Theo nguyên tắc bảo toàn vốn khi bò ≈ gấu, quyết định là **THEO DÕI**, không MUA.

---

## Kế hoạch giao dịch (mã THEO DÕI — chỉ kích hoạt nếu điều kiện xác nhận xảy ra)

### VRE
- **Vùng theo dõi/entry tiềm năng:** 25.300–25.900đ, **chỉ cân nhắc vào lệnh nếu** vol_ratio tăng rõ rệt (>0.5) xác nhận dòng tiền đi kèm giá giữ vững trên MA50 sau ngày FTSE có hiệu lực (21/9).
- **Chốt lời (+8%):** 27.648đ | **Cắt lỗ (−5%):** 24.320đ | **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất nếu kích hoạt:** 2–3% danh mục (thận trọng, do tín hiệu kỹ thuật còn non).
- **Invalidation:** giá cắt xuống lại dưới MA50 với thanh khoản tăng (xác nhận thất bại của nhịp hồi), hoặc không có phản ứng giá tích cực quanh 21/9 (dấu hiệu "sell the news").

### VIC
- **Vùng theo dõi/entry tiềm năng:** 235.000–242.000đ, **chỉ cân nhắc vào lệnh nếu** vol_ratio cải thiện rõ rệt (hiện 0.10 quá thấp) và giá giữ trên vùng hỗ trợ ngắn hạn sau biến động ngày 21/9.
- **Chốt lời (+8%):** 260.820đ | **Cắt lỗ (−5%):** 229.425đ | **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất nếu kích hoạt:** 2–3% danh mục.
- **Invalidation:** tái lập mẫu hình giảm mạnh trong phiên (>4%) quanh vùng kháng cự 260k, hoặc tin xấu mới về trái phiếu quốc tế/đòn bẩy.

### GAS
- **Vùng theo dõi/entry tiềm năng:** 86.000–89.000đ, **chỉ cân nhắc vào lệnh sau** khi giá điều chỉnh cơ học quanh ngày GDKHQ cổ tức (~23/9, ngày chính xác chưa kiểm chứng) đã phản ánh xong và RSI hạ nhiệt khỏi vùng gần quá mua.
- **Chốt lời (+8%):** 95.796đ | **Cắt lỗ (−5%):** 84.265đ | **Time-stop:** 25 phiên.
- **Cỡ vị thế đề xuất nếu kích hoạt:** 2–3% danh mục.
- **Invalidation:** RSI vượt 70 rồi đảo chiều giảm mạnh (xác nhận quá mua thất bại), hoặc thêm công bố bất lợi về rủi ro "công ty đại chúng".

## Mã TRÁNH — không lập kế hoạch giao dịch

- **GVR:** không giải ngân cho đến khi có catalyst tin tức tích cực rõ ràng hoặc kỹ thuật xác nhận xu hướng tăng thật sự (thoát vùng đi ngang, volume cải thiện).
- **PNJ:** không giải ngân cho đến khi có BCTC Q3 (26/10/2026) xác nhận dứt điểm khoản dự phòng và giá tạo đáy kỹ thuật rõ ràng (hiện vẫn dưới MA50, downtrend dốc).

---

## Stance tổng danh mục

**Khẩu vị rủi ro chung: Thận trọng.**

Lý do: (1) mô hình nền có edge yếu và base win-rate thấp hơn buy-and-hold trên tập kiểm định — không có cơ sở thống kê để tự tin vào tín hiệu score; (2) 2 trong 3 mã có luận điểm bò (VIC, VRE) phụ thuộc cùng một catalyst FTSE (21/9/2026) — rủi ro tương quan cao, không phải hai cơ hội độc lập; (3) mã có kỹ thuật/cơ bản tốt nhất nhóm (GAS) lại vướng hai lực ép giá cơ học/kỹ thuật trùng thời điểm trong đúng khung nắm giữ.

**Phân bổ gợi ý:** không giải ngân mới cho nhóm 5 mã này ở thời điểm hiện tại; giữ tỷ trọng tiền mặt cao, chỉ xem xét vào lệnh nhỏ (2–3%/mã) nếu điều kiện xác nhận ở trên xảy ra sau sự kiện FTSE 21/9. Không dồn vốn vào cả VIC và VRE cùng lúc vì rủi ro tương quan catalyst.

## Cần theo dõi tuần tới

- **21/9/2026:** FTSE Russell chính thức nâng hạng có hiệu lực — theo dõi phản ứng giá VIC/VRE ngay trong và sau phiên (xác nhận "buy the rumor, sell the news" hay dòng vốn thực sự vào).
- **~23/9/2026 (ngày chính xác chưa kiểm chứng):** GAS chốt danh sách cổ đông nhận cổ tức 25% tiền mặt — theo dõi mức điều chỉnh giá tham chiếu và diễn biến RSI quanh vùng quá mua.
- **26/10/2026:** PNJ công bố BCTC Q3/2026 — đánh giá lại tồn kho kim cương, có thể là điểm đảo chiều (nếu dứt điểm dự phòng) hoặc điểm rủi ro mới.
- Diễn biến vol_ratio của VIC/VRE/GAS trong tuần tới — nếu không cải thiện rõ rệt dù có catalyst, củng cố thêm cho luận điểm gấu.
- Thông tin bổ sung (chưa kiểm chứng trong phiên này) về thời hạn khắc phục tình trạng "không đủ điều kiện công ty đại chúng" của GAS/GVR — nguy cơ hủy niêm yết bắt buộc nếu không xử lý.

---

*Tổng hợp bởi Agent E (CIO) dựa trên whiteboard PHIÊN 1–3 (Agent A/B/C/D) và signals_latest.csv. KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.*
