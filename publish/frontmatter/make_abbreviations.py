#!/usr/bin/env python3
"""Write pages/10_abbreviations.html from the one list rv/references.tsv (REQUIREMENTS B3.7, C10): the legend printed in every volume, the same in all.
Rows with status 'legend' (the edition's own legend) and 'extra' (works cited in the volumes but not in the edition's legend) are printed, in the list's
order; 'mistake' rows (known misreadings) are never printed. Columns: the abbreviation used in this translation | the form of the original's print in
Devanagari (made from the Kannada form by script; nobody types it) | the work. A row with two forms ("X or Y", B3.6 forbids it) is printed with the
first form only. Run:  python3 publish/frontmatter/make_abbreviations.py  (needs indic-transliteration)."""
import csv, html, pathlib, re
from indic_transliteration import sanscript
HERE = pathlib.Path(__file__).resolve().parent
rows = list(csv.DictReader(open(HERE.parent.parent / 'rv' / 'references.tsv', encoding='utf8'), delimiter='\t'))
def first(s, sep): return re.split(sep, s)[0].strip()
body = []
for r in rows:
    if r['status'] not in ('legend', 'extra'): continue
    en = first(r['english'], r' or ')
    dv = sanscript.transliterate(first(r['kannada'], r' ಅಥವಾ '), 'kannada', 'devanagari')
    body.append(f'<tr><td class="ab-en">{html.escape(en)}</td><td class="ab-dv">{html.escape(dv)}</td><td>{html.escape(r["work"])}</td></tr>')
out = f'''<section class="fm fm-text abbr-page" id="fm-abbr" data-fm="abbreviations">
 <h2 data-orig="">List of Abbreviations</h2>
 <p class="ab-intro">The works cited in the commentary, with the abbreviations used in this translation and the form in which the original prints them.</p>
 <table class="ab-table"><thead><tr><th>Used here</th><th>In the original</th><th>Work</th></tr></thead><tbody>
{chr(10).join(body)}
</tbody></table>
</section>
'''
(HERE / 'pages' / '10_abbreviations.html').write_text(out, encoding='utf8')
print(len(body), 'rows')
