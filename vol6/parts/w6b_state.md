# w6b part file — Vol 6 numeral/[?]/accent pass
Range: printed pp. 282–620 (Sūktas 71–80). Branch claude/pass2-vol6-b. Edits log vol6/review/edits_w6b.txt.
Done through: printed p. 308 (Sūkta 71 intro + Ṛks 71.1–71.5 complete; unit 1 = pp. 282–297, unit 2 = pp. 297–308).
Next unit: p. 309 (Rik 71.6 Saṃhitā, file line ~6251) to the end of Sūkta 71 (p. 332), then Sūkta 72 (p. 333).
Check pages built: Vol6_verify_p297-308.html (20 rows), Vol6_doubts_p297-308.html (5 doubts); vol6/review/html/Vol6_verify_p282-297.html (27 rows), Vol6_doubts_p282-297.html (11 doubts; json vol6/review/doubts_w6b_p282-297.json).
Helpers: vol6/tools/crop_w6b.py, stack_w6b.py (several crops of one page in one image — saves views), lines_w6b.py (line bands as text-block fractions; on some pages the block includes the running head as line 1).
Digit calibration (from the print): ೨ = loop at top-left (header "ಅ. ೧೨"); ೭ = loop at bottom-left (header "ಸೂ. ೭೧"); ೩ = ಖ-like (Ṛk number "|| ೩ ||", pluta ೩); ʒ-like = ೫.
NOTE: doubts_v6.py crops by WHOLE-PAGE fractions (its docstring says text block): write text-block fractions and convert with vol6/tools/tb2page_w6b.py (entries with "pagefrac": true kept). Unit-1 doubts page rebuilt with page fractions.
Scan notes: view.py textbox() cuts the right margin on some pages (283, 285, 286, 290): use x up to 1.07 or FULL=1. The source's Ni. numbers (e.g. 3-9 for fingers, strength and food) do not follow the usual Nighaṇṭu sections; recorded as printed. p. 291 running head prints Aṣṭaka "೨" (for 1).
tesseract + kan needed for build_verify_v6.py: apt-get install tesseract-ocr tesseract-ocr-kan.
Open items: the source prints Ni. 3-9 for the names of fingers, strength, food and going (pp. 285, 290, 295, 305, 306) — flagged once on the doubts page (p. 306); p. 305's Ni. numeral is cut off in the better scan and was read from the old scan; p. 297's Saṃhitā lies below view.py's text box (use FULL=1). doubts listed in the doubts page; p. 293 bhāṣya "Meaning" paraphrase not updated for the restored clause (re-translation not in scope).
