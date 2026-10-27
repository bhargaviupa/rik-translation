# Vol 1 — state

Status of the files (as of Oct 27, 2026; folder set up from the existing files, content not changed).

## Done
- Translation complete: `Rigveda_Samhita_Vol1_English_Translation.md` (main) and
  `Rigveda_Samhita_Vol1_Gaps_English_Translation.md` (the portions translated late, printed pp. 95–167, 191–205,
  261–283, 288–295). File closed for general editing (CLAUDE.md); the numeral + [?] pass was authorised separately.
- Numeral + [?] pass on the better scan: logged for **PDF 1–743** (last log entry Oct 26, 16:00, PDF 701–743;
  `vol1_pass_log.md`; word-[?] pass log `vol1_qmarks_log.md`). Review pages and the user's edits per batch in `review/`.
- Print build exists: `publish/out/vol1_full.pdf` (from `publish/work/vol1_clean.md`).

## To do / not covered
- PDF 744–945 (the scan has 945 pages): not in the pass log. The main file ends with the colophon and a sample of the
  Alphabetical Index of mantras (the index is characterized, not transcribed) — confirm whether anything after PDF 743
  needs the pass.
- Rebuild the print PDF after the pass (`python3 publish/build_vol1.py full`) and regenerate the worklist
  (`python3 publish/review_all.py`) — not yet logged as done after the pass.
- Kannada text (`kannada/Rigveda_Samhita_Vol1_Kannada_Text.md`, pilot) and its review list: per CLAUDE.md, the
  combined back-fill pass (English [?] + Kannada file) for Vols 1–10 needs the user's agreement.

## Open readings
- `[?]` count now: main file 105, Gaps file 14, Kannada text 193 (raw counts; include header-note conventions).
- Listed as genuine in the last handoff (written at PDF 600; not re-checked since): Gaps pp. 127, 132, 139 (table rows
  6–7 vs printed 664), 273; main p. 556 first word of the TA 2-16 quote. Later batches: see the pass-log entries.

## To be reviewed by the user
- The pass log entries list each judgement call per batch; `vol1_handoff.md` keeps the session's rules and method.
