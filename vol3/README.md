# Volume 3 — everything needed to finalise it

Vol 3 = Maṇḍala 1, Sūktas 20–32, Second Adhyāya of the First Aṣṭaka (printed pp. 1–647).
Current work: the numeral + [?] + accent pass (set up Oct 27, 2026; starts when the Vol 2 pass is done), branch `claude/numerals-vol3`.

| Path | What it is |
|---|---|
| `vol3_state.md` | **Where the pass stands**: done / to do / open readings / to be reviewed. Read first. |
| `vol3_runbook.md` | How each 100-PDF-page batch is done (steps, rules, digit key, page map). |
| `vol3_pass_log.md` | One log entry per finished batch. |
| `Rigveda_Samhita_Vol3_English_Translation.md` | The translation (the file being corrected). `.docx` = last DOCX build. Sūkta 29 Ṛks 6–7 and Sūkta 30 are corrected in the SUPERSEDING REDO block near its end. |
| `Session_Report_Vol3_Sukta29-32.md` | The audit report on Sūktas 29–32 (why the REDO block exists). |
| `scans/` | `03 Rigveda Samhitha Volume 03 1.pdf` … `7.pdf` = the better scan in seven parts (global PDF 1–660; plain git files); `Rig_Vol3.pdf` = the original scan, needed for printed pp. 487 and 646, which the better scan lacks. |
| `review/` | Per batch: `review_PDFA-B.html/.json` (numeral crops), `edits_PDFA-B.txt` (every numeral as read), `notes_PDFA-B.txt` (what changed). |
| `tools/` | The pass tools, copied from `vol2/tools/` (`cfg.py` = paths and scan parts, `pages.py` = page map; run from this folder). |

Kept in the shared publishing pipeline (used by all volumes): `publish/build.py` (builds Vol 3: `cd publish && python3 build.py 3 full`;
reads this folder's translation), `publish/assets/cover_vol3.jpg`, output `publish/out/vol3_full.pdf`; the all-volume reviewer
worklist `publish/review/All_volumes_review_worklist.xlsx` (`publish/review_all.py`).
