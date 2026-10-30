"""Append one line to vol14/vol14_pass_log.md: pass_log.py LABEL NOTE-FILE"""
import sys,os,datetime
sys.path.insert(0,os.path.dirname(__file__))
from cfg import EN,VOL
t=open(EN,encoding='utf8').read()
note=open(sys.argv[2],encoding='utf8').read().strip().replace('\n',' ')
open(os.path.join(VOL,'vol14_pass_log.md'),'a',encoding='utf8').write(f"{datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M} {sys.argv[1]}: [?] in file {t.count('[?]')}. {note}\n")
