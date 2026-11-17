# Prompt for the Vol 2 clean-up session (paste into a new Claude Code session on this repo)

You clean up **Volume 2** of the Rigveda translation (repo `bhargaviupa/rik-translation`; Maṇḍala 1 Sūktas 3–19; `vol2/Rigveda_Samhita_Vol2_English_Translation.md`, 17,942 lines). **It is not re-translated and not restructured.** Read `CLAUDE.md`, `PUBLICATION_TODO.md`, `vol2/STATUS.md`, and in `docs/LESSONS.md` the entry of Nov 12 2026 on Vol 16 (removing remarks by pattern left about 70 sentences with broken punctuation: that must not happen here).

## What the user said (Nov 17 2026)
> I did the translation and second reading from scans and it is in a good condition. A lot of ? are Claude remarks that can be removed or questions as part of the content that can be ignored. Since the work was done from scan, the page number is correct too. So let's not go for retranslation yet. See what you can clean up. I think I did not have the reference file for accents during that translation, so we may have to reverify the accents.

So: the English and the page headings (`### Page N`) are trusted. The work is (A) removing what is ours from the text and (B) verifying the accents of the verses against the reference. Nothing is spent on the API.

## Start
1. `git fetch origin main && git merge origin/main` on the branch this session was given; `pip install indic-transliteration rapidfuzz openpyxl`. Never force-push; no pull request; push to `main` only when the user says so.
2. Record in `vol2/STATUS.md` that the file is opened for this agreed pass (user, Nov 17 2026). Every change to the text is a logged repair: `vol2/review/repair_log.md` (what, how many places, how it was checked).

## Part A — what is ours comes out of the text

**Step A1: count and propose; change nothing yet.** Make `vol2/review/cleanup_proposal.md`: every kind of mark or remark, its count, three examples with their page, and what you propose to do with it. Counts taken on Nov 17 2026, to be confirmed by your own:

| Kind | Count | Likely action |
|---|---|---|
| `[?]` in all | 432 | — |
| … inside a sentence of ours about the marks ("numerals marked [?] where unsure") | about 66 | the whole sentence of ours goes |
| … after a number or reference ("6-1-5 [?]") | about 259 | mark goes, number stays as read |
| … after Devanagari or transliterated Sanskrit | about 64 | mark goes, reading stays |
| … elsewhere | about 43 | read each one |
| `[sic]` | 143 | mark goes |
| `[as printed]` (146), other "as printed" wording (about 750 more) | 901 | read a sample first: some are ours, some may be the commentary's own words |
| "mine and tentative" | 92 | the remark goes; decide with the user whether the gloss it is attached to stays |
| "I read …", "I am unsure", "best effort", "not legible" | about 58 | read each one |
| the "Translator's Preface" and "Roadmap" at the head, the closing progress note, old mid-file notes, a stray Cyrillic string (see `vol2/STATUS.md`) | few | list them; front matter is rebuilt later, the notes go |

Also search for what this table does not name: first-person sentences, "the scan", "the print", "Claude", "session", "pass", bracketed asides, letters of other scripts inside English words. **Show the user the proposal and wait for a yes before Step A2.** Ask in the same message what is to happen to the places where a `[?]` stands for a reading that is really uncertain (proposal: the mark goes from the text and the place is kept in `vol2/review/open_readings.tsv` with page and sentence, so that nothing is forgotten).

**Step A2: carry out, one kind at a time.**
- By script (in `tools/rv/`, not a per-volume tool; extend `to_note_style.py` if it fits), and only for forms you can describe exactly. A remark is removed whole, with its brackets, its separator and its space; never half a sentence.
- Every removed remark is written to `vol2/review/removed_remarks.tsv` (page, line, text removed, the sentence before and after), so that any removal can be undone.
- After each kind: check by script for damage (empty brackets, a bracket without its partner, doubled or missing spaces, ` ,` ` .` `;;` `( `, a sentence that now begins with a lower-case word or ends without a stop) and **read 30 of the changed sentences yourself**, before and after. Report both counts. If more than one of the 30 is damaged, undo that kind and do it differently.
- Devanagari and transliteration are not touched in Part A. No sentence of the translation is reworded.
- Commit and push after each kind.

## Part B — accents of the verses

The user decided on Nov 13 2026: the reference text (`refs/mandala/rv_mandala1.html`) is the correct source of every verse. Vol 2's accents were read from the scans in Oct 2026 (about 6,300 lines carry accent marks).

1. **The shared tool does not see this volume yet:** `python3 publish/tools/accents/accent_volume.py 2 --dry` reports nothing (run Nov 17 2026), because Vol 2's layout is older (verse blocks as `>` lines ending in `॥N॥`, 188 Saṃhitā labels, labels such as `**॥ Pada-pāṭhaḥ ॥**`). Teach the shared tool this layout; do not write a Vol 2 tool.
2. **Report first, by script:** for every Ṛk of Sūktas 3–19, the Saṃhitā lines in the file against the reference: equal with accents; letters equal and accents differ; letters differ; not found. The count of verses must equal the reference's for these sūktas; say so. Write `vol2/review/accent_report.tsv` and tell the user the four counts with five examples of each kind of difference.
3. **On the user's yes:** the Saṃhitā lines are replaced by the reference's (accents and letters), each replacement listed in `vol2/review/verse_corrections.tsv`. Where a verse is not found, nothing is changed and the place is listed.
4. **Pada-pāṭha and verses quoted inside the commentary:** the reference has only the Saṃhitā. Count how many of these carry accents in the file and report; change nothing without the user's word.
5. Check afterwards: no accent mark after a virāma, no doubled digit with accents, no dotted circle; look at 20 replaced verses yourself.

## Not in this session
Re-translation; changing the layout or the page headings; the Kannada book (it needs the supplied machine-read text of Vol 2, which the user will upload to `vol2/html/`; if it is there, say so and stop for instructions); PDFs; reading scans (only if a single place cannot be settled otherwise, and then say which page).

## At the end
`vol2/STATUS.md` updated (what was removed by kind, what remains, the accent counts); `PUBLICATION_TODO.md` updated: Vol 2's column in §1 and steps 3.4 and 1.4, "Last updated", a line in the change log; `docs/LESSONS.md` extended if something recurred. Commit, push, and report in a few lines: counts before and after for each kind, how each was checked, what is left for the user.

## Stop and ask when
A kind of remark cannot be told apart from the commentary's own words by its form; the verse count does not equal the reference; a removal would change what the translation says; the usage limit is near (commit and push first; the next session resumes from `vol2/review/repair_log.md`).
