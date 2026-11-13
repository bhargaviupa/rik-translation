"""sam_w3.py BATCH.json -- for sections whose Saṃhitā is inline ('**Saṃhitā-pāṭha** *(accent-marks …)*: deva\n*iast*'):
BATCH = [[heading_prefix, page_label, ["deva line", ...], ["iast line", ...], extra_note_or_empty], ...]
replaces those two lines with the accented blockquote form used from Sūkta 31 on. iast lines may be null -> accent.iast."""
import sys,os,json,re
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN
from accent import iast
t=open(EN,encoding='utf8').read(); n0=len(t)
for pre,pg,dl,il,note in json.load(open(sys.argv[1])):
    h=t.index('\n'+pre)+1
    s=t.index('**Saṃhitā-pāṭha**',h); assert s-h<3000,(pre,'no inline Saṃhitā')
    e=t.index('\n',t.index('\n',s)+1)+1          # end of the IAST line
    old=t[s:e]; assert old.split('\n')[1].startswith('*'),old
    fl=lambda l:(l.replace(' [accent ?]','').replace('[accent ?]','').rstrip(),' [accent ?]' if '[accent ?]' in l else '')
    dv=[fl(l) for l in dl]
    il=il or [iast(d) for d,_ in dv]
    new=f'**Saṃhitā-pāṭha** *({pg})*\n\n'+''.join(f'> {d}{f}\n' for d,f in dv)+'>\n'+''.join(f'> *{x}*{f}\n' for x,(d,f) in zip(il,dv))
    new+='\n*(Saṃhitā accents as printed; Pada unaccented.'+(' '+note if note else '')+')*\n'
    print(new); t=t[:s]+new+t[e:]
assert len(t)>n0-3000
open(EN,'w',encoding='utf8').write(t)
