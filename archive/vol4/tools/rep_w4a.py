"""rep_w4a.py BATCH.json -- exact replacements inside one region of the Vol 4 file.
BATCH = {"from": "heading line text (start of region)", "to": "heading line text (end of region, exclusive)", "edits": [[old,new,count],...]}
Each old must occur exactly `count` times inside the region; refuses otherwise. File must not shrink by more than the edits imply."""
import sys,json
sys.path.insert(0,__import__('os').path.dirname(__file__))
from cfg import EN
B=json.load(open(sys.argv[1])); t=open(EN,encoding='utf-8').read()
a=t.index(B['from']); assert t.count(B['from'])==1, 'from not unique'
b=t.index(B['to'],a+1)
reg=t[a:b]
for old,new,n in B['edits']:
    c=reg.count(old)
    if c!=n: sys.exit(f'COUNT {c}!={n}: {old[:80]}')
    reg=reg.replace(old,new)
open(EN,'w',encoding='utf-8').write(t[:a]+reg+t[b:]); print('ok',len(B['edits']),'edits')
