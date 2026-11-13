# To do — open points that are parked on purpose

*One list at the root, so that nothing parked is forgotten. Each point says what is done for now and what remains. Add to it; do not let it grow stale: strike a point when it is settled and say where.*

## Text

1. **Verse differences between the reference and the Kannada edition** (user, Nov 13 2026).
   *Done:* the user checked the differences word by word and found that the Pada-pāṭha or the word meanings often have the right form. The script now settles those itself: where they have the reference form, the supplied verse is taken as misread and gets no footnote. Vol 17: 393 differing places — 136 settled this way, 257 still carry a footnote (83 where the Pada-pāṭha or word meanings agree with the supplied verse, 174 that they do not settle).
   *Remains:* the 257 footnoted places of Vol 17 (`vol17/review/source_faults.tsv`, column "decision"; the 136 settled places are not in that list, only in the record `vol17/review/verse_misreadings_settled.tsv`): real readings of the 1952 edition, or misreadings the machine text repeats? Only the printed book decides. The same list will come for every volume.
2. **Spelling of the printed verse.** The reference writes इन्द्र and final म् where the edition writes इंद्र and ं, so the verse differs in spelling from the Pada-pāṭha and bhāṣya under it. *For now:* the reference as it stands. *Remains:* the user's decision whether to adapt it to the edition's habit.
3. **Other disagreements between the verse and the Pada-pāṭha, word meanings or bhāṣya** (requirement F1, second half). *For now:* listed only. *Remains:* decide whether any are printed.
4. **Questions for the editor.** Vol 17: 471 open (`vol17/review/notes.tsv`); a published book may carry none.
5. **Faults found by the new structure step in Vol 17's English** (`vol17/review/import_report.md`): word meanings of 4.17.7 missing; seven parts with no label in the Kannada file. To be repaired when Vol 17 is taken to a release candidate.
6. **Abbreviations not in the one list**, and suspected misreadings such as "Bhā. U." (`vol17/review/references_report.md`, `docs/REFERENCES.md` part 3): the editor decides; nothing is corrected until then.
7. **Vol 16:** about 70 places with broken punctuation left by the removal of "as supplied" comments on Nov 12 2026. Repair, or undo that step.

## Book

8. **Layout of the pages before the preface** (user, Nov 13 2026: "it may change again later").
   *For now:* the order of requirement A2 as built in `rv/printer.py` (`front_matter`): cover, king, guru, board of scholars, present day, translation credentials, copyright and thanks, contents.
   *Remains:* the final layout and wording; the pictures and texts only the user can supply (present king and guru, credentials picture, publisher, ISBN, thanks, the user's preface); checking the typeset portrait captions against Vol 1 pp. 4–5.
9. **Length.** Volumes are not split for now; several exceed what print-on-demand printers accept (Vol 17 English review copy: about 1,780 pages). Returns when a printer and page size are chosen.
10. ~~The print's ornament line ("— : 0 : —")~~ **Settled Nov 13 2026 (user: "strays — remove"):** stray lines, the ornament line among them, are removed from both books and stay listed in `volN/review/source_faults.tsv`.
11. **Heading of the edition's English:** "English translation", no name, until it is verified whether the text is H. H. Wilson's or adapted from it.

## Before anything is published

12. **Rights** (requirement H1): the Kannada edition; the reference text of the verses ("personal study only"); portraits and cover; the statement of how the translation was made.
13. **A scholar's sample** of every volume; the release standard of requirement H2.

## Building (design, `docs/DESIGN.md` §12)

14. Opus as second reader: measure on the 72 pages of `vol12/review/reader_test/`.
15. Steps B, D, E, F, G of the design: translation in the new form, editor's decisions and the release gate, the older volumes, the scan-based volumes (need the user's machine-read text for Vols 1–4, 6–10, 13), tidy-up (`OPERATING.md`, short `CLAUDE.md`).
16. Move the review PDFs that still sit in `publish/out/` to their volume folders; `publish/out/` is for final copies only.
17. Branch `claude/dreamy-cerf-z4h3f4`: kept unmerged; consult when the printer takes over all volumes, then delete.
