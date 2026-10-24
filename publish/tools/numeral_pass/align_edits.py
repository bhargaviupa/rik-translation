"""Place reviewed numeral readings in the files: align the crops of a page (print order) with the numeral groups of the
Kannada page section (same order as the print), then find the same group in the English page section.
python3 align_edits.py REVIEW.json EDITS.txt [FIRST LAST] -> prints proposals; writes WORK/proposals.json"""
import sys,os,re,json,difflib
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','verify11'))
from cfg import WORK,EN,KN
KD='೦೧೨೩೪೫೬೭೮೯'; K2A=str.maketrans(KD,'0123456789'); A2K=str.maketrans('0123456789',KD)
R=json.load(open(sys.argv[1])); E={}
for l in open(sys.argv[2],encoding='utf8').read().splitlines():
    if ':' in l: k,v=l.split(':',1); E[k.strip()]=v.strip()
lo,hi=(int(sys.argv[3]),int(sys.argv[4])) if len(sys.argv)>4 else (0,10**6)
def sections(path,kind):
    t=open(path,encoding='utf8').read(); out={}
    pat=r'\n(?=### Printed p\. )' if kind=='en' else r'\n(?=<!-- PDF )'
    for s in re.split(pat,t):
        m=re.match(r'### Printed p\. \S+\s+\(.*?PDF (\d+)',s) if kind=='en' else re.match(r'<!-- PDF (\d+)',s)
        if m: out[int(m.group(1))]=out.get(int(m.group(1)),'')+s
    return out
ENS=sections(EN,'en'); KNS=sections(KN,'kn')
SEG=r'(?:[{d}]{{1,4}}|\[\?\])'
def groups(text,digits):
    seg=SEG.format(d=digits)
    rx=re.compile(r'(?<![\w{d}])({s}(?:\s*-\s*{s}){{0,4}})(\s*\[\?\])?'.format(d=digits,s=seg))
    out=[]
    for m in rx.finditer(text):
        v=m.group(1)
        if v=='[?]': continue
        out.append(dict(v=v,flag=bool(m.group(2)),start=m.start(),end=m.end(),ctx=text[max(0,m.start()-35):m.end()+8].replace('\n',' ')))
    return out
def sim(a,b):
    a=a.translate(K2A); da=re.sub(r'[^\d?]','',a.replace('[?]','?')); db=re.sub(r'\D','',b)
    if not da or not db: return 0
    return difflib.SequenceMatcher(None,da,db).ratio()
def align(crops,kg):
    n,m=len(crops),len(kg); G=-0.25
    S=[[0]*(m+1) for _ in range(n+1)]; P=[[None]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1): S[i][0]=S[i-1][0]+G; P[i][0]='u'
    for j in range(1,m+1): S[0][j]=S[0][j-1]+G; P[0][j]='l'
    for i in range(1,n+1):
        for j in range(1,m+1):
            s=sim(kg[j-1]['v'],crops[i-1][1]); d=S[i-1][j-1]+(s-0.45)*2
            S[i][j],P[i][j]=max((d,'d'),(S[i-1][j]+G,'u'),(S[i][j-1]+G,'l'))
    i,j=n,m; pairs={}
    while i>0 or j>0:
        p=P[i][j]
        if p=='d':
            if sim(kg[j-1]['v'],crops[i-1][1])>=0.34: pairs[i-1]=j-1
            i,j=i-1,j-1
        elif p=='u': i-=1
        else: j-=1
    return pairs
props=[]
bypage={}
for r in R: bypage.setdefault(int(r['pdf']),[]).append(r)
for pdf in sorted(bypage):
    if not lo<=pdf<=hi: continue
    crops=[(r['id'],E.get(r['id'],r['prop'])) for r in bypage[pdf] if E.get(r['id'],r['prop'])]
    kg=groups(KNS.get(pdf,''),KD); eg=groups(ENS.get(pdf,''),'0-9')
    pairs=align(crops,kg)
    for ci,(cid,val) in enumerate(crops):
        if cid not in E: continue
        if ci not in pairs: props.append(dict(pdf=pdf,id=cid,new=val,kn=None,en=None)); continue
        k=kg[pairs[ci]]; kv=k['v'].translate(K2A)
        same=[g for g in eg if g['v']==kv]
        occ=[g for g in kg if g['v'].translate(K2A)==kv].index(k)
        e=same[occ] if occ<len(same) else (same[0] if same else None)
        props.append(dict(pdf=pdf,id=cid,new=val,kn=k,en=e,occ=occ,nsame_en=len(same)))
json.dump(props,open(WORK+'proposals.json','w'),ensure_ascii=False,indent=0)
for p in props:
    if not p['kn']: print(f"{p['id']:7} NEW {p['new']:12} -- no Kannada group aligned"); continue
    print(f"{p['id']:7} {p['kn']['v'].translate(K2A)+(' [?]' if p['kn']['flag'] else ''):14} -> {p['new']:11} | KN …{p['kn']['ctx'][-45:]}"+('' if p['en'] else '   (EN not found)'))
