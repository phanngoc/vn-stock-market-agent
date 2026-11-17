"""Event study: what would a viewer earn by copying disclosed fund trades?

For each disclosed major-shareholder trade (fund, ticker, side, trade date T,
date the disclosure became public D), measure:
  - fund_edge: stock return T -> D (move the copier could not get)
  - copy_20: return from close of D to D+20 sessions, minus VN-Index (excess)
  - copy_now: return from close of D to the latest close, minus VN-Index
For SELL events the "copy" is avoiding the stock, so a NEGATIVE excess means
the fund was right.

Usage: python analysis/scripts/fund_event_study.py analysis/funds/<date>/events.csv
Writes event_study.csv next to the events file. Prices: vnstock VCI (adjusted).
"""
import sys, time
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from vn_swing.data import fetch_one  # noqa: E402

START, END = "2025-12-01", pd.Timestamp.today().strftime("%Y-%m-%d")


def prices(sym):
    df = fetch_one(sym, START, END)
    time.sleep(3.5)
    return df.set_index("date")["close"]


def at_or_after(s, d):
    idx = s.index.searchsorted(pd.Timestamp(d))
    return idx if idx < len(s) else None


def main(path):
    ev = pd.read_csv(path)
    vni = prices("VNINDEX")
    cache, rows = {}, []
    for e in ev.itertuples():
        if e.ticker not in cache:
            cache[e.ticker] = prices(e.ticker)
        s = cache[e.ticker]
        iT, iD = at_or_after(s, e.trade_date), at_or_after(s, e.public_date)
        jD = at_or_after(vni, s.index[iD])
        r = lambda ser, a, b: ser.iloc[b] / ser.iloc[a] - 1
        row = dict(fund=e.fund, ticker=e.ticker, side=e.side,
                   trade_date=s.index[iT].date(), public_date=s.index[iD].date(),
                   px_T=s.iloc[iT], px_D=s.iloc[iD], px_now=s.iloc[-1],
                   fund_edge=r(s, iT, iD))
        n20 = iD + 20
        if n20 < len(s):
            row["stk_20"] = r(s, iD, n20)
            row["exc_20"] = row["stk_20"] - r(vni, jD, jD + 20)
        row["stk_now"] = r(s, iD, len(s) - 1)
        row["exc_now"] = row["stk_now"] - r(vni, jD, len(vni) - 1)
        row["sessions"] = len(s) - 1 - iD
        sign = 1 if e.side == "BUY" else -1
        row["fund_right_now"] = sign * row["exc_now"] > 0
        rows.append(row)
    out = pd.DataFrame(rows)
    out.to_csv(Path(path).with_name("event_study.csv"), index=False)
    pd.set_option("display.width", 200)
    fmt = out.copy()
    for c in ["fund_edge", "stk_20", "exc_20", "stk_now", "exc_now"]:
        if c in fmt:
            fmt[c] = (fmt[c] * 100).round(1)
    print(fmt.drop(columns=["px_T"]).to_string(index=False))
    print("latest VNI", vni.index[-1].date(), vni.iloc[-1])


if __name__ == "__main__":
    main(sys.argv[1])
