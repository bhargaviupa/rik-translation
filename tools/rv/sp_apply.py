#!/usr/bin/env python3
"""Second pass, step S3: carry out a batch's applied repairs, one exact place each, every one logged.

  python3 tools/rv/sp_apply.py VOL EDITS.tsv [--dry]

EDITS.tsv (tab separated, header line): page, target (en|kn), old, new, kind, basis
  en: `old` must stand exactly ONCE inside the page's `### Page N` section of volN/Rigveda_Samhita_VolN_English_Translation.md; it is replaced by `new`.
      A line of volN/review/repair_log.md is written.
  kn: `old` must stand exactly once inside the page's `<!-- printed N -->` section of the Kannada book; it is replaced.  The same text is replaced in the
      supplied file volN/html/*.md when it stands exactly once in the files (else only the book changes and the result says so).
      A row of volN/data/source_fixes.tsv is written (place, as supplied, as corrected, reason, basis, who decided).
An edit whose `old` is not found exactly once is NOT applied and is reported (result file EDITS.result.tsv: status applied|not_found|ambiguous|same).
Nothing is guessed; the progress note at the end of the English file is never touched."""
import re,sys,os,glob,csv,datetime
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import sp_sanskrit,recheck
def main():
    a=sys.argv[1:]
    if len(a)<2: sys.exit(__doc__)
    vol,ed=a[0],a[1]; dry='--dry' in a; d=f'vol{vol}'
    en_p=f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md'; kn_p=f'{d}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md'
    en_ps=[en_p]+sorted(glob.glob(f'{d}/Rigveda_Samhita_Vol{vol}_*English_Translation.md')); en_ps=[p for i,p in enumerate(en_ps) if os.path.exists(p) and p not in en_ps[:i]]
    ENS={p:open(p,encoding='utf8').read() for p in en_ps}; KN=open(kn_p,encoding='utf8').read()
    src={p:open(p,encoding='utf8').read() for p in sorted(glob.glob(f'{d}/html/rig_*.md'))}
    KNP,_=recheck.read_kn(kn_p)
    rows=list(csv.DictReader(open(ed,encoding='utf8'),delimiter='\t',quoting=csv.QUOTE_NONE)); res=[]; log=[]; fixes=[]; today=datetime.date.today().isoformat()
    def sections(t,pat,page):
        """all sections whose heading carries this page (a page may have two headings, e.g. a 'lower part'): list of (start, end)"""
        out=[]; nxt=re.compile(pat.replace('%s','[^\\s—:>]+'))
        for m in re.finditer(pat%re.escape(str(page)),t):
            n=nxt.search(t,m.end()); out.append((m.start(),n.start() if n else len(t)))
        if pat.startswith('(?m)^### Page') and str(page).isdigit():      # a combined heading 'Pages 46–47' / 'Page 15–16' carries every page of its range
            for m in re.finditer(r'(?m)^### Pages? (\d+)\s*[–-]\s*(\d+)\b',t):
                if int(m.group(1))<=int(page)<=int(m.group(2)) and int(m.group(1))!=int(page):
                    n=nxt.search(t,m.end()); out.append((m.start(),n.start() if n else len(t)))
        return out
    for r in rows:
        pg,tg,old,new=r['page'],r['target'],r['old'],r['new']; st='applied'
        if old==new: st='same'
        elif tg=='en' and '--nogate' not in a and re.search('[\u0900-\u097f]',new) and sp_sanskrit.gate(KNP,int(pg) if pg.isdigit() else 0,new):
            st='sanskrit_not_in_kannada'      # Devanagari that the Kannada of the page does not support: not applied, becomes a question
        elif tg=='en':
            hits=[]
            for ep,T in ENS.items():
                for s0,e0 in sections(T,r'(?m)^### Page %s\b',pg):
                    c=T[s0:e0].count(old)
                    if c: hits.append((ep,s0,e0,c))
            if not hits: st='not_found'
            elif sum(h[3] for h in hits)>1: st='ambiguous'
            else:
                ep,s0,e0,_=hits[0]; T=ENS[ep]; ENS[ep]=T[:s0]+T[s0:e0].replace(old,new,1)+T[e0:]
                log.append(f"| {pg} | `{old[:90]}` → `{new[:90]}` | SECOND-PASS {r['kind']}: {r['basis'][:160]} |")
        elif tg=='kn':
            T=KN; secs=sections(T,r'(?m)^<!-- printed %s -->$',pg); hit=[(s0,e0) for s0,e0 in secs if old in T[s0:e0]]; c=sum(T[s0:e0].count(old) for s0,e0 in hit)
            if not secs or c==0: st='not_found'
            elif c>1: st='ambiguous'
            else:
                s0,e0=hit[0]; KN=T[:s0]+T[s0:e0].replace(old,new,1)+T[e0:]
                hits=[p for p,t in src.items() if t.count(old)==1]
                note='supplied file and book' if len(hits)==1 else 'book only (text not unique in the supplied files)'
                if len(hits)==1: src[hits[0]]=src[hits[0]].replace(old,new,1)
                fixes.append((f'p. {pg}',old,new,r['kind']+' second pass; '+note,r['basis'],'second-pass reader (Sonnet), rule: supplied text, intended reading certain'))
        else: st='bad_target'
        res.append((pg,tg,st,old[:60]))
    out=ed.replace('.tsv','.result.tsv')
    with open(out,'w',encoding='utf8') as f:
        f.write('page\ttarget\tstatus\told\n'); [f.write('\t'.join(x)+'\n') for x in res]
    n=sum(1 for x in res if x[2]=='applied'); print(f'{len(rows)} edits: applied {n}; '+', '.join(f'{k} {sum(1 for x in res if x[2]==k)}' for k in ('not_found','ambiguous','same','bad_target','sanskrit_not_in_kannada') if any(x[2]==k for x in res)))
    if dry: return
    [open(p,'w',encoding='utf8').write(t) for p,t in ENS.items()]; open(kn_p,'w',encoding='utf8').write(KN)
    for p,t in src.items(): open(p,'w',encoding='utf8').write(t)
    if log:
        with open(f'{d}/review/repair_log.md','a',encoding='utf8') as f: f.write(f'\n### {today} second pass, batch {os.path.basename(ed)}\n| page | old → new | why |\n|---|---|---|\n'+'\n'.join(log)+'\n')
    if fixes:
        sf=f'{d}/data/source_fixes.tsv'; os.makedirs(os.path.dirname(sf),exist_ok=True); new=not os.path.exists(sf)
        with open(sf,'a',encoding='utf8') as f:
            if new: f.write('place\tas_supplied\tas_corrected\treason\tbasis\tdecided_by\n')
            for x in fixes: f.write('\t'.join(y.replace('\t',' ').replace('\n',' ') for y in x)+'\n')
main()
