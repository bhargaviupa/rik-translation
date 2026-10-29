"""pg_w4a.py PDF [DPI] -- render one better-scan page (global PDF number) at DPI (default 120), grayscale, trimmed to the text block,
with a light coordinate ruler -> /tmp/w4a/p{PDF}.png.   Zoom: pg_w4a.py PDF z DPI x0 y0 x1 y1 [OUT] -- crop given in the 120-dpi
TRIMMED image's pixel coordinates, re-rendered at DPI (300/450) -> /tmp/w4a/z.png (or OUT)."""
import sys,os,subprocess,json
from PIL import Image,ImageDraw
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
W='/tmp/w4a/'; os.makedirs(W,exist_ok=True)
def render(g,dpi):
    f=f'{W}full{g}_{dpi}.png'
    if not os.path.exists(f):
        path,k=part_of(g); subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r',str(dpi),'-gray','-png','-singlefile',path,f[:-4]],check=True)
    return Image.open(f)
g=int(sys.argv[1])
if len(sys.argv)>2 and sys.argv[2]=='z':
    dpi=int(sys.argv[3]); x0,y0,x1,y1=map(float,sys.argv[4:8]); out=sys.argv[8] if len(sys.argv)>8 else W+'z.png'
    T=json.load(open(f'{W}p{g}.json')); s=dpi/120
    im=render(g,dpi); c=im.crop((int((T['x0']+x0)*s),int((T['y0']+y0)*s),int((T['x0']+x1)*s),int((T['y0']+y1)*s)))
    c.save(out); print(out,c.size); sys.exit()
dpi=int(sys.argv[2]) if len(sys.argv)>2 else 120
im=render(g,120); a=np.array(im)<128
rows=np.where(a.sum(1)>15)[0]; y0,y1=max(0,rows[0]-10),min(im.height,rows[-1]+10)
cols=np.where(a[y0:y1].sum(0)>8)[0]; x0,x1=max(0,cols[0]-10),min(im.width,cols[-1]+10)
c=im.crop((x0,y0,x1,y1)).convert('RGB'); d=ImageDraw.Draw(c)
for y in range(0,c.height,50):
    d.line((0,y,8 if y%100 else 16,y),fill=(255,0,0),width=1)
    if y%100==0: d.text((18,y-5),str(y),fill=(255,0,0))
for x in range(0,c.width,100): d.line((x,0,x,8),fill=(0,0,255),width=1); d.text((x+2,9),str(x),fill=(0,0,255))
c.save(f'{W}p{g}.png'); json.dump(dict(x0=int(x0),y0=int(y0)),open(f'{W}p{g}.json','w')); print(f'{W}p{g}.png',c.size)
