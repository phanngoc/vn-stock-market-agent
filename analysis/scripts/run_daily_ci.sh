#!/usr/bin/env bash
# Orchestrator headless cho bản tin swing hằng ngày — dùng cho CI (GitHub Actions) VÀ cron cục bộ.
# Path-relative (tự tìm repo root), KHÔNG phụ thuộc Workflow tool tương tác.
# Chuỗi: pipeline ML -> scaffold -> 5 agent (A,B,C,D,E qua `claude -p`) -> compile -> daily_digest.
# Degrade gracefully: nếu phần LLM lỗi, daily_digest.py vẫn ra bản quant-only.
# KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"       # scripts/ nằm ở analysis/scripts
AN="$REPO/analysis"
AG="$REPO/.claude/skills/vn-swing-debate/agents"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"
CLAUDE_FLAGS="--dangerously-skip-permissions"
[ -n "${CLAUDE_MODEL:-}" ] && CLAUDE_FLAGS="$CLAUDE_FLAGS --model $CLAUDE_MODEL"

cd "$AN"

# Freshness + throttle cho VCI (Guest 20 req/min): làm mới cache tăng dần + giãn nhịp fetch.
export VN_REFRESH="${VN_REFRESH:-1}"
export VN_FETCH_DELAY="${VN_FETCH_DELAY:-4}"

# ---- 1. Pipeline + scaffold (BẮT BUỘC thành công; lỗi -> abort, không commit) ----
set -e
echo "== [1/6] pipeline: run_analysis.py =="
python run_analysis.py
echo "== [1/6] scaffold whiteboard =="
python debate/scaffold.py runs/latest
RUN_DIR="$(python -c "import os;print(os.path.realpath('runs/latest'))")"
set +e
NOTES="$RUN_DIR/debate/notes"
AS_OF="$(python -c "import pandas as pd;print(pd.read_csv('$RUN_DIR/signals_latest.csv')['date'].iloc[0])" 2>/dev/null)"
echo "RUN_DIR=$RUN_DIR  AS_OF=$AS_OF"

DIS='KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ. Không bịa số/tin (nếu không chắc ghi "chưa kiểm chứng"). Tôn trọng edge mô hình yếu (AUC ~0.53-0.55).'

run_agent () {  # $1=label  $2=prompt
  echo "== agent: $1 =="
  if ! "$CLAUDE_BIN" -p "$2" $CLAUDE_FLAGS; then
    echo "WARN: agent $1 thất bại (bỏ qua, digest sẽ tự fallback)."
  fi
}

# ---- 2. Bằng chứng: A kỹ thuật, B news (tuần tự trong CI) ----
run_agent "A:technical" "Bạn là Agent A (phân tích kỹ thuật) trong hội đồng đầu tư swing TTCK Việt Nam. RUN_DIR=$RUN_DIR, dữ liệu as-of $AS_OF. Đọc kỹ hướng dẫn $AG/A_technical.md và LÀM ĐÚNG (thay <RUN_DIR>=$RUN_DIR). Đọc $RUN_DIR/signals_latest.csv (RSI, trend, vol_ratio) — chỉ kỹ thuật, không tin tức. Write kết quả vào $NOTES/A_technical.md (đúng dòng tiêu đề template). $DIS"
run_agent "B:news"      "Bạn là Agent B (news/cơ bản) trong hội đồng đầu tư swing TTCK Việt Nam. RUN_DIR=$RUN_DIR, as-of $AS_OF. Đọc $AG/B_news.md và LÀM ĐÚNG. DÙNG WebSearch/WebFetch tìm tin MỚI cho từng mã trong $RUN_DIR/signals_latest.csv + vĩ mô; MỖI khẳng định kèm link nguồn. Write vào $NOTES/B_news.md. $DIS"

# ---- 3. Tranh luận: C bò -> D gấu ----
run_agent "C:bull" "Bạn là Agent C (phe BÒ). RUN_DIR=$RUN_DIR. Đọc $AG/C_bull.md và LÀM ĐÚNG. Đọc THẲNG $NOTES/A_technical.md và $NOTES/B_news.md (bằng chứng A,B) + $RUN_DIR/signals_latest.csv. Dựng luận điểm MUA mạnh nhất nhưng chỉ dùng điểm tích cực CÓ THẬT. Write vào $NOTES/C_bull.md. $DIS"
run_agent "D:bear" "Bạn là Agent D (phe GẤU/phản biện). RUN_DIR=$RUN_DIR. Đọc $AG/D_bear.md và LÀM ĐÚNG. Đọc THẲNG $NOTES/A_technical.md, $NOTES/B_news.md, $NOTES/C_bull.md; PHẢN BIỆN TRỰC TIẾP từng luận điểm của Agent C + rủi ro downside. Write vào $NOTES/D_bear.md. $DIS"

# ---- 4. Quyết định CIO ----
run_agent "E:cio" "Bạn là Agent E (Giám đốc Chiến lược/CIO, quyết định cuối). RUN_DIR=$RUN_DIR. Đọc $AG/E_cio.md và LÀM ĐÚNG. Đọc THẲNG toàn bộ note $NOTES/{A_technical,B_news,C_bull,D_bear}.md + $RUN_DIR/signals_latest.csv. Ưu tiên BẢO TOÀN VỐN; bò≈gấu -> THEO DÕI. Ghi ĐỦ 3 file: $RUN_DIR/debate/DECISION.md, $NOTES/E_cio.md, và $RUN_DIR/debate/decision.json (đúng schema template, parse được, KHÔNG comment; mỗi mã ứng viên 1 pick). $DIS"

# ---- 5. Compile whiteboard + render bản tin (LUÔN chạy) ----
echo "== [5/6] compile whiteboard =="
python debate/compile.py "$RUN_DIR" || echo "WARN: compile lỗi"
echo "== [6/6] render DAILY_DIGEST.md =="
python daily_digest.py "$RUN_DIR" || { echo "ERROR: daily_digest lỗi"; exit 1; }

# ---- 6. Mirror artifact tranh luận + lưu bản lịch sử theo ngày (để commit) ----
mkdir -p "$AN/results"
cp -r "$RUN_DIR/debate" "$AN/results/debate" 2>/dev/null || true
ARCH="$AN/daily/$AS_OF"
mkdir -p "$ARCH"
cp "$RUN_DIR/DAILY_DIGEST.md" "$ARCH/DAILY_DIGEST.md" 2>/dev/null || true
cp "$RUN_DIR/debate/DECISION.md" "$ARCH/DECISION.md" 2>/dev/null || true
cp "$RUN_DIR/debate/WHITEBOARD.md" "$ARCH/WHITEBOARD.md" 2>/dev/null || true   # toàn bộ tranh luận A→E
cp "$RUN_DIR/debate/decision.json" "$ARCH/decision.json" 2>/dev/null || true
cp "$RUN_DIR/signals_latest.csv" "$ARCH/signals_latest.csv" 2>/dev/null || true
cp -r "$RUN_DIR/debate/notes" "$ARCH/notes" 2>/dev/null || true                # note riêng từng agent
# con trỏ ổn định tới bản mới nhất
cp "$RUN_DIR/DAILY_DIGEST.md" "$AN/daily/LATEST_DIGEST.md" 2>/dev/null || true

echo "DONE. Digest: $RUN_DIR/DAILY_DIGEST.md  | archive: $ARCH"
