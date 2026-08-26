# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-08-26 07:24 · dữ liệu giá as-of **2026-08-26** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Toàn bộ 5 mã ứng viên có vol_ratio dưới 1 (không xác nhận dòng tiền), 3/5 mã cùng ngành RealEstate (rủi ro tập trung), và thanh khoản thị trường chung đang giảm khi VN-Index thử vùng cản 1.775-1.810.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **PDR** | TB | 12300-12600 | 13,554 | 11,922 | 25 phiên | 1.5-2.5% |
| **VIC** | TB | 218000-223000 | 240,840 | 211,850 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **KDH** | Cao | Kỹ thuật thấp nhất nhóm (3/10) - Agent A gọi đây là 'bắt dao rơi': dưới cả MA20/MA50, mới bật 2 phiên, khối lượng thấp. Cơ bản tốt (lãi 2025 vượt 63% KH) nhưng thiếu catalyst ngắn hạn trong khung 5 tuần. |
| **PNJ** | TB | Không có luận điểm bò được xây dựng; tin xấu cụ thể đã xảy ra (lỗ 283 tỷ đồng Q2/2026, nguyên nhân chưa rõ) cộng kỹ thuật yếu, rủi ro 'dead-cat bounce' sau nhịp hồi +40% từ đáy. |
| **VRE** | TB | Kỹ thuật yếu nhất trong 3 mã được Agent C chọn (4/10, vẫn dưới MA50, chưa đảo chiều rõ); catalyst cổ tức dùng làm điểm tựa thực chất là lực cản kỹ thuật ở ngày GDKHQ (giá tham chiếu bị điều chỉnh giảm), lợi ích FTSE chỉ là 'có thể', chưa xác nhận. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **PDR** — Catalyst insider-buying (Chủ tịch đăng ký mua 20 triệu cp, cửa sổ đến 29/8/2026) là tín hiệu thật đang diễn ra, nhưng đối trọng bởi vol_ratio thấp nhất nhóm (0.17) và rủi ro pha loãng ~20% (phát hành 200 triệu cp) chưa rõ thời điểm GDKHQ - bò/gấu cân bằng.
  - *Huỷ luận điểm nếu:* Công bố ngày GDKHQ chốt quyền mua cổ phiếu 5:1 trong thời gian tới; Chủ tịch không hoàn tất mua theo đăng ký; giá đóng cửa xuyên SL 11,922đ.
- **VIC** — Setup kỹ thuật tốt nhất nhóm (breakout khỏi vùng tích lũy 4 tháng, trend_up=True, 7/10) nhưng khối lượng xác nhận vẫn dưới 1 (0.55) và catalyst FTSE nâng hạng đã công bố từ 5 tháng trước nên có thể đã phần nào phản ánh vào giá - bò/gấu cân bằng.
  - *Huỷ luận điểm nếu:* vol_ratio tiếp tục dưới 0.6 trong hơn 3 phiên tới (breakout không được dòng tiền xác nhận); thêm tin tiêu cực từ nhóm Vingroup; giá đóng cửa dưới SL 211,850đ.

### 📅 Cần theo dõi tuần này
- VIC: vol_ratio có vượt 1.0 để xác nhận breakout khỏi vùng tích lũy 200-230k không
- PDR: kết quả cuối cùng đợt đăng ký mua 20 triệu cp của Chủ tịch (hạn 29/8/2026) và tin ngày GDKHQ đợt phát hành 200 triệu cp
- VRE: thông báo ngày GDKHQ cổ tức tiền mặt 10% dự kiến Q3/2026 (là lực cản kỹ thuật, không phải lực đẩy)
- Ngành BĐS: kết quả cụ thể Luật Phát triển đô thị (Quốc hội dự kiến thông qua 24/8/2026) - tác động từng mã chưa kiểm chứng
- VN-Index có vượt dứt điểm vùng cản 1.775-1.810 kèm thanh khoản cải thiện hay không; diễn biến dư nợ margin
- PNJ: báo cáo tài chính chi tiết Q2/2026 để hiểu nguyên nhân khoản lỗ 283 tỷ đồng - chưa kiểm chứng

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.352** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- ⚠️ 4/5 mã top đang **dưới MA50** → phần lớn là kèo hồi kỹ thuật/bắt đáy, rủi ro cao hơn kèo momentum.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-08-26_07-09-05`. Chạy lại: skill `vn-swing-daily`.*
