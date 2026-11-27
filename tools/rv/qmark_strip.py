#!/usr/bin/env python3
"""Clear `[?]` marks that need no reading of the Kannada (shared tool; Vol 10 first, Nov 27 2026, user: "if you cannot resolve the ? marks the second pass is of no use").

  python3 tools/rv/qmark_strip.py VOL [--write] [--samples N]

Classes (every mark of the English file falls in exactly one; dry run by default, prints counts and N samples per class):
  BLOCK   the mark stands on a blockquote line (`> ...`: the Saṃhitā, Pada and Sāyaṇa-bhāṣya blocks, Devanagari or IAST twin). These blocks come from the
          Wikisource reference (REQUIREMENTS B1.2, K9) and the English file's Sanskrit is derived data, so a doubt about the old reading is moot: ` [?]` is removed.
  BARE    a whole-line remark of ours (starts `*(`, `(`, `*[`) that has no digit and no Kannada letter and speaks only of doubtful/small-type/image readings
          (boilerplate): the whole line is removed (B4.1: nothing of ours in the text).
  NUMREAD (and NUMOK, see code) a reference whose doubtful form is followed by the old reader's own reading `as read "೧-೧೦"` (Kannada digits): when the supplied Kannada of the page (and its
          neighbours) has exactly that reference, the whole doubtful form, the `as read` and its marks become the reference in Latin figures (numbers are taken from the Kannada).
  OTHER   everything else (prose, tables, remarks with a number or a word): left for a reader; listed.
--write applies BLOCK, BARE and NUMREAD and logs one summary line per class (and every removed BARE line) in volN/review/repair_log.md and volN/review/qmark_strip_removed.tsv."""
import os, re, sys, datetime, collections, random
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
vol = sys.argv[1]; write = '--write' in sys.argv
ns = int(sys.argv[sys.argv.index('--samples') + 1]) if '--samples' in sys.argv else 6
p = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md')
L = open(p, encoding='utf8').read().split('\n')
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
kn = open(os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md'), encoding='utf8').read()
KP = {int(m.group(1)): m.group(2) for m in re.finditer(r'<!-- printed (\d+)(?::[^>]*)? -->(.*?)(?=<!-- printed |\Z)', kn, re.S)}
def refs_of(pg):
    s = ''.join(KP.get(q, '') for q in (pg - 1, pg, pg + 1)).translate(KD)
    return set(re.sub(r'\s*[-.:–]\s*', '-', x) for x in re.findall(r'\d+(?:\s*[-.:–]\s*\d+)+', s))
NUMREAD = re.compile(r'(?P<name>(?:[A-ZĀṚŚ][^\s()\[\]]*\.?\s?){1,3})(?P<num>(?:\d|\[\?\]|-|–)+)[,;]?\s*\(?(?:as read|as printed|read) "(?P<kn>[೦-೯0-9][೦-೯0-9\-–]*)"(?:\s*\[\?\])?\)?')
DIG = re.compile(r'[0-9೦-೯०-९]'); KNS = re.compile('[ಀ-೿]')
BOIL = re.compile(r'doubtful|small type|small-type|read from the (?:image|print|zoom)|zoom|OCR|not settled|glyph|as read|as printed|uncertain|cannot read|illegible', re.I)
def is_remark(l):
    s = l.lstrip(); return s.startswith('*(') or s.startswith('(') or s.startswith('*[') or s.startswith('[')
# NUMOK: a complete reference (no mark inside) followed only by a doubt clause `as printed [?]` / `[as read, [?]]`; when the Kannada pages have that very reference, only the clause goes.
NUMOK = re.compile(r'(?P<name>(?:[A-ZĀṚŚ][^\s()\[\]]*\.?\s?){1,3})(?P<num>\d+(?:-\d+)+)(?P<cl>,?\s*(?:\[\s*)?(?:as read|as printed)(?:,?\s*\[\?\])?(?:\s*\])?)(?=[\s)\]*.,;]|$)')
page = None; newL = list(L); nr = 0; nr_rows = []
for i, l in enumerate(L):
    m = re.match(r'### (?:Page|Printed p\.) (\d+)\b', l)
    if m: page = int(m.group(1))
    if '[?]' not in l or page is None or l.lstrip().startswith('>'): continue
    R = refs_of(page)
    def sub(mm):
        global nr
        kref = re.sub(r'\s*[-–]\s*', '-', mm.group('kn').translate(KD))
        if kref in R:
            nr += 1; nr_rows.append((i + 1, mm.group(0), mm.group('name') + kref)); return mm.group('name') + kref
        return mm.group(0)
    def sub2(mm):
        global nr
        if '[?]' in mm.group('cl') and mm.group('num') in R:
            nr += 1; nr_rows.append((i + 1, mm.group(0), mm.group('name') + mm.group('num'))); return mm.group('name') + mm.group('num')
        return mm.group(0)
    newL[i] = NUMOK.sub(sub2, NUMREAD.sub(sub, l))
L0 = L; L = newL
cls = {}; cnt = collections.Counter(); ex = collections.defaultdict(list)
for i, l in enumerate(L):
    k = l.count('[?]')
    if not k: continue
    if l.lstrip().startswith('>'):
        t = l.lstrip('> ').strip()    # Vol 8 (Nov 27 2026): only the Sanskrit lines (Devanagari, italic IAST) and digit-free remarks are moot; an English line of a block (a translation) or a reference line with a number is left for a reader
        if re.search('[\u0900-\u097F]', t) or (t.startswith('*') and not t.startswith('*(')): c = 'BLOCK'
        elif (t.startswith('(') or t.startswith('*(')) and not DIG.search(t): c = 'BLOCK'
        else: c = 'OTHER'
    elif is_remark(l) and not DIG.search(l) and not KNS.search(l) and BOIL.search(l) and len(l) < 260 and not re.search(r'Sense|Gist|Translation|means|meaning|GLOSS|\[sic', l): c = 'BARE'   # a **GLOSS** marker or a [sic] stays (user, Nov 24 2026; Vol 8 lost 15 GLOSS markers by this class and got them back)
    else: c = 'OTHER'
    cls[i] = c; cnt[c] += k; ex[c].append(i)
print(f'NUMREAD: {nr} places settled from the Kannada page; marks left after it:', sum(l.count('[?]') for l in L), 'of', sum(l.count('[?]') for l in L0))
print(f'Vol {vol}: {sum(cnt.values())} marks on {len(cls)} lines;', ', '.join(f'{c} {cnt[c]} ({len(ex[c])} lines)' for c in ('BLOCK', 'BARE', 'OTHER')))
random.seed(5)
print('== NUMREAD samples')
for n, a, b in random.sample(nr_rows, min(ns, len(nr_rows))): print(f'  {n}: {a!r} -> {b!r}')
for c in ('BLOCK', 'BARE', 'OTHER'):
    print(f'== {c}')
    for i in random.sample(ex[c], min(ns, len(ex[c]))):
        l = L[i]; m = l.find('[?]'); print(f'  {i+1}: ' + (l[:200] if c == 'BARE' else l[max(0, m - 70):m + 50]).replace('\n', ' '))
if write:
    out = []; rm = []; today = datetime.date.today().isoformat()
    for i, l in enumerate(L):
        c = cls.get(i)
        if c == 'BARE': rm.append((i + 1, l)); continue
        if c == 'BLOCK': l = re.sub(r' ?\[\?\]', '', l)
        out.append(l)
    open(p, 'w', encoding='utf8').write('\n'.join(out))
    d = os.path.join(ROOT, f'vol{vol}', 'review'); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'qmark_strip_removed.tsv'), 'a', encoding='utf8') as f:
        for n, l in rm: f.write(f'{today}\tBARE\t{n}\t{l.replace(chr(9), " ")}\n')
    with open(os.path.join(d, 'repair_log.md'), 'a', encoding='utf8') as f:
        f.write(f'\n### {today} qmark_strip.py: BLOCK {cnt["BLOCK"]} marks removed from {len(ex["BLOCK"])} Sanskrit-block lines (derived data, K9); BARE {len(rm)} boilerplate remark lines removed ({cnt["BARE"]} marks); OTHER {cnt["OTHER"]} marks left\n')
    print('written')
