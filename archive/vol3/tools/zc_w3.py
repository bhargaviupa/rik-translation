"""zc_w3.py PDF x0 y0 x1 y1 OUT [DPI] [SCALE] -- crop a box given in the coordinates of the 120-dpi trimmed render
(render_v3b.py PDF 1 120 -> /tmp/v3num/rPDF_0.png) from a DPI render (default 300) of the same page; PDF may be 'old:K'."""
import sys,os,subprocess
from PIL import Image
import numpy as np
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,VOL
arg=sys.argv[1]; x0,y0,x1,y1=map(float,sys.argv[2:6]); out=sys.argv[6]
dpi=int(sys.argv[7]) if len(sys.argv)>7 else 300; sc=float(sys.argv[8]) if len(sys.argv)>8 else 1.0
def render(d):
    if arg.startswith('old:'): path,k=os.path.join(VOL,'scans/Rig_Vol3.pdf'),int(arg[4:]); tag='old'+arg[4:]
    else: path,k=part_of(int(arg)); tag=arg
    f=f'/tmp/v3num/full_{tag}_{d}'
    if not os.path.exists(f+'.png'):
        subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r',str(d),'-gray','-png','-singlefile',path,f],check=True)
    return Image.open(f+'.png')
def trim(im):
    a=np.array(im)<128
    rows=np.where(a.sum(1)>a.shape[1]*0.01)[0]; y0,y1=max(0,rows[0]-15),min(im.height,rows[-1]+15)
    cols=np.where(a[y0:y1].sum(0)>(y1-y0)*0.01)[0]; x0,x1=max(0,cols[0]-15),min(im.width,cols[-1]+15)
    return x0,y0
lo=render(120); lx,ly=trim(lo); hi=render(dpi); r=dpi/120
c=hi.crop((int((x0+lx)*r),int((y0+ly)*r),int((x1+lx)*r),int((y1+ly)*r)))
if sc!=1: c=c.resize((int(c.width*sc),int(c.height*sc)),Image.LANCZOS)
c.save(out); print(out,c.size)
