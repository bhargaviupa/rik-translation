"""mont.py PDF OUT S x0 y0 x1 y1 [S x0 y0 x1 y1 ...] -- stack crops given in displayed-strip coordinates (strip index S first); zoom 3"""
import sys,json,os
from PIL import Image
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
g=int(sys.argv[1]); out=sys.argv[2]; a=sys.argv[3:]; Z=float(os.environ.get('Z','3'))
P=json.load(open(f'/tmp/v4num/s{g}.json')); sc=2400/(P['x1']-P['x0']); im=Image.open(f'/tmp/v4num/full{g}.png'); tiles=[]
for k in range(0,len(a),5):
    i=int(a[k]); x0,y0,x1,y1=[float(v)*1.2 for v in a[k+1:k+5]]; top=max(0,int(P['H']*i/P['n'])-50)
    c=im.crop((int(P['x0']+x0/sc),int(P['y0']+top+y0/sc),int(P['x0']+x1/sc),int(P['y0']+top+y1/sc)))
    W=int(c.width*Z*sc); tiles.append(c.resize((W,int(c.height*W/c.width)),Image.LANCZOS))
W=max(t.width for t in tiles); H=sum(t.height+8 for t in tiles); m=Image.new('L',(W,H),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height+8
m.save(out); print(m.size)
