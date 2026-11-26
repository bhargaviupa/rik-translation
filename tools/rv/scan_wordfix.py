#!/usr/bin/env python3
"""Words with `[?]` settled by the Wikisource text (Saṃhitā, Pada, Sāyaṇa-bhāṣya) of the same and the neighbouring sūktas (shared tool; Vol 25 first). No API.

  python3 tools/rv/scan_wordfix.py VOL [--apply] [--ratio 0.85]
For every `[?]` after a Kannada word in volN/work/scan_pages/pNNNN.md (user, Nov 25 2026: "if these occur in saṃhitā/pada/sāyaṇa, correct using the reference"):
  * the word (avagraha ಽ removed) is in the lexicon of the page's sūkta ± one neighbour (Saṃhitā + Pada + bhāṣya words in Kannada script) → `confirmed`: the mark is removed;
  * the word is a headword of a word-meaning entry (followed by `—`) or ends in ಃ, is not in the lexicon, and ONE lexicon word is at least --ratio similar
    (the next best at least 0.08 lower, same first letter) → `corrected`: the word is replaced by the lexicon word (without ಽ) and the mark removed;
  * otherwise it stays (`open`). Prose words of the Kannada commentary are never replaced, only confirmed.
Preview by default; --apply edits the page files and logs every change in volN/review/wordfix_applied.tsv (+ a line in repair_log.md)."""
import os, re, sys, glob, sqlite3, difflib
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); sys.path.insert(0, os.path.dirname(__file__))
import ws_fill
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789'); WORD = re.compile(r'[\u0C80-\u0CE5\u0CF0-\u0CFF]+')
def norm(w): return w.replace('ಽ', '').replace('‌', '').replace('‍', '')
def main():
    a = sys.argv[1:]; vol = a[0]; apply = '--apply' in a; ratio = float(a[a.index('--ratio') + 1]) if '--ratio' in a else 0.85
    con = sqlite3.connect(os.path.join(ROOT, 'refs', 'wikisource', 'index', 'ws.sqlite'))
    d = os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pages'); files = sorted(glob.glob(os.path.join(d, 'p*.md')))
    pages = {int(re.search(r'p(\d+)\.md', f).group(1)): open(f, encoding='utf8').read().split('\n') for f in files}
    H = re.compile(r'ಮಂಡಲ\s*[—–-]\s*([೦-೯]+)\s*[॥|]+\s*ಅನುವಾಕ\s*[—–-]\s*([೦-೯]+)\s*[॥|]+\s*ಸೂಕ್ತ\s*[—–-]\s*([೦-೯]+)')
    cur = None; on = {}
    for pg in sorted(pages):
        s = {cur} if cur else set()
        for l in pages[pg]:
            m = H.search(l)
            if m: cur = (int(m.group(1).translate(KD)), int(m.group(3).translate(KD))); s.add(cur)
        on[pg] = s
    allsk = [tuple(r) for r in con.execute('select m,s from sukta order by m,s')]; cache = {}
    def lex(sk):
        if sk in cache: return cache[sk]
        txt = []
        for col in ('samhita', 'pada'): txt += [r[0] or '' for r in con.execute(f'select {col} from rik where m=? and s=?', sk)]
        txt += [r[0] or '' for r in con.execute('select deva from para where m=? and s=?', sk)]
        W = set()
        for t in txt:
            for w in WORD.findall(ws_fill.kn(t)): W.add(norm(w))
        cache[sk] = W; return W
    changes = []; opened = 0
    for pg in sorted(pages):
        sks = set()
        for sk in on[pg]:
            if sk in allsk:
                i = allsk.index(sk); sks.update(allsk[max(0, i - 1):i + 2])
        if not sks: continue
        L = set().union(*[lex(sk) for sk in sks]); Ls = sorted(L)
        for li, line in enumerate(pages[pg]):
            for m in reversed(list(re.finditer(r'([\u0C80-\u0CE5\u0CF0-\u0CFF]+)\[\?\]', line))):
                w = m.group(1); n = norm(w); head = bool(re.match(r'\s*[—-]', line[m.end():m.end() + 4])); new = None; how = None
                if len(n) >= 3 and n in L: new, how = w, 'confirmed'
                elif head or w.endswith('ಃ'):
                    sc = sorted(((difflib.SequenceMatcher(None, n, c).ratio(), c) for c in Ls if c[:1] == n[:1] and abs(len(c) - len(n)) <= 2), reverse=True)
                    if sc and sc[0][0] >= ratio and (len(sc) == 1 or sc[0][0] - sc[1][0] >= 0.08): new, how = sc[0][1], 'corrected'
                if new is not None and how == 'corrected' and (norm(new) == n or new.replace('ೄ', 'ೃ') == w.replace('ೄ', 'ೃ')): new = None   # no visible change, or only the ṛ/ṝ sign (a Wikisource quirk)
                if new is None: opened += 1; continue
                changes.append((pg, li + 1, w, new, how)); pages[pg][li] = pages[pg][li][:m.start()] + new + pages[pg][li][m.end():]   # m already ends after the [?] (Nov 26 2026: '+ 3' deleted the three characters after every settled word); line = pages[pg][li]
    from collections import Counter
    print(dict(Counter(c[4] for c in changes)), 'open (word/lone marks left):', opened)
    for c in [x for x in changes if x[4] == 'corrected'][:15]: print('  corrected p%d l%d: %s → %s' % c[:4])
    if apply:
        for pg in {c[0] for c in changes}: open(os.path.join(d, f'p{pg:04d}.md'), 'w', encoding='utf8').write('\n'.join(pages[pg]))
        with open(os.path.join(ROOT, f'vol{vol}', 'review', 'wordfix_applied.tsv'), 'w', encoding='utf8') as o:
            o.write('pdf_page\tline\twas\tnow\thow\n'); [o.write('\t'.join(map(str, c)) + '\n') for c in changes]
        with open(os.path.join(ROOT, f'vol{vol}', 'review', 'repair_log.md'), 'a', encoding='utf8') as o:
            o.write(f'\n- scan_wordfix.py --apply: {len(changes)} words with [?] settled by the Wikisource Saṃhitā/Pada/bhāṣya words of the page\'s sūkta ±1 ({dict(Counter(c[4] for c in changes))}; list: review/wordfix_applied.tsv).\n')
        print('applied', len(changes))
main()
