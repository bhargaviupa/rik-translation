"""Append a chunk (stdin) to Rigveda_Samhita_Vol14_English_Translation.md before the single trailing '**Progress note:**', which is replaced by NOTE.
python3 append_en.py "PROGRESS NOTE TEXT" < chunk.md   (asserts: file did not shrink, exactly one note afterwards, old note in last 20000 chars)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
chunk=sys.stdin.read().rstrip('\n'); note=sys.argv[1].strip()
s=open(EN,encoding='utf8').read(); n0=len(s)
i=s.rfind('**Progress note:**')
if i>=0:
    assert i>len(s)-20000,'progress note not near the end'; s=s[:i].rstrip('\n')
s=s+'\n\n'+chunk+'\n\n---\n\n**Progress note:** '+note+'\n'
assert s.count('**Progress note:**')==1 and len(s)>=n0-2000
open(EN,'w',encoding='utf8').write(s); print('ok',len(s))
