"""Copy the running-head Aṣṭaka/Adhyāya/Varga of odd pages from the English file into the Kannada file's
'*[ಋಗ್ವೇದಸಂಹಿತಾ]*' header lines (as the print has them: 'ಅ. ೨. ಅ. ೨. ವ. ೪.'); doubtful numerals keep [?]."""
import re,sys
sys.path.insert(0,'publish/tools/verify11')
from cfg import EN,KN
K=str.maketrans('0123456789','೦೧೨೩೪೫೬೭೮೯')
en=open(EN,encoding='utf8').read(); kn=open(KN,encoding='utf8').read()
hdr={}
for s in re.split(r'\n(?=### Printed p\. )',en):
    m=re.match(r'### Printed p\. \S+\s+\(.*?PDF (\d+)',s)
    if not m: continue
    h=re.search(r'Header: "Ṛgvedasaṃhitā"; ([^)]*)',s)
    if not h: continue
    h=h.group(1); a=re.search(r'Aṣṭaka (\d+), Adhyāya (\d+)',h)
    v=re.search(r'Varga (?:numeral )?(\d+)( \[\?\])?',h) or re.search(r'varga numeral printed "(\d+)\??"( \[\?\])?',h)
    vs=(v.group(1)+(' [?]' if v.group(2) or '?"' in h else '')) if v else '[?]'
    pre=f'ಅ. {a.group(1)}. ಅ. {a.group(2)}. ' if a else ''
    hdr[int(m.group(1))]=(pre+f'ವ. {vs}.').translate(K)
out=[];n=0
for s in re.split(r'(?=<!-- PDF )',kn):
    m=re.match(r'<!-- PDF (\d+)',s)
    if m and int(m.group(1)) in hdr and '*[ಋಗ್ವೇದಸಂಹಿತಾ]*' in s:
        s=s.replace('*[ಋಗ್ವೇದಸಂಹಿತಾ]*','*['+hdr[int(m.group(1))]+'  ಋಗ್ವೇದಸಂಹಿತಾ]*',1); n+=1
    out.append(s)
new=''.join(out); assert len(new)>=len(kn) and new.count('**Progress note:**')==1
open(KN,'w',encoding='utf8').write(new); print('headers filled',n,'of',kn.count('*[ಋಗ್ವೇದಸಂಹಿತಾ]*'))
