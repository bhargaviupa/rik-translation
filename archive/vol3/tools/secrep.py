"""Replace references inside one printed-page section of the Vol 3 file, in every script form.
python3 secrep.py BATCH.json   BATCH = [[file('en'|'gaps'), printed page, old, new], ...]
old/new are given in Arabic digits ("1.2.37" -> "1-2-36"); each pair is applied to the Arabic form and to the
Devanagari-digit form (१.२.३७ -> १-२-३६). The section runs from "### Page N" to the next "### Page".
old must occur at least once in the section (in some form); the batch is all-or-nothing; the file must not shrink by
more than the edits explain. A pair whose old starts with '=' is matched literally (no Devanagari form)."""
import sys,os,re,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
A2D=str.maketrans('0123456789','०१२३४५६७८९')
F={'en':EN}; T={k:open(v,encoding='utf8').read() for k,v in F.items()}; T0=dict(T)
def section(t,p):
    m=re.search(r'^### Page '+re.escape(str(p))+r'\b.*$',t,re.M)
    if not m: raise SystemExit(f'no section for page {p}')
    n=re.search(r'^### Page ',t[m.end():],re.M); e=m.end()+n.start() if n else len(t)
    return m.start(),e
B=json.load(open(sys.argv[1])); log=[]
for f,p,o,nw in B:
    t=T[f]; s,e=section(t,p); sec=t[s:e]
    pairs=[(o[1:],nw)] if o.startswith('=') else [(o,nw),(o.translate(A2D),nw.translate(A2D))]
    c=0
    for a,b in pairs:
        pat=re.compile(r'(?<![\d०-९.\-])'+re.escape(a)+r'(?![\d०-९]|\.\d|\.[०-९])')
        sec,k=pat.subn(lambda m:b,sec); c+=k
    if c==0: raise SystemExit(f'not found: {f} p.{p} {o!r}')
    T[f]=t[:s]+sec+t[e:]; log.append(f'{f} p.{p}: {o} -> {nw} ({c}x)')
for k in F:
    if T[k]!=T0[k]: open(F[k],'w',encoding='utf8').write(T[k])
print('\n'.join(log))
