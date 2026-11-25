# Vol 24 — independent QA sample (Kannada → English)

Date: 2026-11-24. Read-only check; no file other than this report was changed.

**Method.** For each printed page I compared the Kannada prose with the English page section in `vol24/Rigveda_Samhita_Vol24_English_Translation.md` (`### Printed p. N`). The prose checked was Pratipadārtha, Bhāvārtha, printed English, Anuvāda/introduction, Particulars and Special Topics. The Kannada came from the per-window `vol24/work/wNNNN/kn_final.md`, which the script builds from `vol24/html/rig_24.md`. For p. 75 and the page-label finding I also read the raw `html/rig_24.md` directly.

I did not judge the Sanskrit blocks. I read the Gists only for things that have nothing to do with the Sanskrit, such as translator remarks.

## Pages checked

| # | Printed p. | Sample | Content | Result |
|---|---|---|---|---|
| 1 | 20 | a | S. 21 Ṛk 15 tr., Ṛk 16 Pratipadārtha | OK |
| 2 | 75 | a | S. 24 Ṛk 2 end (अति, दाशसि, Bhāvārtha, English) | text OK; **page label missing** (F4) |
| 3 | 130 | a | S. 25 last Ṛk; start of S. 26 | 1 MINOR |
| 4 | 190 | a | S. 29 Anuvāda, Particulars | OK |
| 5 | 250 | a | S. 32 Ṛk 24 | OK |
| 6 | 320 | a | S. 36 Pratipadārtha/Bhāvārtha | OK |
| 7 | 380 | a | S. 41 Ṛk 4 | OK |
| 8 | 450 | a | S. 44 last tr.; S. 45 Anuvāda (continues on p. 451) | OK |
| 9 | 520 | a | S. 46 Ṛk 28 tr.; Ṛk 29 | **1 ERROR** (F1) |
| 10 | 600 | a | S. 51 Ṛk 7 | 1 MINOR |
| 11 | 690 | a | S. 61 Ṛk 2–3 | OK |
| 12 | 770 | a | S. 66 Ṛk | OK |
| 13 | 17 | b | S. 21 Ṛk 14 + Special topics | OK |
| 14 | 89 | b | S. 24 Ṛk + Special topics | OK |
| 15 | 153 | b | S. 26 Ṛk 21 + Special topics | OK |
| 16 | 230 | b | S. 32 + Special topics (tūrṇāśa) | **1 ERROR** (F2) |
| 17 | 295 | b | S. 35 + Special topics (sacā) | OK |
| 18 | 377 | b | S. 41 + Special topics (Ni. 10-5) | OK |
| 19 | 422 | b | S. 43 + Special topics (śīraṃ pāvakaśociṣaṃ) | **1 ERROR** (F3) |
| 20 | 483 | b | S. 45 + Special topics (maryāḥ, Ni. 4-2) | OK |
| 21 | 560 | b | S. 48 + Special topics (ṛdūdara, Ni. 6-4) | OK |
| 22 | 635 | b | S. 55/56 + Special topics | OK |
| 23 | 729 | b | S. 63 + Special topics (Ā. 7-12) | 1 MINOR |
| 24 | 789 | b | S. 67 + Special topics (Ā. 3-8) | 1 MINOR |

## Findings

| # | Page | Source (Kannada / supplied text) | English as it stands | Class | Fix |
|---|---|---|---|---|---|
| F1 | 520 | After the Bhāvārtha of Ṛk 29: *English Translation.* "I have now received (a gift) dear to the beneficent king, sixty thousand bulls vigorous like horses." | Missing. The English goes from the Bhāvārtha straight to `#### Ṛk 30`. The sentence occurs nowhere in the file. Count: 730 `English Translation` in the kn_final files against 729 in the English. | ERROR (omission) | Add `##### English translation` plus that sentence after the Ṛk 29 Bhāvārtha, as a logged repair. |
| F2 | 230 | Special topics: "ತೂರ್ಣಾಶಂ—… ಯಾಸ್ಕರು …—ತೂರ್ಣಾಶಂ । ತೂರ್ಣಾಶಮುದಕಂ ಭವತಿ ತೂರ್ಣಮಶ್ನುತೇ । ತೂರ್ಣಾಶಂ ನ ಗಿರೇರಧಿ ಇತ್ಯಪಿ ನಿಗಮೋ ಭವತಿ । (ನಿ. ೫-೧೬)" | Line 10393. The inline quotation runs on far past Yāska. It takes in the end of Sāyaṇa's bhāṣya ("तूर्णाशं न यथा घर्मे…"), the whole Kannada Pratipadārtha and Bhāvārtha transliterated into Devanagari and then into IAST, the printed English sentence twice, and the Special-topics opening again. This is about 4,000 characters with no place in the source passage. | ERROR (addition; the Yāska passage is wrongly given) | Limit the ⟦ ⟧ to the Nirukta passage `तूर्णाशं । तूर्णाशमुदकं भवति तूर्णमश्नुते । तूर्णाशं न गिरेरधि इत्यपि निगमो भवति ।` (Ni. 5-16), delete the rest, and fix the span-closing logic in the shared tool. |
| F3 | 422 | Special topics: "… ಯಾಸ್ಕರು ತಮ್ಮ ನಿರುಕ್ತದಲ್ಲಿ— ಶೀರಂ ಪಾವಕಶೋಚಿಷಂ । ಪಾವಕದೀಪ್ತಿಂ । ಅನುಶಾಯಿನಮಿತಿ ನಾಶಿನಮಿತಿ ನಾ (೨-೪-೧೪)" | Line 19178. The same overrun as F2. The "Yāska" quotation actually holds the Saṃhitā and Pada of Ṛk 30/31, Sāyaṇa's bhāṣya, the Kannada Pratipadārtha and Bhāvārtha (Devanagari, then IAST), and the printed English twice. Only after all that comes the real Nirukta text. | ERROR (addition; wrong quotation) | Limit the quotation to `शीरं पावकशोचिषं । पावकदीप्तिं । अनुशायिनमिति नाशिनमिति ना` (2-4-14), keeping the existing NOTE on `ना`, and delete the rest. |
| F4 | 75 (also 59, 61, 63, 64, 260) | `rig_24.md` l. 3270 has the head "ಆ. ೬. ಆ. ೨. ವ. ೧೫. ] ಋಗ್ವೇದಸಂಹಿತಾ 75", followed by the text of p. 75. | The English has no `### Printed p. 75`. The text of p. 75 (अति, दाशसि, the Ṛk 2 Bhāvārtha and the printed English) sits under `### Printed p. 76`. The same happens for printed heads that exist in the source but have no English marker: p. 59 (l. 2590), 61 (l. 2672), 63 (l. 2752), 64 (l. 2793) and 260 (l. 11031). Their text is under the next marker that exists (pp. 60, 62, 65, 65, 261; for 259–260 it is under p. 258). `STATUS.md` calls these pages "no running head", but the heads are there with OCR slips (ಆ for ಅ, "೩ - .", spacing). | ERROR (page references wrong) | Teach the head detection in `tools/rv/html_pages.py` these variants, then insert the missing `### Printed p. N` markers by a logged repair. I verified pp. 75 and 260; for the others I confirmed only that the head is present in the source. |
| F5 | 490 (found by scan, outside the sample) | Gist of the S. 46 metres passage (Sanskrit only) | "The rest of the statement on the metres, **as the preceding window left it**: …" (line 22469) | MINOR (translator/pipeline remark with no source; breaks rule 2) | Delete the clause "as the preceding window left it". |
| F6 | 729 | "ಪ್ರತಿಪತ್ತೃಚವನ್ನಾಗಿ" (as the pratipad triplet) | "to be recited as the pratipad-ṛcā" | MINOR (term) | Change to "as the pratipad tṛca (opening triplet)". |
| F7 | 789 | "ಅನೇಹೋ ನಃ ಎಂಬ ಈ ಋಕ್ಕನ್ನು" | "this Ṛk "anehoḥ naḥ"" | MINOR (stray ḥ; the quotation is not in ⟦ ⟧ form) | Change to अनेहो नः (*aneho naḥ*), copied in the usual inline form. |
| F8 | 600 | Bhāvārtha: "ದೇವತಾತ್ಮನಾದ ನಿನ್ನನ್ನು ಉದ್ದೇಶಿಸಿ ಅರ್ಪಿಸಿದ ಹವಿರ್ದಾನವು" | "the gift of oblation offered with you, of divine nature, in view" | MINOR (garbled syntax; meaning recoverable) | Change to "the gift of oblation offered to you, who are of divine nature". |
| F9 | 130 | "ಮತೀ—ಸ್ತುತಿಯ ಫಲವಾಗಿ (ಮಿತ್ರಾವರುಣರ ಅನುಗ್ರಹದಿಂದ)" | "मती—praise, as the fruit of praise (…)" | MINOR (adds "praise,") | Change to "मती—as the fruit of the praise (by the favour of Mitra and Varuṇa)". |

Checked and found faithful: numbers (Ṛk counts, anuvāka and varga numbers, Ā./Ni./Anu. references), names (Kaśyapa Mārīca / Manu Vaivasvata, Triśoka Kāṇva, Praskaṇva, Nābhāka), negations (pp. 20, 483, 600, 770) and attribution (p. 483, "Indra said"). Sentences that cross a page break (450/451, 690/691, 377/378, 320/321) are kept on the earlier page, and none was misplaced. Where the English has a NOTE at a source OCR slip (pp. 377, 422, 450), I did not count it as an error.

Observation outside the remit (Sanskrit blocks not judged): several `>` blocks labelled as bhāṣya also hold Kannada prose in Devanagari transliteration. Examples are line 44 (the S. 21 Anuvāda) and lines 13562–13570 (a Kannada Pratipadārtha and Bhāvārtha). In the cases I looked at, the English renderings are still present. This should go to the script check.

## Totals

- Pages checked: **24** (12 fixed pages plus 12 Special-topics pages)
- ERRORs: **4**. F1 is an omission on p. 520. F2 and F3 are quotation overruns on pp. 230 and 422. F4 is missing page markers: p. 75 in the sample and pp. 59, 61, 63, 64 and 260 outside it.
- MINORs: **5** (F5–F9; F5 was found outside the sample)
