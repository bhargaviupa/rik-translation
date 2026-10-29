"""rep_w4b.py BATCH.json -- exact replacements [[old,new,count],...] limited to lines A..B given as "range":[A,B] (1-based, inclusive) in the JSON object {"range":[A,B],"edits":[...]}; refuses count mismatches."""
import sys,json,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
d=json.load(open(sys.argv[1],encoding='utf-8')); A,B=d['range']
L=open(EN,encoding='utf-8').read().split('\n'); n0=sum(len(x) for x in L)
seg='\n'.join(L[A-1:B])
for old,new,c in d['edits']:
    k=seg.count(old)
    if k!=c: sys.exit(f'count {k}!={c}: {old[:80]!r}')
    seg=seg.replace(old,new)
L=L[:A-1]+seg.split('\n')+L[B:]
open(EN,'w',encoding='utf-8').write('\n'.join(L)); print('ok',len(d['edits']))
