"""qlist.py A B [W] -- print each [?] (and 'Pā. ...?' placeholders) in file lines A..B with W chars of context"""
import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
a,b=int(sys.argv[1]),int(sys.argv[2]); W=int(sys.argv[3]) if len(sys.argv)>3 else 110
L=open(EN,encoding='utf8').read().split('\n')
for i in range(a-1,min(b,len(L))):
    for m in re.finditer(r'\[\?\]',L[i]):
        print(f'{i+1}: …{L[i][max(0,m.start()-W):m.start()]}⟦?⟧{L[i][m.end():m.end()+50]}')
