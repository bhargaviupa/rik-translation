"""Apply a batch of exact, unique replacements (JSON list of [old, new]) to the Vol 13 main file.
All-or-nothing: every old string must occur exactly once in the untouched text; the file must not shrink by more than 500
characters; the number of '**Progress note' blocks must not change.   python3 apply.py BATCH.json"""
import sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
B=json.load(open(sys.argv[1])); t=open(EN,encoding='utf8').read(); n0=len(t); spots=[]
for o,n in B:
    c=t.count(o); assert c==1,(c,o)
    spots.append((t.index(o),o,n))
spots.sort(reverse=True)
for i in range(len(spots)-1): assert spots[i+1][0]+len(spots[i+1][1])<=spots[i][0],('overlap',spots[i][1],spots[i+1][1])
u=t
for i,o,n in spots: u=u[:i]+n+u[i+len(o):]
assert len(u)>n0-500 and u.count('**Progress note')==t.count('**Progress note')
open(EN,'w',encoding='utf8').write(u); print(len(spots),'edits',len(u)-n0,'chars')
