#!/usr/bin/env python3
"""Extract the book's printed English translation of a Ṛk from a scanned page with Tesseract (English only).

The volumes print, under the heading "English Translation", the Ṛk in English (Wilson's translation), in clean
Latin type. This finds that heading and returns the English lines below it, up to where the Kannada begins
(Tesseract's confidence drops there). Misprints in the source are kept as printed; the output is a DRAFT to be
pasted with the source's misprints marked [sic] by the translator.

Usage:  python3 english_block.py PDF PAGE [--dpi 300]      (PAGE = PDF page number)
Needs:  tesseract with the 'eng' data, poppler (pdftoppm).
"""
import subprocess, sys, csv, io, re, tempfile, glob, os

def run(pdf, page, dpi=300):
    with tempfile.TemporaryDirectory() as t:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', '-f', str(page), '-l', str(page), '-png', pdf, t + '/p'], check=True)
        img = glob.glob(t + '/p*.png')[0]
        r = subprocess.run(['tesseract', img, 'stdout', '-l', 'eng', '--psm', '4', 'tsv'], capture_output=True, text=True)
    rows = list(csv.DictReader(io.StringIO(r.stdout), delimiter='\t', quoting=csv.QUOTE_NONE))
    lines = {}
    for w in rows:
        if w['level'] != '5' or not (w['text'] or '').strip(): continue
        lines.setdefault((w['block_num'], w['par_num'], w['line_num']), []).append(w)
    ordered = sorted(lines.values(), key=lambda ws: (int(ws[0]['top']) // 10, int(ws[0]['left'])))
    out, on = [], False
    for ws in ordered:
        text = ' '.join(w['text'] for w in ws)
        conf = sum(float(w['conf']) for w in ws) / len(ws)
        alpha = sum(c.isascii() and c.isalpha() for c in text) / max(1, len(text))
        if not on:
            if re.search(r'English', text, re.I) and re.search(r'Transl', text, re.I): on = True
            continue
        if conf < 60 or alpha < 0.6: break
        out.append(text)
    s = ' '.join(out)
    return re.sub(r'(\w)- (\w)', r'\1\2', s)

if __name__ == '__main__':
    if len(sys.argv) < 3: sys.exit(__doc__)
    print(run(sys.argv[1], int(sys.argv[2]), int(sys.argv[sys.argv.index('--dpi') + 1]) if '--dpi' in sys.argv else 300))
