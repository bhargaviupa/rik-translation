# Volume 6

Vol 6 = Maṇḍala 1, Sūktas 62–80, the Fifth Adhyāya of the First Aṣṭaka (638 PDF pages in the old scan `Rig_Vol6.pdf`; printed page = PDF − 18, to be re-checked against the better scan). Translation complete (printed pp. 1–620); file closed until the combined back-fill pass. Sūktas 65–70 are *dvaipada*.

| Path | What it is |
|---|---|
| `vol6_state.md` | Where the pass stands (not started). Read first. |
| `vol6_runbook.md` | How each batch is done (to be written when the pass is agreed; model: `vol5/vol5_runbook.md`). |
| `vol6_pass_log.md` | One log entry per finished batch. |
| `scans/` | The better scan, in parts (`06 rigveda samhita volume 6 N.pdf`). |
| `parts/` | One state file per worker. |
| `review/` | Per batch: review HTML/JSON, `edits_*.txt`, notes. |
| `tools/` | `cfg.py` (paths, page map), `view.py`, `apply.py`, `qctx.py`, `pass_log.py`, copied from `vol5/tools/` and renamed; add review/verify builders from `vol5/tools/` when needed. |

Still at the repository root: `Rig_Vol6.pdf` (old scan), `Rigveda_Samhita_Vol6_English_Translation.md/.docx/.pdf`.
Print build: `python3 publish/build_vol45.py 6 full` (cleaner `publish/vol67_clean.py`).
