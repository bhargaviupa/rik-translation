"""render_wr.py VOL GPDF DPI OUT [y0 y1]  - render a global PDF page of the better scan (vol3/vol4), grayscale,
optionally only the vertical band y0..y1 (fractions of page height)."""
import sys,subprocess,importlib.util,os
vol,g,dpi,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(os.path.dirname(here))
spec=importlib.util.spec_from_file_location('cfg',os.path.join(root,vol,'tools','cfg.py')); cfg=importlib.util.module_from_spec(spec); spec.loader.exec_module(cfg)
pdf,p=cfg.part_of(g)
cmd=['pdftoppm','-f',str(p),'-l',str(p),'-r',str(dpi),'-gray','-png','-singlefile']
if len(sys.argv)>6:
    info=subprocess.run(['pdfinfo','-f',str(p),'-l',str(p),pdf],capture_output=True,text=True).stdout
    line=[l for l in info.splitlines() if l.startswith(f'Page{p:>5} size') or l.startswith('Page size')][0]
    w,h=[float(x) for x in line.split(':')[1].split('pts')[0].split('x')]
    W,H=int(w/72*dpi),int(h/72*dpi); y0,y1=float(sys.argv[5]),float(sys.argv[6])
    cmd+=['-x','0','-y',str(int(y0*H)),'-W',str(W),'-H',str(int((y1-y0)*H))]
subprocess.run(cmd+[pdf,out],check=True)
