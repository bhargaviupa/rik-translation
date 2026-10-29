"""sam_w4b.py HEADING_PREFIX NOTE LINE1 LINE2 ... -- replace the bold Saṃhitā block (and its IAST paragraph) of the section
starting with HEADING_PREFIX by accented lines; a line may end in ' [accent ?]'. NOTE ('' for none) is added to the standard note."""
import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cfg import EN
from accent import iast
pre,note,lines=sys.argv[1],sys.argv[2],sys.argv[3:]
t=open(EN,encoding='utf8').read(); n0=len(t)
h=t.index('\n'+pre)+1; s=t.index('**Saṃhitā-pāṭha**',h); assert s-h<300
e=t.index('**Pada-pāṭha**',s)
hd=t[s:t.index('\n',s)]; pg=re.search(r'\(p+\. [^;)]*',hd).group(0)
fl=[(l.replace(' [accent ?]',''),' [accent ?]' if l.endswith('[accent ?]') else '') for l in lines]
dv='\n'.join(f'> **{d}**{f}' for d,f in fl)
ia='\n'.join(f'*{iast(d)}*{f}' for d,f in fl)
nt='*(Saṃhitā accents as printed; Pada unaccented.'+(' '+note if note else '')+')*'
new=f'**Saṃhitā-pāṭha** *{pg})*\n\n{dv}\n\n{ia}\n\n{nt}\n\n'
print(t[s:e]); print('->'); print(new)
t=t[:s]+new+t[e:]; assert len(t)>n0-1500
open(EN,'w',encoding='utf8').write(t)
