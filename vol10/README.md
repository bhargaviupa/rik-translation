# Volume 10

Vol 10 = **Maṇḍala 1, Sūktas 122–136, First Adhyāya of the Second Aṣṭaka** (printed pp. 2–707; printed = PDF − 21, to be re-checked). **Already fully translated** (`Rigveda_Samhita_Vol10_English_Translation.md`, repo root, ~2,870 `[?]`); the numeral/`[?]` pass, the docx/PDF check and the Kannada text file are not done. Scan: the old `vol10/scans/Rig_Vol10.pdf` (repo root, 728 pp, 300 ppi 1-bit, Git LFS) unless a better scan is uploaded to `scans/`.

| Path | What it is |
|---|---|
| `vol10_state.md` | Where the work stands. Read first. |
| `vol10_runbook.md` | Method: Phase 1 (numerals from the user's xls files, no images), explicit stop, Phase 2 (reading the scan). Sonnet only. |
| `numerals/` | The user's xls/xlsx numeral files. |
| `START_PROMPT.md` | Prompt to start a new session on Vol 10. |
| `scans/` | Better scan parts, if uploaded (`10 Rigveda Samhitha Volume 10 N.pdf`); see its README. |
| `parts/` | One state file per worker/session. |
| `review/` | Doubts JSON/pages, edit logs, page map. |
| `tools/` | `page.py` (read a page as strips), `view.py`, `numsheets.py` (header strips for the offset), `apply.py` (unique-match edits), `append_en.py`, `doubt.py`, `cfg.py`. Copied from the Vol 13/14 tools and adapted; test before relying on them. |
