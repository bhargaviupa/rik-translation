"""Crop a review box with some context: python3 crop.py ID OUT.png  (uses the review JSON boxes, 300-dpi page coords)"""
import sys,os,json,glob,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import WORK,part_of
from PIL import Image
k=sys.argv[1]; g=int(k.split('_')[0])
R={}
for f in glob.glob(os.path.join(os.path.dirname(__file__),'../../../../docs/numeral_review/vol2/review_PDF*.json')):
    for x in json.load(open(f)): R[x['id']]=x
x,y,w,h=R[k]['box']; path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','300','-gray',path,d+'/p'],check=True)
im=Image.open(d+'/'+os.listdir(d)[0]); W=im.size[0]
im.crop((0,max(0,y-int(sys.argv[3]) if len(sys.argv)>3 else y-25),W,y+h+25)).save(sys.argv[2]); subprocess.run(['rm','-rf',d])
