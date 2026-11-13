"""w5b helper: stack several horizontal strips of one page (whole-page fractions) into one image.
python3 strips_w5b.py PDFPAGE OUT.png DPI y0:y1[:x0:x1] ..."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from PIL import Image
g,OUT,dpi=int(sys.argv[1]),sys.argv[2],int(sys.argv[3])
im=render(g,dpi); W,H=im.size; parts=[]
for s in sys.argv[4:]:
    v=[float(t) for t in s.split(':')]; x0,x1=(v[2],v[3]) if len(v)>3 else (0.05,0.97)
    parts.append(im.crop((int(W*x0),int(H*v[0]),int(W*x1),int(H*v[1]))))
out=Image.new('L',(max(p.size[0] for p in parts),sum(p.size[1]+6 for p in parts)),255); y=0
for p in parts: out.paste(p,(0,y)); y+=p.size[1]+6
out.save(OUT); print(out.size)
