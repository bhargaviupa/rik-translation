# Vol 15 printed contents — check against the user's complete front-matter scan (Nov 8 2026, 15 pages, contents iii–ix)
- All 159 page numbers of the typeset contents were compared item by item with the scan (pages iii–ix): identical.
- One repair was needed in the md text: line 393 "ಮಾತರಿಶ್ವಾ ಎಂಬ ಶಬ್ದದ ನಿರ್ವಚನ" lost its number (766) in the machine reading and had been joined to the next line;
  `vol15/contents_fixes.json` restores it as its own item (page 766, as printed).
- "ಜಾತವೇದಶ್ಯಬ್ದ ವಿವರಣೆ **443**" (md line 318) is **as printed** on p. vii of the original (the sequence reads 538, 443, 549; the Jātavedas
  discussion is on pp. 541–544, so 543 was probably meant). Kept as printed, not corrected; `contents_parse.py --check` flags it.
  (An earlier version of this build set 543 before the full scan was available: reverted.)
