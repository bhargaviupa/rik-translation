# Vols 1–10 and 13: correcting the errors and making the Kannada books at low cost — proposal (DRAFT)

**Nov 12 2026, for the user's review. Nothing has been run; every cost below is an estimate and is marked as such.** It answers the user's point: these volumes "still need error correction and Kannada PDF files; we have to invent a way to reduce the cost of doing this."

## 1. Where these volumes stand (counted Nov 12 2026)

| Volume | English (words) | Kannada file | Supplied machine-read text in the repo | Open, by the records |
|---|---|---|---|---|
| 1 | 238,000 | yes (read from scans) | no — the user will supply it | 312 doubt marks; 148 pages without their Sanskrit |
| 2 | 322,000 | none | no | 11 numerals unchecked |
| 3 | 233,000 | none | no | 537 doubt marks |
| 4 | 218,000 | none | no | 151 doubt marks, 103 accent doubts |
| 5 | 270,000 | none | one file of several | user's readings for pp. 578–625 not applied |
| 6 | 238,000 | none | no | 183 numeral rows await the user |
| 7 | 229,000 | none | no | 173 numeral differences |
| 8 | 336,000 | none | no | 225 numeral differences; about 280 flagged pages |
| 9 | 204,000 | none | no | 274 numeral differences |
| 10 | 282,000 | none | no | 2,869 doubt marks |
| 13 | (old text set aside) | none | no | to be re-translated (decided Nov 11) |

Together about 2.6 million words of English, on roughly 7,500–8,000 printed pages. What is wrong with them is known in kind (`docs/ERROR_KINDS.md`, Part 2): **mostly misreadings from the page images** — digits above all (where the user's numeral files were compared, about a quarter of the numbers differed), then Sanskrit letters, then Kannada words — and, less often, errors of meaning.

## 2. What it would cost done the plain way (estimate)
- **Re-translate everything** by the Batch API as Vols 17, 18 and 11 were: measured so far at $0.010–0.015 a page, so about **$80–120** for 8,000 pages, plus the second reading that the new method requires, about half as much again. Total roughly **$120–180**. It would also discard eleven volumes of existing English.
- **Check page by page with agents** (the Vol 1 plan): about 10,000 tokens of the session's allowance per page for translation-grade work; less for checking, but still the most expensive way per page.

## 3. The idea: three sieves, each cheaper than the next would be
The errors are of different kinds, and most kinds do not need a model at all. Each sieve removes what it can, so the costly step sees only what is left.

**Sieve 1 — by script, no model cost. Needs the supplied text of the volume.**

| What | How | Error kinds removed (`ERROR_KINDS.md`) |
|---|---|---|
| The **Kannada book** | made from the supplied text by the existing scripts, as for Vols 11–18 | this is the whole of the missing Kannada books |
| **Saṃhitā** | taken from the reference text (requirement B1.2) | S10, S12 |
| **Pada-pāṭha, Sāyaṇa-bhāṣya, quoted verses** | the Sanskrit read from the scans is replaced by the Sanskrit of the supplied text; the English around it stays | S7, S8, S9, S11 |
| **Numbers and references** | each number in the English is compared with the supplied text at the same place and replaced where the place is found once and unambiguously; the rest is listed | S1, S2, S4, S5, S6 |
| **Structure** | pages, sūktas and Ṛks are checked against the supplied text and the reference; missing or doubled parts are listed | S17, S19–S21 |

In Vol 17's Kannada file about a quarter of the text is verbatim Sanskrit; in the scan-based volumes that quarter is exactly where the reading errors sit, and none of it needs to pass through a model.

**Sieve 2 — a reader that only reports, at low cost.**
Each page of English is read against the Kannada of the supplied text by the model, through the Batch API, with one instruction: *list what is wrong* (wrong sense, reversed roles, something added, something left out, a name or term misread). It does not rewrite anything.
- This is the **same second reading** that the new method needs for every volume (requirement D2). Built once, it serves the old volumes and the new ones.
- Why it is cheap: the price of a model's output is five times the price of its input. Translation writes a page of output for every page; a reader writes a few lines. The Sanskrit blocks, already settled by Sieve 1, are left out of what it is sent.
- Estimate: **$0.004–0.008 a page**, so **$30–65 for all eleven volumes**. Not measured.

**Sieve 3 — correction, only where Sieve 2 found something.**
The flagged passages, and only those, are corrected: by the model with the Kannada beside it, as a logged repair; anything doubtful goes to the editor's list.
- If one page in four is flagged (the rate of Vol 12's sample), this is a quarter of the pages and a paragraph or two on each. Estimate: **$5–15 in all**. Not measured.

**Estimated total: $35–80 for the eleven volumes, against $120–180 for re-translating them**, and the existing English is kept.

## 4. Further ways to hold the cost down
1. **Measure before spending.** Vol 12 has 72 pages on which 18 errors are already known from its QA sample. Running the reader on those pages shows, for well under a dollar, how many of the known errors it finds. If it misses many, the plan changes before any volume is touched.
2. **Try a cheaper model as the reader** on the same 72 pages. If it finds the same errors, Sieve 2 costs a third as much; if not, it is not used.
3. **Fix the format first.** The open questions of `REQUIREMENTS.md` (section names, transliteration under the bhāṣya, the footer) are settled before the old volumes are rebuilt, so that no volume is paid for twice.
4. **Use what the user has already paid for in time:** the numeral files of Vols 6–10 and 13 and the typed readings. Where a file and the supplied text agree, the number is settled without a model.
5. **Worst first, or wanted first.** The order is the user's: by error load (10, 13, 8, 3) or by which volume is to be published first.
6. **Vol 13 as the experiment.** It is to be re-translated anyway and its old English exists. Doing 30 pages both ways — re-translation, and the three sieves on the old text — gives the real cost and the real difference in quality for the same pages.

## 5. What it depends on
1. **The supplied machine-read text for Vols 1–4, 6–10 and 13** (Vol 5 has one file of several). Without it there is no cheap Kannada book and no Sieve 1. This is the one thing only the user can provide.
2. The old English must be **aligned** with the supplied text page by page and part by part. The old volumes have page headings and section labels, in several older forms; where a passage cannot be aligned it falls through to translation. How often that happens is not known until it is tried.
3. The **meaning errors that the reader misses** remain. The measurement of §4.1 says how many to expect.
4. Rebuilding the old volumes in the standard structure changes their layout; the Vol 16 trial showed that doing this by pattern-matching on finished text damages sentences. Here the structure comes from the supplied text and the old English is placed into it, which is a different operation, but it needs its own test on a few pages before a volume.

## 6. Decisions for the user
1. Can the supplied text for Vols 1–4, 6–10 and 13 be provided, and in what order?
2. Shall the free measurement of §4.1 be run first (it needs a few cents of API budget and no volume is changed)?
3. Vol 13: re-translate as decided, or use it for the two-way experiment of §4.6?
4. Is it acceptable that an old volume, once corrected this way, keeps its existing English wording wherever the reader found nothing wrong?
