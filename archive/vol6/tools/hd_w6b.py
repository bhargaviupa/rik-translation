"""w6b helper: stack running-head strips (whole-page fractions) of several printed pages with page labels. python3 hd_w6b.py OUT.png DPI Y0 Y1 X0 X1 P1 P2 ..."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import OFFSET,WORK
from view import render
from PIL import Image,ImageDraw
out,dpi,y0,y1,x0,x1=sys.argv[1],int(sys.argv[2]),*map(float,sys.argv[3:7]); cs=[]
for p in map(int,sys.argv[7:]):
    c=os.path.join(WORK,f'w6b_{p}_{dpi}.png')
    if os.path.exists(c): im=Image.open(c)
    else: im=render(p+OFFSET,dpi); im.save(c)
    W,H=im.size; cs.append((p,im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))).convert('L')))
w=max(x[1].size[0] for x in cs)+60; h=sum(x[1].size[1]+6 for x in cs); o=Image.new('L',(w,h),255); y=0; d=ImageDraw.Draw(o)
for p,x in cs: o.paste(x,(60,y)); d.text((2,y+4),str(p),fill=0); y+=x.size[1]+6; d.line((0,y-3,w,y-3),fill=150)
o.save(out); print(o.size)
