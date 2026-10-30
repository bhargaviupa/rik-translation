# w5e state (Vol 5 Pariśiṣṭa bare-? reference pass, pp. 626–708, worker w5e)

Branch: claude/pass2-vol5-pari2. Log: vol5/review/edits_w5e.txt. Tools as w5d (refs_w5d.py, parens_w5d.py, ltile_w5c.py; scipy needed: pip install scipy).
Better-scan map (checked from headers): p. 626 = PDF 646, 627 = 647, 628 = 644, 629 = 645, 630 = 642, 631 = 643; from p. 632 on PDF = p. + 16 (checked at 633, 660, 690, 708).
Glyphs: bold "2" with a straight base and loop at top = ೨ (2); rounded, ఒ-like foot = ೭ (7) (consistent with p. 636 4-27-1, 9-51-2, 9-86-27); ಲ/ಅ-like = ೮; ε/ಕ-like with tail = ೯; ಜ-like = ೫; hook top-left = ೬.

Done through: p. 636 (check pages: p626-629, p630-631, p632-635).
Next page: p. 637 (PDF 653).
Open items:
- p. 634: 9-66-16 and 17 [?] (last number unsure); p. 635: print has "೯-೮೭-೯-೯;೯೬-೨" written 9-87-9; 9-96-2 [?]; p. 635 weapons printed "(೯; ೯೬-೧೬)" written 9-96-16.
- Workflow: refs_w5d.py PAGE (list); parens_w5d.py PDF PREFIX 550 (montage); ltile_w5c.py PDF OUT A B 200 1 (strips for structure: the file often has a ref missing/extra vs the print); z_w5d.sh PDF "line:f0:f1" 500 (fractions); apply with refs_w5d.py PAGE apply MAP.json (+ "_text"); log lines prefixed with two spaces, added/merged refs written by hand.
- Check pages for pp. 626-631 need PDF overrides: /tmp wrapper patched SECT with {626:646,...,631:643}; from p. 632 the plain build_verify_v5.py works.
- p. 630: Kā. Śrau. Sū. 9-5-12 [?]; 9-7-4 [?] (last digits unsure); p. 631: Vai. Saṃ. 16-9 [?] (16-9 or 1-6-9).
- The file's "(PDF N)" headers for pp. 626–631 give old-scan numbers; build_verify crops for those pages may come from the wrong better-scan page.
- File first digits are often wrong (e.g. 9 printed 8 or 5); changed to the print. Where the file's ref structure differed from the print (p. 627: an extra ref, a missing one, Kā./Śat. Brā.), the passage was set to the print and logged as one line.
