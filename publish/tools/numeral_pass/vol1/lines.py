"""Montage of the printed lines holding given crops (crop boxed in red), for placing edits.
python3 lines.py REVIEW.json OUT.png ID [ID ...]   (ids of one or more pages)"""
import sys,os,json,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image,ImageDraw
R={r['id']:r for r in json.load(open(sys.argv[1]))}; OUT=sys.argv[2]; ids=sys.argv[3:]
DPI=170; k=DPI/300; pages={}; tiles=[]
for i in ids:
    g=R[i]['pdf']
    if g not in pages:
        path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
        subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(DPI),'-gray',path,d+'/p'],check=True)
        pages[g]=Image.open(d+'/'+os.listdir(d)[0]).convert('RGB'); subprocess.run(['rm','-rf',d])
    im=pages[g]; x,y,w,h=[int(v*k) for v in R[i]['box']]; lh=max(h,int(22*k*1.9))
    W=im.width; X=float(os.environ.get("CTX","0.9")); t=im.crop((int(W*0.06),max(0,y-int(lh*X)),int(W*0.94),y+h+int(lh*X))).copy()
    d=ImageDraw.Draw(t); ox=int(W*0.06); oy=max(0,y-int(lh*X))
    d.rectangle((x-ox-2,y-oy-2,x-ox+w+2,y-oy+h+2),outline=(220,0,0),width=2)
    d.rectangle((0,0,70,13),fill=(255,255,0)); d.text((2,1),i,fill=(0,0,0)); tiles.append(t)
Wm=max(t.width for t in tiles); m=Image.new('RGB',(Wm,sum(t.height+3 for t in tiles)),'white'); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height+3
m.save(OUT); print(m.size)
