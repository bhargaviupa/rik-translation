#!/usr/bin/env python3
"""List every `[?]` of the transcribed scan pages as a question (shared tool; Vol 25 first). No API, no cost.

  python3 tools/rv/scan_questions.py VOL FIRST LAST [--offset 12] [--out volN/review/questions.tsv]
One row per `[?]`: id, pdf page, printed page, line, half of the page image (a = top, b = bottom; by the line's place in the page), kind
(head = the running head; number = a digit/numeral before the mark; ref = a sūtra/verse/page reference line; word = a word or letter),
the reading (the token the mark follows), the context (the line), and empty columns `answer` and `source` for the user's reading.
Numbers come first in the sort order inside a page. Nothing is corrected here: the file is the checklist."""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KD = '೦-೯0-9'
def rows(vol, first, last, offset):
    d = os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pages'); out = []
    for pg in range(first, last + 1):
        f = os.path.join(d, f'p{pg:04d}.md')
        if not os.path.exists(f): continue
        lines = open(f, encoding='utf8').read().split('\n'); n = len(lines)
        for i, l in enumerate(lines):
            for nth, m in enumerate(re.finditer(r'\[\?\]', l), 1):
                before = l[:m.start()]; tok = re.split(r'[\s—,।|()]', before)[-1] if before.strip() else ''
                # include the following token if the mark stands inside a word (e.g. ಮಂ[?].)
                if i == 0: kind = 'head'
                elif re.search(f'[{KD}]$', before): kind = 'number'
                elif re.search(r'(ಸೂ|ಋ|ಅ|ವ|ಮಂ|ಪು|ಪುಟ|ನಿ|ಯಜು|ಅಥ|ಶ|ತೈ|ಐ|ಕಾ|ಮೈ|ಛಾ|ಬೃ|ಗೋ|ಕೌ|ಆಶ್ವ|ಸಾ)[. ]*[' + KD + r'\-೦-೯]+\s*$', before): kind = 'ref'
                else: kind = 'word'
                out.append((pg, pg - offset, i + 1, 'a' if (i + 0.5) / n < 0.5 else 'b', kind, (tok + '[?]'), nth, l.strip()[:160]))
    return out
if __name__ == '__main__':
    a = sys.argv[1:]; off = 12; outf = None
    if '--offset' in a: i = a.index('--offset'); off = int(a[i + 1]); del a[i:i + 2]
    if '--out' in a: i = a.index('--out'); outf = a[i + 1]; del a[i:i + 2]
    vol, first, last = a[0], int(a[1]), int(a[2]); outf = outf or os.path.join(ROOT, f'vol{vol}', 'review', 'questions.tsv')
    R = rows(vol, first, last, off); order = {'head': 0, 'number': 1, 'ref': 2, 'word': 3}
    R.sort(key=lambda r: (r[0], order[r[4]], r[2], r[6]))
    os.makedirs(os.path.dirname(outf), exist_ok=True)
    with open(outf, 'w', encoding='utf8') as o:
        o.write('id\tpdf_page\tprinted_page\tline\tnth_mark\timage\tkind\treading\tcontext\tanswer\tsource\n')
        for k, r in enumerate(R, 1): o.write(f'Q{k:04d}\t{r[0]}\t{r[1]}\t{r[2]}\t{r[6]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[7]}\t\t\n')
    from collections import Counter
    c = Counter(r[4] for r in R); print(f'{len(R)} questions → {outf}:', dict(c))
