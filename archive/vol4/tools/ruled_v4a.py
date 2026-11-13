"""ruled_v4a.py PDF N -- run zoom_strips.py PDF N, then write /tmp/v4num/r{PDF}_{i}.png: each strip resized to 2000 px wide (the view size) with a grey ruler every 50 px (labels = the coordinates zc_v4a.py takes)"""
import sys,os,subprocess
from PIL import Image,ImageDraw
g,n=sys.argv[1],int(sys.argv[2]); here=os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable,os.path.join(here,'zoom_strips.py'),g,str(n)],check=True,stdout=subprocess.DEVNULL)
for i in range(n):
    im=Image.open(f'/tmp/v4num/s{g}_{i}.png').convert('RGB'); im=im.resize((2000,int(im.height*2000/2400)),Image.LANCZOS)
    d=ImageDraw.Draw(im)
    for y in range(0,im.height,50):
        d.line((0,y,25 if y%100 else 45,y),fill=(255,0,0),width=2)
        if y%100==0: d.text((48,y-6),str(y),fill=(255,0,0))
    for x in range(0,2000,100):
        d.line((x,0,x,20),fill=(0,0,255),width=2); d.text((x+3,22),str(x),fill=(0,0,255))
    im.save(f'/tmp/v4num/r{g}_{i}.png')
print('ok')
