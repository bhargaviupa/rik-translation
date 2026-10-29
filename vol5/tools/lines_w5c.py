"""w5c: list text-line y-ranges of a 120-dpi view image (from view.py), numbered from 1.  python3 lines_w5c.py VIEW.png"""
import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('L'); w,h=im.size; px=im.load()
ink=[sum(px[x,y]<110 for x in range(0,w,2)) for y in range(h)]
th=max(2,w//2//60); L=[];y=0
while y<h:
    if ink[y]>th:
        a=y
        while y<h and ink[y]>th: y+=1
        if y-a>=5: L.append((a,y))
    y+=1
# merge fragments closer than 3 px
M=[]
for a,b in L:
    if M and a-M[-1][1]<3: M[-1]=(M[-1][0],b)
    else: M.append((a,b))
print(' '.join(f'{i}:{a}-{b}' for i,(a,b) in enumerate(M,1)))
