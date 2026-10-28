"""Accent zoom: acc.py PDF Y0FRAC Y1FRAC OUT.png [x0frac x1frac] — 450 dpi strip of the page (fractions of page height/width)"""
import sys,os,subprocess,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,WORK
from PIL import Image
g=int(sys.argv[1]); a,b=float(sys.argv[2]),float(sys.argv[3]); OUT=sys.argv[4]
x0,x1=(float(sys.argv[5]),float(sys.argv[6])) if len(sys.argv)>6 else (0.08,0.92)
path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','450','-gray',path,d+'/p'],check=True)
im=Image.open(d+'/'+os.listdir(d)[0]); subprocess.run(['rm','-rf',d])
W,H=im.size; c=im.crop((int(W*x0),int(H*a),int(W*x1),int(H*b))); c.save(OUT); print(c.size)
