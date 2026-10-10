# Vol 8 numeral second pass — method, status, how to continue

**Status (Oct 2026).** Done: Pīṭhike pp. ii–ix; Sūkta 95 (printed pp. 1–61) and Sūkta 96–97 (pp. 62–133) of the Seventh Adhyāya. **Not done:** Sūktas 98–112 (printed pp. 134–832) — their numerals still carry the old `[?]` flags and some wrong numbers. The reader decided not to redo them now: this note is where the fix is recorded. Nothing else in Vols 1–7 was touched.

## Source for the pass
Alternate clean scan of the same edition: branch `alt-scan-vol8` (Git LFS), `Rig_Vol8_alt.pdf`, 853 pp., 600 ppi. Pīṭhike pp. i–ix = same PDF numbers as our scan (6–14). Main text: **alt PDF page = printed page + 21** (our scan: + 20). Check out with `git worktree add /tmp/altwt/w alt-scan-vol8` (needs `git lfs pull`).

## Digit key for this print (confirmed by the reader)
`೧` = "∩"; `೦` = "○"; **flat-footed "2"-like glyph = 7, curled "2"-like glyph = 2**; `೬` has a hook at top-left; `೮` looks like ಲ/ಅ; `೯` like ಕ; `೪` like ಳ; `೫` like ಣ; `೩` like ಇ. My recurring confusions: 3/5, 6/7, 2/9, 8/9 (e.g. the reader's corrections: Uṇ. 4-537→4-557, 2-9?2→2-252, 1-27→1-26). Always zoom each digit; context (the verse/sūtra cited) is a sanity check only — **record what is printed** and say if it differs from the standard number.

## What the print does and does not contain
- Grammar notes cite a lot of sūtra numbers, but for many sūtras the print gives **no number at all**; earlier drafts had supplied numbers from memory. Where the print gives none, remove the number.
- Running heads give Adhyāya 7 and a Varga number (Varga 1 up to p. 31, 2 on pp. 33–59, 3 on pp. 61?–93 (see the file), 4 on pp. 95–109, 5 on pp. 111–133); a sūkta/anuvāka heading block gives Maṇḍala, Anuvāka, Sūkta, Aṣṭaka, Adhyāya, Varga, Ṛk count.
- Some printed numbers differ from the usual ones (e.g. Pā. 6-1-128 for 6-1-178, 8-4-3 for 8-3-106, 6-1-183 for 6-1-193); record the print as printed.

## Procedure that worked
1. Read the page at 200 dpi in 3 strips (`pg.py`), make a montage of all numerals at 600 dpi (`mont.py`, per-process temp names so parallel runs do not clash), decode each digit.
2. Compare with the page section of the .md (`### Page N (PDF M)`); produce **patches** `{page, old, new, confidence, note}` against exact unique text; never edit the .md while reading.
3. Apply all patches with `apply_patches.py <names>` (asserts uniqueness per page section, keeps exactly one trailing progress note; a section runs to the next `### Page` heading).
4. Parallel readers worked well (about 8 pages per reader; 150k tokens each). Brief: `BRIEF.md`.
5. Keep `[?]` where the digit is ambiguous; remove it where the print is legible.

## Open readings left flagged (examples; full lists are in the patch files and the git history)
Ṛ. 1-70-2 vs 1-70-3 (*garbho yo apāṃ…*, pp. 12, 21, 25); Uṇ. 4-202 vs 4-642 (p. 22/26); Dhā. 19-63-67 (p. 22); Ni. 3-2 (p. 25); Pā. 7-1-100, 7-1-109; Bṛ. De. 3-129 (p. 5); many Uṇādi numbers (pp. 8–10, 14–15, 37, 43, 48, 52, 56, 80, 84, 106–107, 122); Bṛ. De. 3-125, 2-24/25, 3-61/65 (pp. 64, 67); Ṛ. 3-14-7 (p. 78); Ṛ. 4-8-2 (p. 87); Ṛ. 1-151-8 vs 1-151-7 (pp. 97/98); Tāṇḍya Brāhmaṇa 13-6-9 last digit (pp. 110–113).

## Rebuilds still needed after any edit
`.docx` (pandoc `-f markdown-yaml_metadata_block`), plain PDF (LibreOffice), designed print PDF (`python3 publish/build_vol45.py 8 full`), review worklist (`python3 publish/review_all.py`). Not yet rebuilt after the numeral pass.
