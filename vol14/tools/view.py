"""Render a PDF page (or a crop) of the Vol 14 scan for viewing. Crops are WHOLE-PAGE fractions (one coordinate system everywhere).
python3 view.py PDFPAGE OUT.png [DPI] [y0 y1] [x0 x1]   (default 100 dpi, whole page). Pages stored upside down (cfg.flipped) are rotated upright."""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of,flipped
from PIL import Image
def render(g,r,flip=None):
    if flip is None: flip=flipped(g)
    p,n=part_of(g); d=tempfile.mkdtemp(dir=WORK); subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(r),'-gray',p,d+'/p'],check=True)
    im=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d]); return im.rotate(180) if flip else im
def crop(g,dpi,y0=0,y1=1,x0=0,x1=1,flip=None):
    im=render(g,dpi,flip); W,H=im.size
    return im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1)))
if __name__=='__main__':
    g,OUT=int(sys.argv[1]),sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 100
    y0,y1=(float(sys.argv[4]),float(sys.argv[5])) if len(sys.argv)>5 else (0,1)
    x0,x1=(float(sys.argv[6]),float(sys.argv[7])) if len(sys.argv)>7 else (0,1)
    im=crop(g,dpi,y0,y1,x0,x1); im.save(OUT); print(im.size)
