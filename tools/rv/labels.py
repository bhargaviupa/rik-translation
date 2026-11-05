"""Normalise per-Ṛk section labels to the Vol 14 standard (label lines only; no content is touched)."""
import re
MAP=[(r'\*{1,2}Ṛk (\d+)\*{1,2}',r'#### Ṛk \1'),
 (r'\*{1,2}Saṃhitā-pāṭha\*{1,2}','**॥ संहितापाठः ॥**'),
 (r'\*{1,2}Pada-pāṭha\*{1,2}','**॥ पदपाठः ॥**'),
 (r'\*{1,2}Sāyaṇa-bhāṣya\*{1,2}','**॥ सायणभाष्यम् ॥**'),
 (r'\*{1,2}Pratipadārtha\*{1,2}','**प्रतिपदार्थ (Pratipadārtha)**'),
 (r'\*{1,2}Bhāvārtha\*{1,2}','**भावार्थ (Bhāvārtha)**'),
 (r'\*{1,2}Special Topics( \(Viśeṣaviṣayagaḷu\))?\*{1,2}','**विशेषविषयगळु (Viśeṣaviṣayagaḷu)**'),
 (r'\*{1,2}Viśeṣaviṣayagaḷu \(Special Topics\)\*{1,2}','**विशेषविषयगळु (Viśeṣaviṣayagaḷu)**')]
def normalise(text):
    out=[]
    for l in text.split('\n'):
        s=l.strip()
        for pat,rep in MAP:
            if re.fullmatch(pat,s): l=re.sub(pat,rep,s); break
        out.append(l)
    return '\n'.join(out)
