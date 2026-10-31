"""Render one scan page for reading: trimmed to the text block, cut into full-width strips, each strip at the highest dpi the viewer shows without shrinking it (the viewer reduces any image wider/taller than ~2000 px).
python3 page.py PDFPAGE OUTPREFIX [--dpi 400] [--strips 2]      -> OUTPREFIX_0.png, OUTPREFIX_1.png ... (printed top to bottom)
python3 page.py PDFPAGE OUTPREFIX --zoom Y0 Y1 [X0 X1] [--dpi 600]  -> OUTPREFIX_z.png, one band of the trimmed block (fractions 0-1); rarely needed.
Cuts fall in blank gaps between lines. PDFPAGE is the global PDF page (cfg.part_of maps it to a part)."""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
import numpy as np
from PIL import Image
from cfg import part_of,WORK
LIM=1950
def render(g,dpi):
    p,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(dpi),'-gray','-png',p,d+'/p'],check=True)
    f=[x for x in os.listdir(d)][0]; im=Image.open(d+'/'+f).convert('L'); im.load(); subprocess.run(['rm','-rf',d]); return im
def trim(im,pad=12):
    ys,xs=np.where(np.array(im)<140)
    x0,x1=int(np.percentile(xs,.1)),int(np.percentile(xs,99.9)); y0,y1=int(np.percentile(ys,.1)),int(np.percentile(ys,99.9))
    return im.crop((max(0,x0-pad),max(0,y0-pad),min(im.width,x1+pad),min(im.height,y1+pad)))
def best_dpi(g,want):
    """largest dpi <= want at which the trimmed block is no wider than LIM px"""
    w=trim(render(g,100)).width
    return max(100,min(want,int(LIM*100/w)))
def strips(im,n):
    blank=(np.array(im)<140).sum(axis=1)<=1; runs=[];s=None
    for y,b in enumerate(blank):
        if b and s is None: s=y
        if not b and s is not None:
            if y-s>=10: runs.append((s,y))
            s=None
    cuts=[]
    for k in range(1,n):                       # nearest wide gap to each equal division
        t=im.height*k//n; r=min(runs,key=lambda r:abs((r[0]+r[1])/2-t)); cuts.append((r[0]+r[1])//2)
    ys=[0]+sorted(set(cuts))+[im.height]
    return [im.crop((0,ys[i],im.width,ys[i+1])) for i in range(len(ys)-1)]
if __name__=='__main__':
    a=sys.argv[1:]; g,out=int(a[0]),a[1]
    opt=lambda k,d:type(d)(a[a.index(k)+1]) if k in a else d
    want=opt('--dpi',400)
    if '--zoom' in a:
        i=a.index('--zoom'); v=[float(x) for x in a[i+1:i+5] if not x.startswith('--')]
        y0,y1=v[0],v[1]; x0,x1=(v[2],v[3]) if len(v)>3 else (0,1)
        im=trim(render(g,want)); W,H=im.size
        c=im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))); c.save(out+'_z.png'); print(out+'_z.png',c.size)
    else:
        dpi=best_dpi(g,want); im=trim(render(g,dpi)); n=opt('--strips',max(1,-(-im.height//LIM)))
        for k,s in enumerate(strips(im,n) if n>1 else [im]): s.save(f'{out}_{k}.png'); print(f'{out}_{k}.png',s.size,f'{dpi} dpi')
