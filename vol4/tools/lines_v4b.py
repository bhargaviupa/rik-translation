"""lines_v4b.py PDF [N]  -- render (450 dpi, cached) + trim like zoom_strips.py, find text-line runs, write N labelled reading strips
/tmp/v4num/L{PDF}_{i}.png (2000 px wide, run numbers in red at the left) and /tmp/v4num/L{PDF}.json (run y-ranges in the 450-dpi render).
lines_v4b.py PDF OUT a-b [c-d ...]  -- crop runs a..b (inclusive, padded) full width, cut into K pieces (env K, default 2), Z scale (default 1.3)."""
import sys,os,json,subprocess
from PIL import Image,ImageDraw
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
g=int(sys.argv[1]); f=f'/tmp/v4num/full{g}.png'
if not os.path.exists(f):
    path,k=part_of(g); subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r','450','-gray','-png','-singlefile',path,f[:-4]],check=True)
im=Image.open(f).convert('L'); a=np.array(im)<128
rows=np.where(a.sum(1)>40)[0]; y0,y1=max(0,rows[0]-30),min(im.height,rows[-1]+30)
cols=np.where(a[y0:y1].sum(0)>20)[0]; x0,x1=max(0,cols[0]-30),min(im.width,cols[-1]+30)
ink=a[:,x0:x1].sum(1)>2; runs=[]; y=y0
while y<y1:
    if ink[y]:
        s=y
        while y<y1 and (ink[y] or ink[y:y+int(os.environ.get("GAP","4"))].any()): y+=1
        if y-s>4:
            h=y-s; n=max(1,round(h/int(os.environ.get('PITCH','98')))) if h>150 else 1
            for k in range(n): runs.append((s+h*k//n,s+h*(k+1)//n))
    y+=1
if len(sys.argv)<=3 or sys.argv[2].isdigit():
    n=int(sys.argv[2]) if len(sys.argv)>2 else 4
    json.dump(dict(x0=int(x0),x1=int(x1),runs=[(int(p),int(q)) for p,q in runs]),open(f'/tmp/v4num/L{g}.json','w'))
    # split runs into n groups of similar height
    H=y1-y0; bounds=[y0+H*i//n for i in range(n+1)]
    for i in range(n):
        rr=[(j,p,q) for j,(p,q) in enumerate(runs) if bounds[i]<=(p+q)//2<bounds[i+1]]
        if not rr: continue
        top=rr[0][1]-15; bot=rr[-1][2]+15
        c=im.crop((x0-90,top,x1,bot)).convert('RGB'); d=ImageDraw.Draw(c)
        for j,p,q in rr: d.text((5,(p+q)//2-top-20),str(j),fill=(255,0,0),font_size=48)
        c=c.resize((2000,int(c.height*2000/c.width)),Image.LANCZOS); c.save(f'/tmp/v4num/L{g}_{i}.png')
    print(len(runs),'runs')
else:
    out=sys.argv[2]; K=int(os.environ.get('K','2')); Z=float(os.environ.get('Z','1.3')); tiles=[]
    for r in sys.argv[3:]:
        p,q=(int(v) for v in r.split('-')) if '-' in r else (int(r),int(r))
        top=runs[p][0]-12; bot=runs[q][1]+12; W=x1-x0
        for k in range(K):
            c=im.crop((int(x0+W*k/K-(40 if k else 0)),top,int(x0+W*(k+1)/K+40),bot)); tiles.append(c.resize((int(c.width*Z),int(c.height*Z)),Image.LANCZOS))
    Wm=max(t.width for t in tiles); H=sum(t.height+10 for t in tiles); m=Image.new('L',(Wm,H),255); yy=0
    for t in tiles: m.paste(t,(0,yy)); yy+=t.height+10
    m.save(out); print(m.size)
