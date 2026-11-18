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
# --- suggestions: what a form probably is, with the reason; the user approves (Nov 18 2026: "you give your suggestions and I approve")
numshape = collections.defaultdict(collections.Counter)
for r in csv.DictReader(open(os.path.join(ROOT, 'CROSS_REFERENCES.tsv'), encoding='utf8'), delimiter='\t'):
    numshape[r['work']][len(re.split(r'[-–,]', r['number'].strip()))] += 1
def norm(x): return re.sub(r'[\s.]', '', x).lower()
listforms = {}
for f, r in lst.items():
    if r['status'] in ('legend', 'extra'):
        for g in f.split(' or '): listforms[g.strip()] = r
ALIAS = {'Kaṭha.': 'Ka. U.', 'Kaṭh.': 'Ka. U.', 'Kaṭha. U.': 'Ka. U.', 'Kar.': 'Ka. U.', 'kaṭha.': 'Ka. U.', 'Vā. Sū.': 'Pā. Sū.', 'vā. sū.': 'Pā. Sū.', 'Vai. Saṃ.': 'Mai. Saṃ.', 'Ait. Ār.': 'Ai. Ā.', 'Ait. Ā.': 'Ai. Ā.', 'Ait. Br.': 'Ai. Brā.', 'Pū. Mī.': 'Jai. Sū.', 'muṃ. uṃ.': 'Mu. U.', 'muṃ. u.': 'Mu. U.', 'ṛ. sa.': 'Ṛ. Saṃ.', 'pā. dū.': 'Pā. Sū.', 'pā. rū.': 'Pā. Sū.', 'pā. sava.': 'Pā. Sū.', 'pā. sā.': 'Pā. Sū.', 'Sā. Ve.': 'Sā. Saṃ.', 'Śata. Brā.': 'Śa. Brā.', 'Si.': 'Ni.', 'Ma. Saṃ.': 'Ṛ. Saṃ.', 'Mā. Saṃ.': 'Ṛ. Saṃ.', 'U.': 'U. Sū.', 'u.': 'U. Sū.', 'Ṛk. Saṃ.': 'Ṛ. Saṃ.', 'Ṛg. Saṃ.': 'Ṛ. Saṃ.', 'Ṛgve.': 'Ṛ. Saṃ.', 'Ṛ.': 'Ṛ. Saṃ.', 'Nir.': 'Ni.', 'Niru.': 'Ni.', 'Śat. Brā.': 'Śa. Brā.', 'Ś. Brā.': 'Śa. Brā.',
         'Ait. Brā.': 'Ai. Brā.', 'Ai. Br.': 'Ai. Brā.', 'Tai. Br.': 'Tai. Brā.', 'Āśv.': 'Ā. Sū.', 'Āś.': 'Ā. Sū.', 'Vāj. Saṃ.': 'Vā. Saṃ.', 'Uṇ.': 'U. Sū.', 'Uṇ. sū.': 'U. Sū.',
         'sā. sū.': 'Pā. Sū.', 'tā. sū.': 'Pā. Sū.', 'paṃ. sū.': 'Pā. Sū.', 'Av.': 'Ath. Saṃ.', 'Ṛ. Ve.': 'Ṛ. Saṃ.', 'Ā. Ve.': 'Ath. Saṃ.'}
def dev2iast(w):
    try:
        from indic_transliteration import sanscript
        return sanscript.transliterate(w, sanscript.DEVANAGARI, sanscript.IAST)
    except Exception: return ''
def suggest(w):
    """-> (suggested form, basis, confidence)"""
    base = w; note = ''
    if re.search('[\u0900-\u097f]', w):
        base = dev2iast(w).replace('ṁ', 'ṃ'); note = 'Devanagari read as ' + base + '; '
        if not base: return ('', 'cannot transliterate', 'none')
    if base in ('Ma.', 'ma.', 'M.'):
        sh = numshape.get(w, collections.Counter()); tt = sum(sh.values()) or 1; share = sum(v for k, v in sh.items() if k >= 3) / tt
        if w in ('M.', 'म.', 'Ma.', 'ma.'): return ('M.', note + 'user, Nov 18 2026: M. / म. / Ma. is the Mahābhāṣya on a Pāṇini sūtra', 'high')
        if share >= 0.8: return ('M.', note + f'Mahābhāṣya (user: M. / म.); {round(100 * share)}% of its numbers have 3-4 parts, the shape of sūtra and vārttika numbers (Ma. Bhā. is the Mahābhārata)', 'medium')
    if w == 'Pā. Ma.': return ('Pā. Sū.', note + 'user, Nov 18 2026: Pā. Ma. (and पा. म.) is Pāṇini sūtra', 'high')
    if re.search('[\u0900-\u097f]', w) and re.match(r'pā\. \S', base): return ('Pā. Sū.', note + 'user, Nov 18 2026: all पा. … forms are Pāṇini sūtra (the second word is a misreading of सू.)', 'high')
    if w in ('Pā. Mabhā.', 'Pā. Mā.', 'Pā. Rū.', 'Pā. Saṃ.', 'Pā. su.', 'Pā. sū. Ma.', 'Pā. sū. ma.', 'Pā. sū. vārtti.'): return ('Pā. Sū.', note + 'user, Nov 18 2026: "Pāṇini sūtra as well" (the second word is a misreading or names the vārttika / Mahābhāṣya)', 'high')
    key = base if base in listforms else None
    if key: return (key, note + 'the form of the list', 'high')
    if base == 'saṃ.' or (base != w and base == 'saṃ.'): return ('Ṛ. Saṃ.', note + 'user, Nov 18 2026: lower-case saṃ. (from ऋ/म सं.) is Ṛ. Saṃ.; NOT true for capital Saṃ.', 'medium')
    if base in ('U.', 'u.'): return ('U. Sū.', note + 'user decision, Nov 18 2026: bare U. / u. is U. Sū. (Uṇādi-sūtra)', 'high')
    if base in ALIAS: return (ALIAS[base], note + 'known spelling of ' + ALIAS[base], 'high')
    hit = [f for f in listforms if norm(f) == norm(base)]
    if hit: return (hit[0], note + 'same letters; only capitals, dots or spaces differ', 'high')
    hit = [f for f in ALIAS if norm(f) == norm(base)]
    if hit: return (ALIAS[hit[0]], note + 'known spelling of ' + ALIAS[hit[0]] + ' (capitals/dots differ)', 'high')
    words = [x for x in re.split(r'\s+', base.lower()) if x]
    cand = [f for f in listforms if [x.lower() for x in f.split()][:len(words)] == words and len(f.split()) > len(words)]
    if cand:
        shapes = numshape.get(w, collections.Counter()); tot = sum(shapes.values()) or 1
        if 'Pā. Sū.' in cand and shapes and sum(v for k, v in shapes.items() if k >= 3) / tot >= 0.8:
            return ('Pā. Sū.', note + f'short for Pā. Sū.; {round(100 * sum(v for k, v in shapes.items() if k >= 3) / tot)}% of its numbers have 3 parts (sūtra numbers); Pā. Śi. would have 1-2', 'medium')
        if len(words) == 1 and len(re.sub(r'[^\w]', '', words[0])) <= 2: return ('', note + 'too short to tell: could be ' + ' or '.join(cand[:4]), 'none')
        if len(cand) == 1: return (cand[0], note + 'short for ' + cand[0] + ' (the only list form that begins so)', 'medium')
        return ('', note + 'could be ' + ' or '.join(cand[:4]), 'none')
    return ('', note + 'no list form close to it', 'none')
appr = {}
if os.path.exists(os.path.join(ROOT, 'rv', 'reference_approvals.tsv')):
    for r in csv.DictReader(open(os.path.join(ROOT, 'rv', 'reference_approvals.tsv'), encoding='utf8'), delimiter='\t'): appr[r['form as written']] = r['approved form']
rows = []
for w, c in cnt.items():
    if re.search('[\u0900-\u097f]', w): st, mean = 'Devanagari', ''
    elif w in lst: st, mean = lst[w]['status'], lst[w]['work']
    else: st, mean = 'NOT IN LIST', ''
    sg = suggest(w) if st in ('NOT IN LIST', 'Devanagari') else ('', '', '')
    rows.append((st, w, mean, sum(c.values()), c, sg))
order = {'NOT IN LIST': 0, 'mistake': 1, 'extra': 2, 'legend': 3, 'Devanagari': 4}
rows.sort(key=lambda r: (order[r[0]], -r[3]))
with open(os.path.join(ROOT, 'REFERENCES_MASTER.tsv'), 'w', encoding='utf8') as o:
    o.write('status\tform as written\tmeaning / form to use\tsuggested form\tbasis\tconfidence\tapproved\ttotal\t' + '\t'.join(f'vol{v}' for v in vols) + '\n')
    for st, w, mean, tot, c, sg in rows: o.write('\t'.join([st, w, mean, sg[0], sg[1], sg[2], ('yes' if appr.get(w) == sg[0] and sg[0] else ''), str(tot)] + [str(c.get(v, '')) for v in vols]) + '\n')
by = collections.Counter(); ref = collections.Counter()
for st, w, mean, tot, c, sg in rows: by[st] += 1; ref[st] += tot
md = ['# Master list of reference abbreviations (all volumes)', '',
      '*Made by `python3 tools/rv/refs_master.py` from `CROSS_REFERENCES.tsv` and the one list `rv/references.tsv`. The full table, one row per form with its count in every volume, is `REFERENCES_MASTER.tsv`. Settle a form once in `rv/references.tsv` (status `mistake` and "→ form" to rewrite it, `extra` or `legend` for a work), then rebuild.*', '',
      '| status | forms | references |', '|---|---|---|'] + [f'| {k} | {by[k]} | {ref[k]} |' for k in ('NOT IN LIST', 'mistake', 'extra', 'legend', 'Devanagari') if k in by] + ['',
      '## Forms not in the list, most used first (first 60)', '', '| form | total | suggestion | volumes (count) |', '|---|---|---|---|']
for st, w, mean, tot, c, sg in rows:
    if st == 'NOT IN LIST' and len(md) < 80: md.append(f'| {w} | {tot} | {sg[0] or "?"} ({sg[2]}) | ' + ', '.join(f'{v} ({c[v]})' for v in sorted(c)) + ' |')
open(os.path.join(ROOT, 'REFERENCES_MASTER.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
print(dict(by), dict(ref))

# places of the forms with no suggestion (and not yet in the list): vol, printed page, line, number, text; for the user's reading (Nov 18 2026)
none = {w: (sg[1]) for st, w, mean, tot, c, sg in rows if st in ('NOT IN LIST', 'Devanagari') and sg[2] == 'none'}
tot_by = {w: tot for st, w, mean, tot, c, sg in rows}
places = [r for r in csv.DictReader(open(os.path.join(ROOT, 'CROSS_REFERENCES.tsv'), encoding='utf8'), delimiter='\t') if r['work'] in none]
places.sort(key=lambda r: (-tot_by[r['work']], r['work'], int(r['vol']), int(re.match(r'\d+', r['page']).group()) if re.match(r'\d+', r['page']) else -1, int(r['line']) if r['line'].isdigit() else 0))
with open(os.path.join(ROOT, 'REFERENCES_NONE_PLACES.tsv'), 'w', encoding='utf8') as o:
    o.write('form as written\tforms like it (why no suggestion)\ttotal uses\tvol\tprinted page\tline in the English file\tnumber after it\tyour reading (what it is)\ttext around it\n')
    for r in places: o.write('\t'.join([r['work'], none[r['work']], str(tot_by[r['work']]), r['vol'], r['page'], r['line'], r['number'], '', r['text'][:160].replace('\t', ' ')]) + '\n')
print(len(none), 'forms without suggestion;', len(places), 'places -> REFERENCES_NONE_PLACES.tsv')

# capital-S bare Saṃ. is NOT taken as Ṛ. Saṃ. (user, Nov 18 2026): its places are listed for reading, with the collection the line itself names if any
OTHER = re.compile(r'Yajus|Yajur|Ya Saṃ|Kāṭhaka|Kāvya|Śrī|Atharva|Ath\.|Taitt|Tai\.|Vāj|Maitr|Mai\.|Sāma|Sā\.', re.I)
with open(os.path.join(ROOT, 'REFERENCES_CAPITAL_SAM_PLACES.tsv'), 'w', encoding='utf8') as o:
    o.write('vol\tprinted page\tline\tnumber\tbare form\tthe line names another collection?\ttext around it\n')
    for r in csv.DictReader(open(os.path.join(ROOT, 'CROSS_REFERENCES.tsv'), encoding='utf8'), delimiter='\t'):
        if r['work'] == 'Saṃ.':
            hit = OTHER.search(r['text']); o.write('\t'.join([r['vol'], r['page'], r['line'], r['number'], r['work'], hit.group(0) if hit else '', r['text'][:170]]) + '\n')
