"""zb.py ID OUT [padx pady width] -- tight 450-dpi crop of a review box, upscaled"""
import sys,os,json,subprocess
from PIL import Image
sys.path.insert(0,'/home/user/rik-translation/vol4/tools')
from cfg import part_of
import glob
R={}
for _f in glob.glob('/home/user/rik-translation/vol4/review/review_PDF*.json'):
    for r in json.load(open(_f)): R[r['id']]=r
k=sys.argv[1]; r=R[k]; g=r['pdf']; f=f'/tmp/v4num/full{g}.png'
if not os.path.exists(f):
    path,n=part_of(g); subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','450','-gray','-png','-singlefile',path,f[:-4]],check=True)
im=Image.open(f); x,y,w,h=[v*1.5 for v in r['box']]; px=int(sys.argv[3]) if len(sys.argv)>3 else 60; py=int(sys.argv[4]) if len(sys.argv)>4 else 30; W=int(sys.argv[5]) if len(sys.argv)>5 else 1200
c=im.crop((int(x-px),int(y-py),int(x+w+px),int(y+h+py))); c=c.resize((W,int(c.height*W/c.width)),Image.LANCZOS); c.save(sys.argv[2]); print(c.size, r['box'])
