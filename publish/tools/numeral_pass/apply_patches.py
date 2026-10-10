import json,re,sys
f='/home/user/rik-translation/Rigveda_Samhita_Vol8_English_Translation.md'
S='/tmp/claude-0/-home-user-rik-translation/4b61173c-0ed7-5073-81ed-e66fb47d38a4/scratchpad/agents/'
names=sys.argv[1:]
s=open(f,encoding='utf-8').read(); before=len(s)
def section(s,page):
    m=re.search(r'^### Page %d \(PDF \d+\)\s*$'%page,s,re.M)
    if not m: return None
    n=re.search(r'^### Page \d+ \(PDF \d+\)\s*$',s[m.end():],re.M)
    return m.start(), m.end()+(n.start() if n else len(s)-m.end())
patches=[]
for n in names:
    d=json.load(open(S+f'patches_{n}.json'))
    for p in d['patches']: p['agent']=n; patches.append(p)
ok=0;failed=[]
for p in patches:
    old,new=p['old'],p['new']; done=False
    for pg in (p['page'],p['page']-1,p['page']+1):
        r=section(s,pg)
        if not r: continue
        a,b=r; sec=s[a:b]
        if sec.count(old)==1:
            if new=='':
                i=sec.index(old); j=i-1 if i>0 and sec[i-1]==' ' else i
                sec=sec[:j]+sec[i+len(old):]
            else: sec=sec.replace(old,new,1)
            s=s[:a]+sec+s[b:]; ok+=1; done=True; break
        if sec.count(old)>1: break
    if not done: failed.append((p['agent'],p['page'],old[:70]))
assert s.count('**Progress note:**')==1 and len(s)>before-20000
open(f,'w',encoding='utf-8').write(s)
print('applied',ok,'failed',len(failed))
for x in failed: print(x)
