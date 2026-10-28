# Volume 4 — numeral + [?] + accent pass (structure set up Oct 28, 2026)

Vol 4 = Maṇḍala 1, Sūktas 33–46, Third Adhyāya of the First Aṣṭaka (printed pp. 1–608). Translation complete; this folder holds the
numeral/[?]/accent pass, laid out like `vol2/` and `vol3/`. **The pass has not started.** Branch `claude/numerals-vol4`
(merge into `main` only when the user says; no PRs).

| Path | What it is |
|---|---|
| `vol4_state.md` | Where the pass stands. Read first. |
| `vol4_runbook.md` | How each 100-PDF-page batch is done (adapted from `vol3/vol3_runbook.md`). |
| `vol4_pass_log.md` | One log entry per finished batch. |
| `review/` | Per batch: `review_PDFA-B.html/.json`, `edits_PDFA-B.txt`, `notes_PDFA-B.txt`. Empty so far. |
| `scans/` | Empty. Vol 4 has only the single scan `../Rig_Vol4.pdf` (622 PDF pp., printed = PDF − 14). A better scan can be added here later. |
| `tools/` | Pass tools copied from `vol3/tools/` and pointed at Vol 4 (`cfg.py` = paths, `pages.py` = page map; run from this folder). |

**Files that stay at the repository root** (the build pipeline reads them there; not moved): `Rigveda_Samhita_Vol4_English_Translation.md`
(+ `.docx`; the file the pass edits), `Rig_Vol4.pdf` (scan), `publish/build_vol45.py`, `publish/vol45_clean.py`, `publish/assets/cover_vol4.jpg`,
`publish/out/vol4_full.pdf`.
