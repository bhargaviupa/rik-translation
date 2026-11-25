# Brief: second reading of the English of Sāyaṇa's bhāṣya (by a reader who did not write it)

Why: measured on this work, a drafter's own reading misses much (Fable second readings of Sonnet drafts of 3.32–3.39 made 242 corrections in 93 Ṛks, 73 of them changing what a reader would understand Sāyaṇa to say), and the Sonnet drafters of 1.2 and 1.4 reported that they did not do their own second reading. The form check cannot see any of this.

You get one sūkta `M.S`. The Sanskrit units are in `sayana_book/task/M<m>_S<sss>.md` (run `python3 tools/rv/wsbook.py task M S` if the file is missing); the English is `sayana_book/en/M<m>_S<sss>.md`. Read `docs/WSBOOK_BRIEF.md` and `tools/rv/BHASHYA_BRIEF.md` rules 1, 2, 4, 5, 6, 8: the English is held to them.

For EVERY unit, one by one, read the Sanskrit first, then the English, and ask two questions only:
(a) **Does the unit say this?** Anything the unit does not say (an accent, a rule, a reason, a gloss, an epithet, an "our" for "for us", a dictionary sense where Sāyaṇa gives his own gloss, an epithet moved to another word) is wrong: correct it.
(b) **Is every word and clause of the unit rendered?** `अपि`, `एव`, `यद्वा`, the alternatives, the possessives, the grammar at the end of the unit. What is missing is added.
Also check each ⟦ ⟧ citation for sense: the sense of a cited root or word must stand in the English.

Correct the English file in place (keep the `## SBh …` headings and the unit order; do not touch the Sanskrit; keep the translator's `**NOTE**{…}` marks unless the NOTE is plainly answered by the unit itself). Log every change as a row of `sayana_book/review/M<m>_S<sss>.tsv`: unit · kind (dropped / wrong sense / wrong attachment / addition / citation / wording) · before (a few words) · after (a few words). A change of wording only (no change of meaning) is allowed but counted separately: do not polish for style. Run `python3 tools/rv/wsbook.py check M S` at the end; it must print VERIFIED. Do not commit or push.

Report: the number of units read, the number of changes by kind, and the units where the Sanskrit itself seems damaged or you could not decide (say so; do not guess). The count is the point: report it honestly, including zero.
