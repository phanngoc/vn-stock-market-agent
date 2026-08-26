#!/usr/bin/env bash
# Cron wrapper cục bộ (macOS) — gọi orchestrator dùng chung run_daily_ci.sh.
# Lịch: crontab 08:30 các ngày giao dịch (T2–T6). KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ.
# Yêu cầu: Mac đang thức lúc 08:30, `claude` CLI đã đăng nhập, có mạng.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"
LOG_DIR="$REPO/analysis/runs/cron_logs"
mkdir -p "$LOG_DIR"
STAMP="$(date +%Y-%m-%d_%H-%M-%S)"
LOG="$LOG_DIR/cron_${STAMP}.log"

# PATH tối giản khi chạy từ cron: cần claude + pyenv python
export PATH="/Users/ngocp/.local/bin:/Users/ngocp/.pyenv/shims:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

{
  echo "==== vn-swing-daily cron @ ${STAMP} ===="
  bash "$SCRIPT_DIR/run_daily_ci.sh"
  echo "==== done @ $(date +%Y-%m-%d_%H-%M-%S) ===="
} >>"$LOG" 2>&1
