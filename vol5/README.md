# Volume 5

Vol 5 = Maṇḍala 1, Sūktas 47–61, the Fourth Adhyāya of the First Aṣṭaka (printed pp. 1–529 = PDF 17–545; printed page = PDF − 16),
plus the Kannada Pariśiṣṭa on the deities and persons of the Ṛgveda (printed pp. 531–708 = PDF 547–724). Translation complete; file closed until the combined back-fill pass.

| Path | What it is |
|---|---|
| `vol5_state.md` | Where the back-fill pass stands (not started). Read first. |
| `vol5_runbook.md` | How each batch of the pass is to be done (to be written when the pass is agreed; model: `vol2/vol2_runbook.md`). |
| `vol5_pass_log.md` | One log entry per finished batch. |
| `scans/` | Scan parts for Vol 5, named like Vols 1–3: `05 Rigveda Samhitha Volume 05 1.pdf`, `… 2.pdf`, … (one file per part, in page order). Git LFS. |
| `review/` | Per batch: `review_PDFA-B.html/.json`, `edits_PDFA-B.txt`, `notes_PDFA-B.txt`. |
| `tools/` | Pass tools and `cfg.py` (paths); copy from `vol2/tools/` and adapt when the pass starts. |

Not yet moved here (they stay at the repository root until the Vol 5 back-fill pass is agreed):
`Rig_Vol5.pdf` (the original scan) and `Rigveda_Samhita_Vol5_English_Translation.md/.docx`.
Shared publishing pipeline for Vol 5 stays in `publish/` (`python3 publish/build_vol45.py 5 full`, cleaner `publish/vol45_clean.py`).
