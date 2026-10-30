# w5e state (Vol 5 Pariśiṣṭa bare-? reference pass, pp. 626–708, worker w5e)

Branch: claude/pass2-vol5-pari2. Log: vol5/review/edits_w5e.txt. Tools as w5d (refs_w5d.py, parens_w5d.py, ltile_w5c.py; scipy needed: pip install scipy).
Better-scan map (checked from headers): p. 626 = PDF 646, 627 = 647, 628 = 644, 629 = 645, 630 = 642, 631 = 643; from p. 632 on PDF = p. + 16 (checked at 633, 660, 690, 708).
Glyphs: loop-footed 2 = ೨, flat-footed (ఒ-like) = ೭; ಲ/ಅ-like = ೮; ε/ಕ-like with tail = ೯; ಜ-like = ೫; hook top-left = ೬.

Done through: p. 629.
Next page: p. 630 (PDF 642): 48 refs, many in [ ] in the file; 4 already filled (9-31-4, 9-102-12, 4-33-11, 3-?-1/8-?-1 partly); check the print structure with ltile_w5c.py strips (200 dpi) before applying.
Open items:
- Workflow: refs_w5d.py PAGE (list); parens_w5d.py PDF PREFIX 550 (montage); ltile_w5c.py PDF OUT A B 200 1 (strips for structure: the file often has a ref missing/extra vs the print); z_w5d.sh PDF "line:f0:f1" 500 (fractions); apply with refs_w5d.py PAGE apply MAP.json (+ "_text"); log lines prefixed with two spaces, added/merged refs written by hand.
- Check pages not yet built (none run yet; run build_verify_v5.py for 626-6xx at the next batch end).
- The file's "(PDF N)" headers for pp. 626–631 give old-scan numbers; build_verify crops for those pages may come from the wrong better-scan page.
- File first digits are often wrong (e.g. 9 printed 8 or 5); changed to the print. Where the file's ref structure differed from the print (p. 627: an extra ref, a missing one, Kā./Śat. Brā.), the passage was set to the print and logged as one line.
