"""Merge several worker doubts JSONs (vol6/review/doubts_w6?_p*.json: lists of {page,y0,y1,...}) into ONE doubts page.
python3 vol6/tools/consolidate_doubts_v6.py OUT.html [--from-page N] [--include page:substring ...] FILES...
 --from-page N : keep only rows with printed page >= N
 --include 104:Uṇ 231:मनो : also keep these earlier rows (printed page : substring of "file"), even below --from-page
Rows are de-duplicated (page, y0, y1, file) and sorted by page; ids become <page>_d<k> unique over the whole page.
Builds OUT.json (merged source) and OUT.html via doubts_v6.py."""
import sys,os,json,subprocess
args=sys.argv[1:]; out=args.pop(0); frm=0; inc=[]; files=[]
while args:
    a=args.pop(0)
    if a=='--from-page': frm=int(args.pop(0))
    elif a=='--include':
        while args and ':' in args[0] and not args[0].endswith('.json'): inc.append(args.pop(0))
    else: files.append(a)
rows=[]; seen=set()
for f in files:
    for r in json.load(open(f,encoding='utf8')):
        k=(r['page'],round(r['y0'],3),round(r['y1'],3),r.get('file',''))
        if k in seen: continue
        keep=r['page']>=frm or any(r['page']==int(i.split(':',1)[0]) and i.split(':',1)[1] in r.get('file','')+r.get('ctx','') for i in inc)
        if keep: seen.add(k); rows.append(r)
rows.sort(key=lambda r:(r['page'],r['y0']))
src=out.replace('.html','_src.json'); json.dump(rows,open(src,'w'),ensure_ascii=False,indent=0)
subprocess.run([sys.executable,os.path.join(os.path.dirname(__file__),'doubts_v6.py'),src,out,'Vol 6: all remaining doubts, one page'],check=True)
print(len(rows),'rows')
