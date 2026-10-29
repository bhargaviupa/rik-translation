"""band_v4b.py PDF OUT S y0 y1 [S y0 y1 ...] -- full-width line bands (displayed-strip y coordinates, 2000-px view of the
zoom_strips.py strips), each cut into K halves (env K, default 2) stacked, from the 450-dpi render; Z env scale (default 1.6)."""
import sys,json,os
from PIL import Image
g=int(sys.argv[1]); out=sys.argv[2]; a=sys.argv[3:]; Z=float(os.environ.get('Z','1.6')); K=int(os.environ.get('K','2'))
P=json.load(open(f'/tmp/v4num/s{g}.json')); sc=2400/(P['x1']-P['x0']); full=Image.open(f'/tmp/v4num/full{g}.png'); tiles=[]
for j in range(0,len(a),3):
    i=int(a[j]); y0,y1=[float(v)*1.2 for v in a[j+1:j+3]]; top=max(0,int(P['H']*i/P['n'])-50)
    Y0=P['y0']+top+y0/sc; Y1=P['y0']+top+y1/sc; W=P['x1']-P['x0']
    for k in range(K):
        X0=P['x0']+W*k/K-(30 if k else 0); X1=P['x0']+W*(k+1)/K+30
        c=full.crop((int(X0),int(Y0),int(X1),int(Y1))); tiles.append(c.resize((int(c.width*Z),int(c.height*Z)),Image.LANCZOS))
Wm=max(t.width for t in tiles); H=sum(t.height+10 for t in tiles); m=Image.new('L',(Wm,H),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height+10
m.save(out); print(m.size)
