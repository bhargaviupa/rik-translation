# Vol 10 scans

Upload a better scan here as `10 Rigveda Samhitha Volume 10 N.pdf` (N = 1, 2, … in page order, 100–180 pages each is fine). While this folder has no numbered PDF, the tools use the old `vol10/scans/Rig_Vol10.pdf` in the repo root (728 pp, 300 ppi 1-bit). After uploading: re-check the page offset (`tools/numsheets.py`) and set OFFSET in `tools/cfg.py`; check for duplicated or missing pages (e.g. compare the header number at the start and end of each part).

**Scans were removed from the repository on Nov 7–8 2026 and purged from all git history (user decision: repo size).** They cannot be restored from git; the originals are held by the user. To work with a scan locally, copy it into this folder: `.gitignore` keeps `vol*/scans/*` (except this README) out of commits.