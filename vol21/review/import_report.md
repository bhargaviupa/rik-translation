# Vol 21: import report (rv import)

English file cut into 3337 pieces; units now 4676 (13 summary units added beside their bhāṣya).

## Proof 1: every English paragraph placed once
- paragraphs of English text in the file: 8641
- placed in a unit: 8257
- not placed (their piece has no unit): 384 in 1423 pieces: (6, 29, 1, 'bhashya'), (6, 29, 1, 'pada'), (6, 29, 1, 'samhita'), (6, 29, 2, 'bhashya'), (6, 29, 2, 'pada'), (6, 29, 2, 'samhita'), (6, 29, 3, 'bhashya'), (6, 29, 3, 'pada'), (6, 29, 3, 'samhita'), (6, 29, 4, 'bhashya'), (6, 29, 4, 'pada'), (6, 29, 4, 'samhita')
- placed more than once: 22
- parts that the English has and the Kannada file has no label for (units without Kannada; a fault of the supplied text or of its labels): 53: 21.6.075.06.english, 21.6.075.06.vishesha, 21.6.075.07.pratipada, 21.6.075.07.bhavartha, 21.6.075.07.english, 21.6.075.07.vishesha, 21.6.075.08.pratipada, 21.6.075.08.bhavartha, 21.6.075.08.english, 21.6.075.08.vishesha, 21.6.075.09.pratipada, 21.6.075.09.bhavartha, 21.6.075.09.english, 21.6.075.09.vishesha, 21.6.075.10.pratipada, 21.6.075.10.bhavartha, 21.6.075.10.english, 21.6.075.10.vishesha, 21.6.075.11.pratipada, 21.6.075.11.bhavartha, 21.6.075.11.english, 21.6.075.11.vishesha, 21.6.075.12.pratipada, 21.6.075.12.bhavartha, 21.6.075.12.english, 21.6.075.12.vishesha, 21.6.075.13.pratipada, 21.6.075.13.bhavartha, 21.6.075.13.english, 21.6.075.13.vishesha, 21.6.075.14.pratipada, 21.6.075.14.bhavartha, 21.6.075.14.english, 21.6.075.14.vishesha, 21.6.075.15.loose, 21.6.075.15.pratipada, 21.6.075.15.bhavartha, 21.6.075.15.english, 21.6.075.15.vishesha, 21.6.075.16.pratipada, 21.6.075.16.bhavartha, 21.6.075.16.english, 21.6.075.17.pratipada, 21.6.075.17.bhavartha, 21.6.075.17.english, 21.6.075.17.vishesha, 21.6.075.18.pratipada, 21.6.075.18.bhavartha, 21.6.075.18.english, 21.6.075.19.pratipada, 21.6.075.19.bhavartha, 21.6.075.19.english, 21.6.075.19.vishesha
- units that should have English and have none: 931: 21.front.pratipada, 21.front.bhavartha, 21.front.pratipada, 21.front.bhavartha, 21.front.pratipada, 21.front.bhavartha, 21.front.pratipada, 21.front.bhavartha, 21.front.pratipada, 21.front.bhavartha, 21.front.pratipada, 21.front.bhavartha, 21.front.pratipada, 21.front.bhavartha, 21.front.pratipada

## Proof 2: the Sanskrit of the English file equals the source (verse, Pada, bhāṣya)
- different from the source: 2
- no block in the English file: 1384
- units that differ: 21.6.030.03.samhita, 21.6.065.03.samhita

## Repairs applied from data/import_fixes.json
- none

## Questions for the editor
- NOTE marks in the English file: 258; rows in review/notes.tsv: 258; attached to units: 209
- decided (data/decisions.tsv): 0; still open: 209
- abbreviations replaced by the form of the one list: 26 (Ṛgve. 15, Ā. Gṛ. 4, Ya. Saṃ. 2, Śai. Saṃ. 1, Ma. 1, Ṛ. 1, Trai. Ā. 1, Ma. Saṃ. 1)
- paragraphs changed to carry out a decision (data/import_fixes.json, replace_en): 0; reference repairs by substring (replace_sub): 0

## Left behind on purpose
- NOTE marks numbered in file order: 258
- Sanskrit blocks in the English file: 1497
- page headings (not taken over: pages come from the Kannada side): 608
