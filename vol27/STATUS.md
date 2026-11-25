# Vol 27 — status

*Update at the end of every working session. Rules: `CLAUDE.md`. Route: Batch API (as Vols 23 and 30).*

## Scope
Ṛgveda-saṃhitā Part 27: Aṣṭaka 7, adhyāyas 5–8 = Maṇḍala 9 Sūktas 101–114 and Maṇḍala 10 Sūktas 1–40 (`"mandalas": [9, 10]`). Printed pp. 1–992 (editor's preface dated 7-5-1954 and contents before p. 1). Editor-translator H. P. Venkata Rao. Branch `claude/zen-euler-5ntywc`.

## Source and inputs
Supplied by the user (Nov 25 2026) as three machine-read files, `rig_27_1.md` (pp. 1–385), `rig_27_2.md` (386–785), `rig_27_3.md` (786–992); concatenated into `vol27/html/rig_27.md` (inputs not kept; the user has them). Changes to the supplied text, and nothing else: (1) converter footers `Pages: N/N` removed; (2) the leading `Markdown source` line of parts 2 and 3 removed; (3) 79 embedded pictures moved to `vol27/html/figures/` by `tools/rv/extract_figures.py`; (4) `<!-- page 1 -->` inserted before the body title page (line 354); (5) 60 Pratipadārtha words corrected from the Wikisource Pada (`data/source_fixes.tsv`). The seams carry running heads (pp. 385/386, 785/786).
`html_pages.py` (with the head-variant fixes of Nov 25 2026, including a structural head pattern): 975 pages for printed 1–992; 17 printed numbers without a page of their own: 137, 148, 177, 241, 242, 281, 312, 349, 518, 549, 624, 625, 639, 773, 835, 843, 903 (not checked one by one).

## Word-meaning check (REQUIREMENTS C4/D18)
Before: 96 `fix-certain` rows; 60 applied (one letter, not an ending/voicing/visarga/initial vowel); after: 3,676 Pratipadārtha words ok (+60), 36 `fix-certain` left for the editor. Ṛks not matched to the reference: 930 Pada words (17%), 162 Pratipadārtha words.

## Preface
Translated by `api_front.py 27 2 72 preface` ($0.035, checks PASS, 0 NOTE), installed Nov 25 2026.

## Plan and batch
Full plan: 163 windows, 991 pages, 3,698,515 input tokens (estimate $3.70 + output $9.25–22.19). The user has about $8 of API budget (Nov 25 2026), so the batch is cut to the FIRST 120 windows (pp. 1–about 732, 2,739,105 input tokens; expected real cost $6.7–7.1 from Vols 23 and 30: $2.4–2.6 per million input tokens). The remaining 43 windows (about pp. 733–992, about $2.4) wait for more budget: `api_batch.py plan 27 --windows 60` continues after the last committed page.

## Status
Done through printed p. 794 (windows 1–130 of 163; the first batch 1–120 through p. 733, then a second batch of 10 windows, pp. 734–794, cost $0.58; one API batch of 120 windows submitted and collected Nov 25 2026; `batch.py audit 27` passes; `check_labels.py 27`: 1412 English blocks, 1412 Kannada, 0 not matched; `rkheads 27 --dry-run`: nothing to change). Sūktas present in order: Maṇḍala 9 Sūktas 101–114 and Maṇḍala 10 Sūktas 1–27 (41 headings). Preface translated and installed. **Real cost $6.95 + $0.58 for the two batches + $0.035 preface = $7.57 of the user's $8 (balance left about $0.22)** (estimate 2.74M input tokens: $2.5 per million). 304 `**NOTE**` marks, 383 rows in `review/notes.tsv`.

## Repairs (in `review/repair_log.md`)
10 windows stopped or failed after the commit: page mark of p. 148 (garbled head), a page heading glued into another heading (w0326), remarks (w0338, w0593), a wrongly numbered quoted verse (w0363), a glued word-list entry (w0393), garbled Pada labels (w0495, w0644), an inline quotation off from kn.md (w0611), a chapter-level `## Special Topics` heading (w0320), a second line of a Saṃhitā with its own headings (w0399).

## Second batch (Nov 25 2026)
The user's API balance showed $0.80: ONE more batch of 10 windows (pp. 734–794, 243,154 input tokens, expected $0.62) submitted; `collect 27` after it ends. Then 33 windows (pp. 795–992, about $1.9) remain.

## Not done: the last 33 windows (printed pp. 795–992, Maṇḍala 10 Sūktas 28–40 and the colophon)
They need about $1.9 more (33 windows × $0.058). When the user has the budget: `python3 tools/rv/api_batch.py plan 27 --windows 50` (free), show the estimate, `submit 27`, then the dry-run sweep and `collect 27`. The supplied text is complete (the colophon stands on p. 992).

## Open items
1. (user) about $2 of API budget for the last 33 windows.
2. (user) 383 `**NOTE**` questions in `review/notes.tsv`; 36 `fix-certain` word-meaning rows left and the `near`/`absent` rows (`review/pratipada_check_source.tsv`).
3. 17 printed numbers have no page of their own (see above).
4. After the last page: finishing checklist (HANDBOOK §11).
