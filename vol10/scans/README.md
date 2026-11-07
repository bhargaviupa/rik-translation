# Vol 10 scans

Upload a better scan here as `10 Rigveda Samhitha Volume 10 N.pdf` (N = 1, 2, … in page order, 100–180 pages each is fine). While this folder has no numbered PDF, the tools use the old `vol10/scans/Rig_Vol10.pdf` in the repo root (728 pp, 300 ppi 1-bit). After uploading: re-check the page offset (`tools/numsheets.py`) and set OFFSET in `tools/cfg.py`; check for duplicated or missing pages (e.g. compare the header number at the start and end of each part).

**Scans removed (Nov 7 2026, on the user's confirmation):** the PDF scan files of this volume were `git rm`-ed. Git history keeps them: `git checkout 08c041f -- "vol10/scans/<file>.pdf"` restores one.
