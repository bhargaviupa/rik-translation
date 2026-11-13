"""Line-scoped exact replacements in the Vol 6 main file: JSON list of [LINENO, old, new]; old must occur exactly once on that line.
All-or-nothing; line count must not change; exactly one progress note.   python3 ledit_w6a.py BATCH.json"""
import sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
B=json.load(open(sys.argv[1])); L=open(EN,encoding='utf8').read().split('\n'); n0=len(L)
for ln,o,n in B:
    s=L[ln-1]; assert s.count(o)==1,(ln,s.count(o),o); L[ln-1]=s.replace(o,n)
t='\n'.join(L); assert len(t.split('\n'))==n0 and t.count('**Progress note')==1
open(EN,'w',encoding='utf8').write(t); print('applied',len(B))
