import sys,subprocess
from PIL import Image
n=int(sys.argv[1]); P='/tmp/altwt/w/Rig_Vol8_alt.pdf'
subprocess.run(['pdftoppm','-jpeg','-r','200','-f',str(n),'-l',str(n),P,f'pg{n}'])
im=Image.open(f'pg{n}-{n:03d}.jpg');w,h=im.size
k=int(sys.argv[2]) if len(sys.argv)>2 else 4
step=h/k
for i in range(k):
    im.crop((0,int(i*step-20 if i else 0),w,int(min(h,(i+1)*step+20)))).save(f'pg{n}_{i}.jpg')
print(w,h)
