# 📈 Bản tin swing hằng ngày — TTCK Việt Nam

*Tạo lúc 2026-09-11 05:07 · dữ liệu giá as-of **2026-09-11** (vnstock/VCI) · hội đồng 5 tác nhân đã tranh luận.*

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.** Đây là kết quả mô phỏng (ML + khung tranh luận đa tác nhân) trên dữ liệu quá khứ, edge mô hình YẾU (AUC ~0.53–0.55). Quyết định là của bạn; ưu tiên quản trị rủi ro.

## 🎩 Khẩu vị danh mục hôm nay: **Thận trọng**
Volume yếu trên toàn bộ nhóm top 5 (vol_ratio <1), mô hình có edge yếu (AUC ~0.53-0.55), và nhiều luận điểm bò bị phản biện đứng vững bằng chính bằng chứng kỹ thuật/tin tức nên không mã nào đạt ngưỡng MUA phiên này.


### 👀 THEO DÕI
| Mã | Tin cậy | Vùng vào | Chốt lời | Cắt lỗ | Time-stop | Cỡ vị thế |
|---|---|---|---|---|---|---|
| **VIC** | TB | 245000-250000 | 267,300 | 235,125 | 25 phiên | 2-3% |
| **GVR** | TB | 31000-32000 | 34,074 | 29,972 | 25 phiên | 2-3% |
| **VRE** | Thấp | 25500-26200 | 27,918 | 24,558 | 25 phiên | 2% |

### ⛔ TRÁNH
| Mã | Độ tin cậy | Lý do |
|---|---|---|
| **PNJ** | Cao | Duoi MA50 (downtrend, ky thuat yeu nhat nhom theo A: 3/10), volume eo uot, Q2/2026 lo ~283 ty du diem mo hinh cao nhat nhom (0.6248) - rui ro bat dao roi ro rang. |
| **GAS** | TB | Co tuc 25% + KQKD H1 tot la diem cong that, nhung su kien rui ro phap ly nhi phan cu the (DHDCD bat thuong 14/9 ve nguy co mat tu cach cong ty dai chung) roi ngay dau ky nam giu; GDKHQ 23/9 chi la dieu chinh gia co hoc, khong phai luc do that. |

### 📋 Chi tiết luận điểm & điều kiện huỷ
- **VIC** — Uptrend + LNST +360.5% + catalyst FTSE GEIS 21/9 ro ngay, nhung RSI 66.2 gan qua mua di cung volume thap nhat nhom (0.13) - phan ky gia/khoi luong that, da tang ~30%/3 tuan nen rui ro sell-the-news; bo/gau can suc nen theo doi cho xac nhan dong tien truoc khi vao.
  - *Huỷ luận điểm nếu:* RSI vuot 70 ma khong co volume xac nhan; xac nhan cu the dong von ETF noi ban rong >1500 ty; gia thung MA50.
- **GVR** — Setup ky thuat tot nhat nhom (uptrend, RSI 51 can bang) nhung khong co catalyst ngan han cu the xac nhan (khong thuoc ro FTSE GEIS), rui ro thanh tra/phap ly thang 2/2026 chua xac nhan da khep lai, volume van duoi 1.
  - *Huỷ luận điểm nếu:* Thanh tra Chinh phu cong bo ket luan bo sung tieu cuc; gia thung MA50; volume khong cai thien sau 10 phien.
- **VRE** — Ky hoach kinh doanh 2026 tich cuc + co tuc 10% + ky thuat khong xau, nhung tin hieu FTSE mau thuan giua 2 nguon (them vao GEIS Small Cap vs bi loai khoi FTSE Vietnam Index) - chua kiem chung ro chieu dong von rong.
  - *Huỷ luận điểm nếu:* Xac nhan bi loai khoi ro chi so co dong von thu dong theo doi (dong ra rong); gia thung MA50.

### 📅 Cần theo dõi tuần này
- 14/9/2026: GAS họp DHDCD bat thuong ve nguy co mat tu cach cong ty dai chung
- 21/9/2026: FTSE Russell chinh thuc ap dung nang hang, VIC vao ro FTSE GEIS Large Cap - theo doi volume/gia quanh moc nay
- 23/9/2026: GAS chot quyen co tuc tien mat 25% (GDKHQ, gia se dieu chinh giam co hoc)
- Xac minh chieu dong von FTSE thuc te voi VRE (them vao GEIS Small Cap hay bi loai khoi FTSE Vietnam Index - hai nguon tin mau thuan)
- Vol_ratio ca 5 ma hien deu duoi 1.0 - theo doi ma nao vuot ro nguong nay kem gia giu tren MA50
- Ngay cong bo KQKD Q3/2026 cua PNJ/VIC/GVR/VRE/GAS (chua xac dinh)

---
### 🧭 Bối cảnh & cảnh báo
- Mô hình tốt nhất OOS: **LogReg** · base win-rate **0.357** · quy tắc sóng **chốt +8% / cắt −5% / time-stop 25 phiên (~5 tuần)**.
- Chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin. Danh sách nên cập nhật lại **mỗi phiên**.

### 🔗 Xem thêm
- Báo cáo ML đầy đủ: [`REPORT.md`](REPORT.md) · tín hiệu máy đọc: [`signals_latest.csv`](signals_latest.csv)
- Tranh luận đầy đủ: [`debate/WHITEBOARD.md`](debate/WHITEBOARD.md) · quyết định CIO: [`debate/DECISION.md`](debate/DECISION.md)
- Biểu đồ nến: [`charts/overview_top6.png`](charts/overview_top6.png)

*Nguồn: run `log_run_2026-09-11_04-49-55`. Chạy lại: skill `vn-swing-daily`.*
