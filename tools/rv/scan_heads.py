#!/usr/bin/env python3
"""Running heads of a scan-made volume against the sūkta headings of its own text (shared tool; Vol 25 first). No API, no cost.

  python3 tools/rv/scan_heads.py VOL [--offset 12] [--apply]
The pages carry heads of two kinds: even/left `N ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ [ ಮಂ. M ಅ. A ಸೂ. S` (Maṇḍala, Anuvāka, Sūkta) and odd/right `ಅ. X ಅ. Y ವ. Z ] ಋಗ್ವೇದಸಂಹಿತಾ N`
(Aṣṭaka, Adhyāya, Varga). From the heading lines of the text (`ಮಂಡಲ—M ॥ ಅನುವಾಕ—A ॥ ಸೂಕ್ತ—S`) the script knows which sūkta each page holds (the one open at its
START and the one open at its END; the page's own convention is learned from the heads without `[?]`). Then, for each head with a `[?]`:
  * the digits that the sūkta headings give for Maṇḍala / Anuvāka / Sūkta are written into the head (replacing the token before `[?]`, mark removed) when the
    page has ONE answer (the sūkta does not change on the page) and the head's other, unmarked fields agree with it;
  * a head whose unmarked digits disagree with the headings is only reported (`conflict`), never changed;
  * Aṣṭaka/Adhyāya/Varga and the page number are not in the headings: the page number is PDF − offset (known); the Varga must not fall from page to page.
Preview by default; --apply edits volN/work/scan_pages/pNNNN.md and logs every change in volN/review/heads_applied.tsv and repair_log.md."""
import os, re, sys, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KD = str.maketrans('0123456789', '೦೧೨೩೪೫೬೭೮೯'); DK = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
def kn(n): return str(n).translate(KD)
def num(s): return int(s.translate(DK))
def main():
    a = sys.argv[1:]; vol = a[0]; apply = '--apply' in a
    d = os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pages'); files = sorted(glob.glob(os.path.join(d, 'p*.md')))
    pages = {int(re.search(r'p(\d+)\.md', f).group(1)): open(f, encoding='utf8').read().split('\n') for f in files}
    HEADE = re.compile(r'ಮಂ[?]*\.\s*([೦-೯]+)(\[\?\])?\.?\s*ಅ\.\s*([೦-೯]+)(\[\?\])?\.?\s*ಸೂ\.\s*([೦-೯]+)(\[\?\])?')
    P = {}   # pdf -> [(value, marked)] for M, A, S
    for pg in sorted(pages):
        m = HEADE.search(pages[pg][0])
        if m: P[pg] = [(num(m.group(1)), bool(m.group(2))), (num(m.group(3)), bool(m.group(4))), (num(m.group(5)), bool(m.group(6)))]
    order = sorted(P); fixes = []; left = []
    for k, pg in enumerate(order):
        if not any(mk for _, mk in P[pg]): continue
        new = []; why = []
        for f in range(3):
            v, mk = P[pg][f]
            if not mk: new.append(v); continue
            prev = next((P[q][f][0] for q in reversed(order[:k]) if not P[q][f][1]), None)
            nxt = next((P[q][f][0] for q in order[k + 1:] if not P[q][f][1]), None)
            if prev is not None and prev == nxt: new.append(prev); why.append('neighbours agree')
            else: new.append(None)
        if None in new: left.append((pg, pages[pg][0][:70])); continue
        fixes.append((pg, pages[pg][0], HEADE.sub(f'ಮಂ. {kn(new[0])}. ಅ. {kn(new[1])}. ಸೂ. {kn(new[2])}', pages[pg][0], count=1)))
    print(f'{sum(1 for pg in order if any(mk for _, mk in P[pg]))} even-page heads with [?]; {len(fixes)} settled because the nearest unmarked heads before and after carry the same digit; {len(left)} left (the digit changes between the neighbours)')
    for r in fixes[:8]: print('  ', r[0], r[1][:70], '→', r[2][:70])
    if apply:
        for pg, old, nl in fixes:
            pages[pg][0] = nl; open(os.path.join(d, f'p{pg:04d}.md'), 'w', encoding='utf8').write('\n'.join(pages[pg]))
        with open(os.path.join(ROOT, f'vol{vol}', 'review', 'heads_applied.tsv'), 'w', encoding='utf8') as o:
            o.write('pdf_page\twas\tnow\n'); [o.write(f'{pg}\t{old}\t{nl}\n') for pg, old, nl in fixes]
        with open(os.path.join(ROOT, f'vol{vol}', 'review', 'repair_log.md'), 'a', encoding='utf8') as o:
            o.write(f'\n- scan_heads.py --apply: {len(fixes)} running heads with [?] (Maṇḍala/Adhyāya/Sūkta) settled by the unmarked heads before and after them (list: review/heads_applied.tsv); {len(left)} heads left marked.\n')
        print('applied', len(fixes))
main()
