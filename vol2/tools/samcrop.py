"""Accent reading aid: the Saṃhitā lines of a page region at 450 dpi, each split into halves, stacked; every svarita
stroke above the line gets a red guide line drawn down through the letters, every anudātta bar below gets a blue one.
python3 samcrop.py PDF Y0 Y1 OUT.png   (Y fractions of page height that enclose the Saṃhitā block)"""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,WORK
from PIL import Image,ImageOps,ImageDraw
g=int(sys.argv[1]); a,b=float(sys.argv[2]),float(sys.argv[3]); OUT=sys.argv[4]
path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','450','-gray',path,d+'/p'],check=True)
im=Image.open(d+'/'+os.listdir(d)[0]); subprocess.run(['rm','-rf',d])
W,H=im.size
if os.environ.get('BOX'):   # fractions of the text block exactly as view.py computes it (from a 40 dpi render)
    from view import textbox as vtb
    d=tempfile.mkdtemp(dir=WORK); subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','40','-gray',path,d+'/p'],check=True)
    sm=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d])
    k=450/40; bb=[v*k for v in vtb(sm)]
    a,b=(bb[1]+a*(bb[3]-bb[1]))/H,(bb[1]+b*(bb[3]-bb[1]))/H
reg=im.crop((0,int(H*a),W,int(H*b)))
bw=ImageOps.invert(reg).point(lambda v:255 if v>110 else 0); px=bw.load(); w,h=bw.size
rows=[sum(px[x,y]>0 for x in range(0,w,2)) for y in range(h)]
thr=max(rows)*0.12; lines=[]; y=0
while y<h:
    if rows[y]>thr:
        s=y
        while y<h and rows[y]>thr: y+=1
        if y-s>30: lines.append((s,y))
    y+=1
def marks(s,e):
    """svarita strokes: short thick vertical bars in the band above the letter body; anudātta bars: short
    horizontal bars in the band below it"""
    top=max(0,s-60); st=[]; x=0
    while x<w:
        if any(px[x,yy]>0 for yy in range(top,s-6)):
            x0=x
            while x<w and any(px[x,yy]>0 for yy in range(top,s-6)): x+=1
            hgt=max(sum(px[xx,yy]>0 for yy in range(top,s-6)) for xx in range(x0,x))
            if 4<=x-x0<=18 and hgt>=18: st.append((x0+x)//2)
        x+=1
    ba=[]; x=0; bot=min(h,e+40)
    while x<w:
        if any(px[x,yy]>0 for yy in range(e+4,bot)):
            x0=x
            while x<w and any(px[x,yy]>0 for yy in range(e+4,bot)): x+=1
            hgt=max(sum(px[xx,yy]>0 for yy in range(e+4,bot)) for xx in range(x0,x))
            if 25<=x-x0<=90 and hgt<=12: ba.append((x0+x)//2)
        x+=1
    return st,ba
tiles=[]
for s,e in lines:
    st,ba=marks(s,e)
    cols=[x for x in range(w) if any(px[x,yy]>0 for yy in range(s,e,2))]
    x0,x1=cols[0]-10,cols[-1]+10; mid=(x0+x1)//2
    rgb=reg.convert('RGB'); dr=ImageDraw.Draw(rgb)
    for x in st: dr.line([(x,s-60),(x,e)],fill=(230,0,0),width=2)
    for x in ba: dr.line([(x,s),(x,e+40)],fill=(0,90,255),width=2)
    for xa,xb in ((x0,mid+60),(mid-60,x1)):
        tiles.append(rgb.crop((xa,max(0,s-70),xb,min(h,e+55))))
Wt=max(t.width for t in tiles); m=Image.new('RGB',(Wt,sum(t.height+10 for t in tiles)),(255,255,255)); yy=0
for t in tiles: m.paste(t,(0,yy)); yy+=t.height+10
m.save(OUT); print(len(lines),'lines',m.size)
