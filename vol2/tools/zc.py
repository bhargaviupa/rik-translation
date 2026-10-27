"""Zoom several review boxes (with left context) into one image at full 300 dpi: zc.py REVIEW.json OUT.png ID..."""
import sys,os,json,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image
R={r['id']:r for r in json.load(open(sys.argv[1]))}; OUT=sys.argv[2]; ids=sys.argv[3:]; P={}; T=[]
for k in ids:
    r=R[k]; g=r['pdf']
    if g not in P:
        path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
        subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','450','-gray',path,d+'/p'],check=True)
        P[g]=Image.open(d+'/'+os.listdir(d)[0]); subprocess.run(['rm','-rf',d])
    x,y,w,h=[int(v*1.5) for v in r['box']]; T.append(P[g].crop((max(0,x-120),y-20,x+w+60,y+h+20)))
W=max(t.width for t in T); m=Image.new('L',(W,sum(t.height+6 for t in T)),255); yy=0
for t in T: m.paste(t,(0,yy)); yy+=t.height+6
m.save(OUT); print(m.size)
