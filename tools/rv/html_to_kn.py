"""Kannada text of printed pages, made by script from the supplied machine-read HTML/markdown (the base text for Vol 15 onwards).

  python3 tools/rv/html_to_kn.py "file.html@1-84" "file.md@85-184" --pages 86 87 88 [--section bhashya]

Cleaning (no model involved): '||' -> '॥', '|' -> '।'; a Latin 's' between Kannada letters -> the avagraha 'ಽ'; OCR notes such as 'This image contains no discernible text.'
are dropped; the section labels (Saṃhitā, Pada, Sāyaṇa-bhāṣya, Pratipadārtha, Bhāvārtha, English Translation, Viśeṣa-viṣayagaḷu, Vyākaraṇa-prakriyā) are recognised
despite the usual OCR variants (ಪಾರಃ for ಪಾಠಃ, ಭಾನಾರ್ಥ for ಭಾವಾರ್ಥ …) and written in one standard form. Lines of the Saṃhitā, Pada and bhāṣya sections become '> ' blocks;
everything else is prose. A page that starts without a label continues the section of the previous page (--section gives the state before the first page).
Letters and digits are NEVER changed (the text is taken as supplied) — one exception, by the user's decision (Nov 9 2026): the misread reference abbreviations (tools/rv/refs_fix.py); the translator checks numerals against the user's numeral file.

Structure repairs done by script since Nov 10 2026 (measured on Vol 12 pp. 2-196, where they were the bulk of the translator's hand-fixes; no letter or digit is changed):
  * garbled section labels: a short line that resembles the label expected next (order Saṃhitā, Pada, bhāṣya, Pratipadārtha, Bhāvārtha, English, Viśeṣa, Vyākaraṇa)
    is kept as an italic note '*[garbled]*' and the standard label is written after it;
  * missing labels: the Saṃhitā ends with its verse number '॥ N ॥', so the Pada starts after it and the bhāṣya after the Pada's '॥ N ॥'; a run of Latin text after
    the Bhāvārtha starts the printed English; a line that matches the next verse of the accented reference (refs/mandala) starts a Saṃhitā;
  * a word broken by a line-end hyphen is joined (same page, same kind of line; Kannada letters on both sides);
  * stray lines (signature marks '[5] Vol. 12', ornaments, 'This image contains ...') become italic notes '*[stray line as supplied: ...]*';
  * Devanagari letters inside a Kannada line are rewritten letter for letter as Kannada, with a note line.
The translator still checks the result; `batch.py prep` lists what the script did in WIN/TASK.md."""
import re,sys,os,difflib
sys.path.insert(0,os.path.dirname(__file__)); import html_pages, refs_fix
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.insert(0,os.path.join(ROOT,'publish','tools','translit'))
KN='[ಀ-೿]'; KL='[ಀ-೥ೱ-೿]'   # KL: letters and signs without the digits
LABELS=[('samhita',r'^ಸಂಹಿತಾ ?.{1,4}$'),('pada',r'ಪದ ?ಪಾ.{0,2}ಃ?$|^ಪದಪಾ|^ಪದಸಾರಃ$|^ಸದಪಾಠಃ$'),('bhashya',r'ಸಾಯಣ ?ಭಾಷ್ಯಂ$'),('pratipada',r'ಪ್ರತಿಪದಾರ್ಥ$'),('bhavartha',r'ಭಾ[ವನ]ಾರ್[ಥಧ]$|ಭಾವಾರ್ಥ$|ಭಾನಾರ್ಥ$'),
        ('english',r'^English Translation\.?$'),('special',r'ವಿಶೇಷ ?ವಿಷಯ.{0,6}$'),('grammar',r'ವ್ಯಾಕರಣ ?ಪ್ರಕ್ರಿಯ.{0,3}$')]
CANON={'samhita':'ಸಂಹಿತಾಪಾಠಃ','pada':'ಪದಪಾಠಃ','bhashya':'ಸಾಯಣಭಾಷ್ಯಂ','pratipada':'ಪ್ರತಿಪದಾರ್ಥ','bhavartha':'ಭಾವಾರ್ಥ','english':'English Translation.','special':'ವಿಶೇಷವಿಷಯಗಳು','grammar':'ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ'}
BLOCK={'samhita','pada','bhashya'}
DROP=()   # nothing is dropped any more: stray lines are kept as notes (CLAUDE.md rule)
def clean_line(l):
    l=l.replace('||','॥').replace('|','।').translate(TELUGU_DIGITS)     # Telugu digits (౧౦-౧೨೦) are Kannada digits misread (Vol 16 lesson 38)
    l=re.sub('(?<='+KN+')[sS](?=-?'+KN+')','ಽ',l)   # also before a line-end hyphen (ತೇs-ಸ್ಮಿನ್), recurring in Vol 12
    l=refs_fix.fix_kn(l.strip().strip('*').strip())      # ಸಿ.→ನಿ., ಮಿ./ಮ./ಪು. ಸಂ.→ಋ. ಸಂ., ಇ. ಬ್ರಾ.→ಐ. ಬ್ರಾ. before a number (the user's reading of the print, Nov 9 2026)
    return '' if re.fullmatch(r'[-~_=. ]{3,}',l) else l

TELUGU_DIGITS=str.maketrans('౦౧౨౩౪౫౬౭౮౯','೦೧೨೩೪೫೬೭೮೯')
ORDER=['samhita','pada','bhashya','pratipada','bhavartha','english','special','grammar']
NEXT={None:ORDER,'samhita':['pada'],'pada':['bhashya'],'bhashya':['pratipada'],'pratipada':['bhavartha'],'bhavartha':['english'],
      'english':['special','grammar','samhita'],'special':['grammar','samhita'],'grammar':['samhita']}
DECO=r'[॥।|#*\s:.,;\-–—_~=°೦-೯0-9\[\]()]+'
ENDNUM=re.compile(r'॥\s*[೦-೯0-9]{1,3}\s*(॥|।।)?\s*$')
START=[None]
EXTRA=[]        # printed pages found inside another page (missed running heads) in the last kn_pages call
LOG=[]          # what the structure pass did (shown to the translator by batch.py prep)
def _core(l): return re.sub('^'+DECO+'|'+DECO+'$','',l)
def _ratio(a,b): return difflib.SequenceMatcher(None,a,b).ratio()
def label_of(l):
    t=re.sub(r'[॥।#*\s]+',' ',l).strip().rstrip('.,:; ')
    if not t or len(t)>40: return None
    for k,pat in LABELS:
        if re.search(pat,t): return k
    return None
def fuzzy_label(l,section):
    """garbled label? -> key or None.  Only a short standalone line qualifies; the label expected next needs less resemblance than any other."""
    c=_core(l)
    if 'ಸಹಿತಾ' in c: return None            # a title line ('ಸಾಯಣಭಾಷ್ಯ ಸಹಿತಾ'), not the bhāṣya label (Vol 17 p. 1)
    if not c or len(c)>20 or len(c.split())>3 or not re.search(KN,c) or ENDNUM.search(l) or l.rstrip().endswith('.') and not l.rstrip().endswith('ಃ.'): return None
    best=None
    for k in ORDER:
        if k=='english': continue
        r=_ratio(c.replace(' ',''),CANON[k]); need=0.58 if k in NEXT.get(section,ORDER) else 0.78
        if r>=need and (best is None or r>best[0]): best=(r,k)
    return best[1] if best else None
def is_latin(l):
    a=re.findall(r'[A-Za-z]',l); k=re.findall(KN,l)
    return len(a)>=25 and len(a)>4*len(k) and len(l.split())>=6 and not l.startswith(('This image','The image','[figure'))
def stray(l):
    if re.match(r'(This|The) image (contains|is|shows)',l) or re.fullmatch(r'Pages?: ?\d+/\d+',l): return True
    if re.fullmatch(r'[\[(]?\s*\d{1,3}\s*[\])]?\s*Vol\.?\s*\d+\s*\]?|[\[(]\s*\d{1,3}\s*[\])]',l): return True
    return bool(not re.search(KN+'|[A-Za-z]{2}',l) and not re.search(r'[೦-೯0-9]',l) and len(l)<=12 and not re.fullmatch(r'[॥।\s]+',l))
_REF={}
def ref_index(mandalas):
    """{(m,s,r): normalised first line} of the accented reference (None if unavailable)"""
    key=tuple(mandalas or ())
    if key not in _REF:
        idx={}
        try:
            sys.path.insert(0,os.path.join(ROOT,'publish','tools','accents')); import accent_volume
            for m in key:
                f=os.path.join(ROOT,'refs','mandala',f'rv_mandala{m}.html')
                if os.path.exists(f):
                    for rid,line in accent_volume.read_ref(f): idx.setdefault(rid,_norm_deva(line))
        except Exception as e: LOG.append(f'reference text not used ({type(e).__name__}: {e})')
        _REF[key]=idx or None
    return _REF[key]
def _norm_deva(s): return re.sub(r'[^ऀ-ॣ]','',s.replace('॒','').replace('॑','').replace('ं','म्').replace('ऽ',''))[:40]
def _norm_kn(l):
    from kannada_to_deva import kn2deva
    return _norm_deva(kn2deva(l))
def quote_follows(lines,i):
    """a quotation inside the commentary (Vol 18 p. 625: Ṛk 4.57.2 quoted under Ṛk 1) is followed within three lines by its reference in brackets,
    e.g. (ಋ. ಸಂ. ೪-೫೭-೨); a Saṃhitā block is followed by the Pada-pāṭha, never by such a line (user, Nov 11 2026: a spurious label broke the label count)"""
    return any(re.fullmatch(r'\(.{2,40}[೦-೯0-9]+\s*[-–—]\s*[೦-೯0-9]+.*\)\.?',x.strip()) for x in lines[i+1:i+4])
def verse_start(l,ref,last,anywhere=False):
    """does this line begin a verse of the reference? -> id or None.  With a known position only the next verse (or the first of the next sūkta) is accepted."""
    if not ref or len(l)<18 or not re.search(KN,l): return None
    n=_norm_kn(l)
    if len(n)<12: return None
    if last: cand=[(last[0],last[1],last[2]+1),(last[0],last[1]+1,1),(last[0]+1,1,1)]
    elif anywhere: cand=list(ref)
    else: return None
    for rid in cand:
        r=ref.get(rid)
        if r and abs(len(r)-len(n))<=8 and _ratio(n[:len(r)],r[:len(n)])>=(0.8 if last else 0.92) and (last or len(n)>=28): return rid
    return None
def deva_to_kn_line(l):
    if not re.search('[ऀ-ॣ०-ॿ]',l): return l,False
    from deva_to_kannada import deva2kn
    return re.sub('[ऀ-ॣ०-ॿ]+',lambda m:deva2kn(m.group(0)),l),True
def kn_page(printed,head,text,section=None,st=None):
    """returns (markdown of the page, section at the end of the page).  st: dict carried from page to page (ref index, last verse, pending label)."""
    st=st if st is not None else {}; ref=st.get('ref'); st['page']=printed
    out=[f'<!-- printed {printed} -->']
    if head: out.append('*['+clean_line(head)+']*')
    out.append('')
    def setlabel(k,garbled=None,why=None):
        nonlocal section
        if garbled is not None: out.append(f'*[{garbled}]*')
        if why: LOG.append(f'p. {printed}: {why}')
        if st.get('lastlabel')==k and not st.get('content'): section=k; st['force']=None; return      # the same label twice with nothing between (block split by a page/window break)
        st['lastlabel']=k; st['content']=False
        section=k; out.extend(['',f'*{CANON[k]}*','']); st['force']=None; st['fresh']=(k=='samhita')
    lines=[clean_line(r) for r in text.split('\n')]; lines=[l for l in lines if l]
    for i,l in enumerate(lines):
        l,conv=deva_to_kn_line(l)
        if conv: out.append('*[Devanagari letters in the next line of the supplied text are rewritten letter for letter as Kannada (by script).]*'); LOG.append(f'p. {printed}: Devanagari letters rewritten as Kannada in: {l[:40]}')
        nx=st.get('page',printed)+1                 # a running head the splitter missed (misspelled title): the next printed page starts here
        if nx not in st.get('known',()) and '[' in l+']'[:0] or ']' in l:
            m=re.match(r'^(\d{1,4})\s+\S',l) or re.search(r'\S\s*(\d{1,4})$',l)
            if m and int(m.group(1))==nx and nx not in st.get('known',()) and len(l)<80 and re.search('ಹಿತಾ|ಪೀತಾ|ಭಾಷ್ಯ',l) and re.search(r'ಮಂ|ಅ\.|ಆ\.|ಸೂ',l):
                out.extend(['',f'<!-- printed {nx} -->',f'*[{l}]*','']); st['page']=nx; st.setdefault('extra',[]).append(nx)
                LOG.append(f'p. {nx}: running head not recognised by the page splitter ("{l[:40]}"): page marker inserted by script (add "### Printed p. {nx}" in en.md)'); continue
        k=label_of(l)
        if k: setlabel(k); continue
        if len(l)<=24 and _ratio(l.lower().rstrip('. '),'english translation')>=0.8: setlabel('english',l,f'garbled label "{l}" -> English Translation.'); continue
        if l.startswith('[figure'): out.append(l); continue
        if stray(l): out.append(f'*[stray line as supplied: {l}]*'); continue
        force=st.get('force'); fz=fuzzy_label(l,section if not force else {'pada':'samhita','bhashya':'pada'}[force])
        if force:                                   # the block before ended with its verse number: the next section is certain
            c=_core(l)
            if fz==force or (len(c)<=14 and len(c.split())<=3 and not ENDNUM.search(l)): setlabel(force,l,f'garbled label "{l}" -> {CANON[force]}'); continue
            setlabel(force,None,f'label {CANON[force]} missing in the supplied text: inserted')
        elif fz: setlabel(fz,l,f'garbled label "{l}" -> {CANON[fz]}'); continue
        if section!='samhita':
            rid=verse_start(l,ref,st.get('last'))
            if rid and quote_follows(lines,i): LOG.append(f'p. {printed}: verse-like lines {l[:30]}… followed by a printed reference: a quotation in the commentary, no label inserted'); rid=None
            if rid:
                st['last']=rid; prev=out[-1] if out else ''
                c=_core(prev)
                if prev and not prev.startswith(('*','<!--')) and c and len(c)<=14 and len(c.split())<=3 and not ENDNUM.search(prev):   # a short unreadable line right before the verse = its label
                    out.pop(); setlabel('samhita',prev.lstrip('> '),f'garbled label "{prev.lstrip("> ")}" before the verse {rid[1]}.{rid[2]} -> {CANON["samhita"]}')
                else: setlabel('samhita',None,f'label {CANON["samhita"]} missing before the verse {rid[1]}.{rid[2]}: inserted')
        elif st.get('fresh'):
            rid=verse_start(l,ref,st.get('last'),True) or verse_start(l,ref,None,True); st['fresh']=False
            if rid: st['last']=rid
        if section=='bhavartha' and is_latin(l): setlabel('english',None,'label English Translation missing: inserted before the Latin text')
        out.append(('> '+l) if section in BLOCK else l); st['content']=True
        if section in ('samhita','pada') and ENDNUM.search(l): st['force']={'samhita':'pada','pada':'bhashya'}[section]
    out=drop_dup_figures(out,printed)
    return '\n'.join(join_hyphens(out))+'\n',section
def drop_dup_figures(out,printed):
    """A `[figure: …]` line is the picture of a verse block or of a sūkta head that the machine-read text already has right after it: it is dropped
    and logged with its file name (user, Nov 11 2026; 13 of 13 figures in Vol 18 were of this kind, each compared by eye).  Not dropped: a figure
    with nothing after it on the page, or followed by anything else (the gate in batch.py then asks for the picture to be read)."""
    res=[]; samp=('*%s*'%CANON['samhita'],'*%s*'%CANON['pada'])
    for i,l in enumerate(out):
        if l.startswith('[figure'):
            nx=next((x for x in out[i+1:] if x.strip() and not x.startswith('*[')),'')      # notes (a stray picture description, a garbled label) are skipped
            if nx.startswith('> ') or nx in samp or nx.startswith(('ಸೂಕ್ತ','ಮಂಡಲ—')):
                LOG.append(f'p. {printed}: picture line {l} dropped by script: the supplied text has the verse block / sūkta head right after it (or the picture is an ornament)'); continue
        res.append(l)
    return res
def join_hyphens(out):
    """a word broken at a line end ('...ಪ್ರಥಿವೀ-' / 'ಶಬ್ದೋ ...') is joined: same page, both lines of the same kind (block or prose), Kannada letters on both sides"""
    res=[]
    for l in out:
        p=res[-1] if res else ''
        kind=lambda x: None if (not x or x.startswith(('*','<!--','[figure'))) else ('b' if x.startswith('> ') else 'p')
        if kind(p) and kind(p)==kind(l) and re.search('('+KL+'|(?<='+KL+')[sS])-$',p) and re.match('(> )?'+KL,l) and not ENDNUM.search(p):
            res[-1]=re.sub('[sS]$','ಽ',p[:-1])+(l[2:] if l.startswith('> ') else l)
        else: res.append(l)
    return res
def kn_pages(specs,pages,section=None,mandalas=None,warm=12):
    """Kannada text of `pages`.  The section (and the verse reached) at the start is found by running the same pass over the `warm` pages before
    (deterministic, so no state file is needed); `section` is used only when there are no earlier pages."""
    H={}; P=html_pages.load_many(specs,H); md=[]; st={'ref':ref_index(mandalas) if mandalas else None,'known':set(P)}
    before=[p for p in sorted(P) if p<min(pages)][-warm:] if pages else []
    for p in before: _,section=kn_page(p,H.get(p,''),P[p],section if p!=before[0] else None,st)
    START[:]=[section]                    # the section in which the first page of the window begins (a block there may continue a bhāṣya)
    del LOG[:]; st['extra']=[]
    for p in pages:
        if p not in P: md.append(f'<!-- printed {p}: NOT IN THE SUPPLIED TEXT -->\n'); continue
        t,section=kn_page(p,H.get(p,''),P[p],section,st); md.append(t)
    EXTRA[:]=st['extra']
    return '\n'.join(md),section
if __name__=='__main__':
    a=sys.argv[1:]; sec=a[a.index('--section')+1] if '--section' in a else None
    specs=[x for x in a if '.html' in x or '.md' in x]; pi=a.index('--pages')+1; pages=[int(x) for x in a[pi:] if x.isdigit()]
    t,sec=kn_pages(specs,pages,sec); print(t); print('<!-- section at the end:',sec,'-->')
