# Volume 1 — everything needed to finalise it

| Path | What it is |
|---|---|
| `vol1_state.md` | Where Vol 1 stands: done / to do / open readings / to be reviewed. Read first. |
| `vol1_handoff.md` | Handoff of the numeral + [?] pass (rules, method, tools); written at PDF 600. |
| `vol1_runbook.md` | How the finishing pass is done (Vol 2 method, up to PDF 743): steps, rules, digit key. |
| `vol1_review_prompt.md` | The earlier session prompt for the user-review numeral pass (was `docs/NUMERAL_REVIEW_PROMPT_VOL1.md`). |
| `vol1_pass_log.md` / `vol1_qmarks_log.md` | Logs of the numeral pass and of the word-[?] pass. |
| `Rigveda_Samhita_Vol1_English_Translation.md` (+ `.docx`) | The translation (main file). |
| `Rigveda_Samhita_Vol1_Gaps_English_Translation.md` | The portions translated late (pp. 95–167, 191–205, 261–283, 288–295). |
| `kannada/` | `Rigveda_Samhita_Vol1_Kannada_Text.md` (Kannada transcription, pilot) and its review list. |
| `scans/` | `01 Rigveda Samhitha Volume 1 1.pdf` … `10.pdf` = the better scan in ten parts (global PDF 1–945; part 4 is named `4,pdf.pdf`); `Rig_Vol1(1).pdf`, `Rig_Vol1(2).pdf` = the original scans. Git LFS. |
| `review/` | Per batch: `review_PDFA-B.html/.json` (numeral crops) and `edits_PDFA-B.txt` (the user's readings). |
| `tools/` | The pass tools plus the Vol 2 reading tools (`cfg.py` = paths; run from this folder). |

Kept in the shared publishing pipeline, pointing here: `publish/vol1_clean.py` (reads the two translation files in
`vol1/`), `publish/build_vol1.py`, `publish/style_vol1.css`, `publish/assets/cover_vol1.jpg`, outputs
`publish/work/vol1_clean.md`, `publish/work/vol1_audit.md`, `publish/out/vol1_full.pdf`/`.html`; the all-volume worklist
`publish/review/All_volumes_review_worklist.xlsx`.
