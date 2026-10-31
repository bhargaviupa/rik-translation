"""Log a doubtful reading with its crop (whole-page fractions) while viewing.
python3 doubt.py PDFPAGE Y0 Y1 X0 X1 "what is doubtful / my reading"   -> appends to vol14/review/doubts_v14.json"""
import sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import REVIEW,OFFSET
f=os.path.join(REVIEW,'doubts_v14.json'); d=json.load(open(f)) if os.path.exists(f) else []
g,y0,y1,x0,x1=int(sys.argv[1]),*map(float,sys.argv[2:6])
d.append({'pdf':g,'printed':g-OFFSET-(1 if g>=224 else 0),'crop':[y0,y1,x0,x1],'note':sys.argv[6],'answer':''})
json.dump(d,open(f,'w'),indent=1,ensure_ascii=False); print(len(d),'doubts logged')
