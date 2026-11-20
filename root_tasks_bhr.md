# What this session did (Nov 10 – Nov 20 2026)

*Written at the end of the session `claude/affectionate-faraday-2iv8y4`, at the user's request, as one plain account of everything done in it, why, and what was left open. Counts are from commands run in the session on the dates given; estimates are called estimates. For the live state of any volume read `volN/STATUS.md`; for what stands between a volume and publication read `PUBLICATION_TODO.md`; for parked decisions read `TODO.md`.*

---

## 1. Where it started, and the turn it took

The session began as a continuation of the batch translation of the Ṛgveda volumes (Kannada edition of 1949–52, Sāyaṇa's bhāṣya with H. P. Venkata Rao's Kannada commentary, translated into English). Early on it finished Vol 17 by the Batch API ($20.14), repaired its Ṛk headings, wrote the prompt for re-checking Vol 1, made the Vol 17 PDFs, scaffolded Vol 13 for re-translation, extended `check_labels.py` to the older layouts (Vol 15 pp. 237–238 repaired) and converted the layout of Vol 16 to the Vol 17 form, removing the remarks "as supplied".

That last step damaged about 70 sentences of Vol 16 (the punctuation around removed remarks). The user then said the 40-window batch approach "is not working… too many mistakes are creeping in" (Vol 11, re-translated in another session, again had many errors). The user asked to stop and think before changing anything, and the rest of the session was, first, a redesign, and then work on getting every volume to a publishable state.

## 2. The redesign (Nov 12–13)

At the user's request the session wrote the documents that replace the scattered notes:

| Document | What it is |
|---|---|
| `docs/REQUIREMENTS.md` | What a volume must be: volume structure (Part A), generic rules (B), specific rules per section (C), checks (D), working rules (E), open questions with the user's decisions (F), effect on old volumes (G), and what is missing before anything can be **published** (H: rights, editorial readiness, making the physical book, registration). |
| `docs/DESIGN.md` | How: **the book is data**. A volume is an ordered list of units (`volN/data/units.jsonl`); structure comes from the Kannada text and the accented reference by script; the model only fills English or reads; the same work can be run by the API or by agents; second reading; release gate; review copies in `volN/review/`, final copies only in `publish/out/`. Approved by the user on Nov 13. |
| `docs/ERROR_KINDS.md` | Every kind of error in the records, scan-based and html-based volumes separately, each with what would prevent or catch it. |
| `docs/TOOLKIT_PROPOSAL.md` | Which documents, tools, reports and logs are really needed, and for what. |
| `docs/LEGACY_VOLUMES_PLAN.md` | A low-cost way to correct Vols 1–10 and 13 and make their Kannada books ("three sieves": script, a reader that only reports, correction only where something was found). |
| `docs/review/USER_REVIEW_2026-11-12.md` | The user's review comments, verbatim. |
| `docs/REDESIGN_START.md` | A prompt for starting the redesign in a new session. |

The user answered the open questions (F1–F17) and gave the constraints that shaped everything after: **the user has little API credit and must be able to choose agents for any task**; `publish/out/` holds final copies only; no `.docx`/`.html` in the volume folders; old per-volume scripts moved to `archive/volN/` (418 files); the English printed under the verses is headed "English translation" with no name until its source is verified; the Sanskrit grammar section is Sanskrit; no split of volumes for now.

## 3. The new tool `rv/` and the proof on Vol 17 (Phase A)

`python3 -m rv structure|import|refs|print VOL` (new code beside the old pipeline, which keeps working):

- **structure**: cuts a volume into units from the Kannada text and the reference verses; compares every verse with the reference; writes the faults and decisions as data.
- **import**: lays the existing English into the units, proves every paragraph is placed once, that every Sanskrit block equals the source, attaches the editor's questions, applies the editor's decisions and the one list of abbreviations.
- **print**: builds the review copies (English and Kannada) in the agreed order of front matter, with a footer carrying edition page, Maṇḍala, Anuvāka, Sūkta, Aṣṭaka, Adhyāya, Varga and "REVIEW COPY".

Proof on Vol 17: 41 sūktas, 441 verses all matched to the reference; 10,967 of 10,967 English paragraphs placed once; 1,316 of 1,320 Sanskrit blocks equal to the source; 471 of 471 questions attached; review PDFs of about 1,750 pages (English) and 1,181 (Kannada). The user: "I am happy with the outcome."

Rulings the user gave while this was built (all recorded in `TODO.md`, `docs/REQUIREMENTS.md` and `vol17/data/`):

- **The reference text is the correct source of every verse.** A difference of the supplied verse is a misreading of the machine text and gets no footnote, unless the editor records that the printed book really differs (`data/verse_decisions.tsv`). The user checked six differing places against the book; all six agreed with the reference. The Kannada book's verse is corrected from the reference too, word by word (Vol 17: 374 words in 257 verses, listed).
- Stray lines (page numbers, ornaments) are removed from both books and kept only as a record.
- The first sūkta follows the Maṇḍala heading on the same page; "Viśeṣa-viṣaya" is printed as "Special Topics".
- One list of abbreviations of works (`rv/references.tsv` → `docs/REFERENCES.md`); the user decided 21 forms on Nov 14 (Kṛ. U./Saṃ./Ā. are Tai. U./Saṃ./Ā.), and the rest of the proposed corrections.
- The user answered 67 of Vol 17's 471 questions from a spreadsheet; they are carried out (88 decided, 47 paragraphs changed). **383 questions are still open**, six answers wait for the word in script (rows 6, 11, 13, 16, 21, 60) and one was lost by the spreadsheet (row 15).
- A **second-reader measurement** on 72 Vol 12 pages with 18 known errors: Sonnet found 10, Haiku 7 (about 13,500 agent tokens per page). An Opus or Fable measurement was offered; the user declined it ("lets not do it"). Fable costs four times Sonnet per token, so Sonnet stays the translator.

## 4. Supplied text, volume by volume (Nov 17–19)

The user supplied the machine-read text (HTML/markdown) of the volumes made from scans, to be used to cross-check the English, make the Kannada books, and correct numbers and Sanskrit. Each file was put in `volN/html/`, embedded pictures were moved to `volN/html/figures/` (`tools/rv/extract_figures.py`, now also reading `<img src="data:…">` anywhere in a line), the page range and page heads were checked, and `volN/STATUS.md` records what was done.

| Volume | Supplied text now | Notes |
|---|---|---|
| 1 | whole (3 files; file 2 converted from HTML to markdown with pandoc at the user's request) | the existing Kannada file (704 of 720 pages) was made from the HTML form and should be made again from the markdown |
| 2 | whole, pp. 2–808 | a file uploaded twice as `rig_2_1.md` was from another volume (Maṇḍala 6–7) and was not kept; the right one arrived later |
| 3 | whole, pp. 2–647 | file 1 was HTML under a `.md` name; converted to markdown |
| 4 | whole, pp. 2–608 | |
| 5 | whole, pp. 2–708 (7 files) | pp. 273–286 and 584 stand in two files |
| 6 | whole, pp. 2–619 (4 files) | p. 82 supplied as its own file |
| 7, 8, 9, 10, 13 | **none yet** | |
| 11, 12, 14–21 | already in the repository from earlier work | |

The page splitter (`tools/rv/html_pages.py`) now takes the line after pandoc's `::: header` as a running head whatever its words. **Lesson 67 (user):** page numbers without a running head are generally the first pages of a new sūkta or maṇḍala; they are listed once and not chased.

## 5. Vol 2 clean-up, glosses and cross-references

- **Vol 2**: the user did its translation and second reading from scans and called it good; page numbers are right; many `[?]` are remarks of ours; accents were made without the reference. A separate session (prompt `vol2/CLEANUP_PROMPT.md`) removed remarks by kind, with every removal logged, and replaced the Saṃhitā verses of Sūktas 3–19 by the reference's (93 of 176 verses changed). Not decided: what to do with the 429 `[?]` it kept at the time.
- **Cross-references**: `CROSS_REFERENCES.tsv` / `.md` at the root list every reference in every volume by page and line (`tools/rv/crossrefs.py`; at the last run 42,953 references in 21 volumes, 6,627 to Ṛks, 23,914 grammatical sūtras, 12,412 to other works).
- **Glosses of quoted Ṛks**: the edition quotes verses without a Kannada meaning and the translation added its own glosses, many incomplete. **Decided by the user:** our own edition's translation of that Ṛk will fill the gloss by script; until that volume exists a placeholder stands, and **a final copy is not printed while a placeholder remains** (requirement B3.5, gate D9). Not built, at the user's word. Meanwhile 682 labelled glosses of Vols 2–8 were replaced by the marker `**GLOSS**` (`tools/rv/gloss_marker.py`; removed text kept in `volN/review/glosses_removed.tsv`; 30 changes read before and after; none damaged). A further gloss session (prompt `docs/GLOSS_PROMPT.md`) replaced 277 more and left four questions for the user (T12 in `PUBLICATION_TODO.md`).

## 6. Prompts written for other sessions

| File | For |
|---|---|
| `vol19/CONTINUE_PROMPT_HTML.md`, `vol20/CONTINUE_PROMPT_HTML.md` | translating Vols 19 and 20 **by agents, not by the API** (preparation of the text, the three-window agent loop, stage checks with the new tool, `**GLOSS**` for unexplained quotations in Vol 20) |
| `vol2/CLEANUP_PROMPT.md` | the Vol 2 clean-up |
| `docs/GLOSS_PROMPT.md` | the gloss work |
| `vol1/CONTINUE_PROMPT_HTML.md`, `vol13/CONTINUE_PROMPT_HTML.md` | the re-check of Vol 1 and the re-translation of Vol 13 |

Vols 19, 20 and 21 were translated in their own sessions on their own branches and merged into `main`; their audits pass.

## 7. The publication list

`PUBLICATION_TODO.md` (root) is the user's one list: where each volume stands (counted), the 13 things only the user can supply (rights in the Kannada edition, permission for the accented verses, portraits and cover, the statement of how the translation was made, the user's preface, publisher and ISBNs, printer and page size, a scholar's sample, decisions on the question lists, and so on), eleven steps from supplied text to release with a box per volume, work still to be done on the tools (T1–T13), a suggested order and a change log. `CLAUDE.md` tells every session to keep it current. Its first line is still true: **no volume can be published today.**

## 8. Git work

- Everything of this session is on `main`. Branches of other sessions were merged where the user asked: `amazing-ride` (gloss session), `elegant-rubin` (Vol 21 PDFs) and `serene-ride` (Vol 20 PDFs). The first had conflicts in four volume texts (gloss markers against reference-name corrections on the same lines): the gloss version was kept and the names were re-applied by `tools/rv/refs_apply.py` (30 places); marker counts equal the removed-gloss records (82, 115, 248, 9).
- The small tool fixes of the Vol 19 session (page-head reading, introduction lines, `check_labels`) were brought to `main` for Vols 19 and 20.
- **Not merged, on purpose:** `claude/happy-mendel-dlsvjz` (128 commits, another session's bhāṣya-reader and second-reading work) and `claude/dreamy-cerf-z4h3f4` (kept for its build-time transliteration, to be consulted when the printer takes over all volumes).
- Remote branch deletions often return HTTP 403 from here; the user deleted merged branches on GitHub.

## 9. Still open (nothing below was done in this session)

1. **Rights and permissions** (the Kannada edition, the verses, portraits, the statement on AI assistance): block every volume; need the user, probably with advice.
2. **Supplied text still wanted:** Vols 7, 8, 9, 10 and 13.
3. **The questions in each new-style volume** (Vol 17: 383 open; Vol 11: 471; Vol 18: 333) and the user's answers still outstanding (Vol 17 rows 6, 11, 13, 15, 16, 21, 60; 39 abbreviation forms).
4. **Vol 16:** about 70 places with broken punctuation from the removal of "as supplied": repair or undo, undecided.
5. **Not built yet:** the translation step in the new form (units instead of windows), the second reading as a regular step, the release gate and final-copy build, the import of the older layouts (Vols 1–10), units for continuous prose (Vol 1's first 605 pages), the table of Ṛk translations that fills the glosses, the one vocabulary for the whole series.
6. **Parked decisions** in `TODO.md`: spelling of the printed verse (इन्द्र or इंद्र), layout of the pages before the preface, whether the edition's English is H. H. Wilson's, volume length for the printer, the scholar's sample.
7. **Standing rules to keep:** the API key stays in `RIK_API_KEY` and is never printed; any API spending only after the user has seen the estimate; agents must always be possible instead; the supplied text is the base, except that the Saṃhitā comes from the reference; no force-push; no pull requests unless asked.
