
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
