"""Numeral corrections for Vol 11 PDF 25-90: the user's review edits (docs/numeral_review/edits_PDF25-90.txt) plus the user's
gold answers for the 94 test crops; placed by page-order alignment (proposals_25_90.json) or by viewing the printed line."""
import sys,json,re
sys.path.insert(0,'publish/tools/verify11')
from fx import en,kn,sk
from cfg import EN,KN
K=str.maketrans('0123456789','೦೧೨೩೪೫೬೭೮೯'); k=lambda s:s.translate(K)
def sec(path,kind,pdf):
    t=open(path,encoding='utf8').read()
    pat=r'\n(?=### Printed p\. )' if kind=='en' else r'\n(?=<!-- PDF )'
    return ''.join(s for s in re.split(pat,t) if (re.match(r'### Printed p\. \S+\s+\(.*?PDF %d\)'%pdf,s) if kind=='en' else re.match(r'<!-- PDF %d '%pdf,s)))
AP={'53_15'}          # printed number differs from the usual one
ALIGNED=['27_27','31_7','41_26','46_20','46_24','50_21','52_6','52_12','53_15','54_4','57_33','58_3','58_5','58_14','59_6','68_22','69_3','71_4','72_8','78_4','81_8','84_5','84_7','84_8','88_27','90_5','90_6']
P={p['id']:p for p in json.load(open('publish/tools/numeral_pass/batches/proposals_25_90.json'))}
# compute every anchor from the untouched page text, then apply from the end of the page backwards
from collections import defaultdict
jobs=defaultdict(list)
for i in ALIGNED:
    p=P[i]; pdf=p['pdf']; new=p['new'].replace('3-1 84','3-1-84')
    for kind,g,val in (('kn',p['kn'],k(new)),('en',p['en'],new+(' [as printed]' if i in AP else ''))):
        if g: jobs[(kind,pdf)].append((g['start'],g['end'],val))
        elif kind=='en': print('   EN to do by hand:',i,pdf,new)
for (kind,pdf),js in jobs.items():
    s=sec(KN if kind=='kn' else EN,kind,pdf); pairs=[]
    for st,e,val in sorted(js,reverse=True):
        a=s[max(0,st-25):e]; pairs.append((a,a[:len(a)-(e-st)]+val))
    (kn if kind=='kn' else en)(pdf,pairs)
# EN for the list on p. 40 (PDF 58) and 10-119-1 [?] on PDF 84 handled below if not aligned
# --- placed by viewing the printed line ---
kn(52,[('೯-೬೨-೧[?];','೯-೬೭-೧೨;')]); en(52,[('9-62-1[?],','9-67-12,')])
kn(53,[('ಅಭ್ಯಾಸಕ್ಕೆ ಹ್ರಸ್ವ; ಪದಸಂಜ್ಞೆ…)','ಅಭ್ಯಾಸಕ್ಕೆ ಹ್ರಸ್ವ; ಧಾತುವಿನ ಆಕಾರಕ್ಕೆ ಲೋಪ (ಪಾ. ಸೂ. ೬-೪-೬೪); ಪದಸಂಜ್ಞೆ…; ನಕಾರಕ್ಕೆ ರುತ್ವ (ಪಾ. ಸೂ. ೮-೩-೮); ಆತೋಽಟಿ ನಿತ್ಯಮ್ (ಪಾ. ಸೂ. ೮-೩-೩))'),
        ('ಬಹುಲಂ ಛಂದಸಿ; ಶ್ಲೌ)','ಬಹುಲಂ ಛಂದಸಿ; ಶ್ಲೌ; ಉರತ್ (ಪಾ. ಸೂ. ೭-೪-೬೬))')])
en(53,[('*ririvān* not *pada*, hence the *ni*…)','loss of the root\'s *ā* (Pā. Sū. 6-4-64); *ririvān* not *pada*, hence the *ni*…; *ru* for the *n* (Pā. Sū. 8-3-8); *āto \'ṭi nityam* (Pā. Sū. 8-3-3))'),
       ('*luk* of *śap* and so on)','*luk* of *śap* and so on; *urat* (Pā. Sū. 7-4-66))'),
('Sūtra numbers not read.','Sūtra numbers partly read (better scan).')])
kn(53,[('ಸೂತ್ರಸಂಖ್ಯೆಗಳನ್ನು ಓದಿಲ್ಲ.','ಸೂತ್ರಸಂಖ್ಯೆಗಳನ್ನು ಭಾಗಶಃ ಓದಿದೆ.')])
kn(60,[('ವಕ್ತವ್ಯಃ** ಎಂಬುದರಿಂದ','ವಕ್ತವ್ಯಃ** (ಪಾ. ಸೂ. ೬-೩-೨೬-೧) ಎಂಬುದರಿಂದ')]); en(60,[('*ubhayatra vāyoḥ pratiṣedho vaktavyaḥ*;','*ubhayatra vāyoḥ pratiṣedho vaktavyaḥ* (Pā. Sū. 6-3-26-1);')])
en(64,[('reads 5-62-3 [?])','reads 5-62-3)')])
sk(67,[('निरुक्तम् । ३-३ [?] ।','निरुक्तम् । ५-५ ।')])
sk(73,[('त्रिबन्धुरः [?] । ऋ. [?] ।','त्रिबन्धुरः [?] । ऋ. ८-२२-५ ।')])
kn(76,[('ಷೀದನ್ [?] ।  (ಋ. ಸಂ. ೭-[?]-[?])'.replace('  ','\n\n'),'ಷೀದನ್ [?] ।  (ಋ. ಸಂ. ೭-೩೪-೧೬)'.replace('  ','\n\n'))])
en(76,[('ṣīdan [?] |*  (Ṛ. Saṃ. 7-[?]-[?] [?])'.replace('  ','\n\n'),'ṣīdan [?] |*  (Ṛ. Saṃ. 7-34-16)'.replace('  ','\n\n'))])
kn(77,[('ಚಿಣ್ ಭಾವಕರ್ಮಣೋಃ (ಪಾ. ಸೂ. [?])','ಚಿಣ್ ಭಾವಕರ್ಮಣೋಃ (ಪಾ. ಸೂ. ೩-೧-೬೬)'),('ತನಾದಿಕೃಞ್ಭ್ಯ ಉಃ (ಪಾ. ಸೂ. [?])','ತನಾದಿಕೃಞ್ಭ್ಯ ಉಃ (ಪಾ. ಸೂ. ೩-೧-೭೯)'),('ನಭ್ರಾಣ್ನಪಾತ್… (ಪಾ. ಸೂ. [?])','ನಭ್ರಾಣ್ನಪಾತ್… (ಪಾ. ಸೂ. ೬-೩-೭೫)')])
en(77,[('*ciṇ bhāvakarmaṇoḥ* (Pā. Sū. 3-1-[?])','*ciṇ bhāvakarmaṇoḥ* (Pā. Sū. 3-1-66)'),('hya uḥ* (Pā. Sū. 3-1-[?])','hya uḥ* (Pā. Sū. 3-1-79)'),('*nabhrāṇnapāt…* (Pā. Sū. 6-3-[?])','*nabhrāṇnapāt…* (Pā. Sū. 6-3-75)')])
kn(81,[('…[?]; ಅಂತ್ಯೋದಾತ್ತಸ್ವರ ಬರುತ್ತದೆ; ತೃತೀಯಾ ಬಹುವಚನಾಂತರೂಪ','…[?] (ಪಾ. ಸೂ. ೬-೧-೧೯೭) ಎಂಬುದರಿಂದ ಆದ್ಯುದಾತ್ತಸ್ವರ ಬರುತ್ತದೆ; ತೃತೀಯಾ ಬಹುವಚನಾಂತರೂಪ')])
en(81,[('(Pā. Sū. 6-1-[?]) final-syllable; instrumental plural','(Pā. Sū. 6-1-197) first-syllable accent; instrumental plural')])
kn(88,[('ಹೋತಾರಂ** ಎಂಬ ಸೂತ್ರದಿಂದ ವಿವೃತವಾಗಿರುವುದು. (ಆ. [?]-[?])','ಹೋತಾರಂ** ಎಂಬ ಸೂತ್ರದಿಂದ ವಿವೃತವಾಗಿರುವುದು. (ಆ. ೮-೧)')]); en(88,[("'gniṃ hotāram*) (Āś. [?]-[?])","'gniṃ hotāram*) (Āś. 8-1)")])
kn(89,[('(ತೈ. ಸಂ. ೩-[?]-[?]-[?])','(ತೈ. ಸಂ. ೨-೫-೧೧-೮)'),('ಶಿವಃ ಸಖಾ ।  (ಋ. ಸಂ. ೧-[?]-[?])'.replace('  ','\n\n'),'ಶಿವಃ ಸಖಾ ।  (ಋ. ಸಂ. ೧-೩೧-೧)'.replace('  ','\n\n'))])
en(89,[('(Tai. Saṃ. 3-[?]-[?]-[?] [?].)','(Tai. Saṃ. 2-5-11-8.)'),('(Ṛ. Saṃ. 1-31-[?] [?].)','(Ṛ. Saṃ. 1-31-1.)')])
# the English text of the p. 40 list sits at the end of the PDF 57 section (the sentence crosses the page break)
en(57,[('in Ṛ. Saṃ. 5-58-9 [?]; 2-30-11; 6-58-8 [?] and others','in Ṛ. Saṃ. 5-56-9; 2-30-11; 7-56-8 and others')])
