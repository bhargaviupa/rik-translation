# Reading the small Kannada numerals — what we tried, what failed, what to try next

Brief for a fresh session (Opus or Fable class model, deeper research allowed). It is self-contained. Read it, then `CLAUDE.md`, then `publish/tools/numeral_pass/METHOD.md`. Do not start by reading page images at random: first build the test set in §6.

## 1. The problem

The 1949 Kannada commentary prints **reference numerals in small Kannada digits** inside parentheses, mostly in the grammar notes and the Special Topics: Pāṇini sūtras (`ಪಾ. ಸೂ. ೬-೧-೧೬೩`), Uṇādi sūtras (`ಉ. ಸೂ.`), Nirukta (`ನಿ. ೨-೯`), Ṛgveda (`ಋ. ಸಂ. ೧೦-೧೬೨-೩`), Śatapatha/Taittirīya/Bṛhaddevatā/Upaniṣad references, plus page-header numerals (Aṣṭaka, Adhyāya, Varga) and counts. Each reference is 2–4 numbers joined by hyphens, in type about 2.5 mm tall. Reading them wrongly is the main source of error that survives our passes, and a wrong digit looks as plausible as a right one.

Scale in Vol 11 (rough, by pattern count): about **1,400 numeral-position `[?]` in the English file and about 1,700 in the Kannada file**, out of 6,621 / 4,389 `[?]` in total. The better 600 dpi scan covers only PDF pages 1–140; numerals on PDF 141–714 are still unread.

## 2. Digit key for this print (confirmed by the user)

`೧` looks like "∩"; `೦` like "○"; **the flat-footed "2"-like glyph is ೭ (7); the curled "2"-like glyph is ೨ (2)**; `೬` has a hook at top-left; `೮` looks like ಲ/ಅ; `೯` like ಕ; `೪` like ಳ; `೫` like ಣ; `೩` like ಇ. Our recurring confusions: **3/5, 6/7, 2/9, 8/9**, also 1/7 when the foot is faint and 0/9 in a blurred "○". The font also draws ಮ like "ಮು" and ṅ (ಙ) like ಜ, which matters only for words.

## 3. What we tried

| # | Method | Where | Result |
|---|---|---|---|
| 1 | Read page at 120–150 dpi, write numerals in the first pass | Vols 1–10 | Fast, but many numerals wrong or flagged `[?]`. Roughly 9,000 `[?]` remain across the project. |
| 2 | **Numeral second pass** from a clean 600 ppi alternate scan: 3 strips at 200 dpi, a montage of all numerals at 600 dpi, patch files `{page, old, new, confidence, note}`, parallel readers (~8 pages each, ~150k tokens each) | Vol 8, Pīṭhike and Sūktas 95–97 only | Worked, and the user's corrections showed it still left errors: Uṇ. 4-537→4-557, 2-9?2→2-252, 1-27→1-26. Not done for Sūktas 98–112 (~280 flagged pages). Method in `publish/tools/numeral_pass/METHOD.md`. |
| 3 | Tesseract `kan+san+eng`, 300 dpi, on whole pages | Vol 8 test, 3 pages | Read the numerals **well** (10 of 12 references) but the words badly. |
| 4 | Google Docs OCR | Vols 8–9 extracts | Many word errors, wrong digits at the **ends** of Ṛg references. Dropped. |
| 5 | Tesseract `kan` via OCRmyPDF on a 600 dpi 15-page extract (Oct 2026) | Vol 12 pages 71–78 | Prose ~85–90% right; `ಪಾ. ಸೂ.` came out `ವಾ ಸೂ`; reference numerals unreliable; English paragraphs turned into digit garbage. Not usable for numerals. |
| 6 | **Better 600 dpi scan, 260 dpi strips + 520 dpi zoom tiles**, one tile per numeral, resolve `[?]` page by page | Vol 11, PDF 25–72, ~1,100 `[?]` cleared | Much better than #1. Most Pāṇini numerals became legible. Still some left `[?]` (listed in `docs/PASS_LOG.md`). Tools in `publish/tools/verify11/`. |
| 7 | Plausibility check from the cited sūtra/verse (no outside lookups, just "does this look like a real number") | all | Useful only as a sanity flag; it cannot choose between two legible-looking readings. |
| 8 | Repeating the same sūtra across pages (e.g. *citaḥ* 6-1-163 appears many times) to confirm | informal | Helped on common sūtras; not systematised. |

## 4. Failures and their causes

- **Digit confusions** listed in §2 persist even at 520 dpi when the print is faint or the glyph is clipped.
- **Wrong zoom boxes.** The viewer shows strips smaller than their pixels (e.g. 2,078 px shown as 2,000), so coordinates read off the screen must be multiplied by `orig_width / displayed_width` (about 1.04–1.09); several zooms landed on the wrong line before we found this. Always check the first tile shows the target numeral before reading it.
- **Stroke/underline ambiguity** (accent marks) overlaps numerals in the page headers; not the main issue but it hides digits.
- **Memory leaking in.** Earlier drafts supplied sūtra numbers from memory; the project rule is to record **what is printed**, even if it differs from the standard number, and to give no number where none is printed. Several reference numbers in the early volumes had to be removed for this reason.
- **Printed numbers that differ from the usual ones** (Pā. 6-1-128 for 6-1-178, 8-4-3 for 8-3-106, 6-1-183 for 6-1-193): a reader who "corrects" these destroys real information.
- **Small type.** Numerals inside grammar notes are smaller still; the project rule for Vols 11+ says "no zooming" there, so those were left `[?]`.
- **No ground truth.** Until now we had no scored test set, so every method was judged by feel.
- **Cost.** Reading and zooming costs about 10,000–15,000 tokens per page in this workflow.

## 5. Ideas to try (roughly in order of expected value)

1. **Build a scored test set first** (§6). Nothing else can be compared without it.
2. **Glyph clustering and one-time labelling.** Detect every reference group (the text between `(` and `)`, usually after a bold headword), split into digit glyphs, cluster visually (perceptual hash, or small CNN embeddings), and show the user a contact sheet of each cluster once to label the ten digits and the hyphen. The print is one typeface, so ~10 digit classes with some variants should cover everything. Then classify every numeral automatically and flag low-confidence ones for visual reading. Segmentation (touching glyphs, clipped feet) is the hard part.
3. **Numeral-only Tesseract.** Crop each parenthesised group and run Tesseract with `-l kan --psm 7` and a character whitelist of `೦೧೨೩೪೫೬೭೮೯-.()`. This is the one configuration where Tesseract did well (#3). Use as an independent second reader; disagreements go to visual reading.
4. **Multiple independent readers with voting.** Two or three model passes (different crops, scales, even different models) per numeral; accept only unanimous reads; send splits to a stronger reader. Cheap if the crops are tiny.
5. **Super-resolution / de-blur** (Lanczos ×3, unsharp mask, adaptive threshold) before viewing; test on the confusion pairs.
6. **Format validators.** Reject or flag impossible values: Pāṇini adhyāya 1–8 / pāda 1–4 / sūtra within the real count of that pāda; Uṇādi pāda 1–5; Nirukta chapter ≤ 14; Nighaṇṭu chapter 1–5; Ṛg maṇḍala 1–10 with the real sūkta and mantra counts; Aṣṭaka 1–8, Adhyāya 1–8, Varga within the adhyāya. These are only "does this exist" checks; they cannot supply a number.
7. **Candidate-driven checking.** For each cited sūtra or Ṛk, the cited *words* are printed next to the number. Look up which real numbers match those words and ask which of them is consistent with the glyphs. **Policy question for the user:** `CLAUDE.md` says take the Kannada source at face value, except standard reference material. Using a concordance only to *choose among readings the glyphs allow* and to flag discrepancies seems consistent with that; supplying a number the glyphs do not show is not. Ask before using it, and mark every number so confirmed.
8. **Consistency table.** Build a table `cited item → numbers read on each page`. The same sūtra read two ways in different places is a flag; the majority reading is a hypothesis to be checked against the glyph.
9. **Structural redundancy.** Page headers repeat Aṣṭaka/Adhyāya/Varga on every page of a run; a closing line says "ಇಲ್ಲಿಗೆ ... ನೇ ಸೂಕ್ತವು ಮುಗಿದುದು"; Ṛk counts per sūkta are known from the front matter. Use them to cross-check or fix header numerals.
10. **Different scans.** If the user can supply an even cleaner scan (≥ 800 dpi, or a second copy of the book), the confusions may vanish. A flat scan versus a photographed page matters.

## 6. Test set to build first

- **Gold (user-verified):** the user's review corrections in git history — commits `d218cc7` and `6eced87` on `main` change numerals in the Pīṭhike and Sūkta 137; and `publish/tools/numeral_pass/METHOD.md` lists the Vol 8 corrections (4-537→4-557, 2-9?2→2-252, 1-27→1-26). Extract (page, before, after) triples with `git show`.
- **Silver (this pass):** every numeral resolved in PDF 25–72 with a zoom tile; in `docs/PASS_LOG.md` and in the diffs of the commits titled "Vol 11: resolve [?] on printed pp. …". Treat as likely right, not certain.
- **Doubtful:** the numerals deliberately kept as `[?]` (grep `[?]` next to digits on PDF 25–72).
- Ask the user to confirm ~100 more numerals chosen to cover all confusion pairs (3/5, 6/7, 2/9, 8/9). That gives the test set a real gold core. Report accuracy per method on it.

## 7. Where everything is

- Repo: `bhargaviupa/rik-translation`, branch `main`.
- Files to correct: `Rigveda_Samhita_Vol11_English_Translation.md` and `Rigveda_Samhita_Vol11_Kannada_Text.md` (sections `### Printed p. N  (PDF M)` and `<!-- PDF M · printed N -->`; printed = PDF − 18). Each numeral appears in both files, in the same page section.
- Better scans: **not in the repo.** The user holds `11_Rigveda_Samhitha_Volume_11-1-70.pdf` and `…-71-140.pdf` (600 dpi). Merge with `sh publish/tools/verify11/merge_scans.sh a.pdf b.pdf` (needs poppler). Lower-quality full scan: `Rig_Vol11.pdf` (Git LFS; `git lfs pull`).
- Tools: `publish/tools/verify11/` (`ctx.py` lists `[?]` with context; `strips.py`, `tiles.py` render and zoom; `fx.py` edits both files safely; `pass_log.py` in `publish/tools/` logs a batch), `publish/tools/translit/` (script conversions), `publish/tools/numeral_pass/METHOD.md`.
- Older numeral-pass scripts (`pg.py`, `mont.py`, `apply_patches.py`, `BRIEF.md`) and the alternate Vol 8 scan (branch `alt-scan-vol8`) were used for Vol 8 and are **not on `main`**; look in `git log --all` and the remote branches if you need them. The Vol 8 review notes (`publish/review/Vol8_*numeral*`) are likewise only in history.
- Related briefs: `docs/VERIFY_PASS_REQUIREMENTS.md` (the page-by-page `[?]` pass), `docs/KANNADA_OCR_REQUIREMENTS.md` (an OCR-training project).
- Rules: `CLAUDE.md`. Digit key: §2 above.

## 8. Rules for this task

- Record numerals **as printed**; say "as printed" if they differ from the standard. Give no number where none is printed. Never complete a numeral from memory.
- Keep `[?]` when the glyphs allow two readings after the best effort; add a note naming the two candidates in the log, not in the text.
- Edit both files together, with `fx.py` (it refuses ambiguous edits). Log every batch with `pass_log.py`. Commit small; push to your assigned branch; no pull request unless asked.
- Do not edit other volumes' files. Do not commit the scans.
- Ask the user before using external concordances (§5, idea 7), before long jobs, and before sharing anything outside the repo.

## 9. Deliverables for the first session

1. `docs/numeral_testset.csv`: page, file, context, printed reading (if known), source (gold/silver/doubtful), notes — at least 300 rows.
2. A report comparing, on that set, at least three methods (e.g. visual strip reading, numeral-only Tesseract, glyph clustering) with accuracy per confusion pair.
3. A recommendation for how to read the remaining ~1,400 English / ~1,700 Kannada numeral `[?]` in Vol 11 (and the same in Vols 9–10), with an estimate of tokens per page.
4. If the user agrees, the chosen method run on Vol 11 PDF 73–140 first, then on PDF 24 and the pages that kept doubtful numerals.
