"""zc_v4c.py PDF OUT DPI fx0 fy0 fx1 fy1 [fx0 fy0 fx1 fy1 ...] -- crops (fractions of the full page) rendered at DPI, stacked; width capped at 1500"""
import sys,os,subprocess
from PIL import Image
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import part_of
g=int(sys.argv[1]); out=sys.argv[2]; dpi=int(sys.argv[3]); a=[float(x) for x in sys.argv[4:]]
path,k=part_of(g); W,H=8.27*dpi,11.69*dpi
import re
info=subprocess.run(['pdfinfo','-f',str(k),'-l',str(k),path],capture_output=True,text=True).stdout
m=re.search(r'Page\s+%d size:\s+([\d.]+) x ([\d.]+)'%k,info)
if m: W,H=float(m.group(1))*dpi/72,float(m.group(2))*dpi/72
tiles=[]
for j in range(0,len(a),4):
    x0,y0,x1,y1=a[j:j+4]; f=f'/tmp/v4num/zc{g}_{j}'
    subprocess.run(['pdftoppm','-f',str(k),'-l',str(k),'-r',str(dpi),'-gray','-png','-singlefile','-x',str(int(x0*W)),'-y',str(int(y0*H)),'-W',str(int((x1-x0)*W)),'-H',str(int((y1-y0)*H)),path,f],check=True)
    c=Image.open(f+'.png')
    if c.width>1500: c=c.resize((1500,int(c.height*1500/c.width)),Image.LANCZOS)
    tiles.append(c)
Wm=max(t.width for t in tiles); Hm=sum(t.height+8 for t in tiles); m=Image.new('L',(Wm,Hm),255); y=0
for t in tiles: m.paste(t,(0,y)); y+=t.height+8
m.save(out); print(m.size)
