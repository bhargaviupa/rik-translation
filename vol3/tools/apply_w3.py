"""apply_w3.py BATCH.json -- BATCH = {"start": heading text, "end": text after the unit (exclusive), "edits": [[old,new],...]}.
Every old must occur exactly once inside [start, end); replacements are applied only there."""
import sys,json
F='/home/user/rik-translation/vol3/Rigveda_Samhita_Vol3_English_Translation.md'
t=open(F,encoding='utf8').read(); B=json.load(open(sys.argv[1]))
assert t.count(B['start'])==1,('start',t.count(B['start']))
s=t.index(B['start']); e=t.index(B['end'],s+len(B['start'])); sec=t[s:e]; bad=0
for a,b in B['edits']:
    c=sec.count(a)
    if c!=1: print('COUNT',c,repr(a[:80])); bad=1
if bad: sys.exit(1)
for a,b in B['edits']: sec=sec.replace(a,b)
t2=t[:s]+sec+t[e:]; open(F,'w',encoding='utf8').write(t2)
print('ok', len(B['edits']),'edits; delta',len(t2)-len(t),'; [?] in file',t2.count('[?]'))
