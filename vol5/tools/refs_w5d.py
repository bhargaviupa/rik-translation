"""w5d: list the references of a printed page of the Pariśiṣṭa in order (index, ref, context); '*' = contains '?'.
python3 refs_w5d.py PAGE        |  apply: python3 refs_w5d.py PAGE apply MAP.json  (MAP = {"index": "new ref", ...})"""
import sys,re,json,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
R=re.compile(r'(?<![\w.])(?:\d+|\?)(?:-(?:\d+|\?))+(?![\w])')
P=int(sys.argv[1]); txt=open(EN,encoding='utf-8').read()
a=txt.index(f'\n### Printed p. {P} ('); b=txt.index('\n### ',a+5); seg=txt[a:b]
ms=list(R.finditer(seg))
if len(sys.argv)>2 and sys.argv[2]=='apply':
    J=json.load(open(sys.argv[3])); T=J.pop('_text',[]); M={int(k):v for k,v in J.items()}; out=[]; last=0
    for i,m in enumerate(ms,1):
        out.append(seg[last:m.start()]); out.append(M.get(i,m.group())); last=m.end()
    out.append(seg[last:]); new=''.join(out)
    for o,n in T:
        assert new.count(o)==1,o; new=new.replace(o,n); print(f'p. {P}: "{o}" -> "{n}"')
    for i,v in M.items(): assert '?' in ms[i-1].group() or v!=ms[i-1].group(), i
    t2=txt[:a]+new+txt[b:]; assert t2.count('**Progress note')==txt.count('**Progress note')
    open(EN,'w',encoding='utf-8').write(t2)
    for i in sorted(M): print(f'p. {P}: {ms[i-1].group()} -> {M[i]}')
else:
    for i,m in enumerate(ms,1):
        c=re.sub(r'\s+',' ',seg[max(0,m.start()-22):m.start()]).replace('\n',' ')
        print(f"{i}{'*' if '?' in m.group() else ''} {m.group()} | {c[-22:]}")
