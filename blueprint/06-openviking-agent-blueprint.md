# 06 — Blueprint: OpenViking làm Context Database cho AI Agent phân tích cổ phiếu Việt Nam

> **Không phải khuyến nghị đầu tư.** Đây là bản thiết kế kỹ thuật (technical blueprint) minh hoạ cách tổ chức context cho một AI agent phân tích cơ bản. API dựa trên OpenViking Python SDK (`openviking_sdk.SyncHTTPClient`) và CLI `ov` tại thời điểm nghiên cứu — kiểm tra lại với [docs.openviking.ai](https://docs.openviking.ai/) trước khi triển khai.

## Vì sao dùng OpenViking cho bài toán phân tích cổ phiếu?

Phân tích cơ bản là bài toán **context-heavy**: một mã cổ phiếu kéo theo hàng chục BCTC quý, bản cáo bạch, nghị quyết ĐHĐCĐ, tin tức, dữ liệu ngành và vĩ mô. Nhồi tất cả vào prompt vừa **tốn token** vừa **nhiễu**. OpenViking giải quyết đúng 3 điểm đau này:

1. **Một filesystem cho mọi context** — mỗi tài liệu là một URI `viking://`, agent duyệt bằng `ls`/`tree`/`find` thay vì truy vấn một vector store hộp đen. → quyết định *đọc cái gì* trở nên tường minh, kiểm toán được (quan trọng với tài chính).
2. **Tải theo tầng L0/L1/L2** — agent đọc **L0 (abstract, ~100 token)** để lọc mã/tài liệu liên quan, **L1 (overview, ~2k token)** để lập kế hoạch phân tích, chỉ mở **L2 (chi tiết)** khi thật sự cần con số → cắt token đáng kể.
3. **Retrieval quan sát được (observable trajectory)** — mỗi truy vấn để lại đường đi duyệt thư mục. Với domain tài chính, **truy vết nguồn của một luận điểm** (provenance) là bắt buộc, không thể chấp nhận "hộp đen".
4. **Session → memory** — sau mỗi phiên phân tích, agent chắt lọc *sở thích người dùng* (phương pháp định giá ưa dùng, khẩu vị rủi ro) và *kinh nghiệm* (những red flag từng gặp) thành bộ nhớ dài hạn.

## Cây context đề xuất (`viking://`)

```
viking://
├── resources/
│   └── vn_market/
│       ├── .abstract                 # L0: "TTCK Việt Nam — HOSE/HNX/UPCoM, vĩ mô, ngành, mã"
│       ├── macro/                    # GDP, CPI, lãi suất SBV, tín dụng, tỷ giá VND/USD
│       │   ├── .overview
│       │   └── 2026Q2_macro.md
│       ├── regulation/               # Luật Chứng khoán, nâng hạng FTSE, hệ thống KRX, room ngoại
│       ├── sectors/
│       │   ├── banks/                # NIM, CASA, NPL, room tín dụng, CAR
│       │   ├── real_estate/          # quỹ đất, backlog, đáo hạn trái phiếu
│       │   ├── retail/               # SSSG, số cửa hàng
│       │   └── securities/           # margin, thị phần môi giới
│       └── tickers/
│           ├── PNJ/
│           │   ├── .abstract         # L0: mô tả 1 câu về PNJ + luận điểm hiện tại
│           │   ├── .overview         # L1: mô hình KD, tài chính tóm tắt, catalyst/rủi ro
│           │   ├── financials/       # L2: BCTC quý (P&L, BS, CF) theo kỳ
│           │   │   ├── 2026Q2.md
│           │   │   └── 2026Q1.md
│           │   ├── filings/          # nghị quyết ĐHĐCĐ, bản cáo bạch, công bố thông tin
│           │   ├── valuation/        # mô hình DCF/RIM, bảng peer, output định giá
│           │   └── news/             # tin tức đã gán ngày + nguồn
│           ├── FPT/
│           └── HPG/
└── user/
    └── {analyst_id}/
        ├── memories/
        │   └── preferences/
        │       ├── valuation_style   # "ưu tiên P/B–ROE cho bank, DCF cho tiêu dùng"
        │       ├── risk_appetite     # khẩu vị rủi ro, giới hạn vị thế
        │       └── output_format     # "bảng ratio + luận điểm + disclaimer"
        ├── skills/
        │   ├── dcf_valuation         # SKILL.md: quy trình DCF (mục §3.2 của khung)
        │   ├── bank_pb_roe           # định giá ngân hàng bằng P/B–ROE
        │   ├── ratio_screen          # sàng lọc ROE/nợ/định giá
        │   └── red_flag_check        # checklist §5 governance
        └── peers/
            └── portfolio/            # danh mục đang theo dõi, thesis & mốc review
```

**Nguyên tắc thiết kế:** mỗi thư mục (ngành, mã) đều có `.abstract`/`.overview` để agent phán đoán liên quan **trước khi** đọc file đầy đủ. Đây chính là cơ chế *directory recursive retrieval* của OpenViking: vector search định vị thư mục điểm cao nhất (vd `tickers/PNJ/financials/`) rồi mới drill-down.

## Vòng đời một phiên phân tích (agent loop)

```
1. Người dùng: "Cập nhật luận điểm PNJ sau BCTC quý mới"
2. Agent → find("PNJ định giá luận điểm", target_uri="viking://resources/vn_market/tickers")
          → khoanh vùng viking://.../tickers/PNJ/
3. Đọc L0/L1 của PNJ (abstract/overview) để nạp bối cảnh (rẻ token)
4. Mở L2 cần thiết: financials/2026Q2.md, valuation/*, news mới
5. Áp skill: ratio_screen → dcf_valuation/bank_pb_roe → red_flag_check
6. Sinh output: bảng tỷ số + định giá + luận điểm + rủi ro + DISCLAIMER
7. Commit session → OpenViking chắt lọc: cập nhật memories/preferences,
   ghi kinh nghiệm (vd "PNJ: chú ý biên gộp vàng miếng vs trang sức")
```

Mỗi bước 3–5 để lại **trajectory** → có thể trả lời "luận điểm này dựa trên file/số nào" (audit).

## Mã tham chiếu (Python SDK)

Xem [`../scripts/vn_stock_context.py`](../scripts/vn_stock_context.py) — script chạy được (khi có server OpenViking ở `http://localhost:1933`) để:
- Nạp tài liệu một mã (URL/file/thư mục) vào `viking://resources/vn_market/tickers/<TICKER>/`.
- Tạo cây thư mục ngành/mã với mô tả (`mkdir`).
- Truy hồi theo tầng (abstract → overview → find → read) đúng thứ tự tiết kiệm token.

## Ánh xạ khung phân tích 6 bước → OpenViking

| Bước (xem `docs/03`) | Context đọc | Cơ chế OpenViking |
|---|---|---|
| 1. Vĩ mô | `resources/vn_market/macro/` | `overview()` để nạp nhanh |
| 2. Ngành | `resources/vn_market/sectors/<x>/` | `find()` + `abstract()` lọc |
| 3. Doanh nghiệp | `tickers/<T>/financials`, `filings` | `read()` L2 khi cần số |
| 4. Định giá | skill `dcf_valuation` / `bank_pb_roe` | `skills/` + ghi output vào `valuation/` |
| 5. Rủi ro | skill `red_flag_check` + `news/` ([`docs/05`](../docs/05-rui-ro-va-nguon-du-lieu.md)) | checklist + tin mới nhất |
| 6. Thesis & theo dõi | `user/{id}/peers/portfolio/` | session → memory |

## Lưu ý triển khai thực tế

- **Nguồn dữ liệu:** OpenViking là *context DB*, không phải nguồn dữ liệu tài chính. Vẫn cần pipeline lấy BCTC/giá từ nguồn (xem [`../docs/05-rui-ro-va-nguon-du-lieu.md`](../docs/05-rui-ro-va-nguon-du-lieu.md) — CafeF, Vietstock, FiinTrade, SSI iBoard, Wichart, official hsx.vn/hnx.vn) rồi `add_resource` vào cây trên.
- **Tính tươi (freshness):** dữ liệu tài chính có tính thời điểm mạnh → gắn ngày/kỳ vào tên file & metadata, ưu tiên số kiểm toán, và làm mới `.abstract`/`.overview` khi có BCTC mới.
- **Kiểm chứng số:** agent phải trích dẫn URI nguồn cho mỗi con số trong luận điểm; không "chế" số. Đây là ranh giới an toàn quan trọng nhất của ứng dụng tài chính.
- **Tuân thủ:** nếu triển khai cho người dùng thật ở VN, chú ý pháp lý tư vấn đầu tư/chứng khoán và bảo vệ dữ liệu cá nhân (PDPL). Sản phẩm nên định vị là *công cụ hỗ trợ nghiên cứu*, kèm disclaimer, không phải khuyến nghị.
