import sys,subprocess
from PIL import Image
# usage: mont.py PDF OUT DPI "line x0 x1" ...
pdf,out,dpi=sys.argv[1],sys.argv[2],sys.argv[3]
ims=[]
for k,s in enumerate(sys.argv[4:]):
    l,a,b=s.split()
    f=f'/tmp/v3num/_m{k}.png'
    subprocess.run(['python3','zl_w3.py',pdf,l,a,b,f,dpi],check=True,capture_output=True)
    ims.append(Image.open(f))
W=max(i.width for i in ims);H=sum(i.height for i in ims)+10*len(ims)
o=Image.new('L',(W,H),255);y=0
for i in ims: o.paste(i,(0,y)); y+=i.height+10
o.save(out); print(o.size)
