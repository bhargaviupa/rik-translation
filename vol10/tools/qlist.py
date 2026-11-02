"""List the [?] places of PDF pages FROM..TO (only pages that have any): python3 qlist.py FROM TO"""
import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
a,b=int(sys.argv[1]),int(sys.argv[2])
t=open(EN,encoding='utf8').read()
H=re.compile(r'^### Printed p\. (\S+)\s+\(PDF (\d+)[^)]*\)',re.M);hs=list(H.finditer(t))
for i,h in enumerate(hs):
    g=int(h.group(2))
    if not a<=g<=b: continue
    blk=t[h.start():hs[i+1].start() if i+1<len(hs) else len(t)]
    ms=list(re.finditer(r'\[\?\]',blk))
    if not ms: continue
    print('=== PDF %d (printed %s): %d places'%(g,h.group(1),len(ms)))
    for m in ms: print('   ...'+blk[max(0,m.start()-90):m.end()+50].replace('\n',' ')+'...')
