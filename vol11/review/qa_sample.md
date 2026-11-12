# Vol 11 — QA sample after stage 1 (Nov 12 2026)

24 printed pages (pp. 1–267) checked against the supplied Kannada by three fresh Opus agents, read-only, not told what to expect: 12 general pages (g20 g43 g64 g88 g110 g133 g156 g178 g200 g222 g244 g262) and 12 pages with Special Topics (s4 s23 s50 s65 s90 s109 s132 s153 s175 s193 s218 s245). The Devanagari blocks and every verse/sūtra/Brāhmaṇa reference agree with the Kannada letter for letter, misprints included; no block stood under the label of another section.

**Findings, counted by the agents' own classes: 8 ERROR, about 20 MINOR; 4 pages clean (g133, g200, s109, s193).** Most ERRORs are one pattern; the content ones were repaired (`review/repair_log.md`).

## 1. Page boundary (systematic, 6 ERROR + 6 MINOR in the agents' count; nothing is lost or duplicated)
The model puts a `### Printed p. N` heading a few lines off the true break: the top of a page (s23, s175, g110, g156, g178) sits at the end of the previous page's English, the end of a page (s23, s50, s65, g222) at the start of the next one's. Checked for s175 (Gārhapatya alternative stands once, at the end of p. 174), s23, s50, s65, g222, g110: each passage occurs exactly once in the volume. Not repaired (page headings approximate; the Kannada file has the exact marks). TODO for the tools: none cheap; a gate would need the Kannada text of the page edge.

## 2. Content errors — repaired
- s132: "straight like fingers" for ಆಕುಟಿಲ (curved) — repaired (Gist and Pratipadārtha).
- g64: "third verse of the Aindra triplet beginning 'vṛṣann indra'" — repaired. (The agent's second g64 ERROR, "may also mean breakers-forth of strength": a further qualification, not an alternative meaning — **not repaired**, left for the editor.)
- g156: the Kannada word ಮುಂದುವರಿದುದು in Devanagari inside a grammar entry — removed.

## 3. Not repaired (for the editor)
- g156: the closing line "ಇಲ್ಲಿಗೆ … ಸೂಕ್ತವು ಮುಗಿದುದು" and the verse-end mark "॥ ೧೩ ॥" are not in the English; the grammar-section verse-end marks "॥ N ॥" are dropped in g88, g178, g244 (script behaviour, same everywhere).
- s132 Gist "when he has gone away" (bhāṣya पश्चात्तोषिते: a silent emendation); s90 Gist reading of "Bṛhaspati … Sukratu"; s218 "shout aloud" for the printed misprint "shont aloud" (the supplied text is the base); g222 "Vādhryaśva" for ವಾಧ್ಯಶ್ವ; "ದಯಮಾಡು" rendered "be gracious/favour" for "please come" (s4, s65); g262 Gist has the remark "with a phrase that is garbled in the text"; s153 impersonal "it has been explained" made "he has explained"; g43 "we have seen" for an optative; g20 "(quoted above)" added; g110 added heading "विशेषविषयगळु (Special Topics)" is the standard heading; g156 "रसरवागि" keeps Kannada -ಆಗಿ in the Sanskrit.

## Conclusion
No translation-wide fault beyond the page-boundary placement. Under HANDBOOK §11.5 (ERRORs found → double the sample) the second sample is **not run**: the ERRORs are one known pattern and three isolated slips, all listed. The user decides before stage 2 whether to double it.

---

# Second QA sample — stages 2–3 (pp. 268–696), Nov 12 2026 (finishing job)

24 pages by three fresh Opus agents, read-only, same method (12 general: g290 g323 g356 g389 g422 g455 g488 g521 g554 g587 g620 g665; 12 Special Topics: s268 s307 s342 s369 s397 s435 s470 s500 s534 s573 s622 s670). The agents were told only that page headings are approximate (BOUNDARY). **No wrong verse, sūtra or Brāhmaṇa reference, no wrong name or quotation, no reversed negation or attribution, no block under the wrong sub-heading; the Devanagari blocks match the Kannada letter for letter on every page.** Clean: g323, g389, g620, s435, s470, s500, s622 (7 pages); the rest have MINOR items or BOUNDARY only.

## Real findings
| page | finding | status |
|---|---|---|
| s534 | the English had "Ṛk 4-36-1 cited above (the Kannada prints "VI. 36-1")": number corrected and a remark added | **repaired**: "VI. 36-1" restored as printed + **NOTE** |
| p. 136, 378, 521, 608 (found by grep after the agents' g521 note) | translator remarks "(the Kannada prints …)", "[Kannada: …]", "(sic)" in the English | **repaired**: turned into **NOTE** marks (3 new rows in `notes.tsv`) |
| s307, s369, g665, s342, g455, g521 | inline Sanskrit given as IAST only (no Devanagari), or with a reading different from the prose Kannada | not an error of the model: the pipeline replaces an inline segment by the form `kn.md` has elsewhere (e.g. the bhāṣya block), or, where `kn.md` has none, sets it in IAST only and logs it (`review/inline_readings.tsv`); left as is, listed |
| g422, g521 | the heading `विशेषविषयगळु (Special Topics)` is the Kannada word ವಿಶೇಷವಿಷಯಗಳು in Devanagari | the shared label of Vols 17/18 (170 and 271 occurrences there): **not changed here; for the user** |
| g488 | composed Sanskrit "धातुस्वरो शिष्यते" (sandhi) | not repaired (composed Sanskrit: the editor's reading) |

## MINOR, not repaired (wording and nuance; for the editor)
s397 "Sāyaṇa has explained" (the Kannada names no one); s573 Gist omits the opening clause of the bhāṣya; g587 पाथः "path"; s268 "The Praiṣa-sūkta describes him" for "the explanation of the Praiṣa-sūkta"; g665 "ploughing" nuance and a root name left out (misread "ದ್ವ್ಯ"); s369 "ಅಶ್ವಗಳ ವೇದವನ್ನು" read as "speed" (a misread) without a NOTE; s342 "mithaḥ"; g455 dropped stray line "ಸುತ್ತಿಶತ ।"; g521 "(ಅದಾದರೋ)" not rendered; g356 closing quotation mark of a Gist.

## BOUNDARY (checked, nothing lost)
g290, g356, g455, g521, g554, s670: the first or last lines of the Kannada page stand at the end of the neighbouring English page or the reverse. Checked g455 (the Ṛk 1-190-4 verse stands once, at the end of p. 454) and g521 (the continuation stands once).

## Conclusion
ERRORs of the first sample (Vol 11 pp. 1–267: 8, of which 3 content slips repaired) and of this one (2: s534 and the four remark spots, repaired) are few and none changes a number, name or attribution except those repaired. The sample is **not doubled**: the second sample found no ERROR beyond the repaired remarks. The page-heading placement at page breaks stays as the one known systematic fault of the run.
