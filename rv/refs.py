"""`rv refs N`: the one list of works and abbreviations (rv/references.tsv; requirement B3) against a volume.
Every abbreviation that stands before a reference number in the English of the units is looked up; the report says which are in the list,
which are known mistakes, and which the list does not have.  It also prints docs/REFERENCES.md from the list."""
import re, os, csv, collections
from .common import *
RX = re.compile(r'((?:[A-ZĀĪŪṚŚṢÑ][A-Za-zāīūṛṃḥṇṭḍśṣñ]{0,6}\.\s?){1,4})\s?(\d+(?:[-–.]\d+)*)')

def load():
    rows = list(csv.DictReader(open(os.path.join(ROOT, 'rv', 'references.tsv'), encoding='utf8'), delimiter='\t')); return rows

def write_doc(rows):
    out = ['# Works cited and their abbreviations — the one list for all volumes', '',
           '*Printed from `rv/references.tsv` by `python3 -m rv refs N`; edit the list, not this page. Requirement B3 of `docs/REQUIREMENTS.md`.*', '',
           '## 1. The legend of the Kannada edition', '', '| Used in the English | Printed in the edition | Work |', '|---|---|---|']
    out += [f"| {r['english']} | {r['kannada']} | {r['work']} |" for r in rows if r['status'] == 'legend']
    out += ['', '## 2. Used in the volumes but not in the edition\'s legend (expansions to be confirmed by the editor)', '', '| Used in the English | Kannada form | Work |', '|---|---|---|']
    out += [f"| {r['english']} | {r['kannada']} | {r['work']} |" for r in rows if r['status'] == 'extra']
    out += ['', '## 3. Known and suspected mistakes (of the machine reading, the print, or the translation)', '', '| Form met | Kannada form | Stands for | Note |', '|---|---|---|---|']
    out += [f"| {r['english']} | {r['kannada']} | {r['work'].replace('→ ', '')} | {r['note']} |" for r in rows if r['status'] == 'mistake']
    out += ['', 'A form marked "?" or "to confirm" is not corrected anywhere until the editor decides; it is only reported.']
    open(os.path.join(ROOT, 'docs', 'REFERENCES.md'), 'w', encoding='utf8').write('\n'.join(out) + '\n')

def run(vol):
    rows = load(); write_doc(rows); known = {}
    for r in rows:
        for form in re.split(r'\s+or\s+', r['english']): known[form.strip()] = r['status']
    c = collections.Counter()
    for u in load_units(vol):
        for it in u.get('en', []):
            if it[0] == 'text':
                for m in RX.finditer(it[1]): c[re.sub(r'\s+', ' ', m.group(1)).strip()] += 1
    by = collections.Counter(); unknown = []; mist = []
    for form, n in c.most_common():
        stt = known.get(form)
        if stt in ('legend', 'extra'): by[stt] += n
        elif stt == 'mistake': by['mistake'] += n; mist.append(f'{form} ({n})')
        else: by['not in the list'] += n; unknown.append(f'{form} ({n})')
    rep = [f'# Vol {vol}: abbreviations against the one list (rv refs)', '', f'References found in the English of the units: {sum(c.values())}, in {len(c)} different forms.',
           f'- in the edition\'s legend: {by["legend"]}', f'- in the list, not in the legend: {by["extra"]}', f'- known or suspected mistakes: {by["mistake"]}: ' + ', '.join(mist),
           f'- forms the list does not have: {by["not in the list"]}: ' + ', '.join(unknown[:60])]
    P = vol_paths(vol); open(os.path.join(P['review'], 'references_report.md'), 'w', encoding='utf8').write('\n'.join(rep) + '\n'); print('\n'.join(rep))
