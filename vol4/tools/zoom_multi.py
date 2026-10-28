"""multi.py OUT id1[:padL:padR] id2 ... -- stacked tight crops (450 dpi, x3.2) of review boxes, labelled"""
import sys,os,json,glob,subprocess
from PIL import Image,ImageDraw
sys.path.insert(0,'/home/user/rik-translation/vol4/tools')
from cfg import part_of
R={}
for f in glob.glob('/home/user/rik-translation/vol4/review/review_PDF*.json'):
    for r in json.load(open(f)): R[r['id']]=r
tiles=[]
for a in sys.argv[2:]:
    p=a.split(':'); r=R[p[0]]; L=int(p[1]) if len(p)>1 else 200; Rr=int(p[2]) if len(p)>2 else 60
    g=r['pdf']; f=f'/tmp/v4num/full{g}.png'
    if not os.path.exists(f):
        path,n=part_of(g); subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','450','-gray','-png','-singlefile',path,f[:-4]],check=True)
    im=Image.open(f); x,y,w,h=[v*1.5 for v in r['box']]
    c=im.crop((int(max(0,x-L)),int(y-14),int(x+w+Rr),int(y+h+14))); s=float(os.environ.get("S","3.0")); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    t=Image.new('L',(c.width,c.height+16),255); t.paste(c,(0,16)); ImageDraw.Draw(t).text((3,2),a,fill=0); tiles.append(t)
W=max(t.width for t in tiles); H=sum(t.height for t in tiles); m=Image.new('L',(W,H),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height
m.save(sys.argv[1]); print(m.size)
