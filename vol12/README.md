# Volume 12

Vol 12 = **Maṇḍala 1, Third Adhyāya of the Second Aṣṭaka** (Vol 11 precedes it, Vol 13 starts at Sūkta 166); the exact Sūkta range, printed-page count and offset come from the title page and contents of the scan (`vol12_state.md`). **First translation** of this volume (not a correction pass). English-only file, lean method of Vols 13/14 (a Kannada text file only if the user asks).

| Path | What it is |
|---|---|
| `vol12_state.md` | Facts, open decisions, status. Read first. |
| `vol12_runbook.md` | Method: Sonnet translators on 3-page batches, numerals from the user's files, turn economy. |
| `START_PROMPT.md`, `CONTINUE_PROMPT.md` | Prompts for a new dispatcher session. |
| `numerals/` | The user's xls/xlsx numeral files (correct Kannada numerals). |
| `scans/` | Scan parts (`12 Rigveda Samhitha Volume 12 N.pdf`); see its README. The only scan in the repo today is the old `vol12/scans/Rig_Vol12.pdf` (root; 743 pp, 300 ppi 1-bit, low quality). |
| `parts/` | `session_state.md` (position) and `batch_costs.md`. |
| `review/` | Doubts JSON/pages, page map. |
| `tools/` | `page.py` (read a page as strips), `view.py`, `numsheets.py`, `apply.py`, `append_en.py`, `doubt.py`, `cfg.py` (copied from the Vol 10/14 tools; test before relying on them). |

Output (repo root): `Rigveda_Samhita_Vol12_English_Translation.md`.
