#!/usr/bin/env python3
"""Settle NUMBERS and WORDS of transcribed Saṃhitā and Pada blocks against the Wikisource reference (refs/wikisource/index/ws.sqlite).

  python3 tools/rv/ref_verify.py DIR --mandala 7 [--report OUT.tsv] [--write LOG.tsv]
DIR: pdfN.md page files (PDF page order; consecutive pages form one text, so a block may continue over a page break).

Method. Every Pada block (label ಪದಪಾಠಃ) is matched to the closest reference Ṛk of the mandala (normalised Devanagari, rapidfuzz ratio; below 80 the block is
reported 'noref' and nothing is changed). The matched Ṛk fixes the VERSE NUMBER: the number printed in '॥ N ॥' at the end of the Pada block (and of the
Saṃhitā block just before it, which stands for the same Ṛk) must equal the Ṛk's number: otherwise it is replaced (kind 'number'). Words: the block's
words are aligned with the reference words (difflib); every difference (kind 'check') is only REPORTED, for the page image to decide: Wikisource has its own
typos and the print has misprints, so a word is never replaced by script.
Nothing is changed without --write; with --write the changes are applied to the page files and every change is a row of LOG.tsv
(pdf, kind, was, now, rik). The reference is Wikisource's text: its own typos exist (docs/WIKISOURCE_NOTES.md), so only differences of <= 2 letters are applied and each is logged."""
import re, sys, glob, os, sqlite3, difflib, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'publish' / 'tools' / 'translit'))
from rapidfuzz import fuzz, process
from rapidfuzz.distance import Levenshtein
import pratipada_check as P
from deva_to_kannada import deva2kn
KN = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789'); KNDIG = '೦೧೨೩೪೫೬೭೮೯'
args = sys.argv[1:]
def opt(name):
    if name in args:
        i = args.index(name); v = args[i+1]; del args[i:i+2]; return v
mand = [int(x) for x in (opt('--mandala') or '7').split(',')]; report = opt('--report'); wlog = opt('--write')
d = args[0]
pages = {int(re.search(r'pdf(\d+)\.md', f).group(1)): f for f in glob.glob(os.path.join(d, 'pdf*.md'))}
con = sqlite3.connect(P.DB)
REF = []        # (ref 'm.s.r', r, norm pada words, norm samhita words, plain pada words, plain samhita words)
for ref, r, pada, sam in con.execute('select ref,r,pada,samhita from rik where m in (%s) order by m,s,r' % ','.join('?'*len(mand)), mand):
    pw = P.words(pada or ''); sw = P.words(re.sub(r'॥.*', '', sam or '').replace('ॐ', ''))
    REF.append((ref, r, [P.norm(w) for w in pw], [P.norm(w) for w in sw], pw, sw))
PADA_STR = [' '.join(x[2]) for x in REF]
LABEL = re.compile(r'^\s*(ಸಂಹಿತಾಪಾಠಃ?|ಪದಪಾಠಃ?|ಸಾಯಣಭಾಷ್ಯಂ|ಪ್ರತಿಪದಾರ್ಥ|ಭಾವಾರ್ಥ|ವಿಶೇಷವಿಷಯಗಳು|English Translation)')
NUMRE = re.compile(r'॥\s*([0-9೦-೯]{1,3})(?:\s*\[\?\])?\s*॥')
def kn_words(line):
    return [w for w in re.split(r'\s*\|\s*|\s+', line.strip()) if w and not NUMRE.fullmatch(w) and w not in ('॥', '।')]
changes = []; rows = []
texts = {n: open(f, encoding='utf8').read() for n, f in pages.items()}
def blocks(n):
    """(label, start_offset, end_offset) of every Saṃhitā/Pada block inside page n"""
    t = texts[n]; res = []; pos = 0; cur = None
    for line in t.split('\n'):
        m = LABEL.match(line)
        if m:
            if cur: res.append((cur[0], cur[1], pos))
            cur = (('sam' if m.group(1).startswith('ಸಂಹಿತಾ') else 'pad' if m.group(1).startswith('ಪದ') else 'other'), pos + len(line) + 1)
        pos += len(line) + 1
    if cur: res.append((cur[0], cur[1], pos))
    return [b for b in res if b[0] != 'other']
EDITS = []; pend = None; prev_n = None
for n in sorted(pages):
    t = texts[n]; edits = []
    if prev_n is not None and n != prev_n + 1: pend = None      # a gap in the pages: nothing carries over
    prev_n = n
    for kind, a, b in blocks(n):
        body = t[a:b]
        if kind == 'sam': pend = (n, a, b); continue
        if kind != 'pad': continue
        flat = ' '.join(l for l in body.split('\n') if l.strip())
        mm = NUMRE.search(flat)
        words_kn = kn_words(NUMRE.sub(' ', flat))
        dev = [P.norm(P.kn2dev(w)) for w in words_kn]
        key = ' '.join(dev)
        best = process.extractOne(key, PADA_STR, scorer=fuzz.ratio)
        if not best or best[1] < 80:
            rows.append((n, 'noref', key[:40], '', f'score {best[1] if best else 0:.0f}')); continue
        ref, r, pw, sw, ppl, spl = REF[best[2]]
        if pend:                                  # the Saṃhitā block just before this Pada stands for the same Ṛk: its number must be the Ṛk's too
            ms = NUMRE.search(texts[pend[0]][pend[1]:pend[2]])
            if ms and int(ms.group(1).translate(KN)) != r:
                news = ''.join(KNDIG[int(c)] for c in str(r)) if ms.group(1)[0] in KNDIG else str(r)
                rows.append((pend[0], 'number', ms.group(0), f'॥ {news} ॥', ref + ' (Saṃhitā)')); EDITS.append((pend[0], pend[1], ms.group(0), f'॥ {news} ॥'))
            pend = None
        if mm:
            v = int(mm.group(1).translate(KN))
            if v != r:
                new = ''.join(KNDIG[int(c)] for c in str(r)) if mm.group(1)[0] in KNDIG else str(r)
                rows.append((n, 'number', mm.group(0), f'॥ {new} ॥', ref)); EDITS.append((n, a, mm.group(0), f'॥ {new} ॥'))
        sm = difflib.SequenceMatcher(None, dev, pw, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal': continue
            if op == 'replace' and i2 - i1 == j2 - j1:
                for k in range(i2 - i1):
                    x, y = dev[i1+k], pw[j1+k]
                    rows.append((n, 'check', words_kn[i1+k], ppl[j1+k], ref))        # a word is never replaced from the reference by script: the page image decides
            else:
                rows.append((n, 'check', ' '.join(words_kn[i1:i2]) or '(missing)', ' '.join(ppl[j1:j2]) or '(extra)', ref))
if wlog:
    by = {}
    for pg_, a_, old, new in EDITS: by.setdefault(pg_, []).append((a_, old, new))
    for pg_, lst in by.items():
        t2 = texts[pg_]
        for a_, old, new in sorted(lst, reverse=True):
            idx = t2.find(old, max(0, a_ - 5))
            if idx >= 0: t2 = t2[:idx] + new + t2[idx+len(old):]
        open(pages[pg_], 'w', encoding='utf8').write(t2)
import collections
for r_ in rows: print('\t'.join(str(x) for x in (f'pdf{r_[0]}',) + r_[1:]))
if report: open(report, 'w', encoding='utf8').write('pdf\tkind\tprinted\treference\trik\n' + '\n'.join('\t'.join(str(x) for x in (r_[0],) + r_[1:]) for r_ in rows) + '\n')
if wlog:
    open(wlog, 'w', encoding='utf8').write('pdf\tkind\twas\tnow\trik\n' + '\n'.join('\t'.join(str(x) for x in (r_[0],) + r_[1:]) for r_ in rows if r_[1] in ('number', 'word')) + '\n')
print('SUMMARY', dict(collections.Counter(r_[1] for r_ in rows)), '| pages', len(pages), file=sys.stderr)
