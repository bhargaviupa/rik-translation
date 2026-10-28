"""sec_v3b.py SPEC.py -- v3b section patcher. SPEC defines HEAD (heading prefix) and EDITS = [(start_marker, end_marker, new_text)]:
the text from start_marker (inclusive) up to end_marker (exclusive), both searched inside that section only, is replaced.
end_marker None = replace the start_marker string only. Helpers for SPEC: blk(text) -> Devanagari quote + IAST quote;
sam(text) -> accented Saṃhitā quote + IAST with accents."""
import sys,os,re
sys.path.insert(0,os.path.dirname(__file__)); sys.path.insert(0,os.path.join(os.path.dirname(__file__),'../../publish/tools/translit'))
from cfg import EN
from add_iast import deva_to_iast
from accent import iast as acc_iast
def _q(lines,f): return '\n'.join('> '+f(l) for l in lines)
def blk(t):
    L=[l.strip() for l in t.strip().split('\n')]
    return _q(L,lambda l:l)+'\n\n'+_q(L,lambda l:'*'+deva_to_iast(l)+'*')
def sam(t):
    L=[l.strip() for l in t.strip().split('\n')]
    def fl(l): return (l.replace('[accent ?]','').rstrip(),' [accent ?]' if '[accent ?]' in l else '')
    return '\n'.join(f'> {a}{b}' for a,b in map(fl,L))+'\n\n'+'\n'.join(f'> *{acc_iast(a)}*{b}' for a,b in map(fl,L))
G={'blk':blk,'sam':sam}; exec(open(sys.argv[1],encoding='utf8').read(),G)
t=open(EN,encoding='utf8').read(); n0=len(t)
h=t.index('\n'+G['HEAD'])+1; nx=t.find('\n### Pages ',h+5); nx2=t.find('\n## ',h+5)
e=min(x for x in (nx,nx2,len(t)) if x>0)
S=t[h:e]
for a,b,new in G['EDITS']:
    assert S.count(a)==1,('start',S.count(a),a[:60])
    i=S.index(a)
    j=i+len(a) if b is None else S.index(b,i+len(a))
    S=S[:i]+new+S[j:]
t=t[:h]+S+t[e:]
assert len(t)>n0*0.98
open(EN,'w',encoding='utf8').write(t); print('ok',len(t)-n0)
