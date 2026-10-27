# Volume 2 — everything needed to finalise it

Vol 2 = Maṇḍala 1, Sūktas 3–19, First Adhyāya of the First Aṣṭaka (printed pp. 1–808).
Current work: the numeral + [?] + accent pass (Oct 2026), branch `claude/numerals-vol2`.

| Path | What it is |
|---|---|
| `vol2_state.md` | **Where the pass stands**: done / to do / open readings / to be reviewed. Read first. |
| `vol2_runbook.md` | How each 100-PDF-page batch is done (steps, rules, digit key). |
| `vol2_pass_log.md` | One log entry per finished batch. |
| `Rigveda_Samhita_Vol2_English_Translation.md` | The translation (the file being corrected). `.docx` = last DOCX build. |
| `scans/` | `02 Rigveda Samhitha Volume 02  1.pdf` … `5.pdf` = the better scan in five parts (global PDF 1–822); `Rig_Vol2.pdf` = the original scan. Git LFS. |
| `review/` | Per batch: `review_PDFA-B.html/.json` (numeral crops), `edits_PDFA-B.txt` (every numeral as read), `notes_PDFA-B.txt` (what changed). |
| `tools/` | The pass tools (`cfg.py` = paths; run from this folder). |

Kept in the shared publishing pipeline (used by all volumes), pointing here:
`publish/vol2_clean.py` (reads `vol2/Rigveda_Samhita_Vol2_English_Translation.md`), `publish/build_vol2.py`,
`publish/assets/cover_vol2.jpg`, outputs `publish/work/vol2_clean.md` and `publish/out/vol2_full.pdf`;
the all-volume reviewer worklist `publish/review/All_volumes_review_worklist.xlsx` (`publish/review_all.py`).
