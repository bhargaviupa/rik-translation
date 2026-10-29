"""mon_v4c.py PDF OUT DPI S y0 y1 x0 x1 [x0 x1 ...] -- crops of one band of strip S, placed side by side (no vertical overlap)"""
import sys,os,subprocess
from PIL import Image
g,out,dpi,s,y0,y1=sys.argv[1:7]; xs=sys.argv[7:]; ims=[]
for j in range(0,len(xs),2):
    f=f'/tmp/v4num/mon_{j}.png'
    subprocess.run(['python3',os.path.join(os.path.dirname(os.path.abspath(__file__)),'zs_v4c.py'),g,f,dpi,s,xs[j],y0,xs[j+1],y1],check=True,capture_output=True)
    ims.append(Image.open(f))
W=sum(i.width for i in ims)+12*len(ims); H=max(i.height for i in ims); m=Image.new('L',(W,H),255); x=0
for i in ims: m.paste(i,(x,0)); x+=i.width+12
m.save(out); print(m.size)
