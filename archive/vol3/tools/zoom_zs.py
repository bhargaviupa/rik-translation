"""zs.py PDF i x0 y0 x1 y1 OUT [zoom] -- crop given in DISPLAYED strip px (2000-wide view of strip i); zoom default 2.5"""
import sys,json
from PIL import Image
g=int(sys.argv[1]); i=int(sys.argv[2]); x0,y0,x1,y1=[float(v)*1.2 for v in sys.argv[3:7]]
P=json.load(open(f'/tmp/v3num/s{g}.json')); sc=2400/(P['x1']-P['x0']); top=max(0,int(P['H']*i/P['n'])-50)
im=Image.open(f'/tmp/v3num/full{g}.png')
px=lambda x:P['x0']+x/sc; py=lambda y:P['y0']+top+y/sc
c=im.crop((int(px(x0)),int(py(y0)),int(px(x1)),int(py(y1)))); z=float(sys.argv[8]) if len(sys.argv)>8 else 2.5
W=int(min(2200,c.width*z*sc)); c=c.resize((W,int(c.height*W/c.width)),Image.LANCZOS); c.save(sys.argv[7]); print(c.size)
