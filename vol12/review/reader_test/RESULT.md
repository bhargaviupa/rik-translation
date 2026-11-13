# Second-reader measurement on Vol 12 — result (Nov 13 2026)

**Test:** the 72 pages of the Vol 12 QA sample, as the text stood before the QA repairs (commit `b6d01a3`). On them an Opus QA of Nov 10 2026 had found 18 errors (`known_errors.tsv`). Fresh agents read each page against the Kannada with the instruction in `INSTRUCTION.md`, twelve pages per agent, without being told what was known. Their findings are in `out/sonnet/` and `out/haiku/`. Scoring: a known error counts as found when the reader reported it on its page, whatever severity the reader gave it. Scored by the dispatcher by reading the findings; no API money was spent.

## Score

| Reader | Known errors found | Pages with nothing reported | Findings in all |
|---|---|---|---|
| Sonnet | **10 of 18** | 37 of 72 | 12 graded ERROR, 37 graded MINOR |
| Haiku | **7 of 18** | — | — |

| No. | Page | Known error | Sonnet | Haiku |
|---|---|---|---|---|
| 1 | 371 | quotation cut short | found | found |
| 2 | 415 | adjunct given to the Lord instead of the individual self | missed | missed |
| 3 | 652 | English translation of a quotation added | found | found |
| 4 | 708 | who helped whom reversed | found | found |
| 5 | 653 | "iti ca brāhmaṇaṃ" cut from the quotation | missed | missed |
| 6 | 653 | three added translations | found | found |
| 7 | 663 | "both worlds life-giving to each other" | found | missed |
| 8 | 51 | Gist: Heaven and Earth measure the rays (reverse of Sāyaṇa) | missed | missed |
| 9 | 52 | Sanskrit gloss given only in English | missed | missed |
| 10 | 259 | added translations of Sanskrit glosses | found | missed |
| 11 | 274 | sentence about the root "bhur" (subject is the bird) | missed | missed |
| 12 | 297 | "Lord of the universal Self" for "lordship of the universal Self" | missed | missed |
| 13 | 341 | added translation | found | found |
| 14 | 359 | anudātta for ādyudātta | missed | missed |
| 15 | 359 | "Saura root" for sautra root | found | found |
| 16 | 382 | added translation | missed | missed |
| 17 | 400 | added translation before the Kannada's own gloss | found | missed |
| 18 | 414 | headword omitted | found | found |

**Cost of the run:** 1,942,024 agent tokens for the twelve readers together (72 pages read twice, once by each model): about 13,500 tokens for one reading of one page, the reader's instruction and tool use included. No API money.

## What it shows
- **By kind (Sonnet):** additions 5 of 6 found; omissions 2 of 4; meaning and term 3 of 8. The reader is good at what can be seen by setting the two texts side by side (something added, something cut, roles plainly reversed) and weak at errors that need the Sanskrit or the grammar to be understood (nos. 2, 8, 11, 12, 14).
- **What it reports is mostly right.** Of Sonnet's 12 findings graded ERROR, 8 are known errors, 3 are faults the QA had also listed (as minor: pp. 31, 170, 285), and 1 is a false alarm caused by reading one page alone (p. 442, a sentence that runs on to the next page).
- **Grading is unreliable.** Four of the ten known errors that Sonnet found it graded MINOR. The reader's own ERROR/MINOR label cannot decide what is repaired.
- **Haiku is not good enough** as the reader: 7 of the 18 known errors, and of the eight meaning and term errors it found two.
- **The limit of this test:** the 18 known errors are the ones an Opus reader found. How many errors Opus itself misses is not known, so 10 of 18 is Sonnet's score against Opus, not against the truth.

## Consequences for the design (DESIGN §5.4, §8.2)
1. A second reading by Sonnet would remove roughly half of the errors of the kind found so far, and most of the additions and cuts. It does not by itself meet the release standard "no error of meaning left unrepaired".
2. Every finding is acted on, not only those graded ERROR.
3. The reader must see the neighbouring pages (or whole units, as the design has it), to avoid the page-boundary false alarms.
4. For meaning errors a stronger reader is needed: Opus as the reader, at least for the Summary of the bhāṣya, the Viśeṣa-viṣaya and the grammar, where five of the eight meaning and term errors sat; and the scholar's sample.
5. Haiku is not used as a reader.
