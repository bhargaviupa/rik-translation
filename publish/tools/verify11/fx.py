"""Edit helpers. Each replaces text only inside one PDF page's section and refuses (prints '!!') unless the old text occurs exactly once.
en(pdf,[(old,new)])  English file | kn(pdf,[(old,new)])  Kannada file
sk(pdf,[(old_deva,new_deva)])  Sanskrit: patches Devanagari + IAST (English file) and the Kannada-script copy."""
import sys,re,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','translit'))
from add_iast import deva_to_iast
from deva_to_kannada import deva2kn
from cfg import EN as E, KN as K
def _span(t,kind,pdf):
    if pdf is None: return 0,len(t)
    if kind=='en':
        m=re.search(r'### Printed p\. \S+\s+\([^)]*?PDF %d\)'%pdf,t)
        if not m: raise SystemExit('no EN page %d'%pdf)
        n=re.search(r'\n### Printed p\. ',t[m.end():]); return m.start(), m.end()+(n.start() if n else len(t)-m.end())
    m=re.search(r'<!-- PDF %d ·'%pdf,t)
    if not m: raise SystemExit('no KN page %d'%pdf)
    n=re.search(r'\n<!-- PDF ',t[m.end():])
    return m.start(), m.end()+(n.start() if n else len(t)-m.end())
def _sub(t,kind,pdf,a,b,label):
    s,e=_span(t,kind,pdf); seg=t[s:e]; n=seg.count(a)
    if n!=1: print('!!',label,pdf,n,repr(a[:60])); return t
    return t[:s]+seg.replace(a,b,1)+t[e:]
def en(pdf,pairs):
    t=open(E,encoding='utf8').read()
    for a,b in pairs: t=_sub(t,'en',pdf,a,b,'EN')
    open(E,'w',encoding='utf8').write(t)
def kn(pdf,pairs):
    t=open(K,encoding='utf8').read()
    for a,b in pairs: t=_sub(t,'kn',pdf,a,b,'KN')
    open(K,'w',encoding='utf8').write(t)
def sk(pdf,pairs):
    t=open(E,encoding='utf8').read(); k=open(K,encoding='utf8').read()
    for a,b in pairs:
        t=_sub(t,'en',pdf,a,b,'EN-dev')
        t=_sub(t,'en',pdf,deva_to_iast(a),deva_to_iast(b),'EN-iast')
        k=_sub(k,'kn',pdf,deva2kn(a),deva2kn(b),'KN-sk')
    open(E,'w',encoding='utf8').write(t); open(K,'w',encoding='utf8').write(k)
