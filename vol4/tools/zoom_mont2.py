"""mont2.py PAGE... -- montage of every review box on printed page(s) (PDF=page+14), json picked by PDF number; out /tmp/v3num/q{page}_{k}.png"""
import sys,os,json,subprocess,glob
from PIL import Image,ImageDraw
sys.path.insert(0,'/home/user/rik-translation/vol4/tools')
from cfg import part_of
J={}
for f in glob.glob('/home/user/rik-translation/vol4/review/review_PDF*.json'):
    for r in json.load(open(f)): J.setdefault(r['pdf'],{})[r['id']]=r
def run(page,per=8):
    g=page+14; R=sorted(J.get(g,{}).values(),key=lambda r:(r['box'][1]//40,r['box'][0]))
    f=f'/tmp/v3num/full{g}.png'
    if not os.path.exists(f):
        path,n=part_of(g); subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','450','-gray','-png','-singlefile',path,f[:-4]],check=True)
    im=Image.open(f); k=1.5; tiles=[]
    for r in R:
        x,y,w,h=[v*k for v in r['box']]; c=im.crop((int(max(0,x-420)),int(y-26),int(x+w+60),int(y+h+26))); c=c.resize((int(c.width*1.7),int(c.height*1.7)),Image.LANCZOS)
        t=Image.new('L',(c.width,c.height+16),255); t.paste(c,(0,16)); ImageDraw.Draw(t).text((3,2),f"{r['id']} y={r['box'][1]}",fill=0); tiles.append(t)
    out=[]
    for i in range(0,len(tiles),per):
        ts=tiles[i:i+per]; W=max(t.width for t in ts); H=sum(t.height for t in ts); m=Image.new('L',(W,H),255); y=0
        for t in ts: m.paste(t,(0,y)); y+=t.height
        fn=f'/tmp/v3num/q{page}_{i//per}.png'; m.save(fn); out.append(fn)
    print(page,len(R),'boxes ->',out)
for p in sys.argv[1:]: run(int(p))
