import sys,json
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from cfg import EN as F
t=open(F,encoding='utf8').read(); n0=len(t)
R=json.load(open(sys.argv[1]))
for a,b,cnt in R:
    c=t.count(a)
    if c!=cnt: print('MISMATCH',c,'!=',cnt,repr(a[:70])); continue
    t=t.replace(a,b)
assert len(t)>n0-3000
open(F,'w',encoding='utf8').write(t)
print('left [?]:',t.count('[?]'))
