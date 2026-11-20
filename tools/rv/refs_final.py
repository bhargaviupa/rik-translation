#!/usr/bin/env python3
"""The final list: one work, ONE form, in the three scripts (user, Nov 19-20 2026: "one book is referenced in one way ONLY").
Made from rv/references.tsv (legend + extra rows) with the user's decisions applied: more complete variant wins, no "or" forms, duplicates merged.
  python3 tools/rv/refs_final.py   -> REFERENCES_FINAL.tsv and REFERENCES_FINAL.md (a proposal for the user; rv/references.tsv itself is not changed here)."""
import csv, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
from indic_transliteration import sanscript
lst = list(csv.DictReader(open(os.path.join(ROOT, 'rv', 'references.tsv'), encoding='utf8'), delimiter='\t'))
three = {r['English form']: r for r in csv.DictReader(open(os.path.join(ROOT, 'REFERENCES_THREE_SCRIPTS.tsv'), encoding='utf8'), delimiter='\t')} if os.path.exists(os.path.join(ROOT, 'REFERENCES_THREE_SCRIPTS.tsv')) else {}
def dev(en):
    d = sanscript.transliterate(en, sanscript.IAST, sanscript.DEVANAGARI); return re.sub(r'(\S)्\.', r'\1.', d)
# decisions: english form in the list -> (final English, final Kannada or None = keep, merged-into note)
RENAME = {'Ā. Sū. or Ā.': ('Ā. Sū.', 'ಆ. ಸೂ.'), 'Phi. or Phi. Sū.': ('Phi. Sū.', 'ಫಿ. ಸೂ.'), 'Jai. Sū.': ('Jai. Pū. Sū.', 'ಜೈ. ಪೂ. ಸೂ.')}
MERGE = {'A. Ve.': 'Ath. Saṃ.', 'Pa. Brā.': 'Tā. Brā.', 'Uṇ. Sū.': 'U. Sū.', 'Īśa.': 'Īśa U.', 'Śā. Bhā.': 'Śa. Bhā.'}
GUESS = {'Kā.', 'M.', 'Sāṃ. Gṛ. Sū.', 'Vāl.', 'Anu.', 'Dhā.', 'Ṛgvi.', 'Piṅ.', 'Pā. Gṛ. Sū.', 'Pā. Sū. Vā.', 'Mu. U. Śa. Bhā.', 'Ya Saṃ.', 'Ṛ. Saṃ. Bhā.', 'Tai. Saṃ. Bha. Bhā.', 'Ai. U. Śa. Bhā.', 'Tai. U. Śa. Bhā.', 'Śa. Bhā. Bra. Sū.', 'Kau. Brā.', 'Ka. U.', 'Pa. Brā.', 'Mā. Gṛ. Sū.'}
GIVEN = {'Tai. U.', 'Kau. U.', 'Pra. U.', 'Īśa U.', 'Ke. U.', 'Mā. U.', 'Śa. Bhā.', 'Bṛ. De.'}
out = []
for r in lst:
    if r['status'] not in ('legend', 'extra'): continue
    en = r['english']
    if en in MERGE: continue
    k = r['kannada']; note = ''
    if en in RENAME: en, k = RENAME[en]; note = 'more complete form of the print'
    src = 'edition legend' if r['status'] == 'legend' else ('given by the user in Kannada' if en in GIVEN else ('MY GUESS: to confirm' if en in GUESS else 'earlier list (not confirmed)'))
    t = three.get(r['english'], {})
    out.append(dict(en=en, kn=k, dv=dev(en), work=r['work'].replace(' (the legend has U. Sū.)', ''), src=src, uses=(t.get('uses: English') or '0'), note=note))
merged = {a: b for a, b in MERGE.items()}
with open(os.path.join(ROOT, 'REFERENCES_FINAL.tsv'), 'w', encoding='utf8') as o:
    o.write('English (the one form)\tKannada\tDevanagari (made by script)\twork\tKannada form comes from\tuses in the English text now\tnote\n')
    for x in out: o.write('\t'.join([x['en'], x['kn'], x['dv'], x['work'], x['src'], x['uses'], x['note']]) + '\n')
md = ['# Final list of references: one work, one form (PROPOSAL, Nov 20 2026)', '', f'{len(out)} works. Made by `python3 tools/rv/refs_final.py` from `rv/references.tsv` with the decisions of Nov 19–20 applied.', '',
      'Merged (the left form disappears, every volume and script gets the right one): ' + '; '.join(f'{a} → {b}' for a, b in merged.items()) + '.', '',
      '| English | Kannada | Devanagari | Work | Kannada from |', '|---|---|---|---|---|'] + [f"| {x['en']} | {x['kn']} | {x['dv']} | {x['work']} | {x['src']} |" for x in out]
open(os.path.join(ROOT, 'REFERENCES_FINAL.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
import collections; print(len(out), 'works', dict(collections.Counter(x['src'] for x in out)))
