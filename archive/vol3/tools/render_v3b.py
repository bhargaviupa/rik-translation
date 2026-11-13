"""render_v3b.py PDF [N] [DPI] -- render a global PDF page of the better scan (or 'old:K' for scans/Rig_Vol3.pdf page K),
trim margins, cut into N overlapping horizontal strips -> /tmp/v3num/r{PDF}_{i}.png"""
import sys,os,subprocess
from PIL import Image
import numpy as np
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,VOL
arg=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 2; dpi=sys.argv[3] if len(sys.argv)>3 else '200'
if arg.startswith('old:'):
    path,k=os.path.join(VOL,'scans/Rig_Vol3.pdf'),int(arg[4:]); tag='old'+arg[4:]
else:
    path,k=part_of(int(arg)); tag=arg
f=f'/tmp/v3num/full_{tag}_{dpi}'
if not os.path.exists(f+'.png'):
    subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r',dpi,'-gray','-png','-singlefile',path,f],check=True)
im=Image.open(f+'.png'); a=np.array(im)<128
rows=np.where(a.sum(1)>a.shape[1]*0.01)[0]; y0,y1=max(0,rows[0]-15),min(im.height,rows[-1]+15)
cols=np.where(a[y0:y1].sum(0)>(y1-y0)*0.01)[0]; x0,x1=max(0,cols[0]-15),min(im.width,cols[-1]+15)
im=im.crop((x0,y0,x1,y1)); H=im.height; ov=int(H*0.03)
for i in range(n):
    a_=max(0,i*H//n-ov); b_=min(H,(i+1)*H//n+ov)
    o=f'/tmp/v3num/r{tag}_{i}.png'; im.crop((0,a_,im.width,b_)).save(o); print(o,im.width,b_-a_)
