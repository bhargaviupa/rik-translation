#!/usr/bin/env python3
"""Compare Sāyaṇa's bhāṣya in three texts, sūkta by sūkta: the volume's supplied text, sa.wikisource.org
(saved by wikisource_sayana.py) and the reference text of vishvasa.github.io (sayana_ref.py).

    python3 tools/rv/wikisource_compare.py N [S1 [S2]]     # volume N (its mandala from volcfg.json), sūktas S1..S2
Writes volN/review/wikisource_compare.tsv (one row per place where the texts differ) and prints a summary.

Method (so the figures can be judged): each text is reduced to Devanagari words: accent marks, quotation marks,
daṇḍas, digits, brackets and the nasal spelling (ṅ ñ ṇ n m + consonant = anusvāra) are removed or unified; then
the three word lists are aligned two by two. A "place" is a run of words that differ. Reference abbreviations and
numbers are therefore NOT compared (digits are dropped; abbreviations differ by edition and are the reference
corrector's business). Nothing is corrected anywhere.
"""
import difflib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'rv'))
import sayana_ref

ACC = re.compile('[॒॑॓॔᳐-᳿]')


def words(t):
    t = ACC.sub('', t)
    t = re.sub(r'\([^()]{0,80}\)', ' ', t)                        # parenthesised references (wikisource style)
    t = re.sub('[ङञणनम]्(?=[क-ह])', 'ं', t)
    t = t.replace('ऽ', '')
    t = re.sub(r'[^ऀ-ॿ]+|[०-९।॥]+', ' ', t)             # keep Devanagari letters only
    t = re.sub(r'[०-९।॥]', ' ', t)
    return t.split()


def supplied(vol, s):
    """Quote lines of the Sāyaṇa-bhāṣya blocks of sūkta s in the volume's English file (continuations over page
    marks included): a quote group belongs to the type of the last heading, or of the previous group."""
    f = ROOT / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_English_Translation.md'
    lines = f.read_text(encoding='utf-8').split('\n')
    inside, typ, out, prev_quote = False, None, [], False
    for l in lines:
        m = re.match(r'## Sūkta (\d+) ', l)
        if m:
            inside = int(m.group(1)) == s
            typ, prev_quote = None, False
            continue
        if not inside:
            continue
        if l.startswith('##### '):
            if 'सायणभाष्यम्' in l:
                typ = 'bhashya'
            elif 'संहितापाठः' in l or 'पदपाठः' in l:
                typ = 'other'                 # other headings (Gist, Grammar...) leave the type: a quote after a page mark continues it
        elif l.startswith('> '):
            if typ == 'bhashya':
                out.append(l[2:])
    return ' '.join(out)


def places(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return [(i1, i2, j1, j2) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']


def main(a):
    vol = int(a[0])
    cfg = json.loads((ROOT / f'vol{vol}' / 'volcfg.json').read_text(encoding='utf-8'))
    m = cfg['mandalas'][0]
    wsdir = ROOT / 'refs' / 'wikisource'
    if len(a) > 1:
        ss = list(range(int(a[1]), int(a[2] if len(a) > 2 else a[1]) + 1))
    else:
        ss = sorted(int(p.stem.split('_S')[1]) for p in wsdir.glob(f'M{m:02d}_S*.json'))
    rows, tot = [], dict(sup=0, ws=0, vi=0, sw=0, sv=0, wv=0, swonly=0, svonly=0, wvdiff3=0)
    print(f'{"sūkta":>6} {"words S/W/V":>16} {"S≠W":>5} {"S≠V":>5} {"W≠V":>5}  {"S≠W, V=W":>9}')
    for s in ss:
        d = json.loads((wsdir / f'M{m:02d}_S{s:03d}.json').read_text(encoding='utf-8'))
        S = words(supplied(vol, s))
        W = words(d['intro'] + ' ' + ' '.join(r['bhashya'] for r in d['rks']))
        V = words(' '.join(sayana_ref.blocks(m, s)))
        sw, sv, wv = places(S, W), places(S, V), places(W, V)
        # a place S≠W where V agrees with W: the supplied text is the odd one out
        both = 0
        for i1, i2, j1, j2 in sw:
            wtxt = ' '.join(W[j1:j2])
            if wtxt and wtxt in ' '.join(V):
                both += 1
        print(f'{m}.{s:>3} {len(S):>5}/{len(W):>5}/{len(V):>5} {len(sw):>5} {len(sv):>5} {len(wv):>5}  {both:>9}')
        for i1, i2, j1, j2 in sw:
            sj, wj = ''.join(S[i1:i2]), ''.join(W[j1:j2])
            kind = ('only in wikisource' if not sj else 'only in supplied' if not wj else
                    'spacing/sandhi spelling only' if sj == wj else 'letters differ')
            rows.append((f'{m}.{s}', kind, ' '.join(S[max(0, i1 - 3):i1]), ' '.join(S[i1:i2]),
                         ' '.join(W[j1:j2]), ' '.join(W[j2:j2 + 3]),
                         'vishvasa agrees with wikisource' if ' '.join(W[j1:j2]) and ' '.join(W[j1:j2]) in ' '.join(V) else ''))
        for k, v in dict(sup=len(S), ws=len(W), vi=len(V), sw=len(sw), sv=len(sv), wv=len(wv), swonly=both).items():
            tot[k] += v
    print(f'\ntotal words S/W/V: {tot["sup"]}/{tot["ws"]}/{tot["vi"]}; places S≠W {tot["sw"]}, S≠V {tot["sv"]}, W≠V {tot["wv"]}; '
          f'S≠W places where V agrees with W: {tot["swonly"]}')
    out = ROOT / f'vol{vol}' / 'review' / 'wikisource_compare.tsv'
    out.parent.mkdir(exist_ok=True)
    with out.open('w', encoding='utf-8') as fh:
        fh.write('sūkta\tkind\tbefore (supplied)\tsupplied\twikisource\tafter (wikisource)\tnote\n')
        for r in rows:
            fh.write('\t'.join(r) + '\n')
    import collections
    kinds = collections.Counter(r[1] for r in rows)
    print('places by kind:', dict(kinds))
    print(f'{len(rows)} rows written to {out.relative_to(ROOT)}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
