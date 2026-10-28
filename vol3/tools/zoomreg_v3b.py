"""zoomreg_v3b.py PDF|old:K X0 Y0 X1 Y1 OUT [SCALE] -- crop of the margin-trimmed page at 400 dpi (fractions of the trimmed page)"""
import sys,os,subprocess
from PIL import Image
import numpy as np
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,VOL
arg=sys.argv[1]
if arg.startswith('old:'): path,k=os.path.join(VOL,'scans/Rig_Vol3.pdf'),int(arg[4:]); tag='old'+arg[4:]
else: path,k=part_of(int(arg)); tag=arg
f=f'/tmp/v3num/full_{tag}_400'
if not os.path.exists(f+'.png'):
    subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r','400','-gray','-png','-singlefile',path,f],check=True)
im=Image.open(f+'.png'); a=np.array(im)<128
rows=np.where(a.sum(1)>a.shape[1]*0.01)[0]; y0,y1=max(0,rows[0]-30),min(im.height,rows[-1]+30)
cols=np.where(a[y0:y1].sum(0)>(y1-y0)*0.01)[0]; x0,x1=max(0,cols[0]-30),min(im.width,cols[-1]+30)
im=im.crop((x0,y0,x1,y1)); W,H=im.size
X0,Y0,X1,Y1=map(float,sys.argv[2:6]); s=float(sys.argv[7]) if len(sys.argv)>7 else 1
c=im.crop((int(W*X0),int(H*Y0),int(W*X1),int(H*Y1)))
if s!=1: c=c.resize((int(c.width*s),int(c.height*s)))
c.save(sys.argv[6]); print(c.size)
