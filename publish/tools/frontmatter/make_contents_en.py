#!/usr/bin/env python3
"""English contents of a volume from the Kannada transcription and a data file (Nov 28 2026; replaces the private make_contents_en.py of Vols 28-30 for new volumes).

  python3 publish/tools/frontmatter/make_contents_en.py N [--end WORD] [--check]

Reads  volN/contents_src/contents_kn.md  (the user's transcription of the printed contents; end of the region = the line holding WORD, default
'end of contents', or the volume's pubcfg `contents.end`)  and  volN/contents_src/contents_en.tsv  (one row per parsed block: `src<TAB>English`, src = line number
in contents_kn.md; `{S}` in the English = "33. The thirty-third sūkta, beginning ⟦incipit⟧", incipit = the words before ' ಎಂಬ ' of the Kannada line),
and writes volN/contents_en.json [{"src": n, "en": "..."}], the form volbook.py reads (`contents_en` in pubcfg.json).
Rules enforced (nothing is written when one fails): every parsed block has exactly one row and no row stands for a missing block; every ⟦word⟧ is Kannada script and
occurs in the Kannada line of its block (Sanskrit is copied from the Kannada, never typed: CLAUDE.md rule 1); an English row is not empty.  --check = dry run."""
import re, sys, json, pathlib, csv
PUB = pathlib.Path(__file__).resolve().parents[2]; ROOT = PUB.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import contents_parse
KD = dict(zip('೦೧೨೩೪೫೬೭೮೯', '0123456789'))
ONES = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = 'x x twenty thirty forty fifty sixty seventy eighty ninety'.split()
ORD = {'one': 'first', 'two': 'second', 'three': 'third', 'five': 'fifth', 'eight': 'eighth', 'nine': 'ninth', 'twelve': 'twelfth'}
def card(n):
    if n < 20: return ONES[n]
    if n < 100: return TENS[n // 10] + ('-' + ONES[n % 10] if n % 10 else '')
    return ONES[n // 100] + ' hundred' + (' ' + card(n % 100) if n % 100 else '')
def ordinal(n):
    w = card(n); last = re.split(r'[- ]', w)[-1]
    if last in ORD: return w[:len(w) - len(last)] + ORD[last]
    if last.endswith('y'): return w[:-1] + 'ieth'
    return w + 'th'
def main(a):
    n = int(next(x for x in a if x.isdigit())); check = '--check' in a
    end = a[a.index('--end') + 1] if '--end' in a else None
    d = ROOT / f'vol{n}'; kn = d / 'contents_src' / 'contents_kn.md'; tsv = d / 'contents_src' / 'contents_en.tsv'
    if end is None:
        pc = d / 'pubcfg.json'; end = (json.loads(pc.read_text(encoding='utf8')).get('contents') or {}).get('end') if pc.exists() else None
    end = end or 'end of contents'
    lines = kn.read_text(encoding='utf8').split('\n'); blocks = contents_parse.parse(lines, 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ', end, {}); by = {b['src']: b for b in blocks}
    rows = {}
    for r in csv.reader(open(tsv, encoding='utf8'), delimiter='\t', quoting=csv.QUOTE_NONE):
        if len(r) < 2 or not r[0].strip().isdigit(): continue
        s = int(r[0]); assert s not in rows, f'row {s} twice'; rows[s] = r[1].strip()
    bad = []
    for s in sorted(set(by) - set(rows)): bad.append(f'no English row for block at line {s}: {by[s]["text"][:50]}')
    for s in sorted(set(rows) - set(by)): bad.append(f'row {s} is not a block of the contents')
    out = []
    for s in sorted(rows):
        if s not in by: continue
        b = by[s]; en = rows[s]
        if not en: bad.append(f'row {s} empty'); continue
        if '{S}' in en:
            if b['t'] != 'sukta': bad.append(f'row {s}: {{S}} on a block that is not a sūkta'); continue
            num = int(''.join(KD[c] for c in b['no'])); inc = b['text'].split(' ಎಂಬ ')[0].strip()
            en = en.replace('{S}', f'{num}. The {ordinal(num)} sūkta, beginning ⟦{inc}⟧')
        kline = re.sub(r'\s+', ' ', b['text'])
        for w in re.findall(r'⟦([^⟧]*)⟧', en):
            if not re.search('[ಀ-೿]', w): bad.append(f'row {s}: ⟦{w}⟧ is not Kannada script')
            elif re.sub(r'\s+', ' ', w) not in kline: bad.append(f'row {s}: ⟦{w}⟧ does not occur in its Kannada line "{kline[:50]}"')
        out.append({'src': s, 'en': en})
    print(f'vol{n}: {len(blocks)} blocks, {len(rows)} rows, {len(out)} written')
    for x in bad: print('  FAIL', x)
    if bad: sys.exit(1)
    if not check: (d / 'contents_en.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8'); print('written', f'vol{n}/contents_en.json')
if __name__ == '__main__': main(sys.argv[1:])
