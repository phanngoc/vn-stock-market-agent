"""Merge an agent's note file into the shared WHITEBOARD.md, under a named section.

The whiteboard is the single board everyone reads; each agent writes its own note
(to avoid concurrent-write races), and the orchestrator appends notes into the board
in order. Content is inserted at the END of the target section (before the next
`# 🗣️` header or `---` boundary), preserving A→B→C→D→E ordering.

Usage:
  python debate/assemble.py <whiteboard.md> "<section substring>" <note.md>
  # e.g. python debate/assemble.py runs/latest/debate/WHITEBOARD.md "PHIÊN 1" runs/latest/debate/notes/A_technical.md
"""
from __future__ import annotations

import sys


def append_to_section(wb_path: str, section_sub: str, note_path: str) -> None:
    lines = open(wb_path, encoding="utf-8").read().splitlines()
    note = open(note_path, encoding="utf-8").read().rstrip()

    # locate section header line
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("# 🗣️") and section_sub in ln:
            start = i
            break
    if start is None:
        raise SystemExit(f"Section '{section_sub}' not found in {wb_path}")

    # find end of section = next top-level 🗣️ header after start
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("# 🗣️"):
            end = j
            break

    # trim trailing blank/separator lines within the section, then insert note
    insert_at = end
    while insert_at - 1 > start and (lines[insert_at - 1].strip() in ("", "---")):
        insert_at -= 1

    block = ["", note, ""]
    new = lines[:insert_at] + block + lines[insert_at:]
    open(wb_path, "w", encoding="utf-8").write("\n".join(new) + "\n")
    print(f"  merged {note_path.split('/')[-1]} -> section '{section_sub}'")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        raise SystemExit(1)
    append_to_section(sys.argv[1], sys.argv[2], sys.argv[3])
