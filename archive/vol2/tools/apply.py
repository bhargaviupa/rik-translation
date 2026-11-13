"""Apply a batch of exact, unique replacements (JSON list of [file, old, new]) to the Vol 2 files.
file: 'en' or 'gaps'. All-or-nothing: every old string must occur exactly once in the untouched text.
python3 apply.py BATCH.json"""
import sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
B=json.load(open(sys.argv[1])); F={'en':EN}; T={k:open(v,encoding='utf8').read() for k,v in F.items()}
spots={}
for f,o,n in B:
    c=T[f].count(o); assert c==1,(c,f,o)
    spots.setdefault(f,[]).append((T[f].index(o),o,n))
for f,L in spots.items():
    L.sort(reverse=True); t=T[f]; n0=len(t)
    for i in range(len(L)-1): assert L[i+1][0]+len(L[i+1][1])<=L[i][0],('overlap',L[i][1],L[i+1][1])
    for i,o,n in L: t=t[:i]+n+t[i+len(o):]          # from the end backwards, anchors from the untouched text
    assert len(t)>n0-500 and t.count('**Progress note')==T[f].count('**Progress note')
    open(F[f],'w',encoding='utf8').write(t); print(f,len(L),'edits',len(t)-n0,'chars')
