"""Lấy chỉ số cơ bản TTM (Vietcap IQ) cho universe → fundamentals.csv.
Usage: python scripts/fetch_fundamentals.py <out_csv>
"""
import json, subprocess, sys, time, os
import pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from vn_swing.data import UNIVERSE, SECTOR

URL = "https://iq.vietcap.com.vn/api/iq-insight-service/v1/company/{}/statistics-financial"

def fetch(sym):
    raw = subprocess.run(["curl", "-s", "-m", "20", "--compressed", "-A", "Mozilla/5.0",
                          "-H", "Referer: https://trading.vietcap.com.vn/", URL.format(sym)],
                         capture_output=True, text=True).stdout
    return pd.DataFrame(json.loads(raw)["data"])

rows = []
SYMS = sys.argv[2].split(",") if len(sys.argv) > 2 else UNIVERSE
for s in SYMS:
    try:
        d = fetch(s).sort_values(["yearReport", "quarter"]).reset_index(drop=True)
    except Exception as e:
        print("skip", s, e); continue
    d = d[d["pe"].notna()]
    last = d.iloc[-1]
    earn = d["marketCap"] / d["pe"].replace(0, float("nan"))
    g = earn.iloc[-1] / earn.iloc[-5] - 1 if len(d) >= 5 and earn.iloc[-5] > 0 else float("nan")
    hist = d[d["yearReport"] >= last["yearReport"] - 5]
    pe_med = hist["pe"][(hist["pe"] > 0) & (hist["pe"] < 100)].median()
    pb_med = hist["pb"][hist["pb"] > 0].median()
    rows.append(dict(symbol=s, sector=SECTOR.get(s, ""), period=f"Q{int(last['quarter'])}/{int(last['yearReport'])}",
                     mcap_bn=round(last["marketCap"] / 1e9), pe=round(last["pe"], 1), pe_5y_med=round(pe_med, 1),
                     pb=round(last["pb"], 2), pb_5y_med=round(pb_med, 2), roe=round(last["roe"] * 100, 1),
                     roa=round(last["roa"] * 100, 1), de=round(last.get("debtToEquity") or 0, 2),
                     npl=round((last.get("npl") or 0) * 100, 2), div_yield=round((last.get("dividendYield") or 0) * 100, 1),
                     ttm_profit_yoy=round(g * 100, 1)))
    print(s, rows[-1]["pe"], rows[-1]["roe"], rows[-1]["ttm_profit_yoy"])
    time.sleep(0.6)
pd.DataFrame(rows).to_csv(sys.argv[1], index=False)
