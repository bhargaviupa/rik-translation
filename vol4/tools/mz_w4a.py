"""mz_w4a.py PDF DPI OUT x0 y0 x1 y1 [x0 y0 x1 y1 ...] -- several crops (120-dpi trimmed coords of pg_w4a.py) re-rendered at DPI, stacked."""
import sys,subprocess,os
from PIL import Image
g,dpi,out=sys.argv[1],sys.argv[2],sys.argv[3]; a=sys.argv[4:]; tiles=[]
here=os.path.dirname(os.path.abspath(__file__))
for j in range(0,len(a),4):
    subprocess.run([sys.executable,os.path.join(here,'pg_w4a.py'),g,'z',dpi,*a[j:j+4],f'/tmp/w4a/_t{j}.png'],check=True,stdout=subprocess.DEVNULL)
    tiles.append(Image.open(f'/tmp/w4a/_t{j}.png'))
W=max(t.width for t in tiles); H=sum(t.height+12 for t in tiles); m=Image.new('L',(W,H),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height+12
m.save(out); print(out,m.size)
