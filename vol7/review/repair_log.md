
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

### 2026-11-27 second pass, batch m112-261.tsv
| page | old → new | why |
|---|---|---|
| 147 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 147.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 147.` | SECOND-PASS Q1: running head of Kannada p.147 reads ವ. ೯ (Varga 9) |
| 149 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 149.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 149.` | SECOND-PASS Q1: running head of Kannada p.149 reads ವ. ೯ (Varga 9) |
| 151 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 151.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 151.` | SECOND-PASS Q1: running head of Kannada p.151 reads ವ. ೯ (Varga 9) |
| 153 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 153.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 153.` | SECOND-PASS Q1: running head of Kannada p.153 reads ವ. ೯ (Varga 9) |
| 155 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 155.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 155.` | SECOND-PASS Q1: running head of Kannada p.155 reads ವ. ೯ (Varga 9) |
| 157 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 157.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 157.` | SECOND-PASS Q1: running head of Kannada p.157 reads ವ. ೯ (Varga 9) |
| 159 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 159.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 159.` | SECOND-PASS Q1: running head of Kannada p.159 reads ವ. ೯ (Varga 9) |
| 161 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 161.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 161.` | SECOND-PASS Q1: running head of Kannada p.161 reads ವ. ೯ (Varga 9) |
| 163 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 163.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 163.` | SECOND-PASS Q1: running head of Kannada p.163 reads ವ. ೯ (Varga 9) |
| 165 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 165.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 165.` | SECOND-PASS Q1: running head of Kannada p.165 reads ವ. ೯ (Varga 9) |
| 167 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 167.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 167.` | SECOND-PASS Q1: running head of Kannada p.167 reads ವ. ೯ (Varga 9) |
| 169 | `Va. [?]"; centre: "Ṛgvedasaṃhitā"; right: 169.` → `Va. 9"; centre: "Ṛgvedasaṃhitā"; right: 169.` | SECOND-PASS Q1: running head of Kannada p.169 reads ವ. ೯ (Varga 9) |
| 171 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 171.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 171.` | SECOND-PASS Q2: running head of Kannada p.171 reads ವ. ೧೦ (Varga 10) |
| 173 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 173.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 173.` | SECOND-PASS Q2: running head of Kannada p.173 reads ವ. ೧೦ (Varga 10) |
| 175 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 175.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 175.` | SECOND-PASS Q2: running head of Kannada p.175 reads ವ. ೧೦ (Varga 10) |
| 177 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 177.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 177.` | SECOND-PASS Q2: running head of Kannada p.177 reads ವ. ೧೦ (Varga 10) |
| 179 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 179.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 179.` | SECOND-PASS Q2: running head of Kannada p.179 reads ವ. ೧೦ (Varga 10) |
| 181 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 181.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 181.` | SECOND-PASS Q2: running head of Kannada p.181 reads ಪ ೧೮, a misprint for ೧೦ (pp.179 and 183 read ೧೦); Varga 10 |
| 183 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 183.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 183.` | SECOND-PASS Q2: running head of Kannada p.183 reads ವ. ೧೦ (Varga 10) |
| 185 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 185.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 185.` | SECOND-PASS Q2: running head of Kannada p.185 reads ವ. ೧೦ (Varga 10) |
| 187 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 187.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 187.` | SECOND-PASS Q2: running head of Kannada p.187 reads ವ. ೧೦ (Varga 10) |
| 189 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 189.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 189.` | SECOND-PASS Q2: running head of Kannada p.189 reads ವ. ೧೦ (Varga 10) |
| 191 | `Va. 10 [?]"; centre: "Ṛgvedasaṃhitā"; right: 191.` → `Va. 10"; centre: "Ṛgvedasaṃhitā"; right: 191.` | SECOND-PASS Q2: running head of Kannada p.191 reads ವ. ೧೦ (Varga 10) |
| 193 | `Va. 11 [?]"; centre: "Ṛgvedasaṃhitā"; right: 193.` → `Va. 11"; centre: "Ṛgvedasaṃhitā"; right: 193.` | SECOND-PASS Q2: running head of Kannada p.193 reads ವ. ೧೧ (Varga 11) |
| 195 | `Va. 11 [?]"; centre: "Ṛgvedasaṃhitā"; right: 195.` → `Va. 11"; centre: "Ṛgvedasaṃhitā"; right: 195.` | SECOND-PASS Q2: running head of Kannada p.195 reads ವ. ೧೧ (Varga 11) |
| 197 | `Va. 11 [?]"; centre: "Ṛgvedasaṃhitā"; right: 197.` → `Va. 11"; centre: "Ṛgvedasaṃhitā"; right: 197.` | SECOND-PASS Q2: running head of Kannada p.197 reads ವ. ೧೧ (Varga 11) |
| 199 | `Va. 11 [?]"; centre: "Ṛgvedasaṃhitā"; right: 199.` → `Va. 11"; centre: "Ṛgvedasaṃhitā"; right: 199.` | SECOND-PASS Q2: running head of Kannada p.199 reads ವ. ೧೧ (Varga 11) |
| 201 | `Va. 11 [?]"; centre: "Ṛgvedasaṃhitā"; right: 201.` → `Va. 11"; centre: "Ṛgvedasaṃhitā"; right: 201.` | SECOND-PASS Q2: running head of Kannada p.201 reads ವ. ೧೧ (Varga 11) |
| 203 | `Va. 11 [?]"; centre: "Ṛgvedasaṃhitā"; right: 203.` → `Va. 11"; centre: "Ṛgvedasaṃhitā"; right: 203.` | SECOND-PASS Q2: running head of Kannada p.203 reads ವ. ೧೧ (Varga 11) |
| 205 | `Va. 12 [?]"; centre: "Ṛgvedasaṃhitā"; right: 205.` → `Va. 12"; centre: "Ṛgvedasaṃhitā"; right: 205.` | SECOND-PASS Q2: running head of Kannada p.205 reads ವ. ೧೨ (Varga 12) |
| 207 | `Va. 12 [?]"; centre: "Ṛgvedasaṃhitā"; right: 207.` → `Va. 12"; centre: "Ṛgvedasaṃhitā"; right: 207.` | SECOND-PASS Q2: running head of Kannada p.207 reads ವ. ೧೨ (Varga 12) |
| 211 | `Va. 12 [?]"; centre: "Ṛgvedasaṃhitā"; right: 211.` → `Va. 12"; centre: "Ṛgvedasaṃhitā"; right: 211.` | SECOND-PASS Q2: running head of Kannada p.211 reads ವ. ೧೨ (Varga 12) |
| 213 | `Va. 12 [?]"; centre: "Ṛgvedasaṃhitā"; right: 213.` → `Va. 12"; centre: "Ṛgvedasaṃhitā"; right: 213.` | SECOND-PASS Q2: running head of Kannada p.213 reads ವ. ೧೨ (Varga 12) |
| 209 | `Va. 12 [?]"; centre: "Ṛgvedasaṃhitā"; right: 209. Foot: printer's signature "[?]1 … Volume` → `Va. 12"; centre: "Ṛgvedasaṃhitā"; right: 209. Foot: printer's signature "14 … Volume 7"` | SECOND-PASS Q1: Kannada p.209 head reads ವ. ೧೨; foot reads "4]" (the 1 lost); signatures on pp.161, 177, 193 are 11, 12, 13, so 14 |
| 146 | ` (Ni. [11-13] [?])` → `` | SECOND-PASS S3: Kannada p.146 has no Nirukta number after the Yāska quotation |
| 146 | `te astu*' (Ṛ. Saṃ. 8-[?]-[?] [?])` → `te astu*' (Ṛ. Saṃ. 8-96-7)` | SECOND-PASS Q1: Kannada p.146: ಋ. ಸಂ. ೮-೯೬-೭ after ಮರುದ್ಧಿರಿಂದ್ರ ಸಖ್ಯಂ ತೇ ಅಸ್ತು |
| 146 | ` [the count as read, "ಮೂವತ್ತಮೂರು" — 33; flagged [?] as the numerals are cramped.]` → `` | SECOND-PASS Q2: Kannada p.146 reads ಮೂವತ್ತುಮೂರು (33), as the English has; doubt note dropped |
| 147 | `, read with doubt [?]):*` → `):*` | SECOND-PASS Q2: numerals of p.147 (1-133-6, 8-96-8) settled from Kannada p.147 |
| 147 | `marutaḥ*' (Ṛ. Saṃ. 8-96-7)` → `marutaḥ*' (Ṛ. Saṃ. 8-96-8)` | SECOND-PASS Q1: Kannada p.147 reads (ಋ. ಸಂ. ೮-೯೬ ೮) = 8-96-8 for ತ್ರಿ ಷಷ್ಟಿಸ್ತಾ ಮರುತೋ |
| 148 | `(Ṛ. Saṃ. 1-[165]; 1-160)` → `(Ṛ. Saṃ. 1-165; 1-170)` | SECOND-PASS Q1: Kannada p.148: (ಋ.ಸಂ. ೧-೧೬೫ ; ೧-೧೭೦) |
| 148 | `2-[34-9]; 2-[34-12]; 2-[34-3]; 1-[?]; 1-[?]; 1-[?]; 1-[?]; the numerals are cramped and ar` → `7-56-9; 7-56-17; 7-57-4; 1-171-1; 1-172-2; 1-164-8; 1-64-9)` | SECOND-PASS Q1: Kannada p.148: ( ಋ. ಸಂ. ೭-೫೬-೯ ; ೭-೫೬-೧೭ ; ೭-೫೭-೪ ; ೧-೧೭೧-೧ ; ೧-೧೭೨-೨ ; ೧-೧೬೪-೮ ; ೧-೬೪-೯ ) |
| 149 | ` (Ni. [?]); so *rodasī* means` → `; so *rodasī* means` | SECOND-PASS S3: Kannada p.149 has no number after the rodasī (Nirukta) passage |
| 151 | `Tai. Brā. [?] |` → `Tai. Brā. 1-4-1-5 |` | SECOND-PASS Q1: Kannada p.151: (ಶೈ. ಬ್ರಾ. ೧-೪-೧-೫) for ಇಯಂ ವೈ ಪೃಶ್ನಿಃ, p.155 reads ತೈ. ಬ್ರಾ. ೧-೪-೧-೫ (ಶೈ a misprint) |
| 151 | `; the Brāhmaṇa references are [?].)*` → `.)*` | SECOND-PASS Q2: the one Brāhmaṇa reference settled from Kannada pp.151/155 |
| 152 | `(Ṛ. Saṃ. 5-[57?]-[?] [?]; numerals not legible)` → `(Ṛ. Saṃ. 5-29-3)` | SECOND-PASS Q1: Kannada p.152: (ಋ. ಸಂ. ೫-೨೯-೩) after ಪೃಶ್ನೇಃ ಪುತ್ರಾ ಉಪಮಾಸೋ… |
| 154 | `(Ṛ. Saṃ. 1-[89]-[7] [?])` → `(Ṛ. Saṃ. 1-89-7)` | SECOND-PASS Q1: Kannada p.154: (ಋ. ಸಂ. ೧-೮೯-೭) for ಪೃಷದಶ್ವಾ ಮರುತಃ |
| 154 | `jigātana ‖* (Ṛ. Saṃ. 5-[?]-[?] [?])` → `jigātana ‖* (Ṛ. Saṃ. 5-59-6)` | SECOND-PASS Q1: Kannada p.154: (ಋ. ಸಂ. ೫-೫೯-೬) for ಸುಜಾತಾಸೋ ಜನುಷಾ |
| 154 | `vāyubhir vāśrāsaḥ pṛśnimātaraḥ ‖* (Ṛ. Saṃ. 2-14-[?] [?])` → `vāyubhir vāśrāsaḥ pṛśnimātaraḥ ‖* (Ṛ. Saṃ. 8-7-3)` | SECOND-PASS Q1: Kannada p.154: (ಋ. ಸಂ. ೮-೭-೩) for ಉದೀರಯಂತ ವಾಯುಭಿರ್ವಾಶ್ರಾಸಃ |
| 154 | `ut stomaiḥ pṛśnimātaraḥ ‖* (Ṛ. Saṃ. 2-14-[?] [?])` → `ut stomaiḥ pṛśnimātaraḥ ‖* (Ṛ. Saṃ. 8-7-17)` | SECOND-PASS Q1: Kannada p.154: (ಋ. ಸಂ. ೮-೭-೧೭) for ಉದು ಸ್ವಾನೇಭಿರೀರತ |
| 154 | `duhate pṛśnimātaraḥ ‖* (Ṛ. Saṃ. 9-[?]-[?] [?])` → `duhate pṛśnimātaraḥ ‖* (Ṛ. Saṃ. 9-34-5)` | SECOND-PASS Q1: Kannada p.154: (ಋ. ಸಂ. ೯-೩೪-೫) for ಅಭೀಮೃತಸ್ಯ ನಿಷ್ಟಪಂ |
| 154 | `śubham ‖* (Ṛ. Saṃ. 5-[?]-[?] [?])` → `śubham ‖* (Ṛ. Saṃ. 5-57-2)` | SECOND-PASS Q1: Kannada p.154: (ಋ. ಸಂ. ೫-೫೭-೨) for ಸ್ವಶ್ವಾಃ ಸ್ಥ ಸುರಥಾಃ |
| 155 | `pṛthvādibhya imanij vā*, Pā. Sū. 8-6-17)` → `pṛthvādibhya imanij vā*, Pā. Sū. 5-1-122)` | SECOND-PASS Q1: Kannada p.155: (೫-೧-೧೨೨) after ಪೃಥ್ವಾದಿಭ್ಯ ಇಮನಿಜ್ವಾ |
| 155 | `raidyubhyaḥ*, Pā. Sū. 6-1-171)` → `raidyubhyaḥ*)` | SECOND-PASS S3: Kannada p.155 has no number after ಊಡಿದಂಪದಾದಿ |
| 155 | `phaḍhakhachaghām*, Pā. Sū. 7-1-2)` → `phaḍhakhachaghām*)` | SECOND-PASS S3: Kannada p.155 has no number after ಆಯನೇಯೀ… |
| 155 | `(Rik 85.2)** *(grammar page, noted briefly; every sūtra read is given in three layers, the` → `(Rik 85.2)** *(grammar page, noted briefly; every sūtra read is given in three layers)*` | SECOND-PASS Q2: numerals of the page settled against Kannada p.155 (5-2-93, 1-4-1-5, 5-1-122, 5-4-158; none elsewhere) |
| 157 | `yāditvena [?] padatvāt` → `yāditvena padatvāt` | SECOND-PASS Q2: Devanagari twin (Wikisource) reads मतुप्प्रत्ययस्य यादित्वेन पदत्वात् without a mark |
| 160 | `pṛṣatyo marutām iti [?] |` → `pṛṣatyo marutāmityuktatvāt |` | SECOND-PASS Q1: Kannada p.160 reads ಪೃಷತ್ಯೋ ಮರುತಾಮಿತ್ಯುಕ್ತತ್ವಾತ್; Devanagari twin has मरुतामित्युक्तत्वात् |
| 160 | `; the clause "pṛṣatya iti marudvāhanānāṃ saṃjñā" is followed by a short Nirukta-like phras` → `.)*` | SECOND-PASS Q1: phrase read from Kannada p.160 (ityuktatvāt); sūtra number 8-2-25 is on Kannada p.160 |
| 160 | `seven (companies [?])` → `seven (companies)` | SECOND-PASS Q2: Kannada p.160 reads …ಸಪ್ತಸಂಘಾತ್ಮಕಾ, a group of seven |
| 160 | `(the Nirukta [?] says 'the *pṛṣatīs* of the Maruts')` → `(as it is said: 'the *pṛṣatīs* of the Maruts')` | SECOND-PASS Q1: Kannada p.160 reads ಪೃಷತ್ಯೋ ಮರುತಾಮಿತ್ಯುಕ್ತತ್ವಾತ್ ('since it is said'), no work is named |
| 161 | `niyuto vāyoḥ ‖* (Ni. 2-[?] [?])` → `niyuto vāyoḥ ‖* (Ni. 2-28)` | SECOND-PASS Q1: Kannada p.161: (ನಿ. ೨-೨೮) after ನಿಯುತೋ ವಾಯೋಃ |
| 162 | `vārttika 2 [?])` → `vārttika 2)` | SECOND-PASS Q2: Kannada p.162: (ಪಾ. ಸೂ. ೩-೨-೧೭೮ ವಾ. ೨) |
| 165 | `ajānan ‖* (Ṛ. Saṃ. 1-[?]-[?] [?])` → `ajānan ‖* (Ṛ. Saṃ. 1-22-18)` | SECOND-PASS Q1: Kannada p.165: (ಋ. ಸಂ. ೧-೨೨-೧೮) after ಅಧ ಕ್ಷರಂತಿ ಸಿಂಧವೋ ನ ಸೃಷ್ಟಾಃ |
| 167 | `hal-ṅyor īti [?] ītvābhāvaḥ` → `hal-ṅyor īti ītvābhāvaḥ` | SECOND-PASS Q2: Devanagari twin (Wikisource) reads हल्ङ्योरिति… without a mark; Kannada p.167 has no number there |
| 167 | `, and the exact wording and the number are given with doubt [?];` → `;` | SECOND-PASS Q2: Pā. Sū. 8-3-46 is on Kannada p.167; wording as in Devanagari twin |
| 169 | `kvip ca*, Pā. Sū. 3-2-72)` → `kvip ca*, Pā. Sū. 3-2-76)` | SECOND-PASS Q1: Kannada p.169: (ಪಾ. ಸೂ. ೩-೨ ೭೬) after ಕ್ವಿಪ್ ಚ |
| 169 | `tāntantāmaḥ*, Pā. Sū. 3-4-101)` → `tāntantāmaḥ*)` | SECOND-PASS S3: Kannada p.169 has no number after ತಸ್‌ಥಸ್— |
| 169 | `pāghrādhmā…*, Pā. Sū. 7-3-78)` → `pāghrādhmā…*)` | SECOND-PASS S3: Kannada p.169 has no number after ಪಾಘ್ರಾಧ್ಮಾ- |
| 169 | `*ī halyaghoḥ*, Pā. Sū. 2-14-113)` → `*ī halyaghoḥ*, Pā. Sū. 6-4-113)` | SECOND-PASS Q1: Kannada p.169: ಹಲ್ಯಘೋಃ (ಪಾ. ಸೂ. ೬-೪-೧೧೩) |
| 169 | `(Rik 85.6)** *(grammar page, noted briefly; every sūtra read is in three layers, the numer` → `(Rik 85.6)** *(grammar page, noted briefly; every sūtra read is in three layers)*` | SECOND-PASS Q2: numerals of the page settled against Kannada p.169 |
| 169 | `*kāsilakādi* [?] group` → `*kāpilakādi* group` | SECOND-PASS Q1: Kannada p.169 reads ಕಾಪಿಲಕಾದಿಯಲ್ಲಿ (sp_sanskrit: kāpilakādi) |
| 169 | `(Ni. [2-?-?] [?])` → `(Ni. 2-14-113)` | SECOND-PASS Q1: Kannada p.169: ಜಿಗಾತಿ (ನಿರು. ೨-೧೪-೧೧೩) |
| 169 | ` *(The sūtra number is read as given, with a numeral in doubt [?].)*` → `` | SECOND-PASS Q2: Pā. Sū. 8-3-46 is on Kannada p.169 (೮-೩-೪೬) |
| 171 | `yady ebhyo [?] marudbhyo` → `yady ebhyo marudbhyo` | SECOND-PASS Q2: Kannada p.171 reads ಯದ್ಯೇಭ್ಯೋ ಮರುದ್ಭೋ, nothing between; Devanagari twin has no mark |
| 171 | `viṣṇur hāvat [?] |` → `viṣṇur hāvat |` | SECOND-PASS Q2: Kannada p.171 reads ವಿಷ್ಣುರ್ಹಾವತ್ ವಿಷ್ಣುರೇವಾಗತ್ಯ; Devanagari twin has no mark |
| 171 | `omitted [?]; the clause beginning* yady ebhyo *is read with doubt.)*` → `omitted.)*` | SECOND-PASS Q2: the yady ebhyo clause agrees with Kannada p.171 and the Devanagari twin; the omission note stands, mark dropped |
| 172 | `marutaḥ [?] indrasya` → `marutaḥ indrasya` | SECOND-PASS Q2: Kannada p.172 reads ಮರುತ ಇಂದ್ರಸ್ಯ; Devanagari twin has no mark |
| 172 | `(Ṛ. Saṃ. 8-100-[12] [?])` → `(Ṛ. Saṃ. 8-100-12)` | SECOND-PASS Q1: Kannada p.172: (ಋ. ಸಂ. ೮-೧೦೦-೧೨) |
| 173 | `in the Ṛks Ṛ. Saṃ. 9-342-?]; 8-[?]; 10-[?]; 6-[?]; 6-[?]; 6-[?]; 2-[?]; 7-[?]; 7-[?]; 7-[?` → `in the Ṛks (Ṛ. Saṃ. 8-27-8; 8-83-7; 10-92-11; 9-33-3; 9-34-2; 9-56-4; 9-63-3; 9-65-20; 7-3` | SECOND-PASS Q1: Kannada p.173 lists ಋ. ಸಂ. ೮-೨೭-೮ ; ೮-೮೩-೭ ; ೧೦-೯೨-೧೧ ; ೯-೩೩-೩ ; ೯-೩೪-೨ ; ೯-೫೬-೪ ; ೯-೬೩-೩ ; ೯-೬೫-೨೦ ; ೭-೩೭-೯ ; ೮-೧೨-೧೬ ; ೫-೮೭-೧ ; ೫-೮೭-೮ |
| 175 | `nittvād ādyudāttatvam [?] |` → `nittvād ādyudāttatvam |` | SECOND-PASS Q2: Kannada p.175 reads ನಿತ್ತ್ವಾದಾದ್ಯುದಾತ್ತತ್ವಂ, nothing after; Devanagari twin has no mark |
| 176 | ` (Ni. [2-17] [?]) — *pṛtanāsu* means` → ` — *pṛtanāsu* means` | SECOND-PASS S3: Kannada p.176 has no number after the sixty-six battle names passage |
| 177 | `(Pā. Sū. 6-4-[98])` → `(Pā. Sū. 6-4-98)` | SECOND-PASS Q1: Kannada p.177: (ಪಾ. ಸೂ. ೬-೪-೯೮) |
| 177 | `Pā. Sū. 6-4-[120])` → `Pā. Sū. 6-4-120)` | SECOND-PASS Q1: Kannada p.177: (ಪಾ. ಸೂ. ೬-೪-೧೨೦) |
| 177 | `(Rik 85.8)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read ` → `(Rik 85.8)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the page settled against Kannada p.177 (3-2-171-2, 3-2-170, 6-4-98, 6-4-120) |
| 178 | `since the affix is *pit* [?], by` → `when the affix follows, by` | SECOND-PASS Q1: Kannada p.178 reads ಪ್ರತ್ಯಯಪರವಾದಾಗ ಪುಗಂತಲಘೂಪಧಸ್ಯಚ |
| 179 | `lopaḥ [?]… nipātyate` → `lopaḥ… nipātyate` | SECOND-PASS Q2: Devanagari twin (Wikisource) reads लोपः… निपात्यते without a mark |
| 180 | `(*gatir anantaraḥ*, Pā. Sū. 6-2-[49] [?])` → `(*gatir anantaraḥ*, Pā. Sū. 6-2-49)` | SECOND-PASS Q1: Kannada p.180: ಗತಿರನಂತರಃ (ಪಾ ಸೂ. ೬-೨-೪೯) |
| 182 | `; the Āvaṭa/avata etymology sentence "avastrāta iti bhavaty avataḥ kūpaḥ" is read with dou` → `.)*` | SECOND-PASS Q2: the English wording equals the Wikisource Devanagari twin (अवस्त्रात इति भवत्यवतः कूपः); Kannada p.183 reads ಅವಸ್ತಾತ್ತತೋ ಭವತೀತ್ಯವತಃ ಕೂಪಃ (variant, English kept) |
| 183 | ` *(The Nirukta wording, as printed, is partly clotted [?].)*` → `` | SECOND-PASS Q2: same sentence as q210: English = Wikisource twin; Kannada p.183 has the variant ಅವಸ್ತಾತ್ತತೋ |
| 184 | `(Rik 85.10)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read` → `(Rik 85.10)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: every numeral of the page (6-4-76, 7-3-78, 6-1-159) is on Kannada p.184 |
| 186 | `āhāve vānayan [?] |` → `āhāve vānayan |` | SECOND-PASS Q2: Kannada p.186 reads ಆಹಾವೇಽವಾನಯನ್; Devanagari twin has no mark |
| 186 | `āto manin [?] … iti manin` → `āto manin … iti manin` | SECOND-PASS Q2: Devanagari twin (Wikisource) reads धाधातेरातो मनिन्… इति मनिन् without a mark |
| 187 | `Pā. Sū. 6-1-[182] [?])` → `Pā. Sū. 6-1-182)` | SECOND-PASS Q1: Kannada p.187: (ಪಾ. ಸೂ. ೬-೧-೧೮೨) |
| 189 | `(*pradānānām* [?])` → `(*pradānānām*)` | SECOND-PASS Q2: Kannada p.189 reads ಪ್ರದಾನಾನಾಮಿತಿ ಖಂಡೇ |
| 189 | `chāndase loṭi [?] …` → `chāndase loṭi …` | SECOND-PASS Q2: Devanagari twin (Wikisource) reads छान्दसे लोटि … without a mark |
| 189 | `partly omitted [?].)*` → `partly omitted.)*` | SECOND-PASS Q2: the omission is the Wikisource "…" (Devanagari twin), not a doubt |
| 190 | ` (Ni. [3-?] [?] [as read: *śaśatir arcatikarmā*])` → `` | SECOND-PASS S3: Kannada p.190 has no number after ಶಶತಿರರ್ಚತಿ… |
| 190 | ` *(The Skandasvāmin sentence is read with doubt [?].)*` → `` | SECOND-PASS Q2: Kannada p.190 reads ತ್ರಿಧಾತೂನಿ । ಧೀಯಂತೇ ಪ್ರಾಣಿನಾಂ ದೇಹೇಷ್ಟಿತಿ ಧಾತವಃ ಅನ್ನರಸಾಃ, as the English |
| 191 | `cānaś*, Pā. Sū. 3-2-[129])` → `cānaś*, Pā. Sū. 3-2-129)` | SECOND-PASS Q1: Kannada p.191 has 3-2-129 |
| 191 | `(Pā. Sū. 7-1-[45])` → `(Pā. Sū. 7-1-45)` | SECOND-PASS Q1: Kannada p.191 has 7-1-45 |
| 191 | `(Pā. Sū. 6-4-[37])` → `(Pā. Sū. 6-4-37)` | SECOND-PASS Q1: Kannada p.191 has 6-4-37 |
| 191 | `(Pā. Sū. 6-4-[9])` → `(Pā. Sū. 6-4-9)` | SECOND-PASS Q1: Kannada p.191 has 6-4-9 |
| 191 | `(Rik 85.12)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read` → `(Rik 85.12)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the page settled against Kannada p.191 |
| 192 | `converted letter by letter; numerals [?])**` → `converted letter by letter)**` | SECOND-PASS Q2: the one differing numeral (Ā. 4-11) corrected from Kannada p.192; the rest agree |
| 192 | `आ. ४-११ ।` → `आ. ८-११ ।` | SECOND-PASS Q1: Kannada p.192: ಆ. ೮-೧೧ (digits via sp_sanskrit) |
| 192 | `Ā. 4-11 |` → `Ā. 8-11 |` | SECOND-PASS Q1: Kannada p.192: ಆ. ೮-೧೧ (twin of the Devanagari line) |
| 192 | `the *Āgnimāruta*' (Ā. Sū. 4-11). In the *Aindrāmāruta*` → `the *Āgnimāruta*' (Ā. Sū. 8-11). In the *Aindrāmāruta*` | SECOND-PASS Q1: Kannada p.192: ಆ. ೮-೧೧ |
| 192 | `āgnimārutam*' (Ā. Sū. 4-11)` → `āgnimārutam*' (Ā. Sū. 8-11)` | SECOND-PASS Q1: Kannada p.192: ಆ. ೮-೧೧ |
| 193 | ` (the numerals are small and read with doubt [?])` → `` | SECOND-PASS Q2: Kannada p.193 reads ವರ್ಗ— ೧೧, ೧೨ as the English Varga 11, 12 |
| 196 | `sūtras read are in three layers, numerals [?]):*` → `sūtras read are in three layers):*` | SECOND-PASS Q2: numerals of the page settled against Kannada p.196 |
| 196 | `Uṇ. Sū. 4-660)` → `Uṇ. Sū. 4-666)` | SECOND-PASS Q1: Kannada p.196: (ಉ. ಸೂ. ೪-೬೬೬) |
| 196 | `"tṛja eva svaraḥ" is read with doubt [?]. ` → `` | SECOND-PASS Q2: tṛja eva svaraḥ is in the Wikisource Devanagari twin (तृज एव स्वरः) |
| 196 | `; the following [?] removed)` → `)` | SECOND-PASS Q2: self-referential mark removed |
| 198 | `vyatyayena madhyamaḥ [?] |` → `vyatyayena madhyamaḥ |` | SECOND-PASS Q2: Kannada p.198 reads ವ್ಯತ್ಯಯೇನ ಮಧ್ಯಮಃ; Devanagari twin has no mark |
| 198 | ` [as printed; so read with doubt [?]]` → `` | SECOND-PASS Q2: Kannada p.198 reads ವ್ಯತ್ಯಯೇನ ಮಧ್ಯಮಃ, as the English |
| 200 | `; the clause beginning* madidhātunā yuktā *and the last sentence on* vyatyayenotvābhāvaḥ *` → `.)*` | SECOND-PASS Q2: both clauses agree with Kannada p.200 (ಮದಿಧಾತುನಾ ಯುಕ್ತಾ …, ವ್ಯತ್ಯಯೇನೋತ್ವಾಭಾವಃ) |
| 202 | `susūdhāgṛdhibhyaḥ kran (Uṇ. 2-[25] [?]) |` → `susūdhāgṛdhibhyaḥ kran |` | SECOND-PASS S3: Kannada p.202 has no number after ಸುಸೂಧಾಗೃಧಿಭ್ಯಃ ಕ್ರನ್ |
| 202 | `क्रन् (उ. २-[२५]) ।` → `क्रन् ।` | SECOND-PASS S3: Kannada p.202 has no number (Devanagari twin of the IAST edit) |
| 202 | `with *kran* (Uṇ. 2-[25] [?]);` → `with *kran*;` | SECOND-PASS S3: Kannada p.202 has no number after ಕ್ರನ್ |
| 203 | `Pā. Sū. 3-1-[34])` → `Pā. Sū. 3-1-34)` | SECOND-PASS Q1: Kannada p.203 has 3-1-34 |
| 203 | `(Rik 86.5)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read ` → `(Rik 86.5)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the page settled against Kannada p.203 |
| 206 | `Pā. Sū. 4-1-[44])` → `Pā. Sū. 4-1-44)` | SECOND-PASS Q1: Kannada p.206 has 4-1-44 |
| 206 | `Pā. Sū. 8-2-[77])` → `Pā. Sū. 8-2-77)` | SECOND-PASS Q1: Kannada p.206 has 8-2-77 |
| 206 | `Pā. Sū. 8-1-[34])` → `Pā. Sū. 8-1-34)` | SECOND-PASS Q1: Kannada p.206 has 8-1-34 |
| 206 | `Pā. Sū. 6-1-[177])` → `Pā. Sū. 6-1-177)` | SECOND-PASS Q1: Kannada p.206 has 6-1-177 |
| 206 | `(Rik 86.6)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read ` → `(Rik 86.6)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the page settled against Kannada p.206 |
| 207 | `uttarapadādyudāttatvam [?] | parṣatha` → `uttarapadādyudāttatvam | parṣatha` | SECOND-PASS Q2: Kannada p.207 reads ಕ್ರತ್ವಾದಯಶ್ಚೇತ್ಯುತ್ತರಪದಾದ್ಯುದಾತ್ತತ್ವಂ; Devanagari twin has no mark |
| 207 | `; the sūtra-wording after* subhagaḥ *is read with doubt [?].)*` → `.)*` | SECOND-PASS Q2: wording agrees with Kannada p.207 and the Devanagari twin |
| 209 | `jhādeśaḥ [?] | bahulaṃ` → `jhādeśaḥ | bahulaṃ` | SECOND-PASS Q2: Devanagari twin (Wikisource) reads झादेशः । बहुलं without a mark; Kannada p.209 has ಝಾದೇಶ |
| 209 | `saṃhitāyāṃ dīrghaḥ [?] | kāmasya` → `saṃhitāyāṃ dīrghaḥ | kāmasya` | SECOND-PASS Q2: Devanagari twin (Wikisource) reads व्येचोतेस्तृज इति संहितायां दीर्घः without a mark |
| 209 | `; "jhādeśaḥ" and "vyecotes tṛja" are read with doubt [?].)*` → `.)*` | SECOND-PASS Q2: both readings equal the Devanagari twin |
| 209 | `the substitute (*jha*-type) [?],` → `the substitute (*jha*-type),` | SECOND-PASS Q2: jhādeśaḥ equals the Devanagari twin; Kannada p.209 ಝಾದೇಶ |
| 209 | `[hence *vidā* in the Saṃhitā] [?];` → `[hence *vidā* in the Saṃhitā];` | SECOND-PASS Q2: equals the Devanagari twin (संहितायां दीर्घः) |
| 210 | `(Pā. Sū. 3-2-[129])` → `(Pā. Sū. 3-2-129)` | SECOND-PASS Q1: Kannada p.210 has 3-2-129 |
| 210 | `(Rik 86.8)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read ` → `(Rik 86.8)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the page settled against Kannada p.210 (3-2-129, 6-3-135; 7-1-41 removed) |
| 210 | `"लोपस्त आत्मनेपदेषु" (Pā. Sū. 7-1-41) the loss` → `"लोपस्त आत्मनेपदेषु" the loss` | SECOND-PASS S3: Kannada p.210 has no number after ಲೋಪಸ್ತ ಆತ್ಮನೇಪದೇಷು |
| 210 | `the word *vinta*? [as read: "*vinata*"]` → `the word *vidata*` | SECOND-PASS Q1: Kannada p.210 reads ವಿದತ ಎಂದಿರುವಾಗ (sp_sanskrit: vidata) |
| 210 | ` *(The sūtra and the reasoning on* vidā *are read with doubt [?]; the clipped print does n` → `` | SECOND-PASS Q2: the reasoning on vidā follows Kannada p.210 step by step; 6-3-135 is on the page |
| 211 | `saṃhitāyāṃ dīrghaḥ [?] ‖` → `saṃhitāyāṃ dīrghaḥ ‖` | SECOND-PASS Q2: Kannada p.211 reads ತುನುಘಮಕ್ಷುತಜ್ಞತಿ ಸಂಹಿತಾಯಾಂ ದೀರ್ಘಃ; Devanagari twin has no mark |
| 211 | ` and are read with doubt [?].)*` → `.)*` | SECOND-PASS Q2: idudupadhasya (8-3-41) and the lengthening clause equal the Devanagari twin and Kannada p.211 |

### 2026-11-27 second pass, batch m112-261_2.tsv
| page | old → new | why |
|---|---|---|
| 203 | `(Pā. Sū. 6-3-88) no ` → `(Pā. Sū. 7-3-88) no ` | SECOND-PASS Q1: Kannada p.203 has 7-3-88 (भूसुवोस्तिङि) |

### 2026-11-27 second pass, batch m123-272.tsv
| page | old → new | why |
|---|---|---|
| 215 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 215.` → `Va. 12"; centre: "Ṛgvedasaṃhitā"; right: 215.` | SECOND-PASS Q1: running head of Kannada p.215 reads ವ. 12 (Varga 12) |
| 216 | `(as printed; numerals [?])` → `(as printed)` | SECOND-PASS Q2: the numeral of the note (Ā. 5-20) is the same in the Kannada p.216; clause dropped |
| 216 | `१३ [?] — *Aṣṭaka 1 · Adhyāya 6 · Varga 13 [?]*` → `१३ — *Aṣṭaka 1 · Adhyāya 6 · Varga 13*` | SECOND-PASS Q2: Kannada p.216 prints ವರ್ಗ—೧೩ for sūkta 87; Devanagari line and its IAST twin settled together |
| 217 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 217.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 217.` | SECOND-PASS Q2: running head of Kannada p.217 reads ವ. 13 (Varga 13) |
| 217 | `abhyāsasyātvam [?] |` → `abhyāsasyātvam |` | SECOND-PASS Q2: Kannada p.217 has the same words (āta aderityabhyāsasyātvaṃ; a/ā only) |
| 219 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 219.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 219.` | SECOND-PASS Q2: running head of Kannada p.219 reads ವ. 13 (Varga 13) |
| 219 | `tenarjīṣī somaḥ ‖* (Ni. [?] [?]) — **GLOSS**` → `tenarjīṣī somaḥ ‖* — **GLOSS**` | SECOND-PASS S3: Kannada p.219 has the quotation ... tenarjiṣī somaḥ with no reference number after it |
| 220 | `7.1)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `7.1)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: only numeral of the section (Uṇ. Sū. 4-666) is the same on Kannada p.220 |
| 222 | `ratheṣv āsaktā [?] meghāḥ` → `ratheṣv āsaktā meghāḥ` | SECOND-PASS Q2: Kannada p.222 reads ratheṣvāsaktā meghāḥ |
| 222 | `(Pā. Sū. 3-2-171 [?])` → `(Pā. Sū. 3-2-171)` | SECOND-PASS Q2: Kannada p.224 gives Pā. Sū. 3-2-171 for yayim (āṅgamahanajana…), same word |
| 223 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 223.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 223.` | SECOND-PASS Q2: running head of Kannada p.223 reads ವ. 13 (Varga 13) |
| 223 | ` *(printed Sanskrit of Skandasvāmin in the text, partly clotted [?])*` → `` | SECOND-PASS Q2: Kannada p.223 has the Skandasvāmin Sanskrit clear (upahvareṣu gahvareṣu parvatapradeśeṣu antarikṣapradeśeṣu) |
| 224 | `*yatra pradeśe yuṣmadīyā rathā vayaṃ tiṣṭhanti* [as read] *tatra rathacakradhārābhir vidya` → `*yatra pradeśe yuṣmadīyā rathā vyavatiṣṭhante tatra rathacakradhārābhiḥ vidyamānā meghāḥ p` | SECOND-PASS Q1: Kannada p.224 reads yatra pradeśe yuṣmadīyā rathā vyavatiṣṭhante tatra rathacakradhārābhiḥ vidyamānā meghāḥ prakṣarantīty arthaḥ (IAST made by sp_sanskrit.py) |
| 224 | ` *(The Skandasvāmin Sanskrit is clotted in the print and read with doubt [?].)*` → `` | SECOND-PASS Q2: quotation now follows the Kannada p.224 reading; doubt remark dropped |
| 224 | `7.2)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `7.2)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: Pā. Sū. 3-3-118, 3-2-171 and Ni. 2-21, 2-24 of the section are all on Kannada p.224 in the same places (brackets of 118 and 171 removed) |
| 224 | `(Pā. Sū. 3-3-[118]` → `(Pā. Sū. 3-3-118` | SECOND-PASS Q2: Kannada pp.223-226 has the same sūtra number in the same place; brackets of the older reading removed |
| 224 | `" (Pā. Sū. 3-2-[171]) the affix *kin*; s` → `" (Pā. Sū. 3-2-171) the affix *kin*; s` | SECOND-PASS Q2: Kannada pp.223-226 has the same sūtra number in the same place; brackets of the older reading removed |
| 225 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 225.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 225.` | SECOND-PASS Q2: running head of Kannada p.225 reads ವ. 13 (Varga 13) |
| 227 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 227.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 227.` | SECOND-PASS Q2: running head of Kannada p.227 reads ವ. 13 (Varga 13) |
| 228 | `7.3)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `7.3)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: all numerals of the section are now those of Kannada pp.228-229 (Uṇ. 1-137, Pā. 2-4-56, 6-1-203, Kā. 2-4-56, Ni. 2-21, 3-21); brackets removed |
| 228 | `(Uṇ. Sū. 1-127)` → `(Uṇ. Sū. 1-137)` | SECOND-PASS Q1: Kannada p.228 reads ಉ. ಸೂ. 1-137 for arti-stu-su… man |
| 228 | `(Pā. Sū. 2-4-[56]` → `(Pā. Sū. 2-4-56` | SECOND-PASS Q2: Kannada pp.227-230 has the same sūtra number in the same place; brackets of the older reading removed |
| 228 | `(Ni. 2-4-562, Yāska` → `(Ni. 3-21, Yāska` | SECOND-PASS Q1: Kannada p.228 reads (ನಿರು. 3-21) for bhyasate rejate iti bhayavepanayoḥ |
| 228 | `" (Pā. Sū. 6-1-[203]) a` → `" (Pā. Sū. 6-1-203) a` | SECOND-PASS Q2: Kannada pp.227-230 has the same sūtra number in the same place; brackets of the older reading removed |
| 229 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 229.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 229.` | SECOND-PASS Q2: running head of Kannada p.229 reads ವ. 13 (Varga 13) |
| 231 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 231.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 231.` | SECOND-PASS Q2: running head of Kannada p.231 reads ವ. 13 (Varga 13) |
| 232 | `7.4)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `7.4)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the section settled from Kannada pp.232-233: 3-1-124, 3-2-129, 7-2-113, 7-4-50 confirmed; 3-685 applied as printed; 6-2-[2] removed (print has none) |
| 232 | `" (Pā. Sū. 7-2-[113]) the loss of the *id* of *idam*; b` → `" (Pā. Sū. 7-2-113) the loss of the *id* of *idam*; b` | SECOND-PASS Q2: Kannada pp.231-234 has the same sūtra number in the same place; brackets of the older reading removed |
| 232 | `(Pā. Sū. 6-1-[128] vārttika)` → `(Pā. 3-685 vārttika)` | SECOND-PASS Q1: Kannada p.232 reads (ಪಾ. 3-685) for īṣākṣādīnāṃ chandasi prakṛtibhāvo vaktavyaḥ; applied as printed, listed in open.tsv |
| 232 | `(Pā. Sū. 3-2-[129]` → `(Pā. Sū. 3-2-129` | SECOND-PASS Q2: Kannada pp.231-234 has the same sūtra number in the same place; brackets of the older reading removed |
| 232 | `(Pā. Sū. 7-4-[50]` → `(Pā. Sū. 7-4-50` | SECOND-PASS Q2: Kannada pp.231-234 has the same sūtra number in the same place; brackets of the older reading removed |
| 232 | `"न नेद्यः" [?] and` → `"न नेद्यः" and` | SECOND-PASS Q2: Kannada p.232 reads ನ ನೇದ್ಯಃ ಅನೇದ್ಯಃ (na nedyaḥ anedyaḥ) |
| 232 | `(Pā. Sū. 6-2-[2]) the accent` → `the accent` | SECOND-PASS S3: Kannada p.232 has no sūtra number after ಶತ್ಪುರುಷೇ ತುಲ್ಯಾರ್ಥ— |
| 232 | `" (Pā. Sū. 3-1-[124]) the affix *ṇyat*; since it is *i` → `" (Pā. Sū. 3-1-124) the affix *ṇyat*; since it is *i` | SECOND-PASS Q2: Kannada pp.231-234 has the same sūtra number in the same place; brackets of the older reading removed |
| 233 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 233.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 233.` | SECOND-PASS Q2: running head of Kannada p.233 reads ವ. 13 (Varga 13) |
| 234 | `worthy of sacrifice [?], *dadhire*` → `worthy of sacrifice, *dadhire*` | SECOND-PASS Q2: Kannada p.234 reads yajñiyāni yajñārhāṇi |
| 235 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 235.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 235.` | SECOND-PASS Q2: running head of Kannada p.235 reads ವ. 13 (Varga 13) |
| 235 | `7.5)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `7.5)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: the section holds no numerals at all (sūtra names only) |
| 237 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 237.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 237.` | SECOND-PASS Q2: running head of Kannada p.237 reads ವ. 13 (Varga 13) |
| 238 | ` *(the Skandasvāmin phrase is partly clotted [?])*` → `` | SECOND-PASS Q2: Kannada p.238 has satyasaṃpattilakṣaṇāyai śriyai, same as the English |
| 239 | `Va. 13 [?]"; centre: "Ṛgvedasaṃhitā"; right: 239.` → `Va. 13"; centre: "Ṛgvedasaṃhitā"; right: 239.` | SECOND-PASS Q2: running head of Kannada p.239 reads ವ. 13 (Varga 13) |
| 239 | `(Ṛ. Saṃ. 5-58-2-[?] [?])` → `(Ṛ. Saṃ. 5-58-2)` | SECOND-PASS Q1: Kannada p.239 reads (ಋ. ಸಂ. 5-58-2) after tveṣaṃ gaṇaṃ tavasaṃ… |
| 239 | ` *(Both reference numerals are small and doubtful [?].)*` → `` | SECOND-PASS Q2: both numbers (5-58-2, 5-54-11) are those of Kannada p.239 |
| 240 | `39 (grammar, noted briefly; sūtras read in three layers, numerals as read [?]):*` → `39 (grammar, noted briefly; sūtras read in three layers):*` | SECOND-PASS Q2: Pā. Sū. 3-1-7 confirmed on Kannada p.240; 3-1-[35] removed (print has none); Uṇ. 1-142 and Pā. 6-4-76 now as printed |
| 240 | `(Pā. Sū. 3-1-[35]) forbids` → `forbids` | SECOND-PASS S3: Kannada p.240 has no sūtra number after अमन्त्रे |
| 240 | `(Uṇ. Sū. 1-[147] [?])` → `(Uṇ. Sū. 1-142)` | SECOND-PASS Q1: Kannada p.240 reads ಇಷಿಯುಧೀಂಧಿ—(ಉ. ಸೂ. 1-142) |
| 240 | `" (Pā. Sū. 6-4-66) ` → `" (Pā. Sū. 6-4-76) ` | SECOND-PASS Q1: Kannada p.240 reads ಇರಯೋರೇ (ಪಾ. ಸೂ. 6-4-76) |
| 241 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 241.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 241.` | SECOND-PASS Q2: running head of Kannada p.241 reads ವ. 14 (Varga 14) |
| 242 | `१४ [?] — *Aṣṭaka 1 · Adhyāya 6 · Varga 14 [?]*` → `१४ — *Aṣṭaka 1 · Adhyāya 6 · Varga 14*` | SECOND-PASS Q2: Kannada p.242 prints ವರ್ಗ-೧೪ for sūkta 88; Devanagari line and its IAST twin settled together |
| 242 | ` *(as printed on the heading line; the digits "३-४०" for the Triṣṭubh Ṛks are read as "2–4` → `` | SECOND-PASS Q2: Kannada p.242 heading line reads ೨-೪. ತ್ರಿಷ್ಟುಪ್, as the English already has (2–4) |
| 243 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 243.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 243.` | SECOND-PASS Q2: running head of Kannada p.243 reads ವ. 14 (Varga 14) |
| 243 | `Ni. 11-13, 14 [?] |` → `Ni. 11-13, 14 |` | SECOND-PASS Q2: Kannada p.243 reads ನಿ. 11-13, 14 after the same quotation |
| 243 | `(Ni. [11-13, 14] [?])` → `(Ni. 11-13, 14)` | SECOND-PASS Q1: Kannada p.243 reads ನಿ. 11-13, 14 after the same quotation |
| 245 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 245.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 245.` | SECOND-PASS Q2: running head of Kannada p.245 reads ವ. 14 (Varga 14) |
| 245 | `(Ni. [11-13] [?])` → `(Ni. 11-13)` | SECOND-PASS Q1: Kannada p.245 reads (ನಿ- 11-13) after maruto mitarāviṇo vā … |
| 245 | ` *(as read, partly clotted [?])*` → `` | SECOND-PASS Q2: Kannada p.245 reads ವರ್ಷಿಷ್ಠಯಾ—ವೃಷ್ಟಿಪ್ರದಾನದಿಂದ ಆಹಾರೋತ್ಪತ್ತಿಗೆ ಸಾಧನಭೂತವಾದ, clear |
| 245 | `(Ni. 11-132 ff.] [?])` → `(Ni. 11-13-14)` | SECOND-PASS Q1: Kannada p.246 reads (ನಿ. 11-13-14) after the quotation |
| 246 | `8.1)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `8.1)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: sūtra numbers of the section (Pā. 8-2-10, 6-1-176, 6-4-157, 3-1-55, 7-4-19 and Uṇ. 1-149) are those of Kannada pp.246-247; brackets removed |
| 246 | `(Pā. Sū. 8-2-[10]` → `(Pā. Sū. 8-2-10` | SECOND-PASS Q2: Kannada pp.245-248 has the same sūtra number in the same place; brackets of the older reading removed |
| 246 | `(Pā. Sū. 6-1-[176]` → `(Pā. Sū. 6-1-176` | SECOND-PASS Q2: Kannada pp.245-248 has the same sūtra number in the same place; brackets of the older reading removed |
| 246 | `(Pā. Sū. 6-4-[157]` → `(Pā. Sū. 6-4-157` | SECOND-PASS Q2: Kannada pp.245-248 has the same sūtra number in the same place; brackets of the older reading removed |
| 246 | ` Pā. Sū. 3-1-[55]` → ` Pā. Sū. 3-1-55` | SECOND-PASS Q2: Kannada pp.245-248 has the same sūtra number in the same place; brackets of the older reading removed |
| 246 | `(Pā. Sū. 7-4-[19]` → `(Pā. Sū. 7-4-19` | SECOND-PASS Q2: Kannada pp.245-248 has the same sūtra number in the same place; brackets of the older reading removed |
| 247 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 247.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 247.` | SECOND-PASS Q2: running head of Kannada p.247 reads ವ. 14 (Varga 14) |
| 249 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 249.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 249.` | SECOND-PASS Q2: running head of Kannada p.249 reads ವ. 14 (Varga 14) |
| 250 | `d (grammar, noted briefly; sūtras read in three layers, numerals as read [?]):*` → `d (grammar, noted briefly; sūtras read in three layers):*` | SECOND-PASS Q2: sūtra numbers of the section (Pā. 8-2-77, 6-1-174, 7-4-85 …) are those of Kannada p.250; brackets removed |
| 250 | `(Pā. Sū. 8-2-[77]` → `(Pā. Sū. 8-2-77` | SECOND-PASS Q2: Kannada pp.249-252 has the same sūtra number in the same place; brackets of the older reading removed |
| 250 | `" (Pā. Sū. 6-1-[174]) t` → `" (Pā. Sū. 6-1-174) t` | SECOND-PASS Q2: Kannada pp.249-252 has the same sūtra number in the same place; brackets of the older reading removed |
| 250 | `(Pā. Sū. 7-4-[85]` → `(Pā. Sū. 7-4-85` | SECOND-PASS Q2: Kannada pp.249-252 has the same sūtra number in the same place; brackets of the older reading removed |
| 251 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 251.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 251.` | SECOND-PASS Q2: running head of Kannada p.251 reads ವ. 14 (Varga 14) |
| 253 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 253.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 253.` | SECOND-PASS Q2: running head of Kannada p.253 reads ವ. 14 (Varga 14) |
| 253 | `(Ni. [1-4] [?])` → `(Ni. 1-9)` | SECOND-PASS Q1: Kannada p.253 reads (ನಿ.1-9) after ಆಥಾಪಿ ಪಾದಪೂರಣಾ ಕಮಿಮಿದ್ |
| 253 | `8.3)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `8.3)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: Pā. Sū. 3-1-80 and 3-4-117 are on Kannada pp.253-254 in the same places; brackets removed |
| 253 | `(Pā. Sū. 3-1-[80]` → `(Pā. Sū. 3-1-80` | SECOND-PASS Q2: Kannada pp.252-255 has the same sūtra number in the same place; brackets of the older reading removed |
| 253 | `(Pā. Sū. 3-4-[117]` → `(Pā. Sū. 3-4-117` | SECOND-PASS Q2: Kannada pp.252-255 has the same sūtra number in the same place; brackets of the older reading removed |
| 255 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 255.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 255.` | SECOND-PASS Q2: running head of Kannada p.255 reads ವ. 14 (Varga 14) |
| 256 | `(Ni. [2-1] [?])` → `(Ni. 3-1)` | SECOND-PASS Q1: Kannada p.256 reads (ನಿ-3-1) after ಧಿಯಂ—ಕರ್ಮವನ್ನು … |
| 257 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 257.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 257.` | SECOND-PASS Q2: running head of Kannada p.257 reads ವ. 14 (Varga 14) |
| 257 | `8.4)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `8.4)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the section now as in Kannada pp.257-258: 3-4-110, 6-4-76, 6-1-49 (as printed); other brackets confirmed |
| 257 | `(Pā. Sū. 6-1-[96])` → `(Pā. Sū. 6-1-49)` | SECOND-PASS Q1: Kannada p.257 reads ಉಸ್ಯಪದಾಂತಾತ್ (ಪಾ. ಸೂ. 6-1-49); applied as printed, listed in open.tsv |
| 257 | `(Pā. Sū. 2-4-[45]` → `(Pā. Sū. 2-4-45` | SECOND-PASS Q2: Kannada pp.256-259 has the same sūtra number in the same place; brackets of the older reading removed |
| 257 | `(Pā. Sū. 3-4-[110]` → `(Pā. Sū. 3-4-110` | SECOND-PASS Q2: Kannada pp.256-259 has the same sūtra number in the same place; brackets of the older reading removed |
| 257 | `" (Pā. Sū. 3-1-[124]) the affix *ṇyat*; since it is *ṇ` → `" (Pā. Sū. 3-1-124) the affix *ṇyat*; since it is *ṇ` | SECOND-PASS Q2: Kannada pp.256-259 has the same sūtra number in the same place; brackets of the older reading removed |
| 257 | `(Pā. Sū. 6-476)` → `(Pā. Sū. 6-4-76)` | SECOND-PASS Q1: Kannada p.257 reads ಇರಯೋರೇ (ಪಾ. ಸೂ. 6-4-76) |
| 259 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 259.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 259.` | SECOND-PASS Q2: running head of Kannada p.259 reads ವ. 14 (Varga 14) |
| 261 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 261.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 261.` | SECOND-PASS Q2: running head of Kannada p.261 reads ವ. 14 (Varga 14) |
| 261 | `8.5)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `8.5)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: Pā. Sū. 3-1-66 and 6-4-104 are on Kannada p.261 in the same places; brackets removed |
| 261 | `(Pā. Sū. 3-1-[66]` → `(Pā. Sū. 3-1-66` | SECOND-PASS Q2: Kannada pp.260-263 has the same sūtra number in the same place; brackets of the older reading removed |
| 261 | `(Pā. Sū. 6-4-[104]` → `(Pā. Sū. 6-4-104` | SECOND-PASS Q2: Kannada pp.260-263 has the same sūtra number in the same place; brackets of the older reading removed |
| 263 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 263.` → `Va. 14"; centre: "Ṛgvedasaṃhitā"; right: 263.` | SECOND-PASS Q2: running head of Kannada p.263 reads ವ. 14 (Varga 14) |
| 264 | `e, noted briefly; sūtras read in three layers, numerals as read [?]):*` → `e, noted briefly; sūtras read in three layers):*` | SECOND-PASS Q2: Pā. Sū. 7-2-106, 4-1-5, 6-1-174 are on Kannada p.264 in the same places; brackets removed |
| 264 | `(Pā. Sū. 7-2-[106]` → `(Pā. Sū. 7-2-106` | SECOND-PASS Q2: Kannada pp.263-266 has the same sūtra number in the same place; brackets of the older reading removed |
| 264 | `(Pā. Sū. 4-1-[5]` → `(Pā. Sū. 4-1-5` | SECOND-PASS Q2: Kannada pp.263-266 has the same sūtra number in the same place; brackets of the older reading removed |
| 264 | `" (Pā. Sū. 6-1-[174]) s` → `" (Pā. Sū. 6-1-174) s` | SECOND-PASS Q2: Kannada pp.263-266 has the same sūtra number in the same place; brackets of the older reading removed |
| 264 | `[*anu*-5] [?]` → `*anu* 9-5` | SECOND-PASS Q1: Kannada p.264 reads ಅನು 9-5 in the same place |
| 265 | `Va. 14 [?]"; centre: "Ṛgvedasaṃhitā"; right: 265.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 265.` | SECOND-PASS Q1: running head of Kannada p.265 reads ವ. 15 (Varga 15) |
| 265 | `(Ai. Brā. [3-10] [?])` → `(Ai. Brā. 3-31)` | SECOND-PASS Q1: Kannada p.265 reads (ಐ. ಬ್ರಾ. 3-31) after ಸದೈವ ಪಂಚಜನೀಯಯಾ ಪರಿದಧ್ಯಾತ್ |
| 265 | `५-१८ — *Aṣṭaka 1 · Adhyāya 6 · Varga 5-18* (the numerals are small and read with doubt [?]` → `१५, १६ — *Aṣṭaka 1 · Adhyāya 6 · Varga 15, 16*` | SECOND-PASS Q1: Kannada p.265 reads ವರ್ಗ- 15, 16 for sūkta 89 |
| 267 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 267.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 267.` | SECOND-PASS Q2: running head of Kannada p.267 reads ವ. 15 (Varga 15) |
| 267 | `(Ni. [12-?] [?])` → `(Ni. 12-39)` | SECOND-PASS Q1: Kannada p.268 reads (ನಿ. 12-39) after ವಿಶ್ವೇ ದೇವಾಃ ಸರ್ವೇ ದೇವಾಃ |
| 268 | `a number of whole sūktas with the Viśvedevas as their deity: in the first maṇḍala, the sūk` → `58 whole sūktas with the Viśvedevas as their deity: in the first maṇḍala, the sūktas 14, 8` | SECOND-PASS Q1: Kannada p.268 prints the whole list (58 sūktas; maṇḍala 1: 14, 89, 90, 105-107, 121, 122; 2: 29, 31; 3: 54; 4: 55; 5: 41-45, 47-51; 6: 49-52; 7: 35-37, 39, 40,  |
| 268 | `9.1)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `9.1)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: Pā. Sū. 6-4-81 and 7-2-15 are on Kannada p.268 in the same places; brackets removed |
| 268 | `(Pā. Sū. 6-4-[81]` → `(Pā. Sū. 6-4-81` | SECOND-PASS Q2: Kannada pp.267-270 has the same sūtra number in the same place; brackets of the older reading removed |
| 268 | `(Pā. Sū. 7-2-[15]` → `(Pā. Sū. 7-2-15` | SECOND-PASS Q2: Kannada pp.267-270 has the same sūtra number in the same place; brackets of the older reading removed |
| 269 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 269.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 269.` | SECOND-PASS Q2: running head of Kannada p.269 reads ವ. 15 (Varga 15) |
| 271 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 271.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 271.` | SECOND-PASS Q2: running head of Kannada p.271 reads ವ. 15 (Varga 15) |
| 272 | `; numerals as read [?]` → `` | SECOND-PASS Q2: Pā. Sū. 3-1-8 and 5-1-176, 6-1 and 6-4 numerals confirmed on Kannada p.272; 7-4-25 and 3-4-[90] removed (print has none); brackets removed |
| 272 | `" (Pā. Sū. 7-4-25) t` → `" t` | SECOND-PASS S3: Kannada p.272 has no sūtra number after अकृत्सार्वधातुकयोर्दीर्घः |
| 272 | `" (Pā. Sū. 6-1-[173]) the case-ending *` → `" (Pā. Sū. 6-1-173) the case-ending *` | SECOND-PASS Q2: Kannada pp.271-274 has the same sūtra number in the same place; brackets of the older reading removed |
| 272 | `(Pā. Sū. 3-3-[96]` → `(Pā. Sū. 3-3-96` | SECOND-PASS Q2: Kannada pp.271-274 has the same sūtra number in the same place; brackets of the older reading removed |
| 272 | `(Pā. Sū. 3-4-[90]) ` → `` | SECOND-PASS S3: Kannada p.272 has no sūtra number after ಆಮೇತಃ— |
| 272 | `(Pā. Sū. 6-4-[120]` → `(Pā. Sū. 6-4-120` | SECOND-PASS Q2: Kannada pp.271-274 has the same sūtra number in the same place; brackets of the older reading removed |
| 273 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 273.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 273.` | SECOND-PASS Q2: running head of Kannada p.273 reads ವ. 15 (Varga 15) |
| 273 | `; the Taittirīya numerals [?].)*` → `.)*` | SECOND-PASS Q2: Tai. Brā. 1-7-10-1 (twice) is on Kannada pp.273-274 in the same places |
| 275 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 275.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 275.` | SECOND-PASS Q2: running head of Kannada p.275 reads ವ. 15 (Varga 15) |
| 275 | ` (Ni. [?-?] [?]);` → ` (Ni. 2-23);` | SECOND-PASS Q1: Kannada p.275 reads (ನಿ. 2-23) after ನಿವಿದಾ ... ಎಂದರ್ಥವು |
| 275 | `adīnā devamātā ‖* (Ni. [?-?] [?]) — **GLOSS**` → `adīnā devamātā ‖* — **GLOSS**` | SECOND-PASS S3: Kannada p.275 has no reference number after this Yāska quotation |
| 276 | `(Tai. Brā. [1-2-10-1] [?])` → `(Tai. Brā. 1-7-10-1)` | SECOND-PASS Q1: Kannada p.274 reads ತೈ. ಬ್ರಾ. 1-7-10-1 after ವಾರುಣೀ ರಾತ್ರಿಃ |
| 276 | `9.3)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `9.3)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: Pā. Sū. 6-4-… numerals confirmed on Kannada p.276-277; 6-1-[32] removed (print has none) |
| 276 | `(Pā. Sū. 6-1-[32]) ` → `` | SECOND-PASS S3: Kannada p.277 has no sūtra number after ಹ್ವಃ ಸಂಪ್ರಸಾರಣಮ್— |
| 276 | `(Pā. Sū. 6-4-[2]` → `(Pā. Sū. 6-4-2` | SECOND-PASS Q2: Kannada pp.275-278 has the same sūtra number in the same place; brackets of the older reading removed |
| 277 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 277.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 277.` | SECOND-PASS Q2: running head of Kannada p.277 reads ವ. 15 (Varga 15) |
| 279 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 279.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 279.` | SECOND-PASS Q2: running head of Kannada p.279 reads ವ. 15 (Varga 15) |
| 280 | `9.4)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `9.4)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: Pā. Sū. 1-2-47, 3-2-90 (and bracketed numerals) are those of Kannada p.280; 6-4-[51] removed (print has none) |
| 280 | `(Pā. Sū. 6-4-[51]) ` → `` | SECOND-PASS S3: Kannada p.280 has no sūtra number after ಣೇರನಿಟಿ- |
| 280 | `(Pā. Sū. 1-2-[47]` → `(Pā. Sū. 1-2-47` | SECOND-PASS Q2: Kannada pp.279-282 has the same sūtra number in the same place; brackets of the older reading removed |
| 280 | `(Pā. Sū. 3-2-70)` → `(Pā. Sū. 3-2-90)` | SECOND-PASS Q1: Kannada p.280 reads ಸೋಮೇ ಸುಞ್ (ಪಾ. ಸೂ. 3-2-90) |
| 280 | `" (Pā. Sū. 3-1-[74]) the *śnu* *vikaraṇa* and *` → `" (Pā. Sū. 3-1-74) the *śnu* *vikaraṇa* and *` | SECOND-PASS Q2: Kannada pp.279-282 has the same sūtra number in the same place; brackets of the older reading removed |
| 281 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 281.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 281.` | SECOND-PASS Q2: running head of Kannada p.281 reads ವ. 15 (Varga 15) |
| 283 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 283.` → `Va. 15"; centre: "Ṛgvedasaṃhitā"; right: 283.` | SECOND-PASS Q2: running head of Kannada p.283 reads ವ. 15 (Varga 15) |
| 283 | `9.5)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `9.5)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: Pā. Sū. 6-4-131, 8-3-60, 8-3-53, 3-3-113 are on Kannada p.283 in the same places; brackets removed |
| 283 | `(Pā. Sū. 6-4-[131]` → `(Pā. Sū. 6-4-131` | SECOND-PASS Q2: Kannada pp.282-285 has the same sūtra number in the same place; brackets of the older reading removed |
| 283 | `" (Pā. Sū. 8-3-[60]) the *ṣatva* for the *s* of *vas*; *` → `" (Pā. Sū. 8-3-60) the *ṣatva* for the *s* of *vas*; *` | SECOND-PASS Q2: Kannada pp.282-285 has the same sūtra number in the same place; brackets of the older reading removed |
| 283 | `(Pā. Sū. 8-3-[53]` → `(Pā. Sū. 8-3-53` | SECOND-PASS Q2: Kannada pp.282-285 has the same sūtra number in the same place; brackets of the older reading removed |
| 283 | `(Pā. Sū. 3-3-[113]` → `(Pā. Sū. 3-3-113` | SECOND-PASS Q2: Kannada pp.282-285 has the same sūtra number in the same place; brackets of the older reading removed |
| 285 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 285.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 285.` | SECOND-PASS Q1: running head of Kannada p.285 reads ವ. 16 (Varga 16) |
| 286 | `(Ṛ. Saṃ. [?]; Āśvalāyana Śrauta-sūtra [?])` → `(Ṛ. Saṃ. 2-4-1; Āśvalāyana Śrauta-sūtra 10-7)` | SECOND-PASS Q1: Kannada p.286 reads ಖಿಲಮಂತ್ರಗಳಲ್ಲಿಯೂ (2-4-1) ಆಶ್ವಲಾಯನ ಶೌತಸೂತ್ರದಲ್ಲಿಯೂ (ಆ. 10-7) |
| 286 | `Sūkta 10-7 of the Ṛg. Saṃ. is addressed to Tārkṣya." *(numerals read with doubt [?])*` → `Sūkta 10-174 of the Ṛg. Saṃ. is addressed to Tārkṣya."` | SECOND-PASS Q1: Kannada p.286 reads ಋ. ಸಂ. 10-174 ನೇ ಸೂಕ್ತವು ತಾರ್ಕ್ಷ್ಯ ದೇವತಾಕವಾಗಿದೆ |
| 287 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 287.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 287.` | SECOND-PASS Q1: running head of Kannada p.287 reads ವ. 16 (Varga 16) |
| 287 | `9.6)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read [?])*` → `9.6)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: Pā. Sū. 1-105, 6-1-157 (from 6-1-156), 6-1-2 … confirmed on Kannada p.287; brackets removed |
| 287 | `(Pā. Sū. 6-2-[106]` → `(Pā. Sū. 6-2-106` | SECOND-PASS Q2: Kannada pp.286-289 has the same sūtra number in the same place; brackets of the older reading removed |
| 287 | `(Pā. Sū. 6-1-156)` → `(Pā. Sū. 6-1-157)` | SECOND-PASS Q1: Kannada p.287 reads ತದ್ಬೃಹತೋಃ ಕರಪತ್ಯೋಃ (ಪಾ. ಸೂ. 6-1-157) |
| 287 | `" (Pā. Sū. 6-2-[140]) t` → `" (Pā. Sū. 6-2-140) t` | SECOND-PASS Q2: Kannada pp.286-289 has the same sūtra number in the same place; brackets of the older reading removed |
| 289 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 289.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 289.` | SECOND-PASS Q1: running head of Kannada p.289 reads ವ. 16 (Varga 16) |
| 289 | `'*pṛṣatyo marutām*' (Ni. [?-?] [?]) — so the Nirukta says."` → `'*pṛṣatyo marutām*' — so the Nirukta says."` | SECOND-PASS S3: Kannada p.289 has pṛṣatyo marutāṃ èṃdu niruktavacanaviruvudu with no reference number |
| 290 | `(Ṛ. Saṃ. [1-?-?] [?])` → `(Ṛ. Saṃ. 1-44-14)` | SECOND-PASS Q1: Kannada p.290 reads (ಋ. ಸಂ. 1-44-14) after the same quotation |
| 290 | `n agnijihvāḥ ‖* (Ṛ. Saṃ. [?-?-?] [?]) — **GLOSS**` → `n agnijihvāḥ ‖* (Ṛ. Saṃ. 3-54-10) — **GLOSS**` | SECOND-PASS Q1: Kannada p.290 reads (ಋ. ಸಂ. 3-54-10) after the same quotation |
| 290 | `(Ṛ. Saṃ. [6-?-?] [?]) — **GLOSS** *(the second half is read with doubt [?])*` → `(Ṛ. Saṃ. 6-21-11) — **GLOSS**` | SECOND-PASS Q1: Kannada p.290 reads (ಋ. ಸಂ. 6-21-11) after ಯೆಃ ಅಗ್ನಿಜಿಹ್ವಾ ಋತಸಾಪ ಆಸುರ್ಯೇ ಮನುಂ ಚಕ್ರುರುಪರಂ ದಸಾಯ; second half agrees |
| 290 | `ā agnijihvāḥ ‖* (Ṛ. Saṃ. [?-?-?] [?]) — **GLOSS**` → `ā agnijihvāḥ ‖* (Ṛ. Saṃ. 6-50-2) — **GLOSS**` | SECOND-PASS Q1: Kannada p.290 reads (ಋ. ಸಂ. 6-50-2) after the same quotation |
| 290 | `m ‖* (Ṛ. Saṃ. [?-?-?] [?]) — *` → `m ‖* (Ṛ. Saṃ. 6-52-13) — *` | SECOND-PASS Q1: Kannada p.290 reads (ಋ. ಸಂ. 6-52-13) after the same quotation |
| 290 | `aḥ ‖* (Ṛ. Saṃ. [?-?-?] [?]) — **` → `aḥ ‖* (Ṛ. Saṃ. 7-66-10) — **` | SECOND-PASS Q1: Kannada p.290 reads (ಋ. ಸಂ. 7-66-10) after the same quotation |
| 290 | `(Ṛ. Saṃ. [10-?-?] [?])` → `(Ṛ. Saṃ. 10-65-7)` | SECOND-PASS Q1: Kannada p.290 reads (ಋ. ಸಂ. 10-65-7) after the same quotation |
| 290 | ` *(The seven citations are given as read; all Ṛgveda reference numerals here are small and` → `` | SECOND-PASS Q2: all seven Ṛgveda references of the list are now those of Kannada p.290 |
| 291 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 291.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 291.` | SECOND-PASS Q1: running head of Kannada p.291 reads ವ. 16 (Varga 16) |
| 291 | `0 (grammar, noted briefly; sūtras read in three layers, numerals as read [?]):*` → `0 (grammar, noted briefly; sūtras read in three layers):*` | SECOND-PASS Q2: Pā. Sū. 3-2-74, 3-2-171 and Ṛ. Saṃ. 1-44-14 are on Kannada p.291/290 in the same places; brackets removed |
| 291 | `(Pā. Sū. 3-2-[74]` → `(Pā. Sū. 3-2-74` | SECOND-PASS Q2: Kannada pp.290-293 has the same sūtra number in the same place; brackets of the older reading removed |
| 291 | `" (Pā. Sū. 3-2-[171]) the affix *kin*; b` → `" (Pā. Sū. 3-2-171) the affix *kin*; b` | SECOND-PASS Q2: Kannada pp.290-293 has the same sūtra number in the same place; brackets of the older reading removed |

### 2026-11-27 second pass, batch m159-308.tsv
| page | old → new | why |
|---|---|---|
| 293 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 293.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 293.` | SECOND-PASS Q1: running head of Kannada p.293 reads ಅ. ೧. ಅ. ೬. ವ. ೧೬ (Varga 16) |
| 295 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 295.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 295.` | SECOND-PASS Q1: running head of Kannada p.295 reads ಅ. ೧. ಅ. ೬. ವ. ೧೬ (Varga 16) |
| 297 | `Va. 15 [?]"; centre: "Ṛgvedasaṃhitā"; right: 297.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 297.` | SECOND-PASS Q1: running head of Kannada p.297 reads ಅ. ೧. ಅ. ೬. ವ. ೧೬ (Varga 16) |
| 299 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 299.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 299.` | SECOND-PASS Q2: running head of Kannada p.299 reads Varga 16, as the English |
| 301 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 301.` → `Va. 16"; centre: "Ṛgvedasaṃhitā"; right: 301.` | SECOND-PASS Q2: running head of Kannada p.301 reads Varga 16, as the English |
| 303 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 303.` → `Va. 17"; centre: "Ṛgvedasaṃhitā"; right: 303.` | SECOND-PASS Q1: running head of Kannada p.303 reads ಅ. ೧. ಅ. ೬. ವ. ೧೭ (Varga 17) |
| 305 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 305.` → `Va. 17"; centre: "Ṛgvedasaṃhitā"; right: 305.` | SECOND-PASS Q1: running head of Kannada p.305 reads ಅ. ೧. ಅ. ೬. ವ. ೧೭ (Varga 17) |
| 307 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 307.` → `Va. 17"; centre: "Ṛgvedasaṃhitā"; right: 307.` | SECOND-PASS Q1: running head of Kannada p.307 reads ಅ. ೧. ಅ. ೬. ವ. ೧೭ (Varga 17) |
| 309 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 309.` → `Va. 17"; centre: "Ṛgvedasaṃhitā"; right: 309.` | SECOND-PASS Q1: running head of Kannada p.309 reads ಅ. ೧. ಅ. ೬. ವ. ೧೭ (Varga 17) |
| 311 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 311.` → `Va. 17"; centre: "Ṛgvedasaṃhitā"; right: 311.` | SECOND-PASS Q1: running head of Kannada p.311 reads ಅ. ೧. ಅ. ೬. ವ. ೧೭ (Varga 17) |
| 313 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 313.` → `Va. 17"; centre: "Ṛgvedasaṃhitā"; right: 313.` | SECOND-PASS Q1: running head of Kannada p.313 reads ಅ. ೧. ಅ. ೬. ವ. ೧೭ (Varga 17) |
| 315 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 315.` → `Va. 18"; centre: "Ṛgvedasaṃhitā"; right: 315.` | SECOND-PASS Q1: running head of Kannada p.315 reads ಅ. ೧. ಅ. ೬. ವ. ೧೮ (Varga 18) |
| 317 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 317.` → `Va. 18"; centre: "Ṛgvedasaṃhitā"; right: 317.` | SECOND-PASS Q1: running head of Kannada p.317 reads ಅ. ೧. ಅ. ೬. ವ. ೧೮ (Varga 18) |
| 319 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 319.` → `Va. 18"; centre: "Ṛgvedasaṃhitā"; right: 319.` | SECOND-PASS Q1: running head of Kannada p.319 reads ಅ. ೧. ಅ. ೬. ವ. ೧೮ (Varga 18) |
| 321 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 321.` → `Va. 18"; centre: "Ṛgvedasaṃhitā"; right: 321.` | SECOND-PASS Q1: running head of Kannada p.321 reads ಅ. ೧. ಅ. ೬. ವ. ೧೮ (Varga 18) |
| 323 | `Va. 16 [?]"; centre: "Ṛgvedasaṃhitā"; right: 323.` → `Va. 18"; centre: "Ṛgvedasaṃhitā"; right: 323.` | SECOND-PASS Q1: running head of Kannada p.323 reads ಅ. ೧. ಅ. ೬. ವ. ೧೮ (Varga 18) |
| 325 | `Va. 17 [?]"; centre: "Ṛgvedasaṃhitā"; right: 325.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 325.` | SECOND-PASS Q1: running head of Kannada p.325 reads ಅ. ೧. ಅ. ೬. ವ. ೧೯ (Varga 19) |
| 327 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 327.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 327.` | SECOND-PASS Q2: running head of Kannada p.327 reads Varga 19, as the English |
| 329 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 329.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 329.` | SECOND-PASS Q2: running head of Kannada p.329 reads Varga 19, as the English |
| 331 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 331.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 331.` | SECOND-PASS Q2: running head of Kannada p.331 reads Varga 19, as the English |
| 333 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 333.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 333.` | SECOND-PASS Q2: running head of Kannada p.333 reads Varga 19, as the English |
| 335 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 335.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 335.` | SECOND-PASS Q2: running head of Kannada p.335 reads Varga 19, as the English |
| 337 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 337.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 337.` | SECOND-PASS Q2: running head of Kannada p.337 reads Varga 19, as the English |
| 339 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 339.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 339.` | SECOND-PASS Q2: running head of Kannada p.339 reads Varga 19, as the English |
| 341 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 341.` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 341.` | SECOND-PASS Q2: running head of Kannada p.341 reads Varga 19, as the English |
| 292 | `(earlier "bhāti [?]"; the lead` → `(earlier "bhāti"; the lead` | SECOND-PASS Q2: Kannada p.292 has ಆತ್ಮೀಯೈಶ್ಚ ಕ್ಷುರ್ಭಿ… (ātmīyaiś cakṣurbhir) as the current reading; the retired reading "bhāti" is history only, mark dropped |
| 296 | `(Kannada script; the clause "dyāvaḥ jyotes tasja iti saṃhitāyāṃ dīrghatvaṃ" is clotted and` → `(Kannada script.)*` | SECOND-PASS Q1: Kannada p.296 reads ದ್ವ್ಯಚೋಽತಸ್ತಿಜ ಇತಿ ಸಂಹಿತಾಯಾಂ ದೀರ್ಘತ್ವಂ (dvyaco 'tastija iti); clause put in the Devanagari and IAST lines, doubt note dropped |
| 296 | `द्यावः ज्योतेस्तस्ज इति` → `द्व्यचोऽतस्तिज इति` | SECOND-PASS Q1: Kannada p.296 reads ದ್ವ್ಯಚೋಽತಸ್ತಿಜ ಇತಿ (dvyaco 'tastija iti); Devanagari and IAST twins applied together |
| 296 | `yaṇādeśaḥ | … saṃhitāyāṃ dīrghatvaṃ` → `yaṇādeśaḥ | dvyaco 'tastija iti saṃhitāyāṃ dīrghatvaṃ` | SECOND-PASS Q1: twin of the Devanagari edit (Kannada p.296 dvyaco 'tastija iti) |
| 299 | `the grammatical tail is compressed [?])*` → `the grammatical tail is compressed)*` | SECOND-PASS Q2: remark about the scan (compressed tail); Kannada p.299 has the tail as continuous text; no place in doubt |
| 300 | `(Āś. [3-9] [?])` → `(Āś. 3-8)` | SECOND-PASS Q1: Kannada p.300 reads (ಆ. ೩-೮) after the sūtra aditir dyaur aditir antarikṣam |
| 300 | `the Aitareya Brāhmaṇa [3-?; 4-?], the Taittirīya Saṃhitā [1-?-?], the Kāṭhaka Saṃhitā [?-?` → `the Aitareya Brāhmaṇa 3-21; 4-27, the Taittirīya Saṃhitā 1-6-1-2, the Kāṭhaka Saṃhitā 5-6;` | SECOND-PASS Q1: Kannada p.300 reads ಐತರೇಯಬ್ರಾಹ್ಮಣ ೩-೨೧ ; ೪-೨೭ ; ತೈತ್ತಿರೀಯಸಂಹಿತಾ ೧-೬-೧-೨ ; ಕಾಠಕಸಂಹಿತಾ ೫-೬ : ೨೨-೬ ; ಬೃಹದಾರಣ್ಯಕೋಪನಿಷತ್ ೪-೨-೯ |
| 300 | `*pañcamānuṣāḥ* (Ṛ. Saṃ. [?]), *janāḥ*, *kṛṣṭayaḥ*, *kṣitayaḥ*, *carṣaṇayaḥ* — are used in ` → `*pañcamānuṣāḥ* (Ṛ. Saṃ. 8-9-2), *janāḥ* (Ṛ. Saṃ. 3-37-9; 3-59-8; 6-14-4; 8-32-22; 9-65-23;` | SECOND-PASS Q1: Kannada pp.300-301 give the reference runs: (ಋ. ಸಂ. ೮-೯-೨) ಜನಾಃ (೩-೩೭-೯ … ೧೦-೪೫-೬) ಕೃಷ್ಟಯಃ (೨-೨-೧೦ … ೧೦-೧೧೯-೬) ಕ್ಷಿತಯಃ (೧-೭-೯ … ೭-೭೯-೧) ಚರ್ಷಣ್ಯಃ (೫-೮೬-೨; ೭-೧೫-೨ |
| 301 | `niveśatāṃ gandharvāḥ pitaro devā asurā rakṣāṃsīti pañcatvam*' [as read, partly clotted [?]` → `nivasatāṃ gandharvāḥ pitaro devā asurā rakṣāṃsīti pañcatvam*'` | SECOND-PASS Q1: Kannada p.301 reads ಮನುಷ್ಯಾಣಾಂ ಪಂಚಾನಾಂ ಕ್ಷಿತೀನಾಂ ನಿವಸತಾಂ ಗಂಧರ್ವಾಃ ಪಿತರೋ ದೇವಾ ಅಸುರಾ ರಕ್ಷಾಂಸೀತಿ ಪಂಚತ್ವಂ (nivasatāṃ); passage legible |
| 301 | `10-178-3-[?] [?], as read "೧೦-೧೪೫-೫" — uncertain)` → `10-178-3)` | SECOND-PASS Q1: Kannada p.301 gives (ಋ. ಸಂ. ೧೦-೧೭೮-೩) for sadyaś cid yaḥ śavasā pañcakṛṣṭīḥ |
| 302 | `(Pā. Sū. 7-440)` → `(Pā. Sū. 7-4-40)` | SECOND-PASS Q1: Kannada p.302 reads (ಪಾ. ಸೂ ೭-೪-೪೦) after ದ್ಯತಿಸ್ಯತಿಮಾಸ್ಥಾಮಿತ್ತಿಕಿತಿ |
| 302 | `तुल्यार्थ…" (Pā. Sū. 6-2-[2]) the first member, an indeclinable, keeps its base accent.` → `तुल्यार्थ…" (Pā. Sū. 6-2-2) the first member, an indeclinable, keeps its base accent.` | SECOND-PASS Q1: Kannada p.302 reads (ಪಾ. ಸೂ. ೬-೨-೨) |
| 302 | `(Rik 89.10)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read` → `(Rik 89.10)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: both numerals of the page (7-4-40, 6-2-2) settled from Kannada p.302 |
| 303 | `converted letter by letter; compressed and read with doubt in places [?])**` → `converted letter by letter; compressed and read with doubt in places)**` | SECOND-PASS Q2: remark about the scan; Kannada p.303 gives the whole Anukramaṇikā block, no place in doubt named |
| 303 | `*bahudevatāka*] [?].` → `*bahudevatāka*].` | SECOND-PASS Q2: Kannada p.303 reads ಬಹುದೇವತಾಕಂ, as the English |
| 303 | `"paryosān kadvato 'paraḥ" is read as printed and not completed [?].)*` → `"paryāsān kadvato 'harahaḥ" is as the Kannada has it and is not completed.)*` | SECOND-PASS Q1: Kannada p.303 reads ಆರಂಭಣೀಯಾಃ ಪರ್ಯಾಸಾನ್ಕದ್ವತೋಽಹರಹಃ ಶಸ್ಯಾನೀತಿ ಹೋತ್ರಕಾ ದ್ವಿತೀಯಾದಿಷ್ಟೇವ (paryāsān kadvato 'harahaḥ) |
| 305 | `(Tai. Brā. [?]).` → `(Tai. Brā.).` | SECOND-PASS S3: Kannada p.305 reads ತೈ. ಬ್ರಾ ಶ್ರುತಿವಚನವಿರುವುದು with no number; number removed with its mark |
| 305 | `(Rik 90.1)** *(grammar page, noted briefly; begins here; sūtras read in three layers, nume` → `(Rik 90.1)** *(grammar page, noted briefly; begins here; sūtras read in three layers)*` | SECOND-PASS Q2: numeral of the page (7-1-36) settled from Kannada p.305 |
| 305 | `(Pā. Sū. 7-1-[36])` → `(Pā. Sū. 7-1-36)` | SECOND-PASS Q1: Kannada p.305 reads (ಪಾ. ಸೂ. ೭-೧-೩೬) |
| 306 | `Pā. Sū. 8-23-14 | iti rephalopaḥ` → `Pā. Sū. 8-3-14 | iti rephalopaḥ` | SECOND-PASS Q1: Kannada p.306 reads ಪಾ. ೮-೩-೧೪, and the Devanagari line already has ८-३-१४ |
| 306 | `"padādilakṣaṇo" and the Pāṇini numeral are read with doubt [?].)*` → `"padādilakṣaṇo" is read with doubt [?].)*` | SECOND-PASS Q1: Pāṇini numeral 8-3-14 settled from Kannada p.306; the word clause remains |
| 307 | `(Rik 90.2)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read ` → `(Rik 90.2)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: the one numeral of the page (7-3-111) settled from Kannada p.307 |
| 307 | `(Pā. Sū. 7-3-[111])` → `(Pā. Sū. 7-3-111)` | SECOND-PASS Q1: Kannada p.307 reads (ಪಾ. ಸೂ. ೭-೩-೧೧೧) |
| 310 | `(Rik 90.3)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read ` → `(Rik 90.3)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the page (3-1-34, 6-2-116, 3-2-61) settled from Kannada p.310 |
| 310 | `(Pā. Sū. 3-1-[34])` → `(Pā. Sū. 3-1-34)` | SECOND-PASS Q1: Kannada p.310 reads (ಪಾ. ಸೂ. ೩-೧-೩೪) |
| 310 | `(Pā. Sū. 6-2-[116])` → `(Pā. Sū. 6-2-116)` | SECOND-PASS Q1: Kannada p.310 reads (ಪಾ. ಸೂ. ೬-೨-೧೧೬) |
| 310 | `(Pā. Sū. 3-2-[61])` → `(Pā. Sū. 3-2-61)` | SECOND-PASS Q1: Kannada p.310 reads (ಪಾ. ಸೂ. ೩-೨-೬೧) |
| 311 | `*(Kannada script; the clause on* suvitāya *is cramped and read in part [?].)*` → `*(Kannada script.)*` | SECOND-PASS Q1: Kannada p.311 has the clause suvitāya | iṇ gatāv ity asmāt karmaṇi niṣṭhā | tanvādīnāṃ chandasi bahulam upasaṃkhyānam ity uvaj; put in the Devanagari and IAST l |
| 311 | `iṇ gatāv iti ktaḥ | svāt karmaṇi niṣṭhā | tenādīnāṃ chandasi bahulam upasaṃkhyānam ity evv` → `iṇ gatāv ity asmāt karmaṇi niṣṭhā | tanvādīnāṃ chandasi bahulam upasaṃkhyānam ity uvaj` | SECOND-PASS Q1: twin of the Devanagari edit (Kannada p.311) |
| 313 | `तै. ब्रा. ३-८-१४-३ । इति` → `तै. ब्रा. २-७-१४-२ । इति` | SECOND-PASS Q1: Kannada p.313 reads ತೈ. ಬ್ರಾ. ೨-೭-೧೪-೨; Devanagari and IAST twins together |
| 313 | `Tai. Brā. 3-8-14-3 [?] | iti` → `Tai. Brā. 2-7-14-2 | iti` | SECOND-PASS Q1: Kannada p.313 reads ತೈ. ಬ್ರಾ. ೨-೭-೧೪-೨ |
| 313 | `(Tai. Brā. [3-8-14-3] [?])` → `(Tai. Brā. 2-7-14-2)` | SECOND-PASS Q1: Kannada p.313 reads ತೈ. ಬ್ರಾ. ೨-೭-೧೪-೨ |
| 315 | `*(application note: the Āśvalāyana Gṛhya numeral is read with doubt [?].)*` → `` | SECOND-PASS Q1: Kannada p.315 reads ಆ. ಗೃ ೧-೨೪-೧೪; numeral put in the Devanagari and IAST lines (24-14 became 1-24-14), doubt note dropped |
| 315 | `आ. गृ. सू. २४-१४` → `आ. गृ. १-२४-१४` | SECOND-PASS Q1: Kannada p.315 reads ಆ. ಗೃ ೧-೨೪-೧೪; Devanagari and IAST twins together |
| 315 | `Ā. Gṛ. Sū. 24-14 | iti` → `Ā. Gṛ. 1-24-14 | iti` | SECOND-PASS Q1: Kannada p.315 reads ಆ. ಗೃ ೧-೨೪-೧೪ |
| 315 | `*madhu vātā ṛtāyate*' (Ā. Gṛ. Sū. 24-14)` → `*madhu vātā ṛtāyate*' (Ā. Gṛ. 1-24-14)` | SECOND-PASS Q1: Kannada p.315 reads ( ಆ. ಗೃ. ೧-೨೪-೧೪ ) |
| 315 | `पा. सू. ४-४-१२१-३` → `पा. सू. ४-४-१२८-२` | SECOND-PASS Q1: Kannada p.315-316 reads ಪಾ. ೪-೪-೧೨೮-೨; Devanagari and IAST twins together |
| 315 | `Pā. Sū. 4-4-121-3 [?] | iti luk` → `Pā. Sū. 4-4-128-2 | iti luk` | SECOND-PASS Q1: Kannada p.315-316 reads ಪಾ. ೪-೪-೧೨೮-೨ |
| 316 | `(Āś. Gṛ. [1-24-14] [?])` → `(Āś. Gṛ. 1-24-14)` | SECOND-PASS Q2: Kannada p.316 reads (ಆ. ಗೃ. ೧-೨೪-೧೪) |
| 318 | `Pā. Sū. 4-1-[2] [?] iti prāgdīvya` → `Pā. Sū. 4-1-85-2 iti prāgdīvya` | SECOND-PASS Q1: Kannada p.318 reads ಪಾ. ೪ ೧ ೮೫. ೨ |
| 318 | `(Pā. Sū. 4-1-[2] [?])` → `(Pā. Sū. 4-1-85-2)` | SECOND-PASS Q1: Kannada p.318 reads ಪಾ. ೪ ೧ ೮೫. ೨ |
| 321 | `(Ṛ. Saṃ. [1-?-?; 3-?-?; 5-?-?]; [?] — numerals read with doubt)` → `(Ṛ. Saṃ. 1-166-5; 3-34-10; 5-7-4; 5-41-8)` | SECOND-PASS Q1: Kannada p.321 reads (ಋ. ಸಂ. ೧-೧೬೬-೫ ; ೩-೩೪-೧೦ ; ೫-೭-೪ ; ೫-೪೧-೮) |
| 321 | `(Ṛ. Saṃ. [3-8-?; 3-8-?; 3-8-?] [?])` → `(Ṛ. Saṃ. 3-8-1; 3-8-3; 3-8-6)` | SECOND-PASS Q1: Kannada p.321 reads ಋ. ಸಂ. ೩-೮-೧ ; ೩-೮-೩ ; ೩-೮-೬ |
| 321 | `made of wood (Ṛ. Saṃ. [?]);` → `made of wood (Ṛ. Saṃ. 2-37-3; 3-53-20; 6-47-26);` | SECOND-PASS Q1: Kannada p.321 reads ಋ. ಸಂ. ೨-೩೭-೩ ; ೩-೫೩-೨೦ ; ೬-೪೭-೨೬ |
| 321 | `(Ṛ. Saṃ. [1-?-?]; Vāj. Saṃ. [10-?] [?]).` → `(Ṛ. Saṃ. 1-91-6; Vāj. Saṃ. 10-23).` | SECOND-PASS Q1: Kannada p.321 reads ಋ. ಸಂ. ೧-೯೧-೬ ; ವಾ. ಸಂ. ೧೦-೨೩ |
| 321 | ` *(the lists of reference numerals are in small Kannada digits, not verified [?])*` → `` | SECOND-PASS Q1: all four lists settled from Kannada p.321; doubt note dropped |
| 323 | `saptadhāmabhiḥ ‖* (Ṛ. Saṃ. [reference not printed on p. 323 [?]])` → `saptadhāmabhiḥ ‖* (Ṛ. Saṃ. [reference not printed on p. 323])` | SECOND-PASS Q2: Kannada p.323 prints the citation with no reference, as the English says |
| 323 | `samūḷham asya pāṃsure ‖* (Ṛ. Saṃ. [reference not printed on p. 323 [?]])` → `samūḷham asya pāṃsure ‖* (Ṛ. Saṃ. [reference not printed on p. 323])` | SECOND-PASS Q2: Kannada p.323 prints the citation with no reference, as the English says |
| 324 | `at the right of each citation, read with doubt [?]):*` → `at the right of each citation):*` | SECOND-PASS Q2: the numerals of the page agree with Kannada p.324 after the correction of Ṛ. Saṃ. 1-22 below |
| 324 | `(Ṛ. Saṃ. [1-22-18, 19, 20 as read] [?])` → `(Ṛ. Saṃ. 1-22-16, 17, 18)` | SECOND-PASS Q1: Kannada p.324 reads (ಋ. ಸಂ. ೧-೨೨-೧೬,೧೭, ೧೮) |
| 325 | `converted letter by letter; compressed and read with doubt in places [?])**` → `converted letter by letter; compressed and read with doubt in places)**` | SECOND-PASS Q2: remark about the scan; Kannada p.325 gives the whole Anukramaṇikā block, no place in doubt named |
| 326 | `Varga 19, 20, 21, 22, 23 [?]** *(the five varga numerals, in small Kannada digits, as read` → `Varga 19, 20, 21, 22, 23**` | SECOND-PASS Q2: Kannada p.326 reads ವರ್ಗ—೧೯, ೨೦, ೨೧, ೨೨, ೨೩, as the English |
| 327 | `praṇītyā pravṛttyarthakeṇa [?] prakṛṣṭanayanena` → `praṇītyā tvatkartṛkeṇa prakṛṣṭanayanena` | SECOND-PASS Q1: Kannada p.327 reads ಪ್ರಣೀತ್ಯಾ ತ್ವತ್ಕರ್ತೃಕೇಣ ಪ್ರಕೃಷ್ಟನಯನೇನ; IAST and Devanagari twins together |
| 327 | `प्रणीत्या प्रवृत्त्यर्थकेण प्रकृष्टनयनेन` → `प्रणीत्या त्वत्कर्तृकेण प्रकृष्टनयनेन` | SECOND-PASS Q1: twin of the IAST edit (Kannada p.327 ತ್ವತ್ಕರ್ತೃಕೇಣ) |
| 327 | `[the words *pravṛttyarthakeṇa* in the print are doubtful [?]]` → `*tvatkartṛkeṇa* [effected by you]` | SECOND-PASS Q1: Kannada p.327 reads ತ್ವತ್ಕರ್ತೃಕೇಣ (having you as agent) |
| 327 | `(Pā. Sū. 64-162)` → `(Pā. Sū. 6-4-162)` | SECOND-PASS Q1: Kannada p.327 reads ಪಾ. ೬-೪-೧೬೨ |
| 327 | ` *(Grammar tail, noted briefly; the numerals read with doubt [?].)*` → `` | SECOND-PASS Q2: both numerals of the tail (6-4-162, 7-1-85) agree with Kannada p.327 |
| 329 | `*yajoci…* [sūtra as printed, clotted [?]]` → `*yajoci ca*` | SECOND-PASS Q1: Kannada p.329 reads ಯಜೋಚಿಚ (yajoci ca) |
| 329 | `(Pā. Sū. 7-4-82 [?])` → `(Pā. Sū. 7-4-82)` | SECOND-PASS Q2: Kannada p.329 reads (ಪಾ. ಸೂ. ೭-೪-೮೨) |
| 329 | ` *(Numerals read with doubt [?].)*` → `` | SECOND-PASS Q2: numerals of the page (7-4-82, 6-2-49, 6-5-162) all agree with Kannada p.329 |
| 330 | `(थो न्थः, [?])` → `(थो न्थः)` | SECOND-PASS S3: Kannada p.330 reads ಥೋಂಥಃ—ಸೂತ್ರದಿಂದ with no number; the empty reference and its mark removed |
| 331 | `(*uttarapadādyudāttatva*) [sūtra as cited, clotted [?]]` → `(*uttarapadādyudāttatva*) [sūtra as cited, clotted]` | SECOND-PASS Q2: Kannada p.331 reads ಬಹುವ್ರೀಹೌ ಕ್ರತ್ವಾದಯಶ್ಚ… ಉತ್ತರಪದಾದ್ಯುದಾತ್ತತ್ವಂ, as the English |
| 331 | `the initial-acute accent [details clotted [?]]` → `the initial-acute accent [details clotted]` | SECOND-PASS Q2: Kannada p.331 reads ದಕ್ಷತೇಽನೇನೇತಿ ದಕ್ಷೋ ಬಲಂ । ಕರಣೇ ಘಞ್ । ಇತ್ತ್ವಾದಾದ್ಯುದಾತ್ತತ್ವಂ, as the English |
| 332 | `In Ṛ. Saṃ. 10-[?]-1 alone` → `In Ṛ. Saṃ. 10-87-1 alone` | SECOND-PASS Q1: Kannada p.332 reads ಋ. ಸ. ೧೦-೮೭-೧ ರಲ್ಲಿ ಮಾತ್ರ |
| 332 | `'*karmapaiḥ puruṣaiḥ*' [as read, doubtful [?]].` → `'*karmaparaiḥ puruṣaiḥ*'.` | SECOND-PASS Q1: Kannada p.332 reads ಕರ್ಮಪರೈಃ ಪುರುಷೈಃ |
| 332 | `*pājaḥ* (Ni. 2-9 [?])` → `*pājaḥ* (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.332 reads (ನಿ. ೩-೯) |
| 332 | `(Ṛ. Saṃ. 1-[?]-3 [?]; the printed numerals, read as "१-१४७-३" [?], are doubtful) *(the Saṃ` → `(Ṛ. Saṃ. 1-147-3)` | SECOND-PASS Q1: Kannada p.332 reads (ಋ. ಸಂ. ೧-೧೪೭-೩) with ರರಕ್ಷ ತಾನ್ ಸುಕೃತೋ ವಿಶ್ವವೇದಾ ದಿಪ್ಸಂತ ಇದ್ರಿಪವೋ ನಾಹ ದೇಭುಃ, as the Saṃhitā text |
| 333 | `3-[?]-[?] [?]; numerals as printed, small and doubtful)` → `3-15-3)` | SECOND-PASS Q1: Kannada p.333 reads (ಋ. ಸಂ. ೩-೧೫-೩) |
| 333 | `3-[?]-6 [?])` → `3-54-6)` | SECOND-PASS Q1: Kannada p.333 reads (ಋ. ಸಂ. ೩ ೫೪-೬) |
| 333 | `In Ṛ. Saṃ. 10-[?]-2 [?] the explanation` → `In Ṛ. Saṃ. 10-139-2 the explanation` | SECOND-PASS Q1: Kannada p.333 reads ಋ. ಸಂ. ೧೦-೧೩೯-೨. ನೆಯ ಋಕ್ಕಿನಲ್ಲಿ ನೃಭಿಃ ರಶ್ಮಿಭಿಃ ಪ್ರಕಾಶಮಾನಃ |
| 333 | `prakāśamānaḥ*' [as read, doubtful [?]].` → `prakāśamānaḥ*'.` | SECOND-PASS Q2: the Kannada p.333 has ನೃಭಿಃ ರಶ್ಮಿಭಿಃ ಪ್ರಕಾಶಮಾನಃ, as the English |
| 333 | `*(Numerals read with doubt [?]; the last lines are partly smudged.)*` → `*(The last lines are partly smudged.)*` | SECOND-PASS Q2: numerals of the page (6-2-118, 6-2-119) agree with Kannada p.333 |
| 334 | `, Pā. Sū. 6-2-139 [?])` → `)` | SECOND-PASS S3: Kannada p.334 reads ಗತಿಕಾರಕೋಪಪದಾತ್ ಕೃತ್—ಎಂಬುದರಿಂದ with no number; number removed with its mark |
| 336 | `kṛṇvan vrajanasya rājā` → `kṛṇvan vṛjanasya rājā` | SECOND-PASS Q1: Kannada p.336 reads ಕೃಣ್ವನ್ ವೃಜನಸ್ಯ ರಾಜಾ; IAST and Devanagari twins together |
| 336 | `कृण्वन्वजनस्य` → `कृण्वन्वृजनस्य` | SECOND-PASS Q1: twin of the IAST edit (Kannada p.336 ವೃಜನಸ್ಯ) |
| 336 | `(Ṛ. Saṃ. 9-[?]-10 [?], numerals as printed, doubtful; *vrajanasya* as read [?])` → `(Ṛ. Saṃ. 9-97-10)` | SECOND-PASS Q1: Kannada p.336 reads (ಋ. ಸಂ. ೯-೯೭-೧೦) and ವೃಜನಸ್ಯ |
| 337 | `9-[?]-[?] [?])` → `9-97-24)` | SECOND-PASS Q1: Kannada p.337 reads (ಋ. ಸಂ. ೯-೯೭-೨೪) after ಪವಿತ್ರೇಭಿಃ ಪವಮಾನೋ ನೃಚಕ್ಷಾ |
| 337 | `Ṛ. Saṃ. [9-?]-? [?], in the same order, the sūkta's printed in full there [as read, doubtf` → `Ṛ. Saṃ. 9-88-8, in the same order.` | SECOND-PASS Q1: Kannada p.337 reads ಇದೇ ಅನುಪೂರ್ವಿಯಿಂದ ಋ. ಸಂ. ೯-೮೮-೮ ನೇ ಋಕ್ಕಿನಲ್ಲಿಯೂ ಪಠಿತವಾಗಿದೆ |
| 337 | `(Ni. 6-[?] [?]) — from the root` → `(Ni. 6-1) — from the root` | SECOND-PASS Q1: Kannada p.337 reads ಶೋಚತೇರ್ಜ್ವಲತಿ ಕರ್ಮಣಃ (ನಿ. ೬-೧) |
| 337 | `*niśi-kram-asmāt-pāpakam* (Ni. 6-[?] [?]) ['sin has been …(?) from him'; as read, doubtful` → `*niṣiktam asmāt pāpakam* (Ni. 6-1) ['sin has been driven away from him'],` | SECOND-PASS Q1: Kannada p.337 reads ನಿಷಿಕ್ತಮಸ್ಮಾತ್ಪಾಪಕಂ (ನಿ. ೬-೧) ಪಾಪವು ಇವನಿಂದ ದೂಡಲ್ಪಟ್ಟಿದೆ |
| 337 | `6-[?]-3 [?])` → `6-74-3)` | SECOND-PASS Q1: Kannada p.337 reads (ಋ. ಸಂ. ೬-೭೪-೩) after ಅವಸ್ಯತಂ ಮುಂಚತಂ |
| 337 | `8-[?]-[?] [?])` → `8-48-7)` | SECOND-PASS Q1: Kannada p.337 reads (ಋ. ಸಂ. ೮-೪೮-೭) after ಸೋಮ ರಾಜನ್ … |
| 338 | `U. 3-96 [?])` → `U. 3-376)` | SECOND-PASS Q1: Kannada p.338 reads (ಉ. ಸೂ. ೩-೩೭೬) in the grammar section for ಶ್ರುದಕ್ಷಿಸ್ಪೃಹಿಗ್ರಹಿಭ್ಯ ಆಯ್ಯಃ |
| 339 | `śāyajapīti [?] hau` → `śāyajapīti hau` | SECOND-PASS Q2: Kannada p.339 reads ಶಾಯಜಪೀತಿ ಹೌ ಶ್ನಾಪ್ರತ್ಯಯಸ್ಯ ಶಾಯಜಾದೇಶಃ with no further word, as the English |
| 339 | `*śāyajapi*…, partly read [?]].` → `*śāyajapi*…, partly read].` | SECOND-PASS Q2: Kannada p.339 reads ಶಾಯಜಪೀತಿ, as the English |
| 339 | `*(Numerals as read, doubtful [?].)*` → `` | SECOND-PASS Q2: numerals of the page (Ā. 2-9, 3-7, 4-3; Pā. Sū. 6-3-132) settled from Kannada p.339 |
| 339 | `(Pā. Sū. 63-132)` → `(Pā. Sū. 6-3-132)` | SECOND-PASS Q1: Kannada p.339 reads ಪಾ. ಸೂ. ೬-೩-೧೩೨ |
| 339 | `Pā. Sū. 63-132 | iti` → `Pā. Sū. 6-3-132 | iti` | SECOND-PASS Q1: Kannada p.339 reads ಪಾ. ಸೂ. ೬-೩-೧೩೨ |
| 339 | `पा. सू. ६३-१३२` → `पा. सू. ६-३-१३२` | SECOND-PASS Q1: Kannada p.339 reads ಪಾ. ಸೂ. ೬-೩-೧೩೨; Devanagari and IAST twins together |
| 339 | `आ. ३-३७६ इति` → `आ. ३-७ इति` | SECOND-PASS Q1: Kannada p.339-340 reads ಆ. ೩-೭; Devanagari and IAST twins together |
| 339 | `Ā. 3-376 iti` → `Ā. 3-7 iti` | SECOND-PASS Q1: Kannada p.339-340 reads ಆ. ೩-೭ |
| 339 | `आ. ४-२ इति` → `आ. ४-३ इति` | SECOND-PASS Q1: Kannada p.340 reads ಆ. ೪-೩ |
| 339 | `(Ā. 3-376).` → `(Ā. 3-7).` | SECOND-PASS Q1: Kannada p.340 reads ಆ. ೩-೭ |
| 339 | `(Ā. 4-2).` → `(Ā. 4-3).` | SECOND-PASS Q1: Kannada p.340 reads ಆ. ೪-೩ |
| 340 | `papriṃ*' (Ā. 3-2 [?]). In the` → `papriṃ*' (Ā. 3-7). In the` | SECOND-PASS Q1: Kannada p.340 reads (ಆ. ೩-೭) |
| 340 | `(Ā. 4-3 [?])` → `(Ā. 4-3)` | SECOND-PASS Q2: Kannada p.340 reads (ಆ. ೪-೩) |
| 341 | `(Ṛ. Saṃ. 4-266;` → `(Ṛ. Saṃ. 4-26-6;` | SECOND-PASS Q1: Kannada p.341 reads (ಋ. ಸಂ. ೪-೨೬-೬) |
| 341 | `9-[?]-4 [?])` → `9-62-4)` | SECOND-PASS Q1: Kannada p.341 reads (೯-೬೨-೪) after ಅಸಾವ್ಯಂಶುರ್ಮದಾಯಾಪ್ಸು ದಕ್ಷೋ ಗಿರಿಷ್ಠಾಃ |
| 341 | `3-48-2; 5-43-4; 9-84-3; 9-59-6 [?] and others (numerals as read from small digits, all dou` → `3-48-2; 5-43-4; 9-85-10; 9-98-9 and others` | SECOND-PASS Q1: Kannada p.341 reads ೩-೪೮-೨ ; ೫-೪೩-೪ ; ೯-೮೫-೧೦ । ೯-೯೮-೯ |
| 342 | `9-[?]-3 [?])` → `9-84-3)` | SECOND-PASS Q1: Kannada p.342 reads (ಋ. ಸಂ. ೯-೮೪-೩) after ಆ ಯೋ ಗೋಭಿಃ ಸೃಜ್ಯತ |
| 342 | `Ṛ. Saṃ. 3-40-13 [?]; 9-97-24; 9-54-3; 9-85-6 [?] and others (numerals as read, doubtful)` → `Ṛ. Saṃ. 2-40-1-5; 9-97-24; 9-54-3; 9-89-6 and others` | SECOND-PASS Q1: Kannada p.342 reads ಋ. ಸಂ. ೨-೪೦-೧-೫ ; ೯-೯೭-೨೪ ; ೯-೫೪-೩ ; ೯-೮೯-೬ (first as printed) |
| 342 | `heḷate* in the Nirukta (Ni. 2-[?] [?])` → `heḷate* in the Nirukta (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.342 reads (ನಿ. ೩-೯) |
| 342 | `1-24-11; 1-[?]-3 [?]; 6-[?]-1 [?]; 10-3[?]-8 [?] and other Ṛks (numerals as read, doubtful` → `1-24-11; 1-138-3; 6-41-1; 10-32-8 and other Ṛks` | SECOND-PASS Q1: Kannada p.342 reads ಋ. ಸಂ. ೧-೨೪-೧೧ ; ೧-೧೩೮-೩ ; ೬-೪೧-೧ ; ೧೦-೩೨-೮ |
| 294 | `(Rik 89.8)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read ` → `(Rik 89.8)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: all numerals of the page settled against Kannada pp.294-295 (7-1-10, 3-1-74, 3-385, 3-1-107, 7-4-61, 3-1-86, 7-4-42, 6-2-48) |
| 294 | `बहुलं छन्दसि" (Pā. Sū. 7-1-[10])` → `बहुलं छन्दसि" (Pā. Sū. 7-1-10)` | SECOND-PASS Q1: Kannada p.294 reads (ಪಾ. ಸೂ. ೭-೧-೧೦) |
| 294 | `शृ च" (Pā. Sū. 3-1-64)` → `शृ च" (Pā. Sū. 3-1-74)` | SECOND-PASS Q1: Kannada p.294 reads ಶ್ರುವಃ ಶೃಚ (ಪಾ. ಸೂ. ೩-೧-೭೪) |
| 294 | `(Uṇ. Sū. 2-385)` → `(Uṇ. Sū. 3-385)` | SECOND-PASS Q1: Kannada p.294 reads (ಉ. ಸೂ. ೩-೩೮೫) |
| 294 | `खयः" (Pā. Sū. 7-4-[61])` → `खयः" (Pā. Sū. 7-4-61)` | SECOND-PASS Q1: Kannada pp.294-295 read ಶರ್ಪೂರ್ವಾಃ ಖಯಃ (ಪಾ. ಸೂ. ೭-೪-೬೧) |
| 294 | `अङ्" (Pā. Sū. 3-1-[86])` → `अङ्" (Pā. Sū. 3-1-86)` | SECOND-PASS Q1: Kannada p.295 reads ಲಿಜ್ಯಾಶಿಷ್ಯಜ್ (ಪಾ. ಸೂ. ೩-೧-೮೬) |
| 294 | `हिः" (Pā. Sū. 7-4-[42])` → `हिः" (Pā. Sū. 7-4-42)` | SECOND-PASS Q1: Kannada p.295 reads ದಧಾತೇರ್ಹಿಃ (ಪಾ. ಸೂ. ೭-೪-೪೨) |
| 294 | `कर्मणि" (Pā. Sū. 6-2-[48])` → `कर्मणि" (Pā. Sū. 6-2-48)` | SECOND-PASS Q1: Kannada p.295 reads ತೃತೀಯಾಕರ್ಮಣಿ (ಪಾ. ಸೂ. ೬-೨-೪೮) |
| 297 | `(Rik 89.9)** *(grammar page, noted briefly; sūtras read in three layers, numerals as read ` → `(Rik 89.9)** *(grammar page, noted briefly; sūtras read in three layers)*` | SECOND-PASS Q2: numerals of the page settled against Kannada pp.297-298 (6-3-133, 7-2-101; no number printed for saptamyās tral) |

### 2026-11-27 second pass, batch m159-308_2.tsv
| page | old → new | why |
|---|---|---|
| 311 | `तेनादीनां छन्दसि` → `तन्वादीनां छन्दसि` | SECOND-PASS Q1: Kannada p.311 reads ತನ್ವಾದೀನಾಂ ಛಂದಸಿ (tanvādīnāṃ); Devanagari twin of the applied IAST edit |
| 311 | `गताविति क्तः । स्वात्कर्मणि` → `गतावित्यस्मात्कर्मणि` | SECOND-PASS Q1: Kannada p.311 reads ಇಣ್ ಗತಾವಿತ್ಯಸ್ಮಾತ್ಕರ್ಮಣಿ ನಿಷ್ಠಾ; Devanagari twin of the applied IAST edit |
| 311 | `मित्येव्वज्` → `मित्युवज्` | SECOND-PASS Q1: Kannada p.311 reads ಮಿತ್ಯುವಜ್; Devanagari twin of the applied IAST edit |
| 318 | `४-१-[२]` → `४-१-८५-२` | SECOND-PASS Q1: Kannada p.318 reads ಪಾ. ೪ ೧ ೮೫. ೨ (4-1-85-2); Devanagari twin of the applied IAST and English edits |
| 333 | `, [?]); *śobhano dakṣo` → `); *śobhano dakṣo` | SECOND-PASS S3: Kannada p.333 gives no number after ಇತ್ಯಾದಿರ್ನಿತ್ಯಮ್; empty reference and its mark removed |
| 297 | ` (Pā. Sū. 5-3-[10])` → `` | SECOND-PASS S3: Kannada p.297 reads ಸಪ್ತಮ್ಯಾಸ್ತ್ರಲ್—ಎಂಬುದರಿಂದ with no number; number removed with its mark |
| 297 | `(Pā. Sū. 6-3-[133])` → `(Pā. Sū. 6-3-133)` | SECOND-PASS Q1: Kannada p.297 reads (ಪಾ. ಸೂ. ೬-೩-೧೩೩) |
| 297 | `(Pā. Sū. 7-4-1)` → `(Pā. Sū. 7-2-101)` | SECOND-PASS Q1: Kannada p.298 reads ಜರಾಯಾ ಜರಸನ್ಯತರಸ್ಯಾಮ್—(ಪಾ. ಸೂ. ೭-೨-೧೦೧) |

### 2026-11-27 second pass, batch m180-329.tsv
| page | old → new | why |
|---|---|---|
| 343 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 343` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 343` | SECOND-PASS Q2: running head of Kannada p.343 reads ವ. (Varga 19) [q180] |
| 345 | `Va. 19 [?]"; centre: "Ṛgvedasaṃhitā"; right: 345` → `Va. 19"; centre: "Ṛgvedasaṃhitā"; right: 345` | SECOND-PASS Q2: running head of Kannada p.345 reads ವ. (Varga 19) [q187] |
| 347 | `Va. 20 [?]"; centre: "Ṛgvedasaṃhitā"; right: 347` → `Va. 20"; centre: "Ṛgvedasaṃhitā"; right: 347` | SECOND-PASS Q2: running head of Kannada p.347 reads ವ. (Varga 20) [q192] |
| 349 | `Va. 20 [?]"; centre: "Ṛgvedasaṃhitā"; right: 349` → `Va. 20"; centre: "Ṛgvedasaṃhitā"; right: 349` | SECOND-PASS Q2: running head of Kannada p.349 reads ವ. (Varga 20) [q198] |
| 351 | `Va. 20 [?]"; centre: "Ṛgvedasaṃhitā"; right: 351` → `Va. 20"; centre: "Ṛgvedasaṃhitā"; right: 351` | SECOND-PASS Q2: running head of Kannada p.351 reads ವ. (Varga 20) [q203] |
| 355 | `Va. 20 [?]"; centre: "Ṛgvedasaṃhitā"; right: 355` → `Va. 20"; centre: "Ṛgvedasaṃhitā"; right: 355` | SECOND-PASS Q2: running head of Kannada p.355 reads ವ. (Varga 20) [q215] |
| 357 | `Va. 20 [?]"; centre: "Ṛgvedasaṃhitā"; right: 357` → `Va. 20"; centre: "Ṛgvedasaṃhitā"; right: 357` | SECOND-PASS Q2: running head of Kannada p.357 reads ವ. (Varga 20) [q218] |
| 359 | `Va. 20 [?]"; centre: "Ṛgvedasaṃhitā"; right: 359` → `Va. 20"; centre: "Ṛgvedasaṃhitā"; right: 359` | SECOND-PASS Q2: running head of Kannada p.359 reads ವ. (Varga 20) [q230] |
| 363 | `Va. 21 [?]"; centre: "Ṛgvedasaṃhitā"; right: 363` → `Va. 21"; centre: "Ṛgvedasaṃhitā"; right: 363` | SECOND-PASS Q2: running head of Kannada p.363 reads ವ. (Varga 21) [q253] |
| 365 | `Va. 21 [?]"; centre: "Ṛgvedasaṃhitā"; right: 365` → `Va. 21"; centre: "Ṛgvedasaṃhitā"; right: 365` | SECOND-PASS Q2: running head of Kannada p.365 reads ವ. (Varga 21) [q258] |
| 367 | `Va. 21 [?]"; centre: "Ṛgvedasaṃhitā"; right: 367` → `Va. 21"; centre: "Ṛgvedasaṃhitā"; right: 367` | SECOND-PASS Q2: running head of Kannada p.367 reads ವ. (Varga 21) [q264] |
| 369 | `Va. 21 [?]"; centre: "Ṛgvedasaṃhitā"; right: 369` → `Va. 21"; centre: "Ṛgvedasaṃhitā"; right: 369` | SECOND-PASS Q2: running head of Kannada p.369 reads ವ. (Varga 21) [q271] |
| 371 | `Va. 21 [?]"; centre: "Ṛgvedasaṃhitā"; right: 371` → `Va. 21"; centre: "Ṛgvedasaṃhitā"; right: 371` | SECOND-PASS Q2: running head of Kannada p.371 reads ವ. (Varga 21) [q278] |
| 373 | `Va. 21 [?]"; centre: "Ṛgvedasaṃhitā"; right: 373` → `Va. 21"; centre: "Ṛgvedasaṃhitā"; right: 373` | SECOND-PASS Q2: running head of Kannada p.373 reads ವ. (Varga 21) [q282] |
| 377 | `Va. 22 [?]"; centre: "Ṛgvedasaṃhitā"; right: 377` → `Va. 22"; centre: "Ṛgvedasaṃhitā"; right: 377` | SECOND-PASS Q2: running head of Kannada p.377 reads ವ. (Varga 22) [q299] |
| 379 | `Va. 22 [?]"; centre: "Ṛgvedasaṃhitā"; right: 379` → `Va. 22"; centre: "Ṛgvedasaṃhitā"; right: 379` | SECOND-PASS Q2: running head of Kannada p.379 reads ವ. (Varga 22) [q304] |
| 381 | `Va. 22 [?]"; centre: "Ṛgvedasaṃhitā"; right: 381` → `Va. 22"; centre: "Ṛgvedasaṃhitā"; right: 381` | SECOND-PASS Q2: running head of Kannada p.381 reads ವ. (Varga 22) [q306] |
| 383 | `Va. 22 [?]"; centre: "Ṛgvedasaṃhitā"; right: 383` → `Va. 22"; centre: "Ṛgvedasaṃhitā"; right: 383` | SECOND-PASS Q2: running head of Kannada p.383 reads ವ. (Varga 22) [q311] |
| 353 | `Va. 20 [?]"; centre: "Ṛgvedasaṃhitā"; right: 353.` → `Va. 20"; centre: "Ṛgvedasaṃhitā"; right: 353.` | SECOND-PASS Q2: running head of Kannada p.353 reads ವ. (Varga 20) [q212] |
| 385 | `Va. 22 [?]"; centre: "Ṛgvedasaṃhitā"; right: 385.` → `Va. 22"; centre: "Ṛgvedasaṃhitā"; right: 385.` | SECOND-PASS Q2: running head of Kannada p.385 reads ವ. (Varga 22) [q321] |
| 375 | `Va. 21 [?]"; centre: "Ṛgvedasaṃhitā"; right: 375` → `Va. 22"; centre: "Ṛgvedasaṃhitā"; right: 375` | SECOND-PASS Q1: running head of Kannada p.375 reads ವ. (Varga 22) [q293] |
| 343 | `, as far as printed; the sūtra number is not legible [?])` → `, Pā. Sū. 6-1-171)` | SECOND-PASS Q1: Kannada p.343 ऊडिदं पदादि (ಪಾ. ಸೂ. ೬-೧-೧೭೧) [q181] |
| 343 | `, Pā. Sū. 7-3-116 [?])` → `)` | SECOND-PASS S3: Kannada p.343 has the sūtra ṅer ām nadyāmnībhyaḥ without a sūtra number; number removed with its mark [q183] |
| 343 | `, Pā. Sū. 8-3-59 [?])` → `)` | SECOND-PASS S3: Kannada p.343 has the sūtra ādeśapratyayayoḥ without a sūtra number; number removed with its mark [q184] |
| 343 | `Vārttika [?], numeral as read "वा. ४४३?" [?])` → `Vārttika 4823)` | SECOND-PASS Q1: Kannada p.343 हृग्रहोर्भश्छन्दसि (ವಾ. ೪೮೨೩) [q185-186] |
| 345 | `(Ā. 1-3 [?])` → `(Ā. 1-5)` | SECOND-PASS Q1: Kannada p.345 (ಆ. ೧-೫) [q188] |
| 346 | `9-24-6; 92-25-3; 9-24-3 [?]; 9-24-9 [?] and many more Ṛks (numerals as read, all doubtful)` → `9-24-6; 9-25-3; 9-28-3; 9-25-9 and many more Ṛks` | SECOND-PASS Q1: Kannada p.346 ಋ. ಸಂ. ೯-೨೪-೬; ೯-೨೫-೩; ೯-೨೮-೩; ೯-೨೫-೯ [q189-190] |
| 346 | `, Pā. Sū. 6-2-1 [?])` → `)` | SECOND-PASS S3: Kannada p.346 has the sūtra bahuvrīhau prakṛtyā pūrvapadam without a sūtra number; number removed with its mark [q191] |
| 347 | `cedarthaṃ [?] | tadyogān nipātair yadyadihanteti [?] nighātapratiṣedhaḥ` → `cedarthaṃ | tadyogān nipātair yadyadihanteti nighātapratiṣedhaḥ` | SECOND-PASS Q2: Kannada p.347 Sāyaṇa block has ಚೇದರ್ಥಂ । ತದ್ಯೋಗಾನ್ನಿಪಾತೈರ್ಯದ್ಯದಿಹಂತೇತಿ ನಿಘಾತಪ್ರತಿಷೇಧಃ [q193-194] |
| 347 | ` [as read, doubtful [?]], and from its connexion` → `, and from its connexion` | SECOND-PASS Q2: Kannada p.347 ಚೇದರ್ಥಂ agrees [q195] |
| 347 | `*nipātair yad yadi hanta…* partly read [?]]` → `*nipātair yad yadi hanta…*]` | SECOND-PASS Q2: Kannada p.347 ನಿಪಾತೈರ್ಯದ್ಯದಿಹಂತ agrees [q196] |
| 348 | `(Ā. 4-11 [?])` → `(Ā. 4-11)` | SECOND-PASS Q2: Kannada p.348 (ಆ. ೪-೧೧) [q197] |
| 349 | `; the same Ṛk cited on p. 337 with a different numeral — both readings doubtful [?])` → `)` | SECOND-PASS Q2: Kannada p.349 ಋ. ಸಂ. ೮-೪೮-೭ agrees with 8-48-7; doubt clause dropped after numeral settled [q199] |
| 349 | `(U. 1-[?] [?])` → `(U. 1-39)` | SECOND-PASS Q1: Kannada p.349 ಜೀವೇ ರಾತುಃ (ಉ.ಸೂ. ೧-೩೯) [q200-201] |
| 350 | `upabhogasamarthaṃ [?] bhagaṃ` → `upabhogasamarthaṃ bhagaṃ` | SECOND-PASS Q2: Kannada p.350 ದಕ್ಷಮುಪಭೋಗಸಮರ್ಥಂ agrees [q202] |
| 351 | ` [fit for enjoyment (the print here is clotted [?])]` → ` fit for enjoyment` | SECOND-PASS Q2: Kannada p.351 ದಕ್ಷಂ—ಅನುಭವಿಸಲು ಯೋಗ್ಯವಾದ and ದಕ್ಷಮುಪಭೋಗಸಮರ್ಥಂ [q205] |
| 351 | `*tumarthe sesenase…*, partly read [?]]` → `*tumarthe sesenase…*]` | SECOND-PASS Q2: Kannada p.352 ತುಮರ್ಥೇ ಸೇಸೇನಸೇ agrees [q206] |
| 351 | `(Ā. 2-10 [?])` → `(Ā. 2-10)` | SECOND-PASS Q2: Kannada p.351 (ಅ. ೨-೧೦) [q207] |
| 352 | `, Pā. Sū. 6-4-133 [?])` → `)` | SECOND-PASS S3: Kannada p.352 has the sūtra śvayuvamaghonām ataddhite without a sūtra number; number removed with its mark [q208] |
| 352 | `, Pā. Sū. 6-1-108 [?])` → `)` | SECOND-PASS S3: Kannada p.352 has the sūtra saṃprasāraṇāc ca without a sūtra number; number removed with its mark [q209] |
| 352 | `, Pā. Sū. 6-3-137 [?]) the lengthening in the Saṃhitā;` → `) the lengthening in the Saṃhitā;` | SECOND-PASS S3: Kannada p.352 has the sūtra anyeṣām api dṛśyate without a sūtra number; number removed with its mark [q210] |
| 352 | `, Pā. Sū. 1-1-39 [?])` → `)` | SECOND-PASS S3: Kannada p.352 has the sūtra kṛn mejantaḥ without a sūtra number; number removed with its mark [q211] |
| 354 | `(Ā. 3-10 [?])` → `(Ā. 2-10)` | SECOND-PASS Q1: Kannada p.354 (ಆ. ೨-೧೦) [q213] |
| 354 | `, Pā. Sū. 3-4-87 [?])` → `)` | SECOND-PASS S3: Kannada p.354 has the sūtra serhy apicca without a sūtra number; number removed with its mark [q214] |
| 355 | `, Pā. Sū. 7-4-33 [?])` → `)` | SECOND-PASS S3: Kannada p.355 has the sūtra kyaci ca without a sūtra number; number removed with its mark [q216] |
| 355 | `the genitive/ablative singular form [the print's case-name doubtful [?]];` → `the genitive singular form;` | SECOND-PASS Q1: Kannada p.355 ಷಷ್ಠೀಏಕವಚನಾಂತರೂಪ [q217] |
| 357 | `(Ā. 2-9 [?])` → `(Ā. 2-9)` | SECOND-PASS Q2: Kannada p.357 (ಆ. ೨-೯) [q219] |
| 357 | `9-113-7-[?] to [?].` → `9-113-7 to 11.` | SECOND-PASS Q1: Kannada p.357 ಋ. ಸಂ.೯-೧೧೩-೭ ರಿಂದ ೧೧ರ ವರೆಗೆ [q220-221] |
| 357 | `with an apparent extra *ma* [?])` → `with an apparent extra *ma*)` | SECOND-PASS Q2: Kannada p.357 prints ಮಾಮಮೃತಂ [q222] |
| 357 | `the same note on *māmamṛtaṃ* [?])` → `the same note on *māmamṛtaṃ*)` | SECOND-PASS Q2: Kannada p.357 prints ಮಾಮಮೃತಂ [q223] |
| 358 | `, Pā. Sū. 6-4-111 [?])` → `)` | SECOND-PASS S3: Kannada p.358 has the sūtra śnasor allopaḥ without a sūtra number; number removed with its mark [q224] |
| 358 | `, Pā. Sū. 6-4-131 [?])` → `)` | SECOND-PASS S3: Kannada p.358 has the sūtra vasoḥ saṃprasāraṇam without a sūtra number; number removed with its mark [q225] |
| 358 | `, Pā. Sū. 8-3-60 [?])` → `)` | SECOND-PASS S3: Kannada p.358 has the sūtra śāsivasighasīnāṃ ca without a sūtra number; number removed with its mark [q226] |
| 358 | `, the sūtra begins thus; the number not legible [?])` → `)` | SECOND-PASS S3: Kannada p.358 has the sūtra aptṛntṛc… without a sūtra number; number removed with its mark [q228] |
| 358 | `, Pā. Sū. 6-1-163 [?]) the final ` → `) the final ` | SECOND-PASS S3: Kannada p.358 has the sūtra cit without a sūtra number; number removed with its mark [q229] |
| 360 | `9-6-8 [?] and the like` → `9-6-8 and the like` | SECOND-PASS Q2: Kannada p.360 ಋ. ಸಂ. ೯-೨-೧೦ ೯-೬-೮ [q232] |
| 360 | `, Pā. Sū. 3-4-6 [?])` → `)` | SECOND-PASS S3: Kannada p.360 has the sūtra chandasi luṅlaṅliṭaḥ without a sūtra number; number removed with its mark [q233] |
| 360 | `Pā. Sū. 6-1-163 [?]) the final-acute.` → `Pā. Sū. 6-1-163) the final-acute.` | SECOND-PASS Q2: Kannada p.360 ಚಿತಃ (ಪಾ. ಸೂ. ೬-೧ ೧೬೩) [q234] |
| 362 | `8-[?]-[?] [?]; 8-[?]-[?] [?] and the like` → `9-91-3; 9-64-23 and the like` | SECOND-PASS Q1: Kannada p.362 ಋ. ಸಂ. ೯-೯೧-೩ ; ೯-೬೪-೨೩ [q236-247-a] |
| 362 | `Ṛ. Saṃ. 6-[?]-[?] [?]; 8-[?]-[?] [?] and other Ṛks` → `Ṛ. Saṃ. 6-15-6; 8-12-19 and other Ṛks` | SECOND-PASS Q1: Kannada p.362 ಋ. ಸಂ. ೬-೧೫-೬ ; ೮-೧೨-೧೯ [q236-247-b] |
| 362 | `the eleven Ṛks of the 113th sūkta of Ṛ. Saṃ. 9 [as read, doubtful [?]] has been explained ` → `Ṛks 7 to 11 of the 113th sūkta of Ṛ. Saṃ. 9 has been explained in the commentary on the Ṛk` | SECOND-PASS Q1: Kannada p.362 ಋ. ಸಂ. ೯-೧೧೩ನೇ ಸೂಕ್ತದ ೭ರಿಂದ ೧೧ನೇ ಋಕ್ಕುಗಳಲ್ಲಿ … ೧-೯೧-೯ನೇ ಋಕ್ಕಿನ ವಿವರಣ [q248-251] |
| 362 | `, Pā. Sū. 7-3-86 [?])` → `)` | SECOND-PASS S3: Kannada p.362 has the sūtra pugantalaghūpadhasya ca without a sūtra number; number removed with its mark [q252] |
| 363 | `कीकन्कनौ [?], U. Sū. 4-464 — the figure is read "४-४६४" here, whereas p. 361 gave "४-२४" [` → `कीकन्ककनौ, U. Sū. 4-464)` | SECOND-PASS Q1: Kannada p.363 ಮೃಡೇಃ ಕೀಕನ್‌ಕಕನೌ (ಉ. ಸೂ. ೪-೪೬೪) [q254-255] |
| 364 | `(Ā. 4-8 [?])` → `(Ā. 4-8)` | SECOND-PASS Q2: Kannada p.364 (ಆ. ೪-೮) [q256] |
| 364 | `(Ā. 2-1 [?])` → `(Ā. 2-1)` | SECOND-PASS Q2: Kannada p.364 (ಆ. ೨-೧) [q257] |
| 365 | `(Ni. 2-10 [?]), i` → `(Ni. 3-9), i` | SECOND-PASS Q1: Kannada p.365 ಮಘಂ, ರೇಕ್ಷಃ … ಧನನಾಮಗಳಲ್ಲಿ (೩-೯) [q259] |
| 365 | `Ṛk 6-24-2 [?] as` → `Ṛk 6-74-2 as` | SECOND-PASS Q1: Kannada p.365 ಋ. ಸಂ. ೬-೭೪-೨ [q260] |
| 365 | `; the final word of the citation is printed *āveśa*, read as *āviveśa* [?])` → `)` | SECOND-PASS Q1: Kannada p.365 ಮಾವಿವೇಶ (āviveśa) [q261] |
| 365 | `food (Ni. 2-9 [?])` → `food (Ni. 5-19)` | SECOND-PASS Q1: Kannada p.365 ವಸು ಶಬ್ದಕ್ಕೆ ಅನ್ನವೆಂದೂ ಅರ್ಥವು (ನಿ. ೫-೧೯) [q262] |
| 366 | `, Pā. Sū. 3-2-178 [?])` → `)` | SECOND-PASS S3: Kannada p.366 has the sūtra anyebhyo pi dṛśyate without a sūtra number; number removed with its mark [q263] |
| 368 | `maraṇadharmā* (Ni. 2-[?] [?])` → `maraṇadharmā* (Ni. 3-15)` | SECOND-PASS Q1: Kannada p.368 ಮರ್ಯೋ ಮನುಷ್ಯೋ ಮರಣಧರ್ಮಾ । (ನಿ. ೩-೧೫) [q267-268] |
| 368 | ` (Pā. Sū. 8-1-72 [?]) it counts as non-existent,` → ` it counts as non-existent,` | SECOND-PASS S3: Kannada p.368 has the sūtra āmantritaṃ pūrvam avidyamānavat without a sūtra number; number removed with its mark [q269] |
| 368 | ` (Pā. Sū. 8-1-28 [?])` → `` | SECOND-PASS S3: Kannada p.368 has the sūtra tiṅ atiṅaḥ (ತಿಜ್ಜತಿಜಿಃ) without a sūtra number; number removed with its mark [q270] |
| 369 | `, as printed, Pā. Sū. 6-1-63 [?])` → `)` | SECOND-PASS S3: Kannada p.369 has the sūtra padd annomās hṛn without a sūtra number; number removed with its mark [q272] |
| 370 | `10-[?]-[?] [?], and also` → `10-86-12, and also` | SECOND-PASS Q1: Kannada p.370 ಋ. ಸಂ. ೧೦-೮೬-೧೨ [q275-277] |
| 371 | `*na rarāṇa na rame*' [as read, doubtful [?]]` → `*na rarāṇa na rame*'` | SECOND-PASS Q2: Kannada p.371 ನ ರರಾಣ ನ ರಮೆ agrees [q279] |
| 371 | `(Pā. Sū. 3-4-97 [?]) ` → `(Pā. Sū. 3-4-97) ` | SECOND-PASS Q2: Kannada p.371 (ಪಾ. ಸೂ. ೩-೪-೯೭) [q280] |
| 371 | `, Pā. Sū. 8-1-66 [?])` → `)` | SECOND-PASS S3: Kannada p.371 has the sūtra yadvṛttān nityam without a sūtra number; number removed with its mark [q281] |
| 373 | `9-[?]-3 [?]; 8-[?]-[?] [?] this word` → `5-24-3; 1-58-9 this word` | SECOND-PASS Q1: Kannada p.373 ಋ. ಸಂ. ೫-೨೪-೩ ; ೧-೫೮-೯ [q283-287] |
| 373 | ` [as read; the print's first word is doubtful [?]]` → `` | SECOND-PASS Q2: Kannada p.373 ಅಂಹತಿಶ್ಚಾಂಹಂಶ್ಚಾಂಹುಶ್ಚ ಹಂತೇಃ (ನಿ. ೪-೨೫): first word agrees [q288] |
| 373 | `, Pā. Sū. 6-3-137 [?]) the lengthening in the Saṃhitā.` → `) the lengthening in the Saṃhitā.` | SECOND-PASS S3: Kannada p.373 has the sūtra anyeṣām api dṛśyate without a sūtra number; number removed with its mark [q289] |
| 373 | `, Pā. Sū. 6-4-24 [?])` → `)` | SECOND-PASS S3: Kannada p.373 has the sūtra aniditāṃ hala upadhāyāḥ kṅiti without a sūtra number; number removed with its mark [q290] |
| 375 | `(Ā. 1-10 [?])` → `(Ā. 1-10)` | SECOND-PASS Q2: Kannada p.375 (ಆ. ೧-೧೦) [q294] |
| 375 | `(Ni. 2-[?] [?]) among the names of battle` → `(Ni. 3-9) among the names of battle` | SECOND-PASS Q1: Kannada p.375 ನಿರುಕ್ತದಲ್ಲಿ (೩.೯) ಸಂಗ್ರಾಮ ನಾಮಗಳಲ್ಲಿ [q295-296] |
| 376 | `, Pā. Sū. 3-4-80 [?])` → `)` | SECOND-PASS S3: Kannada p.376 has the sūtra thāsaḥ se without a sūtra number; number removed with its mark [q297] |
| 376 | ` (Pā. Sū. 6-1-213 [?])` → `` | SECOND-PASS S3: Kannada p.376 has the sūtra yato nāvaḥ (not cited with a number in this word) without a sūtra number; number removed with its mark [q298] |
| 378 | `(Ni. 2-9 [?]) ` → `(Ni. 3-9) ` | SECOND-PASS Q1: Kannada p.378 ಶ್ರವಃ ಶಬ್ದವು ಬಲನಾಮ … (ನಿ. ೩-೯) [q300] |
| 378 | `, Pā. Sū. 5-2-115 [?])` → `)` | SECOND-PASS S3: Kannada p.378 has the sūtra ata ini-ṭhanau without a sūtra number; number removed with its mark [q301] |
| 378 | `, Pā. Sū. 5-3-55 [?])` → `)` | SECOND-PASS S3: Kannada p.378 has the sūtra atiśāyane tamabiṣṭhanau without a sūtra number; number removed with its mark [q302] |
| 378 | ` (Pā. Sū. 7-3-103 [?])` → `` | SECOND-PASS S3: Kannada p.378 has the sūtra bahuvacane jhaly et without a sūtra number; number removed with its mark [q303] |
| 379 | `, Pā. Sū. 3-1-4 [?])` → `)` | SECOND-PASS S3: Kannada p.379 has the sūtra anudāttau suppitau without a sūtra number; number removed with its mark [q305] |
| 381 | `, Pā. Sū. 8-1-22 [?])` → `)` | SECOND-PASS S3: Kannada p.381 has the sūtra te mayāvekavacanasya without a sūtra number; number removed with its mark [q307] |
| 381 | ` (Pā. Sū. 7-2-116 [?]) the p` → ` the p` | SECOND-PASS S3: Kannada p.381 has the sūtra ata upadhāyāḥ without a sūtra number; number removed with its mark [q308] |
| 382 | `, Pā. Sū. 6-1-186 [?])` → `)` | SECOND-PASS S3: Kannada p.382 has the sūtra tāsyanudāttet without a sūtra number; number removed with its mark [q309] |
| 382 | `The third pāda's *paribhūr astu* is read from a print whose conjunct is not wholly clear [` → `` | SECOND-PASS Q2: Kannada p.382 pāda ತಾ ತೇ ವಿಶ್ವಾ ಪರಿಭೂರಸ್ತು ಯಜ್ಞಂ agrees [q310] |
| 384 | `(Ā. 4-4 [?])` → `(Ā. 4-4)` | SECOND-PASS Q2: Kannada p.384 (ಆ.೪-೪) [q316] |
| 384 | `(Ā. 3-2 [?])` → `(Ā. 3-7)` | SECOND-PASS Q1: Kannada p.384 (ಆ. ೩-೭) [q317] |
| 384 | `Ṛ. Saṃ. 1-[?]-[?] [?].` → `Ṛ. Saṃ. 1-91-4.` | SECOND-PASS Q1: Kannada p.384 ಋ. ಸಂ. ೧-೯೧-೪ನೆಯ ಋಕ್ಕನ್ನು ವಿವರಿಸುವಾಗ [q318-320] |
| 385 | `Ṛ. Saṃ. 1-[?]-[?] [?].` → `Ṛ. Saṃ. 1-91-12.` | SECOND-PASS Q1: Kannada p.385 ಋ. ಸಂ. ೧-೯೧-೧೨ನೆಯ ಋಕ್ಕನ್ನು ವಿವರಿಸುವಾಗ [q323-325] |
| 385 | `; the same Ṛk as cited on pp. 337 and 349 — the three numerals read differently [?])` → `)` | SECOND-PASS Q2: Kannada p.385 ( ಋ. ಸಂ. ೮-೪೮-೭ ) agrees with 8-48-7; doubt clause dropped after numeral settled [q326] |
| 385 | ` — the numeral read as "३-१३", whereas the same list was given on p. 365 as "३-४" [?])` → `)` | SECOND-PASS Q2: Kannada p.385 (ನಿ. ೩-೧೩) agrees with Ni. 3-13 [q329] |
| 359 | `मक्षि शर्धो मारुतं मक्षि ` → `मत्सि शर्धो मारुतं मत्सि ` | SECOND-PASS Q1: Kannada p.359 ಮತ್ಸಿ ಶರ್ಧೋ ಮಾರುತಂ ಮತ್ಸಿ (Devanagari twin) [q231] |
| 359 | `मक्षि महामिन्द्रमिन्दो मदाय` → `मत्सि महामिन्द्रमिन्दो मदाय` | SECOND-PASS Q1: Kannada p.359 ಮತ್ಸಿ ಮಹಾಮಿಂದ್ರಮಿಂದೋ ಮದಾಯ (Devanagari twin) [q231] |
| 359 | `*makṣi soma varuṇaṃ makṣi mitraṃ makṣīndram indo pavamāna viṣṇum | makṣi śardho mārutaṃ ma` → `*matsi soma varuṇaṃ matsi mitraṃ matsīndram indo pavamāna viṣṇum | matsi śardho mārutaṃ ma` | SECOND-PASS Q1: Kannada p.359 reads matsi (IAST twin of the Devanagari edit) [q231] |
| 383 | `वीर्यो ज्ञायन्ते इति वीराः पुत्राः` → `वीर्याज्जायन्त इति वीराः पुत्राः` | SECOND-PASS Q1: Kannada p.383 ವೀರ್ಯಾಜ್ಜಾಯಂತ ಇತಿ ವೀರಾಃ ಪುತ್ರಾಃ (Devanagari twin) [q313] |
| 383 | `vīryo jñāyante [?] iti vīrāḥ putrāḥ` → `vīryāj jāyanta iti vīrāḥ putrāḥ` | SECOND-PASS Q1: Kannada p.383 ವೀರ್ಯಾಜ್ಜಾಯಂತ ಇತಿ ವೀರಾಃ ಪುತ್ರಾಃ (IAST twin) [q313] |

### 2026-11-27 second pass, batch m180-329_2.tsv
| page | old → new | why |
|---|---|---|
| 359 | `मक्षि सोम वरुणं मक्षि मित्रं मक्षीन्द्रमिन्दो पवमान ` → `मत्सि सोम वरुणं मत्सि मित्रं मत्सीन्द्रमिन्दो पवमान ` | SECOND-PASS Q1: Kannada p.359 ಮತ್ಸಿ ಸೋಮ ವರುಣಂ ಮತ್ಸಿ ಮಿತ್ರಂ ಮತ್ಸೀಂದ್ರಮಿಂದೋ ಪವಮಾನ (Devanagari twin) [q231] |

### 2026-11-27 second pass, batch m197-346.tsv
| page | old → new | why |
|---|---|---|
| 387 | `Va. 22 [?]"; centre: "Ṛgvedasaṃhitā"; right: 387.` → `Va. 22"; centre: "Ṛgvedasaṃhitā"; right: 387.` | SECOND-PASS Q2: running head of Kannada p.387 reads ಅ. ೧. ಅ. ೬. ವ. 22 (Varga 22) |
| 389 | `Va. 22 [?]"; centre: "Ṛgvedasaṃhitā"; right: 389.` → `Va. 22"; centre: "Ṛgvedasaṃhitā"; right: 389.` | SECOND-PASS Q2: running head of Kannada p.389 reads ಅ. ೧. ಅ. ೬. ವ. 22 (Varga 22) |
| 391 | `Va. 23 [?]"; centre: "Ṛgvedasaṃhitā"; right: 391.` → `Va. 23"; centre: "Ṛgvedasaṃhitā"; right: 391.` | SECOND-PASS Q2: running head of Kannada p.391 reads ಅ. ೧. ಅ. ೬. ವ. 23 (Varga 23) |
| 393 | `Va. 23 [?]"; centre: "Ṛgvedasaṃhitā"; right: 393.` → `Va. 23"; centre: "Ṛgvedasaṃhitā"; right: 393.` | SECOND-PASS Q2: running head of Kannada p.393 reads ಅ. ೧. ಅ. ೬. ವ. 23 (Varga 23) |
| 395 | `Va. 23 [?]"; centre: "Ṛgvedasaṃhitā"; right: 395.` → `Va. 23"; centre: "Ṛgvedasaṃhitā"; right: 395.` | SECOND-PASS Q2: running head of Kannada p.395 reads ಅ. ೧. ಅ. ೬. ವ. 23 (Varga 23) |
| 397 | `Va. 23 [?]"; centre: "Ṛgvedasaṃhitā"; right: 397.` → `Va. 23"; centre: "Ṛgvedasaṃhitā"; right: 397.` | SECOND-PASS Q2: running head of Kannada p.397 reads ಅ. ೧. ಅ. ೬. ವ. 23 (Varga 23) |
| 399 | `Va. 23 [?]"; centre: "Ṛgvedasaṃhitā"; right: 399.` → `Va. 23"; centre: "Ṛgvedasaṃhitā"; right: 399.` | SECOND-PASS Q2: running head of Kannada p.399 reads ಅ. ೧. ಅ. ೬. ವ. 23 (Varga 23) |
| 401 | `Va. 23 [?]"; centre: "Ṛgvedasaṃhitā"; right: 401.` → `Va. 23"; centre: "Ṛgvedasaṃhitā"; right: 401.` | SECOND-PASS Q2: running head of Kannada p.401 reads ಅ. ೧. ಅ. ೬. ವ. 23 (Varga 23) |
| 403 | `Va. 24 [?]"; centre: "Ṛgvedasaṃhitā"; right: 403.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 403.` | SECOND-PASS Q2: running head of Kannada p.403 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 405 | `Va. 24 [?]"; centre: "Ṛgvedasaṃhitā"; right: 405.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 405.` | SECOND-PASS Q2: running head of Kannada p.405 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 407 | `Va. 24 [?]"; centre: "Ṛgvedasaṃhitā"; right: 407.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 407.` | SECOND-PASS Q2: running head of Kannada p.407 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 409 | `Va. 25 [?]"; centre: "Ṛgvedasaṃhitā"; right: 409.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 409.` | SECOND-PASS Q1: running head of Kannada p.409 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 411 | `Va. 25 [?]"; centre: "Ṛgvedasaṃhitā"; right: 411.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 411.` | SECOND-PASS Q1: running head of Kannada p.411 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 415 | `Va. 26 [?]"; centre: "Ṛgvedasaṃhitā"; right: 415.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 415.` | SECOND-PASS Q1: running head of Kannada p.415 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 417 | `Va. 26 [?]"; centre: "Ṛgvedasaṃhitā"; right: 417.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 417.` | SECOND-PASS Q1: running head of Kannada p.417 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 419 | `Va. 26 [?]"; centre: "Ṛgvedasaṃhitā"; right: 419.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 419.` | SECOND-PASS Q1: running head of Kannada p.419 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 421 | `Va. 27 [?]"; centre: "Ṛgvedasaṃhitā"; right: 421.` → `Va. 24"; centre: "Ṛgvedasaṃhitā"; right: 421.` | SECOND-PASS Q1: running head of Kannada p.421 reads ಅ. ೧. ಅ. ೬. ವ. 24 (Varga 24) |
| 423 | `Va. 27 [?]"; centre: "Ṛgvedasaṃhitā"; right: 423.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 423.` | SECOND-PASS Q1: running head of Kannada p.423 reads ಅ. ೧. ಅ. ೬. ವ. 25 (Varga 25) |
| 425 | `Va. 27 [?]"; centre: "Ṛgvedasaṃhitā"; right: 425.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 425.` | SECOND-PASS Q1: running head of Kannada p.425 reads ಅ. ೧. ಅ. ೬. ವ. 25 (Varga 25) |
| 427 | `Va. 28 [?]"; centre: "Ṛgvedasaṃhitā"; right: 427.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 427.` | SECOND-PASS Q1: running head of Kannada p.427 reads ಅ. ೧. ಅ. ೬. ವ. 25 (Varga 25) |
| 429 | `Va. 28 [?]"; centre: "Ṛgvedasaṃhitā"; right: 429.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 429.` | SECOND-PASS Q1: running head of Kannada p.429 reads ಅ. ೧. ಅ. ೬. ವ. 25 (Varga 25) |
| 413 | `"A. 1 A. 6 Va. 30 [?]" on the left` → `"A. 1 A. 6 Va. 30" on the left` | SECOND-PASS Q2: Kannada page headed 513 reads ವ. ೩೦ (Varga 30) |
| 388 | `Ṛ. Saṃ. 3-32-2 [?]; the numerals read "२-२७-७" [?]` → `Ṛ. Saṃ. 2-27-7` | SECOND-PASS Q1: Kannada p.388 reads (ಋ. ಸಂ. ೨-೨೭-೭) for ವಿದಥಾನಿ ಪ್ರಚೋದಯನ್ |
| 388 | `(Ni. 2-3 [?])` → `(Ni. 7-8)` | SECOND-PASS Q1: Kannada p.388 reads (ನಿ. ೭-೮) after ವಿದಥಾನಿ ವೇದನಾನಿ |
| 389 | ` [?], Pā. Sū. 6-4-127 [?]` → `` | SECOND-PASS S3: Kannada p.389 has ಅರ್ವಣಸ್ತ್ರಸಾವನಞ್—ಎಂಬುದರಿಂದ with no sūtra number; the Sanskrit word agrees |
| 389 | ` (Pā. Sū. 6-4-168 [?])` → `` | SECOND-PASS S3: Kannada p.389 has ಯೇಚಾಭಾವ ಕರ್ಮಣೋಃ—ಎಂಬುದರಿಂದ with no number |
| 389 | `, Pā. Sū. 7-1-2 [?]` → `` | SECOND-PASS S3: Kannada p.389 has ಆಯನೇಯೀ—ಸೂತ್ರದಿಂದ with no number |
| 389 | `, Pā. Sū. 6-4-148 [?]` → `` | SECOND-PASS S3: Kannada p.389 has ಯಸ್ಯೇತಿ ಚ—ಸೂತ್ರದಿಂದ with no number |
| 389 | `(Pā. Sū. 8-1-66 [?])` → `(Pā. Sū. 8-1-66)` | SECOND-PASS Q2: Kannada p.389 reads (ಪಾ. ಸೂ. ೮೧-೬೬): same digits 8,1,66, hyphen lost in print |
| 391 | `[root, as read, pyā/pṛ pālanapūraṇayoḥ [?]]` → `pṛ pālanapūraṇayoḥ` | SECOND-PASS Q1: Kannada p.391 reads ಪೃ ಪಾಲನಪೂರಣಯೋಃ |
| 391 | `[root, as read *pyā/pṛ pālanapūraṇayoḥ*]` → `पृ पालनपूरणयोः` | SECOND-PASS Q1: Devanagari twin of the IAST edit; Kannada p.391 reads ಪೃ ಪಾಲನಪೂರಣಯೋಃ |
| 392 | `(Ni. 2-[?] [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.392 reads (ನಿ. ೩-೯) after ಸಂಗ್ರಾಮನಾಮಗಳಲ್ಲಿ |
| 392 | `root *pyā*, which gives the sense of 'to fill' (*pyā pālanapūraṇayoḥ*) [as read [?]],` → `root *pṛ*, which gives the sense of 'to fill' (*pṛ pālanapūraṇayoḥ*),` | SECOND-PASS Q1: Kannada p.392 reads ಪೃ ಪಾಲನಪೂರಣಯೋಃ ಎಂಬ ಪೂರಣಾರ್ಥವನ್ನು ಕೊಡುವ ಪೃ ಧಾತು |
| 392 | `Ṛ. Saṃ. 1-[?]-3 [?]` → `Ṛ. Saṃ. 1-52-3` | SECOND-PASS Q1: Kannada p.392 reads (ಋ. ಸಂ. ೧-೫೨-೩) before ಪಪ್ರಿರಂಧಸಃ |
| 392 | `Ṛ. Saṃ. 9-[?]-[?] [?]; 7-[?]-[?] [?]; 9-[?]-1 [?]` → `Ṛ. Saṃ. 9-65-20; 9-71-8; 9-84-1` | SECOND-PASS Q1: Kannada p.392 reads ಋ. ಸಂ. ೯-೬೫-೨೦ ; ೯-೭೧-೮ ; ೯-೮೪-೧ for the ಅಪ್ಸ್ಯಾಃ Ṛks |
| 392 | `(Ni. 2-17 [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.392 reads (ನಿ. ೩-೯) after ಭರ ಶಬ್ದವು ಸಂಗ್ರಾಮ ನಾಮಗಳಲ್ಲಿ |
| 393 | ` (Pā. Sū. 6-2-2 [?])` → `` | SECOND-PASS S3: Kannada p.393 has ತತ್ಪುರುಷೇ ತುಲ್ಯಾರ್ಥ—ಎಂಬುದರಿಂದ with no number |
| 393 | `*pyā pālanapūraṇayoḥ* [as read [?]]` → `*pṛ pālanapūraṇayoḥ*` | SECOND-PASS Q1: Kannada p.393 reads ಪಪ್ರಿಮ್—ಪೃ ಪಾಲನಪೂರಣಯೋಃ ಧಾತು |
| 393 | `*ur at* [as read [?]]` → `*ur at*` | SECOND-PASS Q2: Kannada p.393 reads ಅಭ್ಯಾಸಕ್ಕೆ ಉರದತ್ವ (ur at) |
| 393 | ` (Pā. Sū. 6-1-197 [?])` → `` | SECOND-PASS S3: Kannada p.393 has ಇತ್ಯಾದಿರ್ನಿತ್ಯಮ್—ಎಂಬುದರಿಂದ with no number |
| 393 | ` (Pā. Sū. 6-3-14 [?])` → `` | SECOND-PASS S3: Kannada p.393 has ತತ್ಪುರುಷೇ ಕೃತಿ ಬಹುಲಮ್—ಎಂಬುದರಿಂದ with no number |
| 393 | ` (Pā. Sū. 3-3-174 [?])` → `` | SECOND-PASS S3: Kannada p.393 has ಕ್ತಿಚ್‌ಕ್ತೌಚಸಂಜ್ಞಾಯಾಂ(ಪಾ.ಸೂ.—ಎಂಬುದರಿಂದ with the number missing |
| 393 | ` (Pā. Sū. 6-1-163 [?])` → `` | SECOND-PASS S3: Kannada p.393 has ಚಿತಃ—ಎಂಬುದರಿಂದ with no number |
| 394 | `, Pā. Sū. 3-4-99 [?]` → `` | SECOND-PASS S3: Kannada p.394 has ನಿತ್ಯಂ ಙಿತಃ—ಎಂಬುದರಿಂದ with no number |
| 394 | ` (Pā. Sū. 7-2-80 [?])` → `` | SECOND-PASS S3: Kannada p.394 has ಅತೋಯೇಯಃ—ಎಂಬುದರಿಂದ with no number |
| 394 | `, Pā. Sū. 6-1-66 [?]` → `` | SECOND-PASS S3: Kannada p.394 has ಲೋಪೋರ್ವೋವಲಿ—ಎಂಬುದರಿಂದ with no number |
| 394 | ` (Pā. Sū. 6-1-198 [?])` → `` | SECOND-PASS S3: Kannada p.394 has ಆಮಂತ್ರಿತಸ್ಯ ಚ—ಎಂಬುದರಿಂದ with no number |
| 395 | ` [reading doubtful [?]]` → `` | SECOND-PASS Q2: Kannada p.395 reads ...ನಿರೋಧಕಮಂಧಕಾರಂ ತದಪಿ: andhakāram agrees |
| 395 | ` [reading doubtful]` → `` | SECOND-PASS Q2: Devanagari twin of the IAST edit (andhakāram agrees with Kannada p.395) |
| 395 | `jyotiṣmātmīyena [clotted [?]]` → `jyotiṣātmīyena` | SECOND-PASS Q1: Kannada p.395 reads ಜ್ಯೋತಿಷಾತ್ಮೀಯೇನ ಪ್ರಕಾಶೇನ |
| 395 | `ज्योतिष्मात्मीयेन [clotted; sense 'with your own light']` → `ज्योतिषात्मीयेन` | SECOND-PASS Q1: Devanagari twin; Kannada p.395 reads ಜ್ಯೋತಿಷಾತ್ಮೀಯೇನ |
| 395 | ` [the print's phrase is clotted [?]]` → `` | SECOND-PASS Q1: Kannada p.395 reads ಜ್ಯೋತಿಷಾತ್ಮೀಯೇನ ಪ್ರಕಾಶೇನ (with own light) |
| 396 | `, Ṛ. Saṃ. 10-97-18 [?]` → `` | SECOND-PASS S3: Kannada p.396 has ಯಾ ಓಷಧೀಃ ಸೋಮರಾಜ್ಞೀಃ ಎಂದು ೧೮ ಮತ್ತು ೧೯ನೆಯ ಋಕ್ಕುಗಳಲ್ಲಿ with no reference number |
| 396 | `Ṛ. Saṃ. 6-44[4]-2[4] [?]` → `Ṛ. Saṃ. 6-44-24` | SECOND-PASS Q1: Kannada p.396 reads ಋ. ಸಂ. ೬-೪೪-೨೪ |
| 396 | `(Ṛ. Saṃ. 9-33-2 [?])` → `(Ṛ. Saṃ. 9-25-3)` | SECOND-PASS Q1: Kannada p.396 reads ( ಋ. ಸಂ. ೯-೨೫-೩) after ಸಂ ದೇವೈಃ ಶೋಭತೇ ವೃಷಾ |
| 396 | `(Ṛ. Saṃ. 6-42-4 [?]; the numerals as read, doubtful)` → `(Ṛ. Saṃ. 6-47-4)` | SECOND-PASS Q1: Kannada p.396 reads ( ಋ. ಸಂ. ೬-೪೭-೪ ) after ಅಯಂ ಪೀಯೂಷಂ |
| 397 | `; the word *sahasāvan* is partly blotted in the scan [?].` → `.` | SECOND-PASS Q2: Kannada p.397-398 carries the word ಸಹಸಾವನ್ (ಸಹ|ಸಾವನ್ line break) complete |
| 398 | `ākāralopajanaḥ [clotted [?]]` → `ākāropajanaḥ` | SECOND-PASS Q1: Kannada p.398 reads ಆಕಾರೋಪಜನಃ |
| 398 | `आकारलोपजनः [clotted]` → `आकारोपजनः` | SECOND-PASS Q1: Devanagari twin; Kannada p.398 reads ಆಕಾರೋಪಜನಃ |
| 398 | `with a Vedic elision of *ā* [clotted [?]]` → `with a Vedic insertion of *ā*` | SECOND-PASS Q1: Kannada p.398 reads ಆಕಾರೋಪಜನಃ (ākāropajana) |
| 400 | `9-66-16 and 12 [?]` → `9-66-16 and 17` | SECOND-PASS Q1: Kannada p.400 reads ಋಕ್ಸಂಹಿತೆಯ ೯-೬೬-೧೬ ಮತ್ತು ೧೭ ನೇ ಋಕ್ಕುಗಳಲ್ಲಿ |
| 401 | ` (Pā. Sū. 5-2-94 [?])` → `` | SECOND-PASS S3: Kannada p.401 has ತದಸ್ಯಾಸ್ತಿ—ಎಂಬುದರಿಂದ with no number |
| 401 | ` (Pā. Sū. 8-2-9 [?])` → `` | SECOND-PASS S3: Kannada p.401 has ಮಾದುಪಧಾಯಾಶ್ಚ—ಎಂಬುದರಿಂದ with no number |
| 402 | `the Anukramaṇī line is garbled in the print — "dvyanonapasyaṃ" as printed [?]` → `the Anukramaṇī line reads "dvyūnoṣasyaṃ"` | SECOND-PASS Q1: Kannada p.402 reads ಏತಾ ಉ ತ್ಯಾ ದ್ವ್ಯೂನೋಷಸ್ಯಂ |
| 403 | ` ‖ Varga 24, 25, 26, 27 [?]** *(the four varga numerals, in small Kannada digits, as read;` → `**` | SECOND-PASS S3: Kannada p.403 heading carries only ಮಂಡಲ-೧, ಅನುವಾಕ-೧೪, ಸೂಕ್ತ-೯೨ and no varga numerals |
| 403 | ` The numerals "15", "16" are small and read with some doubt [?].)*` → `)*` | SECOND-PASS Q2: Kannada p.403 reads ದೇವತಾ— ೧-೧೫ ಉಷಾಃ । ೧೬-೧೮ ಅಶ್ವಿನೌ |
| 405 | `Part [5?], pp. 32–33 [as printed; the part number is read with some doubt [?]]` → `Part 5, pp. 32–33` | SECOND-PASS Q1: Kannada p.405 reads ಋ. ಸಂ. ಭಾಗ ೫ ಪೇಜು 32-33 |
| 405 | `(Ni. 3-9 [?])` → `(Ni. 3-13)` | SECOND-PASS Q1: Kannada p.405 reads (ನಿ- ೩-೧೩) for ಕೇತಃ ಕೇತುಃ ಚೇತಃ |
| 406 | ` (Pā. Sū. 7-1-5 [?])` → `` | SECOND-PASS S3: Kannada p.406 has ಆತ್ಮನೇಪೇದೆಷ್ವನತಃ—ಎಂಬುದರಿಂದ with no number |
| 407 | `, Pā. Sū. 6-1-163 [?]` → `` | SECOND-PASS S3: Kannada p.407 has ಚಿತಃ—ಎಂಬುದರಿಂದ with no number |
| 408 | `caturhṛdīrgā [clotted [?]]` → `catuṣpadīrgā` | SECOND-PASS Q1: Kannada p.408 reads ಸ್ವವಾಹನಭೂತಾಶ್ಚತುಷ್ಪದೀರ್ಗಾ |
| 408 | `चतुर्हृदीर्गा [clotted]` → `चतुष्पदीर्गा` | SECOND-PASS Q1: Devanagari twin; Kannada p.408 reads ಚತುಷ್ಪದೀರ್ಗಾ |
| 408 | `such, being their own vehicles [the middle words clotted [?]] —` → `such, being their own vehicles, four-footed cows —` | SECOND-PASS Q1: Kannada p.408 reads ಸ್ವವಾಹನಭೂತಾಶ್ಚತುಷ್ಪದೀರ್ಗಾ |
| 409 | `Ṛ. Saṃ. 1-[?]-4 [?] and 1-[?]-2 [?]` → `Ṛ. Saṃ. 1-58-4 and 1-63-7` | SECOND-PASS Q1: Kannada p.409 reads ಋ. ಸಂ. ೧-೫೮-೪ ; ೧-೬೩-೭ |
| 409 | `(Ni. 12-7 [?])` → `(Ni. 12-7)` | SECOND-PASS Q2: Kannada p.409 reads (ನಿ. ೧೨-೭) |
| 409 | `(Ni. 2-[?] [?])` → `(Ni. 2-28)` | SECOND-PASS Q1: Kannada p.409 reads (ನಿ. ೨-೨೮) after ಅರುಣೋ ಗಾವ ಉಷಸಾಂ |
| 409 | `(Ni. 3-9 [?])` → `(Ni. 3-13)` | SECOND-PASS Q1: Kannada p.409 reads (ನಿ. ೩-೧೩) for ಕೇತಃ ಕೇತುಃ |
| 409 | `, Pā. Sū. 7-1-3 [?]` → `` | SECOND-PASS S3: Kannada p.409 has ಝೋಂತಃ ಸೂತ್ರದಿಂದ with no number |
| 411 | `dhārṣṭyenopetāḥ [?]` → `dhāṭīmukhena` | SECOND-PASS Q1: Kannada p.411 reads ಸ್ವಕೀಯೈರಾಯುಧೈರ್ಧಾಟೀಮುಖೇನ |
| 411 | `धार्ष्ट्येनोपेताः [print 'dhārṭīmupena', doubtful]` → `धाटीमुखेन` | SECOND-PASS Q1: Devanagari twin; Kannada p.411 reads ಧಾಟೀಮುಖೇನ |
| 411 | `with their own weapons and with boldness [the print here is doubtful [?]], pervade` → `with their own weapons, by assault, pervade` | SECOND-PASS Q1: Kannada p.411 reads ಧಾಟೀಮುಖೇನ (by assault) |
| 414 | `jagatpraśliṣṭāni [print 'jagatpra…ṣṇāni', doubtful [?]] kṛṣṇavarṇāni tamāṃsi sthādhyikena ` → `jagatsvāśliṣṭāni kṛṣṇavarṇāni tamāṃsyadhyādhikyena` | SECOND-PASS Q1: Kannada p.414 reads ಜಗತ್ಸ್ವಾಶ್ಲಿಷ್ಟಾನಿ ಕೃಷ್ಣವರ್ಣಾನಿ ತಮಾಂಸ್ಯಧ್ಯಾಧಿಕ್ಯೇನ |
| 414 | `जगत्प्रश्लिष्टानि [print 'jagatpra…ṣṇāni', doubtful] कृष्णवर्णानि तमांसि स्थाध्यिकेन [clot` → `जगत्स्वाश्लिष्टानि कृष्णवर्णानि तमांस्यध्याधिक्येन` | SECOND-PASS Q1: Devanagari twin; Kannada p.414 reads ಜಗತ್ಸ್ವಾಶ್ಲಿಷ್ಟಾನಿ ... ತಮಾಂಸ್ಯಧ್ಯಾಧಿಕ್ಯೇನ |
| 415 | `-ṣāḥ śāstroktam andhakāraṃ [clotted [?]] vy āvaḥ` → `-ṣāstamo 'ṃdhakāraṃ vy āvaḥ` | SECOND-PASS Q1: Kannada p.415 reads ಷಾಸ್ತಮೋಽಂಧಕಾರಂ ವ್ಯಾವಃ |
| 415 | `षाः शास्त्रोक्तमन्धकारं [clotted] व्यावः` → `षास्तमोऽंधकारं व्यावः` | SECOND-PASS Q1: Devanagari twin; Kannada p.415 reads ಷಾಸ್ತಮೋಽಂಧಕಾರಂ ವ್ಯಾವಃ |
| 415 | ` [the clause between '*uṣāḥ*' and '*andhakāram*' is clotted in the print [?]]` → `` | SECOND-PASS Q1: Kannada p.415 reads ಷಾಸ್ತಮೋಽಂಧಕಾರಂ ವ್ಯಾವಃ (the clause is read) |
| 416 | `(Ni. 6-[?] [?])` → `(Ni. 6-2)` | SECOND-PASS Q1: Kannada p.416 reads (ನಿ. ೬-೨) after ವೃಣೋತೇರ್ವ್ರಜಃ |
| 417 | ` (Pā. Sū. 8-2-76 [?])` → `` | SECOND-PASS S3: Kannada p.417 has ರ್ವೋರುಪಧಾಯಾಃ ಎಂಬುದರಿಂದ with no number |
| 417 | ` (Pā. Sū. 3-4-113 [?])` → `` | SECOND-PASS S3: Kannada p.417 has ತಿಜ್ಶಿತ್ ಸಾರ್ವಧಾತುಕಮ್ ಎಂಬುದರಿಂದ with no number |
| 420 | `(Ni. 1-[?] [?])` → `(Ni. 2-28)` | SECOND-PASS Q1: Kannada p.420 reads (ನಿ.೨-೨೮) after ಅರ್ಚಿಃ ಶೋಚಿಃ ತಪಃ |
| 421 | ` (Pā. Sū. 3-1-66 [?])` → `` | SECOND-PASS S3: Kannada p.421 has ಚಿಣ್ ಭಾವಕರ್ಮಣೋಃ ಎಂಬುದರಿಂದ with no number |
| 424 | `in section 2-[?].` → `in section 12-7.` | SECOND-PASS Q1: Kannada p.424 reads ನಿರುಕ್ತಕಾರರು ೧೨-೭ನೇ ಖಂಡದಲ್ಲಿಯೂ ಸಹ |
| 424 | `(Ni. 3-[?] [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.424 reads ( ನಿ. ೩-೯ ) after ಕಾಂತಿಕರ್ಮನಾಮಗಳಲ್ಲಿ |
| 424 | `**GLOSS** *(Reading of the whole citation doubtful [?].)*` → `` | SECOND-PASS Q2: Kannada p.424 reads the Ṛk ಯಾವನ್ಮಾತ್ರಮುಷಸೋ ನ ಪ್ರತೀಕಂ ಸುಪರ್ಣ್ಯೋ ವಸತೇ ಮಾತರಿಶ್ವಃ (ಋ. ಸಂ. ೧೦-೮೮-೧೯) as the English |
| 424 | `(Ṛ. Saṃ. 1-58-2 [?]; the numerals as read, doubtful)` → `(Ṛ. Saṃ. 1-163-7)` | SECOND-PASS Q1: Kannada p.424 reads ( ಋ. ಸಂ. ೧-೧೬೩-೭ ) after ಯದಾ ತೇ ಮರ್ತೋ ಅನು ಭೋಗಂ |
| 425 | `(Ni. 6-[?] [?])` → `(Ni. 6-8)` | SECOND-PASS Q1: Kannada p.425 reads ( ನಿ. ೬-೮ ) after ಹಿಡಿದುಕೊ |
| 425 | ` (Pā. Sū. 3-4-99 [?])` → `` | SECOND-PASS S3: Kannada p.425 has ನಿತ್ಯಂ ಜಿತಃ ಎಂಬುದರಿಂದ with no number |
| 425 | `by *ato lopaḥ* [as read, doubtful [?]]` → `by *ato lopaḥ*` | SECOND-PASS Q2: Kannada p.425 reads ಅತೋಲೋಪಃ—ಎಂಬುದರಿಂದ |
| 427 | `ye ko 'pi luk [?]` → `yako 'pi luk` | SECOND-PASS Q1: Kannada p.427 reads ಬಹುಲಗ್ರಹಣಾದ್ಯಕೋಽಪಿ ಲುಕ್ |
| 427 | `ये को ऽपि लुक्` → `यको ऽपि लुक्` | SECOND-PASS Q1: Devanagari twin; Kannada p.427 reads ಯಕೋಽಪಿ ಲುಕ್ |
| 427 | `(Ni. 3-[?] [?])` → `(Ni. 2-19)` | SECOND-PASS Q1: Kannada p.427 reads ( ನಿ. ೨-೧೯ ) after ವಿಶೇಷಣಗಳು ಅಥವಾ ಪರ್ಯಾಯ ಪದಗಳು |
| 428 | `'*aśvair yo [yeṣu] boddhavyas te aśvabudhyāḥ tān*' [as read, clotted [?]]` → `'*aśvair ye bodhyante te aśvabudhyāḥ tān*'` | SECOND-PASS Q1: Kannada p.428 reads ಅಶ್ವೈರ್ಯೇ ಬೋಧ್ಯಂತೇ ತೇ ಅಶ್ವಬುಧ್ಯಾಃ ತಾನ್ |
| 428 | `In the 8th Ṛk of the same sūkta [1-92-8 [?]] the same word occurs` → `In the Ṛk 1-121-14 of the Ṛksaṃhitā the same word occurs` | SECOND-PASS Q1: Kannada p.428 reads ಋಕ್ಸಂಹಿತೆಯ ೧-೧೨೧-೧೪ನೆಯ ಋಕ್ಕಿನಲ್ಲಿ ಬರುವ ಈ ಪದಕ್ಕೂ |
| 428 | ` (Pā. Sū. 5-2-94 [?])` → `` | SECOND-PASS S3: Kannada p.428 has ತದಸ್ಯಾಸ್ತ್ಯ—ಎಂಬುದರಿಂದ with no number |
| 428 | ` (Pā. Sū. 8-2-9 [?])` → `` | SECOND-PASS S3: Kannada p.428 has ಮಾದುಪಧಾಯಾಶ್ಚ—ಎಂಬುದರಿಂದ with no number |
| 428 | ` (Pā. Sū. 4-1-6 [?])` → `` | SECOND-PASS S3: Kannada p.428 has ಉಗಿತಶ್ಚ—ಎಂಬುದರಿಂದ with no number |
| 428 | ` (Pā. Sū. 4-1-5 [?])` → `` | SECOND-PASS S3: Kannada p.428 has ಋನ್ನೇಭ್ಯೋ ಜೀಪ್—ಎಂಬುದರಿಂದ with no number |
| 429 | ` (Pā. Sū. 6-1-163 [?])` → `` | SECOND-PASS S3: Kannada p.429 has ಚಿತಃ—ಎಂಬುದರಿಂದ with no number |
| 429 | ` (Pā. Sū. 2-4-73 [?])` → `` | SECOND-PASS S3: Kannada p.429 has ಬಹುಲಂ ಛಂದಸಿ—ಎಂಬಲ್ಲಿ with no number |
| 429 | ` (Pā. Sū. 1-2-4 [?])` → `` | SECOND-PASS S3: Kannada p.429 has ಸಾರ್ವಧಾತುಕಮಪಿತ್—ಎಂಬುದರಿಂದ with no number |
| 430 | `vājaprasūtā [clotted [?]] satī` → `vājaprasūtāsmabhyaṃ dattānnā satī` | SECOND-PASS Q1: Kannada p.430 reads ವಾಜಪ್ರಸೂತಾಸ್ಮಭ್ಯಂ ದತ್ತಾನ್ನಾ ಸತೀ |
| 430 | `वाजप्रसूता [clotted] सती` → `वाजप्रसूतास्मभ्यं दत्तान्ना सती` | SECOND-PASS Q1: Devanagari twin; Kannada p.430 reads ವಾಜಪ್ರಸೂತಾಸ್ಮಭ್ಯಂ ದತ್ತಾನ್ನಾ ಸತೀ |
| 430 | `arśa ādityād anyatrārthīyo 'c [?]` → `arśaāditvān mattvarthiyo 'c` | SECOND-PASS Q1: Kannada p.430 reads ಅರ್ಶಆದಿತ್ವಾನ್ಮತ್ತ್ವರ್ಥಿಯೋಽಚ್ |
| 430 | `अर्श आदित्वादन्यत्रार्थीयोऽच्` → `अर्शआदित्वान्मत्त्वर्थियोऽच्` | SECOND-PASS Q1: Devanagari twin; Kannada p.430 reads ಅರ್ಶಆದಿತ್ವಾನ್ಮತ್ತ್ವರ್ಥಿಯೋಽಚ್ |
| 430 | `dāsayut… [clotted [?]] dāso` → `dāsayutyupakṣapayati śatrūniti dāso` | SECOND-PASS Q1: Kannada p.430 reads ದಾಸಯುತ್ಯುಪಕ್ಷಪಯತಿ ಶತ್ರೂನಿತಿ ದಾಸೋ ಭೃತ್ಯಃ |
| 430 | `दासयुत्कर्मस्वपयति शत्रूननिति [clotted] दासो` → `दासयुत्युपक्षपयति शत्रूनिति दासो` | SECOND-PASS Q1: Devanagari twin; Kannada p.430 reads ದಾಸಯುತ್ಯುಪಕ್ಷಪಯತಿ ಶತ್ರೂನಿತಿ ದಾಸೋ |

### 2026-11-27 second pass, batch m227-376.tsv
| page | old → new | why |
|---|---|---|
| 431 | `Va. 28 [?]"; centre: "Ṛgvedasaṃhitā"; right: 431.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 431.` | SECOND-PASS Q1: running head of Kannada p.431 reads ವ. ೨5 (Varga 25) |
| 433 | `Va. 28 [?]"; centre: "Ṛgvedasaṃhitā"; right: 433.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 433.` | SECOND-PASS Q1: running head of Kannada p.433 reads ವ. ೨5 (Varga 25) |
| 435 | `Va. 29 [?]"; centre: "Ṛgvedasaṃhitā"; right: 435.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 435.` | SECOND-PASS Q1: running head of Kannada p.435 reads ವ. ೨5 (Varga 25) |
| 437 | `Va. 29 [?]"; centre: "Ṛgvedasaṃhitā"; right: 437.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 437.` | SECOND-PASS Q1: running head of Kannada p.437 reads ವ. ೨5 (Varga 25) |
| 439 | `Va. 29 [?]"; centre: "Ṛgvedasaṃhitā"; right: 439.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 439.` | SECOND-PASS Q1: running head of Kannada p.439 reads ವ. ೨5 (Varga 25) |
| 441 | `Va. 29 [?]"; centre: "Ṛgvedasaṃhitā"; right: 441.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 441.` | SECOND-PASS Q1: running head of Kannada p.441 reads ವ. ೨5 (Varga 25) |
| 443 | `Va. 29 [?]"; centre: "Ṛgvedasaṃhitā"; right: 443.` → `Va. 25"; centre: "Ṛgvedasaṃhitā"; right: 443.` | SECOND-PASS Q1: running head of Kannada p.443 reads ವ. ೨5 (Varga 25) |
| 445 | `Va. 30 [?]"; centre: "Ṛgvedasaṃhitā"; right: 445.` → `Va. 26"; centre: "Ṛgvedasaṃhitā"; right: 445.` | SECOND-PASS Q1: running head of Kannada p.445 reads ವ. ೨6 (Varga 26) |
| 447 | `Va. 30 [?]"; centre: "Ṛgvedasaṃhitā"; right: 447.` → `Va. 26"; centre: "Ṛgvedasaṃhitā"; right: 447.` | SECOND-PASS Q1: running head of Kannada p.447 reads ವ. ೨6 (Varga 26) |
| 449 | `Va. 30 [?]"; centre: "Ṛgvedasaṃhitā"; right: 449.` → `Va. 26"; centre: "Ṛgvedasaṃhitā"; right: 449.` | SECOND-PASS Q1: running head of Kannada p.449 reads ವ. ೨6 (Varga 26) |
| 451 | `Va. 30 [?]"; centre: "Ṛgvedasaṃhitā"; right: 451.` → `Va. 26"; centre: "Ṛgvedasaṃhitā"; right: 451.` | SECOND-PASS Q1: running head of Kannada p.451 reads ವ. ೨6 (Varga 26) |
| 453 | `Va. 31 [?]"; centre: "Ṛgvedasaṃhitā"; right: 453.` → `Va. 26"; centre: "Ṛgvedasaṃhitā"; right: 453.` | SECOND-PASS Q1: running head of Kannada p.453 reads ವ. ೨6 (Varga 26) |
| 455 | `Va. 31 [?]"; centre: "Ṛgvedasaṃhitā"; right: 455.` → `Va. 26"; centre: "Ṛgvedasaṃhitā"; right: 455.` | SECOND-PASS Q1: running head of Kannada p.455 reads ವ. ೨6 (Varga 26) |
| 457 | `Va. 31 [?]"; centre: "Ṛgvedasaṃhitā"; right: 457.` → `Va. 26"; centre: "Ṛgvedasaṃhitā"; right: 457.` | SECOND-PASS Q1: running head of Kannada p.457 reads ವ. ೨6 (Varga 26) |
| 459 | `Va. 31 [?]"; centre: "Ṛgvedasaṃhitā"; right: 459.` → `Va. 26"; centre: "Ṛgvedasaṃhitā"; right: 459.` | SECOND-PASS Q1: running head of Kannada p.459 reads ವ. ೨6 (Varga 26) |
| 461 | `Va. 32 [?]"; centre: "Ṛgvedasaṃhitā"; right: 461.` → `Va. 27"; centre: "Ṛgvedasaṃhitā"; right: 461.` | SECOND-PASS Q1: running head of Kannada p.461 reads ವ. ೨7 (Varga 27) |
| 463 | `Va. 32 [?]"; centre: "Ṛgvedasaṃhitā"; right: 463.` → `Va. 27"; centre: "Ṛgvedasaṃhitā"; right: 463.` | SECOND-PASS Q1: running head of Kannada p.463 reads ವ. ೨7 (Varga 27) |
| 431 | `(Ni. 3-[?] [?])` → `(Ni. 2-17)` | SECOND-PASS Q1: Kannada p.431: ನಿ. ೨-೧೭ after ದಾಸೋ ದಸ್ಯತೇರುಪದಾಸಯತಿ ಕರ್ಮಾಣಿ |
| 431 | `Ṛ. Saṃ. 2-[?]-6 [?] [the print's numerals]` → `Ṛ. Saṃ. 3-12-6` | SECOND-PASS Q1: Kannada p.431: ಋ. ಸಂ. ೩-೧೨-೬ at ದಾಸಪತ್ನಿಃ |
| 432 | `(Ni. 2-10 [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.432: (ನಿ.೩-೯) after ಮಘಂ, ರೇಕ್ಣಃ, ರಿಕ್ಷಂ … ಧನ ನಾಮಗಳಲ್ಲಿ |
| 432 | `(Ṛ. Saṃ. 61-4; the Saṃhitā text as read, doubtful [?])` → `(Ṛ. Saṃ. 3-61-4)` | SECOND-PASS Q1: Kannada p.432: ಋ. ಸಂ. ೩-೬೧-೪ and the same words ಸ್ವರ್ಜನಂತೀ ಸುಭಗಾ ಸುದಂಸಾ ಅಂತಾದ್ದಿವಃ ಪಪ್ರಥ ಆ ಪೃಥಿವ್ಯಾಃ |
| 432 | `karmanimitta kīrtyarthaṃ*' [as read [?]]` → `karmanimitta kīrtyarthaṃ*' [as read]` | SECOND-PASS Q2: Kannada p.432 has ಅತಿಶಯವತ್ಕರ್ಮನಿಮಿತ್ತಕೀರ್ತ್ಯರ್ಥಂ, the same words |
| 432 | `1-[?]-[?] [?] earlier` → `1-77-4 earlier` | SECOND-PASS Q1: Kannada p.432: ಋ. ಸಂ. ೧-೭೭-೪ for the same compound (ವಾಜಪ್ರಸೂತಾ) |
| 432 | `, Pā. Sū. 3-4-101 [?])` → `)` | SECOND-PASS S3: Kannada p.432 and p.433 have no number after ತಸ್ಥಸ್ಥಮಿಪಾಮ್— |
| 433 | ` (Pā. Sū. 5-2-127 [?])` → `` | SECOND-PASS S3: Kannada p.433 has no number after ಅರ್ಶಆದಿಭ್ಯೋಚ್— |
| 433 | ` (Pā. Sū. 6-4-51 [?])` → `` | SECOND-PASS S3: Kannada p.433 has no number after ಣೇರನಿಟಿ— |
| 435 | `(Ni. 7-[?] [?])` → `(Ni. 9-27)` | SECOND-PASS Q1: Kannada p.435: ದರ್ಶನಾಯ ( ನಿ. ೯-೨೭ ) |
| 436 | `; the second citation's text is read with doubt from the blotted print [?])` → `)` | SECOND-PASS Q2: Kannada p.436 has ಮಹತ್ತೇ ವಿಷ್ಣೋ ಅಭಿಚಕ್ಷ್ಯಂ ಕೃತಂ ಪಶ್ಯೇಮ ತುರ್ವಶಂ ಯದುಂ ( ಋ. ಸಂ. ೮-೪-೭ ), the same text and number |
| 436 | `(Ṛ. Saṃ. 1-113-8; text as read [?])` → `(Ṛ. Saṃ. 1-124-4)` | SECOND-PASS Q1: Kannada p.436 gives ಅದ್ಮಸನ್ನ ಸಸತೋ ಬೋಧಯಂತೀ … as ಋ. ಸಂ. ೧-೧೨೪.೪ (1-113-8 belongs to the next line) |
| 436 | `(Ṛ. Saṃ. 7-79-1 [?])` → `(Ṛ. Saṃ. 7-79-1)` | SECOND-PASS Q2: Kannada p.436: ವ್ಯು ಷಾ ಅವಃ ಪಥ್ಯಾ … ( ಋ. ಸಂ. ೭-೭೯-೧ ) |
| 437 | `tatkāmasya manāyoḥ* [as read [?]]` → `tatkāmasya manāyoḥ* [as read]` | SECOND-PASS Q2: Kannada p.437 has ಮನ್ಯತೇರರ್ಚತಿಕರ್ಮಣೋ ಮನಾ ಸ್ತುತಿರುಚ್ಯತೇ । ತತ್ಕಾಮಸ್ಯ ಮನಾಯೋಃ, the same words |
| 437 | ` (Ni. 3-[?] [?])` → `` | SECOND-PASS S3: Kannada p.437 has no number after ೪೪ ಪೂಜಾಕರ್ಮನಾಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿರುವುದರಿಂದ |
| 437 | `(Ṛ. Saṃ. 4-24-3; the numerals as read [?])` → `(Ṛ. Saṃ. 4-25-5)` | SECOND-PASS Q1: Kannada p.437: ಪ್ರಿಯಃ ಸುಕೃತ್ಪ್ರಿಯ ಇಂದ್ರೇ ಮನಾಯುಃ … ( ಋ. ಸಂ. ೪-೨೫-೫ ) |
| 437 | `(Ṛ. Saṃ. 4-21-2 [?])` → `(Ṛ. Saṃ. 4-24-7)` | SECOND-PASS Q1: Kannada p.437: ಪ್ರತಿ ಮನಾಯೋರುಚಥಾನಿ ಹರ್ಯನ್ … ( ಋ. ಸಂ. ೪-೨೪-೭ ) |
| 437 | ` (Pā. Sū. 3-2-59 [?])` → `` | SECOND-PASS S3: Kannada p.437 has no number after ಋತ್ವಿಕ್‌ದಧೃಕ್— |
| 437 | ` (Pā. Sū. 6-4-24 [?])` → `` | SECOND-PASS S3: Kannada p.437 has no number after ಅನಿದಿತಾಂ ಹಲಉಪ— |
| 437 | ` (Pā. Sū. 1-4-18 [?])` → `` | SECOND-PASS S3: Kannada p.437 has no number after ಯಚಿ ಭಮ್— |
| 438 | `(Pā. Sū. 3-1-55 [?])` → `(Pā. Sū. 3-1-55)` | SECOND-PASS Q2: Kannada p.438: ಪುಷಾದಿದ್ಯುತಾದಿ-(ಪಾ. ಸೂ. ೩-೧-೫೫) |
| 440 | `'jāṇanāda' [?]]` → `'jāṇanāda']` | SECOND-PASS Q2: Kannada p.440 has ಕೃತ್ನುಃ—ಜಾಣನಾದ |
| 441 | `पुराणे देवी युवतिः` → `पुराणी देवी युवतिः` | SECOND-PASS Q1: Kannada p.441: ಪುರಾಣೀ ದೇವೀ ಯುವತಿಃ ಪುರಂಧಿರನು ವ್ರತಂ ಚರಸಿ ವಿಶ್ವವಾರೇ (Devanagari line; applied with its IAST twin) |
| 441 | `*purāṇe devī yuvatiḥ puraṃdhir anu vrataṃ carasi viśvavāre |*  (Ṛ. Saṃ. 3-61-1; the Saṃhit` → `*purāṇī devī yuvatiḥ puraṃdhir anu vrataṃ carasi viśvavāre |*  (Ṛ. Saṃ. 3-61-1)` | SECOND-PASS Q1: Kannada p.441: ಪುರಾಣೀ ದೇವೀ ಯುವತಿಃ … (ಋ. ಸಂ. ೩-೬೧-೧); IAST twin of the Devanagari edit |
| 442 | `(Ni. 6-11 [?])` → `(Ni. 8-11)` | SECOND-PASS Q1: Kannada p.442: ಶುಂಭಮಾನಾಃ—ಶುಶೋಭಿಷಮಾಣಾಃ (ನಿ. ೮-೧೧) |
| 442 | `gatikarmaṇaḥ* (Ni. 3-[?] [?])` → `gatikarmaṇaḥ* (Ni. 2-6)` | SECOND-PASS Q1: Kannada p.442: ವಿರಿತಿ ಶಕುನಿನಾಮ ವೇತೇರ್ಗತಿಕರ್ಮಣಃ । (ನಿ. ೨-೬) |
| 443 | `(Ni. 5-[?] [?])` → `(Ni. 5-22)` | SECOND-PASS Q1: Kannada p.443: ಋಕ್ಕನ್ನು ಉದಹರಿಸುತ್ತಾರೆ. (ನಿ. ೫-೨೨) |
| 443 | `(Ṛ. Saṃ. 10-43-5; the Saṃhitā text as read, doubtful [?])` → `(Ṛ. Saṃ. 10-43-5)` | SECOND-PASS Q2: Kannada p.443 has ಕೃತಂ ನ ಶ್ವಘ್ನೀ ವಿ ಚಿನೋತಿ ದೇವನೇ ಸಂವರ್ಗಂ ಯನ್ಮಘವಾ ಸೂರ್ಯಂ ಜಯತ್ (ಋ. ಸಂ. ೧೦-೪೩-೫), the same text and number |
| 443 | `Ṛ. Saṃ. 5-[?]-4 [?]; and 10-[?]-5 [?]; 6-[?]-2 [?] [the print's numerals], the word means ` → `Ṛ. Saṃ. 2-12-4; and 4-20-3, the word means *vyādha*, hunter, and in 10-42-9; 10-43-5; 8-45` | SECOND-PASS Q1: Kannada p.443: ೨-೧೨-೪; ೪-೨೦-೩ (ವ್ಯಾಧ) and ೧೦-೪೨-೯; ೧೦-೪೩-೫; ೮-೪೫-೩೮ (ಕಿತವ) – the five places other than this Ṛk |
| 443 | ` (Pā. Sū. 7-3-79 [?])` → `` | SECOND-PASS S3: Kannada p.443 has no sūtra number at this rule |
| 443 | ` (Pā. Sū. 7-2-82 [?])` → `` | SECOND-PASS S3: Kannada p.443 has no sūtra number at this rule |
| 443 | ` (Pā. Sū. 6-1-186 [?])` → `` | SECOND-PASS S3: Kannada p.443 has no sūtra number at this rule |
| 443 | ` (Pā. Sū. 4-1-15 [?])` → `` | SECOND-PASS S3: Kannada p.443 has no sūtra number at this rule |
| 443 | ` (Pā. Sū. 8-4-2 [?])` → `` | SECOND-PASS S3: Kannada p.443 has no sūtra number at this rule |
| 446 | `(Ṛ. Saṃ. 3-[?]-6 [?]; the numerals as read, doubtful)` → `(Ṛ. Saṃ. 5-80-6)` | SECOND-PASS Q1: Kannada p.446: ವ್ಯೂರ್ಣ್ವತೀ ದಾಶುಷೇ … ಪೂರ್ವಥಾಕಃ । ಮು. ಸ. ೫-೮೦-೬ (abbreviation printed ಮು. ಸ.) |
| 446 | `Ṛ. Saṃ. 6-[?]-3 [?], the explanation` → `Ṛ. Saṃ. 9-94-2, the explanation` | SECOND-PASS Q1: Kannada p.446: ಋ. ಸಂ. ೯-೯೪-೨ ಮುಂತಾದ ಋಕ್ಕುಗಳಲ್ಲಿ ಸ್ವತೇಜಸಾ ಆಚ್ಛಾದಯನ್ |
| 447 | `(Ni. 3-[?] [?])` → `(Ni. 3-19)` | SECOND-PASS Q1: Kannada p.447: ಆರು ಅಂತರ್ಹಿತ ನಾಮಗಳಲ್ಲಿ … (ನಿ. ೩-೧೯) |
| 447 | `Ṛ. Saṃ. 3-[?]-3 [?]; 5-[?]-[?] [?]; 8-[?]-3 [?]; 10-[?]-6 [?] the word` → `Ṛ. Saṃ. 2-29-2; 5-45-55; 8-97-3; 10-77-6 the word` | SECOND-PASS Q1: Kannada p.447: ಋಂ. ಸಂ. ೨-೨೯-೨ : ೫-೪೫-೫೫ ; ೮-೯೭-೩ ; ೧೦-೭೭-೬ (5-45-55 applied as printed) |
| 447 | `page 2[?] of Bāl Gaṅgādhar Tilak's book *The Arctic Home in the Vedas* [as printed; the pa` → `page 176 of Bāl Gaṅgādhar Tilak's book *The Arctic Home in the Vedas*.)` | SECOND-PASS Q1: Kannada p.447: ೧೭೬ ನೆಯ ಪುಟದಲ್ಲಿ |
| 448 | `; numerals as read; the first word is printed *īyuṣṭe* [?])` → `)` | SECOND-PASS Q2: Kannada p.448: ಈಯುಷ್ಟೇ ಯೇ ಪೂರ್ವತರಾಮಪಶ್ಯನ್ … (ಋ. ಸಂ. ೧-೧೧೩-೧೧), same number and first word |
| 448 | `Ṛ. Saṃ. 10-[?]-20 [?] (Ni. 12-[?] [?])` → `Ṛ. Saṃ. 10-85-20 (Ni. 12)` | SECOND-PASS Q1: Kannada p.448: ಋ. ಸಂ. ೧೦-೮೫-೨೦ನೇ ಋಕ್ಕನ್ನು ಉದಹರಿಸುತ್ತಾರೆ. ( ನಿ. ೧೨- ) (the Nirukta number after 12- is blank in the print) |
| 448 | ` (Pā. Sū. 8-3-9 [?])` → `` | SECOND-PASS S3: Kannada p.449 has no number after ದೀರ್ಘಾದಟ ಸಮಾನಪಾದೇ— |
| 449 | ` (Pā. Sū. 8-3-3 [?])` → `` | SECOND-PASS S3: Kannada p.449/460 has no number here after ಆತೋಟಿ ನಿತ್ಯಮ್ on p.449 |
| 449 | ` (Pā. Sū. 3-1-66 [?])` → `` | SECOND-PASS S3: Kannada p.449 has no number after ಚಿಣ್‌ಭಾವಕರ್ಮಣೋಃ— |
| 449 | ` (Pā. Sū. 1-1-37 [?])` → `` | SECOND-PASS S3: Kannada p.449 has no number after ಸ್ವರಾದಿನಿಪಾತಮವ್ಯಯಮ್ |
| 450 | `Pā. Sū. 3-1-49 [?] cleḥ sic` → `Pā. Sū. 3-1-49-58 cleḥ sic` | SECOND-PASS Q1: Kannada p.450: ಪಾ ೩-೧-೪೯-೫೮ । ಚೇಃ ಸಿಚ್ (IAST twin of the Devanagari edit) |
| 450 | `पा. सू. ३-१-४९ ` → `पा. सू. ३-१-४९-५८ ` | SECOND-PASS Q1: Kannada p.450: ಪಾ ೩-೧-೪೯-೫೮ । ಚೇಃ ಸಿಚ್ (Devanagari line; applied with its IAST twin) |
| 451 | `(Ni. 1-[?] [?])` → `(Ni. 3-24)` | SECOND-PASS Q1: Kannada p.451: ೩೭ ನದೀನಾಮಗಳಲ್ಲಿ … (ನಿ. ೩-೨೪) |
| 452 | `English insertions [?].)*` → `English insertions.)*` | SECOND-PASS Q2: Kannada p.452 has the sentence ಈ ರೀತಿ ೧-೯೨-೧೧ ಮತ್ತು ೧-೯೨-೧೨ … ಶ್ಲಾಘಿಸುತ್ತಾರೆ, as read |
| 453 | ` (Pā. Sū. 6-1-108 [?])` → `` | SECOND-PASS S3: Kannada p.453 has no number after ಸಂಪ್ರಸಾರಣಾಚ್ಚ— |
| 453 | `in the fifth Ṛk of this very sūkta [92.9 [?]]` → `in the ninth Ṛk of this very sūkta [92.9]` | SECOND-PASS Q1: Kannada p.453: ಇದೇ ಸೂಕ್ತದ ೯ ನೇ ಮಂತ್ರದಲ್ಲಿ ವ್ಯಾಖ್ಯಾತವಾಗಿದೆ |
| 453 | ` (Pā. Sū. 8-2-29 [?])` → `` | SECOND-PASS S3: Kannada p.453 has no number after ಸ್ಕೋಸಂಯೋಗಾದ್ಯೋರಂತೇಚ— |
| 454 | `is clotted in the print [?].]"` → `is clotted in the print.]"` | SECOND-PASS Q2: Kannada p.454 reads the clause clearly: ಅಸ್ಮಿನ್ಪಕ್ಷ ಏತ ಐ । ಪಾ. ೩-೪-೯೩ । ಇತ್ಯೈತ್ವಾಭಾವೋ ವ್ಯತ್ಯಯೇನ ದ್ರಷ್ಟವ್ಯಃ । ಯದ್ವೃತ್ತಯೋಗಾದನಿಘಾತಃ |
| 455 | `(Ni. 3-[?] [?]); so the meaning` → `(Ni. 3-2); so the meaning` | SECOND-PASS Q1: Kannada p.455: ಹದಿನೈದು ಅಪತ್ಯನಾಮಗಳಲ್ಲಿ … ( ನಿ. ೩-೨ ) |
| 455 | `(Ni. 10-[?] [?])."` → `(Ni. 10-7)."` | SECOND-PASS Q1: Kannada p.455: ವಿವರಿಸುತ್ತಾರೆ. (ನಿ. ೧೦-೭) |
| 456 | `(Ṛ. Saṃ. 4-251-9; read as printed, the first words *uṣo maghonyā* [?])` → `(Ṛ. Saṃ. 4-55-9; read as printed, the first words *uṣo maghonyā*)` | SECOND-PASS Q1: Kannada p.456: ಉಷೋ ಮಘೋನ್ಯಾ ವಹ ಸೂನೃತೇ … ( ಮು. ಸಂ. ೪-೫೫-೯ ) (abbreviation printed ಮು. ಸಂ.) |
| 456 | `the print gives *hṛñ*, as read [?]]` → `the print gives *hṛñ*, as read]` | SECOND-PASS Q2: Kannada p.456 has ಹೃಞ್ ಹರಣೇ ಧಾತು |
| 456 | ` (Pā. Sū. 3-4-87 [?])` → `` | SECOND-PASS S3: Kannada p.456 has no number after ಸೇರ್ಹ್ಯಪಿಚ್ಚ— |
| 456 | `hence the root's form here [?].]` → `hence the root's form here.]` | SECOND-PASS Q2: Kannada p.456 has ಹೃಗ್ರಹೋರ್ಭಶ್ಚಂದಸಿ—ಎಂಬುದರಿಂದ, the rule as cited |
| 456 | `(Pā. Sū. 3-4-93 [?])` → `(Pā. Sū. 3-4-93)` | SECOND-PASS Q2: Kannada p.456: ಏತಐ (ಪಾ. ಸೂ. ೩-೪-೯೩) |
| 457 | `का. ६-१-१८६-१ इति` → `का. ६-१-१७६-१ इति` | SECOND-PASS Q1: Kannada p.457: ಕಾ. ೬-೧-೧೭೬-೧ (Devanagari line; applied with its IAST twin) |
| 457 | `Kā. 6-1-186-1 [?] iti` → `Kā. 6-1-176-1 iti` | SECOND-PASS Q1: Kannada p.457: ಕಾ. ೬-೧-೧೭೬-೧ (IAST twin of the Devanagari edit) |
| 457 | `(Pā. Sū. 6-1-37 [?])` → `(Pā. Sū. 6-1-37-6)` | SECOND-PASS Q1: Kannada p.458: ರಯೇರ್ಮತ್ ಬಹುಲಮ್-(ಪಾ. ಸೂ. ೬-೧-೩೭-೬) |
| 457 | `(Kā. 6-1-186 [?])` → `(Kā. 6-1-176-1)` | SECOND-PASS Q1: Kannada p.458: ರೇಶಬ್ದಾಚ್ಚ ಮತುಪ ಉದಾತ್ತತ್ವಂ ವಕ್ತವ್ಯಂ (ಕಾ. ೬-೧-೧೭೬-೧) |
| 457 | `(Ni. 1-[?] [?])` → `(Ni. 2-18)` | SECOND-PASS Q1: Kannada p.458: ಹದಿನಾರು ಉಷೋನಾಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿವೆ. ( ನಿ. ೨-೧೮ ) |
| 458 | ` (Pā. Sū. 5-2-94 [?])` → `` | SECOND-PASS S3: Kannada p.458 has no number after ತದಸ್ಯಾ—ಸೂತ್ರದಿಂದ |
| 458 | ` (Pā. Sū. 8-2-9 [?])` → `` | SECOND-PASS S3: Kannada p.458 has no number after ಮಾಡುಪಧಾಯಾಶ್ಚ— |
| 458 | ` (Pā. Sū. 8-1-18 [?])` → `` | SECOND-PASS S3: Kannada p.458 has no number after ಅಪಾದಾದ್— |
| 459 | `(Ni. 2-[?] [?])` → `(Ni. 2-28)` | SECOND-PASS Q1: Kannada p.459: ಅರುಣಾ ಗಾವ ಉಷಸಾಂ । … (ನಿ. ೨-೨೮) |
| 460 | `वहन्त्वरुणास्व उप` → `वहन्त्वरुणप्सव उप` | SECOND-PASS Q1: Kannada p.460: ವಹಂತ್ವರುಣಪ್ಸವ ಉಪ ತ್ವಾ ಸೋಮಿನೋ ಗೃಹಂ (Devanagari line; applied with its IAST twin) |
| 460 | `*vahantv aruṇāsva upa tvā sominaḥ gṛham |*  (Ṛ. Saṃ. 1-14-[?] [?]; the Saṃhitā text as rea` → `*vahantv aruṇapsava upa tvā sominaḥ gṛham |*  (Ṛ. Saṃ. 1-49-1)` | SECOND-PASS Q1: Kannada p.460: ವಹಂತ್ವರುಣಪ್ಸವ ಉಪ ತ್ವಾ ಸೋಮಿನೋ ಗೃಹಂ (ಋ. ಸಂ. ೧-೪೯-೧) (IAST twin of the Devanagari edit) |
| 460 | `Ṛks 1-30-22 [?]; 1-48-1 [?]; 8-[?]-3 [?]; 4-30-2 [?] and many` → `Ṛks 1-30-22; 1-48-1; 9-11-5; 4-51-7 and many` | SECOND-PASS Q1: Kannada p.460: ೧-೩೦-೨೨ ; ೧-೪೮-೧ ; ೯--೧೧-೫ ; ೪-೫೧-೭ (the doubled hyphen of ೯--೧೧-೫ read as 9-11-5) |
| 460 | ` (Pā. Sū. 3-4-80 [?])` → `` | SECOND-PASS S3: Kannada p.460 has no sūtra number at this rule |
| 460 | ` (Pā. Sū. 8-2-30 [?])` → `` | SECOND-PASS S3: Kannada p.460 has no sūtra number at this rule |
| 460 | ` (Pā. Sū. 8-4-55 [?])` → `` | SECOND-PASS S3: Kannada p.460 has no sūtra number at this rule |
| 460 | ` (Pā. Sū. 8-3-59 [?])` → `` | SECOND-PASS S3: Kannada p.460 has no sūtra number at this rule |
| 460 | ` (Pā. Sū. 5-1-129 [?])` → `` | SECOND-PASS S3: Kannada p.460 has no sūtra number at this rule |
| 461 | `stūyete [?] |` → `stūyete |` | SECOND-PASS Q2: Kannada p.461 has ... ತೃಚೇನ ಸ್ತೂಯೇತೇ ।, the same words |
| 461 | ` (the reading of this clause is doubtful [?])` → `` | SECOND-PASS Q2: Kannada p.461 reads the clause clearly: ಉಷಃಸಾಹಚರ್ಯಾದ್ಬುದ್ಧಿಸ್ಥಾವಶ್ವಿನಾವಿದಮಾದಿಕೇನ ತೃಚೇನ ಸ್ತೂಯೇತೇ |
| 462 | `where a *pañcamī* would be expected [?])` → `where a *pañcamī* would be expected)` | SECOND-PASS Q2: Kannada p.462 has ಸುಪಾಂ ಸುಲುಗಿತಿ ಷಷ್ಠ್ಯಾ ಲುಕ್, the print reading as noted |
| 462 | `(Ā. 4-14 [?])` → `(Ā. 4-15)` | SECOND-PASS Q1: Kannada p.462: ... ತೃಚೌ ಎಂಬ ಸೂತ್ರದಿಂದ ವಿವೃತವಾಗಿರುವುದು (ಆ. ೪-೧೫) |
| 463 | `*vartiṣā* [or similar; the printed Sanskrit before it is clotted [?]]` → `*vartanyā*` | SECOND-PASS Q1: Kannada p.463: ಸಾಯಣರೂ ವರ್ತನ್ಯಾ । ಪ್ರಸಿದ್ಧೇನ ಪಥಾ |

### 2026-11-27 second pass, batch m246-395.tsv
| page | old → new | why |
|---|---|---|
| 465 | `Va. 32 [?]"; centre: "Ṛgvedasaṃhitā"; right: 465` → `Va. 27"; centre: "Ṛgvedasaṃhitā"; right: 465` | SECOND-PASS Q1: running head of Kannada p.465 reads ಅ. ೧. ಅ. ೬. ವ. ೨೭ (Varga 27) [q248] |
| 467 | `Va. 32 [?]"; centre: "Ṛgvedasaṃhitā"; right: 467` → `Va. 27"; centre: "Ṛgvedasaṃhitā"; right: 467` | SECOND-PASS Q1: running head of Kannada p.467 reads ಅ. ೧. ಅ. ೬. ವ. ೨೭ (Varga 27) [q259] |
| 469 | `Va. 33 [?]"; centre: "Ṛgvedasaṃhitā"; right: 469` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 469` | SECOND-PASS Q1: running head of Kannada p.469 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q267] |
| 471 | `Va. 28 [?]"; centre: "Ṛgvedasaṃhitā"; right: 471` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 471` | SECOND-PASS Q2: running head of Kannada p.471 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q277] |
| 473 | `Va. 28 [?]"; centre: "Ṛgvedasaṃhitā"; right: 473` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 473` | SECOND-PASS Q2: running head of Kannada p.473 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q285] |
| 475 | `Va. 29 [?]"; centre: "Ṛgvedasaṃhitā"; right: 475` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 475` | SECOND-PASS Q1: running head of Kannada p.475 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q289] |
| 477 | `Va. 29 [?]"; centre: "Ṛgvedasaṃhitā"; right: 477` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 477` | SECOND-PASS Q1: running head of Kannada p.477 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q298] |
| 479 | `Va. 29 [?]"; centre: "Ṛgvedasaṃhitā"; right: 479` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 479` | SECOND-PASS Q1: running head of Kannada p.479 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q306] |
| 481 | `Va. 30 [?]"; centre: "Ṛgvedasaṃhitā"; right: 481` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 481` | SECOND-PASS Q1: running head of Kannada p.481 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q310] |
| 483 | `Va. 30 [?]"; centre: "Ṛgvedasaṃhitā"; right: 483` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 483` | SECOND-PASS Q1: running head of Kannada p.483 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q316] |
| 485 | `Va. 30 [?]"; centre: "Ṛgvedasaṃhitā"; right: 485` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 485` | SECOND-PASS Q1: running head of Kannada p.485 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q321] |
| 487 | `Va. 31 [?]"; centre: "Ṛgvedasaṃhitā"; right: 487` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 487` | SECOND-PASS Q1: running head of Kannada p.487 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q332] |
| 489 | `Va. 31 [?]"; centre: "Ṛgvedasaṃhitā"; right: 489` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 489` | SECOND-PASS Q1: running head of Kannada p.489 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q347] |
| 491 | `Va. 31 [?]"; centre: "Ṛgvedasaṃhitā"; right: 491` → `Va. 28"; centre: "Ṛgvedasaṃhitā"; right: 491` | SECOND-PASS Q1: running head of Kannada p.491 reads ಅ. ೧. ಅ. ೬. ವ. ೨೮ (Varga 28) [q358] |
| 493 | `Va. 32 [?]"; centre: "Ṛgvedasaṃhitā"; right: 493` → `Va. 29"; centre: "Ṛgvedasaṃhitā"; right: 493` | SECOND-PASS Q1: running head of Kannada p.493 reads ಅ. ೧. ಅ. ೬. ವ. ೨೯ (Varga 29) [q370] |
| 495 | `Va. 32 [?]"; centre: "Ṛgvedasaṃhitā"; right: 495` → `Va. 29"; centre: "Ṛgvedasaṃhitā"; right: 495` | SECOND-PASS Q1: running head of Kannada p.495 reads ಅ. ೧. ಅ. ೬. ವ. ೨೯ (Varga 29) [q377] |
| 497 | `Va. 32 [?]"; centre: "Ṛgvedasaṃhitā"; right: 497` → `Va. 29"; centre: "Ṛgvedasaṃhitā"; right: 497` | SECOND-PASS Q1: running head of Kannada p.497 reads ಅ. ೧. ಅ. ೬. ವ. ೨೯ (Varga 29) [q381] |
| 499 | `Va. 33 [?]"; centre: "Ṛgvedasaṃhitā"; right: 499` → `Va. 29"; centre: "Ṛgvedasaṃhitā"; right: 499` | SECOND-PASS Q1: running head of Kannada p.499 reads ಅ. ೧. ಅ. ೬. ವ. ೨೯ (Varga 29) [q384] |
| 501 | `Va. 33 [?]"; centre: "Ṛgvedasaṃhitā"; right: 501` → `Va. 29"; centre: "Ṛgvedasaṃhitā"; right: 501` | SECOND-PASS Q1: running head of Kannada p.501 reads ಅ. ೧. ಅ. ೬. ವ. ೨೯ (Varga 29) [q390] |
| 503 | `Va. 33 [?]"; centre: "Ṛgvedasaṃhitā"; right: 503` → `Va. 29"; centre: "Ṛgvedasaṃhitā"; right: 503` | SECOND-PASS Q1: running head of Kannada p.503 reads ಅ. ೧. ಅ. ೬. ವ. ೨೯ (Varga 29) [q392] |
| 464 | ` (Pā. Sū. 3-4-101 [?])` → `` | SECOND-PASS S3: Kannada p.464 has no number after ತಸ್‌ಥಸ್ಥ— [q246] |
| 464 | ` (Pā. Sū. 7-3-78 [?])` → `` | SECOND-PASS S3: Kannada p.464 has no number after ಪಾಘ್ರಾಧ್ಮಾ— [q247] |
| 465 | `thirty-two names of speech (Ni. 1-11 [?])` → `fifty-seven names of speech (Ni. 2-33)` | SECOND-PASS Q1: Kannada p.465: ೫೭ ವಾಕ್ ನಾಮಗಳಲ್ಲಿ ( ನಿ. ೨-೩೩ ) (count and reference from the Kannada) [q249] |
| 465 | `(Ṛ. Saṃ. 10-39-12 [?]; numerals as read, doubtful)` → `(Ṛ. Saṃ. 18-39-12)` | SECOND-PASS Q1: Kannada p.465 prints ( ಋ. ಸಂ. ೧೮-೩೯-೧೨ ); applied as printed, listed in open.tsv [q250] |
| 465 | `thirty-six names of food (Ni. 2-7 [?])` → `twenty-eight names of food (Ni. 3-9)` | SECOND-PASS Q1: Kannada p.465: ೨೮ ಅನ್ನನಾಮಗಳಲ್ಲಿ ( ನಿ. ೩-೯ ) (count and reference from the Kannada) [q251] |
| 465 | `1-197-[?] [?]` → `1-157-4` | SECOND-PASS Q1: Kannada p.465: ೧-೧೫೭-೪ನೇ ಋಕ್ಕಿನಲ್ಲಿ ( ಋ. ಸಂ. ೧-೧೫೭-೪ ) [q252 q253] |
| 465 | ` (Pā. Sū. 3-4-82 [?])` → `` | SECOND-PASS S3: Kannada p.465 has no number after ಪರಸ್ಮೈಪದಾನಾಂ— [q254] |
| 466 | `(Pā. Sū. 6-1-197 [?])` → `(Pā. Sū. 6-1-197)` | SECOND-PASS Q2: Kannada p.466 has (ಪಾ. ಸೂ. ೬-೧-೧೯೭) after ಇತ್ಯಾದಿರ್ನಿತ್ಯಮ್— [q255] |
| 466 | ` [read doubtfully; evidently the rule replacing the ending by *am* [?]]` → `` | SECOND-PASS Q2: Kannada p.466 reads ಜೀ ಪ್ರಥಮಯೋರಮ್ as the English prints it [q256] |
| 466 | ` (Pā. Sū. 7-2-92 [?])` → `` | SECOND-PASS S3: Kannada p.466 has no number after ಯುವಾವೌ ದ್ವಿವಚನೇ— [q257] |
| 466 | ` (Pā. Sū. 7-2-90 [?])` → `` | SECOND-PASS S3: Kannada p.466 has no number after ಶೇಷೇ ಲೋಪಃ— [q258] |
| 468 | ` [as read, doubtful [?]]` → `` | SECOND-PASS Q2: Kannada p.468 has ಶಿಂಬಾತಾ, ಶತರಾ as the English [q262] |
| 468 | `Ṛk 6-[?]-2 [?]` → `Ṛk 6-61-7` | SECOND-PASS Q1: Kannada p.468: ೬-೬೧-೭ ನೇ ಋಕ್ಕನ್ನು ಬಿಟ್ಟರೆ [q263 q264] |
| 468 | `(Ṛ. Saṃ. 5-75-2; the Saṃhitā text as printed [?])` → `(Ṛ. Saṃ. 5-75-2)` | SECOND-PASS Q2: Kannada p.468 prints ದಸ್ರಾ ಹಿರಣ್ಯವರ್ತನೀ ಸುಷುಮ್ನಾ … ( ಋ. ಸಂ. ೫-೭೫-೨ ) as the English [q265] |
| 468 | `**GLOSS** *(The Saṃhitā texts and numerals of these four are read from the print and are d` → `` | SECOND-PASS Q2: Kannada p.468 has the four citations 5-75-2, 8-5-11, 8-8-1, 8-87-5 with the same Saṃhitā text; numerals agree [q266] |
| 469 | ` (Pā. Sū. 7-1-3 [?])` → `` | SECOND-PASS S3: Kannada p.469 has no number after ಝೋಂತಃ— [q268] |
| 469 | ` (Pā. Sū. 3-4-86 [?])` → `` | SECOND-PASS S3: Kannada p.469 has no number after ಏರುಃ— [q269] |
| 469 | ` (Pā. Sū. 6-1-97 [?])` → `` | SECOND-PASS S3: Kannada p.469 has no number after ಅತೋಗುಣೇ— [q270] |
| 469 | `'pūrvarūpa' [?])` → `'pūrvarūpa')` | SECOND-PASS Q2: Kannada p.469 has ಪೂರ್ವರೂಪ [q271] |
| 469 | `krameṇānuvākyāḥ [?] |` → `krameṇānuvākyāḥ |` | SECOND-PASS Q2: Kannada p.469 has ಕ್ರಮೇಣಾನುವಾಕ್ಯಾಃ [q272] |
| 469 | ` [reading of the opening words doubtful]` → `` | SECOND-PASS Q2: twin of q272: Kannada p.469 has ಕ್ರಮೇಣಾನುವಾಕ್ಯಾಃ [q272] |
| 469 | ` [reading doubtful [?]]` → `` | SECOND-PASS Q2: Kannada p.469 has ಕ್ರಮೇಣಾನುವಾಕ್ಯಾಃ [q273] |
| 470 | ` [?]** *(the two varga numerals, in small Kannada digits, as read; doubtful [?])*` → `**` | SECOND-PASS Q2: Kannada p.470: ವರ್ಗ— ೨೮, ೨೯ [q274 q275] |
| 470 | `८-३-८१` → `८-३-८२` | SECOND-PASS Q1: Kannada p.470-471: ಪಾ.- ೮-೩-೮೨ (Devanagari twin of q276) [q276] |
| 470 | `Pā. Sū. 8-3-81 [?]*` → `Pā. Sū. 8-3-82*` | SECOND-PASS Q1: Kannada p.470-471: ಪಾ.- ೮-೩-೮೨ [q276] |
| 471 | `(Pā. Sū. 6-3-27 [?])` → `(Pā. Sū. 6-3-27)` | SECOND-PASS Q2: Kannada p.472 has ಈದಗ್ನೇಃ ಸೋಮವರುಣಯೋಃ-(ಪಾ. ಸೂ. ೬-೩-೨೭) [q278] |
| 471 | `'*dedhaprtnāni dāśuṣe*' (garbled in my reading [?]; **corrected after p. 475, where the sa` → `'*dadhad ratnāni dāśuṣe*' ("bestowing jewels on the giver")` | SECOND-PASS Q1: Kannada p.471 and p.475 print ದಧದ್ರತ್ನಾನಿ ದಾಶುಷೇ [q279] |
| 471 | `(Ni. 2-6 [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.471: ಹರತಂ—… ಹರತಿ ಎಂಬುದು ಪಠಿತವಾಗಿರುವುದರಿಂದಲೂ (ನಿ. ೩-೯) [q280] |
| 472 | `(Ni. 3-6 [?])` → `(Ni. 3-13)` | SECOND-PASS Q1: Kannada p.472: ಮಯಃ—ಶರ್ಮ, ಸೂಮಕಂ … ( ನಿ. ೩-೧೩ ) [q281] |
| 472 | ` (Pā. Sū. 6-4-8 [?])` → `` | SECOND-PASS S3: Kannada p.472 has no number after ಸರ್ವನಾಮಸ್ಥಾನೇ ಚಾಸಂಬದ್ಧೌ— [q283] |
| 472 | `(Pā. Sū. 3-3-75 [?])` → `(Pā. Sū. 3-3-75)` | SECOND-PASS Q2: Kannada p.472: ಭಾವೇಽನುಪಸರ್ಗಸ್ಯ (ಪಾ. ಸೂ. ೩-೩-೭೫) [q284] |
| 473 | ` (Pā. Sū. 6-2-144 [?])` → `` | SECOND-PASS S3: Kannada p.473 has no number after ಸೂಪಮಾನಾತ್ ಕ್ತಃ— [q286] |
| 474 | `(Ā. 1-6 [?])` → `(Ā. 1-6)` | SECOND-PASS Q2: Kannada p.474: ( ಆ. ೧-೬ ) [q288] |
| 475 | `(Ṛ. Saṃ. 9-[?]-4 [?];` → `(Ṛ. Saṃ. 9-78-4;` | SECOND-PASS Q1: Kannada p.475: ( ಋ. ಸಂ. ೯-೭೮-೪ ) [q290 q291] |
| 475 | ` (Uṇādi 4-189 [?])` → `` | SECOND-PASS S3: Kannada p.475 has no number after ಸರ್ವಧಾತುಭ್ಯ ಅಸುನ್— [q293] |
| 475 | ` [as printed; a nominal verb-stem [?]]` → `` | SECOND-PASS Q2: Kannada p.475 has ಸಪರ ಪೂಜಾಯಾಂ ಧಾತು as the English [q294] |
| 475 | `(Pā. Sū. 3-1-27 [?])` → `(Pā. Sū. 3-1-27)` | SECOND-PASS Q2: Kannada p.475: ಕಂಡ್ವಾದಿಭ್ಯೋ ಯಕ್ (ಪಾ. ಸೂ. ೩-೧-೨೭) [q295] |
| 475 | ` (Pā. Sū. 6-4-112 [?])` → `` | SECOND-PASS S3: Kannada p.475 has no number after ಶ್ನಾಭ್ಯಸ್ತಯೋರಾತಃ— [q296] |
| 475 | ` (Pā. Sū. 8-4-55 [?])` → `` | SECOND-PASS S3: Kannada p.475 has no number after ಖರಿ ಚ— [q297] |
| 477 | `(Ni. 2-7 [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.477: ( ನಿ. ೩-೯ ) [q299] |
| 477 | `(Ṛ. Saṃ. 10-[?]-[?] [?])` → `(Ṛ. Saṃ. 10-186-1)` | SECOND-PASS Q1: Kannada p.477: ( ಋ. ಸಂ. ೧೦-೧೮೬-೧ ) [q300 q301 q302] |
| 477 | `(Ṛ. Saṃ. 5-255; the Saṃhitā text as read, doubtful)` → `(Ṛ. Saṃ. 5-25-5; the Saṃhitā text as read, doubtful)` | SECOND-PASS Q1: Kannada p.477: ( ಋ. ಸಂ. ೫-೨೫-೫ ) (numeral of the citation the GLOSS speaks of) [q303] |
| 477 | `**GLOSS** *(Both first citations are read with considerable doubt [?].)*` → `` | SECOND-PASS Q2: numerals of both first citations settled from Kannada p.477 (6-2-5, 5-25-5) [q303] |
| 478 | ` (Pā. Sū. 3-3-94 [?])` → `` | SECOND-PASS S3: Kannada p.478 has no number after ಸ್ತ್ರೀಯಾಂ ಕ್ತಿನ್— [q304] |
| 478 | `(Pā. Sū. 6-2-50 [?])` → `(Pā. Sū. 6-2-50)` | SECOND-PASS Q2: Kannada p.478: ತಾದೌಚ ನಿತಿ (ಪಾ. ಸೂ ೬-೨ ೫೦) [q305] |
| 479 | ` (Pā. Sū. 3-1-73 [?])` → `` | SECOND-PASS S3: Kannada p.479 has no number after ಸ್ವಾದಿಭ್ಯಃ ಶ್ನುಃ— [q307] |
| 480 | `tvāṣṭrasakāśād utpannaṃ [?] vṛtram` → `tvāṣṭrasakāśād utpannaṃ vṛtram` | SECOND-PASS Q2: Kannada p.480 has ತ್ವಷ್ಟೃಸಕಾಶಾದುತ್ಪನ್ನಂ ವೃತ್ರಮವಾತಿರತಂ [q308] |
| 480 | ` [reading doubtful] वृत्र` → `वृत्र` | SECOND-PASS Q2: twin of q308 [q308] |
| 480 | ` [reading doubtful [?]]` → `` | SECOND-PASS Q2: Kannada p.480 has ತ್ವಷ್ಟೃಸಕಾಶಾದುತ್ಪನ್ನಂ ವೃತ್ರಂ [q309] |
| 481 | `10-[?]-10 [?] [numerals as read, doubtful]` → `10-169-1` | SECOND-PASS Q1: Kannada p.481: ಋ. ಸಂ. ೧೦-೧೬೯-೧ನೇ ಋಕ್ಕಿನ ಕೊನೆಯ ಪಾದವಾದ ಅವಸಾಯ ಪದ್ವತೇ ರುದ್ರ ಮೃಳ [q311 q312] |
| 482 | `9-34-6 [?]; the same Ṛk as cited on p. 396 with the numeral 9-24-6` → `9-24-6` | SECOND-PASS Q1: Kannada p.482: ( ಋ. ಸಂ. ೯-೨೪-೬ ) after ಪವಸ್ವ ವೃತ್ರಹಂತ… [q315] |
| 483 | ` (Pā. Sū. 8-1-72 [?])` → `` | SECOND-PASS S3: Kannada p.483 has no number after ಆಮಂತ್ರಿತಂ ಪೂರ್ವಮವಿದ್ಯಮಾನವತ್— [q317] |
| 483 | ` (Pā. Sū. 8-4-1 [?])` → `` | SECOND-PASS S3: Kannada p.483 has no number after ರಷಾಭ್ಯಾಂ ನೋಣಃ ಸಮಾನಪದೇ— [q318] |
| 483 | `(Pā. Sū. 7-1-59 [?])` → `(Pā. Sū. 7-1-59)` | SECOND-PASS Q2: Kannada p.483: ಶೇ ಮುಚಾದೀನಾಮ್ (ಪಾ. ಸೂ. ೭-೧-೫೯) [q319] |
| 484 | ` *(The sūtra's words are as printed, with *indrāgnī* where *agnīṣomau* would be expected; ` → `` | SECOND-PASS Q2: Kannada p.484 has ಯುವಮೇತಾನಿ ದಿವಿ ರೋಚನಾನೀಂದ್ರಾಗ್ನೀ ಅವಸಾ ಗತಂ । ಆ. ೧-೬ [q320] |
| 485 | `avadyāt [clotted [?]] pāpād amuñcataṃ` → `avadyāt tasmāt pāpād amuñcataṃ` | SECOND-PASS Q1: Kannada p.485 has ಪ್ರಕಟಿತಾದವದ್ಯಾತ್ತಸ್ಮಾತ್ಪಾಪಾದಮುಂಚತಂ [q322] |
| 485 | `[clotted] पापादमुञ्चतं` → `तस्मात् पापादमुञ्चतं` | SECOND-PASS Q1: twin of q322 [q322] |
| 485 | `Tai. Brā. 3-2-5-1 [?] | iti` → `Tai. Brā. 3-2-5-1 | iti` | SECOND-PASS Q2: Kannada p.485: ತೈ. ಬ್ರಾ. ೩-೨-೫-೧ [q323] |
| 485 | `from the base [?] sin, *amuñcatam*, you two released [the clotted words of the print are g` → `from the base, from that sin, *amuñcatam*, you two released` | SECOND-PASS Q1: Kannada p.485 reads ಅವದ್ಯಾತ್ತಸ್ಮಾತ್ಪಾಪಾತ್ ಅಮುಂಚತಂ [q324 q325] |
| 485 | `(Tai. Brā. 3-2-5-1 [?])` → `(Tai. Brā. 3-2-5-1)` | SECOND-PASS Q2: Kannada p.485: ತೈ. ಬ್ರಾ. ೩-೨-೫-೧ [q326] |
| 486 | `(Ṛ. Saṃ. 627-7; 6-4-2 [?]; 6-44-23 [?]; 9-[?]-[?] [?], and so on)` → `(Ṛ. Saṃ. 6-7-7; 6-8-2; 6-44-23; 9-97-41, and so on)` | SECOND-PASS Q1: Kannada p.486: ( ಋ. ಸಂ. ೬-೭-೭ ; ೬-೮-೨ ; ೬-೪೪-೨೩ ; ೯-೯೭-೪೧ ಇತ್ಯಾದಿ ) [q327 q328 q329 q330 q331] |
| 487 | `(Ni. 1-[?] [?])` → `(Ni. 2-24)` | SECOND-PASS Q1: Kannada p.487: ನದೀನಾಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿರುವುದರಿಂದ (ನಿ. ೨-೨೪) [q333 q334] |
| 487 | `3-2-[5]-1 [?]` → `3-2-5-1` | SECOND-PASS Q2: Kannada p.487: ತೈತ್ತಿರೀಯ ಬ್ರಾಹ್ಮಣದ ೩-೨-೫೧ನೆಯ ವಾಕ್ಯ [q335] |
| 487 | `(Tai. Brā. 3-2-5-1 [?])` → `(Tai. Brā. 3-2-5-1)` | SECOND-PASS Q2: Kannada p.487: ತೈತ್ತಿರೀಯ ಬ್ರಾಹ್ಮಣದ ೩-೨-೫೧ (and p.485 ತೈ. ಬ್ರಾ. ೩-೨-೫-೧) [q336] |
| 487 | ` [as read [?]]` → `` | SECOND-PASS Q2: Kannada p.487 has ಸ್ಯಂದನಾತ್ ಸಿಂಧವೋ ರಶ್ಮಯ ಇಹೋಚ್ಯಂತೇ as the English [q337] |
| 487 | `(Ṛ. Saṃ. 1-[?]-[?] [?])` → `(Ṛ. Saṃ. 1-52-14)` | SECOND-PASS Q1: Kannada p.487: ನ ಸಿಂಧವೋ ರಜಸೋ ಅಂತಮಾನಶುಃ (ಋ. ಸಂ. ೧-೫೨-೧೪) [q338 q339 q340] |
| 487 | ` (Pā. Sū. 7-2-88 [?])` → `` | SECOND-PASS S3: Kannada p.487 has no number after ಪ್ರಥಮಾಯಾಶ್ಚ ದ್ವಿವಚನೇ ಭಾಷಾಯಾಮ್— [q341] |
| 488 | ` (Pā. Sū. 6-4-112 [?])` → `` | SECOND-PASS S3: Kannada p.488 has no number after ಶ್ನಾಭ್ಯಸ್ತಯೋರಾತಃ— [q342] |
| 488 | ` (Pā. Sū. 8-3-2 [?])` → `` | SECOND-PASS S3: Kannada p.488 has no number after ಅತ್ರಾನುನಾಸಿಕಃ ಪೂರ್ವಸ್ಯ ತು ವಾ— [q343] |
| 488 | ` (Pā. Sū. 7-2-35 [?])` → `` | SECOND-PASS S3: Kannada p.488 has no number after ಅರ್ಧಧಾತುಕಸ್ಯೇಡ್ವಲಾದೇಃ— [q344] |
| 488 | ` (Pā. Sū. 6-1-16 [?])` → `` | SECOND-PASS S3: Kannada p.488 has no number after ಗ್ರಹಿಜ್ಯಾವಯಿ— [q345] |
| 488 | `as Vedic [?]. Accent` → `as Vedic. Accent` | SECOND-PASS Q2: Kannada p.489 bhāṣya: ಛಾಂದಸಮಭ್ಯಾಸಸ್ಯ ದೀರ್ಘತ್ವಂ [q346] |
| 489 | `tasmād dhānyadevatāni [clotted [?]] sarvāṇi havīṃṣi hūyante | tasmād yamaṃ [clotted [?]] s` → `tanmadhye 'nyadevatyāni sarvāṇi havīṃṣi hūyante | tanmadhyamaṃ sthānam` | SECOND-PASS Q1: Kannada p.489 reads ತನ್ಮಧ್ಯೇಽನ್ಯದೇವತ್ಯಾನಿ ಸರ್ವಾಣಿ ಹವೀಂಷಿ ಹೂಯಂತೇ । ತನ್ಮಧ್ಯಮಂ ಸ್ಥಾನಮಗ್ನೀಷೋಮಕೃತಂ [q349 q350] |
| 489 | `तस्माद्धैन्यदेवतानि [clotted] सर्वाणि हवींषि हूयन्ते । तस्माद्यमं [clotted] स्थानम` → `तन्मध्येऽन्यदेवत्यानि सर्वाणि हवींषि हूयन्ते । तन्मध्यमं स्थानम` | SECOND-PASS Q1: twin of q349/q350 (Devanagari made from the Kannada by sp_sanskrit.py) [q349 q350] |
| 489 | `so all the oblations of the other deities are offered [the clause is clotted [?]]; so the ` → `in that middle all the oblations of the other deities are offered; that middle place is ma` | SECOND-PASS Q1: Kannada p.489 reads ತನ್ಮಧ್ಯೇಽನ್ಯದೇವತ್ಯಾನಿ … ತನ್ಮಧ್ಯಮಂ ಸ್ಥಾನಮಗ್ನೀಷೋಮಕೃತಂ [q351] |
| 490 | `In the Ṛk 1-96-4 [?] they explain this word as Agni, and in 1-190-3 [?]` → `In the Ṛk 1-96-4 they explain this word as Agni, and in 1-141-3` | SECOND-PASS Q1: Kannada p.490: ಋ. ಸಂ. ೧-೯೬-೪ … ೧-೧೪೧-೩ನೆಯದರಲ್ಲಿ ಯಜಮಾನನೆಂದೂ [q352 q353] |
| 490 | `3-3-3; 3-11-2 [?]; 4-2-3 [?]]` → `3-3-3; 3-11-2; 4-2-3]` | SECOND-PASS Q2: Kannada p.490: ( ಋ. ಸಂ. ೩-೩-೩ ; ೩-೧೧-೨ ; ೪-೨-೩ ಇತ್ಯಾದಿ ) [q354 q355] |
| 490 | `(Ṛ. Saṃ. 1-60-1; the Saṃhitā text as read, doubtful [?])` → `(Ṛ. Saṃ. 1-31-3; the Saṃhitā text as read, doubtful [?])` | SECOND-PASS Q1: Kannada p.490: ತ್ವಮಗ್ನೇ ಪ್ರಥಮೋ ಮಾತರಿಶ್ವನ … ( ಋ. ಸಂ. ೧-೩೧-೩ ); number only, [?] kept for the text [q356] |
| 491 | `(Ṛ. Saṃ. 1-[?]-[?] [?], numerals as read, doubtful)` → `(Ṛ. Saṃ. 1-128-2)` | SECOND-PASS Q1: Kannada p.491: ಯಂ ಮಾತರಿಶ್ವಾ ಮನವೇ ಪರಾವತೋ ದೇವಂ ಭಾಃ ಪರಾವತಃ । ( ಋ. ಸಂ. ೧-೧೨೮-೨) [q359 q360 q361] |
| 491 | `(Ṛ. Saṃ. 10-144-4 [?])` → `(Ṛ. Saṃ. 10-144-4)` | SECOND-PASS Q2: Kannada p.491: ( ಋ. ಸಂ. ೧೦ ೧೪೪-೪ ) after ಯಂ ಸುಪರ್ಣಃ ಪರಾವತಃ [q362] |
| 491 | `(Ai. Brā. 3-25 [read: 3-[?]] to 3-26 [?])` → `(Ai. Brā. 3-25 to 3-27)` | SECOND-PASS Q1: Kannada p.491: (ಐ.ಬ್ರಾ. ೩-೨೫ರಿಂದ ೨೭) [q363 q364] |
| 492 | `3-9-4-10 [?])` → `3-9-4-10)` | SECOND-PASS Q2: Kannada p.492: (ಶ. ಬ್ರಾ. ೩-೪-೧-೧೨; ೩-೯-೪-೧೦) [q366] |
| 492 | `(Ni. 2-7 [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.492: ಅಂಧಃ, ವಾಜಃ, ಪಯಃ ( ನಿ. ೩-೯ ) [q367] |
| 492 | `(Ni. 3-[?] [?])` → `(Ni. 12-34)` | SECOND-PASS Q1: Kannada p.492: ಬ್ರಹ್ಮಶಬ್ದಕ್ಕೆ ಕರ್ಮ ಅಥವಾ ಮಂತ್ರವೆಂದು … (ನಿ. ೧೨-೩೪) [q368 q369] |
| 493 | `[as printed for *bhṛñ*? — the print gives *hṛñ*, with the Vedic *h→bh* by the rule cited b` → `` | SECOND-PASS Q2: Kannada p.493: ಜಭಾರ—ಹೃಞ್ ಹರಣೇ ಧಾತು; ಹೃಗ್ರಹೋರ್ಭಶ್ಚಂದಸಿ— [q371] |
| 493 | ` (Pā. Sū. 3-4-82 [?])` → `` | SECOND-PASS S3: Kannada p.493 has no number after ಪರಸ್ಮೈಪದಾನಾಂ— [q372] |
| 493 | ` (Pā. Sū. 7-2-116 [?])` → `` | SECOND-PASS S3: Kannada p.493 has no number after ಅತ ಉಪಧಾಯಾಃ— [q373] |
| 493 | ` (Pā. Sū. 1-2-4 [?])` → `` | SECOND-PASS S3: Kannada p.493 has no number after ಸಾರ್ವಧಾತುಕಮಪಿತ್— [q374] |
| 493 | ` (Pā. Sū. 6-4-24 [?])` → `` | SECOND-PASS S3: Kannada p.493 has no number after ಅನಿದಿತಾಂ ಹಲಃ— [q375] |
| 494 | `hy asastaṃ [clotted [?]]` → `thasastaṃ` | SECOND-PASS Q1: Kannada p.494: ಥಸಸ್ತಂ (IAST by sp_sanskrit.py) [q376] |
| 494 | `ह्यसस्तं [clotted]` → `थसस्तं` | SECOND-PASS Q1: twin of q376 (Devanagari by sp_sanskrit.py from ಥಸಸ್ತಂ) [q376] |
| 495 | `(Tai. Saṃ. 2-6-10-2 [?])` → `(Tai. Saṃ. 2-6-10-2)` | SECOND-PASS Q2: Kannada p.495: ೨-೬-೧೦-೨) ಎಂಬಲ್ಲಿ ಶಂಯುವೆಂದರೆ ಬೃಹಸ್ಪತಿ ಪುತ್ರ [q380] |
| 497 | `Pā. Sū. 6-2-53-1 [?] iti` → `Pā. Sū. 6-3-95-1 iti` | SECOND-PASS Q1: Kannada p.497: ಪಾ. ೬-೩-೯೫-೧ । ಇತಿ ವಚನಾತ್ [q383] |
| 497 | `६-२-५३-१` → `६-३-९५-१` | SECOND-PASS Q1: twin of q383: Kannada p.497 ಪಾ. ೬-೩-೯೫-೧ [q383] |
| 499 | `(Ṛ. Saṃ. 1-[?]-[?] [?]; numerals as read, doubtful)` → `(Ṛ. Saṃ. 8-48-9)` | SECOND-PASS Q1: Kannada p.499: ಯತ್ತೇ ವಯಂ ಪ್ರಮಿನಾಮ ವ್ರತಾನಿ … (ಋ. ಸಂ. ೮-೪೮-೯) [q385 q386 q387] |
| 499 | `(Ni. 2-2 [?])` → `(Ni. 3-7)` | SECOND-PASS Q1: Kannada p.499: ಮನುಷ್ಯಾಃ, ನರಃ, ಧನಾಃ … (ನಿ.೩-೭) [q388] |
| 501 | `(Ni. 2-6 [?])` → `(Ni. 3-9)` | SECOND-PASS Q1: Kannada p.501: ವಶ್ಮಿ, ಉಷ್ಮಸಿ … ಕಾಂತಿಕರ್ಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿರುವುದರಿಂದ (ನಿ. ೩-೯) [q391] |
| 503 | `(Ni. 2-[?] [?])` → `(Ni. 2-28)` | SECOND-PASS Q1: Kannada p.503: ಜ್ವಲನ ಕರ್ಮಗಳಲ್ಲಿ ಪಠಿತವಾಗಿರುವುದರಿಂದ (ನಿ. ೨-೨೮) [q393 q394] |
| 503 | `(Pā. Sū. 8-1-66 [?])` → `(Pā. Sū. 8-1-66)` | SECOND-PASS Q2: Kannada p.503: ಯದ್ವೃತ್ತಾನಿತ್ಯಮ್ (ಪಾ. ಸೂ. ೮-೧ ೬೬) [q395] |
