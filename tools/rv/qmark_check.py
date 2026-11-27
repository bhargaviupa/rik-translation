#!/usr/bin/env python3
"""For every `[?]` of a legacy volume's English that follows a number, look for that number in the supplied Kannada text of the page and its neighbours.
  python3 tools/rv/qmark_check.py VOL [--apply]
Output: VOL/review/second_pass/qmark_check.tsv  (line, page, number before the mark, status, supplied numbers near the same place).
status SAME = the number stands in the supplied text of pages p-1..p+1 (digits compared after Kannada numerals -> ASCII, separators -> '-'): the `[?]` may go (user's rule, Nov 24 2026: the supplied numerals are correct).
         NEAR = not found; the supplied text has a number of the same length that differs in one place: shown, nothing changed (the editor decides).
         NONE = nothing comparable.
--apply removes the ` [?]` after every SAME number (one edit per mark, each logged in VOL/review/repair_log.md). The page is the nearest page mark above the line."""
import re,sys,csv,collections,datetime,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import recheck as R
vol=sys.argv[1]; apply='--apply' in sys.argv; d=f'vol{vol}'
KN,NOTIN=R.read_kn(f'{d}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md')
E=f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md'; L=open(E,encoding='utf8').read().split('\n')
KD=str.maketrans('೦೧೨೩೪೫೬೭೮೯','0123456789')
def nums(t):
    t=t.translate(KD); t=re.sub(r'(?<=\d)\s*[-–.:]\s*(?=\d)','-',t)
    return set(re.findall(r'\d+(?:-\d+)*',t))
DV=str.maketrans('०१२३४५६७८९','0123456789')
TOK=re.compile(r'((?:[IVX]+-)?\d+(?:[-–.]\d+)*)((?:,\s*\d+)*)\s*\[\?\]')
cur=0; rows=[]; edits=[]
for i,l in enumerate(L,1):
    for m in re.finditer(r'\((?:p|pp)\. ?(\d+)|### Printed p\. (\d+)|### Page (\d+) \(PDF|### Rik [\d.]+ \(pp?\. (\d+)',l): cur=int([g for g in m.groups() if g][0])
    lt=l.translate(DV)
    for m in TOK.finditer(lt):
        num=re.sub(r'[–.]','-',m.group(1)); 
        if re.match(r'[IVX]+-',num): num=str(R._roman(num.split('-')[0]))+'-'+num.split('-',1)[1]
        pool=set()
        for p in (cur-1,cur,cur+1):
            if p in KN and p not in NOTIN: pool|=nums(KN[p])
        # tail numbers ("19-63, 62 [?]"): all must be found as the last part
        tails=[x.strip() for x in m.group(2).split(',') if x.strip()]
        ok=num in pool and all((num.rsplit('-',1)[0]+'-'+t) in pool or t in pool for t in tails)
        near=[]
        if not ok and num in pool and tails:
            for q in pool:
                for tl in tails:
                    if len(q)==len(tl) and '-' not in q and sum(a!=b for a,b in zip(q,tl))==1: near.append('tail:'+q)
        elif not ok:
            base=num.split('-'); 
            for q in pool:
                qs=q.split('-')
                if len(qs)==len(base) and sum(a!=b for a,b in zip(qs,base))==1 and len(q)==len(num): near.append(q)
        st='SAME' if ok else ('NEAR' if near else 'NONE')
        rows.append((i,cur,m.group(0),st,' '.join(sorted(near))[:80]))
        if ok and apply: edits.append((i,l[m.start():m.end()]))
c=collections.Counter(r[3] for r in rows); print(len(rows),'marks after a number;',dict(c))
with open(f'{d}/review/second_pass/qmark_check.tsv','w',encoding='utf8') as f:
    f.write('english_line\tpage_est\tenglish\tstatus\tsupplied_numbers_differing_in_one_place\n')
    for r in rows: f.write('\t'.join(map(str,r))+'\n')
if apply:
    done=0
    for i,s in edits:
        new=s.replace(' [?]','').replace('[?]','')
        if L[i-1].count(s)==1: L[i-1]=L[i-1].replace(s,new); done+=1
    open(E,'w',encoding='utf8').write('\n'.join(L))
    with open(f'{d}/review/repair_log.md','a',encoding='utf8') as f:
        f.write(f"\n## `[?]` removed where the supplied text prints the same number ({datetime.date.today().isoformat()}, tools/rv/qmark_check.py --apply)\n")
        for i,s in edits: f.write(f"- English line {i}: `{s}` → the same number without `[?]`\n")
    print('removed',done)
