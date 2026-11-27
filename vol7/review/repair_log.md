
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
