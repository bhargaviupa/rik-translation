"""Zoom tiles at 520 dpi from a strip made by strips.py. Box coords are ORIGINAL strip pixels
(the viewer shows strips downscaled to ~2000 px wide: multiply displayed coords by orig_width/displayed_width, e.g. 1.07).
python3 tiles.py N STRIP "x0,y0,x1,y1;x0,y0,x1,y1"  -> WORK/tiles.png"""
import sys,json,subprocess,glob
from PIL import Image,ImageDraw
from cfg import WORK,SCAN
n,s=int(sys.argv[1]),int(sys.argv[2]); boxes=[tuple(map(int,b.split(','))) for b in sys.argv[3].split(';')]
meta=json.load(open(f'{WORK}p{n}.json'))[s-1]
f=glob.glob(f'{WORK}zz{n}-*.pgm')
if not f:
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','520','-gray',SCAN,f'{WORK}zz{n}'],check=True); f=glob.glob(f'{WORK}zz{n}-*.pgm')
a=Image.open(f[0]); k=2.0; tiles=[]
for (x0,y0,x1,y1) in boxes:
    tiles.append(a.crop((int((meta[0]+x0)*k),int((meta[1]+y0)*k),int((meta[0]+x1)*k),int((meta[1]+y1)*k))).convert('L'))
W=max(t.size[0] for t in tiles)+60; H=sum(t.size[1]+8 for t in tiles)
o=Image.new('L',(W,H),255); d=ImageDraw.Draw(o); y=0
for i,t in enumerate(tiles):
    d.text((2,y+t.size[1]//2-6),str(i),fill=0); o.paste(t,(40,y)); y+=t.size[1]+8
o.save(f'{WORK}tiles.png'); print(o.size)
