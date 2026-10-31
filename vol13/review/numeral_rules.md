# Vol 13 numeral and glyph notes (from the zoom-fix passes, Oct 31 2026)

Source: `vol13/review/zoomfix_a.json` (per-entry evidence). Read these before re-reading small-type numbers or Sanskrit in the Kannada print.

## 1. Digits 2, 3, 7 look alike (calibrated against page headers)
Calibrate on the running header (`ಅ. ೨೩. ಸೂ. ೧೭೪` = Anuvāka 23, Sūkta 174), which has a known 2, 3, 7 and 4.
- 2 (೨): round glyph with an open loop at the top.
- 3 (೩): hooked glyph, looks like "ಇ" or "ಖ" (curled, flat-footed). It is the one most often misread as 2.
- 7 (೭): flat-bottomed, looks like "ಒ".
- 4 = like ಳ; 5 = like ಣ/ಜ; 8 = like ಲ/ಅ; 9 = like ಕ.
- Several Nirukta refs of the form "?-9" are 3-9, not 2-9 (battle, wealth, food, strength names). Pass A fixed pp. 280, 281, 306, 309, 332, 340, 349, 370, 374.
- About 13 `(Ni. 2-9)` refs from earlier passes are NOT re-checked and may be 3-9. Grep `Ni\. 2-9` in the Vol 13 md.
- The first digit of a ref may be 2, 3 or 7: compare it with the header glyphs in the same crop before writing it.

## 2. Hooked ma and ya are not u
In this typeface plain *ma* and *ya* are drawn with a hook that looks like the ು sign.
- Examples: ಮುರುತಃ = marutaḥ, ಯಜಮಾನಾಯು = yajamānāya, ಅಸಾಮು = asāma, ಸ್ತೋಮು = stoma.
- A wrong "asāmu" and "stomu" were written and reverted on pp. 294 and 307.
- Check any reading that depends on an "ು" next to ಮ or ಯ.
- A real long ā or u is a separate, clearly different mark.

## 3. Pada compound marker
Inside Pada lines a small subscript stroke ("್ಯ"-like) is the compound-division mark (ऽ): ಅರ್ಕ್ಯ್ಸಾತೌ = arka-sātau, ಸಹ್ಯ್ವಾನ್ = saha-vān. It is not ya.

## 4. Practical method
- View a whole column at about 190–230 dpi: bold Sanskrit and the refs are mostly legible and can be compared line by line with the md.
- Zoom (550–700 dpi) only for a ref or a single word.
- Use whole-page fractions for the crop. On tall images (about 2000 px) the displayed coordinates are unreliable, so use shorter bands.
- Where the print gives no reference number (e.g. after "kṣipra names", "itaś ca", "khari ca"), write "(no reference is printed here)", never a number from memory.
- Keep [?] on small-type grammar numerals (Pāṇini, Uṇādi) unless a 450 dpi zoom is unambiguous.

## 5. Added during the part-3 batch (entries 99–191, printed ~380–471)
- Re-read this file after any context compaction. The same rules also stand in CLAUDE.md, item 3.
- PDF page = printed page + 20 in this volume (printed 380 = pdf 400).
- The user supplied lists of numerals "identified" from the PDF (machine-read). They are useful as hints: they agreed with the hooked-3 rule on pp. 20, 33, 35, 39, 43 (e.g. Ni 3-9, 3-11, 3-13 where the file had 2-9, 2-11, 3-3). They also omit references and make errors, so every value must still be confirmed on the page before it is written. A reading is never taken from the list alone.
- Where a Nirukta ref reads "?-9", the first digit is the hooked 3 (3-9) for the lists of names of strength, battle, wealth, food, etc. (The pre-existing `(Ni. 2-9)` in the early part of the file is probably 3-9.)
- When the print puts no number after a Sanskrit sūtra name or citation, write "(no reference is printed here)".
