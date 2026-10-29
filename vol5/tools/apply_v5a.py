"""Like apply.py, but each old string must be unique only inside one section of the Vol 5 file.
python3 apply_v5a.py BATCH.json "### Rik 47.4 "   -- the section runs from that heading to the next "### Rik " / "## SŪKTA" heading
(the "continued" blocks of the same Ṛk are included). All-or-nothing; progress-note count unchanged; no shrink > 500 chars."""
import sys,os,json,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
B=json.load(open(sys.argv[1])); head=sys.argv[2]
t=open(EN,encoding='utf8').read(); n0=len(t)
a=t.index(head); assert t.count(head)==1,head
m=re.compile(r'^(### Rik |## SŪKTA |### Page)',re.M).search(t,a+len(head)); b=m.start() if m else len(t)
s=t[a:b]; bad=[(s.count(o),o[:80]) for o,n in B if s.count(o)!=1]
assert not bad,bad
spots=sorted([(s.index(o),o,n) for o,n in B],reverse=True)
for i in range(len(spots)-1): assert spots[i+1][0]+len(spots[i+1][1])<=spots[i][0],('overlap',spots[i][1][:60])
for i,o,n in spots: s=s[:i]+n+s[i+len(o):]
u=t[:a]+s+t[b:]
assert len(u)>n0-500 and u.count('**Progress note')==t.count('**Progress note')
open(EN,'w',encoding='utf8').write(u); print(len(spots),'edits',len(u)-n0,'chars')
