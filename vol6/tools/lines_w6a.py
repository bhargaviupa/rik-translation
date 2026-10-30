"""Find text-line bands of a Vol 6 scan page and crop chosen lines (no OCR).
python3 lines_w6a.py PDFPAGE                       -> list lines: index, y0,y1 (fractions of the page), ink width
python3 lines_w6a.py PDFPAGE OUT.png DPI SPEC...   SPEC = i[-j][:x0:x1]  (line indices, inclusive; x fractions) -> stacked crops"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from PIL import Image
import numpy as np
def bands(g):
    im=render(g,100); a=np.array(im)<140; H,W=a.shape; r=a.sum(1); on=r>max(3,W*0.004); out=[]; y=0
    while y<H:
        if on[y]:
            s=y
            while y<H and on[y]: y+=1
            if y-s>=6: out.append([s,y])
            elif out and s-out[-1][1]<6: out[-1][1]=y
        y+=1
    m=[]
    for b in out:   # merge accent strokes / underlines into neighbours
        if m and b[0]-m[-1][1]<4: m[-1][1]=b[1]
        else: m.append(b)
    return [(s/H,e/H) for s,e in m]
if __name__=='__main__':
    g=int(sys.argv[1]); B=bands(g)
    if len(sys.argv)==2:
        for i,(s,e) in enumerate(B): print(i,f'{s:.3f},{e:.3f}')
        sys.exit()
    OUT,dpi=sys.argv[2],int(sys.argv[3]); im=render(g,dpi); W,H=im.size; ims=[]
    for sp in sys.argv[4:]:
        p=sp.split(':'); ij=p[0].split('-'); i=int(ij[0]); j=int(ij[-1]); x0,x1=(float(p[1]),float(p[2])) if len(p)>2 else (0,1)
        y0=B[i][0]-0.006; y1=B[j][1]+0.006
        ims.append(im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))))
    w=max(i.width for i in ims); o=Image.new('L',(w,sum(i.height+8 for i in ims)),255); y=0
    for i in ims: o.paste(i,(0,y)); y+=i.height+8
    o.save(OUT); print(o.size)
