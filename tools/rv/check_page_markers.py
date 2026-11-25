#!/usr/bin/env python3
"""Check the printed-page markers of a volume against the supplied text (report only; added after Vol 24, Nov 25 2026).

  python3 tools/rv/check_page_markers.py N [--source FILE.md]

Reference: in the supplied md a `---` line ends every printed page, from the `<!-- page 1 -->` marker on (Vol 24: 797 `---`-chunks for 797 printed pages).
Reports:
  1. chunks versus printed pages: the number of `---` chunks from page 1 on, and the printed pages of the volume file (last `### Printed p. N`);
     a difference means a missing or extra `---` (typically at the seam of two joined input files: add the separator, cf. LESSONS Vol 24);
  2. markers (`### Printed p. N` in the English file, `<!-- printed N -->` in the Kannada file) that are missing, repeated or out of order;
  3. markers whose head line (`*[... NNN]*` in the Kannada file) names another page than the marker: head numbers are often OCR-damaged, so these are
     listed for looking at, not as faults (Vol 24: 59 labelled 60 was a fault; 11 labelled for head '14' was not).
Exit code 1 when 1 or 2 finds something."""
import re, sys, os, json
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
vol = sys.argv[1]
cfg = json.load(open(os.path.join(root, f'vol{vol}', 'volcfg.json'), encoding='utf8'))
srcfile = sys.argv[sys.argv.index('--source') + 1] if '--source' in sys.argv else os.path.join(root, cfg['source'][0].split('@')[0])
en = open(cfg['out']['en'] if os.path.isabs(cfg['out']['en']) else os.path.join(root, cfg['out']['en']), encoding='utf8').read()
kn = open(cfg['out']['kn'] if os.path.isabs(cfg['out']['kn']) else os.path.join(root, cfg['out']['kn']), encoding='utf8').read().split('\n')
src = open(srcfile, encoding='utf8').read().split('\n')
kd = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
bad = 0
start = next((i for i, l in enumerate(src) if '<!-- page 1 -->' in l), None)
pe = [int(x) for x in re.findall(r'^### Printed p\. (\d+)\s*$', en, re.M)]
pk = [int(m.group(1)) for l in kn for m in [re.match(r'<!-- printed (\d+) -->', l)] if m]
last = max(pe + pk) if pe + pk else 0
if not (pe or pk):
    print('no page markers in the volume files yet (nothing translated): chunk count of the source only')
if start is None:
    print('no `<!-- page 1 -->` marker in the source: chunk check skipped')
else:
    seps = [i for i, l in enumerate(src) if i > start and l.strip() == '---']
    chunks = len(seps) + 1
    tail = src[seps[-1] + 1:] if seps else []
    figure_only = all((not l.strip()) or l.startswith('[figure') or l.startswith('*') for l in tail)
    real = chunks - (1 if figure_only else 0)
    print(f'source: {chunks} `---` chunks from page 1 on ({real} without a closing picture-only chunk); volume files: last page marker {last or "none yet"}')
    if last and real != last:
        bad += 1; print(f'  DIFFERENT: {real} chunks against {last} pages: a `---` is missing or extra (seam of joined files?); look at the seam first')
for name, p in (('English', pe), ('Kannada', pk)):
    miss = [x for x in range(1, last + 1) if x not in set(p)]
    dup = sorted({x for x in p if p.count(x) > 1})
    order = [(a, b) for a, b in zip(p, p[1:]) if b <= a]
    print(f'{name}: {len(p)} markers; missing {miss}; repeated {dup}; out of order {order[:10]}')
    if miss or dup or order: bad += 1
dis = []
for i, l in enumerate(kn):
    m = re.match(r'<!-- printed (\d+) -->', l)
    if m and i + 1 < len(kn):
        h = kn[i + 1].strip('*[] ').translate(kd)
        n = re.search(r'ಋಗ್ವೇದ\S*\s*(\d+)\s*$', h) or re.match(r'\s*(\d+)\s+ಸಾ', h)
        if n and int(n.group(1)) != int(m.group(1)): dis.append((int(m.group(1)), int(n.group(1))))
print(f'markers whose head line names another page (marker, head): {dis}')
sys.exit(1 if bad else 0)
