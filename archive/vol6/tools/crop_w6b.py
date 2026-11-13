"""w6b helper: crop a band of a printed page of the better scan.  python3 crop_w6b.py PRINTED OUT.png y0 y1 [x0 x1] [DPI]
Fractions are of the page's text block (as view.py / doubts_v6.py). Renders once per page+dpi into a cache."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,OFFSET
from view import textbox,render
from PIL import Image
pg=int(sys.argv[1]);out=sys.argv[2];y0,y1=float(sys.argv[3]),float(sys.argv[4])
x0,x1=(float(sys.argv[5]),float(sys.argv[6])) if len(sys.argv)>6 else (0,1)
dpi=int(sys.argv[7]) if len(sys.argv)>7 else 120
c=os.path.join(WORK,f'w6b_{pg}_{dpi}.png')
if os.path.exists(c): im=Image.open(c)
else: im=render(pg+OFFSET,dpi); im.save(c)
k=dpi/40; bx=[int(v*k) for v in textbox(render(pg+OFFSET,40))] if not os.environ.get('FULL') else [0,0,im.size[0],im.size[1]]
W=bx[2]-bx[0];H=bx[3]-bx[1]
im.crop((max(0,bx[0]+int(W*x0)-6),max(0,bx[1]+int(H*y0)-6),bx[0]+int(W*x1)+6,bx[1]+int(H*y1)+6)).save(out);print(im.size,bx)
