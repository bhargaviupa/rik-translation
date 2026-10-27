"""Replace the Saṃhitā-pāṭha block of a Ṛk with accented lines read from the print.
python3 sam.py BATCH.json   BATCH = [[page_heading_prefix, ["deva line 1", "deva line 2", ...]], ...]
The block is the first '> ' run after '**॥ Saṃhitā-pāṭhaḥ ॥**' in the section whose heading starts with the prefix."""
import sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
from accent import iast
t=open(EN,encoding='utf8').read(); n0=len(t)
for pre,lines in json.load(open(sys.argv[1])):
    h=t.index('\n'+pre)+1
    s=t.index('**॥ Saṃhitā-pāṭhaḥ ॥**',h); assert s-h<20000,(pre,'no Saṃhitā block near')
    a=t.index('\n>',s)+1; b=a
    while t.startswith('>',b): b=t.index('\n',b)+1
    old=t[a:b]
    flag=lambda l:(l.replace('[accent ?]','').rstrip(),' [accent ?]' if '[accent ?]' in l else '')
    dv=[flag(l) for l in lines]
    new=''.join(f'> {d}{f}\n' for d,f in dv)+'>\n'+''.join(f'> *{iast(d)}*{f}\n' for d,f in dv)
    print(pre,'\n',old,'->\n',new)
    t=t[:a]+new+t[b:]
assert len(t)>n0-2000
open(EN,'w',encoding='utf8').write(t)
