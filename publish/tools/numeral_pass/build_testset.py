"""Build docs/numeral_testset.csv from git history of the Vol 11 English file.
Rows: every hyphenated reference numeral on PDF 7-72, classed
  gold      - changed or un-flagged by the user's review (d218cc7, 6eced87)
  silver_changed / silver_cleared - changed / [?] removed by the better-scan pass (PDF 25-72)
  silver_kept - present before and after the pass, unchanged (seen by the pass reader, not altered)
  doubtful  - still followed by [?]
python3 build_testset.py [MAXPDF] > docs/numeral_testset.csv"""
import re,subprocess,csv,sys,difflib
F='Rigveda_Samhita_Vol11_English_Translation.md'
def show(rev): return subprocess.run(['git','show',f'{rev}:{F}'],capture_output=True,text=True).stdout
def pages(t):
    out={}
    for s in re.split(r'\n(?=### Printed p\. )',t):
        m=re.match(r'### Printed p\. (\S+)\s+\(.*?PDF (\d+)',s)
        if m: out[int(m.group(2))]=(m.group(1),out.get(int(m.group(2)),('',''))[1]+s+'\n')
    return out
SEG=r'(?:\d{1,4}\??|\d*\[\?\]|\?{1,3})'
NUM=re.compile(r'(?<![\w.])('+SEG+r'(?:\s*-\s*'+SEG+r'){1,3})(?![\w])(\s*\[\?\])?')
def nums(line):
    r=[]
    for m in NUM.finditer(line):
        pre=re.sub(r'\[\?\]|\d|\[[^]]*\]|\s+',' ',line[max(0,m.start()-45):m.start()]).strip()[-28:]
        r.append(dict(val=re.sub(r'\s','',m.group(1)),flag=bool(m.group(2)) or '?' in m.group(1),key=pre,
                      ctx=line[max(0,m.start()-40):m.end()+12].replace('\n',' ')))
    return r
def label(ctx):
    for k,v in [('Pā','Panini'),('Uṇ','Unadi'),('Ni.','Nirukta'),('Nigh','Nighantu'),('Ṛ','Rg'),('Ṛg','Rg'),
                ('Brā','Brahmana'),('Saṃ','Samhita'),('De.','Brhaddevata'),('Varga','header'),('pp.','page'),('p. ','page')]:
        if k in ctx[-30:]: return v
    return 'other'
def align_page(old,new):
    """map each numeral on the new page to the most similar-context numeral on the old page"""
    o=[x for l in old.split('\n') for x in nums(l)]; used=set(); res=[]
    for n in [x for l in new.split('\n') for x in nums(l)]:
        best=None;br=0.0
        for i,x in enumerate(o):
            if i in used: continue
            r=difflib.SequenceMatcher(None,x['key'],n['key']).ratio()+(0.15 if x['val']==n['val'] else 0)
            if r>br: br,best=r,i
        if best is not None and br>=0.75: used.add(best); res.append((n,o[best]))
        else: res.append((n,None))
    return res
def align(old,new):
    """map each new numeral to an old one (by preceding text key, then order)"""
    o=nums(old); res=[]; used=set()
    for n in nums(new):
        j=next((i for i,x in enumerate(o) if i not in used and x['key']==n['key']),None)
        if j is None: j=next((i for i,x in enumerate(o) if i not in used),None) if len(nums(old))==len(nums(new)) else None
        if j is not None: used.add(j)
        res.append((n,o[j] if j is not None else None))
    return res
def pairlines(a,b):
    """yield (old_line,new_line) for each new line"""
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        for j in range(j1,j2):
            if tag=='equal': yield a[i1+j-j1],b[j]
            elif tag=='replace':
                best=max(a[i1:i2],key=lambda x:difflib.SequenceMatcher(None,x,b[j]).quick_ratio(),default='')
                yield best,b[j]
            else: yield '',b[j]
MAXPDF=int(sys.argv[1]) if len(sys.argv)>1 else 72
DEV=str.maketrans('०१२३४५६७८९','0123456789')
def rows():
    dev=set()
    now=pages(show('origin/main')); pre=pages(show('92ad6dd^')); prerev=pages(show('d218cc7^'))
    gold_after=pages(show('6eced87'))
    out=[]
    for pdf in sorted(now):
        if pdf>MAXPDF: continue
        pp,txt=now[pdf]
        oldp=pre.get(pdf,(pp,''))[1]
        gl=dict()
        # gold: lines changed by the review commits
        if pdf in prerev:
            if True:
                if True:
                    for n,o in align_page(prerev[pdf][1],gold_after.get(pdf,('',''))[1]):
                        if o and (o['val']!=n['val'] or o['flag']!=n['flag']) and not n['flag']:
                            gl[(n['key'],n['val'])]=o['val']+(' [?]' if o['flag'] else '')
        if True:
            for n,o in align_page(oldp,txt):
                k=(n['key'],n['val'])
                if n['flag']: src='doubtful'
                elif k in gl: src='gold'
                elif pdf>72: src='unverified'
                elif pdf<25 or o is None: src='unscored'
                elif o['val']!=n['val']: src='silver_changed'
                elif o['flag']: src='silver_cleared'
                else: src='silver_kept'
                before=gl.get(k) if src=='gold' else (o['val']+(' [?]' if o['flag'] else '') if o else '')
                val=n['val'].translate(DEV)
                if val!=n['val']: dev.add((pdf,val))
                elif (pdf,val) in dev and re.search(r'[|‖]',n['ctx']): continue   # IAST copy of a Devanagari citation
                n['val']=val
                out.append(dict(pdf=pdf,printed=pp,file='EN',kind=label(n['ctx'][:n['ctx'].find(n['val'][:2])+1] if n['val'][:2] in n['ctx'] else n['ctx']),
                    context=n['ctx'],reading=n['val'],source=src,before=before))
    return out
if __name__=='__main__':
    R=rows(); w=csv.DictWriter(sys.stdout,fieldnames=['id','pdf','printed','file','kind','context','reading','source','before','notes'])
    w.writeheader()
    for i,r in enumerate(R,1):
        r['id']=i; r['notes']=''; w.writerow(r)
    # Vol 8 gold triples (METHOD.md); different volume/scan, kept for reference only
    for i,(b,a) in enumerate([('4-537','4-557'),('2-9?2','2-252'),('1-27','1-26')],len(R)+1):
        w.writerow(dict(id=i,pdf='',printed='',file='Vol8',kind='Unadi' if i<len(R)+3 else 'other',context='Vol 8 review correction (METHOD.md)',reading=a,source='gold_vol8',before=b,notes='no image in this set'))
