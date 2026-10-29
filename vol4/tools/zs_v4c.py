"""zs_v4c.py PDF OUT DPI  S x0 y0 x1 y1 [S x0 y0 x1 y1 ...] -- crops given in pixel coords of strip S as shown by pg_v4c.py; re-rendered at DPI and stacked"""
import sys,os,json,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
g=int(sys.argv[1]); out=sys.argv[2]; dpi=sys.argv[3]; a=sys.argv[4:]
P=json.load(open(f'/tmp/v4num/p{g}.json')); fr=[]
for j in range(0,len(a),5):
    s=int(a[j]); x0,y0,x1,y1=[float(v)/P['sc'] for v in a[j+1:j+5]]
    top=max(0,int(P['H']*s/P['n'])-20)
    fr+= [(P['x0']+x0)/P['W'],(P['y0']+top+y0)/P['Hp'],(P['x0']+x1)/P['W'],(P['y0']+top+y1)/P['Hp']]
subprocess.run(['python3',os.path.join(os.path.dirname(os.path.abspath(__file__)),'zc_v4c.py'),str(g),out,dpi]+[f'{v:.4f}' for v in fr],check=True)
