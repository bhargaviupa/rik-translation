#!/usr/bin/env python3
"""List every reference to another text in the English file of every volume: CROSS_REFERENCES.tsv and CROSS_REFERENCES.md at the root (user, Nov 17 2026).

  python3 tools/rv/crossrefs.py            # all volumes that have an English file
  python3 tools/rv/crossrefs.py 2 7        # only these (the root files then hold only these)

A reference = an abbreviation of a work followed by a number of two or more parts ("Ṛ. Saṃ. 1-164-47", "पा. सू. ६-१-५", "Ni. 10-14").
One row per reference and line: the Devanagari form, its transliterated twin and the English form of the same reference on one line count once.
Reads only; changes no volume.  Columns: vol, page, line, kind (rik | grammar | other), work (as written), number, gloss (labelled gloss or
GLOSS marker on this or the next two lines), text (the line, shortened)."""
import re, sys, os, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit'))
from add_iast import deva_to_iast
DIG = str.maketrans('०१२३४५६७८९೦೧೨೩೪೫೬೭೮೯', '01234567890123456789')
N = r'(?:\d+|[०-९]+|[೦-೯]+)'
LAT = r'[A-Za-zĀāĪīŪūṚṛṢṣṆṇṬṭḌḍŚśṃḥṄṅñ]'
WORD = r'(?:' + LAT + r'{1,7}|[ऀ-ॿ]{1,5}|[ಀ-೿]{1,5})'
SEP = r'(?:\.\.|[.,-])?\s'                       # after a word of the work's name the dot may be missing or replaced by "-", ","  (e.g. "पा सू.", "पा- सू.")
# a work name = 1-4 words, the last one with its dot, then a number of 2-4 parts joined by "-" (also "." or a space where the print or the machine slipped)
DEVW = r'(?:[ऀ-ॿ]{1,5}|[ಀ-೿]{1,5})'
NUM = N + r'(?:(?:\s?[-–]\s?|\.(?=' + N + r')|\s(?=' + N + r'{2,}))' + N + r'){1,4}'
REF = re.compile(r'((?:' + LAT + r'{1,7}\.\s?){1,3}|(?:[ऀ-ॿ]{1,5}\.\s?){1,3}|(?:[ಀ-೿]{1,5}\.\s?){1,3})\s*[“"\']?(' + NUM + ')')
# the work's name in Indic script right after "(" may lack the dot of its first word ("(पा सू. ७-१-३९)", "(पा- सू. …", "(उ सू. …", "(पं- सू. …"): read as the full name
REFB = re.compile(r'[(\[]\s?((?:' + DEVW + r'(?:\.\.|[.,-])?\s){1,2}' + DEVW + r'\.\s?)\s*(' + NUM + ')')
PAGE = re.compile(r'^#{2,4} .*?(?:[Pp]age|[Pp]\.|[Pp]ages|[Pp]p\.)\s*([0-9]+|[ivxlc]+)\b')
GLOSS = re.compile(r'\*\*GLOSS\*\*|\b[Gg]loss(?:es)?\b[^.]{0,30}:|mine and tentative|\(mine\)|— mine\b')
STOP = {'p', 'pp', 'no', 'nos', 'vol', 'vols', 'cf', 'c', 'e', 'g', 'i', 'viz', 'pdf', 'fig', 'ca', 'a', 'b', 'd', 'ch', 'st', 'dpi', 'ie', 'eg', 'etc'}
def normlab(x):
    # words of the name each followed by '. ' (missing dots, '-', ',' and doubled dots made regular); nothing is read from memory
    ws = re.findall(WORD, x)
    return ' '.join(w + '.' for w in ws)
def key(lab):
    s = lab.strip()
    if re.search('[ऀ-ॿ]', s): s = deva_to_iast(s)
    return re.sub(r'[^a-zāīūṛṣṇṭḍśṃḥṅñ]', '', s.lower())
def kind(k):
    if re.match(r'(ṛsa[ṃm]?|ṛgve|ṛksa[ṃm]|ṛks|rv|masa[ṃm]|ṛ$)', k): return 'rik'
    if re.match(r'(pā|uṇ|us[ūu]|u$|phi|vā$|vār|pari|gaṇa|dhā|si[dk])', k): return 'grammar'
    return 'other'
def run(vols):
    rows = []; summ = collections.OrderedDict()
    for v in vols:
        p = os.path.join(ROOT, f'vol{v}', f'Rigveda_Samhita_Vol{v}_English_Translation.md')
        if not os.path.exists(p): continue
        L = open(p, encoding='utf8').read().split('\n'); page = ''; c = collections.Counter()
        for i, l in enumerate(L):
            m = PAGE.match(l)
            if m: page = m.group(1); continue
            seen = set()
            ms = list(REFB.finditer(l)); starts = {m.start(2) for m in ms}
            ms += [m for m in REF.finditer(l) if m.start(2) not in starts]; ms.sort(key=lambda m: m.start(2))
            for m in ms:
                lab = re.sub(r'\s*(\.\.|[.,-])?\s+', lambda mm: '. ', re.sub(r'\s+', ' ', m.group(1)).strip() + ' ').strip() if False else normlab(m.group(1)); k = key(lab)
                if not k or k in STOP or re.search('[ಀ-೿]', lab) and not k: continue
                num = re.sub(r'\s?[–-]\s?|(?<=\d)[.\s](?=\d)', '-', m.group(2).translate(DIG))
                kd = kind(k)
                if (kd, num) in seen: continue                      # the same reference in another script on the same line
                seen.add((kd, num))
                g = 'gloss' if any(GLOSS.search(x) for x in L[i:i + 3]) else ''
                a = max(0, m.start() - 70); txt = re.sub(r'\s+', ' ', l[a:m.end() + 70]).replace('\t', ' ')
                rows.append((v, page, i + 1, kd, lab, num, g, txt)); c[kd] += 1; c['gloss'] += bool(g)
        summ[v] = c
    with open(os.path.join(ROOT, 'CROSS_REFERENCES.tsv'), 'w', encoding='utf8') as f:
        f.write('vol\tpage\tline\tkind\twork\tnumber\tgloss\ttext\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    with open(os.path.join(ROOT, 'CROSS_REFERENCES.md'), 'w', encoding='utf8') as f:
        f.write('# Cross-references in all volumes\n\n*Made by `python3 tools/rv/crossrefs.py` from the English file of each volume; run it again after any change. '
                'The list itself is `CROSS_REFERENCES.tsv` (one row per reference: volume, page, line, kind, work, number, gloss, text). Nothing here is typed by hand.*\n\n'
                '- **rik**: a verse of the Ṛgveda-saṃhitā quoted from elsewhere (its gloss is to come from our own edition, requirement B3.5).\n'
                '- **grammar**: Pāṇini, Uṇādi and the other grammatical sūtras.\n- **other**: Nirukta, Brāhmaṇas, Upaniṣads, Sūtras and the rest.\n'
                '- **with a gloss or marker**: references with a labelled gloss or a `**GLOSS**` marker on the same or the next two lines.\n\n'
                '| Vol | rik | grammar | other | all | with a gloss or marker |\n|---|---|---|---|---|---|\n')
        t = collections.Counter()
        for v, c in summ.items():
            f.write(f"| {v} | {c['rik']} | {c['grammar']} | {c['other']} | {c['rik'] + c['grammar'] + c['other']} | {c['gloss']} |\n"); t.update(c)
        f.write(f"| **all** | {t['rik']} | {t['grammar']} | {t['other']} | {t['rik'] + t['grammar'] + t['other']} | {t['gloss']} |\n\n"
                '**Limits.** A reference is found only where a work\'s abbreviation stands before a number of two or more parts; a quotation without a number, '
                'a reference written in words ("the next Ṛk", "Rik 9 of this sūkta") and a number whose abbreviation was misread beyond recognition are not listed. '
                'The kind is decided from the abbreviation as written; misread abbreviations fall under "other". Vol 13 is not translated; Vol 19 is in translation.\n')
    print(f'{len(rows)} references in {len(summ)} volumes; rik {t["rik"]}, grammar {t["grammar"]}, other {t["other"]}; with a gloss or marker {t["gloss"]}')
if __name__ == '__main__':
    run([int(x) for x in sys.argv[1:]] or list(range(1, 30)))
