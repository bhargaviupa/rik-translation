"""zc_w4b.py PDF OUT Y0 Y1 X0 X1 [DPI] -- crop page-fraction box from a cached 700-dpi render (fractions of the full page), scaled to DPI (default 700)."""
import sys,os,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
g=int(sys.argv[1]); out=sys.argv[2]; y0,y1,x0,x1=[float(v) for v in sys.argv[3:7]]
f=f'/tmp/claude-0/-home-user-rik-translation/ae235999-b0f9-501d-a9a2-05af5dc4c156/scratchpad/w/hi{g}.png'
if not os.path.exists(f):
    path,k=part_of(g); subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r','700','-gray','-png','-singlefile',path,f[:-4]],check=True)
im=Image.open(f); W,H=im.size
im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))).save(out); print(im.size)
