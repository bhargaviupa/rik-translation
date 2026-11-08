# Vol 15 printed contents — check against the clean scan (user's front-matter PDF, Nov 8 2026)
- Scan pages iii–vi (items up to p. 488): all 83 page numbers equal the supplied md (compared item by item).
- Scan pages vii–ix are not in the user's PDF; their numbers are as in the supplied md. `contents_parse.py --check` flags one:
  md line 318 "ಜಾತವೇದಶ್ಯಬ್ದ ವಿವರಣೆ 443" (page goes down after 538). Set to **543** in `vol15/contents_fixes.json`: it fits the sequence
  (538 < 543 < 549) and the Jātavedas discussion is on printed pp. 541–544 of the translation (p. 443 has none). **User to confirm on the scan.**
