#!/usr/bin/env python3
"""For every `[?]` of a legacy volume's English that is NOT after a number: the word(s) before it, converted to Kannada and aligned with the supplied Kannada of the
page (estimated: nearest page mark above, window p-1..p+1; p-2..p+2 when nothing is found). Report only (nothing is changed):
  python3 tools/rv/qword_check.py VOL      -> VOL/review/second_pass/qword_check.tsv
columns: english_line, page_est, text before the mark, word(s) aligned, best alignment %, the supplied words around the alignment.
Uses the functions of tools/rv/recheck.py (qmark_context: Devanagari run or IAST word before the mark -> Kannada letters -> rapidfuzz alignment)."""
import re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import recheck as R
vol=sys.argv[1]; d=f'vol{vol}'
KN,NOTIN=R.read_kn(f'{d}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md')
L=open(f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md',encoding='utf8').read().split('\n')
cur=0; out=[]
for i,l in enumerate(L,1):
    for m in re.finditer(r'\((?:p|pp)\. ?(\d+)|### Printed p\. (\d+)|### Page (\d+) \(PDF|### Rik [\d.]+ \(pp?\. (\d+)',l): cur=int([g for g in m.groups() if g][0])
    if '[?]' not in l or not (1<=cur<=10**4): continue
    for k,m in enumerate(re.finditer(r'\[\?\]',l)):
        pre=l[:m.start()]
        if re.search(r'[\d०-९]\s*(?:[-–,]\s*[\d०-९]+\s*)*$',pre): continue       # a number: qmark_check.py
        found=None
        for w in (1,2):
            pages=[p for p in range(cur-w,cur+w+1) if p in KN and p not in NOTIN]
            hay_raw='\n'.join(KN[p] for p in pages); 
            if not hay_raw: continue
            hay=R.norm_kn(hay_raw)
            r=R.qmark_context(l[:m.end()],hay_raw,hay)
            # qmark_context lists every mark of the line: take the k-th
            if len(r)>k and r[k][3]:
                lab,q,sc,s,e=r[k][3]; found=(lab,sc,R.kn_words_around(hay_raw,hay,s,e)); 
                if sc>=90: break
        out.append((i,cur,pre[-60:].replace('\n',' '),found))
with open(f'{d}/review/second_pass/qword_check.tsv','w',encoding='utf8') as f:
    f.write('english_line\tpage_est\ttext_before\taligned\tscore\tsupplied_words\n')
    for i,p,t,fd in out: f.write(f"{i}\t{p}\t{t}\t{fd[0] if fd else ''}\t{round(fd[1]) if fd else ''}\t{fd[2] if fd else ''}\n")
import collections
c=collections.Counter('none' if not fd else ('>=95' if fd[1]>=95 else ('80-94' if fd[1]>=80 else '<80')) for *_,fd in out); print(len(out),'marks at words;',dict(c))
