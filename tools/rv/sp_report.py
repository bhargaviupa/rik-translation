#!/usr/bin/env python3
"""The one status report of a second pass, the same for every volume.

  python3 tools/rv/sp_report.py N [--stage "S2 reading"] [--pages LO-HI]   writes volN/review/second_pass/STATUS_REPORT.md
  python3 tools/rv/sp_report.py N --add-batch FIRST LAST --tokens 272k --commit abc1234 [--note "..."] [--edits-ok N --edits-failed N]
        appends one row to batches.tsv (rows, applied, questions are COUNTED from findings.tsv for those pages) and rewrites the report

Machine files in volN/review/second_pass/ (the report is made from these, never typed):
  findings.tsv   page, kind (code of docs/ERROR_KINDS.md), reader (R1|R3|R6), place, as_found, proposed, basis, decision (applied|question), log
  questions.tsv  page, place, as_found, question, why_not_settled
  batches.tsv    batch, first, last, rows, applied, edits_ok, edits_failed, questions, tokens, commit, date, note
  open.tsv       (optional) kind (page-absent|boundary-shifted|marker|tool|other), pages, text      — things the editor must know that are not findings
Format: docs/SECOND_PASS_REPORT.md."""
import csv,sys,os,collections,datetime,subprocess,re
def rd(p):
    return list(csv.DictReader(open(p,encoding='utf8'),delimiter='\t',quoting=csv.QUOTE_NONE)) if os.path.exists(p) else []
def main():
    a=sys.argv[1:]
    if not a: sys.exit(__doc__)
    vol=a[0]; d=f'vol{vol}/review/second_pass'; opt=lambda k,df=None:(a[a.index(k)+1] if k in a else df)
    os.makedirs(d,exist_ok=True); bp=f'{d}/batches.tsv'; F=rd(f'{d}/findings.tsv'); Q=rd(f'{d}/questions.tsv'); B=rd(bp); O=rd(f'{d}/open.tsv')
    cols='batch first last rows applied edits_ok edits_failed questions tokens commit date note'.split()
    if '--add-batch' in a:
        i=a.index('--add-batch'); lo,hi=int(a[i+1]),int(a[i+2])
        fr=[r for r in F if r['page'].isdigit() and lo<=int(r['page'])<=hi]; ap=sum(r['decision']=='applied' for r in fr)
        if not os.path.exists(bp): open(bp,'w',encoding='utf8').write('\t'.join(cols)+'\n')
        row=[str(len(B)+1) if opt('--label') is None else opt('--label'),lo,hi,len(fr),ap,opt('--edits-ok',ap),opt('--edits-failed',0),len(fr)-ap,opt('--tokens','?'),opt('--commit','(this commit)'),datetime.date.today().isoformat(),(opt('--note','') or '').replace('\t',' ').replace('\n',' ')]
        open(bp,'a',encoding='utf8').write('\t'.join(map(str,row))+'\n'); B=rd(bp)
    pages=set()
    for b in B:
        if b['first'].isdigit(): pages.update(range(int(b['first']),int(b['last'])+1))
    lo,hi=(map(int,opt('--pages').split('-')) if opt('--pages') else (None,None))
    tot=f' of {hi-lo+1}' if lo else ''
    N=lambda k:sum(int(b[k]) for b in B if b[k].lstrip('-').isdigit())
    tk=sum(float(b['tokens'].rstrip('k')) for b in B if re.fullmatch(r'[\d.]+k',b['tokens']))
    ap=[r for r in F if r['decision']=='applied']; qs=[r for r in F if r['decision']!='applied']
    kind=collections.Counter(r['kind'] for r in F); rdr=collections.Counter(r['reader'] for r in F)
    kapp=collections.Counter(r['kind'] for r in ap)
    L=[f'# Vol {vol} second pass — status report',f'*Made by `python3 tools/rv/sp_report.py {vol}` from `findings.tsv`, `questions.tsv`, `batches.tsv`, `open.tsv`; updated {datetime.date.today().isoformat()}. Format: `docs/SECOND_PASS_REPORT.md`.*','',
       '## 1. State',f'- **Stage:** {opt("--stage","S2 reading in page batches")}',
       f'- **Pages read:** {len(pages)}{tot} ('+(', '.join(f"{b['first']}–{b['last']}" for b in B) if B else 'none yet')+')',
       f'- **Findings:** {len(F)} — applied {len(ap)}, questions {len(qs)}; edits ok {N("edits_ok")}, failed {N("edits_failed")}',
       f'- **Reader tokens (batches so far):** {tk:.0f}k'+(f'; per page {tk/len(pages):.1f}k' if pages else ''),
       f'- **Last commit:** {B[-1]["commit"] if B else "—"}','',
       '## 2. Batches','| Batch | Pages | Findings | Applied | Edits ok / failed | Questions | Tokens | Commit | Note |','|---|---|---|---|---|---|---|---|---|']
    for b in B: L.append(f"| {b['batch']} | {b['first']}–{b['last']} | {b['rows']} | {b['applied']} | {b['edits_ok']} / {b['edits_failed']} | {b['questions']} | {b['tokens']} | {b['commit']} | {b['note']} |")
    L+=['','## 3. Findings by kind','| Kind | Applied | Questions | Total |','|---|---|---|---|']
    for k,n in sorted(kind.items(),key=lambda x:-x[1]): L.append(f'| {k} | {kapp[k]} | {n-kapp[k]} | {n} |')
    L+=['',f'By reader: '+', '.join(f'{k} {v}' for k,v in sorted(rdr.items())),'','## 4. Open items (not findings)']
    L+= [f"- **{o['kind']}** (pages {o['pages']}): {o['text']}" for o in O] or ['- none recorded']
    L+=['','## 5. Questions for the editor',f'{len(Q)} rows in `questions.tsv`'+('; by kind: '+', '.join(f'{k} {sum(1 for r in qs if r["kind"]==k)}' for k in sorted({r["kind"] for r in qs})) if qs else ''),'',
        '## 6. Files',f'`{d}/findings.tsv` · `questions.tsv` · `batches.tsv` · `open.tsv` · `edits/` (edit files and results) · `../repair_log.md` (every English repair, heading "second pass") · `../../data/source_fixes.tsv` (edits of the supplied Kannada)','',
        '## 7. Next',opt('--next','the next page batch; then S3 totals (re-run the S0 checks), S4 coverage, S5 pictures, S6 records')]
    open(f'{d}/STATUS_REPORT.md','w',encoding='utf8').write('\n'.join(L)+'\n'); print(f'{d}/STATUS_REPORT.md written: {len(B)} batches, {len(F)} findings, {len(Q)} questions')
main()
