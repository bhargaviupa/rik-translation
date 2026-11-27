
- **Nov 17 2026, glosses of quoted passages replaced by the marker `**GLOSS**`** (user: glosses are to come from our own edition, requirement B3.5): 143 labelled glosses in exact forms replaced whole by `tools/rv/gloss_marker.py 8 --write`; every removed gloss is kept in `review/glosses_removed.tsv` (line, form, text); 88 labelled lines in other forms left unchanged and listed in `review/glosses_left.tsv`. Checked: 682 changes of all volumes listed before writing, 30 read before and after, none damaged; marker count equals removed rows.
- 2026-11-18: tools/rv/refs_apply.py: reference names made uniform by the one list (rv/references.tsv), numbers untouched: en deva 120, en latin 367, en latin-twin 79; every change is a row of review/refs_applied.tsv.
- 2026-11-18: numeral_apply_different.py --min-ctx=0.8 --min-score=0.85 (alignment of Nov 18): nothing applied; of 18 rows of equal part count, distance < 4 and context >= 0.8 I read all 18: 12 paired Ṛ. Saṃ. or Bṛ. De. references of different sūktas (e.g. 4-4-4 vs file 2-7-2), only 2 reached score 0.85, and their tokens ('3-112, 11') are not whole tokens the script can replace; log numerals/numeral_apply_different_Nov18.applied.tsv.
- 2026-11-18: list for the user, nothing applied: numerals/Vol8_for_user_Nov18.tsv (226 DIFFERENT file rows not applied with the reason, 101 md numerals still [?] with no aligned file row and the closest unmatched file rows; 508 NOT FOUND file rows are only in the sheet 'file rows vs md' of Vol8_file_vs_md_Nov18.xlsx).

- **Nov 18 2026, labelled glosses in further forms replaced by the marker `**GLOSS**`** (gloss session, `docs/GLOSS_PROMPT.md` step 1): 61 by `tools/rv/gloss_marker.py 8 --write` after the forms left over on Nov 17 were added to the shared script (label and quotation inside a longer remark or after a dash, numbered lists, glosses in single quotation marks, `(Mine, tentative.)` after the quotation); 10 more in single odd forms by a hand list through `gloss_marker.py --list` (exact text, found once in its line); every removed gloss is in `review/glosses_removed.tsv`. 22 labelled lines left in `review/glosses_left.tsv`: remarks (not glosses), our translations of the bhāṣya's introduction, and glosses whose label stands after a longer quoted passage (a reading is needed). Checked: all 243 script changes of Vols 3–8 read before writing (removed text with the text before and after it), the results re-read at 45 places; by script on every changed line: markers added = log rows, Devanagari and Kannada letters unchanged, brackets, quotation marks and italics balanced, no empty brackets, no space before a stop. Damaged: 0 (four faults of the new forms were found in the dry runs and corrected before the final write).

### 2026-11-27 second pass, batch e550-559.tsv
| page | old → new | why |
|---|---|---|
| 550 | `6-2-1 as read [?].` → `6-2-1.` | SECOND-PASS Q2: Kannada p. 550 reads ೬-೨-೧ (agrees) |
| 550 | `Uṇ. 1-[?]2 as read [?];` → `Uṇ. 1-57;` | SECOND-PASS Q1: Kannada p. 550 reads ಉ. ಸೂ. ೧-೫೭ |
| 550 | `6-4-12 as read [?],` → `6-4-12,` | SECOND-PASS Q2: Kannada p. 550 reads ೬-೪-೧೨ (agrees) |
| 550 | `## Rik 106.5 — printed pp. 550–[?]` → `## Rik 106.5 — printed pp. 550–554` | SECOND-PASS Q1: Kannada p. 554 ends Rik 5 with ॥ ೫ ॥; p. 555 begins Rik 6 |
| 551 | `ni. 4-2[?] |` → `ni. 4-21 |` | SECOND-PASS Q1: Kannada p. 551 reads ನಿ ೪-೨೧ |
| 552 | `1-8[?]-1 as read [?])` → `1-89-1)` | SECOND-PASS Q1: Kannada p. 552 reads ಋ. ಸಂ. ೧-೮೯-೧ |
| 552 | `(*Ni.* 4-19 as read [?])` → `(*Ni.* 4-19 as read)` | SECOND-PASS Q2: Kannada p. 552 reads ನಿ. ೪-೧೯ (agrees) |
| 552 | `1-102-4 as read [?])` → `1-102-4 as read)` | SECOND-PASS Q2: Kannada p. 552 reads ೧-೧೦೨-೪ (agrees) |
| 552 | `*Bṛ. De.* 3-65 as read [?])` → `*Bṛ. De.* 7-65)` | SECOND-PASS Q1: Kannada p. 552 reads ಬೃ. ದೇ. ೭-೬೫ |
| 552 | `*Ṛ. Saṃ.* 1-436 as read)` → `*Ṛ. Saṃ.* 1-43,6)` | SECOND-PASS S1: Kannada p. 552 reads ಋ. ಸಂ. ೧-೪೩,೬ (English had 1-436) |
| 553 | `Ṛks 9-[?]3-10, 10-[?]-3 and others` → `Ṛks 8-93-10, 10-86-5 and others` | SECOND-PASS Q1: Kannada p. 553 reads ೮-೯೩-೧೦, ೧೦-೮೬-೫ |
| 553 | `2-23-7-[?] as read [?])` → `2-23-7)` | SECOND-PASS Q1: Kannada p. 553 reads ಋ. ಸಂ. ೨-೨೩-೭ |
| 553 | `7-1[?]-2 as read [?])` → `7-104-7)` | SECOND-PASS Q1: Kannada p. 553 reads ಋ. ಸಂ. ೭-೧೦೪-೭ |
| 553 | ` (*Ni.* 3-[?]0); *yoḥ*` → ` *yoḥ*` | SECOND-PASS S2: Kannada p. 553 reads only (ನಿ. ೫-೨೧) after ಶಂ ಎಂದರೆ ಸುಖಂ ಯುಃ; no Ni. reference after the word for happiness, so the English number is removed |
| 553 | `*Ni.* 5-21 as read [?])` → `*Ni.* 5-21 as read)` | SECOND-PASS Q2: Kannada p. 553 reads ನಿ. ೫-೨೧ (agrees) |
| 553 | `son of Bṛhaspati [?] [the Kannada` → `son of Bṛhaspati [the Kannada` | SECOND-PASS Q2: Kannada p. 553 reads ಬೃಹಸ್ಪತಿ ಪುತ್ರನಾದ ಶಂಯು (agrees) |
| 553 | `1-4[?]-3 [as read [?]]` → `1-93-7` | SECOND-PASS Q1: Kannada p. 553 reads ೧-೯೩-೭ |
| 553 | `*Tai. Saṃ.* 2-6-10-2 as read [?])` → `*Tai. Saṃ.* 2-6-10-2 as read)` | SECOND-PASS Q2: Kannada p. 553 reads ಶೈ. ಸಂ. ೨-೬-೧೦-೨ (agrees) |
| 553 | `1-8-1-[?]4 as read [?]; the words as read, "asīyāya" doubtful [?])` → `1-9-1-24)` | SECOND-PASS Q1: Kannada p. 553 reads ಶ. ಬದ್ರ. ೧-೯-೧-೨೪ and ದೇವಲೋಕಮಪೀಯಾಯ |
| 553 | `देवलोकमसीयाय` → `देवलोकमपीयाय` | SECOND-PASS Q1: Kannada p. 553 reads ದೇವಲೋಕಮಪೀಯಾಯ (ಸೀ→ಪೀ: devalokamapīyāya) |
| 553 | `devalokam asīyāya` → `devalokam apīyāya` | SECOND-PASS Q1: Kannada p. 553 reads ದೇವಲೋಕಮಪೀಯಾಯ (devalokamapīyāya) |
| 554 | `1-9-1-[?]4, 3[?] as read [?];` → `1-9-1-25;` | SECOND-PASS Q1: Kannada p. 554 reads ಶ. ಬ್ರಾ. ೧-೯-೧-೨೫ |
| 554 | `6-1-157 as read [?]:` → `6-1-157 as read:` | SECOND-PASS Q2: Kannada p. 554 reads ೬-೧-೧೫೭ (agrees) |
| 554 | `6-1-198 as read [?])` → `6-1-198 as read)` | SECOND-PASS Q2: Kannada p. 554 reads ೬-೧-೧೯೮ (agrees) |
| 554 | `6-4-102 as read [?];` → `6-4-102 as read;` | SECOND-PASS Q2: Kannada p. 554 reads ೬-೪-೧೦೨ (agrees) |
| 554 | `*Ni.* 4-21 as read [?]:` → `*Ni.* 4-21 as read:` | SECOND-PASS Q2: Kannada p. 554 reads ನಿರು. ೪-೨೧ (agrees) |
| 554 | `6-1-197 as read [?]:` → `6-1-197 as read:` | SECOND-PASS Q2: Kannada p. 554 reads ೬-೧-೧೯೭ (agrees) |
| 554 | `6-2-48 as read [?]:` → `6-2-48 as read:` | SECOND-PASS Q2: Kannada p. 554 reads ೬-೨-೪೮ (agrees) |
| 555 | `## Rik 106.6 — printed pp. 555–[?]` → `## Rik 106.6 — printed pp. 555–557` | SECOND-PASS Q1: Kannada p. 557 ends Rik 6 with ॥ ೬ ॥ |
| 556 | `(*Ni.* 3-[?]9 as read [?])` → `(*Ni.* 3-19)` | SECOND-PASS Q1: Kannada p. 556 reads ನಿ. ೩-೧೯ |
| 556 | `deep well' [?].` → `narrow well'.` | SECOND-PASS S14: Kannada p. 556 reads ಇಕ್ಕಟ್ಟಾದ ಬಾವಿಯಲ್ಲಿ (a cramped/narrow well) |
| 557 | `(*Ni.* 1-[?]1 [print: 2-[?]1])` → `(*Ni.* 2-23)` | SECOND-PASS Q1: Kannada p. 557 reads ನಿ. ೨-೨೩ |
| 557 | `(*Ni.* 3-19)` → `(*Ni.* 3-1)` | SECOND-PASS S1: Kannada p. 557 reads ನಿ ೩.೧ as printed |
| 557 | `(*Ni.* 3-[?]9 [?])` → `(*Ni.* 3-13)` | SECOND-PASS Q1: Kannada p. 557 reads ನಿ. ೩-೧೩ |
| 557 | `3-2-87 as read [?];` → `3-2-87 as read;` | SECOND-PASS Q2: Kannada p. 557 reads ೩-೨-೮೭ (agrees) |
| 557 | `6-4-15 as read [?],` → `6-4-12,` | SECOND-PASS Q1: Kannada p. 557 reads ೬-೪-೧೨ (followed by a stray !) |
| 557 | `*ubhe vanaspatyādiṣu*, Pā. Sū. 6-2-140 as read [?];` → `*ubhe vanaspatyādiṣu*;` | SECOND-PASS S2: Kannada p. 557 gives no sūtra number there; number removed |
| 557 | `3-2-102 as read [?];` → `3-2-102 as read;` | SECOND-PASS Q2: Kannada p. 557 reads ೩-೨-೧೦೨ (agrees) |
| 557 | `8-2-31 as read [?];` → `8-2-31 as read;` | SECOND-PASS Q2: Kannada p. 557 reads ೮-೨-೩೧ (agrees) |
| 557 | `8-2-40 as read [?];` → `8-2-40 as read;` | SECOND-PASS Q2: Kannada p. 557 reads ೮-೨-೪೦ (agrees) |
| 557 | `*ḍho ḍhe lopaḥ*, Pā. Sū. 8-3-13 as read [?];` → `*ḍho ḍhe lopaḥ*;` | SECOND-PASS S2: Kannada p. 557 gives no sūtra number there; number removed |
| 557 | `6-2-18 as read [?]]` → `7-2-18]` | SECOND-PASS Q1: Kannada p. 557 reads ೭-೨-೧೮ |
| 557 | `6-2-49 as read [?]).` → `6-2-49 as read).` | SECOND-PASS Q2: Kannada p. 557 reads ೬-೨-೪೯ (agrees) |
| 557 | `[print: *cler luṅi*], Pā. Sū. 3-1-44 as read [?];` → `[print: *cler luṅi*];` | SECOND-PASS S2: Kannada p. 557 gives no sūtra number there; number removed |
| 557 | `3-1-53 as read [?];` → `3-1-53 as read;` | SECOND-PASS Q2: Kannada p. 557 reads ೩-೧-೫೩ (agrees) |
| 557 | `6-1-45 as read [?];` → `6-1-45 as read;` | SECOND-PASS Q2: Kannada p. 557 reads ೬-೧-೪೫ (agrees) |
| 557 | `6-4-64 as read [?];` → `6-4-64 as read;` | SECOND-PASS Q2: Kannada p. 557 reads ೬-೪-೬೪ (agrees) |
| 559 | `(*Ni.* 4-22 as read [?])` → `(*Ni.* 4-22 as read)` | SECOND-PASS Q2: Kannada p. 559 reads ನಿ. ೪-೨೨ (agrees) |
| 559 | `caste [?] and the Niṣādas` → `caste and the Niṣādas` | SECOND-PASS Q2: Kannada p. 559 reads ವರ್ಣಾತ್ಮಕವಾದ ಮತ್ತು ನಿಷಾದರಿಂದ ಕೂಡಿದ ಐದು ಜಾತಿಯ ಜನರೂ (agrees) |

### 2026-11-27 second pass, batch e550-559_2.tsv
| page | old → new | why |
|---|---|---|
| 550 | `*ṭita ātmanepadānāṃ ṭere*, Pā. Sū. 3-4-79 as read [?];` → `*ṭita ātmanepadānāṃ ṭere*;` | SECOND-PASS S2: Kannada p. 550 gives no sūtra number after ಟಿತ ಆತ್ಮನೇ—; number removed |
