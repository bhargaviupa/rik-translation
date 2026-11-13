"""pg_v4c.py PDF N [DPI] -- render a better-scan page, trim margins, cut into N strips -> /tmp/v4num/p{PDF}_{i}.png (width<=1500)"""
import sys,os,subprocess
from PIL import Image
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
g=int(sys.argv[1]); n=int(sys.argv[2]); dpi=int(sys.argv[3]) if len(sys.argv)>3 else 200
path,k=part_of(g); f=f'/tmp/v4num/r{g}_{dpi}'
if not os.path.exists(f+'.png'):
    subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r',str(dpi),'-gray','-png','-singlefile',path,f],check=True)
im=Image.open(f+'.png'); a=np.array(im)<128
rows=np.where(a.sum(1)>dpi//10)[0]; y0,y1=max(0,rows[0]-10),min(im.height,rows[-1]+10)
cols=np.where(a[y0:y1].sum(0)>dpi//20)[0]; x0,x1=max(0,cols[0]-10),min(im.width,cols[-1]+10)
import json
c=im.crop((x0,y0,x1,y1)); H=c.height; sc=min(1,1500/c.width); json.dump(dict(W=im.width,Hp=im.height,x0=int(x0),y0=int(y0),H=int(H),n=n,sc=sc,dpi=dpi),open(f'/tmp/v4num/p{g}.json','w')); print("trim fractions",round(x0/im.width,3),round(y0/im.height,3),round(x1/im.width,3),round(y1/im.height,3))
for i in range(n):
    s=c.crop((0,max(0,int(H*i/n)-20),c.width,min(H,int(H*(i+1)/n)+20)))
    if s.width>1500: s=s.resize((1500,int(s.height*1500/s.width)),Image.LANCZOS)
    s.save(f'/tmp/v4num/p{g}_{i}.png'); print(i,s.size)
