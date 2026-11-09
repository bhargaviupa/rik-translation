#!/usr/bin/env python3
"""Add the printed page to a review TSV whose 2nd column is a line number of the volume's English file.

  python3 tools/rv/annotate_report.py N [vol N/review/accent_report.tsv]

Writes volN/review/accent_report_pages.tsv: page <TAB> original columns (the original file is left unchanged).
Line numbers refer to the English file as it was when the report was made: re-run the report first if the file changed."""
import re, sys, pathlib
vol = int(sys.argv[1]); root = pathlib.Path(__file__).resolve().parents[2]
src = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else root / f'vol{vol}' / 'review' / 'accent_report.tsv'
en = (root / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_English_Translation.md').read_text(encoding='utf8').split('\n')
page, pg = [], 0
for l in en:
    m = re.match(r'### Printed p\. (\d+)', l)
    if m: pg = int(m.group(1))
    page.append(pg)
out = []
for l in src.read_text(encoding='utf8').split('\n'):
    if not l.strip(): continue
    c = l.split('\t')
    try: n = int(c[1]); p = page[n - 1]
    except Exception: p = ''
    out.append(f'{p}\t{l}')
dst = src.with_name(src.stem + '_pages.tsv'); dst.write_text('\n'.join(out) + '\n', encoding='utf8'); print('wrote', dst, len(out), 'rows')
