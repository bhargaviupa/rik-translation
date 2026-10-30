"""Locate the 'Sukta-N / Mandala-1 || Anuvaka' heading block on given PDF pages (LOCATING ONLY: OCR finds the line with 'ಅಷ್ಟಕ' + 'ಅಧ್ಯಾಯ'; readings come from viewing the crop).
python3 findhead.py PDFPAGE... -> prints PDFPAGE y0 y1 (whole-page fractions) of the block, or none."""
import sys,os,subprocess,tempfile,csv,io
sys.path.insert(0,os.path.dirname(__file__))
from cfg import part_of,flipped
from PIL import Image
def find(g,dpi=100):
    p,n=part_of(g); d=tempfile.mkdtemp()
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r',str(dpi),'-gray',p,d+'/p'],check=True)
    f=d+'/'+os.listdir(d)[0]; im=Image.open(f); H=im.size[1]
    t=subprocess.run(['tesseract',f,'-','-l','kan','--psm','6','tsv'],capture_output=True,text=True).stdout
    rows=list(csv.DictReader(io.StringIO(t),delimiter='\t',quoting=csv.QUOTE_NONE)); subprocess.run(['rm','-rf',d])
    hits=[int(r['top'])/H for r in rows if r.get('text') and ('ಅಷ್ಟಕ' in r['text'] or 'ಅನುವಾಕ' in r['text'] or 'ವರ್ಗ' in r['text'])]
    return hits
if __name__=='__main__':
    for a in sys.argv[1:]:
        g=int(a); print(g,[round(h,3) for h in find(g)])
