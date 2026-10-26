"""Sort the user's edits of a review page: A = differs from the matched file reading, E = emptied,
F = same digits as the file (no change), N = typed on a row with no file match: found elsewhere on the page or missing.
python3 classify_edits.py REVIEW.json EDITS.txt > report"""
import sys,os,re,json
sys.path.insert(0,os.path.dirname(__file__))
from pages import page_sections,text_of,label
R={r['id']:r for r in json.load(open(sys.argv[1]))}
E={}
for l in open(sys.argv[2],encoding='utf8').read().splitlines():
    if ':' in l: k,v=l.split(':',1); E[k.strip()]=v.strip()
K2A=str.maketrans('೦೧೨೩೪೫೬೭೮೯०१२३४५६७८९','0123456789'*2)
dig=lambda s:re.sub(r'\D','',s.translate(K2A))
def page_text(g): return ''.join(text_of(f)[s:e] for (f,_,_,s,e) in page_sections(g)).translate(K2A)
def found(g,v):
    """the value's numbers, in order, with any separator (. - , space, 'and'), anywhere on the page section"""
    parts=[p for p in re.split(r'\D+',v) if p]
    if not parts: return False
    rx=r'(?<!\d)'+r'(?:\s*(?:[-.,–:/]|and|,\s*verse|\s)\s*)'.join(parts)+r'(?!\d)'
    t=page_text(g).replace(',000',  '000') if len(parts)==1 else page_text(g)
    return re.search(rx,page_text(g)) is not None or re.search(rx,t) is not None
out={'A':[],'E':[],'F':[],'Nf':[],'Nm':[]}
for k,v in E.items():
    r=R.get(k)
    if r is None: print('unknown id',k); continue
    if r['file'] and '?' not in r['file']:
        if not v: out['E'].append(k)
        elif dig(v)==dig(r['file']): out['F'].append(k)
        else: out['A'].append(k)
    else:
        if not v: continue
        (out['Nf'] if found(r['pdf'],v) else out['Nm']).append(k)
for c,ks in out.items():
    print(f'== {c} {len(ks)}')
    for k in ks:
        r=R[k]; print(f"{k:7} new={E[k]!r:14} file={r['file']!r:12} tess={r['tess']!r:10} | {r['ctx'][-70:]!r}" if c in 'AEF' else f"{k:7} new={E[k]!r:14} tess={r['tess']!r}")
