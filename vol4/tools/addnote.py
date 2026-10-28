"""Append an italic note to a printed-page section of the Vol 4 main file, before its 'Embedded English' block
(or at the section end).  python3 addnote.py BATCH.json   BATCH = [[printed_page, note_text], ...]"""
import sys,os,re,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
t=open(EN,encoding='utf8').read(); n0=len(t)
for p,note in json.load(open(sys.argv[1])):
    m=re.search(r'^### Pages? '+re.escape(str(p))+r'\b.*$',t,re.M)
    if not m: raise SystemExit(f'no page {p}')
    n=re.search(r'^### Pages? ',t[m.end():],re.M); e=m.end()+n.start() if n else len(t)
    sec=t[m.start():e]; k=sec.find('\n---\n\n**Embedded English')
    pos=m.start()+(k if k>=0 else len(sec.rstrip('\n')))
    t=t[:pos]+f"\n\n*({note})*"+t[pos:]
    print('p.',p,'ok')
assert len(t)>n0
open(EN,'w',encoding='utf8').write(t)
