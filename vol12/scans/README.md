# Vol 12 scans

Upload scan parts here in page order as `12 Rigveda Samhitha Volume 12 N.pdf` (N = 1, 2, …; Git LFS if large). Use the best (high-resolution, ~600 dpi) scan; while this folder has no numbered PDF the tools fall back to the old `vol12/scans/Rig_Vol12.pdf` (repo root; 743 pp, 300 ppi 1-bit, low quality), which must not be used without the user's recorded approval (`vol12_state.md`). After uploading: re-check the page offset (`tools/numsheets.py`), set OFFSET in `tools/cfg.py`, check duplicated/missing pages (header number at the start and end of each part).

**Scan removed from the working tree on Nov 8 2026 (user decision: repo size).** It is still in git history; restore with `git checkout 1c14e9c -- vol12/scans/<file>.pdf`. Do not commit scans again; keep them outside the repo.
