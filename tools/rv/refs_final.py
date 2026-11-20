#!/usr/bin/env python3
"""The final list: one work, ONE form, in the three scripts (user, Nov 19-20 2026: "one book is referenced in one way ONLY").
Made from rv/references.tsv (legend + extra rows) with the user's decisions applied: more complete variant wins, no "or" forms, duplicates merged.
  python3 tools/rv/refs_final.py   -> REFERENCES_FINAL.tsv and REFERENCES_FINAL.md (a proposal for the user; rv/references.tsv itself is not changed here)."""
import csv, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
from indic_transliteration import sanscript
lst = list(csv.DictReader(open(os.path.join(ROOT, 'rv', 'references.tsv'), encoding='utf8'), delimiter='\t'))
three = {r['English form']: r for r in csv.DictReader(open(os.path.join(ROOT, 'REFERENCES_THREE_SCRIPTS.tsv'), encoding='utf8'), delimiter='\t')} if os.path.exists(os.path.join(ROOT, 'REFERENCES_THREE_SCRIPTS.tsv')) else {}
def dev(en):
    d = sanscript.transliterate(en, sanscript.IAST, sanscript.DEVANAGARI); return re.sub(r'(\S)्\.', r'\1.', d)
# decisions: english form in the list -> (final English, final Kannada or None = keep, merged-into note)
RENAME = {'Ā. Sū. or Ā.': ('Ā. Sū.', 'ಆ. ಸೂ.'), 'Phi. or Phi. Sū.': ('Phi. Sū.', 'ಫಿ. ಸೂ.'), 'Jai. Sū.': ('Jai. Pū. Sū.', 'ಜೈ. ಪೂ. ಸೂ.')}
MERGE = {'A. Ve.': 'Ath. Saṃ.', 'Pa. Brā.': 'Tā. Brā.', 'Uṇ. Sū.': 'U. Sū.', 'Īśa.': 'Īśa U.', 'Śā. Bhā.': 'Śa. Bhā.'}
GUESS = {'Kā.', 'M.', 'Sāṃ. Gṛ. Sū.', 'Vāl.', 'Anu.', 'Dhā.', 'Ṛgvi.', 'Piṅ.', 'Pā. Gṛ. Sū.', 'Pā. Sū. Vā.', 'Mu. U. Śa. Bhā.', 'Ya Saṃ.', 'Ṛ. Saṃ. Bhā.', 'Tai. Saṃ. Bha. Bhā.', 'Ai. U. Śa. Bhā.', 'Tai. U. Śa. Bhā.', 'Śa. Bhā. Bra. Sū.', 'Kau. Brā.', 'Ka. U.', 'Pa. Brā.', 'Mā. Gṛ. Sū.'}
GIVEN = {'Tai. U.', 'Kau. U.', 'Pra. U.', 'Īśa U.', 'Ke. U.', 'Mā. U.', 'Śa. Bhā.', 'Bṛ. De.'}
KNFULL = {'Ath. Saṃ.': 'ಅಥರ್ವವೇದ ಸಂಹಿತೆ', 'Āp. Sū.': 'ಆಪಸ್ತಂಬ ಶ್ರೌತಸೂತ್ರ', 'Āp. Dha. Sū.': 'ಆಪಸ್ತಂಬ ಧರ್ಮಸೂತ್ರ', 'Āp. Pa. Sū.': 'ಆಪಸ್ತಂಬ ಪರಿಭಾಷಾಸೂತ್ರ', 'Ā. Sū.': 'ಆಶ್ವಲಾಯನ ಶ್ರೌತಸೂತ್ರ', 'U. Sū.': 'ಉಣಾದಿಸೂತ್ರ', 'Ṛ. Saṃ.': 'ಋಗ್ವೇದ ಸಂಹಿತೆ', 'Ai. Ā.': 'ಐತರೇಯ ಆರಣ್ಯಕ', 'Ai. U.': 'ಐತರೇಯ ಉಪನಿಷತ್ತು', 'Ai. Brā.': 'ಐತರೇಯ ಬ್ರಾಹ್ಮಣ', 'Chā. U.': 'ಛಾಂದೋಗ್ಯ ಉಪನಿಷತ್ತು', 'Jai. Pū. Sū.': 'ಜೈಮಿನೀಯ ಪೂರ್ವಮೀಮಾಂಸಾಸೂತ್ರ', 'Jai. Nyā. Vi.': 'ಜೈಮಿನೀಯ ನ್ಯಾಯಮಾಲಾವಿಸ್ತರ', 'Tā. Brā.': 'ತಾಂಡ್ಯ ಮಹಾಬ್ರಾಹ್ಮಣ (ಪಂಚವಿಂಶ ಬ್ರಾಹ್ಮಣ)', 'Tai. Ā.': 'ತೈತ್ತಿರೀಯ ಆರಣ್ಯಕ', 'Tai. Brā.': 'ತೈತ್ತಿರೀಯ ಬ್ರಾಹ್ಮಣ', 'Tai. Saṃ.': 'ತೈತ್ತಿರೀಯ ಸಂಹಿತೆ', 'Ni.': 'ನಿರುಕ್ತ, ನಿಘಂಟು', 'Pā. Sū.': 'ಪಾಣಿನೀಯ ಸೂತ್ರ', 'Pā. Śi.': 'ಪಾಣಿನೀಯ ಶಿಕ್ಷಾ', 'Phi. Sū.': 'ಫಿಟ್ಸೂತ್ರ', 'Bra. Sū.': 'ಬ್ರಹ್ಮಸೂತ್ರ', 'Ma. Bhā.': 'ಮಹಾಭಾರತ', 'Ma. Smṛ.': 'ಮನುಸ್ಮೃತಿ', 'Mai. Saṃ.': 'ಮೈತ್ರಾಯಣೀಯ ಸಂಹಿತೆ', 'Yā. Smṛ.': 'ಯಾಜ್ಞವಲ್ಕ್ಯ ಸ್ಮೃತಿ', 'Vā. Saṃ.': 'ವಾಜಸನೇಯ ಸಂಹಿತೆ', 'Vā. Pu.': 'ವಾಯು ಪುರಾಣ', 'Vi. Pu.': 'ವಿಷ್ಣು ಪುರಾಣ', 'Ve. Sū.': 'ವೇದಾಂತಸೂತ್ರ', 'Śa. Brā.': 'ಶತಪಥ ಬ್ರಾಹ್ಮಣ', 'Sā. Saṃ.': 'ಸಾಮವೇದ ಸಂಹಿತೆ ಇತ್ಯಾದಿ', 'Bṛ. De.': 'ಬೃಹದ್ದೇವತಾ', 'Bṛ. U.': 'ಬೃಹದಾರಣ್ಯಕ ಉಪನಿಷತ್ತು', 'Tai. U.': 'ತೈತ್ತಿರೀಯ ಉಪನಿಷತ್ತು', 'Mai. U.': 'ಮೈತ್ರಾಯಣೀಯ ಉಪನಿಷತ್ತು', 'Mu. U.': 'ಮುಂಡಕ ಉಪನಿಷತ್ತು', 'Mā. U.': 'ಮಾಂಡೂಕ್ಯ ಉಪನಿಷತ್ತು', 'Śve. U.': 'ಶ್ವೇತಾಶ್ವತರ ಉಪನಿಷತ್ತು', 'Pra. U.': 'ಪ್ರಶ್ನ ಉಪನಿಷತ್ತು', 'Bha. Gī.': 'ಭಗವದ್ಗೀತೆ', 'Go. Brā.': 'ಗೋಪಥ ಬ್ರಾಹ್ಮಣ', 'Hi. Gṛ. Sū.': 'ಹಿರಣ್ಯಕೇಶಿ ಗೃಹ್ಯಸೂತ್ರ', 'Ā. Gṛ. Sū.': 'ಆಶ್ವಲಾಯನ ಗೃಹ್ಯಸೂತ್ರ', 'Kau. Sū.': 'ಕೌಶಿಕಸೂತ್ರ', 'Sāṃ. Śrau. Sū.': 'ಸಾಂಖ್ಯಾಯನ ಶ್ರೌತಸೂತ್ರ', 'Tai. Saṃ. Bhā.': 'ತೈತ್ತಿರೀಯ ಸಂಹಿತೆಯ ಸಾಯಣಭಾಷ್ಯ', 'Kau. U.': 'ಕೌಷೀತಕಿ ಉಪನಿಷತ್ತು', 'Kau. Brā.': 'ಕೌಷೀತಕಿ ಬ್ರಾಹ್ಮಣ', 'Ka. U.': 'ಕಠ ಉಪನಿಷತ್ತು', 'Mā. Gṛ. Sū.': 'ಮಾನವ ಗೃಹ್ಯಸೂತ್ರ', 'Ya Saṃ.': 'ಯಜುರ್ವೇದ ಸಂಹಿತೆ', 'Ṛ. Saṃ. Bhā.': 'ಋಗ್ವೇದ ಸಂಹಿತೆಯ ಭಾಷ್ಯ', 'Tai. Saṃ. Bha. Bhā.': 'ತೈತ್ತಿರೀಯ ಸಂಹಿತೆಯ ಭಟ್ಟಭಾಸ್ಕರ ಭಾಷ್ಯ', 'Śa. Bhā.': 'ಶಂಕರ ಭಾಷ್ಯ', 'Ai. U. Śa. Bhā.': 'ಐತರೇಯ ಉಪನಿಷತ್ತಿನ ಶಂಕರ ಭಾಷ್ಯ', 'Tai. U. Śa. Bhā.': 'ತೈತ್ತಿರೀಯ ಉಪನಿಷತ್ತಿನ ಶಂಕರ ಭಾಷ್ಯ', 'Śa. Bhā. Bra. Sū.': 'ಬ್ರಹ್ಮಸೂತ್ರದ ಶಂಕರ ಭಾಷ್ಯ', 'Īśa U.': 'ಈಶ ಉಪನಿಷತ್ತು', 'Ke. U.': 'ಕೇನ ಉಪನಿಷತ್ತು', 'Kā.': 'ಕಾತ್ಯಾಯನ ವಾರ್ತಿಕ', 'M.': 'ಮಹಾಭಾಷ್ಯ (ಪತಂಜಲಿ)', 'Sāṃ. Gṛ. Sū.': 'ಶಾಂಖ್ಯಾಯನ ಗೃಹ್ಯಸೂತ್ರ', 'Vāl.': 'ವಾಲಖಿಲ್ಯ ಸೂಕ್ತ', 'Anu.': 'ಅನುಕ್ರಮಣಿ (ಕಾತ್ಯಾಯನೀಯ ಸರ್ವಾನುಕ್ರಮಣಿ)', 'Dhā.': 'ಧಾತುಪಾಠ', 'Ṛgvi.': 'ಋಗ್ವಿಧಾನ', 'Piṅ.': 'ಪಿಂಗಲ ಛಂದಃಶಾಸ್ತ್ರ', 'Pā. Gṛ. Sū.': 'ಪಾರಸ್ಕರ ಗೃಹ್ಯಸೂತ್ರ', 'Pā. Sū. Vā.': 'ಪಾಣಿನಿ ಸೂತ್ರದ ವಾರ್ತಿಕ', 'Mu. U. Śa. Bhā.': 'ಮುಂಡಕ ಉಪನಿಷತ್ತಿನ ಶಂಕರ ಭಾಷ್ಯ'}
FIXKN = {'ಅಥ, ಸಂ.':'ಅಥ. ಸಂ.','ಆಪ. ಧ. ಸೂ':'ಆಪ. ಧ. ಸೂ.'}
out = []
for r in lst:
    if r['status'] not in ('legend', 'extra'): continue
    en = r['english']
    if en in MERGE: continue
    k = r['kannada']; note = ''
    if en in RENAME: en, k = RENAME[en]; note = 'more complete form of the print'
    src = 'edition legend' if r['status'] == 'legend' else ('given by the user in Kannada' if en in GIVEN else ('MY GUESS: to confirm' if en in GUESS else 'earlier list (not confirmed)'))
    t = three.get(r['english'], {})
    k = FIXKN.get(k, k)
    out.append(dict(en=en, kn=k, knfull=KNFULL.get(en, ''), dv=dev(en), work=r['work'].replace(' (the legend has U. Sū.)', ''), src=src, uses=(t.get('uses: English') or '0'), note=note))
merged = {a: b for a, b in MERGE.items()}
with open(os.path.join(ROOT, 'REFERENCES_FINAL.tsv'), 'w', encoding='utf8') as o:
    o.write('English (the one form)\tKannada\tDevanagari (made by script)\twork\tfull Kannada name (to check)\tKannada form comes from\tuses in the English text now\tnote\n')
    for x in out: o.write('\t'.join([x['en'], x['kn'], x['dv'], x['work'], x['knfull'], x['src'], x['uses'], x['note']]) + '\n')
md = ['# Final list of references: one work, one form (PROPOSAL, Nov 20 2026)', '', f'{len(out)} works. Made by `python3 tools/rv/refs_final.py` from `rv/references.tsv` with the decisions of Nov 19–20 applied.', '',
      'Merged (the left form disappears, every volume and script gets the right one): ' + '; '.join(f'{a} → {b}' for a, b in merged.items()) + '.', '',
      '| English | Kannada | Devanagari | Work | Full Kannada name | Kannada from |', '|---|---|---|---|---|---|'] + [f"| {x['en']} | {x['kn']} | {x['dv']} | {x['work']} | {x['knfull']} | {x['src']} |" for x in out]
open(os.path.join(ROOT, 'REFERENCES_FINAL.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
import collections; print(len(out), 'works', dict(collections.Counter(x['src'] for x in out)))
