"""Thumbnail of a Vol 6 scan page with the line indices of lines_w6a.py drawn in the left margin (for locating lines only).
python3 thumb_w6a.py PDFPAGE OUT.png [DPI=80]"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
from lines_w6a import bands
from PIL import ImageDraw
g,OUT=int(sys.argv[1]),sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 80
im=render(g,dpi).convert('RGB'); W,H=im.size; d=ImageDraw.Draw(im); B=bands(g)
for i,(s,e) in enumerate(B): d.text((2,int(H*(s+e)/2)-5),str(i),fill=(255,0,0))
y0=max(0,int(H*B[0][0])-10); y1=min(H,int(H*B[-1][1])+10); im.crop((0,y0,W,y1)).save(OUT); print(im.crop((0,y0,W,y1)).size)
