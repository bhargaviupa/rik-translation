#!/usr/bin/env python3
"""Check the Sanskrit words that the second pass put into the English against the reference text (the Wikisource index) ONLY.

  python3 tools/rv/second_pass_sanskrit_check.py VOL

For every row of VOL/review/second_pass/findings.tsv that was applied ('[APPLIED' in `log`), the Sanskrit words (italic words, words with IAST letters, Devanagari)
of `proposed` that `as_found` did not have ('new') and those that `proposed` dropped ('old') are looked up in the whole index (refs/wikisource/index/ws.sqlite:
Sāyaṇa's bhāṣya, Saṃhitā, Pada of all maṇḍalas), letters only, accents and spaces ignored, as a substring (sandhi makes whole-word matching useless).
Row class:  N no Sanskrit word changed · A no new word missing and one of 8+ letters found (confirmed) · a no new word missing, found only words of 5-7 letters (weak: such a string
occurs by chance) · B a new word (5+ letters) NOT found while an old word of 8+ letters IS found (the reference supports the old form: candidate to revert) · b the same, old word of 5-7 letters
(weak) · C new word not found, old not found either (not in the index: sūtras, Nirukta, Brāhmaṇas: the reference says nothing) · S only words of under 5 letters.
Writes VOL/review/second_pass/sanskrit_check.tsv (one row per applied row and per word) and prints the counts. Changes nothing in the volume."""
import sys,os,re,csv,sqlite3,unicodedata,collections
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','publish','tools','translit'))
from indic_transliteration import sanscript
vol=sys.argv[1]; d=f'vol{vol}/review/second_pass'
def norm(s):
    s=unicodedata.normalize('NFD',s.lower())
    s=''.join(ch for ch in s if ch not in '॒́̀̍॑')
    s=unicodedata.normalize('NFC',s).replace('ṁ','ṃ').replace('ḹ','ḷ')
    return re.sub(r'[^a-zāīūṛṝḷṃḥṅñṭḍṇśṣ]','',s)
c=sqlite3.connect('refs/wikisource/index/ws.sqlite')
corpus=norm(' '.join(r[0] or '' for r in c.execute('select iast_s from para')))+'|'+'|'.join(norm((a or '')+(b or '')) for a,b in c.execute('select samhita_i,pada_i from rik'))
DEV=re.compile('[ऀ-ॿ]+'); IAST=re.compile('[āīūṛṝḷṃḥṅñṭḍṇśṣ]')
def words(t):
    out=[]
    for m in DEV.finditer(t):
        out.append(norm(sanscript.transliterate(m.group(),sanscript.DEVANAGARI,sanscript.IAST)))
    t2=DEV.sub(' ',t)
    for m in re.finditer(r'\*([^*\n]+)\*',t2):                 # italic: Sanskrit
        for w in re.split(r'[\s\-–—,;:.()\[\]"“”]+',m.group(1)):
            if w: out.append(norm(w))
    for w in re.split(r'[\s\-–—,;:.()\[\]"“”*]+',t2):          # any word with an IAST letter
        if IAST.search(w.lower()): out.append(norm(w))
    return [w for w in out if w]
CS=dict(delimiter='\t',quoting=csv.QUOTE_NONE,quotechar=None)
rows=list(csv.reader(open(f'{d}/findings.tsv',encoding='utf8',newline=''),**CS)); h=rows[0]; ix={x:i for i,x in enumerate(h)}
res=[['page','place','class','new_found','new_not_found','too_short','old_found','old_not_found','as_found','proposed']]; cnt=collections.Counter(); pages=collections.defaultdict(collections.Counter)
for r in rows[1:]:
    r+=['']*(len(h)-len(r))
    if '[APPLIED' not in r[ix['log']]: continue
    a,b=r[ix['as_found']],r[ix['proposed']]
    wa,wb=set(words(a)),set(words(b)); new=wb-wa; old=wa-wb
    inc=lambda w: w in corpus
    # a word of 5-7 letters is found by chance in a corpus of 5 million letters: only 8+ letters count as a real confirmation
    nF=[w for w in new if len(w)>=8 and inc(w)]; nf=[w for w in new if 5<=len(w)<8 and inc(w)]
    nn=[w for w in new if len(w)>=5 and not inc(w)]; sh=[w for w in new if len(w)<5]
    oF=[w for w in old if len(w)>=8 and inc(w)]; of=[w for w in old if 5<=len(w)<8 and inc(w)]
    on=[w for w in old if len(w)>=5 and not inc(w)]
    if not new: cl='N'
    elif nn and oF: cl='B'
    elif nn and of: cl='b'
    elif nn: cl='C'
    elif nF: cl='A'
    elif nf: cl='a'
    else: cl='S'
    cnt[cl]+=1
    res.append([r[ix['page']],r[ix['place']][:60],cl,' '.join(sorted(nF+nf)),' '.join(sorted(nn)),' '.join(sorted(sh)),' '.join(sorted(oF+of)),' '.join(sorted(on)),a,b])
csv.writer(open(f'{d}/sanskrit_check.tsv','w',encoding='utf8',newline=''),lineterminator='\n',**CS).writerows(res)
print(sum(cnt.values()),'applied rows;',dict(sorted(cnt.items())))
