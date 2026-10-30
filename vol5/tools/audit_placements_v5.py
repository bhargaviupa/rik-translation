"""Audit: for each applied review-row edit (id: value) check that the value now stands in the file right after the same words that
preceded the reference when the row was built (ctx of the review JSON). Prints rows where no group with that value has that left context.
python3 audit_placements_v5.py EDITS.txt JSON [JSON...]   (JSON: review json with rows/unmatched carrying ctx)"""
import sys,re,json
f='/home/user/rik-translation/Rigveda_Samhita_Vol5_English_Translation.md'
t=open(f,encoding='utf8').read()
def letters(s): return re.sub(r'[^A-Za-zĀ-ſḀ-ỿ]','',s)
G=re.compile(r'(?<![\w.\-,])((?:\d{1,3}(?:,\d{3})+|\d{1,4}|\?)(?:\s*[-.–]\s*(?:\d{1,4}|\[\?\]|\?)){1,4})(\s*\[\?\])?(?![\w])')
R={}
for jf in sys.argv[2:]:
    J=json.load(open(jf))
    for r in J['rows']: R[r['id']]=r
    for u in J.get('unmatched',[]):
        if 'j' in u: R.setdefault(f"{u['printed']}_{u['j']}",u)
E={}
for l in open(sys.argv[1],encoding='utf8'):
    if ':' in l and not l.startswith('#'): k,v=l.split(':',1); E[k.strip()]=v.split('(applied')[0].strip()
bad=0;n=0
secs={}
def sec(p):
    if p not in secs:
        m=re.search(r'\n### Printed p\. %d \(PDF \d+\)'%p,t); s=m.start(); nn=re.search(r'\n### Printed p\. ',t[s+5:]); secs[p]=t[s:s+5+nn.start()]
    return secs[p]
for k,v in E.items():
    r=R.get(k)
    if not r or v.lower()=='x' or not v: continue
    n+=1; ctx=r['ctx']; i=ctx.find(r['file']); lw=letters(ctx[:i])[-12:]; rw=letters(ctx[i+len(r['file']):])[:6]
    body=sec(r['printed']); ok=False
    if len(lw)<6 and len(rw)<4: print('NO-CONTEXT',k,v); continue
    for m in re.finditer(r'(?<![\d\-])'+re.escape(v)+r'(?![\d])',body):
        L=letters(body[max(0,m.start()-70):m.start()])[-12:]; Rr=letters(body[m.end():m.end()+30])[:6]
        okL= len(lw)>=6 and (L==lw or lw in letters(body[max(0,m.start()-90):m.start()]))
        okR= len(rw)>=4 and Rr[:len(rw)]==rw
        if (okL and okR) or (okL and len(rw)<4) or (okR and len(lw)<6): ok=True;break
    if not ok: bad+=1; print('CHECK',k,'value',v,'| left words',repr(lw),'| file was',r['file'])
print(n,'edits audited,',bad,'to check')
