"""w6b helper: stack several crops of one printed page into one image.  python3 stack_w6b.py PRINTED DPI OUT.png y0,y1,x0,x1 [...]
(text-block fractions; x may exceed 0..1 where the text block is cut)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,OFFSET
from view import textbox,render
from PIL import Image,ImageDraw
pg,dpi,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
c=os.path.join(WORK,f'w6b_{pg}_{dpi}.png')
if os.path.exists(c): im=Image.open(c)
else: im=render(pg+OFFSET,dpi); im.save(c)
k=dpi/40; bx=[int(v*k) for v in textbox(render(pg+OFFSET,40))]; W=bx[2]-bx[0];H=bx[3]-bx[1]
cs=[]
for s in sys.argv[4:]:
    y0,y1,x0,x1=map(float,s.split(','))
    cs.append(im.crop((max(0,bx[0]+int(W*x0)-6),max(0,bx[1]+int(H*y0)-6),min(im.size[0],bx[0]+int(W*x1)+6),bx[1]+int(H*y1)+6)))
w=max(x.size[0] for x in cs); h=sum(x.size[1]+8 for x in cs)
o=Image.new('L',(w,h),255);y=0;d=ImageDraw.Draw(o)
for x in cs: o.paste(x,(0,y)); y+=x.size[1]+8; d.line((0,y-4,w,y-4),fill=128)
o.save(out); print(o.size)
