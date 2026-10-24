"""Resolve merge conflicts between the numeral branch (ours) and main's better-scan pass (theirs) in the two Vol 11 files.
Per conflict hunk, start from theirs (words, headers); inside it, take our numeral where theirs is [?]/missing a number;
where both read a different number, take ours (the user's reading) and report it.  python3 resolve_merge.py FILE..."""
import re,sys,difflib
NUMTOK=r'[0-9೦-೯]+(?:[-–.][0-9೦-೯?\[\]]+)*|\[\?\]'
def numish(s):
    s2=re.sub(r'\[as\s+printed\]|\[\?\]|[\s()\[\];:,.।॥‖|*-]','',s)
    return bool(re.search(r'[0-9೦-೯]',s)) and re.fullmatch(r'[0-9೦-೯ನೇರಿಂದತೋto]*',s2) is not None
def resolve(a,b,report,where):
    aw=re.split(r'(\s+)',a); bw=re.split(r'(\s+)',b); out=[]
    sm=difflib.SequenceMatcher(None,aw,bw,autojunk=False)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        A=''.join(aw[i1:i2]); B=''.join(bw[j1:j2])
        if tag=='equal': out.append(B); continue
        if A and numish(A) and (not B or numish(B) or '[?]' in B):
            da=re.sub(r'\D','',A.translate(str.maketrans('೦೧೨೩೪೫೬೭೮೯','0123456789'))); db=re.sub(r'\D','',B.translate(str.maketrans('೦೧೨೩೪೫೬೭೮೯','0123456789')))
            if '[?]' in B.replace('[as printed]','') or not db: out.append(A)
            elif '[?]' in A.replace('[as printed]','') and '[?]' not in B: out.append(B)
            elif da==db: out.append(A if 'as printed' in A else B)
            else: out.append(A); report.append(f'{where}: ours {A.strip()!r} vs main {B.strip()!r} -> ours')
        else: out.append(B)
    return ''.join(out)
for f in sys.argv[1:]:
    t=open(f,encoding='utf8').read(); rep=[]
    def sub(m):
        pg=re.findall(r'PDF (\d+)',t[:m.start()]); return resolve(m.group(1),m.group(2),rep,f'{f[20:24]} PDF{pg[-1] if pg else "?"}')
    t2=re.sub(r'<<<<<<< HEAD\n(.*?)=======\n(.*?)>>>>>>> [^\n]*\n',sub,t,flags=re.S)
    assert '<<<<<<<' not in t2 and '>>>>>>>' not in t2 and t2.count('**Progress note:**')==1, 'unresolved or progress-note problem'
    open(f,'w',encoding='utf8').write(t2); print(f,'resolved'); print('\n'.join(rep))
