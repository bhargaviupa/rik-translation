"""Set the complex-script (Indic) font in a pandoc DOCX: python3 docx_csfont.py FILE.docx "Noto Serif Devanagari" """
import sys,zipfile,re,shutil,os
f,font=sys.argv[1],sys.argv[2]; tmp=f+'.tmp'
zin=zipfile.ZipFile(f); zout=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    d=zin.read(it.filename)
    if it.filename=='word/styles.xml':
        s=d.decode(); n0=s.count('cstheme')
        s=re.sub(r'w:cstheme="[^"]*"',f'w:cs="{font}"',s)
        if '<w:rPrDefault><w:rPr>' in s and 'w:cs=' not in s.split('</w:rPrDefault>')[0]:
            s=s.replace('<w:rPrDefault><w:rPr>',f'<w:rPrDefault><w:rPr><w:rFonts w:cs="{font}"/>',1)
        d=s.encode(); print(f,'cstheme replaced',n0)
    zout.writestr(it,d)
zout.close(); shutil.move(tmp,f)
