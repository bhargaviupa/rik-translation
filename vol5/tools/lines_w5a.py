"""Crop text lines by index (1-based, counted from the top of the text block, page header = line 1).
python3 lines_w5a.py PDFPAGE OUT.png DPI A B [x0 x1]   -> lines A..B, x by fractions; prints the number of lines found."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render,textbox
g,OUT,dpi,A,B=int(sys.argv[1]),sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
x0f,x1f=(float(sys.argv[6]),float(sys.argv[7])) if len(sys.argv)>7 else (0,1)
x0,t0,x1,t1=[int(v*dpi/40) for v in textbox(render(g,40))]; im=render(g,dpi).crop((x0,t0,x1,t1)); w,h=im.size; px=im.load()
ink=[sum(px[x,y]<120 for x in range(0,w,2)) for y in range(h)]
thr=max(2,w//2//400); bands=[];s=None
for y,v in enumerate(ink+[0]):
    if v>thr and s is None: s=y
    elif v<=thr and s is not None:
        if bands and s-bands[-1][1]<dpi*0.03: bands[-1]=(bands[-1][0],y)   # join accents/underlines to their line
        else: bands.append((s,y))
        s=None
bands=[b for b in bands if b[1]-b[0]>dpi*0.04]
if A==0: print([(i+1,round(b0/h,3)) for i,(b0,b1) in enumerate(bands)]); sys.exit()
a=bands[A-1][0]; b=bands[min(B,len(bands))-1][1]; pad=int(dpi*0.05)
im.crop((int(w*x0f),max(0,a-pad),int(w*x1f),min(h,b+pad))).save(OUT); print(len(bands),'lines')
