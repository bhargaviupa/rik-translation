"""Several thumb_w6a thumbnails side by side in one image (for locating lines only).
python3 thumbs_w6a.py OUT.png DPI PDFPAGE..."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from lines_w6a import bands
from PIL import Image,ImageDraw
OUT,dpi=sys.argv[1],int(sys.argv[2]); ims=[]
for g in map(int,sys.argv[3:]):
    im=render(g,dpi).convert('RGB'); W,H=im.size; d=ImageDraw.Draw(im); B=bands(g)
    for i,(s,e) in enumerate(B): d.text((2,int(H*(s+e)/2)-5),str(i),fill=(255,0,0))
    d.text((W//2,2),f'PDF {g} = p. {g-19}',fill=(0,0,255)); ims.append(im)
o=Image.new('RGB',(sum(i.width+6 for i in ims),max(i.height for i in ims)),'white'); x=0
for i in ims: o.paste(i,(x,0)); x+=i.width+6
o.save(OUT); print(o.size)
