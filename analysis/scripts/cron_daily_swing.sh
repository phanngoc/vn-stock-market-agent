#!/usr/bin/env bash
# Bản tin swing hằng ngày — chạy workflow vn-swing-daily headless qua Claude Code CLI.
# Lịch: crontab 08:30 các ngày giao dịch (T2–T6). KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.
#
# Yêu cầu: Mac đang thức lúc 08:30, `claude` CLI đã đăng nhập, có mạng.
# Log mỗi lần chạy: analysis/runs/cron_logs/ (đã gitignore theo runs/).
set -euo pipefail

REPO="/Users/ngocp/goterm-workspace/vn-stock-market-agent"
WF="$REPO/.claude/workflows/vn-swing-daily.js"
LOG_DIR="$REPO/analysis/runs/cron_logs"
mkdir -p "$LOG_DIR"
STAMP="$(date +%Y-%m-%d_%H-%M-%S)"
LOG="$LOG_DIR/cron_${STAMP}.log"

# đảm bảo PATH có claude + pyenv python khi chạy từ cron (môi trường tối giản)
export PATH="/Users/ngocp/.local/bin:/Users/ngocp/.pyenv/shims:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
cd "$REPO"

{
  echo "==== vn-swing-daily cron @ ${STAMP} ===="
  claude -p "Chạy bản tin swing hằng ngày: gọi Workflow({scriptPath: \"${WF}\"}) rồi khi xong in ra đường dẫn tuyệt đối của DAILY_DIGEST.md vừa tạo. Đây là yêu cầu chạy workflow trực tiếp." \
    --dangerously-skip-permissions
  echo "==== done @ $(date +%Y-%m-%d_%H-%M-%S) ===="
} >>"$LOG" 2>&1
