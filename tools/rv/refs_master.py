#!/usr/bin/env python3
"""Master list of reference abbreviations: every form of a work as written in the English file of every volume, with the count per volume and its
standing in the one list (rv/references.tsv).  Writes REFERENCES_MASTER.tsv and REFERENCES_MASTER.md at the root.  Reads only; changes no volume.

  python3 tools/rv/crossrefs.py && python3 tools/rv/refs_master.py

Input: CROSS_REFERENCES.tsv (made by crossrefs.py from the English file of each volume) and rv/references.tsv.  Status of a form: legend (the edition's
own list), extra (in our list, not in the edition's legend), mistake (decided misreading; shows the form to use), NOT IN LIST (to be decided), Devanagari
(the Sanskrit form of a citation, not an abbreviation of ours).  User, Nov 18 2026: one place to see all references per volume, to settle forms once for all volumes."""
import csv, os, re, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
lst = {r['english']: r for r in csv.DictReader(open(os.path.join(ROOT, 'rv', 'references.tsv'), encoding='utf8'), delimiter='\t')}
cnt = collections.defaultdict(collections.Counter)
for r in csv.DictReader(open(os.path.join(ROOT, 'CROSS_REFERENCES.tsv'), encoding='utf8'), delimiter='\t'): cnt[r['work']][int(r['vol'])] += 1
vols = sorted({v for c in cnt.values() for v in c})
rows = []
for w, c in cnt.items():
    if re.search('[ऀ-ॿ]', w): st, mean = 'Devanagari', ''
    elif w in lst: st, mean = lst[w]['status'], lst[w]['work']
    else: st, mean = 'NOT IN LIST', ''
    rows.append((st, w, mean, sum(c.values()), c))
order = {'NOT IN LIST': 0, 'mistake': 1, 'extra': 2, 'legend': 3, 'Devanagari': 4}
rows.sort(key=lambda r: (order[r[0]], -r[3]))
with open(os.path.join(ROOT, 'REFERENCES_MASTER.tsv'), 'w', encoding='utf8') as o:
    o.write('status\tform as written\tmeaning / form to use\ttotal\t' + '\t'.join(f'vol{v}' for v in vols) + '\n')
    for st, w, mean, tot, c in rows: o.write('\t'.join([st, w, mean, str(tot)] + [str(c.get(v, '')) for v in vols]) + '\n')
by = collections.Counter(); ref = collections.Counter()
for st, w, mean, tot, c in rows: by[st] += 1; ref[st] += tot
md = ['# Master list of reference abbreviations (all volumes)', '',
      '*Made by `python3 tools/rv/refs_master.py` from `CROSS_REFERENCES.tsv` and the one list `rv/references.tsv`. The full table, one row per form with its count in every volume, is `REFERENCES_MASTER.tsv`. Settle a form once in `rv/references.tsv` (status `mistake` and "→ form" to rewrite it, `extra` or `legend` for a work), then rebuild.*', '',
      '| status | forms | references |', '|---|---|---|'] + [f'| {k} | {by[k]} | {ref[k]} |' for k in ('NOT IN LIST', 'mistake', 'extra', 'legend', 'Devanagari') if k in by] + ['',
      '## Forms not in the list, most used first (first 60)', '', '| form | total | volumes (count) |', '|---|---|---|']
for st, w, mean, tot, c in rows:
    if st == 'NOT IN LIST' and len(md) < 80: md.append(f'| {w} | {tot} | ' + ', '.join(f'{v} ({c[v]})' for v in sorted(c)) + ' |')
open(os.path.join(ROOT, 'REFERENCES_MASTER.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
print(dict(by), dict(ref))
