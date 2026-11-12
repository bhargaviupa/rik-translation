#!/usr/bin/env python3
"""Convert a volume made with the older conventions (Vols 12, 14-16: translator remarks, [?], [sic], bold label lines, Kannada script in
the English text) to the Vol 17 conventions, by script, without re-translating.

  python3 tools/rv/to_note_style.py VOL            trial: writes volN/trial/English_converted.md, notes_trial.tsv, remarks_removed.tsv, report.md
                                                   (the volume files are not touched)

What the script does (in this order):
  1. remark paragraphs  *[ ... ]*  : running heads and pure process remarks (window ends, continued, moved, logged) are taken out;
     `*[Gist: ...]*` becomes the Gist; every other remark is taken out and leaves one `**NOTE**` with its text as the question;
  2. inline remarks  *[...]*, *(...)*, [...], (...)  that speak of the print ("as supplied", "so printed", "the supplied text has ..."):
     a bare tag is deleted; a reference followed by 'printed "..."' keeps the reference; anything else becomes `**NOTE**`;
  3. [?] and [sic] become `**NOTE**`;
  4. Kannada digits become Latin digits; label lines in their many spellings become the standard labels;
  5. layout of Vol 17: transliteration under the bhāṣya block removed, sub-headings, Pratipadārtha one word per line, Ṛk headings.
Nothing is lost: every removed remark is a row of remarks_removed.tsv (class 'dropped') or of notes_trial.tsv (class 'NOTE').
What a script cannot do is counted in report.md: Kannada-script words still in the text, remark-like phrases still in the text."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rvlib, batch
ROOT = rvlib.ROOT
KN = '[ಀ-೿]'
PRINTISH = r'as supplied|so supplied|so printed|printed so|as printed|supplied text|the print has|is printed|printed "|printed with|printed without|letters as supplied|kept as supplied'
PROCESS = re.compile(r'^(Running head|The window ends|This window ends|The Special Topics (are|is) continued|Continued (from|on)|.{0,60}continued from the previous (page|window)|Printed p\. \d+ ends here)', re.I)
DECISION = re.compile(r'garbl|missing|expected|slip|doubt|unclear|illegible|oddit|variant|differ|should|wrong|error|not certain|where the|reads |read |printed|supplied|stray|twice|no closing|without', re.I)
BARE = re.compile(r'^[\s,;:.—-]*((?:%s|not changed|kept|here|both|the|letters|is|are|and|,|;|\s)+)[\s,;:.—-]*$' % 'as supplied|so supplied|so printed|printed so|as printed', re.I)
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
LABELS = [  # (regex on the bold label text, standard label or None = keep as plain bold)
    (r'^(Printed English( translation)?( of the Ṛk)?|English [Tt]ranslation \((as )?printed\))\.?$', 'Printed English'),
    (r'^(Grammar|Vyākaraṇa-prakriyā|Grammar notes|Grammatical analysis)\b.*$', 'Grammar (Vyākaraṇa-prakriyā)'),
    (r'^Sāyaṇa-bhāṣya( \(continued\))?$', '॥ सायणभाष्यम् ॥'), (r'^Pada-pāṭha$', '॥ पदपाठः ॥'), (r'^Saṃhitā-pāṭha$', '॥ संहितापाठः ॥'),
    (r'^सायणभाष्यम्$', '॥ सायणभाष्यम् ॥'), (r'^पदपाठः$', '॥ पदपाठः ॥'), (r'^संहितापाठः$', '॥ संहितापाठः ॥'),
    (r'^Pratipadārtha$', 'प्रतिपदार्थ (Pratipadārtha)'), (r'^Bhāvārtha(, continued\.?)?$', 'भावार्थ (Bhāvārtha)'),
    (r'^Special Topics( \(continued\))?$', 'विशेषविषयगळु (Viśeṣaviṣayagaḷu)'),
]
def main():
    vol = int(sys.argv[1]); cfg = rvlib.Cfg(vol); src = open(cfg.en, encoding='utf8').read()
    m = re.search(r'\n---\n+\*\*Progress note:\*\*.*\Z', src, re.S); tail = m.group(0) if m else ''; body = src[:m.start()] if m else src
    notes = []; dropped = []; st = collections.Counter(); page = [None]
    def note(q, ctx): notes.append((page[0], re.sub(r'\s+', ' ', q).strip(), ctx[-60:].strip())); st['NOTE'] += 1; return '**NOTE**'
    def drop(q, why): dropped.append((page[0], why, re.sub(r'\s+', ' ', q).strip())); st['dropped: ' + why] += 1
    # ---- 2/3: inline remarks
    PAR = r'(?:[^()\[\]]|\((?:[^()]|\([^()]*\))*\))*?'
    def inline(l):
        def rep(mm):
            whole = mm.group(0); inner = re.sub(r'^\*?[\[(]|[\])]\*?$', '', whole)
            if not re.search(PRINTISH, inner, re.I) and not (re.search(KN, inner) and whole[0] in '*['): return whole
            if BARE.match(inner): drop(inner, 'bare tag'); return ''
            r = re.match(r'^((?:[A-ZĀṚŚ][\w.āīūṛṃḥṇṭḍśṣ]*\.? ?){1,4}\d[\d\-–.]*)[,;]?\s*(?:printed|as supplied|so printed).*$', inner)     # (Pā. Sū. 3-2-75, printed "…")
            if r and whole[0] == '(' : drop(inner, 'print form of a reference'); return '(' + r.group(1) + ')'
            return ' ' + note(inner, l[:mm.start()])
        l = re.sub(r'\*\[[^\]]*\]\*|\*\(' + PAR + r'\)\*|\[' + r'[^\[\]]*' + r'\]|\(' + PAR + r'\)', rep, l)
        l = re.sub(r'\s*\[sic\]', lambda mm: ' ' + note('[sic]: printed so', l[:mm.start()]), l)
        l = re.sub(r'\s*(?<!`)\[\?\](?!`)', lambda mm: ' ' + note('[?]: doubtful reading', l[:mm.start()]), l)
        l = re.sub(r',?\s*as supplied(?=[).,;])', lambda mm: (drop('as supplied', 'bare tag') or ''), l)
        return re.sub(r'  +', ' ', l).replace(' **NOTE** **NOTE**', ' **NOTE**').replace('( ', '(').replace(' )', ')').replace('()', '').rstrip() if l.strip() else l
    out = []
    for l in body.split('\n'):
        mm = re.match(r'### Printed p\. (\d+)', l)
        if mm: page[0] = int(mm.group(1))
        if l.startswith('> '): out.append(l); continue                       # Sanskrit blocks and their transliteration are never touched
        # ---- 1: remark paragraphs
        mm = re.match(r'\*\[(.*?)(?:\]\*(.*))?$', l)
        if l.startswith('*[') and mm:
            rem, rest = mm.group(1), (mm.group(2) or '').strip()
            g = re.match(r'Gist:\s*(.*)', rem)
            if g:
                gist = g.group(1); cut = re.search(r'\s*(The grammar tail|The grammatical tail|The grammar part)\b.*$', gist)
                extra = cut.group(0).strip() if cut else ''; gist = gist[:cut.start()] if cut else gist
                out.append('*Gist:* ' + inline(gist[0].upper() + gist[1:])); st['Gist'] += 1
                if extra: drop(extra, 'process remark')
            elif PROCESS.match(rem): drop(rem, 'running head' if rem.startswith('Running head') else 'process remark')
            elif DECISION.search(rem): out += [note(rem, out[-1] if out else ''), '']
            else: drop(rem, 'other remark')
            if rest: out.append(inline(rest))
            continue
        # ---- 4: labels
        mm = re.match(r'\*\*([^*]+?)\.?\*\*\s*(.*)$', l)
        if mm:
            name, rest = mm.group(1).strip(), mm.group(2).strip()
            for rx, std in LABELS:
                if re.match(rx, name):
                    out += ['**' + std + '**', '']; st['label normalised'] += name != std
                    if rest: out.append(inline(rest))
                    break
            else: out.append(inline(l))
            continue
        out.append(inline(l))
    t = '\n'.join(out)
    t = '\n'.join(l if l.startswith('> ') else re.sub(KN + '+', lambda mm: mm.group(0).translate(KD), l) for l in t.split('\n'))
    # ---- 5: layout
    L = t.split('\n'); o = []; i = 0; sec = None
    while i < len(L):                                                          # transliteration under the bhāṣya block goes
        l = L[i]
        if re.match(r'\*\*[^*]+\*\*\s*$', l): sec = l
        if sec == '**॥ सायणभाष्यम् ॥**' and l.startswith('> *') and l.rstrip().endswith('*'): st['bhāṣya IAST lines removed'] += 1; i += 1; continue
        if l.startswith('#'): sec = None
        o.append(l); i += 1
    t = '\n'.join(o)
    def pratipada(mm):                                                         # one word per line
        items = [x.strip() for x in re.split(r';\s+(?=\S+ \(\*)', mm.group(2)) if x.strip()]
        return mm.group(1) + '\n'.join('- ' + x.rstrip(';.') for x in items) if len(items) > 2 else mm.group(0)
    t = re.sub(r'(\*\*प्रतिपदार्थ \(Pratipadārtha\)\*\*\n\n)((?:(?!\*\*|#|>|\n).+)(?=\n))', pratipada, t)
    t = batch.subheads(t); t, ch = batch.rk_headings(t); st['Ṛk headings changed'] = len(ch)
    t = re.sub(r'(?m)^##### Printed English\s*$', '##### English translation (H. H. Wilson)', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    # ---- report
    d = os.path.join(ROOT, f'vol{vol}', 'trial'); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'English_converted.md'), 'w', encoding='utf8').write(t + tail)
    open(os.path.join(d, 'notes_trial.tsv'), 'w', encoding='utf8').write('printed page\tquestion\twords before the mark\n' + ''.join(f'{p}\t{q}\t{c}\n' for p, q, c in notes))
    open(os.path.join(d, 'remarks_removed.tsv'), 'w', encoding='utf8').write('printed page\tkind\ttext\n' + ''.join(f'{p}\t{k}\t{q}\n' for p, k, q in dropped))
    body_t = '\n'.join(l for l in t.split('\n') if not l.startswith('> '))
    left_kn = re.findall(KN + '+', body_t); left_rem = re.findall(r'(?i)as supplied|so printed|printed so|supplied text|\*\[|\[sic\]|\[\?\]|running head|this window|next window', body_t)
    pages = len(re.findall(r'(?m)^### Printed p\.', t)); knl = sum(1 for l in body_t.split('\n') if re.search(KN, l)); reml = sum(1 for l in body_t.split('\n') if re.search(r'(?i)as supplied|so printed|printed so|supplied text|\*\[|\[sic\]|\[\?\]|running head|this window|next window', l))
    rep = [f'# Vol {vol}: trial conversion to the Vol 17 conventions (script only)', '', f'Printed pages: {pages}. Source lines: {len(src.splitlines())}; converted lines: {len(t.splitlines())}.', '',
           '## Done by the script'] + [f'- {k}: {v}' for k, v in sorted(st.items())] + ['', f'`**NOTE**` marks in the converted text: {t.count("**NOTE**")} (rows in notes_trial.tsv: {len(notes)}); {t.count("**NOTE**") / max(1, pages):.1f} per page.',
           '', '## Left over (a script cannot settle these)', f'- Kannada-script words still in the English text: {len(left_kn)} on {knl} lines', f'- remark-like phrases still in the text: {len(left_rem)} on {reml} lines',
           f'- sections: {len(re.findall("(?m)^##### ॥ संहितापाठः ॥", t))} Saṃhitā, {len(re.findall("(?m)^#### Ṛk", t))} Ṛk headings, {len(re.findall("(?m)^##### Gist", t))} Gists, {len(re.findall("(?m)^## Sūkta", t))} sūkta headings']
    open(os.path.join(d, 'report.md'), 'w', encoding='utf8').write('\n'.join(rep) + '\n'); print('\n'.join(rep))
if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    main()
