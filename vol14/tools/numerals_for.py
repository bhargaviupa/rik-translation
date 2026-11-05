"""Print the numeral-file rows for one of OUR PDF pages (Vol 14).
python3 vol14/tools/numerals_for.py PDFPAGE [PDFPAGE ...]
File page = printed + 18 = our PDF page (<=222), PDF-1 (224-334), PDF-2 (>=336); our PDF 223 and 335 are duplicates of 222 and 334 (no rows). Printed = PDF-18 (<=222), PDF-19 (224-334), PDF-20 (>=336). PDF 223 is the duplicate of 222 (no rows).
Prints per row: file line | Kannada pattern | English digits | raw OCR line (noisy words, reliable numerals); then every Kannada numeral
group found in the raw lines, converted to English digits, in line order."""
import sys,os,re,glob,openpyxl
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','numerals')
K=str.maketrans('೦೧೨೩೪೫೬೭೮೯','0123456789')
rows=[]
for f in sorted(glob.glob(os.path.join(D,'Rigveda_Clean_Numerals_14_*.xlsx'))):
    ws=openpyxl.load_workbook(f).active
    rows+=[r for r in ws.iter_rows(min_row=2,values_only=True) if r[0] is not None]
def filepage(q): return q if q<=222 else (q-1 if q<=334 else (q-2 if q<=446 else (q-3 if q<=558 else (q-4 if q<=670 else (q-5 if q<=782 else q-6)))))
for q in map(int,sys.argv[1:]):
    if q in (223,335,447,559,671,783): print(f'== PDF {q}: duplicate of the previous page, no rows'); continue
    fp=filepage(q); rs=[r for r in rows if r[0]==fp]
    print(f'== PDF {q} (printed {q-18 if q<=222 else (q-19 if q<=334 else (q-20 if q<=446 else (q-21 if q<=558 else (q-22 if q<=670 else (q-23 if q<=782 else q-24)))))}, file page {fp}): {len(rs)} rows')
    seen=set()
    for p,l,pat,eq,ctx in rs: print(f'  line {l} | {pat} | {eq} | {ctx}')
    print('  numeral groups by line:')
    for l in sorted({r[1] for r in rs}):
        ctx=[r[4] for r in rs if r[1]==l][0]
        toks=[t.translate(K) for t in re.findall(r'[೦-೯]+(?:[-.:][೦-೯]+)*',ctx)]
        print(f'   line {l}: '+'  '.join(toks))
