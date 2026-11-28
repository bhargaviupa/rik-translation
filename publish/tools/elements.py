#!/usr/bin/env python3
"""Content choice for the print build: leave named elements out of a volume's text, in memory only (Nov 27 2026; basis: docs/PDF_ELEMENTS.md).

  python3 publish/tools/elements.py FILE.md --lang kn|en [--without printed_en,grammar] [--out FILE]      dry run + report (writes only with --out)
  import: drop(md, lang, exclude) -> (md, report)

The reader knows the labels of the volumes by an alias table (ALIASES: one regex per element and language; family A `##### …` headings, family B bold-line labels,
the Kannada italic labels).  A section starts at a recognised label and ends at the next recognised label, at any other heading (`## Sūkta`, `#### Ṛk`, an unknown `#####`),
or, for the printed English only, at the first line that has Kannada/Devanagari letters (the printed English is Latin text; what follows is something else).
Never removed from inside a removed section: page markers (`<!-- printed N -->`, `### Printed p. N`) with the running head right after them, so page links and the contents keep working.
A remark line `*[...]*` that stands right before a label belongs to that label (a garbled-label note) and goes with it.
Elements: samhita, pada, bhashya, gist, pratipada, bhavartha, printed_en, special, grammar, anuvada, particulars.
The report counts sections and lines removed per element and lists sections that are suspiciously long (a missing label would make a section swallow its neighbour)."""
import re, sys, collections

ELEMENTS = ['samhita', 'pada', 'bhashya', 'gist', 'pratipada', 'bhavartha', 'printed_en', 'special', 'grammar', 'anuvada', 'particulars']
ALIASES = [      # (element, regex on the label text with #, *, ॥, parentheses' notes kept) -- first match wins
    ('gist',       r'^Gist of the bhāṣya'),
    ('samhita',    r'संहितापाठ|Saṃhitā-pāṭha|^ಸಂಹಿತಾಪಾಠಃ$'),
    ('pada',       r'पदपाठ|Pada-pāṭha|^ಪದಪಾಠಃ$'),
    ('bhashya',    r'सायणभाष्य|Sāyaṇa-bhāṣya|^ಸಾಯಣಭಾಷ್ಯಂ$'),
    ('pratipada',  r'प्रतिपदार्थ|Prati-?padārtha|^ಪ್ರತಿಪದಾರ್ಥ$'),
    ('bhavartha',  r'भावार्थ|Bhāvārtha|^ಭಾವಾರ್ಥ$'),
    ('printed_en', r'^(Embedded )?English [Tt]ranslation|^Printed English|^English Translation\.$'),
    ('special',    r'विशेषविषय|Special Topics|Viśeṣa-?viṣaya|^ವಿಶೇಷವಿಷಯಗಳು$'),
    ('grammar',    r'^Grammar|Vyākaraṇa|^ವ್ಯಾಕರಣಪ್ರಕ್ರಿಯಾ$'),
    ('anuvada',    r'^Anuvāda'),
    ('particulars', r'^Particulars'),
]
KN_LABEL = re.compile(r'^\*([^*\[\]]{3,40})\*$')                       # '*ಪದಪಾಠಃ*'
EN_HEAD = re.compile(r'^#{4,6}\s+(.*)$')                                # '##### English translation'
EN_BOLD = re.compile(r'^\*\*([^*].{1,100}[^*])\*\*(\s+\*\(.*\)\*)?$')  # '**॥ पदपाठः ॥**', '**Pada-pāṭha** *(p. 5)*'
MARK = re.compile(r'^(<!-- printed \d+(?::[^>]*)? -->|### Printed p\. \d+.*)$')
HEADLINE = re.compile(r'^\*(\[|\(|Running head|Header)')                 # head/remark line (kn: *[…]*; en: *Running head…*, *(Header…)*)
BOUNDARY = re.compile(r'^(#{1,3} |#### |---\s*$)')
LONG = 150          # sections longer than this (lines) are listed in the report
INDIC = re.compile(r'[ऀ-ॿಀ-೿]')

def element_of(label):
    t = re.sub(r'^[#\s*॥।]+|[\s*॥।]+$', '', label).strip()
    for e, rx in ALIASES:
        if re.search(rx, t): return e
    return None

def classify(l, lang):
    """-> ('label', element) | ('head', None) for an unknown heading | None"""
    s = l.strip()
    if lang == 'kn':
        m = KN_LABEL.match(s)
        if m:
            e = element_of(m.group(1))
            if e: return ('label', e)
        return None
    m = EN_HEAD.match(s)
    if m and not MARK.match(s):
        if s.startswith('#### Ṛk') or s.startswith('#### Rik') : return ('head', None)
        e = element_of(m.group(1)); return ('label', e) if e else ('head', None)
    m = EN_BOLD.match(s)
    if m:
        e = element_of(m.group(1))
        if e: return ('label', e)
    return None

def drop(md, lang, exclude):
    exclude = set(exclude); bad = exclude - set(ELEMENTS)
    if bad: raise SystemExit(f'unknown element(s): {sorted(bad)}; known: {ELEMENTS}')
    lines = md.split('\n'); out = []; cur = None; pend = []; after_mark = False
    rep = {e: {'sections': 0, 'lines': 0, 'longest': 0, 'ended_by_script': 0} for e in ELEMENTS}; size = 0; where = []; start = 0; long_ = []
    def close():
        nonlocal size
        if cur in exclude and size > rep[cur]['longest']: rep[cur]['longest'] = size
        if cur in exclude and size > LONG: long_.append((cur, start, size))
        size = 0
    def emit(l):
        nonlocal size
        if cur in exclude:
            rep[cur]['lines'] += 1 if l.strip() else 0; size += 1
        else: out.append(l)
    def blank():
        if out and out[-1].strip(): out.append('')
    def flush():
        for p in pend: emit(p)
        pend.clear()
    for n, l in enumerate(lines):
        s = l.strip()
        if MARK.match(s):                                   # a page marker is always kept
            flush(); blank(); out.append(l); after_mark = True; continue
        if after_mark and (HEADLINE.match(s) or not s):    # the running head right after a marker is kept
            out.append(l)
            if s: after_mark = False; out.append('')
            continue
        after_mark = False
        c = classify(l, lang)
        if lang == 'kn' and not c and HEADLINE.match(s) and s.startswith('*['):   # a garbled-label note: goes with the label that follows
            pend.append(l); continue
        if not s and pend: pend.append(l); continue
        if c and c[0] == 'label':
            close(); cur = c[1]; rep[cur]['sections'] += 1; start = n + 1
            if cur in exclude: where.append((cur, n + 1))
            flush()
            if cur not in exclude: blank()
            emit(l); continue
        if (c and c[0] == 'head') or BOUNDARY.match(s):
            flush(); close(); cur = None; blank(); out.append(l); continue
        if cur == 'printed_en' and cur in exclude and s and INDIC.search(s) and not s.startswith('*['):
            flush(); close(); rep['printed_en']['ended_by_script'] += 1; cur = None; blank(); out.append(l); continue
        flush(); emit(l)
    flush(); close()
    text = re.sub(r'\n{3,}', '\n\n', '\n'.join(out))
    rep = {k: v for k, v in rep.items() if k in exclude}; rep['_long'] = long_
    return text, rep

def report(rep):
    for e, r in [(k, v) for k, v in rep.items() if k != '_long']:
        print(f'  {e:11} sections {r["sections"]:5}  lines removed {r["lines"]:6}  longest section {r["longest"]:4} lines  ended by script rule {r["ended_by_script"]}')
    for e, st, n in rep.get('_long', [])[:12]: print(f'  LONG {e}: {n} lines from line {st} — look at it before trusting the removal (essay, or a missing label?)')
    if len(rep.get('_long', [])) > 12: print(f'  … and {len(rep["_long"]) - 12} more long sections')

if __name__ == '__main__':
    a = sys.argv[1:]; f = a[0]; lang = a[a.index('--lang') + 1]
    ex = [x for x in (a[a.index('--without') + 1].split(',') if '--without' in a else []) if x]
    md = open(f, encoding='utf8').read(); t, rep = drop(md, lang, ex)
    print(f'{f}: {len(md.splitlines())} -> {len(t.splitlines())} lines'); report(rep)
    if '--out' in a: open(a[a.index('--out') + 1], 'w', encoding='utf8').write(t)
