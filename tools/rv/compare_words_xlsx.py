"""Word-by-word comparison of two English volume files (scan-based OLD vs supplied-text NEW), printed pages FIRST-LAST, into an xlsx.
python3 tools/rv/compare_words_xlsx.py OLD.md NEW.md FIRST LAST OUT.xlsx
Sheets: Summary, Devanagari (Sanskrit block words), English (prose words), Numerals (reference numerals), Pages."""
import re,sys,difflib,collections
sys.path.insert(0,'tools/rv')
from compare_translations import pages,ACC,refs
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment
def dev_tokens(lines):
    out=[]
    for l in lines:
        if l.startswith('###') or l.startswith('**Progress'): continue
        t=re.sub(r'\[\?\]','',l)
        for y in re.findall(r'[ऀ-ॿ][ऀ-ॿ\-]*',t.replace('॥',' ').replace('।',' ')):
            k=re.sub(r'[^ऄ-हा-्क़-ॣ]','',y.translate(ACC))
            if k: out.append((y,k))
    return out
def prose_tokens(lines):
    out=[]
    for l in lines:
        if l.startswith('> ') or l.startswith('*(') or l.startswith('###') or l.startswith('**Progress'): continue
        t=re.sub(r'\(\*[^*]*\*\)','',l); t=re.sub(r'[ऀ-ॿ]+','',t)
        out+=[(w,w.lower()) for w in re.findall(r"[A-Za-zĀ-ɏḀ-ỿ][\w'’\-]*|\d[\d\-]*",t)]
    return out
def diff(a,b):
    sm=difflib.SequenceMatcher(None,[k for _,k in a],[k for _,k in b],autojunk=False); rows=[]
    for t,i1,i2,j1,j2 in sm.get_opcodes():
        if t=='equal': continue
        ctx=' '.join(w for w,_ in a[max(0,i1-4):i1])+' ['+' '.join(w for w,_ in a[i1:i2])+'] '+' '.join(w for w,_ in a[i2:i2+4])
        rows.append((t,' '.join(w for w,_ in a[i1:i2]),' '.join(w for w,_ in b[j1:j2]),ctx))
    return rows,sm
O,N=sys.argv[1:3],None
old,new,lo,hi,outp=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
PO=pages(old,lo,hi);PN=pages(new,lo,hi)
wb=Workbook();S=wb.active;S.title='Summary';D=wb.create_sheet('Devanagari');E=wb.create_sheet('English');R=wb.create_sheet('Numerals');P=wb.create_sheet('Pages')
for ws,h in((D,['Page','Type','Scan-based (old)','Supplied-text (new)','Context (old)','Verdict (fill in)']),(E,['Page','Type','Scan-based (old)','Supplied-text (new)','Context (old)','Verdict (fill in)']),(R,['Page','Only in scan-based','Only in supplied-text']),(P,['Page','Dev words old','Dev words new','Dev differing','Eng words old','Eng words new','Eng differing','[?] old','[?] new'])):
    ws.append(h)
T=collections.Counter();pg=[p for p in range(lo,hi+1) if p in PO and p in PN]
for p in pg:
    a,b=dev_tokens(PO[p]),dev_tokens(PN[p]);dr,_=diff(a,b)
    for r in dr:D.append([p,*r])
    a2,b2=prose_tokens(PO[p]),prose_tokens(PN[p]);er,_=diff(a2,b2)
    for r in er:E.append([p,*r])
    ro,rn=refs(PO[p]),refs(PN[p]);ra=sorted((ro-rn).keys());rb=sorted((rn-ro).keys())
    if ra or rb:R.append([p,', '.join(ra),', '.join(rb)])
    dd=sum(max(len(r[1].split()),len(r[2].split())) for r in dr);ed=sum(max(len(r[1].split()),len(r[2].split())) for r in er)
    qo=sum(l.count('[?]') for l in PO[p]);qn=sum(l.count('[?]') for l in PN[p])
    P.append([p,len(a),len(b),dd,len(a2),len(b2),ed,qo,qn])
    T.update(dev_old=len(a),dev_new=len(b),dev_diff=dd,en_old=len(a2),en_new=len(b2),en_diff=ed,q_old=qo,q_new=qn,ref=len(ra)+len(rb),dev_ev=len(dr),en_ev=len(er))
ty=collections.Counter(r[1] for r in D.iter_rows(min_row=2,values_only=True));ty2=collections.Counter(r[1] for r in E.iter_rows(min_row=2,values_only=True))
for l in [('Pages compared',f'{pg[0]}-{pg[-1]} ({len(pg)} pages)'),('Note','No scan-based Kannada text exists for these pages (vol14 Kannada file starts at p. 767); Kannada-level differences therefore appear only through the Sanskrit blocks (Devanagari sheet). Kannada prose exists only as English in the scan-based file.'),('',''),
 ('Devanagari words old / new',f"{T['dev_old']} / {T['dev_new']}"),('Devanagari differing words (accents ignored)',f"{T['dev_diff']} = {100*T['dev_diff']/max(1,T['dev_old']):.2f} %"),('Devanagari difference events',T['dev_ev']),('  by type',str(dict(ty))),('',''),
 ('English words old / new',f"{T['en_old']} / {T['en_new']}"),('English differing words (case ignored)',f"{T['en_diff']} = {100*T['en_diff']/max(1,T['en_old']):.2f} %"),('English difference events',T['en_ev']),('  by type',str(dict(ty2))),('',''),
 ('[?] old / new',f"{T['q_old']} / {T['q_new']}"),('Reference numerals differing (distinct per page)',T['ref'])]:S.append(list(l))
for ws in(S,D,E,R,P):
    for c in ws[1]:c.font=Font(bold=True)
    ws.freeze_panes='A2'
for ws,w in((D,[7,9,32,32,60,18]),(E,[7,9,32,32,60,18]),(R,[7,40,40]),(P,[7]+[13]*8),(S,[48,100])):
    for i,x in enumerate(w):ws.column_dimensions['ABCDEFGHI'[i]].width=x
S.column_dimensions['B'].width=100
for r in S.iter_rows():
    for c in r:c.alignment=Alignment(wrap_text=True,vertical='top')
wb.save(outp)
for r in S.iter_rows(values_only=True):print(*r)
