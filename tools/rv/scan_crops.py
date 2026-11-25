#!/usr/bin/env python3
"""Enlarged crops around the doubtful numbers of a scan-made volume, for a focused re-reading (shared tool; Vol 25 first). No API, no cost.

  python3 tools/rv/scan_crops.py VOL [--kinds number,head] [--per 10]
For each open question of volN/review/questions.tsv of those kinds (and not yet answered): the page is rendered, Tesseract (kan+eng, TSV with word boxes, cached in
volN/work/ocr/pNNNN.tsv) gives the printed lines with their boxes; the line that holds the mark is found by matching the letters before and after the mark
(digits ignored) against each printed line. The crop is that line's neighbourhood (a head: the whole head line), enlarged to about 1560 px wide. `per` crops are stacked
into one mosaic image volN/work/crops/mosaic_NNN.png with the question id and the reading printed above each crop; volN/work/crops/mosaic_NNN.tsv lists its ids.
Questions whose line cannot be found (match under 8 letters) are listed in volN/work/crops/nomatch.tsv (they go to the whole-page re-reading)."""
import os, re, sys, csv, subprocess, difflib
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LET = re.compile(r'[^ಀ-೥೰-೿A-Za-z]+')
def letters(s): return LET.sub('', s)
def page_png(vol, pg):
    d = os.path.join(ROOT, f'vol{vol}', 'work', 'crops'); os.makedirs(d, exist_ok=True); out = os.path.join(d, f'full{pg:04d}')
    if not os.path.exists(out + '.png'):
        subprocess.run(['pdftoppm', '-f', str(pg), '-l', str(pg), '-scale-to-x', '2304', '-scale-to-y', '-1', '-gray', '-png', '-singlefile', PDFS[vol], out], check=True)
    return out + '.png'
def lines_of(vol, pg, png):
    tsv = os.path.join(ROOT, f'vol{vol}', 'work', 'ocr', f'p{pg:04d}.tsv')
    if not os.path.exists(tsv):
        env = dict(os.environ, OMP_THREAD_LIMIT='1')
        r = subprocess.run(['tesseract', png, 'stdout', '--psm', '3', '-l', 'kan+eng', 'tsv'], capture_output=True, text=True, env=env); open(tsv, 'w', encoding='utf8').write(r.stdout)
    L = {}
    for r in csv.reader(open(tsv, encoding='utf8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        if not r or r[0] == 'level' or len(r) < 12 or r[11].strip() == '' or float(r[10]) < 0: continue
        k = (r[2], r[3], r[4]); l, t, w, h = map(int, r[6:10]); L.setdefault(k, []).append((l, t, l + w, t + h, r[11]))
    out = []
    for k, ws in L.items():
        ws.sort(); out.append((min(x[0] for x in ws), min(x[1] for x in ws), max(x[2] for x in ws), max(x[3] for x in ws), ' '.join(x[4] for x in ws)))
    return sorted(out, key=lambda x: x[1])
def main():
    a = sys.argv[1:]; vol = a[0]; kinds = (a[a.index('--kinds') + 1] if '--kinds' in a else 'number,head').split(','); per = int(a[a.index('--per') + 1]) if '--per' in a else 10; tag = a[a.index('--tag') + 1] if '--tag' in a else ('num' if 'word' not in kinds else 'word')
    PDFS[vol] = os.path.join(ROOT, f'vol{vol}', 'scans', f'Rig_Vol{vol}.pdf')
    Q = [q for q in csv.DictReader(open(os.path.join(ROOT, f'vol{vol}', 'review', 'questions.tsv'), encoding='utf8'), delimiter='\t') if q['kind'] in kinds and not q['answer']]
    os.makedirs(os.path.join(ROOT, f'vol{vol}', 'work', 'ocr'), exist_ok=True); cd = os.path.join(ROOT, f'vol{vol}', 'work', 'crops')
    try: font = ImageFont.load_default(size=26)
    except TypeError: font = ImageFont.load_default()
    items = []; nomatch = []; cache = {}
    for q in Q:
        pg = int(q['pdf_page']); png = page_png(vol, pg)
        if pg not in cache: cache[pg] = (Image.open(png), lines_of(vol, pg, png))
        img, L = cache[pg]; W, H = img.size
        # the full text line (page file) for the window around the mark
        txt = open(os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pages', f'p{pg:04d}.md'), encoding='utf8').read().split('\n')[int(q['line']) - 1]
        marks = [m.start() for m in re.finditer(r'\[\?\]', txt)]; k = int(q['nth_mark']) - 1
        if k >= len(marks): nomatch.append((q['id'], 'mark gone')); continue
        pos = marks[k]; before = letters(txt[max(0, pos - 40):pos])[-14:]; after = letters(txt[pos + 3:pos + 43])[:14]
        if q['kind'] == 'head':
            top = [x for x in L if x[1] < H * 0.2]; best = top[0] if top else None; sc = 99
            if best is None: nomatch.append((q['id'], 'no head line')); continue
            box = (max(0, best[0] - 30), max(0, best[1] - 25), min(W, best[2] + 30), min(H, best[3] + 25))
        else:
            best = None; sc = 0
            for x in L:
                s = letters(x[4]); m1 = difflib.SequenceMatcher(None, s, before + after).find_longest_match(0, len(s), 0, len(before + after)).size
                m2 = max(difflib.SequenceMatcher(None, s, before).find_longest_match(0, len(s), 0, len(before)).size, difflib.SequenceMatcher(None, s, after).find_longest_match(0, len(s), 0, len(after)).size)
                if max(m1, m2) > sc: sc = max(m1, m2); best = x
            if best is None or sc < 6: nomatch.append((q['id'], f'match {sc}')); continue
            ln = max(1, len(letters(txt))); frac = len(letters(txt[:pos])) / ln
            # the mark's place inside the printed line: proportional to the letters of the full paragraph is not valid for wrapped lines, so use the matched text's place
            s = letters(best[4]); mm = difflib.SequenceMatcher(None, s, before + after).find_longest_match(0, len(s), 0, len(before + after))
            rel = (mm.a + (len(before) - mm.b if mm.b < len(before) else 0)) / max(1, len(s)); cx = best[0] + rel * (best[2] - best[0])
            hw = 600; box = (int(max(0, min(cx - hw, W - 2 * hw))), max(0, best[1] - 25), int(min(W, max(cx + hw, 2 * hw))), min(H, best[3] + 25))
        crop = img.crop(box).convert('RGB'); sc2 = 1560 / crop.width; crop = crop.resize((1560, max(1, int(crop.height * sc2))))
        items.append((q, crop))
    os.makedirs(cd, exist_ok=True)
    n = 0
    for j in range(0, len(items), per):
        grp = items[j:j + per]; n += 1; Hh = sum(c.height + 44 for _, c in grp); M = Image.new('RGB', (1560, Hh), 'white'); d = ImageDraw.Draw(M); y = 0
        for q, c in grp:
            d.rectangle((0, y, 1560, y + 40), fill=(225, 235, 255)); d.text((8, y + 4), f"{q['id']}  PDF p{q['pdf_page']}  {q['kind']}  token before the mark: {q['reading']}", fill='black', font=font); y += 44; M.paste(c, (0, y)); y += c.height
        M.save(os.path.join(cd, f'mosaic_{tag}_{n:03d}.png'))
        with open(os.path.join(cd, f'mosaic_{tag}_{n:03d}.tsv'), 'w', encoding='utf8') as o:
            for q, c in grp: o.write('\t'.join([q['id'], q['pdf_page'], q['kind'], q['reading'], q['context'][:100]]) + '\n')
    with open(os.path.join(cd, f'nomatch_{tag}.tsv'), 'w', encoding='utf8') as o:
        for r in nomatch: o.write('\t'.join(r) + '\n')
    print(f'{len(Q)} questions: {len(items)} cropped into {n} mosaics; {len(nomatch)} without a matching printed line → {cd}')
PDFS = {}
main()
