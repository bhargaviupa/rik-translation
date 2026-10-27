"""Text block of pages at low dpi with a ruler (box fractions) on the left, side by side: ruler.py OUT.png PDF..."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
import subprocess,tempfile
from cfg import part_of,WORK
from view import textbox
from PIL import Image,ImageDraw
tiles=[]
for g in map(int,sys.argv[2:]):
    path,n=part_of(g); d=tempfile.mkdtemp(dir=WORK)
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','40','-gray',path,d+'/p'],check=True)
    sm=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d])
    x0,y0,x1,y1=textbox(sm); k=1.5
    d=tempfile.mkdtemp(dir=WORK); subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','60','-gray',path,d+'/p'],check=True)
    im=Image.open(d+'/'+os.listdir(d)[0]).convert('L'); subprocess.run(['rm','-rf',d])
    c=im.crop((int(x0*k),int(y0*k),int(x1*k),int(y1*k))); t=Image.new('L',(c.width+40,c.height+14),255); t.paste(c,(40,14))
    dr=ImageDraw.Draw(t); dr.text((40,0),str(g),fill=0)
    for i in range(0,21):
        y=14+int(c.height*i/20); dr.line([(30,y),(40,y)],fill=0); 
        if i%2==0: dr.text((0,y-5),f'{i*5:02d}',fill=0)
    tiles.append(t)
m=Image.new('L',(sum(t.width+6 for t in tiles),max(t.height for t in tiles)),255); x=0
for t in tiles: m.paste(t,(x,0)); x+=t.width+6
m.save(sys.argv[1]); print(m.size)
