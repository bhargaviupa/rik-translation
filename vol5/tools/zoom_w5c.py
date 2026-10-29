"""w5c zoom helper: crop regions of a Vol 5 page given in pixel coords of the 120-dpi text-block view (view.py PDF OUT 120)
and stack them vertically.  python3 zoom_w5c.py PDF OUT.png DPI BOX [BOX ...]   (full render cached in V5WORK)
BOX = X0,Y0,X1,Y1  or  L<a>[-<b>][,X0,X1]  (text lines a..b as numbered by lines_w5c.py on V5WORK/view_PDF.png; default full width)
Optional env UP=2 upscales the montage."""
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
cs=[]; LN=None
for b in sys.argv[4:]:
    if b.startswith('L'):
        if LN is None:
            import subprocess as sp
            o=sp.run([sys.executable,os.path.join(os.path.dirname(__file__),'lines_w5c.py'),os.path.join(WORK,f'view_{g}.png')],capture_output=True,text=True).stdout.split()
            LN={int(a):tuple(map(int,r.split('-'))) for a,r in (x.split(':') for x in o)}
        f=b[1:].split(','); a,_,bb=f[0].partition('-'); bb=bb or a
        y0,y1=LN[int(a)][0]-4,LN[int(bb)][1]+4; x0,x1=(float(f[1]),float(f[2])) if len(f)>2 else (0,640)
    else: x0,y0,x1,y1=map(float,b.split(','))
    cs.append(im.crop((int(ox+x0*s),int(oy+y0*s),int(ox+x1*s),int(oy+y1*s))))
W=max(c.width for c in cs); H=sum(c.height+6 for c in cs); o=Image.new('L',(W,H),128); y=0
for c in cs: o.paste(c,(0,y)); y+=c.height+6
U=int(os.environ.get('UP','1'))
if U>1: o=o.resize((o.width*U,o.height*U))
o.save(out); print(o.size)
