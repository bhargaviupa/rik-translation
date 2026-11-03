# Repo cleanup report (inventory only — nothing deleted)

Branch `claude/cleanup` from `origin/main`, Nov 3 2026. Sizes in MB (1 MB = 10^6 bytes).

## (a) Size
- Working tree without `.git`: **2.8 GB** (checkout of main); `.git`: **2.6 GB** (pack 2.59 GiB, 6,931 objects, no loose objects, no garbage).
- Tracked bytes by folder: vol1 381 · vol14 354 · vol2 307 · root 305 · vol5 277 · vol13 260 · vol3 254 · vol10 241 · vol4 220 · vol6 202 · publish 97 · docs 2.
- **Scan PDFs under `vol*/scans/` ≈ 2.1 GB** (vol1 371, vol14 354, vol2 297, vol5 267, vol3 242, vol10 239, vol4 220, vol13 219, vol6 197). Scans are ordinary git files, not LFS (except root `Rig_Vol9.pdf`, `Rig_Vol11.pdf`: 133-byte LFS pointers).
- **Deleting files will not shrink `.git`** (history keeps every blob); it shrinks only the checkout/clone-of-HEAD size.

## (b) 60 biggest tracked files
Every one is a scan PDF (class: SCAN). Top of the list; the full 60 are all `vol*/scans/*.pdf` or root `Rig_Vol*.pdf` between 30 and 78 MB:
| MB | path | class |
|---|---|---|
| 78.1 | vol2/scans/02 Rigveda Samhitha Volume 02 5.pdf | scan-part |
| 58.4 | vol13/scans/13 Rigveda Samhitha Volume 13 6.pdf | scan-part |
| 56.0 | vol2/scans/02 Rigveda Samhitha Volume 02  1.pdf | scan-part |
| 55.5 | vol2/scans/02 Rigveda Samhitha Volume 02 3.pdf | scan-part |
| 53.9 | vol2/scans/02 Rigveda Samhitha Volume 02 2.pdf | scan-part |
| 53.9 | vol2/scans/02 Rigveda Samhitha Volume 02 4.pdf | scan-part |
| 53.5 | vol5/scans/05 rigveda samhita volume 5 7.pdf | scan-part |
| 42.2 | vol10/scans/10 Rigveda Samhitha Volume 10 7.pdf | scan-part |
| 41.9 | vol6/scans/06 Rigveda Samhitha Volume 6 6.pdf | scan-part |
| 39.8 | vol14/scans/14 Rigveda Samhitha Volume 14 1.pdf | scan-part |
| 38.6 | vol5/scans/05 rigveda samhita volume 5 6.pdf | scan-part |
| 38.0 | vol1/scans/01 Rigveda Samhitha Volume 1 1.pdf | scan-part |
| 37.2 | vol14/scans/14 Rigveda Samhitha Volume 14 6.pdf | scan-part |
| 36.9 | vol14/scans/14 Rigveda Samhitha Volume 14 7.pdf | scan-part |
| 36.7 | vol1/scans/01 Rigveda Samhitha Volume 1 5.pdf | scan-part |
| 36.7 | vol14/scans/14 Rigveda Samhitha Volume 14 4.pdf | scan-part |
| 36.5 | vol14/scans/14 Rigveda Samhitha Volume 14 3.pdf | scan-part |
| 36.5 | vol1/scans/01 Rigveda Samhitha Volume 1 6.pdf | scan-part |
| 36.4 | vol1/scans/01 Rigveda Samhitha Volume 1 7.pdf | scan-part |
| 36.4 | vol5/scans/05 rigveda samhita volume 5 2.pdf | scan-part |
| 36.1 | vol14/scans/14 Rigveda Samhitha Volume 14 8.pdf | scan-part |
| 36.0 | vol5/scans/05 rigveda samhita volume 5 1.pdf | scan-part |
| 35.5 | vol3/scans/03 Rigveda Samhitha Volume 03 2.pdf | scan-part |
| 35.1 | vol3/scans/03 Rigveda Samhitha Volume 03 1.pdf | scan-part |
| 34.9 | vol5/scans/05 rigveda samhita volume 5 3.pdf | scan-part |
| 34.8 | vol1/scans/01 Rigveda Samhitha Volume 1 3.pdf | scan-part |
| 34.8 | vol1/scans/01 Rigveda Samhitha Volume 1 4,pdf.pdf | scan-part |
| 34.7 | vol3/scans/03 Rigveda Samhitha Volume 03 3.pdf | scan-part |
| 34.7 | vol1/scans/01 Rigveda Samhitha Volume 1 2.pdf | scan-part |
| 34.5 | vol5/scans/05 rigveda samhita volume 5 4.pdf | scan-part |
| 34.2 | vol14/scans/14 Rigveda Samhitha Volume 14 2.pdf | scan-part |
| 34.0 | Rig_Vol5.pdf | scan-orig(root) |
| 33.7 | vol14/scans/14 Rigveda Samhitha Volume 14 5.pdf | scan-part |
| 33.5 | vol4/scans/04 RigvedaSamhithaVolume04 1.pdf | scan-part |
| 33.5 | vol5/scans/05 rigveda samhita volume 5 5.pdf | scan-part |
| 33.2 | vol10/scans/10 Rigveda Samhitha Volume 10 6.pdf | scan-part |
| 33.1 | vol10/scans/10 Rigveda Samhitha Volume 10 1.pdf | scan-part |
| 33.0 | vol10/scans/10 Rigveda Samhitha Volume 10 5.pdf | scan-part |
| 32.9 | vol10/scans/10 Rigveda Samhitha Volume 10 3.pdf | scan-part |
| 32.9 | vol4/scans/04 RigvedaSamhithaVolume04 2.pdf | scan-part |
| 32.8 | vol10/scans/10 Rigveda Samhitha Volume 10 4.pdf | scan-part |
| 32.7 | vol13/scans/13 Rigveda Samhitha Volume 13 4.pdf | scan-part |
| 32.6 | vol4/scans/04 RigvedaSamhithaVolume04 7.pdf | scan-part |
| 32.5 | vol1/scans/01 Rigveda Samhitha Volume 1 8.pdf | scan-part |
| 32.3 | vol10/scans/10 Rigveda Samhitha Volume 10 2.pdf | scan-part |
| 32.1 | vol13/scans/13 Rigveda Samhitha Volume 13 5.pdf | scan-part |
| 32.0 | vol6/scans/06 Rigveda Samhitha Volume 6 4.pdf | scan-part |
| 32.0 | vol13/scans/13 Rigveda Samhitha Volume 13 1.pdf | scan-part |
| 31.9 | vol13/scans/13 Rigveda Samhitha Volume 13 2.pdf | scan-part |
| 31.9 | vol3/scans/03 Rigveda Samhitha Volume 03 5.pdf | scan-part |
| 31.9 | vol13/scans/13 Rigveda Samhitha Volume 13 3.pdf | scan-part |
| 31.6 | vol6/scans/06 Rigveda Samhitha Volume 6 1.pdf | scan-part |
| 31.2 | vol6/scans/06 Rigveda Samhitha Volume 6 2.pdf | scan-part |
| 30.8 | vol3/scans/03 Rigveda Samhitha Volume 03 4.pdf | scan-part |
| 30.7 | vol4/scans/04 RigvedaSamhithaVolume04 4.pdf | scan-part |
| 30.6 | vol4/scans/04 RigvedaSamhithaVolume04 3.pdf | scan-part |
| 30.5 | vol6/scans/06 Rigveda Samhitha Volume 6 3.pdf | scan-part |
| 30.0 | vol4/scans/04 RigvedaSamhithaVolume04 5.pdf | scan-part |
| 30.0 | vol6/scans/06 Rigveda Samhitha Volume 6 5.pdf | scan-part |
| 29.9 | vol4/scans/04 RigvedaSamhithaVolume04 6.pdf | scan-part |

Other large non-scan tracked files: root volume PDFs `Rigveda_Samhita_Vol{6,7,8,9,10,11}_English_Translation.pdf` (61 MB total) and `…Vol11_Kannada_Text.pdf` (12.8 MB) = DELIVERABLE (built from the .md); `publish/out/*` 67.7 MB = BUILD OUTPUT; `vol13/review/html/Vol13_doubts_*.html` ≈ 45 MB = REVIEW (protected); `publish/work/*_clean.md` 12.2 MB = BUILD INTERMEDIATE; `publish/assets/*.jpg` 14.6 MB = ASSET.

## (c) 40 biggest blobs in history
All 40 are the same scan PDFs as in (b) (identical hashes), each present in all 11 remote branches (they reference the same blob). History-only big blobs (not in main's HEAD), i.e. what history carries beyond today's tree:
| MB | path (blob in old commits) | note |
|---|---|---|
| 32 | vol13/scans/13 Rigveda Samhitha Volume 13 … (the removed duplicate `4a`) | removed Nov 3 |
| 12 | vol2/Rigveda_Samhita_Vol2_English_Translation.pdf | older PDF build |
| 9 | vol3/Rigveda_Samhita_Vol3_English_Translation.pdf | older build |
| 8 | Rigveda_Samhita_Vol6_English_Translation.pdf | older build |
| 6 each | older builds of Vol 1/4/5/13 PDFs and `publish/out/vol1–5_full.pdf` | older builds |
Only a history rewrite would reclaim these (not proposed).

## (d) Remote branches (origin; "active" = pushed < 24 h)
| branch | last push | ahead of main | behind | status |
|---|---|---|---|---|
| main | 0.2 h | – | – | – |
| claude/vol14-pilot | 0 h | 14 | 2 | **ACTIVE** (another session) |
| claude/pass2-vol10 | 12.7 h | 1 | 15 | ACTIVE (<24 h), unmerged |
| claude/publish-vol13 | 12.6 h | 0 | 13 | merged → deletable |
| claude/v13-zoomfix-a | 19.0 h | 1 | 258 | ACTIVE (<24 h), unmerged |
| claude/vol12 | 19.2 h | 0 | 142 | merged → deletable (but Vol 12 branch is recent; your call) |
| claude/vol14-fix | 72 h | 0 | 410 | merged → deletable |
| claude/v13-user-readings | 73 h | 0 | 412 | merged → deletable |
| claude/rebuild-vols-1-6-13 | 85 h | 7 | 413 | STALE but **unmerged** (user deferred the rebuild) → ASK |
| claude/vol14 | 85 h | 0 | 752 | merged → deletable |
| claude/vol13 | 85 h | 0 | 504 | merged → deletable |

**WARNING:** `git ls-remote origin 'refs/heads/archive*'` returns **nothing** — `archive/old-history` is NOT on the remote right now (the coordination notes say it was once deleted by mistake and restored from a local ref). I have not touched it; please check it in the GitHub UI and re-push it from a local clone if it is missing.

## (e) Duplicate files (same hash, different paths)
No duplicate scans or PDFs. Duplicates are only small tool scripts copied between volume folders (`vol1–4/tools/*.py`, `vol10/12/13/tools/numsheets.py`, `vol5/6 make_artifact_*.py`) and empty `.gitkeep`/identical state stubs — a few KB; not worth touching.

## (f) Generated outputs rebuilt from sources
| item | MB | rebuilt by |
|---|---|---|
| publish/out/vol1_full.html, vol2_full.html, vol4_full.html | 2.7+3.6+2.5 = 8.8 | publish/build_vol1.py, build_vol2.py, build_vol45.py |
| publish/out/vol1–13_full.pdf (13 files) | 58.9 | same build scripts (print PDFs; some are deliverables) |
| publish/work/vol1,2,4,5_clean.md | 2.4+3.1+2.1+2.2 = 9.8 | publish/vol1_clean.py, vol2_clean.py, vol45_clean.py |
| publish/work/vol11_clean.md | 2.3 | no obvious cleaner script (vol67_clean?) — unclear |
| publish/work/vol*_audit.md | ~0 | keep |
| publish/review/All_volumes_review_worklist.xlsx | 2.3 | publish/review_all.py |
| root `Rigveda_Samhita_VolN_English_Translation.docx/.pdf`, Kannada docx/pdf | ≈ 87 | pandoc + docx_csfont + soffice (see CLAUDE.md); a rebuild pass is pending |

## (g) Checkout leftovers
`git status --ignored`: clean — no untracked or ignored files (only `__pycache__/` is ignored and none exist).

---
# Classification

## REMOVE-SAFE (proposed; needs your "yes")
| path | MB | why |
|---|---|---|
| `vol14/scans/Rig_Vol14(1).pdf`, `Rig_Vol14(2).pdf` | 33.8 | old low-res scan; `vol14/README.md`: "old scan: ignore"; all work uses the 9 new parts; listed as a candidate in the coordination notes |
| `publish/out/vol1_full.html`, `vol2_full.html`, `vol4_full.html` | 8.8 | regenerated by `publish/build_vol1.py`/`build_vol2.py`/`build_vol45.py` |
| `publish/work/vol1_clean.md`, `vol2_clean.md`, `vol4_clean.md`, `vol5_clean.md` | 9.8 | regenerated by `publish/vol1_clean.py`/`vol2_clean.py`/`vol45_clean.py` from the translation .md |
| **Total** | **≈ 52.4** | |

## REMOVE-LATER (needed until the named pass finishes)
| path | MB | until |
|---|---|---|
| `Rig_Vol10.pdf` (root) | 25.2 | Vol 10 numeral/zoom pass on the better scan (`claude/pass2-vol10` active) |
| `Rig_Vol13.pdf` (root) | 23.6 | Vol 13 zoom-fix parts 1–4 finished |
| `vol13/scans/*` (6 parts) | 219 | same (never remove while pass runs) |
| `vol14/scans/*` (9 parts) | 292 | Vol 14 translation finished |
| `vol10/scans/*` (7 parts) | 239 | Vol 10 pass finished |
| `vol1/scans/Rig_Vol1(1).pdf`, `(2).pdf` | 39.0 | Vol 1 numeral pass on the better scan (logged only to PDF 743 of 945) done |
| `vol5/scans/*`, `vol6/scans/*` | 267 / 197 | recorded user readings applied (Vol 5 pp. 578–625; Vol 6 p. 618 + 183 numeral rows) and back-fill pass |

## ASK (not sure)
| path | MB | question |
|---|---|---|
| `Rig_Vol4.pdf`, `Rig_Vol5.pdf`, `Rig_Vol6.pdf` (root, old scans) | 24.2 / 34.0 / 21.5 | better scans exist and passes were merged, but Vol 4's headings still cite old-scan PDF numbers and Vol 5/6 have unapplied user readings. Remove? |
| `Rig_Vol7.pdf`, `Rig_Vol8.pdf`, `Rig_Vol12.pdf` (root) | 19.8 / 28.1 / 25.9 | only scan of those volumes → KEEP unless you have better ones |
| `vol3/scans/Rig_Vol3.pdf` | 22.8 | KEEP: printed pp. 487 and 646 exist only there |
| `vol1…vol6/scans/` better-scan parts of Vols 1–4 | 371 / 297 / 242 / 220 | Vols 1–4 passes are "agreed passes" not finished (Vol 3 conflict check open; back-fill planned). Keep until you say |
| `publish/out/vol*_full.pdf` | 58.9 | designed print PDFs = deliverables; rebuild pending. Remove (rebuildable) or keep? |
| root `Rigveda_Samhita_Vol{6–11}_English_Translation.pdf`, Kannada PDF | 73.6 | rebuildable from .md, but they are your deliverables |
| `publish/work/vol11_clean.md` | 2.3 | no clear generating script |
| `publish/review/All_volumes_review_worklist.xlsx` | 2.3 | regenerable via `publish/review_all.py`; wanted? |
| `publish/assets/cover_vol5_alt.jpg` | 3.8 | unused alternate cover? |
| `vol13/review/html/Vol13_doubts_*.html` | 45 | protected path (review) — left alone; could be regenerated if the generator exists |

---
# Checkpoint — what I need from you
1. Approve the **REMOVE-SAFE list (≈ 52.4 MB)**? (yes / edit list)
2. Branches you could delete in the GitHub UI: merged — `claude/publish-vol13`, `claude/vol12`, `claude/vol14-fix`, `claude/v13-user-readings`, `claude/vol14`, `claude/vol13`. Unmerged and stale: `claude/rebuild-vols-1-6-13` (ASK). Leave `claude/vol14-pilot`, `claude/pass2-vol10`, `claude/v13-zoomfix-a` (active).
3. Check `archive/old-history`, which is missing on the remote.
4. Decide any ASK items you want removed.
