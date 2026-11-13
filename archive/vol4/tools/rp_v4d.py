"""rp_v4d.py PDF OUT [DPI] [y0 y1 [x0 x1]] -- render one better-scan page (global PDF number), optional crop by page fractions."""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
from PIL import Image
g=int(sys.argv[1]); out=sys.argv[2]; dpi=int(sys.argv[3]) if len(sys.argv)>3 else 120
fr=[float(v) for v in sys.argv[4:]]
path,k=part_of(g); d=tempfile.mkdtemp()
subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r',str(dpi),'-gray','-png','-singlefile',path,d+'/p'],check=True)
im=Image.open(d+'/p.png'); W,H=im.size
if fr:
    y0,y1=fr[0],fr[1]; x0,x1=(fr[2],fr[3]) if len(fr)>3 else (0,1)
    im=im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1)))
im.save(out); print(im.size)
