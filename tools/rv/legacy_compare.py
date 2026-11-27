#!/usr/bin/env python3
"""Second reading of a re-translated volume against its old scan-based translation (Vol 13), free, no change to any text.

  python3 tools/rv/legacy_compare.py N

Writes volN/review/legacy_compare.tsv  (printed page, references only in the old text, references only in the new text)
and   volN/review/user_readings_compare.tsv (each reading the user gave for the old file, key page_doubt, with the references of that page of
the new English: 'found' when every reference of the reading stands on that page, else 'differs').
References = numbers like 5-32-5 or 1.112.7 (book/verse chains of two or three numbers). The supplied text is the base: nothing is changed from this list."""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
vol = sys.argv[1]
REF = re.compile(r'(?<![\d-])(\d{1,3})\s*[-.]\s*(\d{1,3})(?:\s*[-.]\s*(\d{1,3}))?(?![\d-])')
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
def pages(path):
    d, cur = {}, 0
    for l in pathlib.Path(path).read_text(encoding='utf8').split('\n'):
        m = re.match(r'### Printed p\. (\d+)', l)
        if m: cur = int(m.group(1)); d.setdefault(cur, []); continue
        d.setdefault(cur, []).append(l)
    return {k: '\n'.join(v) for k, v in d.items()}
def refs(t):
    t = t.translate(KD)
    return {'-'.join(x for x in m.groups() if x) for m in REF.finditer(t)}
new = pages(ROOT / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_English_Translation.md')
old = pages(next((ROOT / f'vol{vol}' / 'legacy').glob('*_scan.md')))
out = ['page\tonly in the old translation\tonly in the new translation']
for p in sorted(set(old) | set(new)):
    if p == 0: continue
    a, b = refs(old.get(p, '')), refs(new.get(p, ''))
    if a != b: out.append(f'{p}\t{"; ".join(sorted(a - b))}\t{"; ".join(sorted(b - a))}')
(ROOT / f'vol{vol}' / 'review' / 'legacy_compare.tsv').write_text('\n'.join(out) + '\n', encoding='utf8')
print(f'legacy_compare.tsv: {len(out) - 1} pages differ of {len(new) - 1}')
rd = ROOT / f'vol{vol}' / 'review' / 'user_readings_part1.tsv'
if rd.exists():
    rows = ['key\tuser reading\tstatus\treferences of the reading missing on that page of the new text']; nf = 0
    for l in rd.read_text(encoding='utf8').split('\n'):
        if not l.strip(): continue
        key, _, txt = l.partition('\t'); m = re.match(r'(\d+)_', key)
        if not m: continue
        p = int(m.group(1)); want = refs(txt)
        if not want: rows.append(f'{key}\t{txt}\tno reference in the reading\t'); continue
        have = refs(new.get(p, '')) | refs(new.get(p + 1, ''))
        miss = sorted(want - have); nf += bool(miss)
        rows.append(f'{key}\t{txt}\t{"differs" if miss else "found"}\t{"; ".join(miss)}')
    (ROOT / f'vol{vol}' / 'review' / 'user_readings_compare.tsv').write_text('\n'.join(rows) + '\n', encoding='utf8')
    print(f'user_readings_compare.tsv: {len(rows) - 1} readings, {nf} with references not found on that page of the new text')
