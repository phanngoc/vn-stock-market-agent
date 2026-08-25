# 03 — Khung phân tích cơ bản cổ phiếu Việt Nam (Fundamental Analysis Framework)

> **Không phải khuyến nghị đầu tư (Not investment advice).** Tài liệu mang tính giáo dục / phương pháp luận. Mọi con số minh hoạ cần được kiểm chứng lại với báo cáo tài chính (BCTC) đã kiểm toán và dữ liệu thị trường tại thời điểm ra quyết định.

Mục tiêu của file này là mô tả một **quy trình phân tích cơ bản có thể lặp lại (reproducible)** cho cổ phiếu niêm yết trên HOSE / HNX / UPCoM — đủ chuẩn để một **AI agent** thực thi từng bước và để lại dấu vết (trajectory) kiểm chứng được. Xem [`../blueprint/`](../blueprint/) để biết cách ánh xạ quy trình này vào context database OpenViking.

---

## 0. Quy trình 6 bước (top-down)

```
Vĩ mô (macro)  →  Ngành (sector)  →  Doanh nghiệp (company)  →  Định giá (valuation)
      ↓                 ↓                     ↓                        ↓
  chu kỳ, lãi suất   vị thế cạnh tranh   chất lượng LN & BS      biên an toàn (MoS)
                                                                       ↓
                                                              Rủi ro & catalyst  →  Quyết định
```

1. **Macro / vĩ mô** — chu kỳ kinh tế, tăng trưởng GDP, lãi suất điều hành của SBV, tín dụng, tỷ giá VND/USD, lạm phát (CPI). Xác định "gió xuôi hay gió ngược".
2. **Ngành** — cấu trúc cạnh tranh (5 forces), vị trí trong chu kỳ ngành, quy định pháp lý đặc thù (vd: ngân hàng có Thông tư của SBV, BĐS có Luật Đất đai/Nhà ở/Kinh doanh BĐS 2024).
3. **Doanh nghiệp** — mô hình kinh doanh, chất lượng lợi nhuận, sức khoẻ bảng cân đối, quản trị (governance), cơ cấu sở hữu, giao dịch bên liên quan.
4. **Định giá** — nhiều phương pháp (multiples + DCF/RIM), so sánh với lịch sử và peer, tính **biên an toàn**.
5. **Rủi ro & catalyst** — điều gì có thể làm sai luận điểm; xúc tác giá trong 6–18 tháng.
6. **Quyết định & theo dõi** — luận điểm đầu tư (thesis) rõ ràng, điều kiện review/thoát, và các mốc cần kiểm tra lại.

---

## 1. Đọc báo cáo tài chính Việt Nam (VAS lưu ý)

BCTC doanh nghiệp VN lập theo **Chuẩn mực Kế toán Việt Nam (VAS)**; lộ trình áp dụng **IFRS** đang triển khai theo Quyết định 345/QĐ-BTC (tự nguyện trước, bắt buộc sau). Một số khác biệt cần lưu ý khi phân tích:

- **Quý** thường công bố dạng chưa kiểm toán; **bán niên** soát xét; **năm** kiểm toán. Ưu tiên số kiểm toán; cảnh giác chênh lệch trước/sau kiểm toán (audit gap) — dấu hiệu chất lượng lợi nhuận thấp.
- Nhiều DN có **lợi nhuận từ hoạt động tài chính / thanh lý tài sản** lớn → tách **lợi nhuận cốt lõi (core earnings)** khỏi khoản bất thường (one-off).
- **Vốn hoá chi phí lãi vay** (BĐS, hạ tầng) làm đẹp P&L nhưng phình nợ trên BS.
- Với **ngân hàng**, P&L/BS đọc khác hẳn DN thường (xem §4).

Ba báo cáo phải đọc cùng nhau: **KQKD (P&L)** — **CĐKT (Balance Sheet)** — **LCTT (Cash Flow)**. Nguyên tắc: *lợi nhuận là quan điểm, tiền mặt là sự thật* → luôn đối chiếu **LNST vs dòng tiền từ HĐKD (CFO)**.

---

## 2. Bộ tỷ số cốt lõi (ratio toolkit)

| Nhóm | Tỷ số | Công thức | Ý nghĩa / lưu ý VN |
|---|---|---|---|
| **Sinh lời** | ROE | LNST / VCSH bình quân | >15–20% bền vững = tốt; tách theo DuPont |
| | ROA | LNST / Tổng TS bình quân | So sánh trong cùng ngành |
| | Biên gộp / ròng | LN gộp (ròng) / DTT | Xu hướng quan trọng hơn mức tuyệt đối |
| | ROIC | NOPAT / Vốn đầu tư | So với WACC → tạo/huỷ giá trị |
| **Tăng trưởng** | CAGR DT/LN | (cuối/đầu)^(1/n) − 1 | Ưu tiên tăng trưởng chất lượng, không phải one-off |
| **Đòn bẩy** | Nợ vay ròng / EBITDA | (Nợ vay − tiền) / EBITDA | >3–4x là căng (trừ ngân hàng/utility) |
| | Khả năng trả lãi | EBIT / Chi phí lãi | <2x = rủi ro |
| | D/E | Nợ / VCSH | So peer; BĐS thường cao |
| **Thanh khoản** | Current / Quick ratio | TSNH / Nợ NH | Cảnh giác hàng tồn kho BĐS "ảo" |
| **Định giá** | P/E, P/B | Giá / EPS, Giá / BVPS | So lịch sử 5–10 năm + peer |
| | EV/EBITDA | EV / EBITDA | Trung tính cấu trúc vốn |
| | P/S, PEG | | PEG<1 hấp dẫn nếu tăng trưởng thật |
| | Dividend yield | Cổ tức tiền / giá | Kèm tỷ lệ chi trả (payout) |
| **Dòng tiền** | FCF | CFO − Capex | Âm kéo dài = cần soi kỹ |
| | Chất lượng LN | CFO / LNST | ~1 hoặc >1 là tốt; <<1 = cảnh báo |

**DuPont mở rộng:** `ROE = Biên ròng × Vòng quay TS × Đòn bẩy TS`. Dùng để biết ROE cao đến từ hiệu quả hoạt động hay từ vay nợ (đòn bẩy → rủi ro).

---

## 3. Định giá (valuation) — dùng nhiều phương pháp, không dựa vào một

### 3.1 Multiples (so sánh tương đối)
- **P/E, P/B, EV/EBITDA** so với: (a) lịch sử chính DN (mean ± 1σ), (b) peer trong ngành, (c) trung bình VN-Index / ngành.
- Cẩn trọng "bẫy giá rẻ" (value trap): P/E thấp có thể vì thị trường định giá đúng rủi ro/suy giảm.

### 3.2 DCF / FCFF (giá trị nội tại)
- Dự phóng FCFF 5–10 năm → chiết khấu về hiện tại theo **WACC**, cộng **giá trị cuối kỳ (terminal value)**.
- **WACC ở VN**: `Re = Rf + β×ERP`. Tham chiếu:
  - `Rf` ≈ lợi suất **trái phiếu Chính phủ VN kỳ hạn 10 năm** (theo thời điểm — cần tra cứu).
  - `ERP` (equity risk premium) thị trường VN thường lấy **~8–10%** (cao hơn thị trường phát triển do rủi ro thị trường cận biên/mới nổi — cần cập nhật theo nguồn như Damodaran).
- DCF nhạy với giả định → luôn chạy **độ nhạy (sensitivity)** theo WACC và g cuối kỳ; đừng tin một điểm số duy nhất.

### 3.3 RIM (Residual Income) & P/B–ROE
- Với ngân hàng/DN tài chính, dùng **P/B gắn với ROE** hoặc **RIM** thay cho DCF (dòng tiền ngân hàng khó định nghĩa).
- Quan hệ then chốt: **P/B hợp lý ≈ (ROE − g) / (Re − g)**. ROE > chi phí vốn → P/B > 1 là chính đáng.

### 3.4 SOTP (Sum-of-the-parts)
- Với tập đoàn đa ngành (vd họ Vingroup, Masan): định giá từng mảng rồi cộng lại, trừ nợ ròng cấp holding và **chiết khấu tập đoàn (conglomerate discount)**.

---

## 4. Điều chỉnh theo nhóm ngành (VN-specific)

- **Ngân hàng (VCB, BID, CTG, TCB, ACB, MBB, VPB…):** tập trung **NIM, CASA, CIR, tăng trưởng tín dụng (room), chất lượng tài sản (NPL, nhóm 2), tỷ lệ bao phủ nợ xấu (LLR/LLCR), CAR (Basel II/III), TOI**. Định giá bằng **P/B–ROE**, không phải EV/EBITDA. Theo dõi Thông tư SBV về phân loại nợ & trích lập.
- **Bất động sản (VHM, NLG, KDH, DXG…):** **giá trị hàng tồn kho & quỹ đất, người mua trả tiền trước (doanh thu chưa ghi nhận / backlog), dòng tiền dự án, đòn bẩy, lịch đáo hạn trái phiếu**. Rủi ro pháp lý dự án là biến số lớn.
- **Chứng khoán (SSI, VCI, VND, HCM…):** dư nợ **margin**, thị phần môi giới, tự doanh (proprietary book) — có tính chu kỳ cao theo thanh khoản thị trường.
- **Thép/vật liệu (HPG, HSG…):** chu kỳ hàng hoá, giá quặng/than, chênh HRC, công suất mới, xuất khẩu.
- **Tiêu dùng/bán lẻ (MWG, MSN, VNM, PNJ, FRT…):** SSSG (tăng trưởng cửa hàng cũ), số cửa hàng, biên gộp, vòng quay tồn kho, sức mua.
- **Điện/nước/dầu khí (GAS, POW, REE, NT2…):** hợp đồng dài hạn, giá đầu vào, quy hoạch điện (PDP8), yếu tố thời tiết (thuỷ điện).

---

## 5. Chất lượng & quản trị (governance / red flags)

Checklist cảnh báo cần soi trước khi tin vào con số:
- **Chất lượng lợi nhuận:** CFO/LNST thấp kéo dài; lợi nhuận chủ yếu từ đánh giá lại tài sản / bán công ty con.
- **Phải thu & tồn kho phình nhanh hơn doanh thu** → nghi ngờ ghi nhận doanh thu sớm.
- **Giao dịch bên liên quan (related-party)** lớn, cho vay/ứng trước cho bên liên quan.
- **Pha loãng:** phát hành riêng lẻ liên tục dưới giá thị trường, ESOP quá lớn.
- **Sở hữu chéo & cầm cố cổ phiếu** của lãnh đạo (margin call rủi ro).
- **Kiểm toán:** ý kiến ngoại trừ/nhấn mạnh; đổi công ty kiểm toán bất thường; chậm nộp BCTC.
- **Cơ cấu sở hữu:** tỷ lệ sở hữu nhà nước (thoái vốn?), free-float thấp (dễ bị lái), room ngoại còn/hết.

---

## 6. Từ phân tích → luận điểm đầu tư (thesis)

Một luận điểm tốt phải trả lời được, dưới dạng có thể kiểm chứng:
1. **Vì sao rẻ / sai giá?** (thị trường đang bỏ lỡ điều gì)
2. **Catalyst** nào và **khi nào** (KQKD, thoái vốn, nâng hạng thị trường, chính sách)?
3. **Định giá mục tiêu** theo ≥2 phương pháp + **biên an toàn**.
4. **Điều gì chứng minh mình sai** (falsification) + mức **cắt lỗ / review**.
5. **Vị thế & quản trị rủi ro** (position sizing, tương quan danh mục).

> Toàn bộ 6 bước trên được thiết kế để một AI agent thực thi tuần tự, mỗi bước đọc đúng lớp context cần thiết (L0 để lọc nhanh, L1 để lập kế hoạch, L2 khi cần số chi tiết) — xem [`../blueprint/06-openviking-agent-blueprint.md`](../blueprint/06-openviking-agent-blueprint.md).
