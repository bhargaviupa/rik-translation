# Build status of the review PDFs

*Written by `publish/build_all.py`; do not edit by hand. Every builder runs the same print step (`publish/printfix.py`, `publish/style_footer.css`; rules: `docs/REQUIREMENTS.md` A4 "Print rules", B4.6, D19). "Check" is `publish/pdf_check.py`; the counts are lines of the PDF that still show a mark or remark (0 wanted for a release).*

| Vol | PDF | Built | Pages | Check | Still printed | Print step and clean-up |
|---|---|---|---|---|---|---|
| 1 | vol1_full.pdf | 26 Nov 2026 09:40 UTC | 1033 | passes | [?] 39; [sic] 15; as printed 29; as supplied 0; NOTE 0; GLOSS 0; session words 7 | page headings out of the body 0; bold sentences and words set plain 1842; label paragraphs 244; paragraphs joined over a page turn 70; contents tables 4; lists continued 3; two-line headings 49; transliterations on their own line 1169; English of quotations not printed 811; Kannada-script places 6; wide tables fitted 23 |
| 1 | vol1_full_Kan.pdf | 26 Nov 2026 09:40 UTC | 766 | passes | [?] 1; [sic] 0; as printed 0; as supplied 2; NOTE 0; GLOSS 0; session words 0 |  |
| 21 | vol21_full_Eng.pdf | 26 Nov 2026 02:55 UTC | 1586 | passes | [?] 0; [sic] 0; as printed 1; as supplied 1; NOTE 348; GLOSS 164; session words 0 | page headings out of the body 0; bold sentences set plain 9; label paragraphs 23; paragraphs joined over a page turn 50; contents tables 1; lists continued 0; two-line headings 0; transliterations on their own line 2937 |
| 21 | vol21_full_Kan.pdf | 26 Nov 2026 02:55 UTC | 978 | passes | [?] 0; [sic] 0; as printed 0; as supplied 25; NOTE 1; GLOSS 0; session words 0 |  |
