"""strips.py PDF N -- full page 450dpi, trim blank margins, cut into N overlapping strips, 2400px wide -> /tmp/v3num/s{PDF}_{i}.png"""
import sys,os,subprocess
from PIL import Image
import numpy as np
sys.path.insert(0,'/home/user/rik-translation/vol3/tools')
from cfg import part_of
g=int(sys.argv[1]); n=int(sys.argv[2]); f=f'/tmp/v3num/full{g}.png'
if not os.path.exists(f):
    path,k=part_of(g); subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r','450','-gray','-png','-singlefile',path,f[:-4]],check=True)
im=Image.open(f); a=np.array(im)<128
rows=np.where(a.sum(1)>3)[0]; cols=np.where(a.sum(0)>3)[0]
y0,y1=max(0,rows[0]-20),min(im.height,rows[-1]+20); x0,x1=max(0,cols[0]-20),min(im.width,cols[-1]+20)
# drop stray specks: use rows with real ink (>40 px)
rows=np.where(a.sum(1)>40)[0]; y0,y1=max(0,rows[0]-30),min(im.height,rows[-1]+30)
cols=np.where(a[y0:y1].sum(0)>20)[0]; x0,x1=max(0,cols[0]-30),min(im.width,cols[-1]+30)
c=im.crop((x0,y0,x1,y1)); H=c.height
for i in range(n):
    s=c.crop((0,max(0,int(H*i/n)-50),c.width,min(H,int(H*(i+1)/n)+50)))
    s=s.resize((2400,int(s.height*2400/s.width)),Image.LANCZOS); s.save(f'/tmp/v3num/s{g}_{i}.png'); print(i,s.size)
print('trim',x0,y0,x1,y1)
import json; json.dump(dict(x0=int(x0),y0=int(y0),x1=int(x1),y1=int(y1),H=int(H),n=n),open(f'/tmp/v3num/s{g}.json','w'))
