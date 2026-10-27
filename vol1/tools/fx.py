"""Exact, unique replacements in a Vol 1 English file, logged.
python3 fx.py en|gaps 'PAGE' <<< 'OLD\x1fNEW\x1fNOTE' (one edit per line; fields split by \\x1f or ' ||| ')"""
import sys,os,datetime
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN,GAPS,ROOT
f={'en':EN,'gaps':GAPS}[sys.argv[1]]; page=sys.argv[2]
t=open(f,encoding='utf8').read(); n0=len(t); log=[]
for line in sys.stdin.read().split('\n'):
    if not line.strip(): continue
    old,new,note=(line.split(' ||| ')+[''])[:3]
    c=t.count(old); assert c==1,(c,old)
    t=t.replace(old,new); log.append(f"- p. {page} ({os.path.basename(f).replace('Rigveda_Samhita_Vol1_','').replace('_English_Translation.md','') or 'main'}): `{old}` → `{new}`" + (f" — {note}" if note else ''))
assert len(t)>n0-2000
open(f,'w',encoding='utf8').write(t)
L=os.path.join(ROOT,'vol1','vol1_qmarks_log.md')
if not os.path.exists(L): open(L,'w').write('# Vol 1: [?] readings checked against the better (~575 dpi) scan\n\n')
open(L,'a',encoding='utf8').write('\n'.join(log)+'\n'); print('\n'.join(log))
