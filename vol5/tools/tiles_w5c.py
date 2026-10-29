"""w5c: a horizontal band of the text block, cut into N overlapping column pieces stacked top to bottom (for reading small
reference numerals).  python3 tiles_w5c.py PDFPAGE OUT.png y0 y1 [dpi=450] [N=3]   (y0,y1 fractions of the text block)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import textbox,render
from PIL import Image
g,OUT,y0,y1=int(sys.argv[1]),sys.argv[2],float(sys.argv[3]),float(sys.argv[4])
dpi=int(sys.argv[5]) if len(sys.argv)>5 else 450; N=int(sys.argv[6]) if len(sys.argv)>6 else 3
k=dpi/40; x0,t0,x1,t1=[int(v*k) for v in textbox(render(g,40))]
x1+=int(0.1*dpi); im=render(g,dpi); H=t1-t0; W=x1-x0; a=t0+int(H*y0)-8; b=t0+int(H*y1)+8; ov=int(W*0.04)
P=[im.crop((max(0,x0+W*j//N-ov),a,min(im.size[0],x0+W*(j+1)//N+ov),b)) for j in range(N)]
w=max(p.size[0] for p in P); out=Image.new('L',(w,sum(p.size[1]+12 for p in P)),255); y=0
for p in P: out.paste(p,(0,y)); y+=p.size[1]+12
out.save(OUT); print(out.size)
