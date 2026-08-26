export const meta = {
  name: 'vn-swing-daily',
  description: 'Chạy 1 phát: pipeline ML swing + hội đồng 5 tác nhân tranh luận → 1 bản tin đầu tư hằng ngày (VN stock)',
  phases: [
    { title: 'Pipeline', detail: 'run_analysis.py (dữ liệu thật vnstock/VCI) + scaffold whiteboard' },
    { title: 'Evidence', detail: 'Agent A kỹ thuật + Agent B news (song song)' },
    { title: 'Debate', detail: 'Agent C bò → Agent D gấu (phản biện)' },
    { title: 'Decision', detail: 'Agent E CIO → DECISION.md + decision.json' },
    { title: 'Digest', detail: 'compile whiteboard + render DAILY_DIGEST.md' },
  ],
}

// ---- paths (absolute) ----
const ROOT = '/Users/ngocp/goterm-workspace/vn-stock-market-agent'
const AN = `${ROOT}/analysis`
const AG = `${ROOT}/.claude/skills/vn-swing-debate/agents`
const DIS = 'KHÔNG PHẢI KHUYẾN NGHỊ ĐẦU TƯ. Không bịa số/tin — nếu không chắc, ghi "chưa kiểm chứng". Tôn trọng edge mô hình yếu (AUC ~0.53–0.55).'

const RUN_SCHEMA = {
  type: 'object',
  required: ['run_dir', 'as_of', 'best_model', 'tickers'],
  properties: {
    run_dir: { type: 'string', description: 'đường dẫn TUYỆT ĐỐI của run dir mới (realpath của runs/latest)' },
    as_of: { type: 'string', description: 'ngày dữ liệu (YYYY-MM-DD) từ signals_latest.csv' },
    best_model: { type: 'string' },
    tickers: { type: 'array', items: { type: 'string' }, description: 'top-5 mã theo score' },
  },
}

// ---------- Phase 1: quant pipeline + scaffold ----------
phase('Pipeline')
const run = await agent(
  `Bạn chạy pipeline phân tích swing TTCK Việt Nam rồi dựng whiteboard tranh luận.
Chạy TUẦN TỰ bằng Bash (python = pyenv 3.12.4 đã có vnstock/torch/sklearn/xgboost):
1. cd ${AN} && python run_analysis.py   (fetch dữ liệu thật -> features -> 5 mô hình + LSTM -> backtest OOS -> tín hiệu -> charts; tạo run dir mới, cập nhật runs/latest). Có thể mất vài phút — chờ xong.
2. cd ${AN} && python debate/scaffold.py runs/latest   (tạo runs/latest/debate/{WHITEBOARD.md, notes/, DECISION.md}).
3. Lấy đường dẫn tuyệt đối: python -c "import os;print(os.path.realpath('${AN}/runs/latest'))"
4. Đọc runs/latest/signals_latest.csv (top-5 mã cột symbol) và summary.json (best_model, cột date lấy as_of).
Trả về JSON đúng schema: run_dir (tuyệt đối), as_of, best_model, tickers (top-5).
Nếu run_analysis.py lỗi, báo lỗi rõ ràng và dừng.`,
  { label: 'pipeline+scaffold', phase: 'Pipeline', schema: RUN_SCHEMA },
)
if (!run || !run.run_dir) {
  return { error: 'pipeline failed', run }
}
const RUN_DIR = run.run_dir
const NOTES = `${RUN_DIR}/debate/notes`
log(`Run dir: ${RUN_DIR} · as-of ${run.as_of} · best=${run.best_model} · top: ${(run.tickers || []).join(', ')}`)

// helper: build a debate-agent prompt that loads its template and targets this run
const deb = (letter, role, tmpl, reads, out, extra) =>
  `Bạn là Agent ${letter} (${role}) trong hội đồng đầu tư swing TTCK Việt Nam.
RUN_DIR = ${RUN_DIR} · dữ liệu as-of ${run.as_of}.
1. Đọc kỹ hướng dẫn vai trò tại ${AG}/${tmpl} và LÀM ĐÚNG theo đó (thay <RUN_DIR> = ${RUN_DIR}).
2. Đọc dữ liệu: ${RUN_DIR}/signals_latest.csv${reads ? ' ; ' + reads : ''}.
${extra || ''}3. Write kết quả vào ${out} (bắt đầu đúng dòng tiêu đề template yêu cầu, có mốc thời gian).
Nguyên tắc: ${DIS}
Trả về đường dẫn file đã ghi.`

// ---------- Phase 2: evidence (A technical || B news) ----------
phase('Evidence')
await parallel([
  () => agent(
    deb('A', 'phân tích kỹ thuật', 'A_technical.md', '', `${NOTES}/A_technical.md`,
      'Chỉ dùng số trong signals_latest.csv (RSI, trend, vol_ratio) và chart nếu xem được — không bàn tin tức.\n'),
    { label: 'A:technical', phase: 'Evidence', agentType: 'general-purpose' },
  ),
  () => agent(
    deb('B', 'phân tích news/cơ bản', 'B_news.md', '', `${NOTES}/B_news.md`,
      'DÙNG WebSearch/WebFetch để tìm tin MỚI thời điểm hiện tại cho từng mã + vĩ mô; MỖI khẳng định kèm link nguồn (cafef/vietstock/tinnhanhchungkhoan...). Phân biệt sự kiện đã xảy ra vs kỳ vọng.\n'),
    { label: 'B:news', phase: 'Evidence', agentType: 'general-purpose' },
  ),
])

// ---------- Phase 3: bull then bear ----------
phase('Debate')
await agent(
  deb('C', 'phe BÒ', 'C_bull.md',
    `${NOTES}/A_technical.md và ${NOTES}/B_news.md (bằng chứng của A và B — whiteboard chưa gộp, đọc thẳng note)`,
    `${NOTES}/C_bull.md`,
    'Dựng luận điểm MUA mạnh nhất nhưng CHỈ khuếch đại điểm tích cực CÓ THẬT trong note của A/B. Trích tên agent khi dùng bằng chứng.\n'),
  { label: 'C:bull', phase: 'Debate', agentType: 'general-purpose' },
)
await agent(
  deb('D', 'phe GẤU / phản biện', 'D_bear.md',
    `${NOTES}/A_technical.md, ${NOTES}/B_news.md, ${NOTES}/C_bull.md (đọc thẳng các note; PHẢN BIỆN TRỰC TIẾP từng luận điểm của Agent C)`,
    `${NOTES}/D_bear.md`,
    'Stress-test luận điểm bò: mã dưới MA50 = bắt dao rơi? vol thấp? catalyst đã vào giá? rủi ro hệ thống (margin, T+2, ±7%)? Không bịa tin xấu.\n'),
  { label: 'D:bear', phase: 'Debate', agentType: 'general-purpose' },
)

// ---------- Phase 4: CIO decision ----------
phase('Decision')
await agent(
  deb('E', 'Giám đốc Chiến lược (CIO) — quyết định cuối', 'E_cio.md',
    `${NOTES}/A_technical.md, ${NOTES}/B_news.md, ${NOTES}/C_bull.md, ${NOTES}/D_bear.md (đọc THẲNG toàn bộ note A→D)`,
    `3 file: ${RUN_DIR}/debate/DECISION.md (đầy đủ), ${NOTES}/E_cio.md (khối tóm tắt PHIÊN 4), và ${RUN_DIR}/debate/decision.json (máy đọc, đúng schema trong template — parse được, KHÔNG comment)`,
    'Phân xử cân bằng bò/gấu; ưu tiên BẢO TOÀN VỐN; bò≈gấu → mặc định THEO DÕI. Mỗi mã ứng viên phải có 1 pick trong decision.json (kể cả TRÁNH). tp_vnd/sl_vnd lấy từ signals_latest.csv.\n'),
  { label: 'E:cio', phase: 'Decision', agentType: 'general-purpose', effort: 'high' },
)

// ---------- Phase 5: compile whiteboard + render single daily digest ----------
phase('Digest')
const digest = await agent(
  `Gộp tranh luận, sinh BẢN TIN và LƯU kết quả theo ngày bằng Bash:
1. cd ${AN} && python debate/compile.py "${RUN_DIR}"   (gộp notes A→E vào WHITEBOARD.md).
2. cd ${AN} && python daily_digest.py "${RUN_DIR}"      (đọc decision.json + signals -> ghi DAILY_DIGEST.md).
3. cd ${AN} && python archive_daily.py "${RUN_DIR}"     (copy TOÀN BỘ run vào analysis/daily/<ngày>/ + cập nhật LATEST_DIGEST.md).
4. Đọc và trả về TOÀN BỘ nội dung ${RUN_DIR}/DAILY_DIGEST.md (đúng nguyên văn markdown).
Nếu decision.json thiếu/không parse được, vẫn chạy daily_digest (nó tự fallback) và ghi chú rõ.`,
  { label: 'compile+digest+archive', phase: 'Digest', effort: 'low' },
)

return { run_dir: RUN_DIR, as_of: run.as_of, digest_path: `${RUN_DIR}/DAILY_DIGEST.md`, digest }
