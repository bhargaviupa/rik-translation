"""w5b helper: list the text-line bands of a page as whole-page fractions (for tight zoom crops with view_v5b.py).
python3 lines_w5b.py PDFPAGE"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import render
im=render(int(sys.argv[1]),60); W,H=im.size; px=im.load()
ink=[sum(1 for x in range(int(W*.05),int(W*.97)) if px[x,y]<120) for y in range(H)]
bands=[];y=0
while y<H:
    if ink[y]>2:
        a=y
        while y<H and ink[y]>2: y+=1
        bands.append((a,y))
    y+=1
for i,(a,b) in enumerate(bands): print(i,f'{a/H:.3f}-{b/H:.3f}',max(ink[a:b]))
