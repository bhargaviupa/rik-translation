"""Kannada text of printed pages, made by script from the supplied machine-read HTML/markdown (the base text for Vol 15 onwards).

  python3 tools/rv/html_to_kn.py "file.html@1-84" "file.md@85-184" --pages 86 87 88 [--section bhashya]

Cleaning (no model involved): '||' -> '॥', '|' -> '।'; a Latin 's' between Kannada letters -> the avagraha 'ಽ'; OCR notes such as 'This image contains no discernible text.'
are dropped; the section labels (Saṃhitā, Pada, Sāyaṇa-bhāṣya, Pratipadārtha, Bhāvārtha, English Translation, Viśeṣa-viṣayagaḷu, Vyākaraṇa-prakriyā) are recognised
despite the usual OCR variants (ಪಾರಃ for ಪಾಠಃ, ಭಾನಾರ್ಥ for ಭಾವಾರ್ಥ …) and written in one standard form. Lines of the Saṃhitā, Pada and bhāṣya sections become '> ' blocks;
everything else is prose. A page that starts without a label continues the section of the previous page (--section gives the state before the first page).
Letters and digits are NEVER changed (the text is taken as supplied) — one exception, by the user's decision (Nov 9 2026): the misread reference abbreviations (tools/rv/refs_fix.py); the translator checks numerals against the user's numeral file."""
import re,sys,os
sys.path.insert(0,os.path.dirname(__file__)); import html_pages, refs_fix
KN='[ಀ-೿]'
LABELS=[('samhita',r'^ಸಂಹಿತಾ ?.{1,4}$'),('pada',r'ಪದ ?ಪಾ.{0,2}ಃ?$|^ಪದಪಾ|^ಪದಸಾರಃ$|^ಸದಪಾಠಃ$'),('bhashya',r'ಸಾಯಣ ?ಭಾಷ್ಯಂ$'),('pratipada',r'ಪ್ರತಿಪದಾರ್ಥ$'),('bhavartha',r'ಭಾ[ವನ]ಾರ್[ಥಧ]$|ಭಾವಾರ್ಥ$|ಭಾನಾರ್ಥ$'),
        ('english',r'^English Translation\.?$'),('special',r'ವಿಶೇಷ ?ವಿಷಯ.{0,6}$'),('grammar',r'ವ್ಯಾಕರಣ ?ಪ್ರಕ್ರಿಯ.{0,3}$')]
CANON={'samhita':'ಸಂಹಿತಾಪಾಠಃ','pada':'ಪದಪಾಠಃ','bhashya':'ಸಾಯಣಭಾಷ್ಯಂ','pratipada':'ಪ್ರತಿಪದಾರ್ಥ','bhavartha':'ಭಾವಾರ್ಥ','english':'English Translation.','special':'ವಿಶೇಷವಿಷಯಗಳು','grammar':'ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ'}
BLOCK={'samhita','pada','bhashya'}
DROP=('This image contains no discernible text',)
def clean_line(l):
    l=l.replace('||','॥').replace('|','।')
    l=re.sub('(?<='+KN+')[sS](?=-?'+KN+')','ಽ',l)   # also before a line-end hyphen (ತೇs-ಸ್ಮಿನ್), recurring in Vol 12
    l=refs_fix.fix_kn(l.strip().strip('*').strip())      # ಸಿ.→ನಿ., ಮಿ./ಮ./ಪು. ಸಂ.→ಋ. ಸಂ., ಇ. ಬ್ರಾ.→ಐ. ಬ್ರಾ. before a number (the user's reading of the print, Nov 9 2026)
    return '' if re.fullmatch(r'[-~_=. ]{3,}',l) else l
def label_of(l):
    t=re.sub(r'[॥।#*\s]+',' ',l).strip()
    if not t or len(t)>40: return None
    for k,pat in LABELS:
        if re.search(pat,t): return k
    return None
def kn_page(printed,head,text,section=None):
    """returns (markdown of the page, section at the end of the page)"""
    out=[f'<!-- printed {printed} -->']
    if head: out.append('*['+clean_line(head)+']*')
    out.append('')
    for raw in text.split('\n'):
        if any(d in raw for d in DROP): continue
        l=clean_line(raw)
        if not l: continue
        k=label_of(l)
        if k: section=k; out+=['',f'*{CANON[k]}*','']; continue
        out.append(('> '+l) if section in BLOCK else l)
    # paragraphs: blank line between non-block prose lines would change the layout; keep one line per printed line
    return '\n'.join(out)+'\n',section
def kn_pages(specs,pages,section=None):
    H={}; P=html_pages.load_many(specs,H); md=[]
    for p in pages:
        if p not in P: md.append(f'<!-- printed {p}: NOT IN THE SUPPLIED TEXT -->\n'); continue
        t,section=kn_page(p,H.get(p,''),P[p],section); md.append(t)
    return '\n'.join(md),section
if __name__=='__main__':
    a=sys.argv[1:]; sec=a[a.index('--section')+1] if '--section' in a else None
    specs=[x for x in a if '.html' in x or '.md' in x]; pi=a.index('--pages')+1; pages=[int(x) for x in a[pi:] if x.isdigit()]
    t,sec=kn_pages(specs,pages,sec); print(t); print('<!-- section at the end:',sec,'-->')
