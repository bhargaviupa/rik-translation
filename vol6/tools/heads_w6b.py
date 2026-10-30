"""w6b helper: stack the running-head strips (left part) of several printed pages.  python3 heads_w6b.py OUT.png DPI X1 P1 P2 ...
(x1 = right edge as text-block fraction; FULL page width used if textbox is cut)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import OFFSET
from view import textbox,render
from PIL import Image,ImageDraw
out,dpi,x1=sys.argv[1],int(sys.argv[2]),float(sys.argv[3]); cs=[]
for p in map(int,sys.argv[4:]):
    im=render(p+OFFSET,dpi); k=dpi/40; bx=[int(v*k) for v in textbox(render(p+OFFSET,40))]; W=bx[2]-bx[0];H=bx[3]-bx[1]
    cs.append(im.crop((max(0,bx[0]-10),max(0,bx[1]-8),bx[0]+int(W*x1),bx[1]+int(H*0.016))))
w=max(x.size[0] for x in cs); h=sum(x.size[1]+6 for x in cs); o=Image.new('L',(w,h),255); y=0; d=ImageDraw.Draw(o)
for x in cs: o.paste(x,(0,y)); y+=x.size[1]+6; d.line((0,y-3,w,y-3),fill=128)
o.save(out); print(o.size)
