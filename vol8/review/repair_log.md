
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

### 2026-11-27 second pass, batch e212-241.tsv
| page | old → new | why |
|---|---|---|
| 213 | `1-100-7 as read [?]` → `1-135-9` | SECOND-PASS Q1: Kannada p. 213 reads (ಋ. ಸಂ. ೧-೧೩೫-೯) |
| 213 | `1-1[4?]0-3 as read [?]` → `1-150-3` | SECOND-PASS Q1: Kannada p. 213 reads (ಋ. ಸಂ. ೧-೧೫೦-೩) |
| 213 | `1-1[1?]3-10 as read [?]` → `1-122-10` | SECOND-PASS Q1: Kannada p. 213 reads (ಋ. ಸಂ. ೧-೧೨೨-೧೦) |
| 213 | `10-[6?]9-[1?]2 as read [?]` → `10-89-15` | SECOND-PASS Q1: Kannada p. 213 reads (ಋ. ಸಂ. ೧೦-೮೯-೧೫) |
| 213 | `3-19[6?] as read [?]` → `3-19` | SECOND-PASS Q1: Kannada p. 213 reads (ನಿ. ೩-೧೯) |
| 213 | `1-3[1?]-13 as read [?]` → `1-31-13` | SECOND-PASS Q1: Kannada p. 213 reads (ಋ. ಸಂ. ೧-೩೧-೧೩) |
| 215 | `printed pp. 215–[?]` → `printed pp. 215–219` | SECOND-PASS Q1: Kannada: the grammar of Rik 10 ends on p. 219 where Rik 11 begins |
| 219 | `printed pp. 219–[?]` → `printed pp. 219–223` | SECOND-PASS Q1: Kannada: the grammar of Rik 11 ends on p. 223 where Rik 12 begins |
| 223 | `printed pp. 223–[?]` → `printed pp. 223–230` | SECOND-PASS Q1: Kannada: the grammar of Rik 12 ends on p. 230 where Rik 13 begins |
| 230 | `printed pp. 230–[?]` → `printed pp. 230–235` | SECOND-PASS Q1: Kannada: the grammar of Rik 13 ends on p. 235 where Rik 14 begins |
| 235 | `printed pp. 235–[?]` → `printed pp. 235–239` | SECOND-PASS Q1: Kannada: the grammar of Rik 14 ends on p. 239; Rik 15 begins on p. 240 |
| 239 | `printed pp. 240–[?]` → `printed pp. 240–243` | SECOND-PASS Q1: Kannada: the grammar of Rik 15 ends on p. 243; Rik 16 begins on p. 244 |
| 216 | `तते [?] । ` → `तते । ` | SECOND-PASS Q2: Kannada p. 216 reads the bhāṣya as the English: ಅಭಿಭವನ್ವರ್ತತೇ । ಮರುತ್ವಾನ್ಸ |
| 216 | `२-१४ [?]` → `२-१५` | SECOND-PASS Q1: Kannada p. 216 reads ಫಿ. ೨-೧೫ |
| 216 | `ate [?] | ` → `ate | ` | SECOND-PASS Q2: Kannada p. 216 reads the bhāṣya as the English: ಅಭಿಭವನ್ವರ್ತತೇ । ಮರುತ್ವಾನ್ಸ |
| 216 | `em] [?]. M` → `em]. M` | SECOND-PASS Q2: Kannada p. 216 has the same sentence (ಅಭಿಭವನ್ವರ್ತತೇ) |
| 218 | `2-[9?] as read [?]` → `3-9` | SECOND-PASS Q1: Kannada p. 218 reads (ನಿ. ೩-೯) |
| 218 | `साः [?] ।` → `साः ।` | SECOND-PASS Q2: Kannada p. 218 reads ನೃಶಂಸಾಃ |
| 218 | `sāḥ [?] |*` → `sāḥ |*` | SECOND-PASS Q2: Kannada p. 218 reads ನೃಶಂಸಾಃ |
| 218 | `ead [?]]: ` → `ead]: ` | SECOND-PASS Q2: Kannada p. 218 reads ನೃಶಂಸಾಃ |
| 218 | `[Phiṭ-sūtra 2-[?]4 as read, ?]` → `[Phiṭ-sūtra 38]` | SECOND-PASS Q1: Kannada p. 218 reads (ಫಿ. ಸೂ. ೩೮) |
| 220 | `पां [?] इन` → `पां इन` | SECOND-PASS Q2: Kannada p. 220 reads ತೇಷಾಮುಭಯವಿಧಾನಾಮಪಾಮಿಂದ್ರಂ |
| 220 | `pāṃ [?] in` → `pāṃ in` | SECOND-PASS Q2: Kannada p. 220 reads ತೇಷಾಮುಭಯವಿಧಾನಾಮಪಾಮಿಂದ್ರಂ |
| 220 | `jeṣṛ [?] ` → `jeṣṛ णेषृ प्रेषृ ` | SECOND-PASS Q1: Kannada p. 220 reads ಜೇಷ್ಯ ಣೇಷೃ ಪ್ರೇಷೃ ಗತೌ (as the Devanagari line) |
| 221 | `as read [?]), the sense` → `as read), the sense` | SECOND-PASS Q2: Kannada p. 221 reads (ನಿ. ೩-೯) |
| 221 | `2-106-72 as read [?]` → `9-106-2` | SECOND-PASS Q1: Kannada p. 221 reads (ಋ. ಸಂ. ೯-೧೦೬-೨) |
| 221 | `as read [?]).` → `as read).` | SECOND-PASS Q2: Kannada p. 221 reads (ನಿ- ೩-೯) |
| 221 | `(*Ni.* 3-9 as read [?]; clotted` → `(*Ni.* 3-9 as read; clotted` | SECOND-PASS Q2: Kannada p. 221 reads (ನಿ. ೩-೯) |
| 221 | `जामुपत्वम् [?] । जमतीर्वा स्यान्निगमनप्रायाः भवति [?]` → `जामपत्यं । जमतेर्वा स्याद्गतिकर्मणो निर्गमनप्राया भवति` | SECOND-PASS Q1: Kannada p. 221 reads ಜಾಮೀರನ್ಯೇಽಸ್ಯಾಂ ಜನಯಂತಿ ಜಾಮಪತ್ಯಂ । ಜಮತೇರ್ವಾ ಸ್ಯಾದ್ಗತಿಕರ್ಮಣೋ ನಿರ್ಗಮನಪ್ರಾಯಾ ಭವತಿ (its gloss that follows, ಮಕ್ಕಳನ್ನು ಉತ್ಪನ್ನ… and ಜಮ್ ಧಾತು, con |
| 221 | `jāmupatvam [?] | jamatīr vā syān nigamanaprāyāḥ bhavati [?]` → `jāmapatyaṃ | jamatervā syādgatikarmaṇo nirgamanaprāyā bhavati` | SECOND-PASS Q1: Kannada p. 221 reads ಜಾಮೀರನ್ಯೇಽಸ್ಯಾಂ ಜನಯಂತಿ ಜಾಮಪತ್ಯಂ । ಜಮತೇರ್ವಾ ಸ್ಯಾದ್ಗತಿಕರ್ಮಣೋ ನಿರ್ಗಮನಪ್ರಾಯಾ ಭವತಿ (its gloss that follows, ಮಕ್ಕಳನ್ನು ಉತ್ಪನ್ನ… and ಜಮ್ ಧಾತು, con |
| 222 | `1-75-3/4?] as read [?]` → `1-65-7` | SECOND-PASS Q1: Kannada p. 222 reads (ಋ. ಸಂ. ೧-೬೫-೭.) |
| 222 | `8-[2?]3-3 as read [?]` → `1-25-3` | SECOND-PASS Q1: Kannada p. 222 reads (ಋ. ಸಂ. ೧-೨೫-೩.) |
| 222 | `9-[3?]9-28-4 as read [?]` → `9-28-4` | SECOND-PASS Q1: Kannada p. 222 reads (ಋ. ಸಂ. ೯-೨೮-೪.) |
| 222 | `9-68-4 as read [?]` → `9-68-4 as read` | SECOND-PASS Q2: Kannada p. 222 reads (ಋ. ಸಂ. ೯-೬೮-೪.) |
| 225 | `6-15 as read [?]` → `7-15` | SECOND-PASS Q1: Kannada p. 225 reads (ನಿ. ೭-೧೫) |
| 226 | `(*Ni.* 51-24 as read [?]) [as read, doubtful [?]]` → `(*Ni.* 7-23)` | SECOND-PASS Q1: Kannada p. 226 reads (ನಿ. ೭-೨೩) |
| 226 | `6-18-3 as read [?]` → `6-18-3 as read` | SECOND-PASS Q2: Kannada p. 226 reads (ಋ. ಸಂ. 618-3, the hyphen after the first figure missing; digits agree with the English) |
| 226 | `6-45-24 as read [?]` → `6-45-24 as read` | SECOND-PASS Q2: Kannada p. 226 reads (ಋ. ಸಂ. ೬-೪೫-೨೪) |
| 226 | `8-76-11 as read [?]` → `8-76-11 as read` | SECOND-PASS Q2: Kannada p. 226 reads (ಋ. ಸಂ. ೮-೭೬-೧೧) |
| 226 | `10-47-4 as read [?]` → `10-47-4 as read` | SECOND-PASS Q2: Kannada p. 226 reads (ಋ. ಸಂ. ೧೦-೪೭-೪) |
| 226 | `1-61-14 as read [?]` → `1-61-14 as read` | SECOND-PASS Q2: Kannada p. 226 reads (ಋ. ಸಂ. ೧-೬೧-೧೪) |
| 226 | `4-17-2 as read [?]` → `4-17-2 as read` | SECOND-PASS Q2: Kannada p. 226 reads (ಋ. ಸಂ. ೪-೧೭-೨) |
| 227 | `897-14 as read [?]` → `8-97-14` | SECOND-PASS Q1: Kannada p. 227 reads (ಋ. ಸಂ. ೮-೯೭-೧೪) |
| 228 | `6-66 as read [?]` → `7-66` | SECOND-PASS Q1: Kannada p. 228 reads (ಬೃ. ದೇ. ೭-೬೬) |
| 228 | `7-67 as read [?]` → `7-67 as read` | SECOND-PASS Q2: Kannada p. 228 reads (ಬೃ. ದೇ. ೭-೬೭) |
| 228 | `6-68[8?] as read [?]` → `7-68` | SECOND-PASS Q1: Kannada p. 228 reads (ಬೃ. ದೇ. ೭-೬೮) |
| 228 | `7-69 as read [?]` → `7-69 as read` | SECOND-PASS Q2: Kannada p. 228 reads (ಬೃ. ದೇ. ೭-೬೯) |
| 228 | `2-20 as read [?]` → `7-20` | SECOND-PASS Q1: Kannada p. 228 reads (ಬೃ. ದೇ. ೭-೨೦) |
| 230 | `[Uṇ. Sū. 2-[?]4 as read, ?]` → `[Uṇ. Sū. 2-159]` | SECOND-PASS Q1: Kannada p. 230 reads (ಉ. ಸೂ. ೨-೧೫೯) |
| 230 | `vārttika 1, as read [?]]` → `vārttika 1, as read]` | SECOND-PASS Q2: Kannada p. 230 reads (ಕಾ. ೪-೩-೫೮-೧) |
| 232 | `1-61-6 as read [?]` → `1-61-6 as read` | SECOND-PASS Q2: Kannada p. 232 reads (ಋ. ಸಂ. ೧-೬೧-೬) |
| 232 | `5-31-4 as read [?]` → `5-31-4 as read` | SECOND-PASS Q2: Kannada p. 232 reads (ಋ. ಸಂ. ೫-೩೧-೪) |
| 232 | `1-121-12 as read [?]` → `1-121-12 as read` | SECOND-PASS Q2: Kannada p. 232 reads (ಋ. ಸಂ. ೧-೧೨೧-೧೨) |
| 232 | `8-100-9 as read [?]` → `8-100-9 as read` | SECOND-PASS Q2: Kannada p. 232 reads (ಋ. ಸಂ. ೮-೧೦೦-೯) |
| 233 | `5-87-8; 2-5-0; 8-18-4 and others, numerals as read [?]` → `5-86-8; 7-3-8; 8-18-4 and others, numerals as read` | SECOND-PASS Q1: Kannada p. 233 reads 5-41-19 5-86-8, 7-3-8, 8-18-4 (೫-೪೧-೧೯ ೫-೮೬-೮, ೭-೩-೮, ೮-೧೮-೪) |
| 233 | `1-73-6 [as read [?]]` → `1-73-6 [as read]` | SECOND-PASS Q2: Kannada p. 233 reads ಋ. ಸಂ. ೧-೭೩-೬ |
| 233 | `2-4-9 [as read [?]]` → `2-4-9 [as read]` | SECOND-PASS Q2: Kannada p. 233 reads ೨-೪-೯ |
| 234 | `[Uṇ. Sū. 3-[?]3 as read, ?]` → `[Uṇ. Sū. 3-393]` | SECOND-PASS Q1: Kannada p. 234 reads (ಉ. ಸೂ. ೩-೩೯೩) |
| 238 | `4-18-4 as read [?]` → `4-18-4 as read` | SECOND-PASS Q2: Kannada p. 238 reads (ಋ. ಸಂ. ೪-೧೮-೪) |
| 238 | `2-[3?]5 as read [?]` → `2-5` | SECOND-PASS Q1: Kannada p. 238 reads ( ನಿ. ೨-೫ ) |
| 238 | `[forty-four, as read, ?] names of the *arcati*-verbs [?],` → `forty-four names of the *arcati*-verbs,` | SECOND-PASS Q1: Kannada p. 238 reads ೪೪ ಅರ್ಚತಿಕರ್ಮಗಳ ನಾಮಗಳಲ್ಲಿ |
| 240 | `लोकद्वयोदपस्य [?]` → `लोकद्वयादप्यस्य` | SECOND-PASS Q1: Kannada p. 240 reads ಲೋಕದ್ವಯಾದಪ್ಯಸ್ಯ ಬಲಮತಿರಿಚ್ಯತ ಇತ್ಯರ್ಥಃ (the English gloss "his strength exceeds even the two worlds" agrees) |
| 240 | `lokadvayodapasya [?]` → `lokadvayādapyasya` | SECOND-PASS Q1: Kannada p. 240 reads ಲೋಕದ್ವಯಾದಪ್ಯಸ್ಯ |

### 2026-11-27 second pass, batch e212-241_2.tsv
| page | old → new | why |
|---|---|---|
| 220 | `[?] गतौ` → `णेषृ प्रेषृ गतौ` | SECOND-PASS Q1: Kannada p. 220 reads ಜೇಷ್ಯ ಣೇಷೃ ಪ್ರೇಷೃ ಗತೌ (ಜೇಷ್ಯ a misprint, English jeṣṛ kept; the mark stood for the omitted ṇeṣṛ preṣṛ) |

### 2026-11-27 qmark_strip.py: BLOCK 1356 marks removed from 750 Sanskrit-block lines (derived data, K9); BARE 49 boilerplate remark lines removed (53 marks); OTHER 2758 marks left

### 2026-11-27 second pass, batch m236-385.tsv
| page | old → new | why |
|---|---|---|
| 242 | `1-25-1 as read [?]` → `1-55-1` | SECOND-PASS Q1: Kannada p. 242 reads (ಋ. ಸಂ. ೧-೫೫-೧) |
| 242 | `1-61-9 as read [?]` → `1-61-9` | SECOND-PASS Q2: Kannada agrees (೧-೬೧-೯) |
| 242 | `[8?]-19-3 as read [?]` → `4-16-5` | SECOND-PASS Q1: Kannada p. 242 reads (ಋ. ಸಂ. ೪-೧೬-೫) |
| 242 | `6-30-4 as read [?]` → `6-30-4` | SECOND-PASS Q2: Kannada agrees (೬-೩೦-೪) |
| 242 | `lokadvayodapasya [?]` → `lokadvayodapasya` | SECOND-PASS Q2: Kannada pp. 240/242 read ಲೋಕದ್ವಯಾದಪ್ಯಸ್ಯ; the note itself states the earlier misreading |
| 243 | `noted briefly; numerals small and doubtful [?])` → `noted briefly; numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 243 | `printed pp. 244–[?]` → `printed pp. 244–250` | SECOND-PASS Q1: Kannada: Rik 16 ends (॥ ೧೬ ॥) on p. 250 |
| 244 | ` Numerals and one clotted clause are marked [?].` → `` | SECOND-PASS S3: doubt sentence only; the grammar summary kept |
| 245 | `Va. 11 [?]"` → `Va. 11"` | SECOND-PASS Q2: Kannada p. 245 head reads ವ. ೧೧ |
| 245 | `6-22 as read [?]` → `6-22` | SECOND-PASS Q2: Kannada agrees (ನಿ. ೬-೨೨) |
| 246 | `2-36-3 as read [?]` → `2-36-3` | SECOND-PASS Q2: Kannada agrees |
| 246 | `3-3-9 as read [?]` → `3-3-9` | SECOND-PASS Q2: Kannada agrees |
| 246 | `8-45-39 as read [?]` → `8-45-39` | SECOND-PASS Q2: Kannada agrees (೮-೪೫-೩೯); rest of the remark kept |
| 247 | `Va. 11 [?]"` → `Va. 11"` | SECOND-PASS Q2: Kannada p. 247 head reads ವ. ೧೧ |
| 247 | `clotted [?]]` → `clotted]` | SECOND-PASS Q2: Kannada p. 247 has the Sanskrit (ಋಜ್ರಾಶ್ವಗ್ರಹಣೇನ … ವಾರ್ಷಾಗಿರಾ ಲಕ್ಷ್ಯಂತೇ), agreeing with the English |
| 247 | `1-116-16 as read [?]` → `1-116-16` | SECOND-PASS Q2: Kannada agrees |
| 247 | `twenty-five [as read, ?] names of man (*Ni.* 2-2 as read [?])` → `twenty-five names of man (*Ni.* 3-7)` | SECOND-PASS Q1: Kannada p. 247: ೨೫ ಮನುಷ್ಯನಾಮಗಳಲ್ಲಿ … (೩-೭) |
| 247 | `8-6-24 as read [?]` → `8-6-24` | SECOND-PASS Q2: Kannada agrees |
| 248 | `7-95-2 as read [?]` → `7-95-2` | SECOND-PASS Q2: Kannada agrees |
| 248 | `6-20 as read [?]` → `6-20` | SECOND-PASS Q2: Kannada agrees |
| 248 | `6-21 and 22 as read [?]` → `6-21 and 22` | SECOND-PASS Q2: Kannada agrees |
| 248 | `6-23 as read [?]` → `6-23` | SECOND-PASS Q2: Kannada agrees |
| 249 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 250 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 250 | `printed pp. 250–[?]` → `printed pp. 250–256` | SECOND-PASS Q1: Kannada: Rik 17 ends (॥ ೧೭ ॥) on p. 256 |
| 250 | `see the note there [?])` → `see the note there)` | SECOND-PASS Q2: Kannada p. 250 reads ಪ್ರಷ್ಟಿಭಿಃ as the English says |
| 251 | `*[as read [?]])` → `*[as read])` | SECOND-PASS Q2: Kannada p. 251 reads ವೋಪಸರ್ಜನಸ್ಯ |
| 251 | ` Clotted rule-names are marked [?].` → `` | SECOND-PASS S3: doubt sentence only |
| 252 | `(*Ai. Brā.*, as printed; the numeral on p. 253 [?])` → `(*Ai. Brā.* 15-6)` | SECOND-PASS Q1: Kannada p. 253 gives the number (೧೫-೬) |
| 252 | `7-82-1 as read [?]` → `7-82-1` | SECOND-PASS Q2: Kannada agrees |
| 253 | `Va. 11 [?]"` → `Va. 11"` | SECOND-PASS Q2: Kannada p. 253 head reads ವ. ೧೧ |
| 253 | `10-68-1 as read [?];` → `10-68-1;` | SECOND-PASS Q2: Kannada agrees (೧೦-೬೮-೧) |
| 253 | `1[3?]-6 as read [?]` → `15-6` | SECOND-PASS Q1: Kannada p. 253 reads (ಇ. ಪತ್ರ. ೧೫-೬) |
| 253 | `6-69-1 as read [?]` → `6-69-1` | SECOND-PASS Q2: Kannada agrees |
| 253 | `[1?]15-6 as read [?]` → `15-6` | SECOND-PASS Q1: Kannada p. 253 reads ಐತರೇಯಬ್ರಾಹ್ಮಣದಲ್ಲಿ (೧೫-೬) |
| 253 | `4-2-3-10 as read [?]` → `4-2-3-10` | SECOND-PASS Q2: Kannada agrees |
| 253 | `is cited in part [?].)*` → `is cited in part.)*` | SECOND-PASS Q2: Kannada p. 253 gives the Śatapatha passage; English gloss agrees |
| 254 | `5-13-1 as read [?];` → `5-13-1;` | SECOND-PASS Q2: Kannada agrees (೫-೧೩-೧) |
| 254 | `4-15-7 [as read [?]]` → `4-15-7` | SECOND-PASS Q2: Kannada agrees (೪-೧೫-೭) |
| 254 | `(2-44-3-4 as read [?])` → `(2-44-3-4)` | SECOND-PASS Q2: Kannada agrees (೨-೪೪-೩-೪) |
| 254 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 256 | `printed pp. 256–[?]` → `printed pp. 256–261` | SECOND-PASS Q1: Kannada: Rik 18 ends (॥ ೧೮ ॥) on p. 261 |
| 257 | ` The Uṇādi numerals and the words marked [?] are clotted.` → `` | SECOND-PASS S3: doubt sentence only |
| 258 | `1-62-4 as read [?]` → `1-62-4` | SECOND-PASS Q2: Kannada agrees |
| 258 | `1-68-4 as read [?]` → `1-68-4` | SECOND-PASS Q2: Kannada agrees |
| 258 | `1-158-3 as read [?];` → `1-158-3;` | SECOND-PASS Q2: Kannada agrees (೧-೧೫೮-೩) |
| 258 | `2-19-3 as read [?]` → `7-62-2` | SECOND-PASS Q1: Kannada p. 258 reads ( ಋ. ಸಂ. ೭-೬೨-೨ ) |
| 259 | `Va. 11 [?]"` → `Va. 11"` | SECOND-PASS Q2: Kannada p. 259 head reads ವ. ೧೧ |
| 259 | `7-18-5/5?] as read [?]` → `7-18-5` | SECOND-PASS Q1: Kannada p. 259 reads (ಋ. ಸಂ. ೭-೧೮-೫) |
| 259 | `2-12-10 as read [?]` → `2-12-10` | SECOND-PASS Q2: Kannada agrees |
| 259 | `6-68-3 as read [?]` → `7-85-2` | SECOND-PASS Q1: Kannada p. 259 reads (ಋ. ಸಂ. ೭-೮೫-೨) |
| 260 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 261 | `Va. 11 [?]"` → `Va. 11"` | SECOND-PASS Q2: Kannada p. 261 head reads ವ. ೧೧ |
| 261 | `printed pp. 261–[?]` → `printed pp. 261–264` | SECOND-PASS Q1: Kannada: Rik 19 bhāṣya ends p. 262, grammar on pp. 263–264; Sūkta 100 ends p. 264 |
| 262 | ` The Pāṇini numerals and the words marked [?] are clotted.` → `` | SECOND-PASS S3: doubt sentence only |
| 263 | `Va. 11 [?]"` → `Va. 11"` | SECOND-PASS Q2: Kannada p. 263 head reads ವ. ೧೧ |
| 263 | `10-6-2 as read [?]` → `10-6-2` | SECOND-PASS Q2: Kannada agrees |
| 263 | `10-63-5 as read [?]` → `10-63-5` | SECOND-PASS Q2: Kannada agrees |
| 264 | `3-128 as read [?]` → `3-128` | SECOND-PASS Q2: Kannada p. 264 (ಬೃ. ದೇ. ೩-೧೨೮) |
| 264 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 265 | `Va. 11 [?]"` → `Va. 12"` | SECOND-PASS Q1: Kannada p. 265 head reads ವ. ೧೨ (its adhyāya numeral ೩ is a misprint for ೭) |
| 265 | `doubtful places [?]):**` → `doubtful places):**` | SECOND-PASS Q2: mark dropped; Sanskrit is derived data |
| 266 | `numerals as read, small [?])` → `numerals as read, small)` | SECOND-PASS Q2: Kannada p. 266 agrees (ಅಷ್ಟಕ ೧, ಅಧ್ಯಾಯ ೭, ವರ್ಗ ೧೨, ೧೩) |
| 266 | `printed pp. 266–[?]` → `printed pp. 266–271` | SECOND-PASS Q1: Kannada: Rik 101.1 ends on p. 271 (grammar pp. 270–271) |
| 267 | `Va. 12 [?]"` → `Va. 12"` | SECOND-PASS Q2: Kannada p. 267 head reads ವ. ೧೨ |
| 267 | `[from them] [?]` → `[from them]` | SECOND-PASS Q2: Kannada p. 267 has the same sense (ಪುತ್ರಾಣಾಮಪ್ಯನುತ್ಪತ್ತ್ಯರ್ಥಂ ಗರ್ಭಿಣೀಸ್ತಸ್ಯ ಭಾರ್ಯಾ ಅವಧೀತ್) |
| 267 | ` Several words are clotted and marked [?].` → `` | SECOND-PASS S3: doubt sentence only |
| 268 | `(*Ni.* 4-24?]1 as read [?])` → `(*Ni.* 4-24)` | SECOND-PASS Q1: Kannada p. 268 (ನಿ. ೪-೨೪) |
| 268 | `(*Ni.* 4-24[1?] as read [?])` → `(*Ni.* 4-24)` | SECOND-PASS Q1: Kannada p. 268 (ನಿ. ೪-೨೪) |
| 268 | `twenty-eight [as read, ?] names of food (*Ni.* 2-7 as read [?])` → `twenty-eight names of food (*Ni.* 3-9)` | SECOND-PASS Q1: Kannada p. 268: ೨೮ ಅನ್ನನಾಮಗಳಲ್ಲಿ … (ನಿ. ೩-೯) |
| 268 | `(*Ni.* 9-24?]4 as read [?])` → `(*Ni.* 9-24)` | SECOND-PASS Q1: Kannada p. 268 (ನಿ. ೯-೨೪) |
| 268 | `1-187-1 as read [?]` → `1-187-1` | SECOND-PASS Q2: Kannada agrees |
| 270 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 271 | `printed pp. 271–[?]` → `printed pp. 271–277` | SECOND-PASS Q1: Kannada: Rik 101.2 ends (॥ ೨ ॥) on p. 277 |
| 272 | `jahṛṣāṇena [?] |` → `jahṛṣāṇena |` | SECOND-PASS Q2: Kannada Pada p. 272 reads ಜಹೃಷಾಣೇನ |
| 272 | `the Pada* jahṛṣāṇena *[?])*` → `the Pada* jahṛṣāṇena*)*` | SECOND-PASS Q2: Kannada Saṃhitā reads ಜಾಹೃಷಾಣೇನ, Pada ಜಹೃಷಾಣೇನ |
| 272 | `*is read as* sakhyāya hvayāmahe *[?].)*` → `*is read as* sakhyāyāhvayāmahe*.)*` | SECOND-PASS Q1: Kannada p. 272 reads ಸಖ್ಯಾಯಾಹ್ವಯಾಮಹೇ (IAST by sp_sanskrit.py) |
| 273 | `Va. 12 [?]"` → `Va. 12"` | SECOND-PASS Q2: Kannada p. 273 head reads ವ. ೧೨ |
| 276 | `given as printed [?])` → `given as printed)` | SECOND-PASS Q2: Kannada p. 276 repeats the line with the same differences (ಉತೋ ಚಿದ್ಯ ಓಹತ ಅಂಡಾ …) |
| 276 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 277 | `Va. 12 [?]"` → `Va. 12"` | SECOND-PASS Q2: Kannada p. 277 head reads ವ. ೧೨ |
| 279 | `Va. 12 [?]"` → `Va. 12"` | SECOND-PASS Q2: Kannada p. 279 head reads ವ. ೧೨ |
| 279 | `4-19-2 as read [?]` → `4-19-2` | SECOND-PASS Q2: Kannada agrees |
| 279 | `4-21-10 as read [?]` → `4-21-10` | SECOND-PASS Q2: Kannada agrees |
| 279 | `3-305 as read [?]` → `3-30-5` | SECOND-PASS Q1: Kannada p. 279 reads (ಋ. ಸಂ. ೩-೩೦-೫) |
| 280 | `8-62-7 as read [?]` → `8-62-7` | SECOND-PASS Q2: Kannada agrees |
| 280 | `8-12-30 as read [?]` → `8-12-30` | SECOND-PASS Q2: Kannada agrees |
| 280 | `twenty-two [as read, ?] names of verbs of going (*Ni.* 2-[?] as read [?])` → `122 names of verbs of going (*Ni.* 3-9)` | SECOND-PASS Q1: Kannada p. 280: ೧೨೨ ಗತಿ ಕರ್ಮಗಳಲ್ಲಿ … (ನಿ. ೩-೯) |
| 280 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 281 | `printed pp. 281–[?]` → `printed pp. 281–286` | SECOND-PASS Q1: Kannada: Rik 101.4 ends (॥ ೪ ॥) on p. 286 |
| 284 | `the first word clotted in print [?])` → `the first word clotted in print)` | SECOND-PASS Q2: Kannada p. 284 reads ವೃತಂಚಯಃ, as the English |
| 285 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 286 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 286 | `printed pp. 286–[?]` → `printed pp. 286–290` | SECOND-PASS Q1: Kannada: Rik 101.5 ends (॥ ೫ ॥) on p. 290 |
| 287 | `[having laid them low] [?]` → `[having laid them low]` | SECOND-PASS Q2: Kannada p. 287: ಅಧರಾನ್ನಿಕೃಷ್ಣಾನ್ಕೃತ್ವಾನಾತಿರತ್ ಅವಧೀತ್, as the English |
| 288 | `3-8-8 as read [?]` → `8-3-6` | SECOND-PASS Q1: Kannada p. 288 reads (ಋ. ಸಂ. ೮-೩-೬) |
| 288 | `3-31-5 to 5 [print: 3-31-5 to 6, as read [?]]` → `3-31-5 to 7` | SECOND-PASS Q1: Kannada p. 288 reads (ಋ. ಸಂ. ೩-೩೧-೫ ರಿಂದ ೭) |
| 289 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 289 | `[Uṇ. Sū. 2-[?]41 as read, ?]` → `[Uṇ. Sū. 2-241]` | SECOND-PASS Q1: Kannada p. 289 reads (ಉ. ಸೂ. ೨-೨೪೧) |
| 290 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 290 | `[Pā. Sū. 8-2-[?]9 as read]` → `[Pā. Sū. 8-3-9]` | SECOND-PASS Q1: Kannada p. 290 reads (ಪಾ. ಸೂ. ೮-೩-೯) |
| 290 | `printed pp. 290–[?]` → `printed pp. 290–294` | SECOND-PASS Q1: Kannada: Rik 101.6 ends on p. 294 (grammar pp. 293–294) |
| 291 | ` Several words are clotted and marked [?].` → `` | SECOND-PASS S3: doubt sentence only |
| 292 | `1-103-5 as read [?]` → `1-103-5` | SECOND-PASS Q2: Kannada agrees |
| 292 | `6-24-3 as read [?]` → `6-24-3` | SECOND-PASS Q2: Kannada agrees |
| 293 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 294 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 294 | `[Uṇ. Sū. 2-[?]4 as read, ?]` → `[Pā. Sū. 3-2-174]` | SECOND-PASS Q1: Kannada p. 294: ಭಿಯಃ ಕ್ರುಕ್ಲುಕನೌ—(ಪಾ. ಸೂ. ೩-೨-೧೭೪) |
| 295 | `printed pp. 295–[?]` → `printed pp. 295–299` | SECOND-PASS Q1: Kannada: Rik 101.7 grammar ends p. 299 |
| 298 | `4-5[2?]-[?] as read [?]` → `4-52-5` | SECOND-PASS Q1: Kannada p. 298 reads (ಋ. ಸಂ. ೪-೫೨-೫) |
| 298 | `vistīrṇam asi vegaṃ vistārayatīty arthaḥ* [as printed, partly clotted [?]]` → `vistīrṇam api vegaṃ vistārayatīty arthaḥ*` | SECOND-PASS Q1: Kannada p. 298 reads ವಿಸ್ತೀರ್ಣಮಪಿ ವೇಗಂ ವಿಸ್ತಾರಯತೀತ್ಯರ್ಥಃ (IAST by sp_sanskrit.py) |
| 298 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 299 | `Va. 13 [?]"` → `Va. 13"` | SECOND-PASS Q2: Kannada p. 299 head reads ವ. ೧೩ |
| 299 | `printed pp. 299–[?]` → `printed pp. 299–302` | SECOND-PASS Q1: Kannada: Rik 101.8 ends (॥ ೮ ॥) on p. 302 |
| 300 | `"Maṃ. 1 A. 15 Sū. 100" [as the numeral reads; 101 is meant [?]]` → `"Maṃ. 1 A. 15 Sū. 101"` | SECOND-PASS Q1: Kannada p. 300 head reads ಸೂ ೧೦೧ |
| 300 | `curādi *[open class?, as read [?]],` → `curādi *,` | SECOND-PASS Q2: Kannada p. 300: ಮಾದಯಾಸೆ—ಮದ ತೃಪ್ತಿಯೋಗೇ ಧಾತು. ಚುರಾದಿ. |
| 300 | ` Some clauses are clotted and marked [?].` → `` | SECOND-PASS S3: doubt sentence only |
| 302 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 302 | `printed pp. 303–[?]` → `printed pp. 303–306` | SECOND-PASS Q1: Kannada: Rik 101.9 ends (॥ ೯ ॥) on p. 306 |
| 303 | `Va. 13 [?]"` → `Va. 13"` | SECOND-PASS Q2: Kannada p. 303 head reads ವ. ೧೩ |
| 304 | `8-62-7 as read [?]` → `8-62-7` | SECOND-PASS Q2: Kannada agrees |
| 305 | `3-41-3 [?])` → `3-41-3)` | SECOND-PASS Q2: Kannada p. 305 has (ಋ. ಸಂ. ೩-೪೧-೩) |
| 305 | `6-457-? [?]` → `6-45-7` | SECOND-PASS Q1: Kannada p. 305: ೫-೩೯-೫, ೬-೨೧-೬, ೬-೪೫-೭ |
| 305 | `3-46-5 [?],` → `3-46-5,` | SECOND-PASS Q2: Kannada p. 305: ೨-೧೮-೬, ೩-೪೬-೫, ೪-೨-೬, ೪-೧೩-೫ |
| 305 | `4-13-5 [?] and` → `4-13-5 and` | SECOND-PASS Q2: Kannada p. 305 agrees |
| 306 | `1-135-4-[?] as read [?]` → `1-135-4` | SECOND-PASS Q1: Kannada p. 306 reads (ಋ. ಸಂ. ೧-೧೩೫-೪) |
| 306 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 306 | `printed pp. 307–[?]` → `printed pp. 307–310` | SECOND-PASS Q1: Kannada: Rik 101.10 ends (॥ ೧೦ ॥) on p. 310 |
| 307 | `Va. 13 [?]"` → `Va. 13"` | SECOND-PASS Q2: Kannada p. 307 head reads ವ. ೧೩ |
| 308 | `6-17 as read [?]` → `6-17` | SECOND-PASS Q2: Kannada agrees (ನಿ. ೬-೧೭) |
| 308 | `1-9-3 as read [?]` → `1-9-3` | SECOND-PASS Q2: Kannada agrees |
| 310 | `numerals small and doubtful [?])` → `numerals small and doubtful)` | SECOND-PASS Q2: Kannada numerals are correct; doubt mark dropped |
| 311 | `Va. 13 [?]"` → `Va. 13"` | SECOND-PASS Q2: Kannada p. 311 head reads ವ. ೧೩ |
| 312 | `(*Ni.* 2-9 as read [?])` → `(*Ni.* 2-9)` | SECOND-PASS Q2: Kannada agrees (ನಿ. ೨-೯) |
| 312 | `1-164-9-[?]9 as read [?]` → `1-164-9` | SECOND-PASS Q1: Kannada p. 312 reads (ಋ. ಸಂ. ೧-೧೬೪-೯) |

### 2026-11-27 second pass, batch m386-535.tsv
| page | old → new | why |
|---|---|---|
| 312 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 101.11)** *(grammar page, noted briefly; ` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 101.11)** *(grammar page, noted briefly; ` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 313 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 313.)*` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 313.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 313 | `**Sāyaṇa's introduction to Sūkta 102 (Sanskrit in Kannada script; doubtful places [?]):**` → `**Sāyaṇa's introduction to Sūkta 102 (Sanskrit in Kannada script; doubtful places):**` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 313 | `- अष्टक १ · अध्याय ७ · वर्ग १४, १५ — *Aṣṭaka 1, Adhyāya 7, Vargas 14, 15* (numerals as rea` → `- अष्टक १ · अध्याय ७ · वर्ग १४, १५ — *Aṣṭaka 1, Adhyāya 7, Vargas 14, 15* (numerals as rea` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 314 | `## Rik 102.1 — printed pp. 314–[?]` → `## Rik 102.1 — printed pp. 314–318` | SECOND-PASS Q1: end page 318: the next Ṛk (printed from p. 319) starts after it |
| 314 | ` Several rule-names and the clause on accent are clotted and marked [?].` → `` | SECOND-PASS S3: doubt sentence only |
| 316 | `1-[?]4-8 as read [?]` → `1-26-8` | SECOND-PASS Q1: Kannada p. 316 reads (ಋ. ಸಂ. ೧-೨೬-೮) |
| 316 | `3-9 as read [?]` → `3-9` | SECOND-PASS Q2: Kannada p. 316 (ನಿ. ೩-೯), agreeing |
| 316 | `> (*Nirukta*, Daivatakāṇḍa, adhyāya 7, khaṇḍa 1–3 [as printed: "adhyāya 7, khaṇḍa 1-3"]; t` → `> (*Nirukta*, Daivatakāṇḍa, adhyāya 7, khaṇḍa 1–3 [as printed: "adhyāya 7, khaṇḍa 1-3"]; t` | SECOND-PASS Q2: Kannada p. 316 has the Nirukta reference (ನಿರುಕ್ತ, ದೈವತಕಾಂಡ, ಅಧ್ಯಾಯ ೭, ಖಂಡ ೧-೩), agreeing |
| 317 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.1)** *(grammar pages, begun on p. 317` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.1)** *(grammar pages, begun on p. 317` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 318 | `**Vyākaraṇa-prakriyā of Rik 102.1, concluded (grammar page, noted briefly; numerals small ` → `**Vyākaraṇa-prakriyā of Rik 102.1, concluded (grammar page, noted briefly; numerals small ` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 319 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 319.)*` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 319.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 319 | `## Rik 102.2 — printed pp. 319–[?]` → `## Rik 102.2 — printed pp. 319–323` | SECOND-PASS Q1: end page 323: the next Ṛk (printed from p. 324) starts after it |
| 320 | `, with doubtful places marked [?]` → `` | SECOND-PASS S3: doubt clause only; the grammar summary kept |
| 320 | `bhṛmṛdṛśi… [?]` → `bhṛmṛdṛśi…` | SECOND-PASS Q2: Kannada p. 320 reads ಭೃಮೃದೃಶೀತ್ಯಾದಿನಾತಚ್, agreeing |
| 321 | `> (*Ṛ. Saṃ.* 1-54-10 as read [?])` → `> (*Ṛ. Saṃ.* 1-54-10)` | SECOND-PASS Q2: Kannada p. 321 (ಋ. ಸಂ. ೧-೫೪-೧೦), agreeing |
| 322 | `> (*Ni.* 1-9 as read [?]; the last words clotted in print [?])` → `> (*Ni.* 1-9; the last words clotted in print)` | SECOND-PASS Q2: Kannada p. 322 (ನಿ. ೧-೯), agreeing |
| 322 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.2)** *(grammar page, noted briefly; n` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.2)** *(grammar page, noted briefly; n` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 322 | `Pā. Sū. 2-3-[?]3 as read]` → `Pā. Sū. 7-2-113]` | SECOND-PASS Q1: Kannada p. 322 reads ಹಲಿ ಲೋಪಃ—(ಪಾ. ಸೂ. ೭-೨-೧೧೩) |
| 322 | `*ādebhyastāt* [Pā. Sū. 3-4-[?]4 as read, i.e. *adabhyastāt*, Pā. Sū. 7-1-4]` → `*adabhyastāt* [Pā. Sū. 7-1-4]` | SECOND-PASS Q1: Kannada p. 322 reads ಅದಭ್ಯಸ್ತಾತ್—(ಪಾ. ಸೂ. ೭-೧-೪); IAST by sp_sanskrit.py |
| 324 | `## Rik 102.3 — printed pp. 324–[?]` → `## Rik 102.3 — printed pp. 324–327` | SECOND-PASS Q1: end page 327: the next Ṛk (printed from p. 327) starts after it |
| 324 | `preraya *[?].)*` → `preraya*.)*` | SECOND-PASS Q2: Kannada p. 324 reads ಪ್ರೇರಯ (preraya), agreeing |
| 325 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 325.)*` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 325.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 326 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.3)** *(grammar pages, pp. 326–327, no` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.3)** *(grammar pages, pp. 326–327, no` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 327 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 327.)*` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 327.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 327 | `## Rik 102.4 — printed pp. 327–[?]` → `## Rik 102.4 — printed pp. 327–330` | SECOND-PASS Q1: end page 330: the next Ṛk (printed from p. 330) starts after it |
| 329 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 329.)*` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 329.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 329 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.4)** *(grammar page, noted briefly; n` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.4)** *(grammar page, noted briefly; n` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 330 | `**Vyākaraṇa-prakriyā of Rik 102.4, concluded (grammar page, noted briefly; numerals small ` → `**Vyākaraṇa-prakriyā of Rik 102.4, concluded (grammar page, noted briefly; numerals small ` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 330 | `## Rik 102.5 — printed pp. 330–[?]` → `## Rik 102.5 — printed pp. 330–332` | SECOND-PASS Q1: end page 332: the next Ṛk (printed from p. 333) starts after it |
| 331 | `asmākam eva *[?];` → `asmākam eva*;` | SECOND-PASS Q2: Kannada p. 331 has ಅಸ್ಮಾಕಂ … ಸ್ಮಾಸ್ಮಾಕಮೇವ, agreeing |
| 331 | `ktini *[?].)*` → `ktini*.)*` | SECOND-PASS Q2: Kannada p. 332 grammar has ಸ್ತ್ರೀಯಾಂ ಕ್ತಿನ್, supporting ktin |
| 332 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.5)** *(grammar page, noted briefly; n` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.5)** *(grammar page, noted briefly; n` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 333 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 333.)*` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 333.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 333 | `## Rik 102.6 — printed pp. 333–[?]` → `## Rik 102.6 — printed pp. 333–337` | SECOND-PASS Q1: end page 337: the next Ṛk (printed from p. 337) starts after it |
| 334 | `partly clotted [?];` → `partly clotted;` | SECOND-PASS Q2: Kannada p. 334 has the word ಅನುಕ್ತಸಮುಚ್ಚಯಾರ್ಥತ್ವಾತ್, agreeing |
| 335 | `1-145-1 as read [?]` → `1-152` | SECOND-PASS Q1: Kannada p. 334 prints (ಋ. ಸಂ. ೧-೧೫೨), applied as printed |
| 335 | `> (*Ṛ. Saṃ.* 10-28-11 [?]; the print's first word clotted [?])` → `> (*Ṛ. Saṃ.* 10-28-11; the print's first word clotted)` | SECOND-PASS Q2: Kannada p. 334 (ಋ. ಸಂ. ೧೦-೨೮-೧೧), agreeing |
| 336 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 1.4)** *(grammar pages, pp. 336–337, note` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 1.4)** *(grammar pages, pp. 336–337, note` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 336 | `Uṇ. Sū. 1-[?]2 as read, ?]` → `Uṇ. Sū. 1-27]` | SECOND-PASS Q1: Kannada p. 336 reads (ಉ. ಸೂ. ೧-೨೭) |
| 337 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 337. A printer'` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 337. A printer's si` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 337 | `## Rik 102.7 — printed pp. 337–[?]` → `## Rik 102.7 — printed pp. 337–341` | SECOND-PASS Q1: end page 341: the next Ṛk (printed from p. 342) starts after it |
| 339 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 339.)*` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 339.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 339 | `2-[7?] as read [?]` → `3-9` | SECOND-PASS Q1: Kannada p. 339 reads (ನಿ. ೩-೯) |
| 340 | `> (*Ṛ. Saṃ.* 2-19-6 as read [?]; as quoted on p. 274)` → `> (*Ṛ. Saṃ.* 2-19-6; as quoted on p. 274)` | SECOND-PASS Q2: Kannada p. 340 (ಋ. ಸಂ. ೨-೧೯-೬), agreeing |
| 340 | `> (*Ṛ. Saṃ.* 6-47-2 as read [?]; the print's second word clotted [?])` → `> (*Ṛ. Saṃ.* 6-47-2; the print's second word clotted)` | SECOND-PASS Q2: Kannada p. 340 (ಋ. ಸಂ. ೬-೪೭-೨), agreeing |
| 340 | `> (*Ṛ. Saṃ.* 2-20-7 as read [?])` → `> (*Ṛ. Saṃ.* 2-20-7)` | SECOND-PASS Q2: Kannada p. 340 (ಋ. ಸಂ. ೨-೨೦-೭), agreeing |
| 340 | `861-10; 6-16-14; 8-61-8; 2-6-[?] [?] and others` → `8-61-10; 6-16-14; 8-61-8; 7-6-2 and others` | SECOND-PASS Q1: Kannada p. 340 reads ೫-೩೦-೧೧ ; ೮-೧-೮ ; ೮-೬೧-೧೦ ; ೬-೧೬-೧೪ ; ೮-೬೧-೮ ; ೭-೬-೨ (the unmarked 861-10 set right in the same list) |
| 340 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.7)** *(grammar pages, pp. 340–341, no` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.7)** *(grammar pages, pp. 340–341, no` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 341 | `*(Running head: left "A. 1 A. 7 Va. 14 [?]"; centre "Ṛgvedasaṃhitā"; right 341.)*` → `*(Running head: left "A. 1 A. 7 Va. 14"; centre "Ṛgvedasaṃhitā"; right 341.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 342 | `## Rik 102.8 — printed pp. 342–[?]` → `## Rik 102.8 — printed pp. 342–346` | SECOND-PASS Q1: end page 346: the next Ṛk (printed from p. 347) starts after it |
| 342 | `read* tīn lokān *[?];` → `read* trīn lokān*;` | SECOND-PASS Q1: Kannada p. 342 reads ತ್ರೀನ್ ಲೋಕಾನ್ (IAST by sp_sanskrit.py) |
| 342 | `reading of a clotted phrase [?].)*` → `reading of* divyādityākhyam*.)*` | SECOND-PASS Q1: Kannada p. 342 reads ದಿವ್ಯಾದಿತ್ಯಾಖ್ಯಮ್ (IAST by sp_sanskrit.py) |
| 343 | `*(Running head: left "A. 1 A. 7 Va. 15 [?]"; centre "Ṛgvedasaṃhitā"; right 343.)*` → `*(Running head: left "A. 1 A. 7 Va. 15"; centre "Ṛgvedasaṃhitā"; right 343.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 343 | `in outline only [?].)*` → `in outline only.)*` | SECOND-PASS Q2: Kannada p. 343 has the passage; doubt mark only |
| 344 | `[of a hundred-fold? as read [?]]` → `[each of three threads]` | SECOND-PASS Q1: Kannada p. 344: ಮೂರು ಹುರಿಗಳನ್ನು … (ಮೂರೆಳೆಯಿಂದ ಕೂಡಿದ) |
| 344 | `2-278 as read [?]` → `2-27-8` | SECOND-PASS Q1: Kannada p. 344 reads (ಋ. ಸಂ. ೨.೨೭-೮) |
| 345 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.8)** *(grammar pages, begun on p. 345` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.8)** *(grammar pages, begun on p. 345` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 346 | `**Vyākaraṇa-prakriyā of Rik 102.8, continued from p. 345 (grammar page, noted briefly; num` → `**Vyākaraṇa-prakriyā of Rik 102.8, continued from p. 345 (grammar page, noted briefly; num` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 347 | `*(Running head: left "A. 1 A. 7 Va. 15 [?]"; centre "Ṛgvedasaṃhitā"; right 347.)*` → `*(Running head: left "A. 1 A. 7 Va. 15"; centre "Ṛgvedasaṃhitā"; right 347.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 347 | `## Rik 102.9 — printed pp. 347–[?]` → `## Rik 102.9 — printed pp. 347–350` | SECOND-PASS Q1: end page 350: the next Ṛk (printed from p. 350) starts after it |
| 348 | ` The words clotted in the print are marked [?].` → `` | SECOND-PASS S3: doubt sentence only |
| 348 | `2-[?]7 as read [?]` → `3-9` | SECOND-PASS Q1: Kannada p. 348 reads (ನಿ. ೩-೯) |
| 349 | `"— in giving the derivation, says, *vidatheṣu kārū* — *yajñeṣu kartārau ṛtvijau*: 'in the ` → `"— in giving the derivation, says, *vidatheṣu kārū* — *yajñeṣu kartārau ṛtvijau*: 'in the ` | SECOND-PASS Q2: Kannada p. 349 (ನಿ. ೮-೧೨), agreeing |
| 349 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.9)** *(grammar page, begun on p. 349,` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.9)** *(grammar page, begun on p. 349,` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 350 | `**Vyākaraṇa-prakriyā of Rik 102.9, continued from p. 349 (grammar page, noted briefly; num` → `**Vyākaraṇa-prakriyā of Rik 102.9, continued from p. 349 (grammar page, noted briefly; num` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 350 | `## Rik 102.10 — printed pp. 350–[?]` → `## Rik 102.10 — printed pp. 350–353` | SECOND-PASS Q1: end page 353: the next Ṛk (printed from p. 354) starts after it |
| 351 | `*(Running head: left "A. 1 A. 7 Va. 15 [?]"; centre "Ṛgvedasaṃhitā"; right 351.)*` → `*(Running head: left "A. 1 A. 7 Va. 15"; centre "Ṛgvedasaṃhitā"; right 351.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 351 | `halyaghoḥ *[?].)*` → `halyaghoḥ*.)*` | SECOND-PASS Q2: Kannada p. 351 reads ಈ ಹಲ್ಯಘೋಃ, agreeing |
| 351 | `halyaghoḥ *[?];` → `halyaghoḥ*;` | SECOND-PASS Q2: Kannada p. 351 reads ಈ ಹಲ್ಯಘೋಃ, agreeing |
| 352 | `4-[?]3)` → `4-15)` | SECOND-PASS Q1: Kannada p. 352 reads (ನಿ. ೪-೧೫) |
| 352 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.10)** *(grammar pages, pp. 352–353, n` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 102.10)** *(grammar pages, pp. 352–353, n` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 353 | `*(Running head: left "A. 1 A. 7 Va. 15 [?]"; centre "Ṛgvedasaṃhitā"; right 353. A printer'` → `*(Running head: left "A. 1 A. 7 Va. 15"; centre "Ṛgvedasaṃhitā"; right 353. A printer's si` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 355 | `**Sāyaṇa's introduction to Sūkta 103 (Sanskrit in Kannada script; doubtful places [?]):**` → `**Sāyaṇa's introduction to Sūkta 103 (Sanskrit in Kannada script; doubtful places):**` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 356 | `- अष्टक १ · अध्याय ७ · वर्ग १६, १७ — *Aṣṭaka 1, Adhyāya 7, Vargas 16, 17* (numerals as rea` → `- अष्टक १ · अध्याय ७ · वर्ग १६, १७ — *Aṣṭaka 1, Adhyāya 7, Vargas 16, 17* (numerals as rea` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 356 | `## Rik 103.1 — printed pp. 356–[?]` → `## Rik 103.1 — printed pp. 356–362` | SECOND-PASS Q1: end page 362: the next Ṛk (printed from p. 362) starts after it |
| 359 | `> (*Ṛ. Saṃ.* 1-111-2; the first two syllables of the Ṛk are not clear [?])` → `> (*Ṛ. Saṃ.* 1-111-2; the first two syllables of the Ṛk are not clear)` | SECOND-PASS Q2: Kannada p. 359 has the Ṛk with (ಋ. ಸಂ. ೧-೧೧೧-೨), agreeing |
| 361 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.1)** *(grammar pages, pp. 361–362, no` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.1)** *(grammar pages, pp. 361–362, no` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 362 | `**Vyākaraṇa-prakriyā of Rik 103.1, concluded (grammar page, noted briefly; numerals small ` → `**Vyākaraṇa-prakriyā of Rik 103.1, concluded (grammar page, noted briefly; numerals small ` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 362 | `## Rik 103.2 — printed pp. 362–[?]` → `## Rik 103.2 — printed pp. 362–368` | SECOND-PASS Q1: end page 368: the next Ṛk (printed from p. 368) starts after it |
| 363 | ` The sūtra numerals and some clauses are clotted and marked [?].` → `` | SECOND-PASS S3: doubt sentence only |
| 364 | `*Ahiṃ ahan* — the word *ahi* is read among the names of cloud (*Ni.* 2-21 as read [?]) and` → `*Ahiṃ ahan* — the word *ahi* is read among the names of cloud (*Ni.* 2-21) and among the n` | SECOND-PASS Q2: Kannada p. 364 (ನಿ. ೨-೨೧; ನಿ. ೨-೨೩), agreeing |
| 365 | `> (*Bṛ. De.* 5-166 as read [?])` → `> (*Bṛ. De.* 5-166)` | SECOND-PASS Q2: Kannada p. 365 (ಬೃ. ದೇ. ೫-೧೬೬), agreeing |
| 365 | `*Rauhiṇam* — the word *rauhiṇa* is read also among the names of cloud (*Ni.* 2-21 as read ` → `*Rauhiṇam* — the word *rauhiṇa* is read also among the names of cloud (*Ni.* 2-21); here t` | SECOND-PASS Q2: Kannada p. 365 (ನಿ. ೨-೨೧), agreeing |
| 366 | `> (*Ṛ. Saṃ.* 4-18-9; the first words clotted in print [?])` → `> (*Ṛ. Saṃ.* 4-18-9; the first words clotted in print)` | SECOND-PASS Q2: Kannada p. 366 (ಋ. ಸಂ. ೪-೧೮-೯), agreeing |
| 366 | `*Śacībhiḥ* — since the word *śacī* is read among the names of action (*Ni.* 3-1 as read [?` → `*Śacībhiḥ* — since the word *śacī* is read among the names of action (*Ni.* 3-1) and also ` | SECOND-PASS Q2: Kannada p. 366 (ನಿ. ೩-೧; ನಿ. ೩-೧೩), agreeing |
| 366 | `*Maghavā* — *dhanavān indraḥ*: since the word *magha* is read among the names of wealth (*` → `*Maghavā* — *dhanavān indraḥ*: since the word *magha* is read among the names of wealth (*` | SECOND-PASS Q2: Kannada p. 366 (ನಿ. ೩-೯), agreeing |
| 366 | `> (*Śat. Brā.* 14-1-1-13; some words clotted in print [?])` → `> (*Śat. Brā.* 14-1-1-13; some words clotted in print)` | SECOND-PASS Q2: Kannada p. 366 (ಶ. ಬ್ರಾ. ೧೪-೧-೧-೧೩), agreeing |
| 367 | `*(Running head: left "A. 1 A. 7 Va. 16 [?]"; centre "Ṛgvedasaṃhitā"; right 367.)*` → `*(Running head: left "A. 1 A. 7 Va. 16"; centre "Ṛgvedasaṃhitā"; right 367.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 367 | `> (*Ṛ. Saṃ.* 7-99-5 as read [?])` → `> (*Ṛ. Saṃ.* 7-99-5)` | SECOND-PASS Q2: Kannada p. 367 (ಋ. ಸಂ. ೭-೯೯-೫), agreeing |
| 367 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.2)** *(grammar pages, pp. 367–368, no` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.2)** *(grammar pages, pp. 367–368, no` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 368 | `## Rik 103.3 — printed pp. 368–[?]` → `## Rik 103.3 — printed pp. 368–373` | SECOND-PASS Q1: end page 373: the next Ṛk (printed from p. 373) starts after it |
| 369 | `*(Running head: left "A. 1 A. 7 Va. 16 [?]"; centre "Ṛgvedasaṃhitā"; right 369. A printer'` → `*(Running head: left "A. 1 A. 7 Va. 16"; centre "Ṛgvedasaṃhitā"; right 369. A printer's si` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 370 | `"— gives for the word *bharmaṇe* the sense *bharaṇāya*, 'for bearing, for nourishing' (*Ni` → `"— gives for the word *bharmaṇe* the sense *bharaṇāya*, 'for bearing, for nourishing' (*Ni` | SECOND-PASS Q2: Kannada p. 370 (ನಿ. ೭-೨೫), agreeing |
| 371 | `> (*Ṛ. Saṃ.* 2-13-11 as read [?])` → `> (*Ṛ. Saṃ.* 2-13-11)` | SECOND-PASS Q2: Kannada p. 371 (ಋ. ಸಂ. ೨-೧೩-೧೧), agreeing |
| 372 | `*Hetim* — *hetir hanteḥ* (*Ni.* 6-3): the word is derived from the root *han*, which gives` → `*Hetim* — *hetir hanteḥ* (*Ni.* 6-3): the word is derived from the root *han*, which gives` | SECOND-PASS Q2: Kannada p. 372 (ನಿ. ೩-೧೧), agreeing |
| 372 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.3)** *(grammar pages, pp. 372–373, no` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.3)** *(grammar pages, pp. 372–373, no` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 372 | `Grammar pages, noted briefly. They treat: *jātobharmā* (root *janī prādurbhāve*; *ḍa* by *` → `Grammar pages, noted briefly. They treat: *jātobharmā* (root *janī prādurbhāve*; *ḍa* by *` | SECOND-PASS Q2: Kannada p. 372 reads ಜಾತೂರ್, agreeing |
| 373 | `*(Running head: left "A. 1 A. 7 Va. 16 [?]"; centre "Ṛgvedasaṃhitā"; right 373.)*` → `*(Running head: left "A. 1 A. 7 Va. 16"; centre "Ṛgvedasaṃhitā"; right 373.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 373 | `## Rik 103.4 — printed pp. 373–[?]` → `## Rik 103.4 — printed pp. 373–378` | SECOND-PASS Q1: end page 378: the next Ṛk (printed from p. 378) starts after it |
| 374 | `nāmakaṃ *at the head is the print's gloss on* nāma *[?].)*` → `nāmakaṃ *at the head is the print's gloss on* nāma*.)*` | SECOND-PASS Q2: Kannada p. 374 has ನಾಮ ಶತ್ರೂಣಾಂ ನಾಮಕಂ at the head, agreeing |
| 375 | `*(Running head: left "A. 1 A. 7 Va. 16 [?]"; centre "Ṛgvedasaṃhitā"; right 375.)*` → `*(Running head: left "A. 1 A. 7 Va. 16"; centre "Ṛgvedasaṃhitā"; right 375.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 377 | `*(Running head: left "A. 1 A. 7 Va. 16 [?]"; centre "Ṛgvedasaṃhitā"; right 377.)*` → `*(Running head: left "A. 1 A. 7 Va. 16"; centre "Ṛgvedasaṃhitā"; right 377.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 377 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.4)** *(grammar pages, begun on p. 377` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.4)** *(grammar pages, begun on p. 377` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 378 | `**Vyākaraṇa-prakriyā of Rik 103.4, concluded (grammar page, noted briefly; numerals small ` → `**Vyākaraṇa-prakriyā of Rik 103.4, concluded (grammar page, noted briefly; numerals small ` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 378 | `## Rik 103.5 — printed pp. 378–[?]` → `## Rik 103.5 — printed pp. 378–383` | SECOND-PASS Q1: end page 383: the next Ṛk (printed from p. 383) starts after it |
| 379 | `*(Running head: left "A. 1 A. 7 Va. 16 [?]"; centre "Ṛgvedasaṃhitā"; right 379.)*` → `*(Running head: left "A. 1 A. 7 Va. 16"; centre "Ṛgvedasaṃhitā"; right 379.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 379 | `*(The print's* śrad dattana *at the second occurrence is* śrad dhattana*; read as the Saṃh` → `*(The print's* śrad dattana *at the second occurrence is* śrad dhattana*; read as the Saṃh` | SECOND-PASS Q2: Kannada p. 378 reads ಧತ್ತನ, agreeing |
| 382 | `80-1; the first words of the line are clotted [?]` → `8-80-1; the first words of the line are clotted` | SECOND-PASS Q1: Kannada p. 382 reads (ಋ. ಸಂ. ೮-೮೦-೧) |
| 382 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.5)** *(grammar pages, pp. 382–383, no` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.5)** *(grammar pages, pp. 382–383, no` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 383 | `*(Running head: left "A. 1 A. 7 Va. 16 [?]"; centre "Ṛgvedasaṃhitā"; right 383.)*` → `*(Running head: left "A. 1 A. 7 Va. 16"; centre "Ṛgvedasaṃhitā"; right 383.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 383 | `## Rik 103.6 — printed pp. 383–[?]` → `## Rik 103.6 — printed pp. 383–386` | SECOND-PASS Q1: end page 386: the next Ṛk (printed from p. 386) starts after it |
| 384 | `*(The grammatical tail is characterized:* ādṛtya *(root* dṛ *'to respect' with* ā*; the* k` → `*(The grammatical tail is characterized:* ādṛtya *(root* dṛ *'to respect' with* ā*; the* k` | SECOND-PASS Q2: Kannada p. 384 (ಪಾ. ೫-೨-೮೯), agreeing |
| 385 | `*(Running head: left "A. 1 A. 7 Va. 16 [?]"; centre "Ṛgvedasaṃhitā"; right 385. A printer'` → `*(Running head: left "A. 1 A. 7 Va. 16"; centre "Ṛgvedasaṃhitā"; right 385. A printer's si` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 385 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.6)** *(grammar pages, begun on p. 385` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.6)** *(grammar pages, begun on p. 385` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 386 | `**Vyākaraṇa-prakriyā of Rik 103.6, concluded from p. 385 (grammar page, noted briefly; num` → `**Vyākaraṇa-prakriyā of Rik 103.6, concluded from p. 385 (grammar page, noted briefly; num` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 386 | `## Rik 103.7 — printed pp. 386–[?]` → `## Rik 103.7 — printed pp. 386–390` | SECOND-PASS Q1: end page 390: the next Ṛk (printed from p. 390) starts after it |
| 387 | `*(Running head: left "A. 1 A. 7 Va. 17 [?]"; centre "Ṛgvedasaṃhitā"; right 387.)*` → `*(Running head: left "A. 1 A. 7 Va. 17"; centre "Ṛgvedasaṃhitā"; right 387.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 389 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.7)** *(grammar pages, begun on p. 389` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.7)** *(grammar pages, begun on p. 389` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 390 | `**Vyākaraṇa-prakriyā of Rik 103.7, concluded (grammar page, noted briefly; numerals small ` → `**Vyākaraṇa-prakriyā of Rik 103.7, concluded (grammar page, noted briefly; numerals small ` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 391 | `*(Running head: left "A. 1 A. 7 Va. 17 [?]"; centre "Ṛgvedasaṃhitā"; right 391.)*` → `*(Running head: left "A. 1 A. 7 Va. 17"; centre "Ṛgvedasaṃhitā"; right 391.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 393 | `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.8)** *(grammar pages, begun on p. 393` → `**॥ व्याकरणप्रक्रिया ॥ — Vyākaraṇa-prakriyā (Rik 103.8)** *(grammar pages, begun on p. 393` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 393 | `Grammar page, noted briefly. It treats: *śuṣṇam* (root *śuṣa śoṣaṇe*; since the causative ` → `Grammar page, noted briefly. It treats: *śuṣṇam* (root *śuṣa śoṣaṇe*; since the causative ` | SECOND-PASS Q2: Kannada p. 393 (ಉ. ಸೂ. ೩-೨೯೨), agreeing |
| 394 | `**Vyākaraṇa-prakriyā of Rik 103.8, concluded from p. 393 (grammar page, noted briefly; num` → `**Vyākaraṇa-prakriyā of Rik 103.8, concluded from p. 393 (grammar page, noted briefly; num` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 394 | `Uṇ. Sū. 4-[?]4 as read, ?]` → `Uṇ. Sū. 4-534]` | SECOND-PASS Q1: Kannada p. 394 reads (ಉ. ಸೂ. ೪-೫೩೪) |
| 394 | `**Sāyaṇa's introduction to Sūkta 104 (Sanskrit in Kannada script; doubtful places [?]):**` → `**Sāyaṇa's introduction to Sūkta 104 (Sanskrit in Kannada script; doubtful places):**` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 394 | `The print's first words are read* yonir ity *and the numeral-word as* anarcam *[for* navar` → `The first words are read* yonir ity*, the numeral-word* navarcam *('of nine Ṛks') and the ` | SECOND-PASS Q1: Kannada p. 394 reads ಯೋನಿರಿತಿ ನವರ್ಚಮ್ … ಯೋನಿರ್ನವೇತ್ಯನುಕ್ರಾಂತಂ |
| 395 | `*(Running head: left "A. 1 A. 7 Va. 18 [?]"; centre "Ṛgvedasaṃhitā"; right 395.)*` → `*(Running head: left "A. 1 A. 7 Va. 18"; centre "Ṛgvedasaṃhitā"; right 395.)*` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
| 395 | `- अष्टक १ · अध्याय ७ · वर्ग १८, १९ — *Aṣṭaka 1, Adhyāya 7, Vargas 18, 19* (numerals as rea` → `- अष्टक १ · अध्याय ७ · वर्ग १८, १९ — *Aṣṭaka 1, Adhyāya 7, Vargas 18, 19* (numerals as rea` | SECOND-PASS Q2: doubt mark only on a note (heading, running head or numerals remark); Kannada page has the text |
