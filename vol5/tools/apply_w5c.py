"""w5c: like apply.py, but each old string must be unique within the section of one printed page of the Pariśiṣṭa
('### Printed p. N' up to the next '### Printed p.' heading).  python3 apply_w5c.py PAGE BATCH.json"""
import sys,os,json,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
p=int(sys.argv[1]); B=json.load(open(sys.argv[2])); t=open(EN,encoding='utf8').read(); n0=len(t)
a=t.index(f'### Printed p. {p} ('); m=re.compile(r'^### Printed p\. \d+',re.M).search(t,a+5); b=m.start() if m else t.index('### Close of the Pariśiṣṭa')
s=t[a:b]; spots=[]
for o,n in B:
    c=s.count(o); assert c==1,(c,o)
    spots.append((s.index(o),o,n))
spots.sort(reverse=True)
for i in range(len(spots)-1): assert spots[i+1][0]+len(spots[i+1][1])<=spots[i][0],('overlap',spots[i][1])
for i,o,n in spots: s=s[:i]+n+s[i+len(o):]
u=t[:a]+s+t[b:]
assert len(u)>n0-500 and u.count('**Progress note')==t.count('**Progress note')
open(EN,'w',encoding='utf8').write(u); print(len(B),'edits',len(u)-n0,'chars')
