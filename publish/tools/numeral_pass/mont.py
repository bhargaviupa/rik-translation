import sys,subprocess,glob,os,json
from PIL import Image,ImageDraw
# mont.py alt k out.jpg 'strip,x,y,w,h;strip,x,y,w,h;...'
n,k,out,spec=sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4]
P='/tmp/altwt/w/Rig_Vol8_alt.pdf'
im=Image.open(f'pg{n}-{int(n):03d}.jpg');H=im.size[1];step=H/k
tiles=[]
for i,t in enumerate(spec.split(';')):
    s,x,y,w,h=map(int,t.split(','))
    y0=int(s*step-20 if s else 0);Y=y0+y
    subprocess.run(['pdftoppm','-jpeg','-r','600','-f',n,'-l',n,'-x',str(int(x*3)),'-y',str(int(Y*3)),'-W',str(int(w*3)),'-H',str(int(h*3)),P,f'/tmp/zm{os.getpid()}_'])
    f=sorted(glob.glob(f'/tmp/zm{os.getpid()}_*.jpg'))[-1];tiles.append((i+1,Image.open(f).convert('RGB')));[os.remove(g) for g in glob.glob(f'/tmp/zm{os.getpid()}_*.jpg')]
W=max(t.width for _,t in tiles)+60;Ht=sum(t.height+6 for _,t in tiles)
M=Image.new('RGB',(W,Ht),'white');d=ImageDraw.Draw(M);yy=0
for i,t in tiles:
    d.text((2,yy+t.height//2-5),str(i),fill='red');M.paste(t,(40,yy));yy+=t.height+6
M.save(out)
