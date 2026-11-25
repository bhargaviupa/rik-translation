# Vol 30 — status

*Update at the end of every working session. Rules: `CLAUDE.md`. Route: Batch API (as Vol 23; `docs/prompts/VOL23_API_PROMPT.md`).*

## Scope
Ṛgveda-saṃhitā Part 30 (Jayachamarajendra Vedaratnamala no. 30), the LAST part of the edition: Aṣṭaka 8, adhyāyas 5–8 = Maṇḍala 10 Sūktas 95–191 (`"mandalas": [10]`); ends with the colophon "ಋಗ್ವೇದಸಂಹಿತೆಯು ಸಮಾಪ್ತವು" and the benediction. Printed pp. 1–1288 (preface roman i–vii and contents viii–xii before p. 1). Editor-translator H. P. Venkata Rao; preface dated 30-9-1955. Branch `claude/zen-euler-5ntywc`.

## Source and inputs
Supplied by the user (Nov 25 2026) as three machine-read markdown files, `rig_30_1.md` (pp. 1–475), `rig_30_2.md` (476–975), `rig_30_3.md` (976–1288); concatenated into `vol30/html/rig_30.md` (the inputs are not kept; the user has them). Changes to the supplied text, and nothing else: (1) the converter footer lines `Pages: N/N` removed from each part; (2) the leading `Markdown source` line of parts 2 and 3 removed; (3) 132 embedded pictures moved to `vol30/html/figures/` by `tools/rv/extract_figures.py` (line replaced by `[figure: …]`); (4) `<!-- page 1 -->` inserted before the body title page (line 667); (5) 83 Pratipadārtha words corrected from the Wikisource Pada (`data/source_fixes.tsv`, see below). The seams (pp. 475/476 and 975/976) carry running heads, nothing lost.

`html_pages.py` (with the head-variant fix of Nov 25 2026, `ಸಾಯಣಭಾವ್ಯ/ಭಾಷ್ಪ/ಭಾಜ್ಯಸಹಿತಾ`, `ಋಗ್ವೇದಸಹಿತಾ`): 1271 pages for printed 1–1288; 17 printed numbers have no page of their own: 27, 148, 207, 237, 242, 243, 344, 598, 599, 941, 1059, 1081, 1129, 1130, 1207, 1241, 1271 (their text stands inside the page before; not checked one by one whether a head is misread).

## Word-meaning check (REQUIREMENTS C4/D18), Nov 25 2026
`pratipada_check.py 30 --source`: before: 143 `fix-certain`; 83 applied by `pratipada_apply.py` (one letter, not a case ending, voicing swap, visarga or an initial vowel added/dropped); after: 5,239 Pratipadārtha words ok (+83), 60 `fix-certain` left for the editor. Ṛks not matched to the reference: 161 Pratipadārtha words, 455 Pada words (small share).

## Preface
Translated by `api_front.py 30 3 253 preface` (one request, $0.119, checks PASS, 0 NOTE) and installed Nov 25 2026.

## Plan (free)
`api_batch.py plan 30 --windows 260`: 212 windows, about 1285 pages, 4,855,941 input tokens, estimate input $4.86 + output $12.14–29.14. Vol 23's real cost was about 74% of the low end of its estimate, so about $12–13 is expected. Not submitted: waiting for the user's yes (ceiling $20, user, Nov 25).

## Batch
Submitted Nov 25 2026 (user's yes, ceiling $20): ONE batch of 212 windows, id in `vol30/work/api_batch.json`. Next: `api_batch.py status 30` until ended, then `collect 30`.

## Open items
1. (user) yes to submit; budget $20 stated Nov 25.
2. (dispatcher) after `collect`: finishing checklist (HANDBOOK §11).
