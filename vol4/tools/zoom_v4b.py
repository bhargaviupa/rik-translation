"""zoom_v4b.py PDF OUT S x0 y0 x1 y1 [S x0 y0 x1 y1 ...] -- crops given in the DISPLAYED coordinates of strip s{PDF}_{S}.png
(2000 px wide view of the 2400 px strip made by zoom_strips.py PDF N); cut from the 450-dpi full render (Z env: scale, default 2.5)."""
import sys,json,os,subprocess
from PIL import Image
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
g=int(sys.argv[1]); out=sys.argv[2]; a=sys.argv[3:]; Z=float(os.environ.get('Z','2.5')); D=int(os.environ.get('DPI','900'))
P=json.load(open(f'/tmp/v4num/s{g}.json')); sc=2400/(P['x1']-P['x0']); tiles=[]
path,k=part_of(g); full=Image.open(f'/tmp/v4num/full{g}.png'); R=D/450
for j in range(0,len(a),5):
    i=int(a[j]); x0,y0,x1,y1=[float(v)*1.2 for v in a[j+1:j+5]]; top=max(0,int(P['H']*i/P['n'])-50)
    X0=P['x0']+x0/sc; Y0=P['y0']+top+y0/sc; X1=P['x0']+x1/sc; Y1=P['y0']+top+y1/sc
    c=full.crop((int(X0),int(Y0),int(X1),int(Y1))); tiles.append(c.resize((int(c.width*Z),int(c.height*Z)),Image.LANCZOS))
W=max(t.width for t in tiles); H=sum(t.height+10 for t in tiles); m=Image.new('L',(W,H),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height+10
m.save(out); print(m.size)
