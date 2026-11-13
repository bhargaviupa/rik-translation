"""Montage of review crops with the box's current proposal, for reading the numerals myself.
python3 montage.py REVIEW.json START COUNT OUT.png  (rows in json order)"""
import sys,os,json,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image,ImageDraw,ImageFont
R=json.load(open(sys.argv[1])); s,c=int(sys.argv[2]),int(sys.argv[3]); OUT=sys.argv[4]
rows=R[s:s+c]; pages={}; tiles=[]
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22)
for r in rows:
    g=r['pdf']
    if g not in pages:
        path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
        subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray',path,d+'/p'],check=True)
        pages[g]=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d])
    x,y,w,h=r['box']; im=pages[g]
    cr=im.crop((max(0,x-70),max(0,y-8),x+w+40,y+h+8))
    cr=cr.resize((int(cr.width*0.8),int(cr.height*0.8)))
    t=Image.new('L',(620,max(cr.height,30)+4),255); t.paste(cr,(0,2))
    ImageDraw.Draw(t).text((min(cr.width+8,400),4),f"{r['id']}  [{r['prop']}]",fill=0,font=F)
    tiles.append(t)
H=sum(t.height for t in tiles); cols=2; per=(len(tiles)+1)//2
colh=[sum(t.height for t in tiles[i*per:(i+1)*per]) for i in range(cols)]
m=Image.new('L',(cols*630,max(colh)),255)
for ci in range(cols):
    yy=0
    for t in tiles[ci*per:(ci+1)*per]: m.paste(t,(ci*630,yy)); yy+=t.height
m.save(OUT); print(m.size)
