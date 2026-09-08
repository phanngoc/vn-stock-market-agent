### 🅰️ Agent A — Phân tích Kỹ thuật · 2026-09-08 05:15

**Nguồn**: `signals_latest.csv` + `charts/<TICKER>_setup.png` (nến + MA20/MA50 + TP/SL), as-of 2026-09-08.

| Mã | Trend (giá vs MA20/50) | RSI(14) | vol_ratio | Điểm KT /10 | Ghi chú |
|---|---|---|---|---|---|
| **VRE** | Trên MA20 & MA50 (MA50 vừa quay đầu tăng) | 57.8 (trung tính, nghiêng tăng) | 0.50 (èo uột nhưng cao nhất nhóm) | **6.5** | Phục hồi từ đáy tháng 7 (~21.5k) lên 26.35k, breakout khỏi MA20/50 rõ nét nhất nhóm; TP 28,458 trùng vùng cung cũ tháng 6 (~28.5k) — hợp lý, không quá xa. |
| **VIC** | Trên MA20 & MA50, giá sát đỉnh gần nhất | 63.2 (tiệm cận vùng quá mua) | 0.21 (thấp nhất nhóm) | **6.0** | Uptrend mạnh nhưng đã tăng nóng lên 260k rồi điều chỉnh về 241.7k; TP 261,036 nằm ngay tại đỉnh cũ → dễ gặp kháng cự trước khi chạm chốt lời; khối lượng xác nhận yếu. |
| **GVR** | Dao động ngang nhiều tháng, giá vừa cắt lên MA20, sát MA50 | 52.98 (trung tính) | 0.23 (rất yếu) | **5.0** | Không có xu hướng rõ, đi ngang biên 25k–40k từ tháng 3; entry 31.7k gần như trùng MA50 → chưa xác nhận breakout; TP 34,236 gần vùng cản tháng 8 (~33–34k), khả thi nhưng cần thanh khoản xác nhận thêm. |
| **PNJ** | **Dưới MA50** (MA50 đang đi ngang/giảm nhẹ), vừa cắt lên MA20 | 47.6 (trung tính) | 0.45 | **4.0** | Downtrend dài (80k→30k từ tháng 3–7), đang có nhịp hồi kỹ thuật từ đáy ~35k nhưng còn dưới MA50 → cảnh báo "bắt dao rơi"; TP 42,120 trùng vùng MA50/kháng cự cũ, hợp lý làm target nhưng xác suất chạm thấp nếu xu hướng chính chưa đảo chiều. |
| **PDR** | **Dưới MA50**, MA50 vẫn đang giảm | 39.8 (gần vùng quá bán) | 0.32 | **3.5** | Downtrend rõ từ tháng 5 (16.5k→11.4k), giá đi ngang đáy vài tuần gần đây nhưng chưa có xác nhận đảo chiều; SL 11,305 khá sát đáy gần nhất → biên độ chịu đựng hẹp; đây là kiểu "dò đáy" rủi ro kỹ thuật cao nhất nhóm. |

## Nhận định chung
- Setup kỹ thuật đẹp nhất nhóm (thuần kỹ thuật): **VRE** — có xác nhận trend-following (trên MA20/50) và vol_ratio tương đối cao nhất, dù vẫn <1.
- Setup yếu/rủi ro nhất: **PDR** và **PNJ** — cả hai đều dưới MA50 trong xu hướng giảm dài hạn, xếp vào nhóm "bắt dao rơi"; xác suất thành công thấp hơn dựa trên vị trí trend.
- Rủi ro kỹ thuật lớn nhất chung của cả 5 mã: **vol_ratio đều dưới 1** (0.21–0.50) — không mã nào có khối lượng xác nhận mạnh cho breakout/hồi phục, nghĩa là các tín hiệu giá hiện tại chưa được dòng tiền ủng hộ rõ ràng.
- VIC dù trend mạnh nhất nhưng RSI đã tiệm cận 63–70 và giá sát đỉnh cũ, nên phần dư địa tăng tới TP hẹp hơn so với vẻ ngoài "uptrend".
- Toàn bộ TP/SL (+8%/−5%) đều được đặt tự động theo quy tắc, không phải tính từ vùng hỗ trợ/kháng cự thực tế cho từng mã — chỉ có PNJ và VRE là TP trùng khá sát vùng kháng cự quan sát được trên chart; các mã còn lại: chưa kiểm chứng khớp với vùng S/R cụ thể.

**KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ** — đây chỉ là góc nhìn kỹ thuật thuần túy, dựa trên mô hình có edge yếu (AUC ~0.53–0.55); cần kết hợp với Agent B (tin tức/cơ bản) và quản trị rủi ro trước khi ra quyết định.
