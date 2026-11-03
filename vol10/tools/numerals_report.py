#!/usr/bin/env python3
"""Rebuild vol10/review/numerals_report_v10.tsv: one line per row of every numeral sheet (applied / already in English / not in English)."""
import re,sys,glob,csv,os
sys.path.insert(0,os.path.dirname(__file__))
import apply_numerals as A, openpyxl
t=open(A.EN).read(); hs=list(A.HEAD.finditer(t)); blk={}
for i,h in enumerate(hs):
    blk[int(h.group(2))]=blk.get(int(h.group(2)),'')+t[h.start():hs[i+1].start() if i+1<len(hs) else len(t)]
applied={}
for l in open(os.path.join(A.REV,'numerals_applied_v10.tsv')):
    f=l.rstrip('\n').split('\t'); applied[f[4]]=f[1]+': '+f[2]+' -> '+f[3]
out=[]
for fn in sorted(glob.glob(os.path.join(A.NUMD,'*.xlsx'))):
    n=int(re.search(r'_(\d+)\.xlsx$',fn).group(1)); ws=openpyxl.load_workbook(fn,read_only=True).active
    for i,r in enumerate(list(ws.iter_rows(values_only=True))[1:],2):
        if r[0] is None or not r[3]: continue
        g=int(r[0])+100*(n-1); num=A.norm(str(r[3])); b=A.to_ascii(blk.get(g,'')); key='%s row %d'%(os.path.basename(fn),i)
        if key in applied: st='APPLIED to the English ('+applied[key]+')'
        elif re.search(r'(?<![\d-])'+re.escape(num)+r'(?![\d-])',b): st='number already in English on this page'
        else: st='number NOT in English on this page, and no [?] to put it in'
        out.append([os.path.basename(fn),i,r[0],g,r[3],st,r[4]])
w=csv.writer(open(os.path.join(A.REV,'numerals_report_v10.tsv'),'w'),delimiter='\t')
w.writerow(['sheet file','sheet row','page in sheet','PDF page','number in sheet','what happened','sheet OCR line']); w.writerows(out)
import collections; print(collections.Counter(x[5].split(' (')[0] for x in out),len(out))
