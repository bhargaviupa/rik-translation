"""rl_w4b.py PDF OUT y0 y1 x0 x1 [SCALE] -- crop (page fractions) from the cached 700-dpi render with a left ruler labelled every 0.005 of page height."""
import sys,os,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
from PIL import Image,ImageDraw
Image.MAX_IMAGE_PIXELS=None
W4=os.environ.get('W4','/tmp/w4b')
g=int(sys.argv[1]); out=sys.argv[2]; y0,y1,x0,x1=[float(v) for v in sys.argv[3:7]]; sc=float(sys.argv[7]) if len(sys.argv)>7 else 0.25
f=f'{W4}/hi{g}.png'
if not os.path.exists(f):
    path,k=part_of(g); subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r','700','-gray','-png','-singlefile',path,f[:-4]],check=True)
im=Image.open(f); W,H=im.size
c=im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1))); c=c.resize((int(c.width*sc),int(c.height*sc)))
M=Image.new('L',(c.width+60,c.height),255); M.paste(c,(60,0)); d=ImageDraw.Draw(M)
t=round(y0*200)/200
while t<=y1:
    yy=int((t-y0)*H*sc)
    if yy>=0: d.line((0,yy,55,yy),fill=0); d.text((2,yy+1),f'{t:.3f}',fill=0)
    t+=0.005
M.save(out); print(M.size)
