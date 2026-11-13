"""zc_v4a.py PDF OUT S x0 y0 x1 y1 [...] -- crops from the 450-dpi full page (made by zoom_strips.py) given DISPLAYED strip coords (2000-px-wide view, x1.2 = strip px); stacked, scaled by Z (default 2)"""
import sys,json,os
from PIL import Image
g=int(sys.argv[1]); out=sys.argv[2]; a=sys.argv[3:]; Z=float(os.environ.get('Z','2'))
P=json.load(open(f'/tmp/v4num/s{g}.json')); im=Image.open(f'/tmp/v4num/full{g}.png'); sc=2400/(P['x1']-P['x0']); tiles=[]
for j in range(0,len(a),5):
    i=int(a[j]); x0,y0,x1,y1=[float(v)*1.2 for v in a[j+1:j+5]]; top=max(0,int(P['H']*i/P['n'])-50)
    c=im.crop((int(P['x0']+x0/sc),int(P['y0']+top+y0/sc),int(P['x0']+x1/sc),int(P['y0']+top+y1/sc)))
    tiles.append(c.resize((int(c.width*Z),int(c.height*Z)),Image.LANCZOS))
W=max(t.width for t in tiles); H=sum(t.height+8 for t in tiles); m=Image.new('L',(W,H),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height+8
m.save(out); print(m.size)
