#!/usr/bin/env python3
"""Reference abbreviations that the machine reading (and so the supplied text) systematically misreads — corrected by the USER's reading of the print (Nov 9 2026):

   ಸಿ.  (Si)              is  ನಿ.  = Nirukta (Ni.)
   ಮಿ. ಸಂ. / ಮ. ಸಂ. / ಪು. ಸಂ. / (ಋ ಸಂ.)   are  ಋ. ಸಂ. = Ṛgveda-saṃhitā (Ṛ. Saṃ.)
   ಇ. ಬ್ರಾ.  (I. Brā.)    is  ಐ. ಬ್ರಾ. = Aitareya Brāhmaṇa (Ai. Brā.)       (not in the user's list; the legend of abbreviations has only ಐ. ಬ್ರಾ.)
Only a token that stands directly before a reference number is touched; all other letters and numbers are left alone.

  python3 tools/rv/refs_fix.py N [--write]      report (and with --write fix) the Kannada and English files of volume N; log in volN/review/repair_log.md
  from refs_fix import fix_kn, fix_en           library use (html_to_kn.py applies fix_kn to every line it writes)
Not corrected, only reported (`--other`): other Kannada abbreviations before numbers that are not in the legend (e.g. ಭಾ. ಉ., ಕೃ. ಸಂ.) — decide with the scan."""
import re, sys, pathlib, datetime, collections
KN = 'ಀ-೿'
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
NUM = r'[೦-೯0-9]+(?:\s*[-–]\s*[೦-೯0-9]+)*'
RULES = [  # (regex of the TOKEN only, Kannada replacement, English replacement); the number after it is only looked at, never consumed
    (rf'(?<![{KN}])ಸಿ\.?(?=[ \t]*[೦-೯0-9])', 'ನಿ.', 'Ni.'),
    (rf'(?<![{KN}])(?:ಮಿ|ಮ|ಪು|ಋ)[.,]?[ \t]*ಸಂ\.?(?=[ \t]*[೦-೯0-9])', 'ಋ. ಸಂ.', 'Ṛ. Saṃ.'),
    (rf'(?<![{KN}])ಇ\.?[ \t]*ಬ್ರಾ\.?(?=[ \t]*[೦-೯0-9])', 'ಐ. ಬ್ರಾ.', 'Ai. Brā.'),
]
def fix_kn(t):
    for rx, kn, en in RULES: t = re.sub(rx, kn, t)
    return t
REFNUM = re.compile(r'(?<=\. )([೦-೯0-9]+(?:[ \t]*[-–][ \t]*[೦-೯0-9]+)*)')
def fix_en(t):
    """English file: token -> Latin abbreviation, and the Kannada digits of that reference -> Latin digits (same line only)"""
    for rx, kn, en in RULES:
        t = re.sub('(' + rx + r')([ \t]*)(' + NUM.replace(r'\s*', r'[ \t]*') + ')', lambda m: en + ' ' + m.group(3).translate(KD).replace(' ', '').replace('\t', '').replace('–', '-'), t)
    # the same misreads written in Latin letters by the translator (Ma./Mi./Pu. Saṃ., Si.)
    t = re.sub(r'(?<![A-Za-zāīūṛṃṭḍṇśṣḥ])(?:Ma|Pu|Mi)\. ?Saṃ\.(?= ?[0-9])', 'Ṛ. Saṃ.', t)
    t = re.sub(r'(?<![A-Za-zāīūṛṃṭḍṇśṣḥ])Si\.(?= ?[0-9])', 'Ni.', t)
    # remarks that only announced the misreading are obsolete once the abbreviation is corrected
    t = re.sub(r' ?\*\[as supplied: (?:ಮ|ಮಿ|ಪು)\. \((?:Ma|Mi|Pu)\.\) for ಋ\. \(Ṛ\.\)\]\*', '', t)
    R = r'(?:Ni|Ṛ\. Saṃ|Ai\. Brā)\. [0-9]+(?:-[0-9]+)*'
    t = re.sub(rf'\(cited as "({R})", as printed\)', r'(\1)', t)
    t = re.sub(rf'\(Reference as printed: ({R})\.?\)', r'(Reference: \1.)', t)
    t = re.sub(rf'\((?:Ni|Nir|Nighaṇṭu)\.? (?P<n>[0-9]+(?:-[0-9]+)*), (?:as )?printed(?: in the supplied text)?,? "Ni\. (?P=n)"\)', lambda m: f'(Ni. {m.group("n")})', t)
    t = re.sub(rf'\(({R}), (?:as printed(?: in the supplied text)?|printed),? "({R})"\)', lambda m: f'({m.group(1)})' if m.group(1) == m.group(2) else m.group(0), t)
    t = re.sub(rf'\((?:as )?printed ({R})(?:, i\.e\. (?:the Nirukta, )?({R}))?\)', lambda m: f'({m.group(1)})', t)
    t = re.sub(rf'\(printed ({R}), i\.e\. ', r'(\1, i.e. ', t)
    return t
if __name__ == '__main__':
    vol = int(sys.argv[1]); write = '--write' in sys.argv
    root = pathlib.Path(__file__).resolve().parents[2]
    files = {'kn': (root / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_Kannada_Text.md', fix_kn),
             'en': (root / f'vol{vol}' / f'Rigveda_Samhita_Vol{vol}_English_Translation.md', fix_en)}
    log = []
    for k, (f, fn) in files.items():
        t = f.read_text(encoding='utf8'); n = fn(t)
        changed = sum(1 for a, b in zip(t.split('\n'), n.split('\n')) if a != b)
        print(f'{k}: {changed} lines changed')
        log.append((k, changed))
        if write and changed: f.write_text(n, encoding='utf8')
    if write:
        with (root / f'vol{vol}' / 'review' / 'repair_log.md').open('a', encoding='utf8') as g:
            g.write(f'- {datetime.date.today()}: tools/rv/refs_fix.py (user\'s reading of the print): ಸಿ.→ನಿ. (Ni.), ಮಿ./ಮ./ಪು. ಸಂ.→ಋ. ಸಂ. (Ṛ. Saṃ.), ಇ. ಬ್ರಾ.→ಐ. ಬ್ರಾ. (Ai. Brā.) before reference numbers; lines changed: ' + ', '.join(f'{k} {n}' for k, n in log) + ' (English file: reference notes rewritten with Latin abbreviations and digits).\n')
