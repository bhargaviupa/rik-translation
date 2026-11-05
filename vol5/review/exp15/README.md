# 15-page experiment: blind scan reading vs the HTML (Vol 5, Nov 5 2026)
Pages (printed, chosen at random, seed 20261105): 5 14 18 21 23 25 40 41 42 54 56 60 76 79 82.
Three Sonnet agents read the scan (better scan, 300 dpi strips, no zoom) blind, without the HTML or the md; `printedN.txt` are their texts.
`python3 tools/rv/compare_html_scan.py --chars --html vol5/html/rig_5_1.html --dir vol5/review/exp15 --pages ... --sheet ...` compares character by character
(spaces, markup, punctuation, Latin letters and digits removed). `all_differences.tsv` lists every differing spot; `sample40_for_adjudication.tsv` is a random 40 of them for a human verdict.
A difference is an error in the HTML or in the scan reading (or both): the verdict column decides.
