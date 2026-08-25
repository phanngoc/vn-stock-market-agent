#!/usr/bin/env python3
"""
vn_stock_context.py — Reference layout of a Vietnamese-stock analyst agent's
context inside OpenViking (https://github.com/volcengine/OpenViking).

This is a *blueprint* script: it shows how the fundamental-analysis workflow in
docs/03 maps onto OpenViking's viking:// filesystem and its tiered L0/L1/L2
retrieval. It uses only public SDK methods verified against the OpenViking repo:

    SyncHTTPClient(url) . initialize() / is_healthy()
    add_resource(path, wait) -> {"root_uri": ...}
    mkdir(uri, description) / ls(uri) / glob(pattern, uri) / read(uri)
    abstract(uri) / overview(uri) / find(query, target_uri)

Prereqs:
    pip install openviking --upgrade
    openviking-server init && openviking-server        # server at :1933

Then:
    python scripts/vn_stock_context.py --ticker PNJ \
        --doc https://raw.githubusercontent.com/volcengine/OpenViking/main/README.md

NOTE: Not investment advice. OpenViking stores/retrieves context; it is NOT a
source of financial data. Feed real filings/prices from the sources in docs/07.
"""
from __future__ import annotations

import argparse
import sys

MARKET_ROOT = "viking://resources/vn_market"

# Sector + per-ticker skeleton the analyst agent browses. Each node gets an
# L0/L1 sidecar automatically so the agent can judge relevance before reading L2.
SECTORS = {
    "banks": "Ngân hàng: NIM, CASA, NPL, room tín dụng, CAR (P/B-ROE valuation)",
    "real_estate": "Bất động sản: quỹ đất, backlog, dòng tiền dự án, đáo hạn trái phiếu",
    "retail": "Bán lẻ/tiêu dùng: SSSG, số cửa hàng, biên gộp, vòng quay tồn kho",
    "securities": "Chứng khoán: dư nợ margin, thị phần môi giới, tự doanh (cyclical)",
    "materials": "Thép/vật liệu: chu kỳ hàng hoá, giá đầu vào, công suất, xuất khẩu",
    "utilities": "Điện/nước/dầu khí: hợp đồng dài hạn, giá đầu vào, quy hoạch điện",
}

TICKER_SUBDIRS = {
    "financials": "L2 — BCTC quý/năm (P&L, CĐKT, LCTT), ưu tiên số kiểm toán",
    "filings": "Nghị quyết ĐHĐCĐ, bản cáo bạch, công bố thông tin",
    "valuation": "Mô hình DCF/RIM, bảng peer, output định giá + biên an toàn",
    "news": "Tin tức có gán ngày + nguồn (provenance)",
}


def build_market_tree(client) -> None:
    """Create the sector/ticker skeleton with human-readable descriptions."""
    client.mkdir(uri=MARKET_ROOT, description="TTCK Việt Nam: vĩ mô, ngành, mã cổ phiếu")
    for name, desc in (
        ("macro", "Vĩ mô: GDP, CPI, lãi suất SBV, tín dụng, tỷ giá VND/USD"),
        ("regulation", "Luật CK, nâng hạng FTSE, hệ thống KRX, room ngoại"),
        ("sectors", "Phân tích ngành"),
        ("tickers", "Phân tích từng mã"),
    ):
        client.mkdir(uri=f"{MARKET_ROOT}/{name}", description=desc)
    for name, desc in SECTORS.items():
        client.mkdir(uri=f"{MARKET_ROOT}/sectors/{name}", description=desc)


def add_ticker(client, ticker: str, docs: list[str]) -> str:
    """Create tickers/<T>/ subtree and ingest documents into financials/."""
    ticker = ticker.upper()
    base = f"{MARKET_ROOT}/tickers/{ticker}"
    client.mkdir(uri=base, description=f"Phân tích cơ bản mã {ticker}")
    for sub, desc in TICKER_SUBDIRS.items():
        client.mkdir(uri=f"{base}/{sub}", description=desc)

    for doc in docs:
        print(f"  + add_resource({doc}) -> {base}/financials")
        res = client.add_resource(path=doc, wait=True)
        print(f"    root_uri: {res.get('root_uri', '?')}")
    return base


def tiered_recall(client, base_uri: str, query: str) -> None:
    """Demonstrate the token-saving L0 -> L1 -> find -> L2 read order."""
    print("\n[L0] abstract (lọc nhanh ~100 token):")
    print("   ", _safe(lambda: client.abstract(uri=base_uri)))

    print("[L1] overview (lập kế hoạch ~2k token):")
    print("   ", _safe(lambda: client.overview(uri=base_uri))[:400], "...")

    print(f"\n[find] semantic search: {query!r}")
    results = _safe(lambda: client.find(query=query, target_uri=base_uri)) or {}
    for r in (results.get("resources") or [])[:5]:
        print(f"    {r.get('uri')} (score={r.get('score', 0.0):.4f})")

    print("\n[L2] read first matching detail file:")
    matches = (_safe(lambda: client.glob(pattern="**/*", uri=base_uri)) or {}).get("matches", [])
    if matches:
        print("   ", _safe(lambda: client.read(uri=matches[0]))[:300], "...")


def _safe(fn):
    try:
        return fn()
    except Exception as e:  # keep the blueprint runnable even if a call is unsupported
        return f"<skipped: {e}>"


def main() -> int:
    p = argparse.ArgumentParser(description="OpenViking context layout for a VN-stock agent")
    p.add_argument("--url", default="http://localhost:1933")
    p.add_argument("--ticker", default="PNJ")
    p.add_argument("--doc", action="append", default=[], help="URL/file/dir to ingest (repeatable)")
    p.add_argument("--query", default="định giá và luận điểm đầu tư")
    args = p.parse_args()

    try:
        from openviking_sdk import SyncHTTPClient
    except ImportError:
        print("Install first: pip install openviking --upgrade", file=sys.stderr)
        return 1

    client = SyncHTTPClient(url=args.url)
    try:
        client.initialize()
        if not client.is_healthy():
            print("Warning: some OpenViking components are not healthy", file=sys.stderr)

        build_market_tree(client)
        base = add_ticker(client, args.ticker, args.doc)
        tiered_recall(client, base, args.query)
        print("\nDone. Browse with:  ov tree viking://resources/vn_market -L 3")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        print("Is the OpenViking server running at", args.url, "?", file=sys.stderr)
        return 1
    finally:
        try:
            client.close()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
