#!/usr/bin/env python3
"""Check the NUMBERS of page transcriptions (Vol 22 re-transcription from the scan), by rules that need no second reading:
  python3 tools/rv/numbers_check.py DIR [--offset 26] [--tsv OUT.tsv]
DIR holds pdfN.md files (N = PDF page; printed page = N - offset).
1. printed page number: the number in the first line (Latin or Kannada digits) must equal N - offset.
2. verse numbers: the numbers in '॥ N ॥' at the end of Saṃhitā lines and of Pada lines, read in page order, must (a) count up by 1 within a sūkta
   (a drop to 1 starts a new sūkta), (b) agree between Saṃhitā and Pada (same verse -> same number), (c) not repeat.
3. head: the varga number ('ವ. N') never decreases from page to page; the sūkta number ('ಸೂ. N') never decreases.
4. --doubts: list every number carrying a [?] mark (default: not listed).
5. --clean LOG.tsv: remove the [?] that stands on a NUMBER (digit, optional closing punctuation, then [?]) from the files and write what was
   removed (pdf, context) to LOG.tsv. A [?] on a word is never touched. Numbers are decided by the rules above, not marked.
Runs of consecutive PDF pages are checked separately (a gap resets the verse sequence). Output: one line per finding."""
import re, sys, glob, os
KN = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
def num(s): return int(s.translate(KN))
args = sys.argv[1:]; off = 26; tsv = None
if '--offset' in args: i = args.index('--offset'); off = int(args[i+1]); del args[i:i+2]
clean=None; doubts='--doubts' in args
if doubts: args.remove('--doubts')
if '--clean' in args: i=args.index('--clean'); clean=args[i+1]; del args[i:i+2]
if '--tsv' in args: i = args.index('--tsv'); tsv = args[i+1]; del args[i:i+2]
d = args[0]
pages = {}
for f in glob.glob(os.path.join(d, 'pdf*.md')):
    pages[int(re.search(r'pdf(\d+)\.md', f).group(1))] = open(f, encoding='utf8').read()
out = []
def flag(n, kind, msg): out.append((n, kind, msg))
D = '[0-9೦-೯]'
VERSE = re.compile(r'॥\s*(' + D + r'{1,3})\s*(?:\[\?\])?\s*॥')
last = {'sam': None, 'pad': None}
last_varga = last_suk = None
prevn = None
for n in sorted(pages):
    if prevn is not None and n != prevn + 1:       # gap in the pages: new run (verse state is not carried over a gap)
        last = {'sam': None, 'pad': None}; last_varga = last_suk = None
    prevn = n
    t = pages[n]; lines = [l for l in t.split('\n') if l.strip()]
    if not lines: flag(n, 'empty', ''); continue
    head = lines[0]
    nums = [num(x) for x in re.findall(r'(?<![0-9೦-೯])(' + D + r'{1,3})(?![0-9೦-೯])', head)]
    printed = n - off
    if printed not in nums: flag(n, 'page-number', f'printed page should be {printed}; head line has {nums}: {head[:70]}')
    m = re.search(r'ವ\.?\s*(' + D + r'{1,2})', head)
    if m:
        v = num(m.group(1))
        if last_varga is not None and v < last_varga: flag(n, 'varga', f'varga {v} after {last_varga}')
        last_varga = v
    m = re.search(r'ಸೂ\.?\s*(' + D + r'{1,2})', head)
    if m:
        sk = num(m.group(1))
        if last_suk is not None and sk < last_suk: flag(n, 'sukta', f'sūkta {sk} after {last_suk}')
        last_suk = sk
    sec = None
    for l in lines[1:]:
        ls = l.strip()
        if ls.startswith('ಸಂಹಿತಾಪಾಠ'): sec = 'sam'; last['sam'] = None; continue
        if ls.startswith('ಪದಪಾಠ'): sec = 'pad'; last['pad'] = None; continue
        if re.match(r'^(ಸಾಯಣಭಾಷ್ಯ|ಪ್ರತಿಪದಾರ್ಥ|ಭಾವಾರ್ಥ|ವಿಶೇಷ|English)', ls): sec = None; continue
        if sec:
            for mm in VERSE.finditer(l):
                v = num(mm.group(1))
                if sec == 'sam':          # a new Ṛk: one more than the previous Ṛk's number (the Pada's), or 1 (new sūkta)
                    ref = last['pad'] if last['pad'] is not None else last['sam']
                    if ref is not None and v != ref + 1 and v != 1: flag(n, 'verse-sam', f'Saṃhitā verse {v}; expected {ref+1} (or 1)')
                else:                     # the Pada closes the same Ṛk as the Saṃhitā just before it
                    if last['sam'] is not None and v != last['sam']: flag(n, 'verse-pad', f'Pada verse {v}; its Saṃhitā had {last["sam"]}')
                last[sec] = v
    if doubts:
        for mm in re.finditer(r'[^\s]{0,12}\[\?\]', t): flag(n, 'doubt', mm.group(0))
rows = sorted(out)
for n, k, m in rows: print(f'pdf{n}\t{k}\t{m}')
if tsv: open(tsv, 'w', encoding='utf8').write('pdf\tkind\tmessage\n' + '\n'.join(f'{n}\t{k}\t{m}' for n, k, m in rows) + '\n')
import collections
c = collections.Counter(k for _, k, _ in rows); print('SUMMARY', dict(c), '| pages', len(pages), file=sys.stderr)

if clean:
    NUMQ = re.compile(r'(' + D + r'{1,3}[\s\)\]।॥.,;:-]{0,3}?)\s*\[\?\]')
    log = []; changed = 0
    for n in sorted(pages):
        t = pages[n]
        def rep(m): log.append((n, t[max(0, m.start()-25):m.end()+10].replace('\n', ' '))); return m.group(1).rstrip()
        t2 = NUMQ.sub(rep, t)
        t2 = re.sub(r'\[\?\]\s*(?=' + D + r')', lambda m: (log.append((n, 'before-number')), '')[1], t2) if False else t2
        if t2 != t: open(os.path.join(d, f'pdf{n}.md'), 'w', encoding='utf8').write(t2); changed += 1
    open(clean, 'w', encoding='utf8').write('pdf\tcontext (the [?] that stood on a number was removed)\n' + '\n'.join(f'{n}\t{c}' for n, c in log) + '\n')
    print(f'cleaned: {len(log)} [?] on numbers removed in {changed} files; log {clean}', file=sys.stderr)
