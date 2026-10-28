"""Show the paragraph(s) around an uncertainty marker on a printed page of the Vol 4 file, with the PDF page(s).
python3 hedge.py en|gaps PRINTED REGEX [CHARS]"""
import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
from pages import printed
f={'en':EN}[sys.argv[1]]; p=sys.argv[2]; rx=re.compile(sys.argv[3],re.I); w=int(sys.argv[4]) if len(sys.argv)>4 else 500
t=open(f,encoding='utf8').read()
m=re.search(r'^### Pages? '+re.escape(p)+r'\b.*$',t,re.M); n=re.search(r'^### Page',t[m.end():],re.M)
sec=t[m.start():(m.end()+n.start() if n else len(t))]
print('PDF',[g for g in range(1,946) if printed(g)==p])
for q in rx.finditer(sec): print('---',sec[max(0,q.start()-w):q.end()+150])
