"""rep_v4d.py BATCH.json -- exact replacements [[old,new,count],...] applied only inside v4d's range (from '## SŪKTA 44' to the
trailing progress note); refuses if a count does not match. Asserts the file outside the range is unchanged."""
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
t=open(EN,encoding='utf8').read()
a=t.index('\n## SŪKTA 44'); b=t.rfind('**Progress note')
if b<a: b=len(t)
head,mid,tail=t[:a],t[a:b],t[b:]
for old,new,n in json.load(open(sys.argv[1])):
    c=mid.count(old)
    if c!=n: sys.exit(f'COUNT {c}!={n}: {old[:80]!r}')
    mid=mid.replace(old,new)
open(EN,'w',encoding='utf8').write(head+mid+tail); print('ok',len(t),'->',len(head+mid+tail))
