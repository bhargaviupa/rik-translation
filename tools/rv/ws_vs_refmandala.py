#!/usr/bin/env python3
"""Compare the accented Saṃhitā of the Wikisource index (refs/wikisource/index/ws.sqlite) with the user's reference text
(refs/mandala/rv_mandala*.html), Ṛk by Ṛk.

    python3 tools/rv/ws_vs_refmandala.py            # all 10,552 Ṛks: summary + refs/wikisource/index/vs_refmandala.tsv
    python3 tools/rv/ws_vs_refmandala.py 1.137 3.3  # summary for these sūktas only

Classes: 1 identical letter for letter and accent for accent · 2 identical except nasal spelling (न्/म्… before a consonant or at
the end of a word ↔ ं) and the place of an accent mark next to ं ँ ः · 3 same letters, accent marks differ · 4 letters differ.
Classes 3 and 4 are listed with the differing places. Nothing is corrected; the two texts are only compared.
"""
import collections, difflib, glob, importlib.util, pathlib, re, sqlite3, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('av', ROOT / 'publish' / 'tools' / 'accents' / 'accent_volume.py')
av = importlib.util.module_from_spec(spec); spec.loader.exec_module(av)
ACCS = '॒॑॓॔'
ACC = re.compile('[' + ACCS + '᳐-᳿]')


def key(s): return re.sub(r'[\s।॥]|[०-९0-9.]+', '', s).replace('‍', '')


def prep(s):
    s = re.sub(r'[॥।]|[०-९0-9.]+', '', s).replace('‍', '')
    s = re.sub(r'म्(?=\s|$)', 'ं', s)
    s = re.sub('[ङञणनम]्(?=[क-ह])', 'ं', s)
    s = re.sub('([' + ACCS + '])([ंँः])', r'\2\1', s)
    return re.sub(r'\s+', '', s)


def classify(r, w):
    if key(r) == key(w): return 1
    a, b = prep(r), prep(w)
    if a == b: return 2
    return 3 if ACC.sub('', a) == ACC.sub('', b) else 4


def places(r, w):
    a, b = prep(r), prep(w)
    if ACC.sub('', a) == ACC.sub('', b):
        a2, b2 = a, b
    else:
        a2, b2 = ACC.sub('', a), ACC.sub('', b)
    return [f'ref «{a2[max(0, i1 - 6):i1]}[{a2[i1:i2]}]{a2[i2:i2 + 4]}» wiki «{b2[max(0, j1 - 6):j1]}[{b2[j1:j2]}]{b2[j2:j2 + 4]}»'
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a2, b2, autojunk=False).get_opcodes() if op != 'equal']


def main(a):
    ref = {}
    for f in sorted(glob.glob(str(ROOT / 'refs' / 'mandala' / 'rv_mandala*.html'))):
        for k, line in av.read_ref(f): ref.setdefault(k, []).append(line)
    con = sqlite3.connect(ROOT / 'refs' / 'wikisource' / 'index' / 'ws.sqlite')
    want = {tuple(int(x) for x in s.split('.')) for s in a}
    c, rows = collections.Counter(), []
    for m, s, r, sa in con.execute('select m,s,r,samhita_acc from rik order by m,s,r'):
        if want and (m, s) not in want: continue
        k = (m, s, r)
        if k not in ref: c['not in the reference'] += 1; continue
        R, W = ' '.join(ref[k]), sa.replace('\n', ' ')
        cl = classify(R, W); c[cl] += 1
        if cl >= 3: rows.append((f'{m}.{s}.{r}', cl, '; '.join(places(R, W)[:3])))
    names = {1: 'identical, letter for letter and accent for accent', 2: 'identical except nasal spelling / accent-mark position',
             3: 'same letters, accent marks differ', 4: 'letters differ'}
    for k in sorted(c, key=str): print(f'{c[k]:6}  {names.get(k, k)}')
    print(f'{sum(c.values()):6}  Ṛks compared')
    if not want:
        out = ROOT / 'refs' / 'wikisource' / 'index' / 'vs_refmandala.tsv'
        out.write_text('Ṛk\tclass\tdifferences\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows), encoding='utf-8')
        print(f'{len(rows)} Ṛks listed in {out.relative_to(ROOT)}')


if __name__ == '__main__':
    main(sys.argv[1:])
