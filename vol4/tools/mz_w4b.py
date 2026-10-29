"""mz_w4b.py PDF OUT SCALE y0 y1 x0 x1 [y0 y1 x0 x1 ...] -- stacked crops (page fractions) from a cached 700-dpi render, scaled by SCALE (1 = 700 dpi)."""
import sys,os,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
W4=os.environ.get('W4','/tmp/claude-0/-home-user-rik-translation/ae235999-b0f9-501d-a9a2-05af5dc4c156/scratchpad/w')
g=int(sys.argv[1]); out=sys.argv[2]; sc=float(sys.argv[3]); v=[float(x) for x in sys.argv[4:]]
f=f'{W4}/hi{g}.png'
if not os.path.exists(f):
    path,k=part_of(g); subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r','700','-gray','-png','-singlefile',path,f[:-4]],check=True)
im=Image.open(f); W,H=im.size; cs=[]
for i in range(0,len(v),4):
    y0,y1,x0,x1=v[i:i+4]; c=im.crop((int(W*x0),int(H*y0),int(W*x1),int(H*y1)))
    cs.append(c.resize((max(1,int(c.width*sc)),max(1,int(c.height*sc)))))
M=Image.new('L',(max(c.width for c in cs),sum(c.height for c in cs)+6*len(cs)),255); y=0
for c in cs: M.paste(c,(0,y)); y+=c.height+6
M.save(out); print(M.size)
