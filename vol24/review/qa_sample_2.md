# Vol 24: independent QA sample 2 (Kannada → English)

Date: 2026-11-24. This was a read-only check. The only file written is this report.

**Method.** I compared each printed page's Kannada prose with the English section under `### Printed p. N` in `vol24/Rigveda_Samhita_Vol24_English_Translation.md`. The Kannada came from the per-window `vol24/work/wNNNN/kn_final.md`, cut at `<!-- printed N -->`, and I went back to `vol24/html/rig_24.md` where a doubt arose. On each page I compared all of the prose:

- Pratipadārtha
- Bhāvārtha
- printed English
- Anuvāda and Particulars
- Special Topics

I did not judge the Sanskrit blocks or the Gists made from the bhāṣya. Where the English has a NOTE at a faithfully kept OCR slip, I did not count it.

**How sample (b) was chosen.** Special Topics (ವಿಶೇಷವಿಷಯಗಳು) occur on these pages: 11, 13, 17, 86, 88, 89, 92, 93, 98, 103, 104, 115, 118, 128, 139, 147, 153, 155, 156, 158, 169, 173, 189, 227, 230, 236, 238, 242, 246, 295, 377, 422, 452, 468, 483, 516, 542, 549, 551, 555, 560, 563, 566, 635, 695, 700, 703, 729, 744, 754, 766, 768, 769, 771, 781, 786 and 789. From these I took eight pages that are at least 10 apart and not on the excluded list: 11, 98, 139, 173, 246, 468, 566 and 754.

## Pages checked

| # | Printed p. | Sample | Content | Result |
|---|---|---|---|---|
| 1 | 45 | a | S. 23 Ṛk 1 Pratipadārtha, Bhāvārtha, English; Ṛk 2 start | OK |
| 2 | 110 | a | S. 25 Ṛk 4 end; Ṛk 5 Pratipadārtha | OK |
| 3 | 165 | a | S. 27 Ṛk 6 Bhāvārtha, English; Ṛk 7 Pratipadārtha | OK |
| 4 | 205 | a | S. 31 Ṛk 1 Pratipadārtha, Bhāvārtha, English | OK |
| 5 | 240 | a | S. 32 Ṛk 14 Bhāvārtha, English; Ṛk 15 | OK |
| 6 | 300 | a | S. 35 Ṛk 6 | OK |
| 7 | 345 | a | S. 38 Ṛk 9 | OK (NOTE at ಅಹ್ವೇನಾನೂ) |
| 8 | 400 | a | S. 43 Ṛk 4 Bhāvārtha, English; Ṛk 5 | OK (NOTE at ಕೇಶವ) |
| 9 | 435 | a | S. 43 Ṛk 12 | OK (NOTE at ತನ್ನಂ) |
| 10 | 500 | a | S. 46 Ṛk 9 Bhāvārtha, English; Ṛk 10 Pratipadārtha | 1 MINOR (G1) |
| 11 | 545 | a | S. 47 Ṛk 17 | 1 MINOR (G2) |
| 12 | 585 | a | S. 52 Ṛk 4 English; Ṛk 5 Pratipadārtha | OK |
| 13 | 625 | a | S. 54 Particulars; Ṛk 1 Pratipadārtha | 1 MINOR (G3) |
| 14 | 660 | a | S. 59 Ṛk 3 Pratipadārtha (crosses 659/660), Bhāvārtha, English | OK |
| 15 | 705 | a | S. 61 Ṛk 15 Pratipadārtha (crosses 704/705), Bhāvārtha, English; Ṛk 16 | OK |
| 16 | 745 | a | S. 64 Ṛk 11 | OK |
| 17 | 11 | b | S. 21 Ṛk 8 Bhāvārtha, English + Special Topics (samasmin, Yāska, four Ṛk refs) | 1 MINOR (G4) |
| 18 | 98 | b | S. 24 Ṛk 24 + Special Topics (paripadām iva) | 1 MINOR (G5) |
| 19 | 139 | b | S. 26 Ṛk 8 + Special Topics (pratīvyam) | OK |
| 20 | 173 | b | S. 27 Ṛk 13 + Special Topics (Ā. 7-12) | OK |
| 21 | 246 | b | S. 32 Ṛk 21 + Special Topics (Soma purchase, Kṛ. Saṃ. 6-1-10) | 1 MINOR (G6) |
| 22 | 468 | b | S. 45 Ṛk 20 + Special Topics (rambha, Ni. 3-5) | 1 MINOR (G7) |
| 23 | 566 | b | S. 49 (Vālakhilya 1) Ṛk 10 + Special Topics (Ā. 3-7) | **1 ERROR (G8)** |
| 24 | 754 | b | S. 65 Ṛk 8 Special Topics (Ā. 5-5); Ṛk 9 | 1 MINOR (G9) |

## Findings

| # | Page | Source (Kannada) | English as it stands | Class | Fix |
|---|---|---|---|---|---|
| G8 | 566 | Special Topics: "…ಆಶ್ವಲಾಯನಶೌತಸೂತ್ರದ-ತ್ವಂ ನಃ ಸೋಮ ವಿಶ್ವತೋ ವಯೋಧಾ ಯಾ ತೇ ಧಾಮಾನಿ ದಿವಿ ಯಾ ಪೃಥಿವ್ಯಾಂ ಎಂಬ ಸೂತ್ರದಿಂದ (ಆ. ೩-೭)" | "…explained by the sutra of the Āśvalāyana-Śrautasūtra, the words या ते धामानि दिवि या पृथिव्यां (*yā te dhāmāni divi yā pṛthivyāṃ*) (Ā. 3-7)." (line 25909) | ERROR (quotation cut short; it drops the first pratīka, the one that names this very Ṛk) | Quote the whole sūtra, `त्वं नः सोम विश्वतो वयोधा या ते धामानि दिवि या पृथिव्यां`, copied from kn.md in ⟦ ⟧, and drop "the words". |
| G1 | 500 | Bhāvārtha: "…ಅದನ್ನು ಹೊಂದಿರುವ ನೀನು ನಮ್ಮ ಯಜ್ಞಗಳಿಗೆ ದಯಮಾಡು" (please come to our sacrifices) | "be gracious to our sacrifices" (line 22880); वरिवस्य is also given as "be gracious" (l. 22915), though the gloss "ಪುರಾ—ಹಿಂದೆಲ್ಲಾ ಬಂದೆಯೋ ಹಾಗೆ" shows that coming is meant | MINOR (term) | Change to "kindly come to our sacrifices", and in the वरिवस्य line to "kindly come". |
| G2 | 545 | Pratipadārtha: "(ಎಲೈ ದೇವತೆಗಳೇ) ವಃ—ನಿಮ್ಮ" | "वः (*vaḥ*)—your" (line 24984); the vocative "(O gods)" is dropped | MINOR (omission of a phrase) | Change to "- (O gods) वः (*vaḥ*)—your". |
| G3 | 625 | Particulars head: "ಸೂಕ್ತ—೫೪ / (ವಾಲವಿಲ್ಯಸೂಕ್ತ-೬)", an OCR slip for ವಾಲಖಿಲ್ಯಸೂಕ್ತ | The Particulars (line 28495) give no "(Vālakhilya Sūkta 6)". The heading at line 28480 is only "Sūkta 54 (Maṇḍala 8)". | MINOR (omission of the sub-head) | Add "(Vālakhilya Sūkta 6)" to the Particulars, with a NOTE on the source spelling. |
| G4 | 11 | Special Topics: "ಇಲ್ಲಿ ಸಮಸ್ಯೆ ಎಂದರೆ ಸರ್ವಸ್ಯ ಎಂದರ್ಥವು" | "Here samasyai means "of all"" (line 472) | MINOR (word form not in the source; the gloss is "sarvasya") | Change to "Here samasye means sarvasya, "of all"". |
| G5 | 98 | Bhāvārtha: "ಪ್ರತಿದಿನವೂ ಬೆಳಗೆದ್ದು ನಾನಾದಿಕ್ಕುಗಳಿಗೆ ಓಡುವ ಪಕ್ಷಿಗಳ ಚಲನವನ್ನು ಆದಿತ್ಯನು ತಿಳಿಯುವಂತೆ" (birds that rise each morning and run in all directions) | "as the sun knows every day, on rising, the movements of the birds…" (line 4419); the rising is given to the sun | MINOR (attribution) | Change to "as the sun knows the movements of the birds that rise every morning and run to the various quarters". |
| G6 | 246 | Special Topics: "ಬಹು ಕ್ರಮಪಟ್ಟ [=ಶ್ರಮಪಟ್ಟು] ಅವುಗಳನ್ನು ದೂರಪ್ರದೇಶಗಳಿಂದ ತಂದವರಿಂದ ಕೊಂಡುಕೊಂಡು" (buy them from those who brought them, with great labour, from distant regions) | "to buy them, at great cost, from those who have brought them from distant regions" (line 11102) | MINOR (sense: the source speaks of the bringers' labour, not of the price) | Change to "to buy them from those who have brought them with great labour from distant regions", and add a NOTE on the OCR "ಕ್ರಮಪಟ್ಟ". |
| G7 | 468 | Pratipadārtha: "ರಂಭಂ ನೆ—ಕೋಲನ್ನು ಆಶ್ರಯಿಸುವಂತೆ । (ವಯಂ—ನಾವು) । ತ್ವಾ—ನಿನ್ನನ್ನು" | The bracketed entry "(वयं—we)" is missing between रंभं नॆ and त्वा (lines 21436–21437) | MINOR (omitted entry) | Add "- (वयं (*vayaṃ*)—we)". |
| G9 | 754 | Special Topics: "…ಎಂಬ ಸೂತ್ರದಿಂದ (ಆ. ೫-೫)" | "(Ā. Sū. 5-5)" (line 34314); "Sū." is added, while elsewhere the English gives "Ā. 7-12" or "Ā. 3-7" | MINOR (reference form changed) | Change to "(Ā. 5-5)". |

**Checked and found faithful.** I checked:

- **Numbers:** the Particulars of S. 54 (varga 24, 25; 8 Ṛks; deity 1, 2, 5-8 Indra; 3, 4 Viśve Devāḥ) and the references Ṛ. Saṃ. 8-75-9, 8-21-8, 5-24-3, 8-39-1 to 10, Ā. 7-12, Ā. 3-7 and Kṛ. Saṃ. 6 1-10-1, 2. The last is kept as supplied, with a NOTE.
- **Names:** Kṛśa, Saptavāṇī, Ārjīkīya, Suṣomā, Śaryaṇāvat, Trita Āptya and Mātariśvā Kāṇva.
- **Negations:** pp. 240 ("there is no one who controls… no one says he does not give") and 754 ("not going to them").

Sentences that cross a page break (659/660, 704/705, 172/173, 565/566) are kept whole on the page where they begin or end, and none was misplaced. On these 24 pages I found no line of Kannada prose turned into Devanagari or Latin inside a quotation; the ⟦ ⟧ spans end where the source quotation ends. On p. 566 the supplied stray line `~v~v~v~` is rightly not translated.

## Totals

- Pages checked: **24** (16 fixed pages plus 8 Special-topics pages)
- ERRORs: **1** (G8: a quotation cut short on p. 566)
- MINORs: **8** (G1–G7, G9)
- Pages with no finding: **15**
