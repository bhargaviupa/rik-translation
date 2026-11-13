"""Full-width strip of a page spanning review boxes ID1..ID2 (same PDF page), at 300 dpi scaled.
python3 zoom.py REVIEW.json ID1 ID2 OUT.png [scale]"""
import sys,os,json,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image
R={r['id']:r for r in json.load(open(sys.argv[1]))}; a,b=R[sys.argv[2]],R[sys.argv[3]]; OUT=sys.argv[4]
sc=float(sys.argv[5]) if len(sys.argv)>5 else 0.6
g=a['pdf']; path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray',path,d+'/p'],check=True)
im=Image.open(d+'/'+os.listdir(d)[0]); subprocess.run(['rm','-rf',d])
y0=min(a['box'][1],b['box'][1])-30; y1=max(a['box'][1]+a['box'][3],b['box'][1]+b['box'][3])+30
c=im.crop((0,max(0,y0),im.width,y1)); c=c.resize((int(c.width*sc),int(c.height*sc))); c.save(OUT); print(c.size)
