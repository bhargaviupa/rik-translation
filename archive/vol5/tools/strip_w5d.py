"""w5d: render a PDF page (better scan) cropped to the text block, cut into N horizontal strips at DPI.
python3 strip_w5d.py PDFPAGE OUTPREFIX [dpi=200] [N=4] [only=1,2..]"""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import textbox,render
g,O=int(sys.argv[1]),sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 200; N=int(sys.argv[4]) if len(sys.argv)>4 else 4
k=dpi/40; x0,t0,x1,t1=[int(v*k) for v in textbox(render(g,40))]; im=render(g,dpi); H=t1-t0; ov=int(H*0.02)
for j in range(N):
    im.crop((max(0,x0-8),max(0,t0+H*j//N-ov-8),x1+8,t0+H*(j+1)//N+ov+8)).save(f'{O}{j+1}.png')
print('ok')
