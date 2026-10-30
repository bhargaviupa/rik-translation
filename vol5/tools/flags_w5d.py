"""w5d: flagged lines per printed page in the Pariśiṣṭa (pp. A..B). python3 flags_w5d.py A B [show]"""
import sys,re
sys.path.insert(0,__import__('os').path.dirname(__file__))
from cfg import EN
A,B=int(sys.argv[1]),int(sys.argv[2]); show=len(sys.argv)>3
L=open(EN,encoding='utf-8').read().split('\n'); pg=None; tot=0
pat=re.compile(r'\[\?\]|\[accent \?\]|\d-\?|\?-\d|\(\?|\?\)|-\?-')
for i,l in enumerate(L):
    m=re.match(r'### Printed p\. (\d+)',l)
    if m: pg=int(m.group(1)); continue
    if l.startswith('**Progress note'): break
    if pg and A<=pg<=B and pat.search(l):
        n=len(re.findall(r'\?',l)); tot+=n
        print(pg,i+1,n,(l[:300] if show else ''))
print('total ?',tot,file=sys.stderr)
