"""rep_v4c.py EDITS.json -- {"start": "anchor text (unique in file)", "end": "anchor text after start", "edits": [[old,new], ...]}
Each old must occur exactly once between start and end (end excluded). Writes the main file."""
import sys,json,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
d=json.load(open(sys.argv[1],encoding='utf8'))
t=open(EN,encoding='utf8').read()
assert t.count(d['start'])==1,'start not unique'
s=t.index(d['start']); e=t.index(d['end'],s+1)
reg=t[s:e]
for o,n in d['edits']:
    c=reg.count(o)
    assert c==1,(c,o[:120])
    reg=reg.replace(o,n)
t2=t[:s]+reg+t[e:]
open(EN,'w',encoding='utf8').write(t2); print('ok',len(t),'->',len(t2))
