#!/usr/bin/env python3
"""Tesseract Kannada OCR of scan pages, as a SECOND, independent reading (shared tool; Vol 25 first). No API, no cost.

  python3 tools/rv/scan_ocr.py run VOL PDF FIRST LAST [--jobs 3]     writes volN/work/ocr/pNNNN.txt (PDF page numbers)
  python3 tools/rv/scan_ocr.py numbers VOL FIRST LAST                for each `[?]` question of volN/review/questions.tsv: the number tokens of the best-matching
                                                                      OCR line (matched by the letters, digits ignored) next to our reading → volN/review/ocr_numbers.tsv
Needs `apt-get install tesseract-ocr tesseract-ocr-kan tesseract-ocr-eng`. The OCR reads Kannada digits badly (the pilot saw ೧೩-೧೮ → 03-08), so it is a vote, never a
correction: agreement raises confidence, disagreement is listed for the user's numeral list. Nothing is written into the page files."""
import os, re, sys, csv, subprocess, difflib
from concurrent.futures import ThreadPoolExecutor
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
BASE = 0   # page-file number minus PDF page (Vol 26 part 2: files p1001.. are PDF pages 1..)
def one(vol, pdf, pg):
    d = os.path.join(ROOT, f'vol{vol}', 'work', 'ocr'); os.makedirs(d, exist_ok=True); out = os.path.join(d, f'p{pg:04d}')
    if os.path.exists(out + '.txt') and os.path.getsize(out + '.txt'): return
    png = out + '_tmp'
    subprocess.run(['pdftoppm', '-f', str(pg - BASE), '-l', str(pg - BASE), '-scale-to-x', '2304', '-scale-to-y', '-1', '-gray', '-png', '-singlefile', pdf, png], check=True)
    subprocess.run(['tesseract', png + '.png', out, '--psm', '3', '-l', 'kan+eng'], capture_output=True); os.remove(png + '.png')
def run(vol, pdf, first, last, jobs):
    with ThreadPoolExecutor(jobs) as ex: list(ex.map(lambda p: one(vol, pdf, p), range(first, last + 1)))
def letters(s): return re.sub(r'[\s0-9೦-೯\-–—.,;:()\[\]|।॥?]+', '', s)
def nums(s): return [re.sub(r'\s', '', x).translate(KD) for x in re.findall(r'[೦-೯0-9]+(?:\s*[-–.]\s*[೦-೯0-9]+)*', s)]
def numbers(vol, first, last):
    Q = [q for q in csv.DictReader(open(os.path.join(ROOT, f'vol{vol}', 'review', 'questions.tsv'), encoding='utf8'), delimiter='\t') if q['kind'] in ('number', 'head') and first <= int(q['pdf_page']) <= last]
    outf = os.path.join(ROOT, f'vol{vol}', 'review', 'ocr_numbers.tsv'); rows = []; agree = 0
    for q in Q:
        f = os.path.join(ROOT, f'vol{vol}', 'work', 'ocr', f'p{int(q["pdf_page"]):04d}.txt')
        if not os.path.exists(f): continue
        L = [l for l in open(f, encoding='utf8').read().split('\n') if l.strip()]; ctx = q['context'].replace('[?]', '')
        best = max(L, key=lambda l: difflib.SequenceMatcher(None, letters(l), letters(ctx)).ratio()); r = difflib.SequenceMatcher(None, letters(best), letters(ctx)).ratio()
        ours = nums(ctx); theirs = nums(best); tok = q['reading'][:-3]; mine = re.sub(r'\s', '', tok).translate(KD)
        hit = 'agree' if any(mine and mine in t for t in theirs) else 'differ'
        agree += hit == 'agree'
        rows.append([q['id'], q['pdf_page'], q['line'], q['kind'], q['reading'], f'{r:.2f}', ' '.join(theirs), hit, best.strip()[:100]])
    with open(outf, 'w', encoding='utf8') as o:
        o.write('id\tpdf_page\tline\tkind\treading\tline_match\tocr_numbers_on_line\tvote\tocr_line\n'); [o.write('\t'.join(r) + '\n') for r in rows]
    print(f'{len(rows)} number/head questions matched to OCR lines; OCR numbers on the line contain our reading: {agree}, not: {len(rows) - agree} → {outf}')
if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'run':
        jobs = int(a[a.index('--jobs') + 1]) if '--jobs' in a else 3; BASE = int(a[a.index('--base') + 1]) if '--base' in a else 0; run(a[1], a[2], int(a[3]), int(a[4]), jobs)
    else: numbers(a[1], int(a[2]), int(a[3]))
