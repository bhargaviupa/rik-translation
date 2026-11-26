# Prompt: make a complete Kannada Text file for every volume

(For a new session on the repository `bhargaviupa/rik-translation`. Read `CLAUDE.md`, `docs/HANDBOOK.md` §4–§5, §7, §15 and `docs/LESSONS.md` first. Written Nov 26 2026.)

## Goal
The user wants, for **every volume 1–30**, a file `volN/Rigveda_Samhita_VolN_Kannada_Text.md`: the Kannada text of the printed pages, made **by script** from the user's machine-read text, with `<!-- printed N -->` page markers, in the format of the existing files of Vols 24 and 29 (look at `vol29/Rigveda_Samhita_Vol29_Kannada_Text.md`: header, `---`, `<!-- printed N -->` + `*[running head]*`, section labels `*ಸಂಹಿತಾಪಾಠಃ*` …). No translation. **Never touch an English file.** Never change a letter or a digit of the supplied text (the only allowed change is the reference-name list `rv/references.tsv` through `tools/rv/refs_apply.py`).

## State on Nov 26 2026 (check it again before you start)
- Have a Kannada Text file already (complete, made during translation): 11, 12, 14–21, 23, 24, 27, 29, 30. Older scan-based files, lower quality, not to be overwritten: 1, 2, 5, 6.
- **No Kannada Text file, source in the repository:**
  - Vol 3: `vol3/html/rig_3_1.md`, `rig_3_2.md`; Vol 4: `vol4/html/rig_4_1.md`, `rig_4_2.md`. Both have an old scan-based English translation: do not use `batch.py new` on them (it would create an empty English file next to the real one).
  - Vols 25 and 26: `vol25/html/rig_25.md`, `rig_25.filled.md`; `vol26/html/rig_26.md`, `rig_26_part2.md`, `rig_26_part2.filled.md`, `rig_26.machine_read.md`. These were read from scans with `?` marks and then filled by number and word passes (`vol25/review`, `vol26/review`). **Ask the user which file is the base before building** (the `.filled` version is probably the one).
  - Vol 22: `vol22/html/rig_22_merged.md`, with many missing pages (`vol22/MISSING_PAGES.md`): build what exists, mark each gap in the file and in a list, do not invent pages.
- **No source in the repository (need the user's upload; ask once, list them, then carry on with the rest):** Vols 7, 8, 9, 10 (scan-based English only), Vol 13 (`vol13/html/` has only a README; the Kannada file is empty because the volume waits for its re-translation), Vol 28 (no folder at all; probably the earlier part of Maṇḍala 10).

## Steps
1. Write ONE shared tool, `tools/rv/kn_full.py VOL [--source FILE…] [--out FILE]` (not per-volume scripts; CLAUDE.md rule 7). It reuses `tools/rv/html_pages.py` (page splitting, `---` = end of printed page, chunk k from `<!-- page 1 -->` on = printed page k; see `tools/rv/check_page_markers.py` and `docs/LESSONS.md` "page markers") and `tools/rv/html_to_kn.py` (`kn_pages`: cleaning, labels, structure repairs). Output as Vol 29's Kannada file, with the Kannada Sūkta/Ṛk headings made as `tools/rv/kn_headings.py` does only if an English file with the same structure exists (otherwise leave them out; say so).
2. Page markers must be complete: run `python3 tools/rv/check_page_markers.py N` logic on the output (every chunk has a marker, none repeated, none out of order) and repair by logged edits only.
3. Run it for Vols 3 and 4 first; look at 20 pages of each against the source text (count of lines, letters, digits equal; the tool must refuse if a digit or Kannada letter differs from the source apart from the documented cleaning).
4. Then 25 and 26 (after the user names the base file) and 22 (partial, gaps listed in `volN/review/kn_gaps.md`).
5. Log every run in `volN/review/repair_log.md` (what was made, from which file, counts); add a line to `PUBLICATION_TODO.md` (ticked with the date, "Last updated"), a lesson to `docs/LESSONS.md`, and update `volN/STATUS.md` ("Kannada Text file made from …").
6. Branch `claude/…` of the session; commit and push often; never force-push; no pull request and no merge into `main` unless the user says so.

## Report to the user
A table: volume | source used | pages made | gaps | checks done (what was verified and how). Say which volumes still wait for an upload, with the exact file names the pipeline expects (`volN/html/rig_N_1.md`, `rig_N_2.md`, … merged by `tools/rv/merge_md.py`).
