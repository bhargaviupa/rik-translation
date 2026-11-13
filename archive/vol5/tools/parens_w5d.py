"""w5d: crop every parenthesised group of a PDF page (better scan) at DPI and stack them into numbered montage images.
Locating only (no reading): parentheses = tall thin connected components of a text line.
python3 parens_w5d.py PDFPAGE OUTPREFIX [dpi=500] [maxw=1100] [maxh=1100]   -> OUTPREFIX1.png ...; prints count"""
import sys,os
import numpy as np
from scipy import ndimage
sys.path.insert(0,os.path.dirname(__file__))
from view import textbox,render
from PIL import Image,ImageDraw
g,O=int(sys.argv[1]),sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 500
MW=int(sys.argv[4]) if len(sys.argv)>4 else 1100; MH=int(sys.argv[5]) if len(sys.argv)>5 else 1100
k=dpi/40; x0,t0,x1,t1=[int(v*k) for v in textbox(render(g,40))]
im=render(g,dpi).crop((max(0,x0-10),max(0,t0-10),x1+10,t1+10)); A=np.array(im)<120
ink=A[:,::2].sum(1); th=max(2,A.shape[1]//2//60); L=[]; y=0; H=A.shape[0]
while y<H:
    if ink[y]>th:
        a=y
        while y<H and ink[y]>th: y+=1
        if y-a>=int(5*dpi/120): L.append([a,y])
    y+=1
M=[]
for a,b in L:
    if M and a-M[-1][1]<int(3*dpi/120): M[-1][1]=b
    else: M.append([a,b])
def sub_ok(lab,s,i):
    sub=(lab[s]==i); h,w=sub.shape
    return sub.sum()<=0.55*h*w   # thin curve, not a filled stroke
groups=[]  # (line, xa, xb)
opens=[]
for li,(a,b) in enumerate(M):
    a2,b2=max(0,a-int(0.25*(b-a))),min(H,b+int(0.25*(b-a)))
    lab,n=ndimage.label(A[a2:b2]); P=[]
    for i,s in enumerate(ndimage.find_objects(lab),1):
        h=s[0].stop-s[0].start; w=s[1].stop-s[1].start
        if h>=0.75*(b-a) and w<=0.35*h and w>=2 and sub_ok(lab,s,i):
            sub=(lab[s]==i); r=np.arange(sub.shape[0]); mid=sub[h//3:2*h//3].nonzero()[1].mean(); ends=np.r_[sub[:h//5].nonzero()[1],sub[-h//5:].nonzero()[1]].mean()
            P.append((s[1].start,s[1].stop,'(' if mid<ends else ')'))
    P.sort(); cur=None
    for xa,xb,t in P:
        if t=='(':
            if cur is not None: groups.append((li,cur,xa))
            cur=xa
        else:
            if cur is None: cur=0
            groups.append((li,cur,xb)); cur=None
    if cur is not None: groups.append((li,cur,A.shape[1]))
    M[li]=(a2,b2)
SEL=[int(v) for v in os.environ.get('SEL','').split(',') if v]
crops=[]
for n,(li,xa,xb) in enumerate(groups,1):
    if SEL and n not in SEL: continue
    a,b=M[li]; c=im.crop((max(0,xa-6),a,min(im.size[0],xb+6),b))
    while c.size[0]>MW-60:   # wrap long groups
        crops.append((n,c.crop((0,0,MW-60,c.size[1])))); c=c.crop((MW-60-40,0,c.size[0],c.size[1])); n=f'{n}+'
    crops.append((n,c))
out=[];cur=[];hh=0
for n,c in crops:
    if hh+c.size[1]+6>MH and cur: out.append(cur);cur=[];hh=0
    cur.append((n,c));hh+=c.size[1]+6
if cur: out.append(cur)
for j,blk in enumerate(out,1):
    W=max(c.size[0] for n,c in blk)+60; img=Image.new('L',(W,sum(c.size[1]+6 for n,c in blk)),255); d=ImageDraw.Draw(img); y=0
    for n,c in blk:
        img.paste(c,(60,y)); d.text((2,y+c.size[1]//3),str(n),fill=0); y+=c.size[1]+6
    img=img.resize((img.size[0],img.size[1])); img.save(f'{O}{j}.png')
print(len(groups),'groups',len(out),'images')
