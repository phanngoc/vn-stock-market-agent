"""Compile all agent notes into the shared WHITEBOARD.md, in A→B→C→D→E order.

After the 5 debate agents each write their own `notes/<X>.md` (so there is no
concurrent-write race), this merges them into the whiteboard's PHIÊN sections.
Idempotent: a note already present on the board is skipped, so re-running is safe.

Usage: python debate/compile.py [run_dir]      (default: runs/latest)
"""
from __future__ import annotations

import glob
import os
import sys

from assemble import append_to_section

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "..", "runs")

# note file -> whiteboard section substring, in debate order
PLAN = [
    ("A_technical.md", "PHIÊN 1"),
    ("B_news.md", "PHIÊN 1"),
    ("C_bull.md", "PHIÊN 2"),
    ("D_bear.md", "PHIÊN 3"),
    ("E_cio.md", "PHIÊN 4"),
]


def _latest_run() -> str | None:
    link = os.path.join(RUNS, "latest")
    if os.path.islink(link):
        return os.path.realpath(link)
    subs = sorted(glob.glob(os.path.join(RUNS, "log_run_*")))
    return subs[-1] if subs else None


def compile_whiteboard(run_dir: str) -> str:
    deb = os.path.join(run_dir, "debate")
    wb = os.path.join(deb, "WHITEBOARD.md")
    notes = os.path.join(deb, "notes")
    if not os.path.isfile(wb):
        raise SystemExit(f"No WHITEBOARD.md in {deb} — run scaffold.py first.")
    board = open(wb, encoding="utf-8").read()
    merged = 0
    for fname, section in PLAN:
        path = os.path.join(notes, fname)
        if not os.path.isfile(path):
            print(f"  (skip {fname}: not written)")
            continue
        head = open(path, encoding="utf-8").read().strip().splitlines()[0].strip()
        if head and head in board:
            print(f"  (skip {fname}: already on board)")
            continue
        append_to_section(wb, section, path)
        board = open(wb, encoding="utf-8").read()  # refresh for idempotency check
        merged += 1
    print(f"compiled {merged} note(s) -> {wb}")
    return wb


if __name__ == "__main__":
    rd = sys.argv[1] if len(sys.argv) > 1 else _latest_run()
    if not rd or not os.path.isdir(rd):
        print("No run dir. Run `python run_analysis.py` first.")
        raise SystemExit(1)
    compile_whiteboard(rd)
