#!/usr/bin/env python3
"""Checks on transcribed scan pages (shared tool; Vol 25 first). No API, no cost.

  python3 tools/rv/scan_check.py VOL FIRST LAST [--offset 12]
      for PDF pages FIRST..LAST: file volN/work/scan_pages/pNNNN.md exists and is not empty; the running head carries the printed page number
      PDF - offset (the number is read from the first line; a page without a head, e.g. a sūkta-opening page, is reported, not failed);
      no letters of other scripts (Tamil, Telugu, Malayalam, Bengali, Devanagari letters; the dandas । ॥ are allowed; Latin is not tested);
      `[?]` per page; block markers only of the three kinds. Exit status 1 if a hard check fails (missing file, wrong page number, other script, bad marker).
"""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
OTHER = re.compile('[\u0900-\u0963\u0966-\u097F\u0980-\u09FF\u0B80-\u0BFF\u0C00-\u0C7F\u0D00-\u0D7F]')

def check(vol, first, last, offset=12):
    d = os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pages'); bad = []; q = 0; rows = []
    for pg in range(first, last + 1):
        f = os.path.join(d, f'p{pg:04d}.md')
        if not os.path.exists(f) or not os.path.getsize(f): bad.append(f'{pg}: file missing or empty'); continue
        t = open(f, encoding='utf8').read(); head = t.split('\n')[0]; n = t.count('[?]'); q += n
        nums = [int(x.translate(KD)) for x in re.findall(r'(?<![0-9೦-೯])[0-9೦-೯]{1,3}(?![0-9೦-೯])', head)]
        want = pg - offset
        if head.startswith('<!--'): print(f'note {pg}: no running head ({head[:40]})')
        elif want not in nums: bad.append(f'{pg}: head has {nums}, expected {want}: {head[:60]}')
        o = OTHER.findall(re.sub(r'\[\[block:[^\]]*\]\]', '', t))
        if o: bad.append(f'{pg}: letters of other scripts: {"".join(sorted(set(o)))}')
        for m in re.findall(r'\[\[block:([^\]]*)\]\]', t):
            if m.strip() not in ('samhita', 'pada', 'bhashya'): bad.append(f'{pg}: bad marker [[block:{m}]]')
        rows.append((pg, n))
    print(f'pages {first}-{last}: {len(rows)} read, [?] total {q}, per page ' + ' '.join(f'{p}:{n}' for p, n in rows))
    for b in bad: print('FAIL', b)
    return not bad

if __name__ == '__main__':
    a = sys.argv[1:]; off = 12
    if '--offset' in a: i = a.index('--offset'); off = int(a[i + 1]); del a[i:i + 2]
    sys.exit(0 if check(a[0], int(a[1]), int(a[2]), off) else 1)
