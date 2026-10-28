"""List every [?] in a printed-page section of the Vol 4 file with its context, and the global PDF page(s) of the
better scan that hold that printed page.  python3 qctx.py en|gaps PRINTED [CHARS]"""
import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
from pages import printed
f={'en':EN}[sys.argv[1]]; p=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 110
t=open(f,encoding='utf8').read()
m=re.search(r'^### Pages? '+re.escape(p)+r'\b.*$',t,re.M); n=re.search(r'^### Page',t[m.end():],re.M)
s,e=m.start(),(m.end()+n.start() if n else len(t)); sec=t[s:e]
pdf=[g for g in range(1,601) if printed(g)==p]
print(f'printed p. {p} -> PDF {pdf}')
for i,q in enumerate(re.finditer(r'\[\?\]',sec)):
    print(f'#{i}', repr(sec[max(0,q.start()-w):q.end()+40]))
