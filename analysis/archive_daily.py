"""Archive a full run into analysis/daily/<as-of-date>/ — the per-day result log.

Replaces the old results/ mirror: every artifact of a run (REPORT.md, signals,
model_metrics, summary, charts/, PNGs, backtest CSVs, DAILY_DIGEST.md and the whole
debate/ folder incl. WHITEBOARD + DECISION + decision.json + notes/) is copied into
one dated folder, so results travel with the daily run log and git keeps history.

Also refreshes two stable pointers at analysis/daily/:
  - LATEST_DIGEST.md  (committed copy of the newest DAILY_DIGEST.md)
  - latest/           (local symlink → newest date folder; gitignored)

Usage: python archive_daily.py [run_dir]        (default: runs/latest)
"""
from __future__ import annotations

import glob
import os
import shutil
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")
DAILY = os.path.join(HERE, "daily")


def _latest_run() -> str | None:
    link = os.path.join(RUNS, "latest")
    if os.path.islink(link):
        return os.path.realpath(link)
    subs = sorted(glob.glob(os.path.join(RUNS, "log_run_*")))
    return subs[-1] if subs else None


def _as_of(run_dir: str) -> str:
    try:
        sig = pd.read_csv(os.path.join(run_dir, "signals_latest.csv"))
        return str(sig["date"].iloc[0])[:10]
    except Exception:
        # fallback: derive from the run folder timestamp name
        base = os.path.basename(run_dir).replace("log_run_", "")
        return base[:10] if base else "unknown"


def archive(run_dir: str) -> str:
    run_dir = os.path.realpath(run_dir)
    as_of = _as_of(run_dir)
    dest = os.path.join(DAILY, as_of)
    os.makedirs(DAILY, exist_ok=True)
    # copy the whole run into the dated folder (overwrite on same-day re-run)
    shutil.copytree(run_dir, dest, dirs_exist_ok=True)

    # stable pointers
    digest = os.path.join(dest, "DAILY_DIGEST.md")
    if os.path.isfile(digest):
        shutil.copy(digest, os.path.join(DAILY, "LATEST_DIGEST.md"))
    link = os.path.join(DAILY, "latest")  # local convenience symlink (gitignored)
    try:
        if os.path.islink(link) or os.path.exists(link):
            os.remove(link)
        os.symlink(as_of, link)
    except OSError:
        pass

    print(f"archived run → {dest}")
    return dest


if __name__ == "__main__":
    rd = sys.argv[1] if len(sys.argv) > 1 else _latest_run()
    if not rd or not os.path.isdir(rd):
        print("No run dir. Run `python run_analysis.py` first.")
        raise SystemExit(1)
    archive(rd)
