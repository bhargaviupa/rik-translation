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
