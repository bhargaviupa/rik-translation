"""w5c zoom helper: crop regions of a Vol 5 page given in pixel coords of the 120-dpi text-block view (view.py PDF OUT 120)
and stack them vertically.  python3 zoom_w5c.py PDF OUT.png DPI X0,Y0,X1,Y1 [X0,Y0,X1,Y1 ...]   (full render cached in V5WORK)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK
from view import textbox,render
from PIL import Image
g,out,dpi=int(sys.argv[1]),sys.argv[2],int(sys.argv[3])
c=os.path.join(WORK,f'full_{g}_{dpi}.png')
if not os.path.exists(c): render(g,dpi).save(c)
im=Image.open(c); k=dpi/40; bx,by,_,_=[int(v*k) for v in textbox(render(g,40))]
s=dpi/120; ox,oy=bx-8*s,by-8*s
cs=[]
for b in sys.argv[4:]:
    x0,y0,x1,y1=map(float,b.split(','))
    cs.append(im.crop((int(ox+x0*s),int(oy+y0*s),int(ox+x1*s),int(oy+y1*s))))
W=max(c.width for c in cs); H=sum(c.height+6 for c in cs); o=Image.new('L',(W,H),128); y=0
for c in cs: o.paste(c,(0,y)); y+=c.height+6
o.save(out); print(o.size)
