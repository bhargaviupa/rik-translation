"""Method C: cut each numeral group into glyphs (connected components) and classify them by shape.
Glyphs of groups where Tesseract's three scales agree and the glyph count fits are used as labelled
examples; every glyph is then classified by k nearest neighbours (leave-one-out for labelled ones).
python3 glyphs.py ITEMS.csv TESS.csv OUT.csv [MONTAGE.png]"""
import sys,os,csv,glob,subprocess,collections,re
import numpy as np
from PIL import Image,ImageDraw
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','verify11'))
from cfg import WORK,SCAN

def components(b):
    """b: bool array (ink). returns list of (y0,x0,y1,x1,mask) via run-length union-find"""
    par=[]
    def f(i):
        while par[i]!=i: par[i]=par[par[i]]; i=par[i]
        return i
    prev=[]; runs=[]
    for y in range(b.shape[0]):
        row=b[y].astype(np.int8); d=np.diff(np.concatenate(([0],row,[0])))
        st=np.where(d==1)[0]; en=np.where(d==-1)[0]; cur=[]
        for s,e in zip(st,en):
            k=len(par); par.append(k); cur.append((s,e,k)); runs.append((y,s,e,k))
            for ps,pe,pk in prev:
                if ps<=e and pe>=s:   # 8-connectivity
                    a,c=f(k),f(pk)
                    if a!=c: par[a]=c
        prev=cur
    G=collections.defaultdict(list)
    for y,s,e,k in runs: G[f(k)].append((y,s,e))
    out=[]
    for rs in G.values():
        ys=[r[0] for r in rs]; y0,y1=min(ys),max(ys)+1; x0=min(r[1] for r in rs); x1=max(r[2] for r in rs)
        m=np.zeros((y1-y0,x1-x0),bool)
        for y,s,e in rs: m[y-y0,s-x0:e-x0]=True
        out.append([y0,x0,y1,x1,m])
    return out

def split_group(img):
    """img: L crop. returns ordered tokens ['d'|'-', x0,x1,y0,y1,(y0,x0,mask)]: digit-sized glyphs (pieces merged),
    hyphens; drops brackets, dots, specks and anything after the first bracket that follows a glyph"""
    b=np.asarray(img)<128
    cs=[c for c in components(b) if c[4].sum()>40]
    if not cs: return []
    big=[c for c in cs if c[2]-c[0]>0.5*max(c_[2]-c_[0] for c_ in cs)]
    hs=sorted(c[2]-c[0] for c in big); H=hs[len(hs)//2]
    top=sorted(c[0] for c in big)[len(big)//2]; bot=top+H
    def ov(a,b): return min(a[3],b[3])-max(a[1],b[1])
    toks=[]; seen_digit=False
    for c in sorted(cs,key=lambda c:c[1]):
        y0,x0,y1,x1,m=c; h,w=y1-y0,x1-x0; yc=(y0+y1)/2
        if h>1.25*H and w<0.55*h:                      # bracket
            if seen_digit: break
            toks=[]; continue                          # text before an opening bracket is not part of the number
        if h<0.4*H and w>1.4*h and top+0.3*H<yc<top+0.85*H and not any(ov(c,o)>0.3*w for o in cs if o is not c):
            toks.append(['-',x0,x1,y0,y1,None]); continue
        if m.sum()<0.04*H*H:                           # dot: a separator if it sits between glyphs
            if h<0.3*H and top+0.2*H<yc<top+1.15*H and m.sum()>0.008*H*H: toks.append(['.',x0,x1,y0,y1,None])
            continue
        toks.append(['p',x0,x1,y0,y1,(y0,x0,m)])
        if h>=0.6*H: seen_digit=True
    # merge pieces into glyphs: overlapping or nearly touching, merged width still digit-sized
    out=[]
    for t in toks:
        if t[0]=='p' and out and out[-1][0]=='p':
            p_=out[-1]; gap=t[1]-p_[2]; X0,X1=min(p_[1],t[1]),max(p_[2],t[2])
            small=min(p_[4]-p_[3],t[4]-t[3])<0.75*H or min(p_[2]-p_[1],t[2]-t[1])<0.45*H
            if (gap<0.15*H and small and X1-X0<1.3*H) or gap<-0.3*min(p_[2]-p_[1],t[2]-t[1]):
                Y0,Y1=min(p_[3],t[3]),max(p_[4],t[4]); M=np.zeros((Y1-Y0,X1-X0),bool)
                for (yy,xx,mm) in (p_[5],t[5]): M[yy-Y0:yy-Y0+mm.shape[0],xx-X0:xx-X0+mm.shape[1]]|=mm
                out[-1]=['p',X0,X1,Y0,Y1,(Y0,X0,M)]; continue
        out.append(t)
    res=[]
    for t in out:
        if t[0]=='p':
            if t[4]-t[3]<0.55*H: continue              # leftover small piece (comma, accent)
            t[0]='d'
        if t[0]=='.':
            if res and res[-1][0]=='d': t[0]='-'       # dot after a digit = separator (kept only if a digit follows)
            else: continue
        if t[0]=='-' and res and res[-1][0]=='-': continue
        res.append(t)
    while res and res[0][0]=='-': res.pop(0)
    while res and res[-1][0]=='-': res.pop()
    return res

def feat(m,H):
    """shape vector: glyph scaled into a 24x24 box keeping aspect, blurred, plus size cues"""
    h,w=m.shape; s=24/max(h,w)
    im=Image.fromarray((m*255).astype(np.uint8)).resize((max(1,round(w*s)),max(1,round(h*s))),Image.BILINEAR)
    c=Image.new('L',(28,28),0); c.paste(im,((28-im.width)//2,(28-im.height)//2))
    a=np.asarray(c,float)/255
    a=(a+np.roll(a,1,0)+np.roll(a,-1,0)+np.roll(a,1,1)+np.roll(a,-1,1))/5
    v=np.concatenate([a.ravel(),[h/H*3,w/H*3]]); return v/np.linalg.norm(v)

if __name__=='__main__':
    items=list(csv.DictReader(open(sys.argv[1]))); tess={r['id']:r for r in csv.DictReader(open(sys.argv[2]))}
    G=[]; cur=None
    for r in items:
        if r['id'] not in tess: continue
        p=int(r['pdf'])
        if p!=cur:
            for f in glob.glob(WORK+'g-*.pgm'): os.remove(f)
            subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','600','-gray',SCAN,WORK+'g'],check=True)
            page=Image.open(glob.glob(WORK+'g-*.pgm')[0]); cur=p
        x0,y0,x1,y1=map(int,r['box600'].split()); toks=split_group(page.crop((x0+40,y0,x1-40,y1)).convert('L'))
        G.append((r['id'],toks))
    X=[];L=[];own=[]
    for gid,toks in G:
        ds=[t for t in toks if t[0]=='d']
        if not ds: continue
        H=sorted(t[4]-t[3] for t in ds)[len(ds)//2]
        t=tess[gid]; lab=None
        pat=''.join('d' if t_[0]=='d' else '-' for t_ in toks)
        if int(t['agree'])==3 and ''.join('d' if c.isdigit() else '-' for c in t['tess'])==pat: lab=[c for c in t['tess'] if c.isdigit()]
        for k,d in enumerate(ds):
            X.append(feat(d[5][2],H)); L.append(lab[k] if lab else None); own.append((gid,k,d))
    X=np.array(X); lab_idx=[i for i,l in enumerate(L) if l]
    print('glyphs',len(X),'labelled',len(lab_idx),collections.Counter(L[i] for i in lab_idx))
    XL=X[lab_idx]; YL=np.array([L[i] for i in lab_idx])
    S=X@XL.T
    TAU=float(os.environ.get('TAU','0.80'))
    best=[np.sort(S[i])[-2 if L[i] else -1] for i in range(len(X))]
    print('best-sim quantiles (labelled)',np.round(np.quantile([best[i] for i in lab_idx],[0,.01,.05,.5]),3),'(unlabelled)',np.round(np.quantile([best[i] for i in range(len(X)) if not L[i]],[.01,.05,.1,.5]),3))
    pred=[];conf=[]
    for i in range(len(X)):
        s=S[i].copy()
        if L[i]: s[lab_idx.index(i)]=-1          # leave-one-out
        nn=np.argsort(-s)[:7]; v=collections.Counter()
        for j in nn: v[YL[j]]+=s[j]
        (a,sa),*rest=v.most_common(2)+[('',0)]
        pred.append(a if s[nn[0]]>=TAU else 'x'); conf.append(round(sa/sum(v.values()),2))
    # leave-one-out confusion on labelled glyphs
    cm=collections.Counter((L[i],pred[i]) for i in lab_idx)
    acc=sum(v for (a,b),v in cm.items() if a==b)/len(lab_idx); print('LOO agreement with Tesseract labels',round(acc,4))
    print('disagreements',sorted(((a,b,v) for (a,b),v in cm.items() if a!=b),key=lambda x:-x[2]))
    # group readings
    by=collections.defaultdict(dict)
    for i,(gid,k,d) in enumerate(own): by[gid][k]=(pred[i],conf[i])
    with open(sys.argv[3],'w',newline='') as f:
        w=csv.writer(f); w.writerow(['id','shape','min_conf','tess'])
        for gid,toks in G:
            s=[];k=0;mc=1
            for t_ in toks:
                if t_[0]=='-': s.append('-')
                else: p_,c_=by[gid][k]; s.append(p_); mc=min(mc,c_); k+=1
            r_=re.sub(r'^[x-]+|[x-]+$','',''.join(s)); w.writerow([gid,r_,mc,tess[gid]['tess']])
    if len(sys.argv)>4:   # montage: 14 labelled samples per digit, for a visual check of each class
        rows=[]
        for dg in '0123456789':
            ids=[i for i in lab_idx if L[i]==dg][:14]
            row=Image.new('L',(14*70+40,74),255); ImageDraw.Draw(row).text((5,30),dg,fill=0)
            for k,i in enumerate(ids):
                m=own[i][2][5][2]; im=Image.fromarray(((~m)*255).astype(np.uint8)); im.thumbnail((64,64)); row.paste(im,(40+k*70,5))
            rows.append(row)
        M=Image.new('L',(rows[0].width,74*10),255)
        for k,r_ in enumerate(rows): M.paste(r_,(0,74*k))
        M.save(sys.argv[4])
