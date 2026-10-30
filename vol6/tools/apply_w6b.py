"""w6b helper: like apply.py, but every old string must occur exactly once inside file lines FIRST..LAST (1-based).
python3 apply_w6b.py BATCH.json FIRST LAST"""
import sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
B=json.load(open(sys.argv[1])); a,b=int(sys.argv[2]),int(sys.argv[3])
L=open(EN,encoding='utf8').read().split('\n'); n0=sum(map(len,L))
pre,mid,post='\n'.join(L[:a-1]),'\n'.join(L[a-1:b]),'\n'.join(L[b:])
for o,n in B: assert mid.count(o)==1,(mid.count(o),o)
for o,n in B: mid=mid.replace(o,n)
u=pre+'\n'+mid+'\n'+post
assert len(u)>n0-500 and u.count('**Progress note')==1
open(EN,'w',encoding='utf8').write(u); print(len(B),'edits')
