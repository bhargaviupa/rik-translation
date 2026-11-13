"""Crop of the full rendered page (no text-block detection), by page fractions.
python3 page_v5a.py PDFPAGE OUT.png DPI y0 y1 [x0 x1]"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
g,OUT,dpi=int(sys.argv[1]),sys.argv[2],int(sys.argv[3]); y0,y1=float(sys.argv[4]),float(sys.argv[5])
x0,x1=(float(sys.argv[6]),float(sys.argv[7])) if len(sys.argv)>7 else (0,1)
im=render(g,dpi); w,h=im.size; im.crop((int(w*x0),int(h*y0),int(w*x1),int(h*y1))).save(OUT); print(w,h)
