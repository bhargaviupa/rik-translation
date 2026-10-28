"""nat.py PDF OUT S x0 y0 x1 y1 [S x0 y0 x1 y1 ...] -- like mont.py but crops are re-rendered from the PDF at 658 dpi (native scan resolution), then scaled by Z (default 1.5 over the 658-dpi crop)"""
import sys,json,os,subprocess
from PIL import Image
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
g=int(sys.argv[1]); out=sys.argv[2]; a=sys.argv[3:]; Z=float(os.environ.get('Z','1.5'))
P=json.load(open(f'/tmp/v4num/s{g}.json')); sc=2400/(P['x1']-P['x0']); R=658/450; tiles=[]
path,k=part_of(g)
for j in range(0,len(a),5):
    i=int(a[j]); x0,y0,x1,y1=[float(v)*1.2 for v in a[j+1:j+5]]; top=max(0,int(P['H']*i/P['n'])-50)
    X0=(P['x0']+x0/sc)*R; Y0=(P['y0']+top+y0/sc)*R; X1=(P['x0']+x1/sc)*R; Y1=(P['y0']+top+y1/sc)*R
    f=f'/tmp/v4num/nat{g}_{j}'
    subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r','658','-gray','-png','-singlefile','-x',str(int(X0)),'-y',str(int(Y0)),'-W',str(int(X1-X0)),'-H',str(int(Y1-Y0)),path,f],check=True)
    c=Image.open(f+'.png'); tiles.append(c.resize((int(c.width*Z),int(c.height*Z)),Image.LANCZOS))
W=max(t.width for t in tiles); H=sum(t.height+8 for t in tiles); m=Image.new('L',(W,H),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height+8
m.save(out); print(m.size)
