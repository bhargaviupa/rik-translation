"""rows_w4b.py PDF -- list text-line bands (page fractions) of the cached 700-dpi render."""
import sys,os,numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
W4=os.environ.get('W4','/tmp/claude-0/-home-user-rik-translation/b3fc490d-ca73-5211-ba91-f6e332c98d63/scratchpad/w')
g=int(sys.argv[1]); f=f'{W4}/hi{g}.png'
if not os.path.exists(f):
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
    from cfg import part_of; import subprocess
    path,k=part_of(g); subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r','700','-gray','-png','-singlefile',path,f[:-4]],check=True)
im=Image.open(f).convert('L'); a=np.asarray(im)<110; H=a.shape[0]
r=a[:,int(a.shape[1]*.1):int(a.shape[1]*.92)].sum(1)>40
bands=[];s=None
for i,v in enumerate(r):
    if v and s is None: s=i
    if not v and s is not None:
        if i-s>25: bands.append((s,i))
        s=None
print(' '.join(f'{s/H:.3f}-{e/H:.3f}' for s,e in bands))
