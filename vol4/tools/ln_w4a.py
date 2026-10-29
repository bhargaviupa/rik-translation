"""ln_w4a.py PDF -- list text-line bands (y0-y1) of the trimmed 120-dpi page made by pg_w4a.py."""
import sys
from PIL import Image
import numpy as np
a=np.array(Image.open(f'/tmp/w4a/p{sys.argv[1]}.png').convert('L'))[:,30:]<110
r=a.sum(1)>3; out=[];y=0
while y<len(r):
    if r[y]:
        s=y
        while y<len(r) and r[y]: y+=1
        if y-s>3: out.append(f'{s}-{y}')
    y+=1
print(' '.join(out))
