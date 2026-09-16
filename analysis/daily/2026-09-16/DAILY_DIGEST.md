# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-16 05:14 · dữ liệu giá as-of **2026-09-16** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Không mã nào đạt ngưỡng MUA phiên này; edge mô hình yếu (AUC ~0.53-0.55) và bò/gấu cân bằng ở các mã tốt nhất nên ưu tiên bảo toàn vốn, chỉ THEO DÕI với vị thế nhỏ.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 238000-244000 | 262,332 | 230,755 | 25 phiên | 2-3% |
| **GVR** | TB | 31800-32500 | 34,830 | 30,638 | 25 phiên | 2-3% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Ky thuat thap nhat nhom (3/10), downtrend dai han tu ~78k chua bi pha, volume phuc hoi qua yeu (0.26) de tin dao chieu, cong overhang cung tu nguoi nha Chu tich (chua kiem chung quy mo). |
| **GAS** | TB | RSI 71 qua mua nhat nhom, gia tham chieu gan nhu chac chan giam ky thuat quanh GDKHQ 22/9 (~2,7%), TP sat khang cu dinh lich su 95-102k, cong rui ro thu tuc cong ty dai chung. |
| **VRE** | TB | Dang cham dung vung khang cu MA50 cu tung bi tu choi (thang 6-7) voi volume hoi phuc yeu (0.21); khong co catalyst tin tuc moi sap toi. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Catalyst FTSE (hiệu lực 21/9) va KQKD tang 360,5% svck la that, nhung vol_ratio 0.12 thap nhat nhom khien tin hieu tang thieu xac nhan dong tien.
  - *Huỷ luận điểm nếu:* Volume khong cai thien quanh/sau 21/9 du gia van giu; hoac gia thung lai vung 230k truoc time-stop; hoac xuat hien tin xau cu the ve tin dung BDS/pha loang tu phat hanh trai phieu quoc te.
- **GVR** — Ky thuat can bang nhat nhom (volume 1.34 cao nhat, SL sat ho tro), nhung vung gia gap MA20/MA50 cung la vung can bang cung-cau de bi quet SL.
  - *Huỷ luận điểm nếu:* Gia dong cua thung ro rang duoi MA50; gia cao su the gioi tiep tuc giam ro ret (khong chi giang co); hoac KQKD Q2/Q3 cho thay da tang truong 56%/85% svck cua Q1 khong duy tri duoc.

### 📅 Cần theo dõi tuần này
- 21/9/2026: FTSE Russell chính thức phân bổ dòng vốn (nâng hạng Secondary Emerging Market) - theo dõi volume thực tế của VIC quanh ngày này
- 22-23/9/2026: GAS chốt quyền cổ tức tiền mặt 25% (GDKHQ 22/9) - quan sát mức điều chỉnh giá tham chiếu
- VRE: vùng kháng cự MA50 cũ 25700-26000d - cần volume tăng rõ rệt để phá vùng này
- PNJ: tin cụ thể về khối lượng/thời điểm bán ra của người nhà Chủ tịch HĐQT (hiện chưa kiểm chứng quy mô)
- GVR: công bố KQKD Q2/Q3 2026 và diễn biến giá cao su thế giới (SHFE/TOCOM)

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-16_04-57-42`. Chạy lại: skill `vn-swing-daily`.*
