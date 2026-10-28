"""zl_v4c.py PDF OUT DPI  S L [xf0 xf1] [; S L xf0 xf1 ...]  -- crop text line L (0-based, as listed by `zl_v4c.py PDF list`) of strip S,
x as fractions of the strip width (default 0 1). Lines are found by horizontal projection of the strip image."""
import sys,os,subprocess
import numpy as np
from PIL import Image
def lines(g,s):
    a=np.array(Image.open(f'/tmp/v4num/p{g}_{s}.png').convert('L'))<140; r=a.sum(1)>2; out=[]; y=0
    while y<len(r):
        if r[y]:
            y1=y
            while y1<len(r) and r[y1]: y1+=1
            if y1-y>=6: out.append((y,y1))
            y=y1
        else: y+=1
    # merge marks (accent strokes / underlines) into adjacent lines: gaps < 6 px
    m=[]
    for l in out:
        if m and l[0]-m[-1][1]<6: m[-1]=(m[-1][0],l[1])
        else: m.append(l)
    return m,a.shape[1]
g=int(sys.argv[1])
if sys.argv[2]=='list':
    for s in (0,1):
        if os.path.exists(f'/tmp/v4num/p{g}_{s}.png'):
            m,w=lines(g,s); print(s,[f'{i}:{a}-{b}' for i,(a,b) in enumerate(m)])
    sys.exit()
out=sys.argv[2]; dpi=sys.argv[3]; specs=' '.join(sys.argv[4:]).split(';'); args=[]
for sp in specs:
    v=sp.split(); s=int(v[0]); L=int(v[1]); xf0,xf1=(float(v[2]),float(v[3])) if len(v)>3 else (0,1)
    m,w=lines(g,s); a,b=m[L]
    args+= [str(s),str(xf0*w),str(a-12),str(xf1*w),str(b+12)]
subprocess.run(['python3',os.path.join(os.path.dirname(os.path.abspath(__file__)),'zs_v4c.py'),str(g),out,dpi]+args,check=True)
