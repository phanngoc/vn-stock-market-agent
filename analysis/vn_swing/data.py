"""Fetch & cache real Vietnamese daily OHLCV via vnstock (VCI source).

Not investment advice. Data source: Vietcap (VCI) through the vnstock library
(https://github.com/thinh-vu/vnstock). Prices are in thousand VND.
"""
from __future__ import annotations

import os
import time
import warnings

import pandas as pd

warnings.filterwarnings("ignore")

CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "data_cache")

# Liquid large/mid-cap universe across the main sectors (VN30-heavy).
UNIVERSE = [
    # Banks
    "VCB", "BID", "CTG", "TCB", "VPB", "ACB", "MBB", "STB", "HDB", "TPB",
    # Real estate
    "VIC", "VHM", "VRE", "KDH", "NLG", "DXG", "PDR",
    # Retail / consumer / F&B
    "MWG", "PNJ", "FRT", "VNM", "MSN", "SAB",
    # Securities
    "SSI", "VCI", "VND", "HCM",
    # Industrials / materials / energy / tech
    "HPG", "HSG", "GAS", "PLX", "DGC", "DCM", "DPM", "POW", "REE", "GVR", "FPT",
]

SECTOR = {
    **{t: "Bank" for t in ["VCB", "BID", "CTG", "TCB", "VPB", "ACB", "MBB", "STB", "HDB", "TPB"]},
    **{t: "RealEstate" for t in ["VIC", "VHM", "VRE", "KDH", "NLG", "DXG", "PDR"]},
    **{t: "Retail/Consumer" for t in ["MWG", "PNJ", "FRT", "VNM", "MSN", "SAB"]},
    **{t: "Securities" for t in ["SSI", "VCI", "VND", "HCM"]},
    "HPG": "Materials", "HSG": "Materials", "DGC": "Materials",
    "DCM": "Materials", "DPM": "Materials", "GVR": "Materials",
    "GAS": "Energy", "PLX": "Energy", "POW": "Utilities", "REE": "Utilities",
    "FPT": "Technology",
}


def _cache_path(symbol: str) -> str:
    return os.path.join(CACHE_DIR, f"{symbol}.csv")


_RATE_MARKERS = ("giới hạn", "rate limit", "maximum api request", "too many requests", "429")


def _is_rate_limit(msg: str) -> bool:
    m = msg.lower()
    return any(k in m for k in _RATE_MARKERS)


def fetch_one(symbol: str, start: str, end: str, retries: int = 5) -> pd.DataFrame | None:
    """Fetch one symbol's daily history from VCI, bypassing Company init.

    Handles VCI's Guest rate limit (20 req/min): on a rate-limit error, waits the
    server-suggested time (parsed from the message, default 50s) and retries.
    """
    from vnstock.explorer.vci import Quote

    for attempt in range(retries):
        try:
            q = Quote(symbol=symbol)
            df = q.history(start=start, end=end, interval="1D")
            if df is None or len(df) == 0:
                return None
            df = df.rename(columns={"time": "date"})
            df["date"] = pd.to_datetime(df["date"])
            df = df.sort_values("date").reset_index(drop=True)
            df["symbol"] = symbol
            return df[["date", "symbol", "open", "high", "low", "close", "volume"]]
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            last = attempt == retries - 1
            if _is_rate_limit(msg):
                import re
                mm = re.search(r"(\d+)\s*(?:giây|second)", msg)
                wait = (int(mm.group(1)) + 3) if mm else 50
                print(f"  [{symbol}] rate-limit VCI → chờ {wait}s rồi thử lại ({attempt + 1}/{retries})")
                time.sleep(wait)
                continue
            if last:
                print(f"  [{symbol}] failed after {retries} tries: {e}")
                return None
            time.sleep(1.5 * (attempt + 1))
    return None


def load_universe(start: str, end: str, universe=None, use_cache: bool = True) -> dict[str, pd.DataFrame]:
    """Return {symbol: OHLCV DataFrame}. Caches per-symbol CSV.

    Throttling: sleeps VN_FETCH_DELAY seconds (default 3.5) between *actual* network
    fetches to stay under VCI's Guest 20-req/min limit (cache hits don't sleep).
    Freshness: set VN_REFRESH=1 to incrementally append new bars to a warm cache
    (1 small request/symbol) — used by the daily CI/cron job so data stays current.
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    universe = universe or UNIVERSE
    delay = float(os.environ.get("VN_FETCH_DELAY", "3.5"))
    refresh = os.environ.get("VN_REFRESH", "0").lower() not in ("0", "", "false", "no")
    end_ts = pd.to_datetime(end)
    out: dict[str, pd.DataFrame] = {}
    for i, sym in enumerate(universe, 1):
        cp = _cache_path(sym)
        if use_cache and os.path.exists(cp):
            df = pd.read_csv(cp, parse_dates=["date"])
            if refresh and len(df):
                last = df["date"].max()
                if end_ts.normalize() > last.normalize():
                    frm = (last + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
                    new = fetch_one(sym, frm, end)
                    time.sleep(delay)
                    if new is not None and len(new):
                        df = (pd.concat([df, new])
                              .drop_duplicates(subset="date", keep="last")
                              .sort_values("date").reset_index(drop=True))
                        df.to_csv(cp, index=False)
        else:
            df = fetch_one(sym, start, end)
            if df is not None and len(df) > 0:
                df.to_csv(cp, index=False)
            time.sleep(delay)  # be gentle with the API (Guest 20 req/min)
        if df is not None and len(df) >= 250:  # need ~1y minimum
            out[sym] = df
            print(f"  [{i:>2}/{len(universe)}] {sym:5} rows={len(df):>5}  {df['date'].min().date()}→{df['date'].max().date()}")
        else:
            print(f"  [{i:>2}/{len(universe)}] {sym:5} SKIPPED (insufficient data)")
    return out


if __name__ == "__main__":
    data = load_universe("2018-01-01", "2026-08-25", universe=["FPT", "HPG", "VCB"])
    print("Loaded:", list(data.keys()))
