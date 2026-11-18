#!/usr/bin/env python3
"""The reference abbreviations in all three scripts (user, Nov 18 2026: every correction must be uniform in the Kannada book, the Devanagari lines and the English).

  python3 tools/rv/crossrefs.py && python3 tools/rv/refs_master.py && python3 tools/rv/refs_three.py

Writes REFERENCES_THREE_SCRIPTS.tsv (one row per work: English form, Kannada form, Devanagari form, and how often each script is found, summed over the
volumes) and REFERENCES_KANNADA_FORMS.tsv (every Kannada form found before a number in the Kannada text of every volume, with its counts and, where the list
knows it, the work it stands for).  Reads only; changes no volume.
The Devanagari form of a work is made from its English (IAST) form by the transliteration script, never typed; where the Sanskrit lines of the volumes
show another form for the same work ("seen") both are listed.  A Kannada form the list does not know is marked "?" for the user."""
import csv, os, re, collections, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit'))
from indic_transliteration import sanscript
lst = list(csv.DictReader(open(os.path.join(ROOT, 'rv', 'references.tsv'), encoding='utf8'), delimiter='\t'))
master = list(csv.DictReader(open(os.path.join(ROOT, 'REFERENCES_MASTER.tsv'), encoding='utf8'), delimiter='\t'))
def dev(en):
    d = sanscript.transliterate(en, sanscript.IAST, sanscript.DEVANAGARI)
    return re.sub(r'(\S)्\.', r'\1.', d)             # a bare consonant before the dot ("म्.") is written "म."
# --- English / Devanagari counts per work (from the master list): every form that reads as the work
canon = [r for r in lst if r['status'] in ('legend', 'extra')]
byform = {}
for r in canon:
    for f in r['english'].split(' or '): byform[f.strip()] = r
uses = collections.defaultdict(lambda: collections.Counter())
seen_dev = collections.defaultdict(collections.Counter)
mistake_to = {r['english']: r['work'][2:].strip() for r in lst if r['status'] == 'mistake' and r['work'].startswith('→ ')}
for r in master:
    f, tot = r['form as written'], int(r['total'] or 0)
    target = None
    if r['status'] in ('legend', 'extra') and f in byform: target = f
    elif r['status'] == 'mistake' and f in mistake_to: target = mistake_to[f]
    elif r['suggested form'] and r['status'] in ('NOT IN LIST', 'Devanagari'): target = r['suggested form']
    if target is None: continue
    script = 'dev' if re.search('[ऀ-ॿ]', f) else 'en'
    uses[target][script] += tot
    if script == 'dev': seen_dev[target][f] += tot
# --- the Kannada text of every volume
KD = '೦೧೨೩೪೫೬೭೮೯'
KN = '[' + KD + ']+'
KREF = re.compile(r'((?:[ಀ-೿]{1,6}\.\s?){1,3})\s*(' + KN + r'(?:\s?[-–]\s?' + KN + r'){1,4})')
kcount = collections.defaultdict(collections.Counter)
for v in range(1, 19):
    for p in (f'vol{v}/Rigveda_Samhita_Vol{v}_Kannada_Text.md', f'vol{v}/html/rig_{v}.md'):
        fp = os.path.join(ROOT, p)
        if os.path.exists(fp):
            for l in open(fp, encoding='utf8'):
                for m in KREF.finditer(l): kcount[re.sub(r'\s+', ' ', m.group(1)).strip()][v] += 1
            break
klist = {}                                                   # Kannada form -> English form of the work
for r in lst:
    k = (r['kannada'] or '').strip()
    if not k: continue
    tgt = r['english'] if r['status'] in ('legend', 'extra') else (r['work'][2:].strip() if r['work'].startswith('→ ') else '')
    for kk in re.split(r'\s+ಅಥವಾ\s+', k): klist[kk.strip()] = tgt
def nrm(x): return re.sub(r'[\s.]', '', x).lower().replace('ē', 'e').replace('ō', 'o').replace('ṁ', 'ṃ')
decided = {}                                                  # normalised form (any script, as IAST) -> the form the user's decisions give
for r in master:
    f = r['form as written']
    if r['status'] in ('legend', 'extra'): tgt = f
    elif r['status'] == 'mistake': tgt = mistake_to.get(f, '')
    else: tgt = r['suggested form']
    if not tgt: continue
    iast = sanscript.transliterate(f, sanscript.DEVANAGARI, sanscript.IAST) if re.search('[\u0900-\u097f]', f) else f
    decided.setdefault(nrm(iast), tgt)
def by_decision(k):
    iast = sanscript.transliterate(k, sanscript.KANNADA, sanscript.IAST)
    return decided.get(nrm(iast), '')
with open(os.path.join(ROOT, 'REFERENCES_KANNADA_FORMS.tsv'), 'w', encoding='utf8') as o:
    o.write('Kannada form\ttotal\tstands for (English form of the work)\tstatus\t' + '\t'.join(f'vol{v}' for v in range(1, 19)) + '\n')
    for k, c in sorted(kcount.items(), key=lambda kv: -sum(kv[1].values())):
        tgt = klist.get(k, ''); st = 'in the list' if tgt else '?'
        if not tgt:
            d = by_decision(k)
            if d: tgt, st = d, 'by the decisions made for the English / Devanagari form of the same letters'
        o.write('\t'.join([k, str(sum(c.values())), tgt, st] + [str(c.get(v, '')) for v in range(1, 19)]) + '\n')
kuse = collections.Counter()
for k, c in kcount.items():
    t = klist.get(k)
    if t: kuse[t] += sum(c.values())
with open(os.path.join(ROOT, 'REFERENCES_THREE_SCRIPTS.tsv'), 'w', encoding='utf8') as o:
    o.write('work\tstatus\tEnglish form\tKannada form\tDevanagari form (made by script)\tDevanagari forms seen in the text\tuses: English\tuses: Devanagari\tuses: Kannada\tto settle\n')
    for r in canon:
        en = r['english']; k = (r['kannada'] or '').strip(); d = dev(en.split(' or ')[0].strip())
        seen = ', '.join(f'{f} ({n})' for f, n in seen_dev[en.split(' or ')[0].strip()].most_common(4))
        todo = []
        if not k: todo.append('Kannada form missing')
        if seen and d not in seen: todo.append('Devanagari form made differs from the one seen')
        o.write('\t'.join([r['work'], r['status'], en, k, d, seen, str(uses[en.split(' or ')[0].strip()]['en']), str(uses[en.split(' or ')[0].strip()]['dev']), str(kuse.get(en, '')), '; '.join(todo)]) + '\n')
unk = [(k, sum(c.values())) for k, c in kcount.items() if k not in klist and not by_decision(k)]
print(len(canon), 'works;', len(kcount), 'Kannada forms,', len(unk), 'not in the list (', sum(n for k, n in unk), 'uses )')
