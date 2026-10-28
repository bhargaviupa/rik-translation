"""repsec_v4d.py START END BATCH.json -- like rep_v4d.py but counts and replaces only inside the text between the first
occurrence of START (at or after '## SŪKTA 44') and the next occurrence of END after it."""
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
t=open(EN,encoding='utf8').read()
r=t.index('\n## SŪKTA 44'); a=t.index(sys.argv[1],r); b=t.index(sys.argv[2],a+len(sys.argv[1]))
mid=t[a:b]
for old,new,n in json.load(open(sys.argv[3])):
    c=mid.count(old)
    if c!=n: sys.exit(f'COUNT {c}!={n}: {old[:80]!r}')
    mid=mid.replace(old,new)
open(EN,'w',encoding='utf8').write(t[:a]+mid+t[b:]); print('ok',len(t),'->',len(t[:a]+mid+t[b:]))
