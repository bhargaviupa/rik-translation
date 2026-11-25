# Vol 5 — second pass, S0 sieve (Nov 24 2026)

Made by `python3 tools/rv/second_pass_sieve.py 5` (new shared script; nothing in the volume was changed). Per-page rows: `sieve.tsv`; per-segment rows with the actual numbers: `sieve_segments.tsv`.
The Kannada used is a **preliminary** file made in the session's scratch directory with `tools/rv/prose_kn.py` (pp. 2–529 with `--rk-from 2`, pp. 531–708 as prose); the committed Kannada book is stage S1.

## (a) Supplied files and page map
- Seven files, 672 page heads found for printed pp. 2–708 (p. 1, the title page, is not supplied; p. 530 is blank by the print). Copies used for the stage: file 1 pp. 2–83 · file 2 pp. 85–184 · file 3 pp. 185–286 · file 45 pp. 287–467 · file 5 pp. 468–485 · file 6 pp. 486–583 and 531–583 as prose · file 7 pp. 584–708.
- **Two copies**: pp. 273–286 (files 3 and 45) and p. 584 (files 6 and 7). The copies agree to 99.5–100 % per page; differences are of punctuation (`:` against `ಃ`, a missing daṇḍa, ZWNJ), a letter now and then (p. 286: `ದ`/`ಧ`, `ಧೃ`/`ಯ`; p. 584: quotation marks and `ೇ`). Choice: file 3 for 273–286 and file 7 for 584 (file 7 is the later, cleaner reading of the end of the volume); each letter difference to be settled by the reader in S2 and not before. *The user may overrule.*
- **Pages without a head of their own (34 numbers, listed, not chased):** 84, 131, 154, 180, 193, 232, 233, 260, 290, 318, 324, 338, 366, 372, 390, 408, 414, 422, 434, 440, 444, 458, 465, 466, 484, 506, 514, 518, 542, 559, 566, 578, 604, 626 (+ 530, blank). Their text stands inside the neighbouring page of the supplied file; the sieve compares each English passage with the pages around it.
- **p. 83/84:** the head that reads 84 is taken as 83 by the splitter (as `STATUS.md` says); the page it holds starts with a picture note ("This image contains no discernible text"), 2 129 letters. Whether p. 84 (Pada and bhāṣya of Rik 48.15 per the English) is inside it is to be looked at in S1.
- The English file is **organised by Ṛk, not by page**, in pp. 1–529 (headings `### Rik a.b (pp. N–M`, inline marks `(p. N`); 201 of the 708 pages carry no mark of their own there. The Pariśiṣṭa has a `### Printed p. N` heading per page (p. 644 has none). The sieve therefore compares each English *segment* (text between two marks) with the Kannada pages *first page − 1 … next segment's first page*. Counts below are per segment, listed under the segment's first page.

## (b) `batch.py audit 5`
Does not run: Vol 5 has no `volcfg.json` (legacy, family L1) — "no config … run `batch.py new 5`". Not created (rule 6: no per-volume set-up outside the shared tools). Invariants checked by the sieve instead: page coverage (above), numbers, references, scripts, remarks.

## (c) Checks
| printed pages | English pages | refs only in the English (pages) | plain numbers (2+ digits) only in the English (pages) | Devanagari quotations of the commentary not found | `[?]` | `[sic]` | bracketed remarks | `**GLOSS**` |
|---|---|---|---|---|---|---|---|---|
| front (before p. 1) | 1 | 9 (1) | 41 (1) | 0 | 4 | 1 | 1 | 0 |
| 1–100 | 81 | 116 (57) | 63 (36) | 5 | 2 | 5 | 23 | 23 |
| 101–200 | 82 | 110 (67) | 61 (40) | 6 | 38 | 18 | 35 | 40 |
| 201–300 | 95 | 139 (71) | 54 (39) | 4 | 46 | 10 | 41 | 18 |
| 301–400 | 94 | 101 (70) | 64 (44) | 0 | 20 | 10 | 37 | 7 |
| 401–500 | 94 | 126 (78) | 60 (45) | 1 | 26 | 18 | 61 | 2 |
| 501–600 | 98 | 163 (74) | 40 (23) | 0 | 29 | 1 | 64 | 1 |
| 601–700 | 99 | 132 (61) | 7 (7) | 0 | 32 | 1 | 121 | 0 |
| 701–708 | 8 | 27 (7) | 10 (2) | 0 | 31 | 0 | 2 | 0 |
| **whole volume** | **652** | **923 (486)** | **400 (237)** | **16 (13 pages)** | **228 (132 pages)** | **64** | **385** | **91** |

- **Numbers and references.** 923 reference tokens (with separators) in the English are not in the supplied pages they should stand on, over 486 pages; 400 plain numbers of 2+ digits over 237 pages. **141 of the 652 English pages show none of the three difference kinds.** These are candidates for R1, not errors: the sieve cannot tell an English that is wrong from a Kannada reference that the English writes in another form (I-32-6, 1.32.6, "Rik 47.1"-style headings, pages cited by number) or from a supplied number that the English moved to the segment before. Example checked by hand, p. 593: English "Ā. Gṛ. Sū. 4-8-10; Kau. Sū. 33", "33 sūktas … 6 … 43", "8-96-8", "13-1-18"; supplied text "೪-೮-೪೧; ಕೌ ಸೂ. ೫೧-೭", "೩೩ … ೭ … ೪೨", "೮-೮೫-೮", "೧೩-೧-೧೩". By the user's decision of Nov 24 2026 such places are settled in favour of the supplied text with a logged repair.
  - Pages 1–184: the repair pilot compared only the `[?]` places there (`html_repair_log.tsv`); its pages are *not* free of number differences: 1–184 still show 205 reference tokens only in the English on 112 pages and 116 plain numbers. The pages after 184 start S2 as the prompt says, but **pp. 1–184 need the number pass of S2 too** (decision for the user, below).
  - The front matter (key to abbreviations, table of contents; "page 0" in the table) holds the English's own page numbers; ignore its 9 + 41.
- **Abbreviations of references** (`refs_apply.py 5`, preview): "Vol 5: nothing to change"; the list has 78 forms and 286 decided mistakes. Nothing for S3 from this check.
- **Letters of other scripts.** English: no Cyrillic, Arabic, Bengali, Tamil, Telugu, Malayalam or CJK letters. 141 English lines hold *Kannada* letters (quoted words and numerals, e.g. lines 3, 30, 123, 302); these are the print's own words and are inventoried, not judged. Supplied Kannada: three places with letters of another script, all **R6 cases for S2**: p. 464 Bengali `শ্রীশ্রীদুর্গা` (a line between the numbers 60 and 466 in the machine reading), p. 606 Telugu `అగ్ని` as a stray line (= ಅಗ್ನಿ), p. 708 Tamil `இவனுக்கு` inside a Kannada sentence (to be decided by the sentence in S2).
- **Legacy remarks inventory (kept, rule 5):** `[?]` 228 in 132 pages (30 of them in pp. 1–184 after the pilot; 31 in pp. 701–708 alone, the last page and the printer's line); `[sic]` 64; bracketed remarks (12+ letters) 385; `**GLOSS**` 91 (matches `STATUS.md`); 18 labelled glosses left (`review/glosses_left.tsv`).
- **Sanskrit citations.** The Saṃhitā, Pada and bhāṣya blocks are *not* compared (rule 2). Devanagari quotations inside the commentary (Vyākaraṇa-prakriyā, Special Topics, Pratipadārtha) compared letter for letter with the supplied page: 16 quotations on 13 pages do not match (pp. 1, 30, 91, 106, 128, 139, 147, 168, 247, 250, 266, 273, 476): R3 candidates for S2.

## What S2 will be
About 650 English pages in 672 supplied pages; pp. 185–708 = 524 pages ≈ 18 batches of 30 pages after the 10-page pilot; pp. 1–184 are another 6 if the user wants the number pass there too (the repair pilot did only the `[?]` places).

## Open decisions for the user
1. Copies to use for pp. 273–286 and 584 (proposed: file 3, file 7).
2. Whether S2 also covers pp. 1–184 for numbers/references (proposed: yes, as the last batches).
3. **The user's readings for pp. 578–625** are in `archive/vol5/review/pending_doubts_p578-625_user_readings.txt` (not in `vol5/`; STATUS and README name no file): 7 entries, 2 of them "x" (crop did not show the place), 5 readings (603_d2 `7-47-1 and 2`, 608_d1 `1-127-1`, 611_d6 `3-1-12 and 13`, 622_d8 `3-62-7, 7-97-7`, 625_d9 `2-24-11`). They are applied in S3 where the supplied text agrees or is silent; where it disagrees both go to `questions.tsv`. No action needed from the user.
