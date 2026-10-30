"""w6b helper: stack crops (WHOLE-page fractions y0,y1[,x0,x1]) of one printed page.  python3 stackp_w6b.py PRINTED DPI OUT.png y0,y1[,x0,x1] ..."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,OFFSET
from view import render
from PIL import Image,ImageDraw
pg,dpi,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
c=os.path.join(WORK,f'w6b_{pg}_{dpi}.png')
if os.path.exists(c): im=Image.open(c)
else: im=render(pg+OFFSET,dpi); im.save(c)
W,H=im.size; cs=[]
for s in sys.argv[4:]:
    v=list(map(float,s.split(',')))+[0,1][len(s.split(','))-2:] if len(s.split(','))<4 else list(map(float,s.split(',')))
    y0,y1,x0,x1=v[:4]
    cs.append(im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))))
w=max(x.size[0] for x in cs); h=sum(x.size[1]+8 for x in cs)
o=Image.new('L',(w,h),255);y=0;d=ImageDraw.Draw(o)
for x in cs: o.paste(x.convert('L'),(0,y)); y+=x.size[1]+8; d.line((0,y-4,w,y-4),fill=128)
o.save(out); print(o.size)
