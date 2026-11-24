#!/usr/bin/env python3
"""S3 of the second pass of a legacy volume: apply the `applied` rows of VOL/review/second_pass/findings.tsv to the ENGLISH file.
  python3 tools/rv/second_pass_apply.py VOL [--dry]
A row is carried out only if its `as_found` stands exactly once in the English line named in `place` ('L1234: …') or, failing that, exactly once within 25 lines of it,
and `proposed` differs; else the row is marked '[NOT APPLIED: reason]' in column `log` and nothing changes. Done rows get '[APPLIED date]' in `log` (never applied twice).
Every applied row is one line of VOL/review/repair_log.md. Rows whose basis says Kannada/source edit are not touched here (they go to data/source_fixes.tsv by hand).
Numbers (H10) are taken from the supplied text by the reader (user, Nov 24 2026)."""
import sys,os,re,csv,datetime
vol=sys.argv[1]; dry='--dry' in sys.argv; d=f'vol{vol}'
F=f'{d}/review/second_pass/findings.tsv'; E=f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md'
CS=dict(delimiter='\t',quoting=csv.QUOTE_NONE,quotechar=None)
rows=list(csv.reader(open(F,encoding='utf8',newline=''),**CS)); hdr=rows[0]; ix={h:i for i,h in enumerate(hdr)}
lines=open(E,encoding='utf8').read().split('\n'); today=datetime.date.today().isoformat(); log=[]; n_ok=n_no=0
for r in rows[1:]:
    r+=['']*(len(hdr)-len(r))
    if r[ix['decision']]!='applied' or '[APPLIED' in r[ix['log']] or 'NOT APPLIED' in r[ix['log']]: continue
    if re.search(r'(?i)kannada (source|text) edit|source_fixes',r[ix['basis']]): continue
    old,new=r[ix['as_found']],r[ix['proposed']]; m=re.match(r'L(\d+)',r[ix['place']]); why=None; tgt=None
    if not old or old==new: why='empty or unchanged'
    elif not m: why='no line number'
    else:
        L=int(m.group(1))-1; cand=[L]+[x for k in range(1,26) for x in (L-k,L+k)]
        hits=[i for i in cand if 0<=i<len(lines) and old in lines[i]]
        if not hits: why='as_found not found near the line'
        elif lines[hits[0]].count(old)!=1: why='as_found stands twice in the line'
        elif hits[0]!=L and len(hits)>1: why='ambiguous (several lines near)'
        else: tgt=hits[0]
    if why: r[ix['log']]=f"[NOT APPLIED: {why}] "+r[ix['log']]; n_no+=1; continue
    n_ok+=1
    if dry: continue
    lines[tgt]=lines[tgt].replace(old,new,1); r[ix['log']]=f'[APPLIED {today}] '+r[ix['log']]
    log.append(f"- p. {r[ix['page']]} (English line {tgt+1}) [{r[ix['kind']]}]: `{old[:140]}` → `{new[:140]}` — {r[ix['basis']][:200]} (second pass S3, findings.tsv)")
if not dry:
    open(E,'w',encoding='utf8').write('\n'.join(lines))
    csv.writer(open(F,'w',encoding='utf8',newline=''),lineterminator='\n',**CS).writerows(rows)
    if log:
        with open(f'{d}/review/repair_log.md','a',encoding='utf8') as f: f.write(f'\n## Second pass S3, {today}\n'+'\n'.join(log)+'\n')
print(f'applied {n_ok}, not applied {n_no}'+(' (dry run)' if dry else ''))
