
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

### 2026-11-27 second pass, batch e2-31.tsv
| page | old → new | why |
|---|---|---|
| 2 | `by the rule beginning 'tu hi' [?] the` → `by the rule beginning 'tu hi' the` | SECOND-PASS Q2: Kannada p. 2 reads the same (tuhyādi) |
| 4 | `शतोरेता वत्सौ` → `तयोरेतौ वत्सौ` | SECOND-PASS Q1: Kannada p. 4 reads ತಯೋರೇತೌ ವತ್ಸೌ; letters copied from the Kannada |
| 4 | `अह्नोऽरुणः [?] ।` → `अह्नोऽग्निः ।` | SECOND-PASS Q1: Kannada p. 4 reads tayoretau vatsau ... ahno agnih (ತಯೋರೇತೌ ವತ್ಸೌ ... ಅಹ್ನೋಽಗ್ನಿಃ); letters copied from the Kannada |
| 4 | `śatoretā vatsau` → `tayor etau vatsau` | SECOND-PASS Q1: twin of the Devanagari line; Kannada p. 4 reads tayor etau vatsau |
| 4 | `ahno 'ruṇaḥ [?] |` → `ahno 'gniḥ |` | SECOND-PASS Q1: twin of the Devanagari line; Kannada p. 4 reads tayor etau vatsau ... ahno agnih |
| 4 | `the two calves of the hundred-fold seed [?], Agni` → `of those two these are the calves, Agni` | SECOND-PASS Q1: Kannada p. 4 reads tayor etau vatsau; p. 7 the same |
| 4 | `[the calf] of the day is red [?]; the coppery` → `[the calf] of the day is Agni; the coppery` | SECOND-PASS Q1: Kannada p. 4 reads ahno agnih, tamro aruna iti; p. 7 the same |
| 4 | `(the rule on '*ekānnābhyāṃ samarthābhyām*' [?], Pā. Sū. 8-1-65)` → `(the rule on '*ekānyābhyāṃ samarthābhyām*', Pā. Sū. 8-1-65)` | SECOND-PASS Q1: Kannada pp. 4 and 9 read ಏಕಾನ್ಯಾಭ್ಯಾಂ ಸಮರ್ಥಾಭ್ಯಾಂ, Pā. 8-1-65 |
| 5 | `the *nighāta* [accent is blocked? — the sentence is clotted in the print [?]].` → `the prohibition of *nighāta*.` | SECOND-PASS Q1: Kannada pp. 4-5 reads ನಿಘಾತಪ್ರತಿಷೇಧಃ (nighatapratisedhah) |
| 5 | `3-129 as read [?])` → `3-129 as read)` | SECOND-PASS Q2: Kannada p. 5 reads ಬೃ. ದೇ. ೩-೧೨೯ |
| 7 | `[as read [?]], that in the singular` → `[as read], that in the singular` | SECOND-PASS Q2: Kannada p. 7 reads ವತ್ಸಸ್ಥಾನೀಯಮಗ್ನಿಂ; only its annonyasya is a misprint of anyonyasya |
| 8 | `(Paribhāṣā 115 [?])` → `(Paribhāṣā 115)` | SECOND-PASS Q2: Kannada p. 8 reads (ಪರಿ-೧೧೫) |
| 12 | `1-70-2 as read [?]; the print has *asāṃ* for *apāṃ* [?])` → `1-70-2 as read; the print has *asāṃ* for *apāṃ*)` | SECOND-PASS Q2: Kannada p. 12 reads ಋ. ಸಂ. ೧-೭೦-೨ and ಅಸಾಂ (misprint; p. 21 has apam) |
| 14 | `तस्मिन्नृप्त्यति [?] प्रवर्धमाने` → `तस्मिन्नतृप्यति प्रवर्धमाने` | SECOND-PASS Q1: Kannada p. 14 reads ತಸ್ಮಿನ್ನತೃಪ್ಯತಿ ಪ್ರವರ್ಧಮಾನೇ; letters from the Kannada |
| 14 | `tasmin nṛptyati [?] pravardhamāne` → `tasminn atṛpyati pravardhamāne` | SECOND-PASS Q1: twin of the Devanagari line; Kannada p. 14 reads tasminn atrpyati |
| 14 | `Since materials for Agni's nourishment were also lacking [?], when he shone` → `Even though materials for Agni's nourishment were lacking, when he shone` | SECOND-PASS Q1: Kannada p. 14: ಅಗ್ನಿಯ ಪೋಷಕ ಸಾಮಗ್ರಿಗಳಿಲ್ಲದೆಯೂ ಸಹ ಆಕಾಶದಲ್ಲಿ ಬೆಳಗುತ್ತಿದ್ದಾಗ |
| 14 | `*hetumati ca* (Pā. Sū. 3-1-26 [?]) as` → `*hetumati ca* as` | SECOND-PASS S2: Kannada p. 14 gives no sutra number here; a number the print has not is removed |
| 14 | `*ata upadhāyāḥ* (Pā. Sū. 7-2-116 [?]);` → `*ata upadhāyāḥ*;` | SECOND-PASS S2: Kannada p. 14 gives no sutra number here; a number the print has not is removed |
| 14 | `*bahulaṃ chandasy amāṅyoge 'pi* (Pā. Sū. 6-4-75 [?]);` → `*bahulaṃ chandasy amāṅyoge 'pi*;` | SECOND-PASS S2: Kannada p. 14 gives no sutra number here; a number the print has not is removed |
| 15 | `*ktra* in the passive by the Uṇādi sūtra (Pā./U. Sū. 4-2-[?] [?])` → `*kta* in the passive by *niṣṭhā* (Pā. Sū. 3-2-102)` | SECOND-PASS Q1: Kannada p. 15: ಕರ್ಮಣಿಯಲ್ಲಿ ನಿಷ್ಠಾ (ಪಾ ಸೂ. ೩-೨-೧೦೨) ಎಂಬುದರಿಂದ ಕ್ತಪ್ರತ್ಯಯ |
| 16 | `परीत्येष [?] समित्येतस्य` → `परीत्येष समित्येतस्य` | SECOND-PASS Q2: Kannada p. 16 reads ಪರೀತ್ಯೇಷ ಸಮಿತ್ಯೇತಸ್ಯ |
| 16 | `parīty eṣa [?] samity etasya` → `parīty eṣa samity etasya` | SECOND-PASS Q2: Kannada p. 16 reads parityesa samityetasya |
| 16 | `*pari* in place of *sam* [as read [?]]` → `*pari* in place of *sam* [as read]` | SECOND-PASS Q2: Kannada p. 16 reads ಪರೀತ್ಯೇಷ ಸಮಿತ್ಯೇತಸ್ಯ ಸ್ಥಾನೇ |
| 16 | `an irregular suffix (*phiñ*? [as read, doubtful [?]])` → `the suffix *ghañ*` | SECOND-PASS Q1: Kannada p. 16: ಜನೀ ಪ್ರಾದುರ್ಭಾವೇ । ಘಞ್ (ghan) |
| 18 | `1-65 to 1-67 as read [?])` → `1-65 to 1-67 as read)` | SECOND-PASS Q2: Kannada p. 18 reads ಬೃ. ದೇ. ೧-೬೫ ರಿಂದ ೬೭ |
| 19 | `[as read [?]])` → `[as read])` | SECOND-PASS Q2: Kannada p. 19 reads ನಿ. ೭-೧೪ ರಿಂದ ೭-೨೫ |
| 19 | `an *ñit*-suffix (the print gives *phiñ* [?])` → `an *ñit*-suffix (*ghañ*)` | SECOND-PASS Q1: Kannada p. 19: ಜನೀ ಪ್ರಾದುರ್ಭಾವೇ ಧಾತು. ಇದಕ್ಕೆ ಘಞ್ ಪ್ರತ್ಯಯ |
| 19 | `*jaśśasoḥ śiḥ* (Pā. Sū. 7-1-20 [?])` → `*jaśśasoḥ śiḥ*` | SECOND-PASS S2: Kannada p. 19 gives no sutra number here; a number the print has not is removed |
| 20 | `*prasanadyāpo 'nuṭ* [?] and` → `*hrasvanadyāpo nuṭ* and` | SECOND-PASS Q1: Kannada p. 20 reads ಹ್ರಸ್ವನದ್ಯಾಪೋನುಟ್ (hrasvanadyapo nut) |
| 20 | `*adiprabhṛtibhyaḥ śapaḥ* (Pā. Sū. 2-4-72 [?])` → `*adiprabhṛtibhyaḥ śapaḥ*` | SECOND-PASS S2: Kannada p. 20 gives no sutra number here; a number the print has not is removed |
| 22 | `(Dhā. 19-63-67 [?])` → `(Dhā. 19-63-67)` | SECOND-PASS Q2: Kannada p. 22 reads ಧಾ. ೧೯-೬೩-೬೭ |
| 23 | `*niṇyaṃ, sasṭaḥ* [as read [?]], *sanutaḥ*` → `*niṇyaṃ, sasvaḥ*, *sanutaḥ*` | SECOND-PASS Q1: Kannada p. 23 reads ನಿಣ್ಯಂ, ಸಸ್ವಃ, ಸನುತಃ (Ni. 3-19) |
| 28 | `प्रत्येक्ते सिंहं सहनं प्रत्यासेनेते [?]` → `प्रत्यक्ते सिंहं सहनं प्रत्यासेवेते` | SECOND-PASS Q1: Kannada p. 28 reads ಪ್ರತ್ಯಕ್ತೇ ಸಿಂಹಂ ಸಹನಂ ಪ್ರತ್ಯಾಸೇವೇತೇ; p. 30 the same; letters from the Kannada |
| 28 | `pratyekte siṃhaṃ sahanaṃ pratyāsenete [?]` → `pratyakte siṃhaṃ sahanaṃ pratyāsevete` | SECOND-PASS Q1: twin of the Devanagari line; Kannada p. 28 reads pratyakte ... pratyasevete |
| 28 | `प्रस्नात्तादौ रेद्धते [?]` → `ह्रस्वात्तादौ तद्धिते` | SECOND-PASS Q1: Kannada p. 28 reads ಹ್ರಸ್ವಾತ್ತಾದೌ ತದ್ಧಿತೇ । ಪಾ ೮-೩-೧೦೧; letters from the Kannada |
| 28 | `prasnāttādau reddhate [?]` → `hrasvāt tādau taddhite` | SECOND-PASS Q1: twin of the Devanagari line; Kannada p. 28 reads hrasvattadau taddhite |
| 29 | `पशुवत्तिर्यक्षीनानां [?] आबूपमात्र्येणामुदरे च तिर्यगीनो` → `पशुवत्तिरश्चीनानां अब्रूपमातृणामुदरे च तिरश्चिनो` | SECOND-PASS Q1: Kannada p. 29 reads ಪಶುವತ್ತಿರಶ್ಚೀನಾನಾಂ ಅಬ್ರೂಪಮಾತೃಣಾಮುದರೇ ಚ ತಿರಶ್ಚಿನೋ (gloss: ಜಲರೂಪವಾದ ಮಾತೃಗಳ ಉದರದಲ್ಲಿ) |
| 29 | `paśuvat tiryakṣīnānām [?] ābūpamātryeṇāmudare ca tiryagīno` → `paśuvat tiraścīnānām abrūpamātṛṇām udare ca tiraścino` | SECOND-PASS Q1: twin of the Devanagari line; Kannada p. 29 reads tiraścinanam abrupamatrnamudare ca tiraścino |
| 30 | `प्रत्यक्ते [?] सिंहं` → `प्रत्यक्ते सिंहं` | SECOND-PASS Q2: Kannada p. 30 reads ಪ್ರತ್ಯಕ್ತೇ ಸಿಂಹಂ |
| 30 | `pratyakte [?] siṃhaṃ` → `pratyakte siṃhaṃ` | SECOND-PASS Q2: Kannada p. 30 reads pratyakte simham |

### 2026-11-27 second pass, batch e32-61.tsv
| page | old → new | why |
|---|---|---|
| 33 | `स्वकीयैश्च [?] वत्सैरादरातिशयेन [?]` → `स्वकीयैश्चरित्रैरादरातिशयेन` | SECOND-PASS Q1: Kannada p. 33 reads स्वकीयैश्चरित्रैरादरातिशयेन (letters changed: वत्सै→चरित्रै) |
| 33 | `svakīyaiś ca [?] vatsair ādarātiśayena [?]` → `svakīyaiś caritrair ādarātiśayena` | SECOND-PASS Q1: Kannada p. 33 reads svakīyaiś caritrair ādarātiśayena (IAST twin of the Devanagari edit) |
| 40 | `यजमाननामैतत् [?] शाकपूणिना` → `यजमाननामैतच्छाकपूणिना` | SECOND-PASS Q1: Kannada p. 40 reads yajamānanāmaitac chākapūṇinā; sandhi joined |
| 40 | `yajamānanāmaitat [?] śākapūṇinā` → `yajamānanāmaitac chākapūṇinā` | SECOND-PASS Q1: Kannada p. 40 reads yajamānanāmaitac chākapūṇinā (IAST twin) |
| 40 | `उभे असि वस्त्राञ्चले गाढं सन्नह्यति [?]` → `उभे अपि वस्त्राञ्चले गाढं सन्नहति` | SECOND-PASS Q1: Kannada p. 40 reads ubhe api vastrāñcale gāḍhaṃ sannahati |
| 40 | `ubhe asi vastrāñcale gāḍhaṃ sannahyati [?]` → `ubhe api vastrāñcale gāḍhaṃ sannahati` | SECOND-PASS Q1: Kannada p. 40 reads ubhe api vastrāñcale gāḍhaṃ sannahati (IAST twin) |
| 41 | `añjatir api …artha [?] |` → `añjatir api kṣepaṇārthaḥ |` | SECOND-PASS Q1: Kannada p. 41 reads añjatir api kṣepaṇārthaḥ |
| 41 | `स्तरीर्नात्कं वृतं [?] वसाना` → `स्तरीर्नात्कं व्युतं वसाना` | SECOND-PASS Q1: Kannada p. 41 reads starīr nātkaṃ vyutaṃ vasānā (वृतं→व्युतं) |
| 41 | `starīr nātkaṃ vṛtaṃ [?] vasānā` → `starīr nātkaṃ vyutaṃ vasānā` | SECOND-PASS Q1: Kannada p. 41 reads vyutaṃ (IAST twin) |
| 46 | `गोभिर्यदीमन्ये अस्मन्नृगं न व्रा न्यगयन्ते [?]` → `गोभिर्यदी मन्ये अस्मन्मृगं न व्रा मृगयन्ते` | SECOND-PASS Q1: Kannada p. 46 reads gobhir yadī manye asmanmṛgaṃ na vrā mṛgayante |
| 46 | `gobhir yad īm anye asmann ṛgaṃ na vrā ny agayante [?]` → `gobhir yadī manye asmanmṛgaṃ na vrā mṛgayante` | SECOND-PASS Q1: Kannada p. 46 reading (IAST twin) |
| 49 | `स्वकीयैरात्मीयैस्ते [?] तेजोभिरस्मान्पाहि` → `स्वकीयैरात्मीयैस्तेजोभिरस्मान्पाहि` | SECOND-PASS Q1: Kannada p. 49 reads svakīyair ātmīyais tejobhir asmān pāhi, without te |
| 49 | `svakīyair ātmīyais te [?] tejobhir asmān pāhi` → `svakīyair ātmīyaistejobhir asmān pāhi` | SECOND-PASS Q1: Kannada p. 49 reading (IAST twin) |
| 51 | `(Ni. 3-9 [?])` → `(Ni. 3-9)` | SECOND-PASS Q2: Kannada p. 51 reads ನಿ. ೩-೯ |
| 57 | `is retained (Pā. Sū. 6-2-139 [?]);` → `is retained;` | SECOND-PASS S2: Kannada p. 57 gives no sūtra number after gatikārakopapadāt kṛt; number removed |
| 61 | `Jātavedas [?]; it is laid down` → `Jātavedas; it is laid down` | SECOND-PASS Q2: Kannada p. 61 anuvāda: nivid mantra of Agni Jātaveda, agrees |

### 2026-11-27 second pass, batch e62-91.tsv
| page | old → new | why |
|---|---|---|
| 66 | `2-7-6 as read [?])` → `2-7-6 as read)` | SECOND-PASS Q2: Kannada p. 66 reads 2-7-6 |
| 66 | `8-75-6 as read [?]` → `8-25-3 as read` | SECOND-PASS Q1: Kannada p. 66 reads ೮-೨೫-೩ (8-25-3) |
| 67 | `2-24 as read [?]` → `2-24 as read` | SECOND-PASS Q2: Kannada p. 67 reads ೨-೨೪ |
| 67 | `2-25 as read [?]` → `2-25 as read` | SECOND-PASS Q2: Kannada p. 67 reads ೨-೨೫ |
| 67 | `3-61; 4-62 as read [?]` → `3-61; 3-65 as read` | SECOND-PASS Q1: Kannada p. 67 reads ೩-೬೧ ; ೩-೬೫ |
| 68 | `2-7-6 as read [?])` → `2-7-6 as read)` | SECOND-PASS Q2: Kannada p. 68 reads ೨-೭-೬ |
| 69 | `Varga 3 [?]"` → `Varga 3"` | SECOND-PASS Q2: Kannada p. 69 head reads ವ. ೩ |
| 69 | `sixty-[?] names` → `fifty-seven names` | SECOND-PASS Q1: Kannada p. 69 reads ಐವತ್ತೇಳು (fifty-seven) |
| 70 | `10-52-3 as read [?]` → `10-52-3 as read` | SECOND-PASS Q2: Kannada p. 70 reads ೧೦-೫೨-೩ |
| 70 | `(Pā. Sū. 3-328-[?] [?])` → `(Pā. Sū. 3-328)` | SECOND-PASS Q1: Kannada p. 70 reads ಪಾ. ೩-೩೨೮ |
| 76 | `tās pūrvayā nividā hūmahe vayaṃ bhagaṃ mitram aditiṃ dakṣam asridham | [the first word as ` → `tān pūrvayā nividā hūmahe vayaṃ bhagaṃ mitram aditiṃ dakṣam asridham |` | SECOND-PASS Q1: Kannada p. 76 reads ತಾನ್ಪೂರ್ವಯಾ (letters changed: tās→tān) |
| 76 | `तास्पूर्वया निविदा` → `तान्पूर्वया निविदा` | SECOND-PASS Q1: Kannada p. 76 reads ತಾನ್ಪೂರ್ವಯಾ (letters changed: तास्→तान्) |
| 78 | `2-14-7 as read [?]` → `2-14-7 as read` | SECOND-PASS Q2: Kannada p. 78 reads ೨-೧೪-೭ |
| 78 | ` [as printed; standard hrasvasya piti kṛti tuk is 6-1-71] [?]` → `` | SECOND-PASS Q1: Kannada p. 78 reads ಸೂ. ೬-೩-೭೧; the Kannada number is taken as printed |
| 80 | `उ. सू. २-८७७ [?]` → `उ. सू. २-८७` | SECOND-PASS Q1: Kannada p. 80 reads ಉ. ೨-೮೭ (digits changed: २-८७७→२-८७) |
| 80 | `u. sū. 2-877 [?]` → `u. sū. 2-87` | SECOND-PASS Q1: Kannada p. 80 reads ಉ. ೨-೮೭ |
| 80 | `U. Sū. 2-877 [?]` → `U. Sū. 2-87` | SECOND-PASS Q1: Kannada p. 80 reads ಉ. ೨-೮೭ |
| 84 | `3-390 as printed [?]` → `3-390 as printed` | SECOND-PASS Q2: Kannada p. 84 reads ೩-೩೯೦ |
| 88 | `*āsādau* [?]` → `*apādādau*` | SECOND-PASS Q1: Kannada p. 88 reads ಅಪಾದಾದೌ (letters changed: āsādau→apādādau) |
| 90 | `‖ 6 [?] ‖` → `‖ 6 ‖` | SECOND-PASS Q2: Kannada p. 90 reads ॥ ೬ ॥ |
| 90 | `अहस्त्रियामे [?] एकं` → `अहस्त्रियामे एकं` | SECOND-PASS Q2: Kannada p. 90 reads ಅಹಸ್ತ್ರಿಯಾಮೇ |
| 90 | `ahastriyāme [?] ekaṃ` → `ahastriyāme ekaṃ` | SECOND-PASS Q2: Kannada p. 90 reads ಅಹಸ್ತ್ರಿಯಾಮೇ |

### 2026-11-27 second pass, batch e92-121.tsv
| page | old → new | why |
|---|---|---|
| 93 | `(Pā. Sū. 6-4-138 [?])` → `(Pā. Sū. 6-4-138)` | SECOND-PASS Q2: Kannada p. 94 reads ೬-೪-೧೩೮ (acaḥ) |
| 93 | `(Pā. Sū. 6-3-138 [?])` → `(Pā. Sū. 6-4-138)` | SECOND-PASS Q1: Kannada p. 94 reads ೬-೪-೧೩೮ for the lengthening ('ಆಚಃ ... ದೀರ್ಘ') |
| 93 | `Pā. Sū. 6-1-106 [?])` → `Pā. Sū. 6-1-106)` | SECOND-PASS Q2: Kannada p. 94 reads ೬-೧-೧೦೬ |
| 96 | `3-55-7 as read [?])` → `3-55-7 as read)` | SECOND-PASS Q2: Kannada p. 96 reads ೩-೫೫-೭ |
| 97 | `1-26-2-[?]; 1-127-2-[?]; 1-140-1` → `1-26-2; 1-127-2; 1-140-1` | SECOND-PASS Q1: Kannada p. 97 reads ೧-೨೬-೨ ; ೧-೧೨೭-೨ ; ೧-೧೪೦-೧ |
| 101 | `Ṛk 1-96-2-[?] of` → `Ṛk 1-96-2 of` | SECOND-PASS Q1: Kannada p. 101 reads ೧-೯೬-೨ |
| 101 | `1-104-2-[?] and` → `1-104-2 and` | SECOND-PASS Q1: Kannada p. 101 reads ೧-೧೦೪-೨ |
| 105 | `2-25 as read [?])` → `2-25 as read)` | SECOND-PASS Q2: Kannada p. 105 reads ೨-೨೫ |
| 105 | `5-86-4 as read [?])` → `5-86-4 as read)` | SECOND-PASS Q2: Kannada p. 105 reads ೫-೮೬-೪ |
| 105 | `6-18-4 as read [?])` → `6-18-4 as read)` | SECOND-PASS Q2: Kannada p. 105 reads ೬-೧೮-೪ |
| 105 | `6-44-5 as read [?])` → `6-44-5 as read)` | SECOND-PASS Q2: Kannada p. 105 reads ೬-೪೪-೫ |
| 106 | `6-5-5 as read [?])` → `6-5-5 as read)` | SECOND-PASS Q2: Kannada p. 106 reads ೬೫೫ (no hyphens printed); same digits |
| 108 | `for the sake of drinking [?] our food` → `for the sake of drinking our food` | SECOND-PASS Q2: Kannada p. 108 reads ಅನ್ನಪಾನಕ್ಕಾಗಿ (for food and drink) |
| 111 | `on the eighth [?] day` → `on the tenth day` | SECOND-PASS Q1: Kannada p. 111 reads ಹತ್ತನೆಯ ದಿವಸ (tenth day) |
| 114 | `(*kaśa*) [the print's word as read [?]]` → `(*kaśa*)` | SECOND-PASS Q2: Kannada p. 114 reads ಕಶೆಗಳಿಂದ, a real word |
| 118 | `(Ṛ. Saṃ. 1-93-4 [?])` → `(Ṛ. Saṃ. 1-96-4)` | SECOND-PASS Q1: Kannada p. 118 reads (೧-೯೬-೪) |
| 118 | `(Pā. Sū. 3-1-0 as printed [?])` → `(Pā. Sū. 3-1-0 as printed)` | SECOND-PASS Q2: Kannada p. 118 prints ೩-೧-೦, applied as printed (listed in open.tsv) |
| 118 | `(Pā. Sū. 7-4-35)` → `(Pā. Sū. 7-4-25)` | SECOND-PASS S2: Kannada p. 118 reads ನಛಂದಸ್ಯಪುತ್ರಸ್ಯ (ಪಾ. ಸೂ. ೭-೪-೨೫) |
| 119 | `दृप्वृक्शब्दके [?] एवाचार्येणातिदिष्कृते` → `दृष्टत्वात्स एवाचार्येणातिश्यते` | SECOND-PASS Q1: Kannada p. 119 reads ದೃಷ್ಟತ್ವಾತ್ಸ ಏವಾಚಾರ್ಯೇಣಾತಿಶ್ಯತೇ; Devanagari from sp_sanskrit |
| 119 | `dṛpvṛkśabdake [?] evācāryeṇātidiṣkṛte` → `dṛṣṭatvātsa evācāryeṇātiśyate` | SECOND-PASS Q1: Kannada p. 119 reads ದೃಷ್ಟತ್ವಾತ್ಸ ಏವಾಚಾರ್ಯೇಣಾತಿಶ್ಯತೇ; IAST from sp_sanskrit |
| 120 | `forty-four [?] names` → `forty-four names` | SECOND-PASS Q2: Kannada p. 120 reads ೪೪ |

### 2026-11-27 second pass, batch e92-121_2.tsv
| page | old → new | why |
|---|---|---|
| 117 | `६-१-१३[?]` → `७-१-३९-१` | SECOND-PASS Q1: Kannada p. 117 reads ಪಾ. ೭-೧-೩೯-೧; digits only |

### 2026-11-27 second pass, batch e122-151.tsv
| page | old → new | why |
|---|---|---|
| 125 | `twenty-eight [?] names` → `twenty-eight names` | SECOND-PASS Q2: Kannada p. 125 reads ೨೮ (28) bala-names (ನಿ. ೩-೯) |
| 126 | `8-102-7 as read [?])` → `8-102-7 as read)` | SECOND-PASS Q2: Kannada p. 126 reads ೮-೧೦೨-೭ |
| 135 | `Varga "6" as read [?]` → `Varga "6" as read` | SECOND-PASS Q2: Kannada p. 135 reads ವರ್ಗ—೬ |
| 137 | `Chāndogya-type sentence, as read [?]]` → `Chāndogya-type sentence, as read]` | SECOND-PASS Q2: Kannada p. 138 cites the Chāndogya (ಛಾ. ಉ. ೫.೨೪-೨) for this sentence |
| 139 | `1-101; 1-102 as read [?])` → `1-101; 1-102 as read)` | SECOND-PASS Q2: Kannada p. 139 reads (ಬೃ. ದೇ. ೧-೧೦೧ ; ೧-೧೦೨) |
| 142 | `a thousand portions of drink [?]` → `thousands of drinks` | SECOND-PASS Q1: Kannada p. 142 reads ಸಹಸ್ರಾರು ಪಾನಗಳನ್ನೂ |
| 143 | `would have been struck down [?] [or: would have slipped]` → `would have become slack and wasted away` | SECOND-PASS Q1: Kannada p. 143 reads ನಿನ್ನ ಪಾದಗಳು ಸಡಿಲವಾಗಿ ಕ್ಷೀಣಿಸಿಬಿಡುತ್ತಿದ್ದವು |
| 143 | `would have burst [?]` → `would have become useless` | SECOND-PASS Q1: Kannada p. 143 reads ನಿನ್ನ ಕೋಶವೂ ಅಪ್ರಯೋಜಕವಾಗುತ್ತಿತ್ತು |
| 146 | `clotted in print [?])` → `clotted in print)` | SECOND-PASS Q2: Kannada p. 146 reads ಋ. ಸಂ. ೧-೧೪೪-೬ and the words ಏನೀ ತ ಏತೇ … ಹಿರಣ್ಯಯೀ |
| 146 | `जात आप्स्यो [?] भुवनानि` → `जात आपृणो भुवनानि` | SECOND-PASS Q1: Kannada p. 146 reads ಜಾತ ಆಪೃಣೋ ಭುವನಾನಿ; Devanagari by sp_sanskrit.py |
| 146 | `jāta āpsyo [?] bhuvanāni` → `jāta āpṛṇo bhuvanāni` | SECOND-PASS Q1: Kannada p. 146 reads ಜಾತ ಆಪೃಣೋ ಭುವನಾನಿ; IAST by sp_sanskrit.py |
| 146 | `*nare saṃjñāyām* [Pā. Sū. 6-3-[?]]` → `*nare saṃjñāyām* [Pā. Sū. 6-3-129]` | SECOND-PASS Q1: Kannada p. 147 reads ೬-೩-೧೨೯ for ನರೇ ಸಂಜ್ಞಾಯಾಂ |
| 146 | `*tādau ca niti* [6-2-[?]]` → `*tādau ca niti* [6-2-50]` | SECOND-PASS Q1: Kannada p. 147 reads ತಾದೌಚನಿತಿ—(ಪಾ. ಸೂ. ೬-೨-೫೦) |
| 146 | `*nañsubhyām* [6-2-[?]]` → `*nañsubhyām* [6-2-172]` | SECOND-PASS Q1: Kannada p. 147 reads ನಞ್ಸುಭ್ಯಾಮ್—(ಪಾ ಸೂ. ೬-೨-೧೭೨) |
| 146 | `*nityaṃ ñitaḥ* [?];` → `*nityaṃ ñitaḥ*;` | SECOND-PASS Q2: Kannada p. 147 reads ನಿತ್ಯಂಜಿತಃ (no number given) |
| 146 | `[Pā. Sū. 3-1-114 as read, ?]` → `[Pā. Sū. 3-1-114]` | SECOND-PASS Q2: Kannada p. 147 reads (ಪಾ. ಸೂ. ೩-೧-೧೧೪) |
| 148 | `printed pp. 148–[?]` → `printed pp. 148–152` | SECOND-PASS Q1: Kannada: Rik 98.2 stands on pp. 148–152; Rik 3 begins on p. 153 |
| 149 | `(*Ā.* 2-[1?]9 as read [?])` → `(*Ā.* 2-15)` | SECOND-PASS Q1: Kannada p. 149 reads (ಆ. ೨-೧೫) |
| 150 | `3-22-2 as read [?])` → `3-22-2 as read)` | SECOND-PASS Q2: Kannada p. 150 reads (ಋ. ಸಂ. ೩-೨೨-೨) |
| 150 | `1-[7?]1-59-3 as read [?]` → `1-59-3` | SECOND-PASS Q1: Kannada p. 150 reads (ಋ. ಸಂ. ೧-೫೯-೩) |
| 150 | `1-67-9?]7-9 as read [?]` → `1-67-9` | SECOND-PASS Q1: Kannada p. 150 reads (ಋ. ಸಂ. ೧-೬೭-೯) |
| 150 | `9-2-1-[8?] as read [?]` → `9-2-1-8` | SECOND-PASS Q1: Kannada p. 150 reads (ಶತಪಥಬ್ರಾಹ್ಮಣ ೯-೨-೧-೮) |
| 151 | `3-9 as read [?])` → `3-9 as read)` | SECOND-PASS Q2: Kannada p. 151 reads (ನಿ. ೩-೯) |
| 151 | `तस्मिन्न्[?]न्ति` → `तस्मिन्त्संति` | SECOND-PASS Q1: Kannada p. 151 reads ತಸ್ಮಿನ್ತ್ಸಂತಿ ಪ್ರಶಿಷಸ್ತಸ್ಮಿನ್ನಿಷ್ಟಯಃ; Devanagari by sp_sanskrit.py |
| 151 | `tasminn [?]nti` → `tasmintsaṃti` | SECOND-PASS Q1: Kannada p. 151 reads ತಸ್ಮಿನ್ತ್ಸಂತಿ; IAST by sp_sanskrit.py |
| 151 | `1-[1?]43-1 as read [?]` → `1-145-1` | SECOND-PASS Q1: Kannada p. 151 reads (ಋ. ಸಂ. ೧-೧೪೫-೧) |
| 151 | `3-1[0?]-2 as read [?]` → `5-10-2` | SECOND-PASS Q1: Kannada p. 151 reads (ಋ. ಸಂ. ೫-೧೦-೨) |
| 151 | `1-[1?]2[2?]-3 as read [?]` → `1-127-3` | SECOND-PASS Q1: Kannada p. 151 reads (ಋ. ಸಂ. ೧-೧೨೭-೩) |
| 151 | `1-145-1?]8 as read [?]` → `8-5-18` | SECOND-PASS Q1: Kannada p. 151 reads (ಶ. ಬತ್ರ. ೮-೫-೧೮) |

### 2026-11-27 second pass, batch e152-181.tsv
| page | old → new | why |
|---|---|---|
| 153 | `धनवदतिप्रियोः [?]` → `धनवदतिप्रियाः` | SECOND-PASS Q1: Kannada p. 153 reads ಧನವದತಿಪ್ರಿಯಾಃ (priyāḥ for priyoḥ) |
| 153 | `dhanavadatipriyoḥ [?]` → `dhanavadatipriyāḥ` | SECOND-PASS Q1: Kannada p. 153 reads ಧನವದತಿಪ್ರಿಯಾಃ |
| 153 | ` [print's wording clotted here [?]]` → `` | SECOND-PASS Q1: Kannada p. 153 reads ಧನವದತಿಪ್ರಿಯಾಃ clearly (and p. 154 glosses it) |
| 154 | `3-13?]2 as read [?]` → `3-13` | SECOND-PASS Q1: Kannada p. 154 reads (ನಿ. ೩-೧೩) |
| 155 | `सत्यमन्वालेभिरे [?]` → `सत्यमन्वालेभिरे` | SECOND-PASS Q2: Kannada p. 155 reads ಸತ್ಯಮನ್ವಾಲೇಭಿರೇ (agrees) |
| 155 | `anvālebhire [?]` → `anvālebhire` | SECOND-PASS Q2: Kannada p. 155 reads ಸತ್ಯಮನ್ವಾಲೇಭಿರೇ (agrees) |
| 155 | `9-5-1-18[3?] as read [?]` → `9-5-1-13` | SECOND-PASS Q1: Kannada p. 155 reads ಶ. ಬ್ರಾ. ೯-೫-೧-೧೩ |
| 155 | `केनवामहा [?]` → `तनवामहा` | SECOND-PASS Q1: Kannada p. 155 reads ತನವಾಮಹಾ ಇತಿ (glossed: let us spread this truth) |
| 155 | `kenavāmahā [?]` → `tanavāmahā` | SECOND-PASS Q1: Kannada p. 155 reads ತನವಾಮಹಾ ಇತಿ |
| 155 | `9-5-1-18[5?] as read [?]` → `9-5-1-18` | SECOND-PASS Q1: Kannada p. 155 reads ಶ. ಬ್ರಾ. ೯-೫-೧-೧೮ |
| 155 | `with this truth what shall we —?' [the end of the sentence, *kenavāmahā*, is doubtful [?]]` → `let us spread this truth (*tanavāmahā*)'` | SECOND-PASS Q1: Kannada p. 155: ಇದಂ ಸತ್ಯಂ ತನವಾಮಹಾ ಇತಿ, glossed ಈ ಸತ್ಯವನ್ನು ಹರಡೋಣ |
| 155 | `1[4?]-3-1-1[8?] as read [?]` → `14-3-1-18` | SECOND-PASS Q1: Kannada p. 155 reads ಶ. ಬ್ರಾ. ೧೪-೩-೧-೧೮ |
| 155 | `7-[7?]7-76-4 as read [?]` → `7-76-4` | SECOND-PASS Q1: Kannada p. 155 reads ಋ. ಸಂ. ೭-೭೬-೪ |
| 155 | `3-[3?]9-[3?] as read [?]` → `3-39-5` | SECOND-PASS Q1: Kannada p. 155 reads ಋ. ಸಂ. ೩-೩೯-೫ |
| 156 | `*dhanavatipriyoḥ* [as printed, doubtful [?]]` → `*dhanavadatipriyāḥ*` | SECOND-PASS Q1: Kannada p. 156 reads ಧನವದತಿಪ್ರಿಯಾಃ |
| 157 | `कश्यपार्षमिति [?]` → `कश्यपार्षमिति` | SECOND-PASS Q2: Kannada p. 157 reads ಕಶ್ಯಪಾರ್ಷಮಿತಿ ॥ (agrees) |
| 157 | `शंसनीया [?]` → `शंसनीया` | SECOND-PASS Q2: Kannada p. 157 reads ಶಂಸನೀಯಾ । (agrees) |
| 157 | `iti [?]` → `iti` | SECOND-PASS Q2: Kannada p. 157 reads ಕಶ್ಯಪಾರ್ಷಮಿತಿ ॥ (agrees) |
| 157 | `śaṃsanīyā [?]` → `śaṃsanīyā` | SECOND-PASS Q2: Kannada p. 157 reads ಶಂಸನೀಯಾ । (agrees) |
| 159 | `गमेर्डः [?]` → `गमेर्डः` | SECOND-PASS Q2: Kannada p. 159 reads ಗಮೇರ್ಡಃ ॥ (agrees) |
| 159 | `ḍaḥ [?]` → `ḍaḥ` | SECOND-PASS Q2: Kannada p. 159 reads ಗಮೇರ್ಡಃ ॥ (agrees) |
| 160 | `*sāhasalaśakya-*, clotted [?]]` → `*sahisalaśakya-*]` | SECOND-PASS Q1: Kannada p. 160 reads ಸಹಿಸಲಶಕ್ಯವಾದ |
| 160 | `7-19 as read [?]` → `7-19` | SECOND-PASS Q2: Kannada p. 160 reads ನಿ. ೭-೧೯ (agrees) |
| 161 | `तथ्येते [?]` → `तथैते` | SECOND-PASS Q1: Kannada p. 160 (the text of p. 161 stands there) reads ತಥೈತೇ ಜಾತವೇದಸಿ |
| 161 | `tathyete [?]` → `tathaite` | SECOND-PASS Q1: Kannada p. 160 reads ತಥೈತೇ ಜಾತವೇದಸಿ |
| 161 | `यज्ञातो [?]` → `यज्ञातो` | SECOND-PASS Q2: Kannada p. 160 reads ಯಜ್ಞಾತೋ ಜಾತವೇದಾಥ (agrees) |
| 161 | `yajjāto [?]` → `yajjāto` | SECOND-PASS Q2: Kannada p. 160 reads ಯಜ್ಞಾತೋ ಜಾತವೇದಾಥ (agrees) |
| 161 | `9-5-1-69 [?]; print shows 9-5-168 with no hyphen after the 1;` → `9-5-168;` | SECOND-PASS Q1: Kannada p. 160 reads ಶ. ಬ್ರಾ. ೯-೫-೧೬೮ (taken as printed) |
| 162 | `1-8 as read [?]` → `1-8` | SECOND-PASS Q2: Kannada p. 162 reads ೧-೮ (agrees) |
| 162 | `[1?]-1-4-8 as read [?]` → `1-4-8` | SECOND-PASS Q1: Kannada p. 162 reads ಕಠೋಪನಿಷತ್. ೧-೪-೮ |
| 162 | `3-29-2 as read [?]` → `3-29-2` | SECOND-PASS Q2: Kannada p. 162 reads ಋ. ಸಂ. ೩-೨೯-೨ (agrees) |
| 162 | `2-[?]-[?] as read [?]` → `2-7-2` | SECOND-PASS Q1: Kannada p. 162 reads ಋ. ಸಂ. ೨-೭-೨ |
| 162 | `3-19-1 as read [?]` → `3-18-1` | SECOND-PASS Q1: Kannada p. 162 reads ಋ. ಸಂ. ೩-೧೮-೧ |
| 165 | `आत्रस्येऽस्य सूक्तस्य ऋषयः [?]` → `अतस्तेऽस्य सूक्तस्य ऋषयः` | SECOND-PASS Q1: Kannada p. 165 reads ಅತಸ್ತೇಽಸ್ಯ ಸೂಕ್ತಸ್ಯ ಋಷಯಃ |
| 165 | `ātrasye 'sya sūktasya ṛṣayaḥ [?]` → `ataste 'sya sūktasya ṛṣayaḥ` | SECOND-PASS Q1: Kannada p. 165 reads ಅತಸ್ತೇಽಸ್ಯ ಸೂಕ್ತಸ್ಯ ಋಷಯಃ |
| 166 | `small [?])` → `small)` | SECOND-PASS Q2: Kannada p. 166 reads ವರ್ಗ—೮, ೯, ೧೦, ೧೧ (agrees) |
| 167 | `णिजादिक इनप्रत्ययः सत्कारान्तादेशश्च [?]` → `औणादिक ईनप्रत्ययस्तकारांतादेशश्च` | SECOND-PASS Q1: Kannada p. 167 reads ಔಣಾದಿಕ ಈನಪ್ರತ್ಯಯಸ್ತಕಾರಾಂತಾದೇಶಶ್ಚ (p. 174 glosses ಈನ ಪ್ರತ್ಯಯ, ದಕಾರಕ್ಕೆ ತಕಾರಾದೇಶ) |
| 167 | `ऋुयि इति मतुवो वत्वम् [?]` → `झय इति मतुपो वत्वं` | SECOND-PASS Q1: Kannada p. 167 reads ಝಯ ಇತಿ ಮತುಪೋ ವತ್ವಂ (p. 175: ಝಯಃ ... ಮತುಪಿನ) |
| 167 | `inapratyayaḥ satkārāntādeśaś ca [?]` → `auṇādika īnapratyayastakārāṃtādeśaśca` | SECOND-PASS Q1: Kannada p. 167 reads ಔಣಾದಿಕ ಈನಪ್ರತ್ಯಯಸ್ತಕಾರಾಂತಾದೇಶಶ್ಚ |
| 167 | `ṛuyi iti matuvo vatvam [?]` → `jhaya iti matupo vatvaṃ` | SECOND-PASS Q1: Kannada p. 167 reads ಝಯ ಇತಿ ಮತುಪೋ ವತ್ವಂ |
| 168 | `1-5[?]-8 as read [?]` → `1-54-8` | SECOND-PASS Q1: Kannada p. 168 reads ಋ. ಸಂ. ೧-೫೪-೮ |
| 168 | `स्तुत [?]` → `स्तुतः` | SECOND-PASS Q1: Kannada p. 168 reads ಸ್ತುತಃ ಶ್ರವಸ್ಯನ್ನವಸೋಪ |
| 168 | `*stuta [?]` → `stutaḥ` | SECOND-PASS Q1: Kannada p. 168 reads ಸ್ತುತಃ ಶ್ರವಸ್ಯನ್ನವಸೋಪ |
| 168 | `1-1[7?]5-18 as read [?]; the first word and *madrig-* clotted in print, not completed from` → `1-177-1` | SECOND-PASS Q1: Kannada p. 168 reads ಋ. ಸಂ. ೧-೧೭೭-೧ and ಸ್ತುತಃ ಶ್ರವಸ್ಯನ್ನವಸೋಪ ಮದ್ರಿಗ್ಯುಕ್ತ್ವಾ |
| 170 | `4-30-10 as read [?]` → `4-30-10` | SECOND-PASS Q2: Kannada p. 170 reads ೪-೩೦-೧೦ (agrees) |
| 170 | `1-[3?]125-4 as read [?]` → `1-55-4` | SECOND-PASS Q1: Kannada p. 170 reads ಋ. ಸಂ. ೧-೫೫-೪ |
| 170 | `1-61-14 as read [?]` → `1-61-14` | SECOND-PASS Q2: Kannada p. 170 reads ೧-೬೧-೧೪ (agrees) |
| 172 | `3-48-3 as read [?]` → `3-48-3` | SECOND-PASS Q2: Kannada p. 172 reads ೩-೪೮-೩ (agrees) |
| 172 | `4-24 as read [?]` → `4-24` | SECOND-PASS Q2: Kannada p. 172 reads ನಿ. ೪-೨೪ (agrees) |
| 172 | `[3?]-4[9?]-3 as read [?]` → `7-98-3` | SECOND-PASS Q1: Kannada p. 172 reads ಋ. ಸಂ. ೭-೯೮-೩ |
| 172 | `2-12-8 as read [?]` → `2-12-8` | SECOND-PASS Q2: Kannada p. 172 reads ೨-೧೨-೮ (agrees) |
| 172 | `6-3[3?]-3 as read [?]` → `6-26-2` | SECOND-PASS Q1: Kannada p. 172 reads ಋ. ಸಂ. ೬-೨೬-೨ |
| 173 | `तान्स्वमदेन्द्रत्ते [?]` → `तान्त्समदविंदत्ते` | SECOND-PASS Q1: Kannada p. 173 reads ತಾನ್ತ್ಸಮದವಿಂದತ್ತೇ ಚತುರ್ಧಾ |
| 173 | `श्रिया ज्योतिष्मानाः [?]` → `श्रियातिष्ठमाना` | SECOND-PASS Q1: Kannada p. 173 reads ಶ್ರಿಯಾತಿಷ್ಠಮಾನಾ |
| 173 | `svamadendratte [?]` → `tāntsamadaviṃdatte` | SECOND-PASS Q1: Kannada p. 173 reads ತಾನ್ತ್ಸಮದವಿಂದತ್ತೇ ಚತುರ್ಧಾ |
| 173 | `śriyā jyotiṣmānāḥ [?]` → `śriyātiṣṭhamānā` | SECOND-PASS Q1: Kannada p. 173 reads ಶ್ರಿಯಾತಿಷ್ಠಮಾನಾ |
| 173 | `3-4-21 as read [?]; the second sentence is clotted in print and not completed from memory` → `3-4-2-1` | SECOND-PASS Q1: Kannada p. 173 reads ಶ. ಚಾ. ೩-೪-೨-೧ and the whole sentence |
| 173 | `2-5-2-6 as read [?]` → `4-3-3-6` | SECOND-PASS Q1: Kannada p. 173 reads ಶ. ಬ್ರಾ. ೪-೩-೩-೬ |
| 173 | `1-6-8 as read [?]` → `1-6-8` | SECOND-PASS Q2: Kannada p. 173 reads ೧-೬-೮ (agrees) |
| 173 | `1-1[6?]6-11 as read [?]` → `1-166-11` | SECOND-PASS Q1: Kannada p. 173 reads ಋ. ಸಂ. ೧-೧೬೬-೧೧ |
| 173 | `1-1[7?]0-3 as read [?]` → `1-171-5` | SECOND-PASS Q1: Kannada p. 173 reads ಋ. ಸಂ. ೧-೧೭೧-೫ |
| 173 | `4-56?]6 as read [?];` → `4-56;` | SECOND-PASS Q1: Kannada p. 173 reads ಬೃ. ದೇ. ೪-೫೬ |
| 174 | `[5-?]-[?] as read [?]` → `5-3` | SECOND-PASS Q1: Kannada p. 174 reads ನಿ. ೫-೩ |
| 174 | `8-68-1 as read [?]` → `8-68-1` | SECOND-PASS Q2: Kannada p. 174 reads ೮-೬೮-೧ (agrees) |
| 177 | `8-1-24 as read [?]` → `8-1-24` | SECOND-PASS Q2: Kannada p. 177 reads ೮-೧-೨೪ (agrees) |
| 177 | `10-112-2 as read [?]` → `10-11-2` | SECOND-PASS Q1: Kannada p. 177 reads ಋ. ಸಂ. ೧೦-೧೧-೨ |
| 177 | `10-49-[7?] as read [?]` → `10-49-7` | SECOND-PASS Q1: Kannada p. 177 reads ಋ. ಸಂ. ೧೦-೪೯-೭ |
| 177 | `10-22-4 as read [?]` → `10-22-4` | SECOND-PASS Q2: Kannada p. 177 reads ೧೦-೨೨-೪ (agrees) |
| 178 | ` […]ṃ [?]` → ` त्वं` | SECOND-PASS Q1: Kannada p. 178 reads ತ್ವಂ ತ್ಯಾ ಚಿದ್ವಾತಸ್ಯಾಶ್ವಾಗಾ |
| 178 | `चिद्वातस्याश्वागा [?]` → `चिद्वातस्याश्वागा` | SECOND-PASS Q2: Kannada p. 178 reads ಚಿದ್ವಾತಸ್ಯಾಶ್ವಾಗಾ (agrees) |
| 178 | `त्वेना [?]` → `त्मना` | SECOND-PASS Q1: Kannada p. 178 reads ತ್ಮನಾ ವಹಧ್ಯೈ |
| 178 | `*[…]ṃ [?]` → `tvaṃ` | SECOND-PASS Q1: Kannada p. 178 reads ತ್ವಂ ತ್ಯಾ ಚಿದ್ವಾತಸ್ಯಾಶ್ವಾಗಾ |
| 178 | `vātasyāśvāgā [?]` → `vātasyāśvāgā` | SECOND-PASS Q2: Kannada p. 178 reads ಚಿದ್ವಾತಸ್ಯಾಶ್ವಾಗಾ (agrees) |
| 178 | `tvenā [?]` → `tmanā` | SECOND-PASS Q1: Kannada p. 178 reads ತ್ಮನಾ ವಹಧ್ಯೈ |
| 178 | `10-22-[?] as read [?]; the first word at the head of the page and several others are clott` → `10-22-5` | SECOND-PASS Q1: Kannada p. 178 reads ಋ. ಸಂ. ೧೦-೨೨-೫ and ತ್ವಂ ತ್ಯಾ ಚಿದ್ವಾತಸ್ಯಾಶ್ವಾಗಾ ... ತ್ಮನಾ ವಹಧ್ಯೈ |
| 178 | `1-166-4 as read [?]` → `1-166-4` | SECOND-PASS Q2: Kannada p. 178 reads ೧-೧೬೬-೪ (agrees) |
| 178 | `5-87-1 as read [?]` → `5-87-1` | SECOND-PASS Q2: Kannada p. 178 reads ೫-೮೭-೧ (agrees) |
| 178 | `5-41-16 as read [?]` → `5-41-16` | SECOND-PASS Q2: Kannada p. 178 reads ೫-೪೧-೧೬ (agrees) |
| 179 | `6-22-10 as read [?]` → `6-22-10` | SECOND-PASS Q2: Kannada p. 179 reads ೬-೨೨-೧೦ (agrees) |
| 179 | `6-736-3 as read [?]` → `6-33-3` | SECOND-PASS Q1: Kannada p. 179 reads ೬-೩೩-೩ |
| 179 | `6-60-6 as read [?]` → `6-60-6` | SECOND-PASS Q2: Kannada p. 179 reads ೬-೬೦-೬ (agrees) |
| 179 | `*Ni.* 3-9 as read [?]` → `*Ni.* 3-9` | SECOND-PASS Q2: Kannada p. 179 reads ನಿ. ೩-೯ (agrees) |
| 179 | `2-23?]3 as read [?]` → `2-23` | SECOND-PASS Q1: Kannada p. 179 reads ನಿ. ೨-೨೩ |
| 181 | `परैरभिगताः [?]` → `परैरनभिगताः` | SECOND-PASS Q1: Kannada p. 181 reads ಪರೈರನಭಿಗತಾಃ । ದುಷ್ಪ್ರಾಪಾ |
| 181 | `parair abhigatāḥ [?]` → `parairanabhigatāḥ` | SECOND-PASS Q1: Kannada p. 181 reads ಪರೈರನಭಿಗತಾಃ |
| 181 | `[print: *parair abhigatāḥ*, as read, doubtful]` → `(*parair anabhigatāḥ*)` | SECOND-PASS Q1: Kannada p. 181 reads ಪರೈರನಭಿಗತಾಃ |

### 2026-11-27 second pass, batch e182-211.tsv
| page | old → new | why |
|---|---|---|
| 182 | `४-१२[३?] [?]` → `४-१२` | SECOND-PASS Q1: Kannada p. 182 reads ४-१२ (ಉ. ೪-೧೨) |
| 182 | `4-12[3?] [?]` → `4-12` | SECOND-PASS Q1: Kannada p. 182 reads 4-12 (ಉ. ೪-೧೨) |
| 183 | `[1-?]3 as read [?]` → `2-23` | SECOND-PASS Q1: Kannada p. 183 reads (ನಿ ೨-೨೩) |
| 183 | `doubtful [?]]` → `doubtful]` | SECOND-PASS Q2: Kannada p. 183 has the same two clauses (ದಿವ ಇತಿ ಪಂಚಮೀ । ನ ಶಬ್ದಃ ಉಪರಿಷ್ಟಾದುಪಚಾರಃ) |
| 183 | `3-9 as read [?]` → `3-9 as read` | SECOND-PASS Q2: Kannada p. 183 reads (ನಿ. ೩-೯) |
| 183 | `[forty-six, as read, ?]` → `forty-six` | SECOND-PASS Q1: Kannada p. 183 reads ೪೬ ಸಂಗ್ರಾಮನಾಮಗಳಲ್ಲಿ |
| 184 | `3-39-4 [?] and 66-2]` → `5-59-4 and 6-66-2]` | SECOND-PASS Q1: Kannada p. 184 reads ೫-೫೯-೪ ; ೬-೬೬-೨ |
| 184 | `केमुत्स्नवे [?] च प्रसवे च सासहिमिन्द्रं देवासः कवसामदन्ननु [?]` → `शमुत्सवे च प्रसवे च सासहिमिन्द्रं देवासः शवसामदन्ननु` | SECOND-PASS Q1: Kannada p. 184 reads ಶಮುತ್ಸವೇ ಚ ... ಶವಸಾಮದನ್ನನು (letters changed: ke->śa, tsna->tsa, ka->śa) |
| 184 | `kemutsnave [?] ca prasave ca sāsahim indraṃ devāsaḥ kavasāmadann anu [?]` → `śamutsave ca prasave ca sāsahim indraṃ devāsaḥ śavasāmadann anu` | SECOND-PASS Q1: Kannada p. 184 reads ಶಮುತ್ಸವೇ ... ಶವಸಾಮದನ್ನನು |
| 184 | `सासहिर्दधानो [?]` → `सासहिर्दधानो` | SECOND-PASS Q2: Kannada p. 184 reads ಸುಪ್ರಕೇತೇಭಿಃ ಸಾಸಹಿರ್ದಧಾನೋ |
| 184 | `sāsahir dadhāno [?]` → `sāsahir dadhāno` | SECOND-PASS Q2: Kannada p. 184 reads ಸಾಸಹಿರ್ದಧಾನೋ |
| 184 | `*supāṃ suṣo bhavanti* [?]` → `*supāṃ supo bhavanti*` | SECOND-PASS Q1: Kannada p. 184 reads ಸುಪಾಂ ಸುಪೋ ಭವಂತಿ (ṣ->p) |
| 184 | `Uṇ. Sū. 4-[?]]` → `Uṇ. Sū. 4-452]` | SECOND-PASS Q1: Kannada p. 185 reads (ಉ. ಸೂ. ೪-೪೫೨) |
| 186 | `printed pp. 186–[?]` → `printed pp. 186–191` | SECOND-PASS Q1: Kannada: the grammar of Rik 4 ends on p. 191 where Rik 5 begins |
| 186 | `४-७३५, ७३६ [?]` → `४-२३५, २३६` | SECOND-PASS Q1: Kannada p. 186 reads ಉ. ಉ. ೪-೨೩೫, ೨೩೬ |
| 186 | `4-735, 736 [?]` → `4-235, 236` | SECOND-PASS Q1: Kannada p. 186 reads ಉ. ಉ. ೪-೨೩೫, ೨೩೬ |
| 186 | `ऽसुन् [?]` → `ऽसुन्` | SECOND-PASS Q2: Kannada p. 186 reads ಇತ್ಯೌಣಾದಿಕೋಽಸುನ್ |
| 186 | `auṇādiko 'sun [?]` → `auṇādiko 'sun` | SECOND-PASS Q2: Kannada p. 186 reads ಇತ್ಯೌಣಾದಿಕೋಽಸುನ್ |
| 186 | `तृतीया [?]` → `तृतीया` | SECOND-PASS Q2: Kannada p. 186 reads ತೃತೀಯಾ |
| 186 | `tṛtīyā [?]` → `tṛtīyā` | SECOND-PASS Q2: Kannada p. 186 reads ತೃತೀಯಾ |
| 187 | `द्रष्टव्यः [?]` → `द्रष्टव्यः` | SECOND-PASS Q2: Kannada p. 187 reads ದ್ರಷ್ಟವ್ಯಃ |
| 187 | `draṣṭavyaḥ [?]` → `draṣṭavyaḥ` | SECOND-PASS Q2: Kannada p. 187 reads ದ್ರಷ್ಟವ್ಯಃ |
| 188 | `1-[4?]958-9 as read [?]` → `1-45-3` | SECOND-PASS Q1: Kannada p. 188 reads (ಋ. ಸಂ. ೧-೪೫-೩) |
| 188 | `1-[7?]8-3 as read [?]` → `1-78-3` | SECOND-PASS Q1: Kannada p. 188 reads (ಋ. ಸಂ. ೧-೭೮-೩) |
| 188 | `1-1-3 as read [?]` → `1-1-3 as read` | SECOND-PASS Q2: Kannada p. 188 reads (ಮುಂಡಕೋಪನಿಷತ್ ೧-೧-೩) |
| 188 | `1-1 as read [?]` → `1-31-1` | SECOND-PASS Q1: Kannada p. 188 reads (ಋ. ಸಂ. ೧-೩೧-೧) |
| 189 | `3-34[4?] as read [?]` → `3-34` | SECOND-PASS Q1: Kannada p. 189 reads (ಐ. ಬ್ರಾ. ೩-೩೪) |
| 189 | `5-11-6 as read [?]` → `5-11-6 as read` | SECOND-PASS Q2: Kannada p. 189 reads (ಋ. ಸಂ. ೫-೧೧-೬) |
| 189 | `1-4-1-25?]5 as read [?]` → `1-4-1-25` | SECOND-PASS Q1: Kannada p. 189 reads (ಬ್ರಾ. ೧-೪-೧-೨೫) |
| 189 | `10-14-6 as read [?]` → `10-14-6 as read` | SECOND-PASS Q2: Kannada p. 189 reads (ಋ. ಸಂ. ೧೦-೧೪-೬) |
| 189 | `3-31-5 to 6 as read [?];` → `3-31-5 to 6 as read;` | SECOND-PASS Q2: Kannada p. 189 reads (ಋ. ಸಂ. ೩-೩೧-೫ ರಿಂದ ೬) |
| 190 | `4-[?]-[?] as read, ?]` → `675-676]` | SECOND-PASS Q1: Kannada p. 190 reads (ಉ ಸೂ ೬೭೫-೬೭೬) |
| 191 | `printed pp. 191–[?]` → `printed pp. 191–196` | SECOND-PASS Q1: Kannada: the grammar of Rik 5 ends on p. 196 where Rik 6 begins |
| 193 | `2-34-2 as read [?]` → `2-34-2 as read` | SECOND-PASS Q2: Kannada p. 193 reads (ಋ. ಸಂ. ೨-೩೪-೨) |
| 193 | `2-11-4 as read [?]` → `2-2-11-4` | SECOND-PASS Q1: Kannada p. 193 reads (ತೈ. ಸಂ. ೨-೨-೧೧-೪) |
| 193 | `1-85-1[5?]-1 as read [?]` → `1-85-1` | SECOND-PASS Q1: Kannada p. 193 reads (ಋ. ಸಂ. ೧-೮೫-೧) |
| 193 | `1-114-6 as read [?]` → `1-114-6 as read` | SECOND-PASS Q2: Kannada p. 193 reads (ಋ. ಸಂ. ೧-೧೧೪-೬) |
| 193 | `1-1[4?]7-9 and 2-3[3?]-1 [as read [?]]` → `1-168-9 and 2-33-1` | SECOND-PASS Q1: Kannada p. 193 reads ೧-೧೬೮-೯ ; ೨-೩೩-೧ |
| 194 | `केवेमे [?] पुत्राः` → `तवेमे पुत्राः` | SECOND-PASS Q1: Kannada p. 194 reads ತವೇಮೇ ಪುತ್ರಾಃ (letters changed: ke->ta, ve->ve) |
| 194 | `keveme [?] putrāḥ` → `taveme putrāḥ` | SECOND-PASS Q1: Kannada p. 194 reads ತವೇಮೇ ಪುತ್ರಾಃ |
| 194 | `11-21 as read [?]` → `11-21 as read` | SECOND-PASS Q2: Kannada p. 194 reads (ನಿ. ೧೧-೨೧) |
| 196 | `printed pp. 196–[?]` → `printed pp. 196–201` | SECOND-PASS Q1: Kannada: the grammar of Rik 6 ends on p. 201 where Rik 7 begins |
| 197 | `निर्माता [?]` → `निर्माता` | SECOND-PASS Q2: Kannada p. 197 reads ನಿರ್ಮಾತಾ |
| 197 | `nirmātā [?]` → `nirmātā` | SECOND-PASS Q2: Kannada p. 197 reads ನಿರ್ಮಾತಾ |
| 197 | `७-३-७८ [?]` → `६-३-७८` | SECOND-PASS Q1: Kannada p. 197 reads (ಪಾ. ೬-೩-೭೮) |
| 197 | `7-3-78 [?]` → `6-3-78` | SECOND-PASS Q1: Kannada p. 197 reads (ಪಾ. ೬-೩-೭೮) |
| 197 | `युष्माकास्माकौ [?] … अस्मच्छब्दस्यास्माकादेशः` → `युष्माकास्माकावित्यण्यस्मच्छब्दस्यास्माकादेशः` | SECOND-PASS Q1: Kannada p. 197 reads ಯುಷ್ಮಾಕಾಸ್ಮಾಕಾವಿತ್ಯಣ್ಯಸ್ಮಚ್ಛಬ್ದಸ್ಯಾಸ್ಮಾಕಾದೇಶಃ |
| 197 | `yuṣmākāsmākau [?] … asmacchabdasyāsmākādeśaḥ` → `yuṣmākāsmākāv ity aṇy asmacchabdasyāsmākādeśaḥ` | SECOND-PASS Q1: Kannada p. 197 reads ಯುಷ್ಮಾಕಾಸ್ಮಾಕಾವಿತ್ಯಣ್ಯಸ್ಮಚ್ಛಬ್ದಸ್ಯಾಸ್ಮಾಕಾದೇಶಃ |
| 197 | `विधेरनित्यत्वादैस्यैष्यभावः [?]` → `विधेरनित्यत्वाद्वृद्ध्यभावः` | SECOND-PASS Q1: Kannada p. 197 reads ವಿಧೇರನಿತ್ಯತ್ವಾದ್ವೃದ್ಧ್ಯಭಾವಃ |
| 197 | `vidher anityatvād aisyaiṣyabhāvaḥ [?]` → `vidher anityatvād vṛddhyabhāvaḥ` | SECOND-PASS Q1: Kannada p. 197 reads ವಿಧೇರನಿತ್ಯತ್ವಾದ್ವೃದ್ಧ್ಯಭಾವಃ |
| 197 | `1-97-3 as read [?]]` → `1-97-3 as read]` | SECOND-PASS Q2: Kannada p. 197 reads (ಋ. ೧-೯೭-೩) |
| 198 | `10-29 as read [?]` → `10-29 as read` | SECOND-PASS Q2: Kannada p. 198 reads (ನಿ. ೧೦-೨೯) |
| 198 | `उदक्रामन्त्स्मैक एव [?]` → `उदक्रामंस्तमेक एव` | SECOND-PASS Q1: Kannada p. 198 reads ಉದಕ್ರಾಮಂಸ್ತಮೇಕ ಏವ |
| 198 | `udakrāman smaika eva [?]` → `udakrāṃs tam eka eva` | SECOND-PASS Q1: Kannada p. 198 reads ಉದಕ್ರಾಮಂಸ್ತಮೇಕ ಏವ |
| 198 | `तान्यस्मिन्नो [?] प्रत्यतिष्ठत् [?]` → `तान्यस्मिन्मन्यौ प्रत्यतिष्ठत्` | SECOND-PASS Q1: Kannada p. 198 reads ತಾನ್ಯಸ್ಮಿನ್ಮನ್ಯೌ ಪ್ರತ್ಯತಿಷ್ಠತ್ |
| 198 | `tāny asminno [?] pratyatiṣṭhat [?]` → `tāny asmin manyau pratyatiṣṭhat` | SECOND-PASS Q1: Kannada p. 198 reads ತಾನ್ಯಸ್ಮಿನ್ಮನ್ಯೌ ಪ್ರತ್ಯತಿಷ್ಠತ್ |
| 198 | `91-1-6 as read [?]` → `9-1-1-6` | SECOND-PASS Q1: Kannada p. 198 reads (ಶ. ಬ್ರಾ. ೯-೧-೧-೬) |
| 199 | `1-122–3 as read [?]` → `1-122-3` | SECOND-PASS Q1: Kannada p. 199 reads (ಬೃ. ಜೆ. ೧-೧೨೨-೩) |
| 199 | `3-9 as read [?]` → `3-9 as read` | SECOND-PASS Q2: Kannada p. 199 reads (ನಿ. ೩-೯) |
| 200 | `1-97-3 as read [?]]` → `1-97-3 as read]` | SECOND-PASS Q2: Kannada p. 200 reads (ಋ. ಸ. ೧-೯೭-೩) |
| 201 | `printed pp. 201–[?]` → `printed pp. 201–206` | SECOND-PASS Q1: Kannada: the grammar of Rik 7 ends on p. 206 where Rik 8 begins |
| 202 | `श्र्युकः किति [?] इति [rule-name clotted] इट्प्रतिषेधः` → `तितुत्रेतीट् प्रतिषेधः` | SECOND-PASS Q1: Kannada p. 202 reads ತಿತುತ್ರೇತೀಟ್ ಪ್ರತಿಷೇಧಃ (Kannada p. 204 gives Pā. Sū. 7-2-9 for this prohibition) |
| 202 | `śryukaḥ kiti [?] iti [rule-name clotted] iṭpratiṣedhaḥ` → `titutretīṭ pratiṣedhaḥ` | SECOND-PASS Q1: Kannada p. 202 reads ತಿತುತ್ರೇತೀಟ್ ಪ್ರತಿಷೇಧಃ |
| 202 | `अन्त्यैकार` → `अन्त्यविकार` | SECOND-PASS Q1: Kannada p. 202 reads ಅಂತ್ಯವಿಕಾರಶ್ಕಾಂದಸಃ (ai->vi) |
| 202 | `ः [?] । यद्वा` → `ः । यद्वा` | SECOND-PASS Q1: Kannada p. 202 reads ಅಂತ್ಯವಿಕಾರಶ್ಕಾಂದಸಃ (mark removed with the correction above) |
| 202 | `antyaikāraś chāndasaḥ [?]` → `antyavikāraś chāndasaḥ` | SECOND-PASS Q1: Kannada p. 202 reads ಅಂತ್ಯವಿಕಾರಶ್ಕಾಂದಸಃ (ai->vi) |
| 203 | `3-47-1 as read [?]` → `3-47-1 as read` | SECOND-PASS Q2: Kannada p. 203 reads (ಋ. ಸಂ. ೩-೪೭-೧) |
| 203 | `1-171-1 as read [?]` → `1-171-1 as read` | SECOND-PASS Q2: Kannada p. 203 reads (ಋ. ಸಂ. ೧-೧೭೧-೧) |
| 203 | `[5?]-52-3 as read [?]` → `7-57-5` | SECOND-PASS Q1: Kannada p. 203 reads (ಋ. ಸಂ. ೭-೫೭-೫) |
| 203 | `2-57-3-20 as read [?]` → `2-5-3-20` | SECOND-PASS Q1: Kannada p. 203 reads (ಶ. ಬ್ರಾ. ೨-೫-೩-೨೦) |
| 204 | `twenty-five [as read, ?] names of man, the sense is 'men' (*Ni.* 2-[2?] as read [?]).` → `twenty-five names of man, the sense is 'men' (*Ni.* 3-7).` | SECOND-PASS Q1: Kannada p. 204 reads ೨೫ ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ ... (ನಿ. ೩-೭) |
| 204 | `3-20-4 as read [?]` → `3-20-4 as read` | SECOND-PASS Q2: Kannada p. 204 reads (ಋ. ಸಂ. ೩-೨೦-೪) |
| 204 | `twenty-six [as read, ?] names of action (*Ni.* 2-1 as read [?])` → `twenty-six names of action (*Ni.* 28)` | SECOND-PASS Q1: Kannada p. 204 reads ೨೬ ಕರ್ಮನಾಮಗಳಲ್ಲಿ ... (ನಿ. ೨೮) |
| 204 | `1-41-33?]2 as read [?]` → `1-4-1-33` | SECOND-PASS Q1: Kannada p. 204 reads (ತ. ಬ್ರಾ. ೧-೪-೧-೩೩) |
| 204 | `11-1-3-4 as read [?]` → `11-1-3-4 as read` | SECOND-PASS Q2: Kannada p. 204 reads (ಶ. ಬ್ರಾ. ೧೧-೧-೩-೪) |
| 206 | `3-133, read in print as 3-[?]3, ?]` → `3-133]` | SECOND-PASS Q1: Kannada p. 206 reads (ಉ. ಸೂ. ೩-೧೩೩) |
| 206 | `printed pp. 206–[?]` → `printed pp. 206–210` | SECOND-PASS Q1: Kannada: the grammar of Rik 8 ends on p. 210 where Rik 9 begins |
| 207 | `क्नप्रत्ययः [?]` → `क्सप्रत्ययः` | SECOND-PASS Q1: Kannada p. 207 reads ವ್ಯತ್ಯಯೇನ ಕ್ಸಪ್ರತ್ಯಯಃ (n->s) |
| 207 | `knapratyayaḥ [?]` → `ksapratyayaḥ` | SECOND-PASS Q1: Kannada p. 207 reads ಕ್ಸಪ್ರತ್ಯಯಃ |
| 207 | `धातोर्[?]` → `धातोर्ह्रस्व` | SECOND-PASS Q1: Kannada p. 207 reads ವ್ಯತ್ಯಯೇನ ಧಾತೋರ್ಹ್ರಸ್ವತ್ವಂ |
| 207 | `त्वम् [?]` → `त्वम्` | SECOND-PASS Q1: Kannada p. 207 reads ಧಾತೋರ್ಹ್ರಸ್ವತ್ವಂ (mark removed with the correction above) |
| 207 | `dhātor[?]tvam [?]` → `dhātor hrasvatvam` | SECOND-PASS Q1: Kannada p. 207 reads ಧಾತೋರ್ಹ್ರಸ್ವತ್ವಂ |
| 208 | `अहोहा` → `अहिमोहा` | SECOND-PASS Q1: Kannada p. 208 reads ಅಹಿಮೋಹಾನಂ (letters changed: ho->himo) |
| 208 | `हानम् [?]` → `हानम्` | SECOND-PASS Q1: Kannada p. 208 reads ಅಹಿಮೋಹಾನಂ (mark removed with the correction above) |
| 208 | `सक्षदिन्द्रः [?]` → `सक्षदिन्द्रः` | SECOND-PASS Q2: Kannada p. 208 reads ಸಕ್ಷದಿಂದ್ರಃ |
| 208 | `ahohānam [?]` → `ahimohānam` | SECOND-PASS Q1: Kannada p. 208 reads ಅಹಿಮೋಹಾನಂ |
| 208 | `sakṣad indraḥ [?]` → `sakṣad indraḥ` | SECOND-PASS Q2: Kannada p. 208 reads ಸಕ್ಷದಿಂದ್ರಃ |
| 208 | `5-30-6 as read [?];` → `5-30-6 as read;` | SECOND-PASS Q2: Kannada p. 208 reads (ಋ. ಸಂ. ೫-೩೦-೬) |
| 208 | `5-22-2 as read [?]` → `5-32-3` | SECOND-PASS Q1: Kannada p. 208 reads (ಋ. ಸಂ. ೫-೩೨-೩) |
| 209 | `कम् [?]` → `कम्` | SECOND-PASS Q2: Kannada p. 209 reads ಶುಷ್ಣ ಸಂಜ್ಞಕಂ |
| 209 | `śuṣṇasaṃjñakam [?]` → `śuṣṇasaṃjñakam` | SECOND-PASS Q2: Kannada p. 209 reads ಶುಷ್ಣ ಸಂಜ್ಞಕಂ |
| 209 | `3-12-7 as read [?]` → `2-12-7` | SECOND-PASS Q1: Kannada p. 209 reads (ಋ. ಸಂ. ೨-೧೨-೭) |
| 209 | `3-24-4 as read [?]` → `3-34-4` | SECOND-PASS Q1: Kannada p. 209 reads (ಖ. ಸಂ. ೩-೩೪-೪) |
| 209 | `5-40-6 as read [?]` → `5-20-6` | SECOND-PASS Q1: Kannada p. 209 reads (ಋ. ಸಂ. ೫-೨೦-೬) |
| 210 | `the print reads *āṭ*, as read [?]]` → `the print reads *aṭ*]` | SECOND-PASS Q1: Kannada p. 210 reads ಅಟ್ ಪ್ರತ್ಯಯ |
| 210 | `4-[?]3 as read, ?]` → `4-628]` | SECOND-PASS Q1: Kannada p. 210 reads (ಉ. ಸೂ. ೪-೬೨೮) |
| 211 | `णिच्चेमन्तः शत्संनित्वे [?]` → `णिच्यमन्तत्वान्मित्वे` | SECOND-PASS Q1: Kannada p. 211 reads ಣಿಚ್ಯಮಂತತ್ವಾನ್ಮಿತ್ವೇ ಮಿತಾಂ ಹ್ರಸ್ವ |
| 211 | `ṇicce mantaḥ śatsaṃnitve [?]` → `ṇicy amantatvān mitve` | SECOND-PASS Q1: Kannada p. 211 reads ಣಿಚ್ಯಮಂತತ್ವಾನ್ಮಿತ್ವೇ |
| 211 | `इति सलोपः [?]` → `इति सलोपः` | SECOND-PASS Q2: Kannada p. 211 reads ಲಿಜಃ ಸಲೋಪ ಇತಿ ಸಲೋಪಃ |
| 211 | `iti salopaḥ [?]` → `iti salopaḥ` | SECOND-PASS Q2: Kannada p. 211 reads ಇತಿ ಸಲೋಪಃ |
