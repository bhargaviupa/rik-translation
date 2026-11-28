#!/usr/bin/env python3
"""Which structural elements does each volume's English / Kannada file actually have?  (read-only; Nov 27 2026; basis of the PDF content profiles)

  python3 tools/rv/element_scan.py [--en|--kn] [--min N] [--vols 3,4,24]   table of line signatures x volumes
  python3 tools/rv/element_scan.py --vol 24 --en --examples KEY            first lines that carry a signature

A signature is the shape of a heading line ('#### Ṛk N') or of a label line (italic-only '*…*' or bold-only '**…**' line, '> *…*' block label), with every digit run
replaced by N and the text cut at 48 characters.  Nothing is written."""
import re, sys, os, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
def sig(l):
    t = l.rstrip()
    if not t.strip(): return None
    if re.match(r'#{1,6} ', t): k = 'H ' + t
    elif re.fullmatch(r'\*{1,2}[^*].*[^*]\*{1,2}', t.strip()) and len(t) < 110: k = 'L ' + t.strip()
    elif re.fullmatch(r'> \*{1,2}[^*].*\*{1,2}', t.strip()) and len(t) < 90: k = 'B ' + t.strip()
    elif t.startswith('<!--'): k = 'C ' + t
    elif re.match(r'\*\*[A-Za-z ]+:?\*\*', t): k = 'S ' + t
    else: return None
    k = re.sub(r'\d+', 'N', k.translate(KD)); k = re.sub(r'(?<=N)[ab]\b', '', k)
    return k[:48]
def files(vol, kind):
    pat = f'vol{vol}/Rigveda_Samhita_Vol{vol}_{"English_Translation" if kind == "en" else "Kannada_Text"}.md'
    return [f for f in glob.glob(os.path.join(ROOT, pat))]
def scan(vol, kind):
    c = collections.Counter(); ex = {}
    for f in files(vol, kind):
        for i, l in enumerate(open(f, encoding='utf8', errors='replace').read().split('\n')):
            k = sig(l)
            if k: c[k] += 1; ex.setdefault(k, (os.path.relpath(f, ROOT), i + 1, l[:100]))
    return c, ex
ELEMENTS = [   # (element, regex on the signature of a heading/label line) -- first match wins
    ('page',       r'^[HC] .*(Printed p\.|Page N|printed N)'),
    ('sukta',      r'^H ##? .*(Sūkta|ಸೂಕ್ತ|Maṇḍala|ಮಂಡಲ)'),
    ('rk',         r'^H ###+ .*(Ṛk N|Rik N|ಋಕ್ N)'),
    ('gist',       r'Gist of the bhāṣya'),
    ('printed_en', r'English [Tt]ranslation|Printed English|Embedded English'),
    ('pratipada',  r'प्रतिपदार्थ|Prati-?padārtha|ಪ್ರತಿಪದಾರ್ಥ'),
    ('bhavartha',  r'भावार्थ|Bhāvārtha|ಭಾವಾರ್ಥ'),
    ('samhita',    r'संहितापाठ|Saṃhitā-pāṭha|ಸಂಹಿತಾಪಾಠ'),
    ('pada',       r'पदपाठ|Pada-pāṭha|ಪದಪಾಠ'),
    ('bhashya',    r'सायणभाष्य|Sāyaṇa-bhāṣya|ಸಾಯಣಭಾಷ್ಯಂ\*'),
    ('special',    r'विशेषविषय|Special Topics|Viśeṣa|ವಿಶೇಷವಿಷಯಗಳು'),
    ('grammar',    r'Grammar|Vyākaraṇa|ವ್ಯಾಕರಣ'),
    ('anuvada',    r'Anuvāda'),
    ('particulars',r'Particulars'),
    ('note',       r'\*\*(NOTE|GLOSS)\*\*'),
    ('remark',     r'Running head|Header:|stray line'),
]
def element(k):
    for name, rx in ELEMENTS:
        if re.search(rx, k): return name
    return None
def matrix(kind, vols):
    names = [n for n, _ in ELEMENTS]; rows = {}
    for v in vols:
        c, _ = scan(v, kind)
        if not c: continue
        r = collections.Counter(); forms = collections.defaultdict(set)
        for k, n in c.items():
            e = element(k)
            if e: r[e] += n; forms[e].add(k)
        rows[v] = (r, forms)
    print('vol  ' + ' '.join(f'{n[:7]:>7}' for n in names)); 
    for v, (r, f) in rows.items(): print(f'{v:>3}  ' + ' '.join(f'{r[n]:>7}' for n in names))
    print('\nnumber of different label spellings per element (all volumes):')
    for n in names: print(f'  {n:12}', len(set().union(*[f[n] for _, f in rows.values()])))
def main(a):
    if '--matrix' in a:
        kind = 'kn' if '--kn' in a else 'en'
        vols = sorted(int(re.search(r'vol(\d+)$', d).group(1)) for d in glob.glob(os.path.join(ROOT, 'vol*')) if re.search(r'vol\d+$', d))
        return matrix(kind, vols)

    kind = 'kn' if '--kn' in a else 'en'; mn = int(a[a.index('--min') + 1]) if '--min' in a else 40
    vols = [int(x) for x in a[a.index('--vols') + 1].split(',')] if '--vols' in a else sorted(int(re.search(r'vol(\d+)$', d).group(1)) for d in glob.glob(os.path.join(ROOT, 'vol*')) if re.search(r'vol\d+$', d))
    if '--vol' in a:
        v = int(a[a.index('--vol') + 1]); key = a[a.index('--examples') + 1] if '--examples' in a else None
        c, ex = scan(v, kind)
        for k, n in c.most_common():
            if key is None or key in k: print(n, k, '|', ex[k][0] + ':' + str(ex[k][1]))
        return
    S = {v: scan(v, kind)[0] for v in vols}; S = {v: c for v, c in S.items() if c}
    tot = collections.Counter(); present = collections.Counter()
    for c in S.values():
        for k, n in c.items(): tot[k] += n; present[k] += 1
    keys = [k for k, n in tot.most_common() if n >= mn]
    print('volumes:', ' '.join(map(str, S))); print()
    for k in keys:
        print(f'{k!r:60} total {tot[k]:6} vols {present[k]:2} | ' + ' '.join(f'{v}:{S[v].get(k, 0)}' for v in S if S[v].get(k, 0)))
if __name__ == '__main__': main(sys.argv[1:])
