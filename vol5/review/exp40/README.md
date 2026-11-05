# 40-page extension of the HTML-vs-scan experiment (Vol 5, Nov 5 2026)
Pages (printed, random, seed 20261106): 2 3 9 10 11 13 15 17 24 28 33 38 50 52 53 68 70 72 78 81 | 86 95 103 111 115 116 125 129 132 139 147 150 152 155 159 160 173 174 177 179
Eight Sonnet agents read the scan blind (300 dpi strips, no zoom). Pages up to 84 are compared with `vol5/html/rig_5_1.html`, pages 85+ with `vol5/html/rig_5_2.md`:
`python3 tools/rv/compare_html_scan.py --chars --html "vol5/html/rig_5_1.html@1-84" "vol5/html/rig_5_2.md@85-184" --dir vol5/review/exp40 --pages ... --sheet ...`
**p. 179 is excluded**: the markdown has no running head for p. 180, so its "page 179" holds two pages. `all_differences.tsv` = every differing spot of the other 39 pages;
`sample40_for_adjudication.tsv` = 40 random spots for a human verdict (HTML / SCAN / BOTH / NEITHER).
