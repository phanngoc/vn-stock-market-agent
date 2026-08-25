# Vietnam Stock Market Research × AI-Agent Context Database (OpenViking)

**Nghiên cứu thị trường chứng khoán Việt Nam (2025–2026)** kết hợp **blueprint dùng [OpenViking](https://github.com/volcengine/OpenViking) làm context database cho AI agent phân tích cổ phiếu.**

> ⚠️ **KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ — NOT INVESTMENT ADVICE.**
> Tài liệu mang tính **giáo dục & phương pháp luận**. Số liệu tổng hợp từ nguồn công khai tại **25/8/2026**, có tính thời điểm; con số gắn nhãn *ước tính (est.)* cần kiểm chứng với công bố chính thức (HOSE/HNX, SSC, VSDC, SBV) trước khi ra bất kỳ quyết định nào. Tác giả không chịu trách nhiệm cho quyết định đầu tư dựa trên tài liệu này.

---

## Repo này là gì?

Hai lớp nội dung bổ trợ nhau — một dành cho *nhà phân tích*, một dành cho *kỹ sư AI agent*:

1. **Nghiên cứu thị trường (`docs/`)** — tổng quan, cấu trúc pháp lý & nâng hạng, khung phân tích cơ bản, cơ cấu ngành/vốn hoá, rủi ro & nguồn dữ liệu của TTCK Việt Nam.
2. **Blueprint AI agent (`blueprint/` + `scripts/`)** — cách tổ chức toàn bộ context (BCTC, tin, vĩ mô, ngành, mã) của một *agent phân tích cổ phiếu* trong virtual filesystem `viking://` của OpenViking, tận dụng tải theo tầng **L0/L1/L2** để tiết kiệm token và **retrieval quan sát được** để truy vết nguồn (provenance) — điều bắt buộc với ứng dụng tài chính.

**Vì sao ghép hai thứ này?** Phân tích cơ bản là bài toán *context-heavy*: một mã kéo theo hàng chục BCTC/tin/tài liệu. OpenViking — "context database for AI agents" của Volcengine — cho phép agent duyệt context như duyệt filesystem (`ls`/`tree`/`find`) thay vì truy vấn một vector store hộp đen, và chỉ nạp đến độ sâu mà tác vụ cần.

## Mục lục

| File | Nội dung |
|---|---|
| [`docs/01-tong-quan-thi-truong.md`](docs/01-tong-quan-thi-truong.md) | Ba sàn (HOSE/HNX/UPCoM), chỉ số VN-Index/VN30, quy mô, NĐT, vĩ mô |
| [`docs/02-cau-truc-quy-dinh.md`](docs/02-cau-truc-quy-dinh.md) | Luật CK, hệ thống KRX, nâng hạng FTSE/MSCI, NPF, room ngoại, TPDN |
| [`docs/03-phuong-phap-phan-tich-co-ban.md`](docs/03-phuong-phap-phan-tich-co-ban.md) | Khung 6 bước, bộ tỷ số, định giá (multiples/DCF/RIM/SOTP), red flags |
| [`docs/04-phan-tich-nganh-von-hoa.md`](docs/04-phan-tich-nganh-von-hoa.md) | Trọng số ngành, top mã vốn hoá, góc phân tích từng nhóm, chủ đề 2026 |
| [`docs/05-rui-ro-va-nguon-du-lieu.md`](docs/05-rui-ro-va-nguon-du-lieu.md) | Bản đồ rủi ro (tập trung, margin, TPDN, vốn ngoại) + nguồn dữ liệu |
| [`blueprint/06-openviking-agent-blueprint.md`](blueprint/06-openviking-agent-blueprint.md) | Cây `viking://`, vòng đời phiên phân tích, ánh xạ khung 6 bước |
| [`scripts/vn_stock_context.py`](scripts/vn_stock_context.py) | Script tham chiếu chạy được với OpenViking SDK |
| [`data/top_stocks.csv`](data/top_stocks.csv), [`data/sector_weights.csv`](data/sector_weights.csv) | Bảng máy đọc được |
| [`analysis/`](analysis/) + [`analysis/results/REPORT.md`](analysis/results/REPORT.md) | **Pipeline ML tìm cơ hội swing** (dữ liệu thật qua vnstock): LSTM + cây + hồi quy, backtest OOS, tín hiệu vào/chốt |

## Phân tích ML tìm cơ hội swing (dữ liệu thật)

Thư mục [`analysis/`](analysis/) chứa một pipeline machine-learning **chạy trên dữ liệu giá thật** (lấy qua [`vnstock`](https://github.com/thinh-vu/vnstock), nguồn VCI/Vietcap, 38 mã VN30-heavy, 2018→2026):

- **Nhiều thuật toán:** Logistic Regression, Random Forest, Gradient Boosting, XGBoost, **LSTM (PyTorch)**.
- **"Sóng" = triple-barrier:** vào tại giá đóng cửa; chốt lời **+8%** / cắt lỗ **−5%** / time-stop **25 phiên (~5 tuần)** → trả lời "vào mã nào, chốt/cắt ở đâu, giữ bao lâu".
- **Kết quả trung thực (out-of-sample 2025-01→2026-08):** AUC ~0.53–0.55 (edge yếu nhưng thực); lọc top-20% tín hiệu nâng win-rate ~0.38→~0.41 (breakeven 0.385). Trong kỳ thị trường tăng, **buy&hold ~+35%** — mô hình cho *lọc + kỷ luật rủi ro*, **không** phải "đánh bại thị trường".
- **Tín hiệu hiện tại + báo cáo:** [`analysis/results/REPORT.md`](analysis/results/REPORT.md), bảng máy đọc [`analysis/results/signals_latest.csv`](analysis/results/signals_latest.csv), so sánh mô hình [`analysis/results/model_metrics.csv`](analysis/results/model_metrics.csv).
- Chạy lại: `pip install -r analysis/requirements.txt && cd analysis && python run_analysis.py`.

> ⚠️ Thuần kỹ thuật, **không** phải khuyến nghị đầu tư; đọc kỹ mục *Hạn chế* trong REPORT (chưa mô phỏng trần/sàn ±7%, T+2, trượt giá, margin…).

## Ảnh chụp thị trường 2026 (snapshot)

- **VN-Index** ~1.768 điểm (21/8/2026), từng lập đỉnh ~1.937 (15/5/2026); +46,6% trong 12 tháng đến 5/2026.
- **Vốn hoá** toàn thị trường >~400 tỷ USD; **ngân hàng ~26% + BĐS ~27% = ~53%**.
- **Nâng hạng FTSE** Frontier → Secondary Emerging, **hiệu lực 21/9/2026** (MSCI mục tiêu riêng 2028–2030).
- **Hệ thống KRX** vận hành 5/5/2025 → hạ tầng cho T+0, phái sinh, bù trừ CCP.
- **~12,1 triệu tài khoản**, cá nhân chiếm **>80% giao dịch**; **margin kỷ lục** ~370–445 nghìn tỷ VND.
- **P/E ~15,0x** (giữa vùng lịch sử); GDP 2025 +8,02%, lãi suất SBV ~4,5%.

*(Chi tiết & cảnh báo độ tin cậy trong từng file.)*

## Dùng blueprint (quickstart)

```bash
# 1) Cài & chạy OpenViking (server ở :1933)
pip install openviking --upgrade
openviking-server init && openviking-server

# 2) Dựng cây context cho một mã và thử truy hồi theo tầng L0/L1/L2
python scripts/vn_stock_context.py --ticker PNJ \
  --doc <URL_hoặc_file_BCTC> --query "định giá và luận điểm đầu tư"

# 3) Duyệt như filesystem
ov tree viking://resources/vn_market -L 3
ov find "rủi ro đòn bẩy margin" --uri viking://resources/vn_market
```

Chi tiết thiết kế: [`blueprint/06-openviking-agent-blueprint.md`](blueprint/06-openviking-agent-blueprint.md).

## Nguồn (Sources)

Dữ liệu tổng hợp 25/8/2026 từ nguồn công khai. Chọn lọc:

**Chính thức / sàn / cơ quan:** HOSE (hsx.vn), HNX (hnx.vn), SSC/UBCKNN (ssc.gov.vn), VSDC (vsd.vn), SBV.
**Chỉ số/vĩ mô:** [Trading Economics – Vietnam](https://tradingeconomics.com/vietnam/stock-market), OECD Economic Survey Vietnam 2025, IMF Article IV 2025.
**Nâng hạng & giao dịch:** [LSEG/FTSE Russell country classification](https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2025/ftse-russell-country-classification-september-2025), [FTSE index notice](https://research.ftserussell.com/products/index-notices/home/getnotice/?id=2617682), [Vietnam Briefing](https://www.vietnam-briefing.com/news/vietnam-eases-foreign-access-to-stock-market-removes-pre-fund-requirements-for-stock-transactions.html/), [ASEAN Briefing](https://www.aseanbriefing.com/news/vietnam-eases-foreign-access-to-equities-what-the-new-rules-mean-for-global-investors/), [Duane Morris Vietnam](https://blogs.duanemorris.com/vietnam/2026/08/04/vietnam-countdown-to-emerging-market-status/).
**Hệ thống KRX:** [Vietstock](https://en.vietstock.vn/2025/05/krx-trading-system-takes-first-steps-36-612002.htm), [Vietnam News](https://vietnamnews.vn/economy/1717047/krx-system-officially-goes-live.html).
**Pháp lý:** [LuatVietnam – Luật 56/2024/QH15](https://english.luatvietnam.vn/tai-chinh/law-amend-law-on-securities-56-2024-qh15-380162-d1.html), [Baker McKenzie – TT giao dịch NĐT ngoại](https://www.bakermckenzie.com/en/insight/publications/2026/03/vietnam-new-securities-trading-rules-for-foreign-investors), [Baker McKenzie – NĐ TPDN](https://bakermckenzie.com/en/insight/publications/2026/06/vietnam-new-decree-on-corporate-bonds).
**NĐT / vốn ngoại / margin:** [VNEconomy – 12 triệu tài khoản](https://en.vneconomy.vn/vietnams-stock-market-surpasses-12-million-domestic-investor-accounts.htm), [FiinGroup – Securities Sector Brief 4/2025](https://fiingroup.vn/upload/docs/RE_Sector-Brief_Vietnam-Securities-Sector_%20April-2025.pdf), [The Investor – khối ngoại](https://theinvestor.vn/when-will-foreign-investors-return-to-net-buying-in-vietnams-stock-market-d18351.html), [The Investor – margin](https://theinvestor.vn/margin-lending-in-vietnams-stock-market-hits-record-but-not-worrisome-d17406.html), [Vietnam News – margin](https://vietnamnews.vn/economy/1716326/margin-lending-soars-to-historic-highs-amid-market-volatility.html).
**Ngành & vốn hoá:** [vietnam.vn – vốn hoá vượt 10 triệu tỷ](https://www.vietnam.vn/en/von-hoa-chung-khoan-vuot-10-trieu-ty-bat-dong-san-ngan-hang-chiem-qua-nua), [The Investor – Vingroup #1](https://theinvestor.vn/vietnams-private-conglomerate-vingroup-reclaims-market-capitalization-crown-after-5-years-d17054.html), [Vietnam News – Big Four top 5](https://vietnamnews.vn/economy/1664780/three-big-four-banks-enter-top-5-largest-companies-on-viet-nam-s-stock-market.html), [MBS – VN Dynamics 2026](https://www.mbs.com.vn/files/uploads/2026/01/VN-Dynamics_2026_Inthesearchoftruegrowthstories.pdf).
**Khủng hoảng TPDN:** [Vietnam News – Vạn Thịnh Phát](https://vietnamnews.vn/economy/1638702/money-recovered-from-massive-van-thinh-phat-bond-fraud-to-be-returned-to-rightful-owners-govt.html), [Global Law Experts](https://globallawexperts.com/vietnams-corporate-bond-market-under-scrutiny-the-government-inspectorates-landmark-conclusions-path-to-reform/), [Fulcrum – tín dụng/GDP](https://fulcrum.sg/vietnams-ambition-for-double-digit-growth-rationale-and-challenges/).
**Tỷ giá:** [UOB](https://theinvestor.vn/uobs-latest-usd-vnd-projections-for-2026-are-26300-in-q1-26100-in-q2-d17841.html), [MUFG Research](https://www.mufgresearch.com/fx/vietnam-modest-risk-of-overheating-amidst-very-positive-structural-reforms-11-december-2025/).
**Công cụ dữ liệu:** [vnstock (GitHub)](https://github.com/vnstock-official/vnstock).
**Nền tảng nghiên cứu:** [OpenViking (GitHub)](https://github.com/volcengine/OpenViking) · [docs.openviking.ai](https://docs.openviking.ai/).

## Ghi chú độ tin cậy (methodology & limits)

- Số liệu do một pipeline nghiên cứu web tổng hợp (25/8/2026); các mức chỉ số/vốn hoá **thay đổi theo phiên**. Con số *ước tính* đã được gắn nhãn rõ.
- Đây **không** phải báo cáo phân tích được cấp phép; không thay thế tư vấn đầu tư/pháp lý chuyên nghiệp.
- OpenViking là *context database* (lưu/truy hồi context), **không** phải nguồn dữ liệu tài chính — cần pipeline dữ liệu riêng (xem `docs/05`).

## License

- Nội dung nghiên cứu (`docs/`, `blueprint/`, `data/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — ghi công khi dùng lại.
- Mã trong `scripts/`: MIT.
- OpenViking là dự án riêng của Volcengine (AGPLv3) — repo này chỉ *tham chiếu*, không chứa mã nguồn OpenViking.
