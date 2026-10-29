"""Zoom crop by fractions of the 120-dpi view.py image (whole text block, margins included).
python3 zoom_w5a.py PDFPAGE OUT.png DPI u0 v0 u1 v1   (fractions 0..1 of that view's width/height)"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render,textbox
g,OUT,dpi=int(sys.argv[1]),sys.argv[2],int(sys.argv[3]); u0,v0,u1,v1=[float(a) for a in sys.argv[4:8]]
x0,t0,x1,t1=[v*dpi/40 for v in textbox(render(g,40))]; m=8*dpi/120
W=x1-x0+2*m; H=t1-t0+2*m; im=render(g,dpi)
im.crop((int(x0-m+u0*W),int(t0-m+v0*H),int(x0-m+u1*W),int(t0-m+v1*H))).save(OUT); print(im.size)
