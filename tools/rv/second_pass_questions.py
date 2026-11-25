#!/usr/bin/env python3
"""Clean list of the open questions of a volume's second pass.   python3 tools/rv/second_pass_questions.py VOL
Reads VOL/review/second_pass/findings.tsv (rows with decision `question`, and rows marked NOT APPLIED), writes VOL/review/second_pass/questions.tsv:
no, page, type, reader, kind, english_line, english_now, kannada_says, proposed, to_decide, answer (empty: for the editor).
Done here: the readers' mixed `kind`/`reader` columns are put in order (reader = R1|R3|R6, kind = an H-code of docs/ERROR_KINDS.md where the reader gave one), exact duplicates
(same page, same english_now) are merged, rows are sorted by page and given a `type`, markdown asterisks are removed from the long cells, cells are cut to 300 letters
(the full text stays in findings.tsv). Nothing is decided here."""
import sys,csv,re,collections
vol=sys.argv[1]; d=f'vol{vol}/review/second_pass'
CS=dict(delimiter='\t',quoting=csv.QUOTE_NONE,quotechar=None)
rows=list(csv.reader(open(f'{d}/findings.tsv',encoding='utf8',newline=''),**CS)); h=rows[0]; ix={x:i for i,x in enumerate(h)}
def clean(s,n=300):
    s=s.replace('**','').replace('*','').strip(); return s if len(s)<=n else s[:n-1]+'…'
def rcode(r):
    for c in (r[ix['reader']],r[ix['kind']]):
        m=re.fullmatch(r'R[1-6]',c.strip())
        if m: return m.group()
    m=re.search(r'\bR[1-6]\b',r[ix['reader']]);  return m.group() if m else ''
def hcode(r):
    c=r[ix['kind']].strip(); return c if re.fullmatch(r'H\d+',c) else ''
def typ(r):
    a,b,bs,lg=r[ix['as_found']],r[ix['proposed']],r[ix['basis']],r[ix['log']]
    txt=(bs+' '+lg).lower()
    if 'NOT APPLIED' in lg: return 'passage to insert by hand'
    if re.search(r'two supplied places|disagree|numbering|differs? from the supplied',txt) and re.search(r'\d',a+b): return 'number: two places disagree'
    if hcode(r)=='H10' or re.search(r'\b\d+-\d+(-\d+)?\b',a+b) and re.search(r'number|reference|digit|printed',txt): return 'number or reference'
    if re.search(r'not a word|garbled|misprint|unclear|illegible|cannot read|can.t read|probably|looks like',txt): return 'unclear Kannada word'
    if re.search(r'sūtra|sutra|pā\.|u\. sū|vārttika|paribhāṣā',txt+a.lower()+b.lower()): return 'sūtra or grammar form'
    if rcode(r)=='R3' or hcode(r) in('H15','H20','H24'): return 'Sanskrit word or quotation'
    return 'meaning or wording'
out=[]; seen={}
for r in rows[1:]:
    r+=['']*(len(h)-len(r))
    if not (r[ix['decision']]=='question' or 'NOT APPLIED' in r[ix['log']]): continue
    key=(r[ix['page']],re.sub(r'\W+','',r[ix['as_found']])[:80])
    m=re.match(r'L(\d+)',r[ix['place']]); ln=m.group(1) if m else ''
    log=re.sub(r'^\[[^\]]*\]\s*','',r[ix['log']])
    rec=[r[ix['page']],typ(r),rcode(r),hcode(r),ln,clean(r[ix['as_found']]),clean(r[ix['basis']]),clean(r[ix['proposed']]) if r[ix['proposed']]!=r[ix['as_found']] else '(no change proposed)',clean(log),'']
    if key in seen: out[seen[key]][8]+=' | '+rec[8][:150]; continue
    seen[key]=len(out); out.append(rec)
out.sort(key=lambda x:(int(re.sub(r'\D','',x[0]) or 0),x[4] and int(x[4]) or 0))
W=csv.writer(open(f'{d}/questions.tsv','w',encoding='utf8',newline=''),lineterminator='\n',**CS)
W.writerow(['no','page','type','reader','kind','english_line','english_now','kannada_says','proposed','to_decide','answer'])
for i,r in enumerate(out,1): W.writerow([str(i)]+r)
c=collections.Counter(r[1] for r in out); print(len(out),'questions;',dict(c.most_common()))
