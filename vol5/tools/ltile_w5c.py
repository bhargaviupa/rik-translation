"""w5c: tile of text lines A..B of a PDF page (line numbers as lines_w5c.py gives for the 120-dpi view), at DPI, cut into
N overlapping column pieces stacked top to bottom.  python3 ltile_w5c.py PDFPAGE OUT.png A B [dpi=450] [N=3] [x0 x1]
With A=0 it only prints the line count."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from view import textbox,render
from PIL import Image
def lines(im):
    w,h=im.size; px=im.load(); ink=[sum(px[x,y]<110 for x in range(0,w,2)) for y in range(h)]
    th=max(2,w//2//60); L=[]; y=0
    while y<h:
        if ink[y]>th:
            a=y
            while y<h and ink[y]>th: y+=1
            if y-a>=5: L.append((a,y))
        y+=1
    M=[]
    for a,b in L:
        if M and a-M[-1][1]<3: M[-1]=(M[-1][0],b)
        else: M.append((a,b))
    return M
g,OUT,A,B=int(sys.argv[1]),sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
dpi=int(sys.argv[5]) if len(sys.argv)>5 else 450; N=int(sys.argv[6]) if len(sys.argv)>6 else 3
fx0,fx1=(float(sys.argv[7]),float(sys.argv[8])) if len(sys.argv)>8 else (0,1)
bx=textbox(render(g,40)); k=120/40; x0,t0,x1,t1=[int(v*k) for v in bx]
v=render(g,120); v=v.crop((x0-8,t0-8,x1+8,t1+8)); M=lines(v)
if A==0: print(len(M)); sys.exit()
s=dpi/120; ya=int((t0-8+M[A-1][0]-4)*s); yb=int((t0-8+M[B-1][1]+5)*s)
X0=int((x0-8)*s); X1=int((x1+20)*s); W=X1-X0; X0,X1=X0+int(W*fx0),X0+int(W*fx1); W=X1-X0; ov=int(W*0.05)
im=render(g,dpi)
P=[im.crop((max(0,X0+W*j//N-ov),ya,min(im.size[0],X0+W*(j+1)//N+ov),yb)) for j in range(N)]
w=max(p.size[0] for p in P); out=Image.new('L',(w,sum(p.size[1]+12 for p in P)),255); y=0
for p in P: out.paste(p,(0,y)); y+=p.size[1]+12
out.save(OUT); print(len(M),out.size)
