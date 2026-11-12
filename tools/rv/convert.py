"""Kannada-first conversion for one window (3 pages).

kn.md  = the Kannada transcription written by the translator from the page images (Sanskrit blocks as '> ' lines; inline Sanskrit may be marked ⟦ಅಗ್ನಿಂ⟧).
en.md  = the English-file chunk written by the translator: English, labels, headings, and for every Sanskrit block a line  [[bN]]  (N = number of the
         '> ' block in kn.md, counted from 1 in order of appearance); inline Sanskrit is written in Kannada script inside ⟦ ⟧ (copied from kn.md).
The script never retypes Sanskrit: [[bN]] is replaced by the Devanagari conversion of block N, ⟦kannada⟧ by ⟦devanagari⟧; IAST is added later by add_iast.py.
"""
import re,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','..','publish','tools','translit'))
from kannada_to_deva import kn2deva
KNC=re.compile('[ಀ-೿]')
def kn_blocks(kn_text):
    """list of blocks (each a list of text lines without '> ') in order of appearance"""
    blocks=[];cur=None
    for l in kn_text.split('\n'):
        if l.startswith('> ') and not l.startswith('> *'):
            if cur is None: cur=[]; blocks.append(cur)
            cur.append(l[2:])
        else: cur=None
    return blocks
def kn_flat(kn_text):
    """kn.md as one line of text for quotation look-up: block prefixes, page markers and note lines dropped, line breaks -> spaces"""
    ls=[re.sub(r'^> ','',l) for l in kn_text.split('\n') if l.strip() and not l.startswith(('<!--','*[','[figure')) and not re.fullmatch(r'\*[^*]+\*',l.strip())]
    return re.sub(r'\s+',' ',' '.join(ls))
RESTORED=[]   # labels put in or normalised by `expand` in the last call
FUZZY=[]     # markers that were resolved approximately in the last call: (marker, passage found)
def _near(q,hay,cut=85):
    """best place of q in hay, tolerant of a few different letters -> (start,end) in hay or None"""
    try:
        from rapidfuzz import fuzz
        al=fuzz.partial_ratio_alignment(q,hay)
        return (al.dest_start,al.dest_end) if al and al.score>=cut and al.dest_end-al.dest_start>=max(3,len(q)-3) else None
    except ImportError:
        import difflib
        m=difflib.SequenceMatcher(None,q,hay,autojunk=False).find_longest_match(0,len(q),0,len(hay))
        return (m.b-m.a,m.b-m.a+len(q)) if m.size>=0.7*len(q) and m.b-m.a>=0 else None
def resolve_markers(en_text,kn_text,prob=None,maxlen=900):
    """⟦START~~END⟧ -> ⟦the passage of kn.md from START to END⟧.  For long quotations: the translator writes only the first and last words and the
    script copies the passage, with a closing danda or printed dots that follow it.  Matching ignores spaces and dandas.  Since Nov 11 2026 (Vol 17:
    most first-pass gate failures were markers) the look-up is forgiving but bounded: quotations are taken in the order of the text, so of several
    places where START occurs the first one after the previous quotation is used; START or END that differ from kn.md by a letter or two are found
    by nearest match; END must follow START within `maxlen` characters (Vol 16: an unbounded home-made expander swallowed pages).  Every
    approximate resolution is listed in FUZZY (batch.py writes them to WIN/markers_fuzzy.tsv)."""
    flat=kn_flat(kn_text); prob=prob if prob is not None else []; del FUZZY[:]
    pos=[i for i,c in enumerate(flat) if c not in ' ।॥']; ns=''.join(flat[i] for i in pos); cur=[0]
    clean=lambda x: re.sub(r'[\s।॥]+','',x)
    def rep(m):
        a,b=[clean(x) for x in m.group(1).split('~~',1)]; b=re.sub(r'[.…]+$','',b); approx=False
        if not a or not b: prob.append('empty START or END in '+m.group(0)[:50]); return m.group(0)
        starts=[x.start() for x in re.finditer(re.escape(a),ns)]
        if not starts:
            nr=_near(a,ns)
            if nr: starts=[nr[0]]; a=ns[nr[0]:nr[1]]; approx=True
        if not starts: prob.append(f'⟦{a}~~…⟧: START not found in kn.md'); return m.group(0)
        starts=[x for x in starts if x>=cur[0]] or starts                # in text order: the first place after the previous quotation
        for i in starts:
            span=ns[i+len(a):i+len(a)+maxlen]; j=span.find(b); ln=len(b)
            if j<0:
                nr=_near(b,span)
                if nr: j,ln=nr[0],nr[1]-nr[0]; approx=True
            if j<0: continue
            i0=pos[i]; j1=pos[i+len(a)+j+ln-1]+1
            if j1-i0>maxlen+200: continue
            m2=re.match(r'[\s.…]*[।॥]?',flat[j1:])              # printed abridgement dots and the danda that closes the quotation belong to it
            if m2: j1+=m2.end()
            cur[0]=i+len(a)+j+ln; out=flat[i0:j1].strip()
            if approx or len(starts)>1: FUZZY.append((m.group(0),out[:120]))
            return '⟦'+out+'⟧'
        prob.append(f'⟦{a}~~{b}⟧: END not found within {maxlen} characters after START'); return m.group(0)
    return re.sub(r'⟦([^⟧]*~~[^⟧]*)⟧',rep,en_text)
SECTION_OF={'ಸಂಹಿತಾಪಾಠಃ':'samhita','ಪದಪಾಠಃ':'pada','ಸಾಯಣಭಾಷ್ಯಂ':'bhashya'}
def block_sections(kn_text,start=None):
    """section of every '> ' block of kn.md, in order ('samhita', 'pada', 'bhashya' or None); `start` = section in which the window begins"""
    out=[];sec=start;inb=False
    for l in kn_text.split('\n'):
        m=re.fullmatch(r'\*([^*\[\]]+)\*',l.strip())
        if m: sec=SECTION_OF.get(m.group(1).strip())
        isb=l.startswith('> ') and not l.startswith('> *')
        if isb and not inb: out.append(sec)
        inb=isb
    return out
LABEL_EN={'samhita':'Saṃhitā-pāṭha','pada':'Pada-pāṭha','bhashya':'Sāyaṇa-bhāṣya'}
def block_labelled(kn_text):
    """for every '> ' block of kn.md: True when a section label line (*ಸಂಹಿತಾಪಾಠಃ* …) stands right before it"""
    out=[];inb=False;prev=''
    for l in kn_text.split('\n'):
        isb=l.startswith('> ') and not l.startswith('> *')
        if isb and not inb: out.append(bool(re.fullmatch(r'\*([^*\[\]]+)\*',prev)) and SECTION_OF.get(prev.strip('*').strip()) is not None)
        inb=isb
        if l.strip(): prev=l.strip()
    return out
def _fix_label(out,sec,restored):
    """the translator left the label out or wrote it as plain text (Vol 18: Ṛk 2 of w0156, Ṛk 4 of w0821, Ṛk 17 of w0235): put `**label**` before the block"""
    name=LABEL_EN[sec]; k=len(out)-1
    while k>=0 and not out[k].strip(): k-=1
    if k>=0 and re.fullmatch(r'\**\s*'+re.escape(name)+r'\s*\**:?',out[k].strip()):
        if out[k].strip()!=f'**{name}**': restored.append(f'{name}: label written as "{out[k].strip()}" -> **{name}**'); out[k]=f'**{name}**'
        return
    if k>=0 and re.fullmatch(r'\*\*[^*]*(pāṭha|bhāṣya)[^*]*\*\*',out[k].strip(),re.I): return      # another spelling of the label: left to labels.normalise
    out+=['',f'**{name}**']; restored.append(f'{name}: label missing before the block: inserted **{name}**')
LABEL_RE=re.compile(r'\*\*(Saṃhitā-pāṭha|Pada-pāṭha|Sāyaṇa-bhāṣya)\*\*')
_LABSEC={'Saṃhitā-pāṭha':'samhita','Pada-pāṭha':'pada','Sāyaṇa-bhāṣya':'bhashya'}
def label_mismatches(en_text,kn_text,start=None):
    """[[bN]] of a Saṃhitā/Pada/bhāṣya block standing under the label of ANOTHER section (the model counted the blocks one off, Vol 18: w0162, w0223,
    w0316, w0371, w0445, w0729: no other gate saw it, the text looked complete)"""
    secs=block_sections(kn_text,start); cur=None; bad=[]
    for l in en_text.split('\n'):
        m=LABEL_RE.fullmatch(l.strip())
        if m: cur=_LABSEC[m.group(1)]; continue
        m=re.fullmatch(r'\s*\[\[b(\d+)\]\]\s*',l)
        if m:
            n=int(m.group(1))
            if cur and n-1<len(secs) and secs[n-1] in LABEL_EN and secs[n-1]!=cur: bad.append(n)
            cur=None
    return bad
NOIAST='§NOIAST§ '
def expand(en_text,kn_text,plain=(),start=None):
    """returns (text, problems)"""
    blocks=kn_blocks(kn_text); used=set(); prob=[]; out=[]; secs=block_sections(kn_text,start); lab=block_labelled(kn_text); del RESTORED[:]
    # ⟪…⟫ = Sanskrit written by the translator in Kannada script (the grammar sections from Vol 17 on): converted to Devanagari, no IAST, not matched against kn.md
    en_text=re.sub(r'⟪([^⟫]*)⟫',lambda m:kn2deva(re.sub(r'\s*\n\s*',' ',m.group(1)).strip()),en_text)
    en_text=resolve_markers(en_text,kn_text,prob)
    en_text=re.sub(r'(⟦[^⟧]*[।॥]\s*⟧)[ \t]*[।॥]',r'\1',en_text)        # the danda already inside the quotation is not written a second time after it (Vol 18: 8 places)
    # a quotation may be broken over several lines in en.md: join it first (add_iast.py and the line-wise conversion below work on single lines)
    en_text=re.sub(r'⟦([^⟧]*)⟧',lambda m:'⟦'+re.sub(r'\s*\n\s*',' ',m.group(1)).strip()+'⟧',en_text)
    for l in en_text.split('\n'):
        m=re.fullmatch(r'\s*\[\[b(\d+)\]\]\s*',l)
        if m:
            n=int(m.group(1))
            if not 1<=n<=len(blocks): prob.append(f'[[b{n}]] does not exist (kn.md has {len(blocks)} blocks)'); out.append(l); continue
            if n in used: prob.append(f'[[b{n}]] used twice')
            if n-1<len(secs) and secs[n-1] in LABEL_EN and n-1<len(lab) and lab[n-1]: _fix_label(out,secs[n-1],RESTORED)
            used.add(n); pre=NOIAST if (n-1<len(secs) and secs[n-1] in plain) else '> '; out+=[pre+kn2deva(x) for x in blocks[n-1]]   # a block listed in `plain` gets no IAST layer
        else:
            if re.search(r'\[\[b\d+\]\]',l): prob.append('[[bN]] must stand alone on its line: '+l[:60])
            out.append(re.sub(r'⟦([^⟧]*)⟧',lambda m:'⟦'+kn2deva(m.group(1))+'⟧' if KNC.search(m.group(1)) else m.group(0),l))
    unused=[i for i in range(1,len(blocks)+1) if i not in used]
    if unused: prob.append('Sanskrit blocks of kn.md not placed in en.md (never omit a block silently): '+', '.join(f'b{i}: '+blocks[i-1][0][:30] for i in unused))
    return '\n'.join(out),prob
def kn_final(kn_text):
    """drop the inline markers; a Devanagari avagraha typed by mistake becomes the Kannada one (U+0CBD)"""
    return kn_text.replace('⟦','').replace('⟧','').replace(chr(0x093D),chr(0x0CBD))
