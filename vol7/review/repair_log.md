
- **Nov 17 2026, glosses of quoted passages replaced by the marker `**GLOSS**`** (user: glosses are to come from our own edition, requirement B3.5): 209 labelled glosses in exact forms replaced whole by `tools/rv/gloss_marker.py 7 --write`; every removed gloss is kept in `review/glosses_removed.tsv` (line, form, text); 41 labelled lines in other forms left unchanged and listed in `review/glosses_left.tsv`. Checked: 682 changes of all volumes listed before writing, 30 read before and after, none damaged; marker count equals removed rows.
- 2026-11-18: tools/rv/refs_apply.py: reference names made uniform by the one list (rv/references.tsv), numbers untouched: en deva 122, en latin 720, en latin-twin 28; every change is a row of review/refs_applied.tsv.
- 2026-11-18: numeral_drop_q_same.py (Nov 18 alignment Vol7_file_vs_md_Nov18.xlsx): [?] dropped on 7 numerals (7 tokens) whose digits equal the aligned file row; log numerals/numeral_drop_q_same_Nov18.applied.tsv.
- 2026-11-18: numeral_apply_different.py --min-ctx=0.8 --min-score=0.85 --exclude-lines=2788 (alignment of Nov 18): 2 tokens changed to the file's value (md lines 12708 1-113-11 -> 1-113-3, 12745 1-113-8 [?] -> 1-113-11); read all 11 rows of equal part count, distance < 4 and context >= 0.8 first: at least 6 of them joined different references (context score alone is not reliable), so the extra score threshold was added; 5-2-5 -> 5-2-51 (line 2788) left alone (file reads the danda as 1); log numerals/numeral_apply_different_Nov18.applied.tsv.
- 2026-11-18: list for the user, nothing applied: numerals/Vol7_for_user_Nov18.tsv (192 DIFFERENT file rows not applied with the reason, 261 md numerals still [?] with no aligned file row and the closest unmatched file rows; 413 NOT FOUND file rows are only in the sheet 'file rows vs md' of Vol7_file_vs_md_Nov18.xlsx).

- **Nov 18 2026, labelled glosses in further forms replaced by the marker `**GLOSS**`** (gloss session, `docs/GLOSS_PROMPT.md` step 1): 39 by `tools/rv/gloss_marker.py 7 --write` after the forms left over on Nov 17 were added to the shared script (label and quotation inside a longer remark or after a dash, numbered lists, glosses in single quotation marks, `(Mine, tentative.)` after the quotation); every removed gloss is in `review/glosses_removed.tsv`. 2 labelled lines left in `review/glosses_left.tsv`: remarks (not glosses), our translations of the bhāṣya's introduction, and glosses whose label stands after a longer quoted passage (a reading is needed). Checked: all 243 script changes of Vols 3–8 read before writing (removed text with the text before and after it), the results re-read at 45 places; by script on every changed line: markers added = log rows, Devanagari and Kannada letters unchanged, brackets, quotation marks and italics balanced, no empty brackets, no space before a stop. Damaged: 0 (four faults of the new forms were found in the dry runs and corrected before the final write).
- 2026-11-19: tools/rv/refs_apply.py: reference names made uniform by the one list (rv/references.tsv), numbers untouched: en latin 1; every change is a row of review/refs_applied.tsv.

### 2026-11-27 qmark_strip.py: BLOCK 163 marks removed from 96 Sanskrit-block lines (derived data, K9); BARE 12 boilerplate remark lines removed (13 marks); OTHER 1763 marks left

### 2026-11-27 second pass, batch m12-161.tsv
| page | old → new | why |
|---|---|---|
| 3 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.3 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 5 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.5 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 7 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.7 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 9 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.9 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 11 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.11 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 13 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.13 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 15 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.15 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 17 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.17 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 19 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 1"` | SECOND-PASS Q1: running head of Kannada p.19 reads ಅ. ೧. ಅ. ೬. ವ. 1 (Varga 1) |
| 21 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 2"` | SECOND-PASS Q1: running head of Kannada p.21 reads ಅ. ೧. ಅ. ೬. ವ. 2 (Varga 2) |
| 23 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 2"` | SECOND-PASS Q1: running head of Kannada p.23 reads ಅ. ೧. ಅ. ೬. ವ. 2 (Varga 2) |
| 25 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 2"` | SECOND-PASS Q1: running head of Kannada p.25 reads ಅ. ೧. ಅ. ೬. ವ. 2 (Varga 2) |
| 27 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 2"` | SECOND-PASS Q1: running head of Kannada p.27 reads ಅ. ೧. ಅ. ೬. ವ. 2 (Varga 2) |
| 29 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 2"` | SECOND-PASS Q1: running head of Kannada p.29 reads ಅ. ೧. ಅ. ೬. ವ. 2 (Varga 2) |
| 31 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 2"` | SECOND-PASS Q1: running head of Kannada p.31 reads ಅ. ೧. ಅ. ೬. ವ. 2 (Varga 2) |
| 33 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.33 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 35 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.35 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 37 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.37 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 39 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.39 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 41 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.41 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 43 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.43 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 45 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.45 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 49 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.49 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 51 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.51 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 53 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 3"` | SECOND-PASS Q1: running head of Kannada p.53 reads ಅ. ೧. ಅ. ೬. ವ. 3 (Varga 3) |
| 55 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.55 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 57 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.57 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 59 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.59 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 61 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.61 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 63 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.63 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 65 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.65 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 67 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.67 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 69 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.69 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 71 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.71 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 73 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.73 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 75 | `Adhyāya 6, Varga [?]"` → `Adhyāya 6, Varga 4"` | SECOND-PASS Q1: running head of Kannada p.75 reads ಅ. ೧. ಅ. ೬. ವ. 4 (Varga 4) |
| 3 | `"na cānyatarasyām" [as read, [?]]` → `"nṛ cānyatarasyām"` | SECOND-PASS Q1: Kannada p.3 reads ನೃ ಚಾನ್ಯತರಸ್ಯಾಮ್ (nṛ cānyatarasyām) |
| 10 | `(as read, the clause is compressed [?])` → `(as read, the clause is compressed)` | SECOND-PASS Q2: Kannada p.10 has the same compressed clause (ಹನಶ್ಚ ದಧಶ್ಚೇತಿ …); no place in doubt |
| 11 | `(Ni. [2-17] [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.11: ಅಜಯಃ — ಯುದ್ಧಗಳು (ನಿ. ೩-೯) |
| 11 | `(the print's reasoning is compressed [?])` → `(the print's reasoning is compressed)` | SECOND-PASS Q2: Kannada p.11 has the reasoning as continuous text; remark about the scan, no place in doubt |
| 15 | `(Ni. [?-?] [?]). Here food means` → `(Ni. 4-9). Here food means` | SECOND-PASS Q1: Kannada p.15: ಅನುಷ್ವಧಂ ಅನ್ವನ್ನಂ … (ನಿ. ೪-೯) |
| 15 | `(Ni. [?-?] [?]). Though` → `(Ni. 3-9). Though` | SECOND-PASS Q1: Kannada p.15: ಉಪಾಕಯೋಃ—ಉಪಾಕವೆಂದರೆ ಸಮೀಪ (ನಿ. ೩-೯) |
| 15 | ` (Pā. Sū. 2-4-39 [?])` → `` | SECOND-PASS S3: Kannada p.15 names the sūtra ಬಹುಲಂ ಛಂದಸಿ without a number |
| 15 | `; sūtra numerals tentative [?].)` → `.)` | SECOND-PASS Q2: after q34 every dashed numeral of the English page occurs in the Kannada pages 14-16 (set check) |
| 24 | `; sūtra numerals tentative [?].*` → `.*` | SECOND-PASS Q2: set check: every dashed numeral of the English page 24 occurs in the Kannada pages 23-25 |
| 28 | `; sūtra numerals tentative [?].*` → `.*` | SECOND-PASS Q2: set check: every dashed numeral of the English page 28 occurs in the Kannada pages 27-29 |
| 49 | `; sūtra numerals tentative [?].*` → `.*` | SECOND-PASS Q2: set check: every dashed numeral of the English page 49 occurs in the Kannada pages 48-50 |
| 60 | `; sūtra numerals tentative [?].*` → `.*` | SECOND-PASS Q2: set check: every dashed numeral of the English page 60 occurs in the Kannada pages 59-61 |
| 17 | `४-१-४२` → `४-१-८५-२` | SECOND-PASS Q1: Kannada p.17: ಪೃಥಿವ್ಯಾ ಇಾಇೌ । ಪಾ. ೪-೧-೮೫-೨ (Devanagari twin of the IAST edit) |
| 17 | `pā. sū. 4-1-42 [?] ity` → `pā. sū. 4-1-85-2 ity` | SECOND-PASS Q1: Kannada p.17: ಪಾ. ೪-೧-೮೫-೨ |
| 17 | `(Pā. Sū. 4-1-42 [?])` → `(Pā. Sū. 4-1-85-2)` | SECOND-PASS Q1: Kannada p.17: ಪಾ. ೪-೧-೮೫-೨ |
| 22 | `glosses mine and tentative; reference numerals as read, all [?]):` → `glosses mine and tentative):` | SECOND-PASS Q2: all five reference numerals of the page are now taken from the Kannada p.22 |
| 22 | `(Ṛk. Saṃ. 2-[?]-[?] [?])` → `(Ṛk. Saṃ. 7-38-2)` | SECOND-PASS Q1: Kannada p.22: ಋ. ಸಂ. ೭-೩೮-೨ |
| 22 | `(Ṛk. Saṃ. 6-[?]-[?] [?])` → `(Ṛk. Saṃ. 7-45-3)` | SECOND-PASS Q1: Kannada p.22: ಋ. ಸಂ. ೭-೪೫-೩ |
| 22 | `(Ṛk. Saṃ. 8-[?]-[?] [?])` → `(Ṛk. Saṃ. 7-16-4)` | SECOND-PASS Q1: Kannada p.22: ಋ. ಸ. ೭-೧೬-೪ |
| 22 | `(Ṛk. Saṃ. 5-[79]-[8] [?])` → `(Ṛk. Saṃ. 7-81-5)` | SECOND-PASS Q1: Kannada p.22: ಋ. ಸಂ. ೭-೮೧-೫ |
| 29 | `(Ni. [5-?]-[?] [?])` → `(Ni. 5-6)` | SECOND-PASS Q1: Kannada p.29: ಸಚಾ-ಸಚ ಸಹೇತ್ಯರ್ಥಃ (ನಿ.-೫-೬) |
| 34 | `[४?] ॥ — *Aṣṭaka 1; Adhyāya 6; Varga "4" as read, doubtful [?].*` → `३ ॥ — *Aṣṭaka 1; Adhyāya 6; Varga 3.*` | SECOND-PASS Q1: Kannada p.34: ॥ ಅಷ್ಟಕ- ೧ ॥ ಅಧ್ಯಾಯ- ೬ ॥ ವರ್ಗ- ೩ ॥ |
| 35 | `(Kā. 3-1-11 [?])` → `(Kā. 3-1-11-2)` | SECOND-PASS Q1: Kannada p.35: ಕಾ. ೩-೧-೧೧-೨ ಇತಿ ಕ್ವಿಪ್ |
| 35 | `have not guessed its details [?].)*` → `have not guessed its details.)*` | SECOND-PASS Q2: Kannada p.35 has the argument; remark about the scan, no place in doubt |
| 39 | `a newest [?] — *matī*` → `a newest — *matī*` | SECOND-PASS Q2: Kannada p.40: ನವಿಷ್ಠಯಾ — ಅತ್ಯಂತ ಹೊಸದೂ ಮತ್ತು ಶ್ರೇಷ್ಠವೂ ಆದ (newest) |
| 43 | `; doubtful places [?]; continues on p. 44` → `; continues on p. 44` | SECOND-PASS Q2: gate check: every chunk of the Devanagari block stands in the Kannada pages 42-44 |
| 46 | `(कात्यायन ?)` → `का. ७-३-८७-१` | SECOND-PASS Q1: Kannada p.46: ಬಹುಲಂ ಛಂದಸೀತಿ ವಕ್ತವ್ಯಂ । ಕಾ. ೭-೩-೮೭ ೧ (Devanagari twin) |
| 46 | `(kātyāyana?) [?] iti` → `kā. 7-3-87-1 iti` | SECOND-PASS Q1: Kannada p.46: ಕಾ. ೭-೩-೮೭ ೧ |
| 47 | `(Tai. Saṃ. 1-3-[?] [?])` → `(Tai. Saṃ. 1-4-28)` | SECOND-PASS Q1: Kannada p.47 (and 46): ತೈ. ಸಂ. ೧-೪-೨೮ |
| 47 | `read with doubt in several words; the reference is [?].)` → `read with doubt in several words.)` | SECOND-PASS Q2: the reference is now taken from the Kannada |
| 51 | `(Uṇ. Sū. 4-[198] [?])` → `(Uṇ. Sū. 4-6-45)` | SECOND-PASS Q1: Kannada p.51: ಅದೇರ್ನುಮ್‌ಧಶ್ಚ (ಉ. ಸೂ. ೪-೬-೪೫) |
| 51 | `(Uṇ. Sū. 4-[188] [?])` → `(Uṇ. Sū. 4-6-28)` | SECOND-PASS Q1: Kannada p.51: ಸರ್ವಧಾತುಭ್ಯೋಽಸುನ್ (ಉ. ಸೂ. ೪-೬-೨೮) |
| 53 | `विभक्त्या राकारः` → `विभक्तेराकारः` | SECOND-PASS Q1: Kannada p.53: ಸುಪಾಂ ಸುಲುಗಿತಿ ವಿಭಕ್ತೇರಾಕಾರಃ (Devanagari made by sp_sanskrit.py) |
| 53 | `vibhaktyā rākāraḥ [?]` → `vibhakterākāraḥ` | SECOND-PASS Q1: Kannada p.53: ವಿಭಕ್ತೇರಾಕಾರಃ (IAST made by sp_sanskrit.py) |
| 53 | `(Ā. Sū. 6-11 [?])` → `(Ā. Sū. 6-11)` | SECOND-PASS Q2: Kannada p.53: ಅಂತ್ಯೇಷ್ವಹಃಸು । ಆ. ೬-೧೧ |
| 54 | `(Tai. Brā. [3-2-?-?] [?])` → `(Tai. Brā. 2-7-2-1)` | SECOND-PASS Q1: Kannada p.54: ಪುಷ್ಟಿರ್ವೈ ಪೂಷಾ … (ತೈ. ಬ್ರಾ. ೨-೭-೨-೧) |
| 56 | `(Āś. [6-5] [?])` → `(Āś. 6-4)` | SECOND-PASS Q1: Kannada p.55-56: ಆ. ೬-೪ (ಅಶ್ವಾವತಿ ಪ್ರೋಗ್ರಾಂ … ಯಾಜ್ಯಾ) |
| 56 | ` ॥ वर्ग—[५?] — *Aṣṭaka 1; Adhyāya 6; Varga "5" as read, doubtful [?].*` → ` — *Aṣṭaka 1; Adhyāya 6.*` | SECOND-PASS S3: the Kannada pages 55-56 print no Varga number for Sūkta 83 |
| 57 | `distinguished knowledge [?] —` → `distinguished knowledge —` | SECOND-PASS Q2: Kannada p.57: ವಿಚೇತಸೋ ವಿಶಿಷ್ಟಜ್ಞಾನಹೇತುಭೂತಾ ಆಪಃ |
| 59 | `"yuvarṇā…" (as read, "yuvarṇaśnaśatvaṃ vācyam" [?])` → `"ṛvarṇānnasya ṇatvaṃ vācyaṃ"` | SECOND-PASS Q1: Kannada p.59: ಋವರ್ಣಾನ್ನಸ್ಯಣತ್ವಂವಾಚ್ಯಂ (ವಾರ್ತಿಕ) (IAST made by sp_sanskrit.py) |
| 61 | `compressed and uncertain [?])*` → `compressed and uncertain)*` | SECOND-PASS Q2: Kannada p.61 has the Brāhmaṇa quotation and Ai. Brā. 2-20 as in the English |
| 62 | `passages affected are marked [?].)*` → `passages affected are marked.)*` | SECOND-PASS Q2: remark about the scan; the Kannada page is present; the places themselves are the other marks |
| 62 | `pā. sū. 5-3-39 [?] ity` → `ity` | SECOND-PASS S3: Kannada p.62: ಪೂರ್ವಾಧರಾವರಾಣಮಸಿ … ಎಂಬ with no number |
| 62 | `पा. सू. ५-३-३९ ` → `` | SECOND-PASS S3: Devanagari twin: Kannada p.62 has no number there |
| 62 | ` (Pā. Sū. 5-3-39 [?])` → `` | SECOND-PASS S3: Kannada p.62 has no number there |
| 62 | `partly broken in the scan [?])*` → `partly broken in the scan)*` | SECOND-PASS Q2: remark about the scan; the Kannada page is present |
| 64 | `(Ni. [?-?] [?]). It is` → `(Ni. 3-9). It is` | SECOND-PASS Q1: Kannada p.64: ಬ್ರಹ್ಮವೆಂದರೆ ಅನ್ನವು (ನಿ. ೩-೯) |
| 64 | `is clotted [?])*` → `is clotted)*` | SECOND-PASS Q2: Kannada p.64 has the paragraph; remark about the scan |
| 66 | `Ai. Brā. 1-38 [?] iti` → `Ai. Brā. 1-29 iti` | SECOND-PASS Q1: Kannada p.66-67: ಐ. ಬ್ರಾ. ೧-೨೯ । ಇತಿ |
| 66 | `१-३८` → `१-२९` | SECOND-PASS Q1: Devanagari twin: Kannada p.67 ೧-೨೯ |
| 66 | `(Ai. Brā. 1-38 [?])` → `(Ai. Brā. 1-29)` | SECOND-PASS Q1: Kannada p.66-67: ಐ. ಬ್ರಾ. ೧-೨೯ |
| 68 | `(1-29-?-?; 6-1-?-?; 6-2-?…) and so on [numerals as read, all [?]]` → `(3-1-3.1; 6-2-9-1; 6-2-9-4; 6-2-11-1-4) and so on` | SECOND-PASS Q1: Kannada p.68: ತೈ. ಸಂ. ೩-೧-೩.೧ ; ೬-೨-೯-೧ ; ೬-೨-೯-೪ ; ೬-೨-೧೧-೧-೪ |
| 68 | ` [as read; *khadira* is the printed word, [?]]` → `` | SECOND-PASS Q1: Kannada p.68: ಛದಿಯು ದರ್ಭೆಗಳಿಂದ ಮಾಡಲ್ಪಟ್ಟಿರುವುದು (darbha), as the English has it |
| 68 | `(1-[3?]-[?] [?])` → `(1-29)` | SECOND-PASS Q1: Kannada p.68: ಐತರೇಯ ಬ್ರಾಹ್ಮಣದಲ್ಲಿ ( ೧-೨೯ ) |
| 68 | `second pāda [?]).*` → `second pāda).*` | SECOND-PASS Q2: Kannada p.68-69 has the verse yuje vāṃ brahma pūrvyaṃ … tasthuḥ as in the English |
| 69 | `(Āś. 4-[9] [?])` → `(Āś. 4-9)` | SECOND-PASS Q1: Kannada p.69: ಯಮೇ ಇವ … ಆರಮೇತ್ ಎಂಬ ಸೂತ್ರ (ಅ. ೪-೯) |
| 70 | `(Pā. Sū. 2-2-62, vārttika 1 [?])` → `(Pā. Sū. 2-3-62, vārttika 1)` | SECOND-PASS Q1: Kannada p.70: ಷಷ್ಠ್ಯರ್ಥೇ ಚತುರ್ಥೀ ವಕ್ತವ್ಯಾ (ಪಾ. ಸೂ. ೨-೩-೬೨ ವಾರ್ತಿಕ ೧) |
| 73 | `(Ni. [2-10] [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada: ಭೋಜನಂ … ಧನವನ್ನು ಎಂದರ್ಥವು (ನಿ. ೩-೯) |

### 2026-11-27 second pass, batch m64-213.tsv
| page | old → new | why |
|---|---|---|
| 77 | `Varga [?]"` → `Varga 4"` | SECOND-PASS Q1: running head of Kannada p.77 reads ವ. 4 |
| 79 | `Varga [?]"` → `Varga 4"` | SECOND-PASS Q1: running head of Kannada p.79 reads ವ. 4 |
| 81 | `Varga [?]"` → `Varga 5"` | SECOND-PASS Q1: running head of Kannada p.81 reads ವ. 5 |
| 83 | `Varga [?]"` → `Varga 5"` | SECOND-PASS Q1: running head of Kannada p.83 reads ವ. 5 |
| 85 | `Varga [?]"` → `Varga 5"` | SECOND-PASS Q1: running head of Kannada p.85 reads ವ. 5 |
| 87 | `Varga [?]"` → `Varga 5"` | SECOND-PASS Q1: running head of Kannada p.87 reads ವ. 5 |
| 89 | `Varga [?]"` → `Varga 5"` | SECOND-PASS Q1: running head of Kannada p.89 reads ವ. 5 |
| 91 | `Varga [?]"` → `Varga 5"` | SECOND-PASS Q1: running head of Kannada p.91 reads ವ. 5 |
| 93 | `Varga [?]"` → `Varga 5"` | SECOND-PASS Q1: running head of Kannada p.93 reads ವ. 5 |
| 95 | `Varga [?]"` → `Varga 6"` | SECOND-PASS Q1: running head of Kannada p.95 reads ವ. 6 |
| 97 | `Varga [?]"` → `Varga 6"` | SECOND-PASS Q1: running head of Kannada p.97 reads ವ. 6 |
| 99 | `Varga [?]"` → `Varga 6"` | SECOND-PASS Q1: running head of Kannada p.99 reads ವ. 6 |
| 101 | `Varga [?]"` → `Varga 6"` | SECOND-PASS Q1: running head of Kannada p.101 reads ವ. 6 |
| 103 | `Varga [?]"` → `Varga 6"` | SECOND-PASS Q1: running head of Kannada p.103 reads ವ. 6 |
| 105 | `Varga [?]"` → `Varga 6"` | SECOND-PASS Q1: running head of Kannada p.105 reads ವ. 6 |
| 107 | `Varga [?]"` → `Varga 6"` | SECOND-PASS Q1: running head of Kannada p.107 reads ವ. 6 |
| 109 | `Varga [?]"` → `Varga 7"` | SECOND-PASS Q1: running head of Kannada p.109 reads ವ. 7 |
| 111 | `Varga [?]"` → `Varga 7"` | SECOND-PASS Q1: running head of Kannada p.111 reads ವ. 7 |
| 113 | `Varga [?]"` → `Varga 7"` | SECOND-PASS Q1: running head of Kannada p.113 reads ವ. 7 |
| 115 | `Varga [?]"` → `Varga 7"` | SECOND-PASS Q1: running head of Kannada p.115 reads ವ. 7 |
| 117 | `Varga [?]"` → `Varga 7"` | SECOND-PASS Q1: running head of Kannada p.117 reads ವ. ೨ (a misprint); pages 115 and 119 read ವ. ೭, so Varga 7 |
| 119 | `Varga [?]"` → `Varga 7"` | SECOND-PASS Q1: running head of Kannada p.119 reads ವ. 7 |
| 121 | `Varga [?]"` → `Varga 7"` | SECOND-PASS Q1: running head of Kannada p.121 reads ವ. 7 |
| 123 | `Varga [?]"` → `Varga 7"` | SECOND-PASS Q1: running head of Kannada p.123 reads ವ. 7 |
| 125 | `Varga [?]"` → `Varga 8"` | SECOND-PASS Q1: running head of Kannada p.125 reads ವ. 8 |
| 127 | `Va. [?]"` → `Va. 8"` | SECOND-PASS Q1: running head of Kannada p.127 reads ವ. 8 |
| 129 | `Va. [?]"` → `Va. 8"` | SECOND-PASS Q1: running head of Kannada p.129 reads ವ. 8 |
| 131 | `Va. [?]"` → `Va. 8"` | SECOND-PASS Q1: running head of Kannada p.131 reads ವ. 8 |
| 133 | `Va. [?]"` → `Va. 8"` | SECOND-PASS Q1: running head of Kannada p.133 reads ವ. 8 |
| 135 | `Va. [?]"` → `Va. 8"` | SECOND-PASS Q1: running head of Kannada p.135 reads ವ. 8 |
| 137 | `Va. [?]"` → `Va. 8"` | SECOND-PASS Q1: running head of Kannada p.137 reads ವ. 8 |
| 139 | `Va. [?]"` → `Va. 8"` | SECOND-PASS Q1: running head of Kannada p.139 reads ವ. 8 |
| 141 | `Va. [?]"` → `Va. 8"` | SECOND-PASS Q1: running head of Kannada p.141 reads ವ. 8 |
| 143 | `Va. [?]"` → `Va. 9"` | SECOND-PASS Q1: running head of Kannada p.143 reads ವ. 9 |
| 145 | `Va. [?]"` → `Va. 9"` | SECOND-PASS Q1: running head of Kannada p.145 reads ವ. 9 |
| 76 | `1-51-11; 1-[83]-[5]; 1-[130]-[9]; 20-11; 8-[23]-[17]; Atharvaveda 4-29-6-[?]; Taittirīya S` → `1-51-11; 1-83-5; 1-121-12; 6-20-11; 7-23-17; Atharvaveda 4-29-6; Taittirīya Saṃhitā 2-5-8-` | SECOND-PASS Q1: Kannada p.76 (Special Topics, Kāvya): ಋ. ಸಂ. ೧-೫೧-೧೧; ೧-೮೩-೫; ೧-೧೨೧-೧೨; ೬-೨೦-೧೧; ೭-೨೩-೧೭; ಅಥರ್ವವೇದ ೪-೨೯-೬; ತೈತ್ತಿರೀಯ ಸಂಹಿತಾ ೨-೫-೮-೫; doubt clause dropped, all i |
| 78 | `अन्त्यैनिकारश्छान्दसः` → `अंत्यविकारश्चांदसः` | SECOND-PASS Q1: Kannada p.78 reads ಅಂತ್ಯವಿಕಾರಶ್ಚಾಂದಸಃ (antyavikāraś chāndasaḥ); Devanagari made by sp_sanskrit; twin of the IAST edit |
| 78 | `antyainikāraś chāndasaḥ [?]` → `aṃtyavikāraścāṃdasaḥ` | SECOND-PASS Q1: Kannada p.78 reads ಅಂತ್ಯವಿಕಾರಶ್ಚಾಂದಸಃ; IAST made by sp_sanskrit; twin of the Devanagari edit |
| 79 | `Ṛ. Saṃ. 1-167-6-[?]" *(numerals as read [?])*.` → `Ṛ. Saṃ. 1-167-6".` | SECOND-PASS Q1: Kannada p.79 (Arka): ಋ. ಸಂ. ೧-೧೬೭-೬ |
| 79 | `(Ṛ. Saṃ. 1-135-7-[?] [?])` → `(Ṛ. Saṃ. 1-135-7)` | SECOND-PASS Q1: Kannada p.79 (Grāvā): ಯತ್ರ ಗ್ರಾವಾ ವದತಿ ... (ಋ. ಸಂ. ೧-೧೩೫-೭) |
| 80 | `1-165-14-[?]; 7-68-94-[?]; 6-[?]-[?]; 10-75-1-[?] [numerals read from the small print and ` → `1-165-14; 7-68-9; 9-112-3; 10-75-1` | SECOND-PASS Q1: Kannada p.80 (Kavi): ೧-೧೬೫-೧೪; ೭-೬೮-೯; ೯-೧೧೨-೩; ೧೦-೭೫-೧ |
| 81 | `laiṅgādanagantavyaḥ [?] ||` → `laiṅgādanagantavyaḥ ||` | SECOND-PASS Q2: Kannada p.81 reads ಸೂಕ್ತವಿನಿಯೋಗೋ ಲಿಂಗಾದನಗಂತವ್ಯಃ, the same as the English |
| 81 | `by indication [?]. In the` → `by indication. In the` | SECOND-PASS Q2: Kannada p.81 has laiṅgād anagantavyaḥ (by indication), agreeing with the English |
| 81 | `ऐ… । अस्य… ।` → `एहू ष्टिति खंडे सूत्रितं ।` | SECOND-PASS Q1: Kannada p.81 reads ಏಹೂಷ್ಟಿತಿ ಖಂಡೇ ಸೂತ್ರಿತಂ where the English has "Ai… | asya…"; Devanagari by sp_sanskrit; twin of the IAST edit |
| 81 | `Ai… [?] | asya… [?] |` → `ehū ṣṭiti khaṃḍe sūtritaṃ |` | SECOND-PASS Q1: Kannada p.81 reads ಏಹೂಷ್ಟಿತಿ ಖಂಡೇ ಸೂತ್ರಿತಂ; IAST by sp_sanskrit; twin of the Devanagari edit |
| 81 | `आ. ६-२` → `आ. ७-८` | SECOND-PASS Q1: Kannada p.81 reads ಆ. ೭-೮ for the second citation (Devanagari twin of the IAST edit) |
| 81 | `Ā. Sū. 9-8 iti ||` → `Ā. Sū. 7-8 iti ||` | SECOND-PASS Q1: Kannada p.81 reads ಆ. ೭-೮ (the English 9-8 is not in the print) |
| 81 | `(Ā. Sū. 9-8).` → `(Ā. Sū. 7-8).` | SECOND-PASS Q1: Kannada p.81 reads ಆ. ೭-೮ |
| 81 | ` (the rest of this sentence is broken in the print [?])` → `` | SECOND-PASS S3: Kannada p.81 has the sentence whole (ಏಹೂಷ್ಟಿತಿ ಖಂಡೇ ಸೂತ್ರಿತಂ ...); the doubt note falls |
| 81 | `recorded as printed; reference numerals [?])*` → `recorded as printed)*` | SECOND-PASS Q1: both citations on the Kannada page (ಆ. ೬-೨, ಆ. ೭-೮) are settled |
| 82 | `[६, ७, ८, ९?] ॥ — *Aṣṭaka 1; Adhyāya 6; Varga "6, 7, 8, 9" as read, doubtful [?].*` → `५, ६, ७, ८ ॥ — *Aṣṭaka 1; Adhyāya 6; Varga 5, 6, 7, 8.*` | SECOND-PASS Q1: Kannada p.82 reads ವರ್ಗ- 5, 6, 7. 8.; running heads agree (p.85 Varga 5 ... p.125 Varga 8) |
| 84 | `(Ni. [?-?] [?])` → `(Ni. 3-22)` | SECOND-PASS Q1: Kannada p.84 (Rajaḥ): ರಜಸೀ ದ್ಯಾವಾಪೃಥಿವಿಗಳೆಂದೂ ... (ನಿ. ೩-೨೨) |
| 85 | `[as read, Pā. Sū. 4-1-161 [?]]` → `(Pā. Sū. 4-1-161)` | SECOND-PASS Q2: Kannada p.86 (same sentence, mānuṣāṇām): ಮನೋರ್ಜಾತಾವಞ್ಯತೌ ಷುಕ್ ಚ (ಪಾ. ಸೂ. ೪-೧-೧೬೧) |
| 88 | `*yojā nv indra te harī* [as read, reference [?]].)*` → `*yojā nv indra te harī*.)*` | SECOND-PASS Q2: Kannada p.88 reads 82 ನೆಯ ಸೂಕ್ತದಲ್ಲಿ 1, 2, 3, 4 ನೇ ಋಕ್ಕುಗಳಲ್ಲಿ ... ಯೋಜಾನ್ವಿಂದ್ರತೇ, the same reference as the English |
| 90 | `(Ni. 8-11). Yāska has given the etymology of the word *śukra*: '*śukraṃ śocater jvalatikar` → `(Ni. 2-24). Yāska has given the etymology of the word *śukra*: '*śukraṃ śocater jvalatikar` | SECOND-PASS Q1: Kannada p.90: ಉದಕವೆಂದೂ ಅರ್ಥವು (ನಿ. ೨-೨೪) ... ಯಾಸ್ಕರ ನಿರ್ವಚನವಿರುವುದು (ನಿ. ೮-೧೧); the English had 8-11 after "water", and the etymology number was the mark |
| 94 | `८-२-८२?` → `८-२-८७-१` | SECOND-PASS Q1: Kannada p.94 reads ಪಾ.8-2-87-1 after तरपीद्रथिनः (Devanagari twin) |
| 94 | `pā. sū. 8-2-82? [?] ity` → `pā. sū. 8-2-87-1 ity` | SECOND-PASS Q1: Kannada p.94 reads ಪಾ.8-2-87-1 after ತರಪೀದ್ರಥಿನಃ (IAST twin) |
| 98 | `(Āś. [7-8] [?])` → `(Āś. 7-8)` | SECOND-PASS Q2: Kannada p.98: ಇದ್ವಿದಯತೇ ಎಂಬ ಸೂತ್ರದಿಂದ ವಿವೃತವಾಗಿರುವುದು (ಆ. 7-8) |
| 98 | `(Ai. Ā. [5]-[?]-[?] [?])` → `(Ai. Ā. 5-2-5)` | SECOND-PASS Q1: Kannada p.98: ಐ. ಆ 5-2-5 after the same sentence |
| 99 | `añceḥ…*' (Ni. [?-?] [?]) —` → `añceḥ…*' —` | SECOND-PASS S3: Kannada p.99 has no reference number after the Yāska quotation |
| 100 | `"avyaye nañ kunipātānām" (Pā. Sū. 6-1-[?]) the first` → `"avyaye nañ kunipātānām" the first` | SECOND-PASS S3: Kannada p.100 names the sūtra (ಅವ್ಯಯೆ ನಞ್ ಕು ನಿಪಾತಾನಾಂ) with no number |
| 102 | `(Ni. [3-18] [?])` → `(Ni. 2-17)` | SECOND-PASS Q1: Kannada p.102: ಅಂಗೇತಿ ಕ್ಷಿಪ್ರನಾಮ । ಅಂಚಿತಮೇವಾಂಕಿತಂ ಭವತಿ ॥ (ನಿ. ೨-೧೭) |
| 105 | `(Kā. 4-1-44, vārttika 1 [?])` → `(Kā. 4-1-44, vārttika 1)` | SECOND-PASS Q2: Kannada p.106 (Sanskrit, same sentence) and p.109 read ಕಾ. ೪-೧-೪೪-೧ |
| 108 | `"dīrghāj jasi ca" (Pā. Sū. 6-1-[?]) forbids` → `"dīrghāj jasi ca" forbids` | SECOND-PASS S3: Kannada p.108 names the sūtra (ದೀರ್ಘಾಜ್ಜಸಿ ಚ) with no number |
| 109 | `[as read: "dhātoḥ nit", Pā. Sū. 6-1-[?]]` → `[as read: "dhātoḥ nit"]` | SECOND-PASS S3: Kannada p.109 has ಧಾನ್ಯೇನಿತ್ ಎಂಬುದರಿಂದ with no number |
| 109 | `(Kā. 4-1-44, vārttika 1 [?])` → `(Kā. 4-1-44, vārttika 1)` | SECOND-PASS Q2: Kannada p.109 reads ಕಾ. ೪-೧-೪೪-೧ |
| 114 | `(Pā. Sū. 6-1-26 [?])` → `(Pā. Sū. 7-1-76)` | SECOND-PASS Q1: Kannada p.115 (asthabhiḥ, same sentence): ಛಂದಸ್ಯಪಿ ದೃಶ್ಯತೇ । ಪಾ. ೭-೧-೭೬ |
| 116 | `1-[80]-[16]; 1-[84]-[13]; 1-[84]-[14]; 1-[116]-[12]; 1-[117]-[22]; 1-119-9 and so on, and ` → `1-80-16; 1-84-13; 1-84-14; 1-116-12; 1-117-22; 1-119-9 and so on, and in the Taittirīya Sa` | SECOND-PASS Q1: Kannada p.116 (lines 20-23) gives all these numerals; doubt clause dropped, all its numerals settled |
| 119 | `1-[84]-[14]; 3-1-[?]; 1-117-22-[?]; 7-6-39-[?]; 10-35-2-[?] and others [numerals as read, ` → `1-84-14; 7-6-39; 7-7-29; 7-64-11; 9-65-22; 9-113-1; 10-35-2 and others` | SECOND-PASS Q1: Kannada p.119 (Śaryaṇāvati): ೧-೮೪-೧೪; ೭-೬-೩೯; ೭-೭-೨೯; ೭-೬೪-೧೧; ೯-೬೫-೨೨; ೯-೧೧೩-೧; ೧೦-೩೫-೨ ಇತ್ಯಾದಿ |
| 122 | `(Āś. [9-8] [?])` → `(Āś. 9-8)` | SECOND-PASS Q2: Kannada p.122: ಸೂತ್ರದಿಂದ ವಿವೃತವಾಗಿರುವುದು (ಆ. 9-8) |
| 125 | `ṛtasya* — the two' (Āś. [?]).` → `ṛtasya* — the two'.` | SECOND-PASS S3: Kannada p.125 has the sūtra quotation (ಕಾಯಂ ದಶಮಂ ... ದ್ವೇ ಇತಿ) with no number |
| 127 | `ṛtasyeti dve*' (Āś. [?])."` → `ṛtasyeti dve*'."` | SECOND-PASS S3: Kannada p.127 gives the sentence without a number |
| 126 | `; numerals [?]; characterized` → `; characterized` | SECOND-PASS Q1: numerals of the page settled against Kannada p.126 (u. 1-14, 3-2-180-1, pā. 3-3-99) |
| 126 | `(Pā. Sū. 3-2-180-1 [?])` → `(Pā. Sū. 3-2-180-1)` | SECOND-PASS Q2: Kannada p.126 reads 3-2-180-1 |
| 126 | `(Pā. Sū. 3-399)` → `(Pā. Sū. 3-3-99)` | SECOND-PASS Q1: Kannada p.126 reads ಪಾ. 3-3-99 (IAST twin) |
| 126 | `३-३९९` → `३-३-९९` | SECOND-PASS Q1: Kannada p.126 reads ಪಾ. 3-3-99 (Devanagari twin) |
| 128 | `(Ni. [?-?] [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.128: ಹೃಣೀಯತೇ ಎಂಬ ಶಬ್ದವು ಪಠಿತವಾಗಿರುವುದರಿಂದ (ನಿ. ೩-೯) |
| 128 | ` *[Printed text partly clotted: "…baddhā-[?]…aśvān"; read as given with doubt.]*` → `` | SECOND-PASS S3: Kannada p.128 reads the passage whole (ಬದ್ಧಾಸ್ತಾನ್ ... ಕುದುರೆಗಳನ್ನು); the doubt note falls |
| 129 | `Uṇ. Sū. 1-[13?] [?])` → `Uṇ. Sū. 1-13)` | SECOND-PASS Q1: Kannada p.129: ಇಷೇಃ ಕಿಚ್ಚ (ಉ. ಸೂ. 1-13) |
| 129 | `, the numerals as read [?]):*` → `):*` | SECOND-PASS Q1: all sūtra numerals of the page agree with Kannada pp.128-130 (set check run) |
| 130 | `, with doubt [?], the print being "anugrahītā indra"-like).*` → `).*` | SECOND-PASS Q2: Kannada p.130 reads ಅನುಗ್ರಹೀತರೀಂದ್ರ ಆಗತೇ ಸತಿ, the same as the English |
| 131 | `चिनेत्य…स्यामृचि` → `चनेत्यस्यामृचि` | SECOND-PASS Q1: Kannada p.131 reads ಕದಾ ಚನೇತ್ಯಸ್ಯಾಮೃಚಿ; Devanagari by sp_sanskrit (twin) |
| 131 | `kadā cin etya[?] … syām ṛci` → `kadā canetyasyāmṛci` | SECOND-PASS Q1: Kannada p.131 reads ಕದಾ ಚನೇತ್ಯಸ್ಯಾಮೃಚಿ; IAST by sp_sanskrit (twin) |
| 131 | ` *(One clause in the middle of this passage, "…kadā cin etya…", is broken in the print and` → `` | SECOND-PASS S3: Kannada p.131 has the clause whole (ಕದಾ ಚನೇತ್ಯಸ್ಯಾಮೃಚಿ); the doubt note falls |
| 134 | `(Uṇ. Sū. 4-150x] [?])` → `(Uṇ. Sū. 4-150)` | SECOND-PASS Q1: Kannada p.134: ನಾಮನ್ಸೀಮನ್ನಿತ್ಯಾದೌ । ಉ. 4-150 |
| 134 | `(Uṇ. Sū. 4-167?] [?])` → `(Uṇ. Sū. 4-167)` | SECOND-PASS Q1: Kannada p.134: ಹುಯಾಮಾಶ್ರುಭಸಿಭ್ಯಸ್ತ್ರನ್ । ಉ. 4-167 |
| 134 | `; the Uṇādi numerals are unreliable at 150 dpi [?]):*` → `):*` | SECOND-PASS Q1: both Uṇādi numerals of the page settled from Kannada p.134 |
| 140 | `*sarvadhātubhyo 'sun*, Uṇ. Sū. [4-189?] [?])` → `*sarvadhātubhyo 'sun*)` | SECOND-PASS S3: Kannada p.140 (ವಚಃ): ಸರ್ವಧಾತುಭ್ಯೋಽಸುನ್ ಎಂಬುದರಿಂದ, no number |
| 144 | `(Ā. Sū. 8-2 [?])` → `(Ā. Sū. 7-7)` | SECOND-PASS Q1: Kannada p.143 (ಇತ್ಯಾಗ್ನಿಮಾರುತಂ ॥ ಆ. 7-7) and p.144 (ವಿವೃತವಾಗಿರುವುದು (ಆ. 7-7)) |
| 144 | `वर्ग २-२ — *Aṣṭaka 1 · Adhyāya 6 · Varga 9, 10* (the numerals are small and read with doub` → `वर्ग ९, १० — *Aṣṭaka 1 · Adhyāya 6 · Varga 9, 10*` | SECOND-PASS Q1: Kannada p.144 reads ವರ್ಗ— 9, 10; running heads of pp.143 and 145 read ವ. ೯ |
| 145 | `yajñāḥ [?] | teṣu` → `yajñāḥ | teṣu` | SECOND-PASS Q2: Kannada p.145 reads ವಿದಥಾ ಯಜ್ಞಾಃ । ತೇಷು ಮದಂತಿ |
| 145 | `gods are to be worshipped [?])` → `gods are to be worshipped)` | SECOND-PASS Q2: Kannada p.145 reads ವಿದಂತ್ಯೇಷು ಯಷ್ಟವ್ಯತಯಾ ದೇವಾನಿತಿ ವಿದಥಾ ಯಜ್ಞಾಃ |
| 145 | `by "somarnase…" [?];` → `by "sormanasī alomoṣasī";` | SECOND-PASS Q1: Kannada p.145 reads ಸೋರ್ಮನಸೀ ಅಲೋಮೋಷಸೀ ಇತ್ಯುತ್ತರಪದಾದ್ಯುದಾತ್ತತ್ವಂ; Latin form by sp_sanskrit |
| 145 | `"ruvidibhyāṃ" [?]]` → `"ruvidibhyāṃ"]` | SECOND-PASS Q2: Kannada p.145 reads ವಿದ ಜ್ಞಾನೇ ರುವಿದಿಭ್ಯಾಂ ಕಿದಿತ್ಯಥಪ್ರತ್ಯಯಃ |
