"""Compare two English volume files page by page (printed-page headings '### Printed p. N'), e.g. the scan-based Vol 14 text and the text
made from the supplied HTML.   python3 tools/rv/compare_translations.py OLD.md NEW.md FIRST LAST [--out report.md] [--tsv pages.tsv]
Per page: Devanagari block words that differ (accents, danda, digits ignored), English-prose word similarity, [?] counts, differing reference numerals.
Report only; nothing is changed."""
import re,sys,difflib,argparse,collections
ACC=dict.fromkeys([0x951,0x952,0x953,0x954,0x1CDA,0x1CF4],None)
def pages(path,lo,hi):
    out={}; cur=None
    for l in open(path,encoding='utf8').read().split('\n'):
        m=re.match(r'### Printed p\. (\d+)',l)
        if m: cur=int(m.group(1)); out.setdefault(cur,[]); continue
        if cur is not None and lo<=cur<=hi: out[cur].append(l)
    return out
def dev_words(lines):
    w=[]
    for l in lines:
        if l.startswith('> ') and not l.startswith('> *'):
            t=re.sub(r'\[\?\]','',l[2:]).translate(ACC)
            w+=[x for x in (re.sub(r'[^ऄ-हा-्क़-ॣ]','',y) for y in t.split()) if x]
    return w
def prose_words(lines):
    w=[]
    for l in lines:
        if l.startswith('> ') or l.startswith('*(') or l.startswith('###') or l.startswith('**Progress'): continue
        t=re.sub(r'\(\*[^*]*\*\)','',l); t=re.sub(r'[ऀ-ॿ]+','',t); t=re.sub(r'\[\?\]','',t)
        w+=re.findall(r"[a-z]+",t.lower())
    return w
def refs(lines):
    t=' '.join(lines); return collections.Counter(re.findall(r'\b\d+(?:-\d+)+\b',t))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('old'); ap.add_argument('new'); ap.add_argument('first',type=int); ap.add_argument('last',type=int); ap.add_argument('--out'); ap.add_argument('--tsv'); a=ap.parse_args()
    O=pages(a.old,a.first,a.last); N=pages(a.new,a.first,a.last); rows=[]; T=collections.Counter()
    for p in range(a.first,a.last+1):
        if p not in O or p not in N: continue
        od,nd=dev_words(O[p]),dev_words(N[p]); sm=difflib.SequenceMatcher(None,od,nd,autojunk=False)
        dd=sum(max(i2-i1,j2-j1) for t,i1,i2,j1,j2 in sm.get_opcodes() if t!='equal')
        op,np_=prose_words(O[p]),prose_words(N[p]); pr=difflib.SequenceMatcher(None,op,np_,autojunk=False).ratio() if op or np_ else 1.0
        ro,rn=refs(O[p]),refs(N[p]); rd=sorted(set((ro-rn).keys())|set((rn-ro).keys()))
        qo=sum(l.count('[?]') for l in O[p]); qn=sum(l.count('[?]') for l in N[p])
        rows.append((p,len(od),len(nd),dd,round(pr,3),len(op),len(np_),qo,qn,' '.join(rd[:6])))
        T['dev_words_old']+=len(od); T['dev_words_new']+=len(nd); T['dev_diff']+=dd; T['prose_old']+=len(op); T['prose_new']+=len(np_); T['q_old']+=qo; T['q_new']+=qn; T['ref_diff']+=len(rd)
    hdr='page\tdev_words_old\tdev_words_new\tdev_words_differing\tprose_similarity\tprose_words_old\tprose_words_new\tq_old\tq_new\treference_numerals_differing'
    tsv=hdr+'\n'+'\n'.join('\t'.join(map(str,r)) for r in rows)+'\n'
    if a.tsv: open(a.tsv,'w',encoding='utf8').write(tsv)
    sims=sorted(rows,key=lambda r:r[4])
    rep=[f'# Comparison of {a.old} and {a.new}, printed pp. {a.first}-{a.last} ({len(rows)} pages in both)','',
     f'- Devanagari block words: old {T["dev_words_old"]}, new {T["dev_words_new"]}; differing {T["dev_diff"]} ({100*T["dev_diff"]/max(1,T["dev_words_old"]):.1f} % of old)',
     f'- English prose words: old {T["prose_old"]}, new {T["prose_new"]}; mean page similarity {sum(r[4] for r in rows)/max(1,len(rows)):.3f}; pages below 0.80: {sum(r[4]<0.8 for r in rows)}',
     f'- `[?]` marks: old {T["q_old"]}, new {T["q_new"]}',f'- reference numerals that differ (distinct per page): {T["ref_diff"]}','','## 15 pages with the lowest prose similarity','page | prose sim | dev words differing',
     '--- | --- | ---']+[f'{r[0]} | {r[4]} | {r[3]}' for r in sims[:15]]+['','## 15 pages with most differing Devanagari words','page | differing | of']+['--- | --- | ---']+[f'{r[0]} | {r[3]} | {r[1]}' for r in sorted(rows,key=lambda r:-r[3])[:15]]
    txt='\n'.join(rep)+'\n'
    if a.out: open(a.out,'w',encoding='utf8').write(txt)
    print(txt)
if __name__=='__main__': main()
