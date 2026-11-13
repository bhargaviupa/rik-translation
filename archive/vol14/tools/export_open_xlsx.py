"""Export the open [?] places of the Vol 14 translation (and the review lists) to an Excel file.
python3 vol14/tools/export_open_xlsx.py [OUT.xlsx]"""
import re,os,sys,json,csv,openpyxl
from openpyxl.styles import Font,Alignment,PatternFill
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
EN=os.path.join(ROOT,'vol14','Rigveda_Samhita_Vol14_scan_English_Translation.md')
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.join(ROOT,'vol14','review','Vol14_open_questions.xlsx')
L=open(EN,encoding='utf8').read().split('\n')
dev=lambda t:re.search('[ऀ-ॿ]',t); kan=lambda t:re.search('[ಀ-೿]',t)
rows=[]; pg=(None,None); suk=''; rik=''
for i,l in enumerate(L):
    m=re.match(r'### Printed p\. (\d+) \(PDF (\d+)',l)
    if m: pg=(int(m.group(1)),int(m.group(2)))
    m=re.match(r'#+ .*?S[ūu]kta[^\n]*',l)
    if m and not l.startswith('####'): suk=re.sub(r'[#*]','',l).strip()[:60]
    m=re.match(r'####+ (Ṛk \d+[^\n]*)',l)
    if m: rik=m.group(1)[:30]
    if pg[0] is None: continue
    if '[?]' not in l or l.startswith('> *') or l.startswith('*(Header') and False: continue
    if re.match(r'^\*[^(\n]',l) and l.rstrip().endswith('*') and not dev(l) : pass
    for mm in re.finditer(r'\[\?\]',l):
        a=max(0,mm.start()-90); b=min(len(l),mm.end()+50); ctx=l[a:b].replace('\n',' ')
        pre=l[max(0,mm.start()-14):mm.start()]
        if re.search(r'\d[\d\-\.\]\) ]{0,3}$',pre) or re.search(r'\d-\[?$',pre) or re.search(r'\[\d',l[max(0,mm.start()-10):mm.start()]): kind='numeral / reference'
        elif dev(l[max(0,mm.start()-60):mm.start()]): kind='Sanskrit word (Devanagari)'
        elif kan(l[max(0,mm.start()-60):mm.start()]): kind='Kannada word'
        elif re.search(r'(note|printed|as read|doubt|read|unclear)',l,re.I) and not dev(ctx): kind='note / English text'
        else: kind='other'
        rows.append([pg[1],pg[0],suk,rik,i+1,kind,ctx.strip(),'',''])
# dedupe identical (page,context)
seen=set(); out=[]
for r in rows:
    k=(r[0],r[6])
    if k in seen: continue
    seen.add(k); out.append(r)
wb=openpyxl.Workbook(); ws=wb.active; ws.title='Open question-mark places'
hdr=['PDF page','Printed page','Sūkta (nearest heading)','Ṛk (nearest heading)','Line in .md','Kind','Context ([?] marks the doubtful place)','Your reading','Status']
ws.append(hdr)
for r in out: ws.append(r)
def style(ws,widths):
    for c in ws[1]: c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor='4F4F4F'); c.alignment=Alignment(wrap_text=True,vertical='top')
    for k,w in enumerate(widths): ws.column_dimensions[chr(65+k)].width=w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=Alignment(wrap_text=True,vertical='top')
    ws.freeze_panes='A2'; ws.auto_filter.ref=ws.dimensions
style(ws,[9,9,24,12,9,22,90,28,14])
def tsv(path,title,widths,skip=0):
    if not os.path.exists(path): return
    w=wb.create_sheet(title)
    for k,r in enumerate(csv.reader(open(path,encoding='utf8'),delimiter='\t')): w.append(r)
    style(w,widths)
tsv(os.path.join(ROOT,'vol14','review','numeral_file_vs_translation_pdf20-572.tsv'),'Numeral file mismatches',[10,10,22,60])
tsv(os.path.join(ROOT,'vol14','review','accent_ref_differences.tsv'),'Accent reference differences',[9,55,55,40])
dj=os.path.join(ROOT,'vol14','review','doubts_v14.json')
if os.path.exists(dj):
    d=json.load(open(dj)); w=wb.create_sheet('Zoom and doubt log'); w.append(['PDF page','Printed page','Crop (y0,y1,x0,x1 as page fractions)','Note','Answer'])
    for x in d: w.append([x.get('pdf'),x.get('printed'),', '.join('%.3f'%v for v in x.get('crop',[])),x.get('note',''),x.get('answer','')])
    style(w,[9,9,32,80,30])
ad=os.path.join(ROOT,'vol14','review','api_doubts.tsv')
if os.path.exists(ad):
    w=wb.create_sheet('API doubts (model notes)'); w.append(['PDF page','What is doubtful / model reading'])
    for l in open(ad,encoding='utf8'):
        p=l.rstrip('\n').split(' | ',1)
        if len(p)==2: w.append(p)
    style(w,[9,110])
wb.save(OUT)
import collections
print(OUT); print(len(out),'open [?] places;',dict(collections.Counter(r[5] for r in out)))
