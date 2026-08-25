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


def fetch_one(symbol: str, start: str, end: str, retries: int = 3) -> pd.DataFrame | None:
    """Fetch one symbol's daily history from VCI, bypassing Company init."""
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
            if attempt == retries - 1:
                print(f"  [{symbol}] failed after {retries} tries: {e}")
                return None
            time.sleep(1.5 * (attempt + 1))
    return None


def load_universe(start: str, end: str, universe=None, use_cache: bool = True) -> dict[str, pd.DataFrame]:
    """Return {symbol: OHLCV DataFrame}. Caches per-symbol parquet."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    universe = universe or UNIVERSE
    out: dict[str, pd.DataFrame] = {}
    for i, sym in enumerate(universe, 1):
        cp = _cache_path(sym)
        if use_cache and os.path.exists(cp):
            df = pd.read_csv(cp, parse_dates=["date"])
        else:
            df = fetch_one(sym, start, end)
            if df is not None and len(df) > 0:
                df.to_csv(cp, index=False)
            time.sleep(0.4)  # be gentle with the API
        if df is not None and len(df) >= 250:  # need ~1y minimum
            out[sym] = df
            print(f"  [{i:>2}/{len(universe)}] {sym:5} rows={len(df):>5}  {df['date'].min().date()}→{df['date'].max().date()}")
        else:
            print(f"  [{i:>2}/{len(universe)}] {sym:5} SKIPPED (insufficient data)")
    return out


if __name__ == "__main__":
    data = load_universe("2018-01-01", "2026-08-25", universe=["FPT", "HPG", "VCB"])
    print("Loaded:", list(data.keys()))
