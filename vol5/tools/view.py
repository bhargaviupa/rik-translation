"""Render a PDF page of the Vol 5 scan, cropped to the text block, for viewing.
python3 view.py PDFPAGE OUT.png [DPI] [y0 y1] [x0 x1]   (fractions of the text block; default 130 dpi, whole block)"""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,SCAN
from PIL import Image,ImageOps,ImageFilter
def textbox(im):
    b=ImageOps.invert(im).point(lambda v:255 if v>100 else 0).filter(ImageFilter.MedianFilter(3)); w,h=b.size; px=b.load()
    rows=[y for y in range(h) if sum(px[x,y]>0 for x in range(0,w,2))>w*0.004]
    cols=[x for x in range(w) if sum(px[x,y]>0 for y in range(0,h,2))>h*0.004]
    return (cols[0],rows[0],cols[-1],rows[-1]) if rows and cols else (0,0,w,h)
def render(g,r):
    d=tempfile.mkdtemp(dir=WORK); subprocess.run(['pdftoppm','-f',str(g),'-l',str(g),'-r',str(r),'-gray',SCAN,d+'/p'],check=True)
    im=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d]); return im
if __name__=='__main__':
    g,OUT=int(sys.argv[1]),sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 130
    y0,y1=(float(sys.argv[4]),float(sys.argv[5])) if len(sys.argv)>5 else (0,1)
    x0f,x1f=(float(sys.argv[6]),float(sys.argv[7])) if len(sys.argv)>7 else (0,1)
    k=dpi/40; x0,t0,x1,t1=[int(v*k) for v in textbox(render(g,40))]
    im=render(g,dpi); H=t1-t0; W=x1-x0
    im.crop((max(0,x0+int(W*x0f)-8),t0+int(H*y0)-8,x0+int(W*x1f)+8,t0+int(H*y1)+8)).save(OUT); print(im.size)
