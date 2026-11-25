#!/usr/bin/env python3
"""Settle the WORDS of transcribed Saṃhitā and Pada blocks from the Wikisource reference (user decision, Nov 25 2026: "Wikisource has no errors").

  python3 tools/rv/ref_settle.py DIR --mandala 7 [--blocks pad|pad,sam] [--write LOG.tsv]      (preview without --write; prints what would change)
  --blocks pad: Pada blocks only (Vol 22: the Saṃhitā blocks differ from Wikisource also in spelling conventions of the print, e.g. न्त्स / न्स: not applied without the user's word)
Every Saṃhitā block (ಸಂಹಿತಾಪಾಠಃ) and Pada block (ಪದಪಾಠಃ) of the pdfN.md page files is matched to its reference Ṛk (normalised Devanagari, rapidfuzz ratio >= 80,
as tools/rv/ref_verify.py; the Pada block fixes the Ṛk, the Saṃhitā block just before it belongs to the same Ṛk). The block's words are aligned with the
reference words (difflib on normalised words: accents, final virama/anusvara, visarga, avagraha, ZWNJ ignored); at every difference the Wikisource word
replaces the transcribed one (written in Kannada script without accents, a final ಮ್ written as ಂ as the print does); extra words are deleted, missing words
inserted; a difference spanning more than 3 words is not touched and listed as 'manual'. Every change is a row of LOG.tsv (pdf, block, was, now, rik).
Numbers are not touched here (tools/rv/ref_verify.py settles them)."""
import re, sys, glob, os, sqlite3, difflib, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'publish' / 'tools' / 'translit'))
from rapidfuzz import fuzz, process
import pratipada_check as P
from deva_to_kannada import deva2kn
args = sys.argv[1:]
def opt(name):
    if name in args:
        i = args.index(name); v = args[i+1]; del args[i:i+2]; return v
mand = [int(x) for x in (opt('--mandala') or '7').split(',')]; wlog = opt('--write'); only = (opt('--blocks') or 'pad,sam').split(','); d = args[0]
pages = {int(re.search(r'pdf(\d+)\.md', f).group(1)): f for f in glob.glob(os.path.join(d, 'pdf*.md'))}
con = sqlite3.connect(P.DB)
REF = []
for ref, pada, sam in con.execute('select ref,pada,samhita from rik where m in (%s) order by m,s,r' % ','.join('?'*len(mand)), mand):
    pw = P.words(pada or ''); sw = P.words(re.sub(r'॥.*', '', sam or '').replace('ॐ', ''))
    REF.append((ref, pw, [P.norm(w) for w in pw], sw, [P.norm(w) for w in sw]))
PSTR = [' '.join(x[2]) for x in REF]; SSTR = [' '.join(x[4]) for x in REF]
DROPACC = re.compile('[॒॑॓॔᳐-᳿‌‍​]')
LABEL = re.compile(r'^\s*(ಸಂಹಿತಾಪಾಠಃ?|ಪದಪಾಠಃ?|ಸಾಯಣಭಾಷ್ಯಂ|ಪ್ರತಿಪದಾರ್ಥ|ಭಾವಾರ್ಥ|ವಿಶೇಷವಿಷಯಗಳು|English Translation)')
TOK = re.compile(r'[^\s|।॥]+')
DIG = re.compile(r'^[0-9೦-೯\[\]?()]+$')
def blocks(t):
    res = []; pos = 0; cur = None
    for line in t.split('\n'):
        m = LABEL.match(line)
        if m:
            if cur: res.append((cur[0], cur[1], pos))
            cur = (('sam' if m.group(1).startswith('ಸಂಹಿತಾ') else 'pad' if m.group(1).startswith('ಪದ') else 'other'), pos + len(line) + 1)
        pos += len(line) + 1
    if cur: res.append((cur[0], cur[1], pos))
    return [b for b in res if b[0] != 'other']
def kn_word(w):
    k = deva2kn(DROPACC.sub('', w))
    return re.sub('ಮ್$', 'ಂ', k)
log = []; manual = []; nchg = 0
for n in sorted(pages):
    t = open(pages[n], encoding='utf8').read(); t0 = t
    bl = blocks(t); rik = None
    # Pada blocks fix the Ṛk; a Saṃhitā block belongs to the Pada block that follows it
    plan = []        # (kind, a, b, ref index)
    for i, (kind, a, b) in enumerate(bl):
        body = t[a:b]
        toks = [m for m in TOK.finditer(body) if not DIG.match(m.group(0))]
        key = ' '.join(P.norm(P.kn2dev(m.group(0))) for m in toks)
        if kind == 'pad':
            best = process.extractOne(key, PSTR, scorer=fuzz.ratio)
            if best and best[1] >= 80:
                plan.append(('pad', a, b, best[2]))
                if i > 0 and bl[i-1][0] == 'sam': plan.append(('sam', bl[i-1][1], bl[i-1][2], best[2]))
    edits = []
    for kind, a, b, ri in plan:
        if kind not in only: continue
        ref, pw, pn, sw, sn = REF[ri]
        body = t[a:b]
        toks = [m for m in TOK.finditer(body) if not DIG.match(m.group(0))]
        dev = [P.norm(P.kn2dev(m.group(0))) for m in toks]
        rn, rw = (pn, pw) if kind == 'pad' else (sn, sw)
        sm = difflib.SequenceMatcher(None, dev, rn, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal': continue
            was = ' '.join(m.group(0) for m in toks[i1:i2]) or '(missing)'; now = ' '.join(rw[j1:j2]) or '(extra)'
            if max(i2 - i1, j2 - j1) > 3: manual.append((n, kind, was, now, ref)); continue
            newkn = [kn_word(w) for w in rw[j1:j2]]
            sep = ' | ' if kind == 'pad' else ' '
            if op == 'replace' and (i2 - i1) == (j2 - j1):
                for k in range(i2 - i1):
                    edits.append((a + toks[i1+k].start(), a + toks[i1+k].end(), newkn[k])); 
                log.append((n, kind, was, ' '.join(newkn), ref))
            elif op in ('replace', 'delete'):
                s0, e0 = a + toks[i1].start(), a + toks[i2-1].end()
                edits.append((s0, e0, sep.join(newkn))); log.append((n, kind, was, sep.join(newkn) or '(deleted)', ref))
            else:       # insert before token i1 (or after the last one)
                if i1 < len(toks): pos = a + toks[i1].start(); edits.append((pos, pos, sep.join(newkn) + sep))
                else: pos = a + toks[-1].end() if toks else a; edits.append((pos, pos, sep + sep.join(newkn)))
                log.append((n, kind, '(missing)', sep.join(newkn), ref))
    if wlog and edits:
        for s0, e0, new in sorted(edits, reverse=True): t = t[:s0] + new + t[e0:]
        t = re.sub(r' \| (?= \||\s*$)', ' ', t)
        open(pages[n], 'w', encoding='utf8').write(t); nchg += 1
for r in log: print('\t'.join(str(x) for x in (f'pdf{r[0]}',) + r[1:]))
for r in manual: print('MANUAL\t' + '\t'.join(str(x) for x in (f'pdf{r[0]}',) + r[1:]))
if wlog: open(wlog, 'w', encoding='utf8').write('pdf\tblock\twas\tnow (Wikisource)\trik\n' + '\n'.join('\t'.join(str(x) for x in r) for r in log) + '\n')
print(f'SUMMARY changes {len(log)} | manual {len(manual)} | pages {len(pages)} | files rewritten {nchg}', file=sys.stderr)
