# Vol 14 pp. 501–766: html-based vs scan-based translation (word-level notes)

Experiment (branch `claude/vol14-exp`, Nov 5–9 2026): printed pp. 501–766 were translated a second time from the user's machine-read text (`vol14/html/rig_14_2_figs.html`) by fresh Sonnet agents, 3-page windows (89 windows), without access to the scan-based translation. The result is the html-based text in `vol14/Rigveda_Samhita_Vol14_English_Translation.md`; the scan-based text is `vol14/Rigveda_Samhita_Vol14_scan_English_Translation.md`.

## Files here
| File | Content |
|---|---|
| `compare_501-766.xlsx` | word-by-word differences, pp. 501–766. Sheets: Summary, Devanagari (Sanskrit words, accents ignored: page, type, scan-based word, html-based word, context, empty verdict column), English (prose words, same columns), Numerals (reference numerals present only in one version), Pages (per-page counts) |
| `compare_501-533.xlsx` | the same for the first 33 pages (first run, pp. 501–533) |
| `side_by_side_pp501-533.html`, `A_scan_based_pp501-533.md`, `B_supplied_text_pp501-533.md` | the two translations of pp. 501–533 side by side and separately, for reading |
| `dispatcher_notes.md` | deviations found while dispatching the 89 windows (colon-joined references, figure readings, added Ṛk numbers, doubled marks fixed by hand, …) |
| `doubts.tsv`, `accent_report.tsv` | `[?]` readings and unmatched Saṃhitā lines of the html-based pp. 501–766 |

## Totals, pp. 501–766 (264 pages; run of Nov 7 2026)
- Sanskrit (Devanagari) words: scan-based 19,085, html-based 17,173. Differing: 6,564 (34.4 %) in 2,653 difference events (2,092 replacements, 426 only in the scan-based text, 135 only in the html-based text).
- English prose words: 64,804 vs 65,157. Differing: 42,374 (65.4 %) in 10,177 events. This number mostly measures different wording of the same Kannada, not errors.
- `[?]` marks: 860 (scan-based) vs 21 (html-based).
- Reference numerals that differ: 408 pages carry at least one difference.
- Kannada: the scan-based Vol 14 has no Kannada text for these pages, so Kannada-level differences show only through the Sanskrit blocks.

## Kinds of Sanskrit differences seen in a sample (pp. 501–533, 246 events)
one-letter differences 91, two- or three-letter 47, only in the scan-based text 66 (mostly fuller bhāṣya tails), same letters but hyphen/space only 22, larger differences 10, only in the html-based text 10. Who is right is not decided: the verdict columns are empty and need the scan or the user.

## Tools
`tools/rv/compare_words_xlsx.py OLD.md NEW.md FIRST LAST OUT.xlsx` (the workbook above) and `tools/rv/compare_translations.py OLD.md NEW.md FIRST LAST` (page-level report). Both only read the two files. The experiment's brief and prompt (`vol14/EXPERIMENT_*.md`) and the stand-alone "Vol 14b" file remain on branch `claude/vol14-exp`.
