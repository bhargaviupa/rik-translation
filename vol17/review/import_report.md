# Vol 17: import report (rv import)

English file cut into 3390 pieces; units now 3390 (0 summary units added beside their bhāṣya).

## Proof 1: every English paragraph placed once
- paragraphs of English text in the file: 10967
- placed in a unit: 10811
- not placed (their piece has no unit): 156
- placed more than once: 156
- parts that the English has and the Kannada file has no label for (units without Kannada; a fault of the supplied text or of its labels): 0
- units that should have English and have none: 0

## Proof 2: the Sanskrit of the English file equals the source (verse, Pada, bhāṣya)
- different from the source: 4
- equal to the source, letter for letter: 1316
- no block in the English file: 3
- units that differ: 17.3.053.05.bhashya, 17.3.062.08.pada, 17.4.002.16.pada, 17.4.012.06.pada

## Repairs applied from data/import_fixes.json
- moved 17.4.001.02.loose -> 17.4.001.01.vishesha (append): two paragraphs of the Special Topics of Ṛk 1 (Pracetasam, Viśvaṃ janata) stood after the heading of Ṛk 2 in the old file
- moved 17.4.014.05.vishesha -> 17.4.015.00.intro (prepend): the introduction of Sūkta 15 (the rite Paryagnikaraṇa) stood under the Special Topics of 4.14.5 in the old file; in the edition it opens Sūkta 15
- set aside (kept in the data, not printed) 17.3.056.02.grammar: a list drawn from the grammatical tail of the bhāṣya; the edition has no grammar section here and the bhāṣya is printed in full
- set aside (kept in the data, not printed) 17.3.057.04.grammar: as above
- set aside (kept in the data, not printed) 17.3.057.05.grammar: as above
- English supplied for 17.4.017.07.pratipada (16 entries): the old file had no word meanings for this Ṛk; supplied Nov 13 2026 from the Kannada, to be read a second time with the rest

## Questions for the editor
- NOTE marks in the English file: 471; rows in review/notes.tsv: 471; attached to units: 471
- decided (data/decisions.tsv): 88; still open: 383
- abbreviations replaced by the form of the one list: 76 (Bhā. U. 12, Ṛgve. 11, Atha. Saṃ. 10, Ṛg. 7, I. Ā. 6, Kṛ. Saṃ. 5, Trai. U. 3, Śai. Saṃ. 3, Manu. 2, Ma. Saṃ. 2, Śai. Brā. 2, Mu. Saṃ. 2, Kṛ. U. 2, Trai. Ā. 2, I. Brā. 2, Ā. Gṛ. 2, I. U. 2, Kṛ. Ā. 1)
- paragraphs changed to carry out a decision (data/import_fixes.json, replace_en): 47

## Left behind on purpose
- "(continued)" headings dropped: 20
- NOTE marks numbered in file order: 471
- Sanskrit blocks in the English file: 1533
- page headings (not taken over: pages come from the Kannada side): 1007
- transliteration lines left behind (made again at print time): 2157
