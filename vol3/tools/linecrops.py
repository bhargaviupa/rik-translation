"""Montage of OCR-located lines: python3 linecrops.py OUT.png PDF:TOP[:LEFT:WIDTH] ...   (TOP/LEFT in the 300-dpi coordinates of review/ocr/PDF.json)
Each crop = the line (+-14 px) from LEFT (default 0) for WIDTH px (default 1900), upscaled x1.6, labelled. One image for many lines."""
import sys,os,subprocess
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image,ImageDraw
tiles=[];cache={}
for a in sys.argv[2:]:
    p=a.split(':'); g=int(p[0]); top=int(p[1]); left=int(p[2]) if len(p)>2 else 0; w=int(p[3]) if len(p)>3 else 1900
    f=f'{WORK}full300_{g}.png'
    if not os.path.exists(f):
        path,n=part_of(g); subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray','-png','-singlefile',path,f[:-4]],check=True)
    im=Image.open(f); c=im.crop((max(0,left),max(0,top-18),min(im.width,left+w),top+78)); c=c.resize((int(c.width*1.6),int(c.height*1.6)),Image.LANCZOS)
    t=Image.new('L',(c.width,c.height+16),255); t.paste(c,(0,16)); ImageDraw.Draw(t).text((3,2),a,fill=0); tiles.append(t)
W=max(t.width for t in tiles); H=sum(t.height for t in tiles); m=Image.new('L',(W,H),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height
m.save(sys.argv[1]); print(m.size)
