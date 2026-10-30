"""w6b helper: list text lines of a printed page as text-block fractions (y0-y1), for targeting crops.  python3 lines_w6b.py PRINTED"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import OFFSET
from view import textbox,render
from PIL import ImageOps
pg=int(sys.argv[1]); dpi=100; im=render(pg+OFFSET,dpi); k=dpi/40
bx=[int(v*k) for v in textbox(render(pg+OFFSET,40))]; W=bx[2]-bx[0];H=bx[3]-bx[1]
b=ImageOps.invert(im.crop(bx)).point(lambda v:255 if v>110 else 0); px=b.load()
rows=[sum(px[x,y]>0 for x in range(0,W,2)) for y in range(H)]
out=[];y=0
while y<H:
    if rows[y]>2:
        s=y
        while y<H and rows[y]>2: y+=1
        if y-s>=4: out.append((s,y))
    y+=1
for i,(s,e) in enumerate(out,1): print(f'{i}:{s/H:.3f}-{e/H:.3f}',end='  ')
print()
