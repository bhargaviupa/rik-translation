"""w6b helper: set accented Saṃhitā lines of a Rik. python3 setverse_w6b.py 'Rik 80.3' 'LINE1' 'LINE2' 'NOTE' [FLAGMARK]
Replaces the '>' lines (2-3) after the heading '...Saṃhitā text of Rik X**' and the optional italic note before them."""
import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
key,*lines=sys.argv[1:]; note=lines.pop()
L=open(EN,encoding='utf8').read().split('\n'); n0=len('\n'.join(L))
i=[k for k,l in enumerate(L) if l.startswith('**॥ संहिताखण्डः ॥') and l.rstrip().endswith(key+'**') or (l.startswith('**॥ संहिताखण्डः ॥') and l.split('Saṃhitā text of ')[-1].startswith(key+'**'))]
assert len(i)==1,i; i=i[0]
j=i+1
while not L[j].startswith('>'): j+=1
k=j
while L[k].startswith('>'): k+=1
new=[f'*({note})*','']+['> '+x for x in lines]
L[i+1:k]=['']+new
u='\n'.join(L); assert len(u)>n0-400
open(EN,'w',encoding='utf8').write(u); print('ok',i+1)
