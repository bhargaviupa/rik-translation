"""zl_w3.py PDF LINES X0 X1 OUT [DPI] [SCALE] -- crop text lines by number (1 = page header line; LINES like 7 or 7-9;
negative counts from the bottom) and horizontal fraction X0..X1 (0..1) of the trimmed page; PDF may be 'old:K'.
zl_w3.py PDF list -- print the line bands."""
import sys,os,subprocess
from PIL import Image
import numpy as np
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,VOL
arg=sys.argv[1]
def render(d):
    if arg.startswith('old:'): path,k=os.path.join(VOL,'scans/Rig_Vol3.pdf'),int(arg[4:]); tag='old'+arg[4:]
    else: path,k=part_of(int(arg)); tag=arg
    f=f'/tmp/v3num/full_{tag}_{d}'
    if not os.path.exists(f+'.png'):
        subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r',str(d),'-gray','-png','-singlefile',path,f],check=True)
    return Image.open(f+'.png').convert('L')
d=int(sys.argv[6]) if len(sys.argv)>6 else 300; sc=float(sys.argv[7]) if len(sys.argv)>7 else 1.0
im=render(d) if sys.argv[2]!='list' else render(300)
a=np.array(im)<140
rows=np.where(a.sum(1)>a.shape[1]*0.005)[0]; y0,y1=rows[0],rows[-1]
cols=np.where(a[y0:y1].sum(0)>(y1-y0)*0.005)[0]; x0,x1=cols[0],cols[-1]
prof=a[:,x0:x1].sum(1)>(x1-x0)*0.004
bands=[];s=None
for y in range(y0,y1+2):
    on=y<len(prof) and prof[y]
    if on and s is None: s=y
    if not on and s is not None:
        bands.append([s,y]); s=None
# merge bands separated by small gaps (accent marks, matras) : gap < 0.25 * median height
h=np.median([b[1]-b[0] for b in bands]); m=[]
for b in bands:
    if m and b[0]-m[-1][1] < 0.22*h and (b[1]-b[0]<0.6*h or m[-1][1]-m[-1][0]<0.6*h): m[-1][1]=b[1]
    else: m.append(b)
m=[b for b in m if b[1]-b[0]>0.25*h]
if sys.argv[2]=='list':
    for i,b in enumerate(m,1): print(i,b[0]*120//300,b[1]*120//300,'h',(b[1]-b[0])*120//300)
    sys.exit()
L=sys.argv[2]; i1,i2=(L.split('_') if '_' in L else (L,L)); i1,i2=int(i1),int(i2)
n=len(m); i1=i1 if i1>0 else n+1+i1; i2=i2 if i2>0 else n+1+i2
pad=int(0.35*h)
ya=max(0,m[i1-1][0]-pad); yb=min(im.height,m[i2-1][1]+pad)
fx0,fx1=float(sys.argv[3]),float(sys.argv[4]); W=x1-x0
c=im.crop((int(x0+fx0*W)-10,ya,int(x0+fx1*W)+10,yb))
if sc!=1: c=c.resize((int(c.width*sc),int(c.height*sc)),Image.LANCZOS)
c.save(sys.argv[5]); print(sys.argv[5],c.size,'lines',i1,i2,'of',n)
