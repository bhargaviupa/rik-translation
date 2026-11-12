#!/usr/bin/env python3
"""Convert a volume made with the older conventions (Vols 12, 14-16: translator remarks, [?], [sic], bold label lines, Kannada script in
the English text) to the Vol 17 conventions, by script, without re-translating.

  python3 tools/rv/to_note_style.py VOL --easy [--write]   the safe subset only (running heads, bare tags, process remarks out; Gists; [?] -> NOTE; layout):
                                                   informative remarks and [sic] stay.  --write applies it to the volume file (logged repair).
  python3 tools/rv/to_note_style.py VOL --drop-phrase [--write]   remove every translator comment that contains "as supplied"
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
def drop_phrase(vol, write, phrase='as supplied'):
    """Remove every translator comment that contains PHRASE (user, Nov 12 2026: 'remove all comments that have "as supplied"').
    A comment = a remark paragraph *[...]*, an inline *[...]* or *(...)*, a [...] bracket, or a plain (...) that speaks of the print.
    A plain parenthesis that is a reference or a citation keeps its content and loses only the tag; the phrase alone in running prose is cut.
    Sanskrit block lines ('> ') are never touched.  Everything removed goes to review/remarks_removed.tsv."""
    cfg = rvlib.Cfg(vol); src = open(cfg.en, encoding='utf8').read(); st = collections.Counter(); rows = []; page = [None]
    PH = re.compile(re.escape(phrase), re.I); TAG = re.compile(r'\s*[,;:—-]?\s*(?:kept |left |both kept |letters )?' + re.escape(phrase) + r'(?:, not changed| \(not corrected\))?', re.I)
    ABOUT = re.compile(r'print|supplied text|the supplied|garbl|stray|hyphen|line end|line break|label|spelling|spelt|slip|' + KN, re.I)
    PAR = r'(?:[^()]|\((?:[^()]|\([^()]*\))*\))*?'
    def log(kind, t): rows.append((page[0], kind, re.sub(r'\s+', ' ', t).strip())); st[kind] += 1
    def fix(l):
        def rep(mm):
            w = mm.group(0)
            if not PH.search(w) or '**NOTE**' in w or '[?]' in w: return w                      # a comment that carries a doubt mark stays
            if w[0] == '*' or w[0] == '[': log('comment with "%s"' % phrase, w); return ''
            inner = w[1:-1]; rest = TAG.sub('', inner).strip(' ,;')
            if not rest: log('bare tag', w); return ''
            if re.match(r'(printed\b|the print\b|the supplied\b|supplied text\b|so printed|printed so|sic\b|the (first |second |last )?(word|label|reference|abbreviation|text|letters?) .{0,80}\b(is|are) (printed|quoted|kept|given)\b|["“]?' + KN + r'+["”]?[.,; ]*$)', rest, re.I): log('comment with "%s"' % phrase, w); return ''
            log('tag cut, content kept', w); return '(' + rest + ')'
        l2 = re.sub(r'\*\[(?:[^\[\]]|\[[^\[\]]*\])*\]\*|\*\(' + PAR + r'\)\*|\[[^\[\]]*\]|\(' + PAR + r'\)', rep, l)
        l2 = re.sub(r'[;,]\s*[^;,()\[\]]{0,70}\b(?:is|are|all|both|kept|left)\s+' + re.escape(phrase) + r'(?=[;,.)\]]|$)', lambda mm: (log('clause cut', mm.group(0)) or ''), l2)
        if PH.search(l2) and '**NOTE**' not in l2 and '[?]' not in l2: l2 = TAG.sub(lambda mm: (log('tag cut in prose', l2[max(0, mm.start() - 50):mm.end()]) or ''), l2)
        return re.sub(r'  +', ' ', l2).replace(' .', '.').replace(' ,', ',').replace('( ', '(').replace(' ()', '').replace('()', '').rstrip() if l2 != l else l
    out = []
    for l in src.split('\n'):
        mm = re.match(r'### Printed p\. (\d+)', l)
        if mm: page[0] = int(mm.group(1))
        if l.startswith('> ') or l.startswith('#') or '**Progress note:**' in l: out.append(l); continue
        if l.startswith('*[') and PH.search(l):
            mm = re.match(r'(\*\[.*\]\*)\s*$', l) or re.match(r'(\*\[.*?\]\*)(.*)$', l)        # the whole line is one remark (it may hold [..] inside), or a remark followed by text
            if '**NOTE**' in l or '[?]' in l: out.append(l); st['kept: carries a doubt mark'] += 1; continue
            if mm and mm.lastindex == 1: log('remark paragraph with "%s"' % phrase, mm.group(1)); continue
            if mm and PH.search(mm.group(1)):
                log('remark paragraph with "%s"' % phrase, mm.group(1)); rest = fix(mm.group(2).strip())
                if rest: out.append(rest)
                continue
            if not mm: log('remark paragraph with "%s"' % phrase, l); continue
        n = fix(l)
        if n.strip() or not l.strip(): out.append(n)
    t = re.sub(r'\n{3,}', '\n\n', '\n'.join(out))
    print(f'Vol {vol}: "{phrase}" before {len(PH.findall(src))}, after {len(PH.findall(t))};', dict(st))
    left = [l for l in t.split('\n') if PH.search(l) and not l.startswith('> ')]
    for l in left[:8]: i = PH.search(l).start(); print('   left:', l[max(0, i - 70):i + 30])
    if write:
        open(cfg.en, 'w', encoding='utf8').write(t); rv = os.path.join(ROOT, f'vol{vol}', 'review'); f = os.path.join(rv, 'remarks_removed.tsv')
        if not os.path.exists(f): open(f, 'w', encoding='utf8').write('printed page\tkind\ttext\n')
        open(f, 'a', encoding='utf8').write(''.join(f'{p}\t{k}\t{q}\n' for p, k, q in rows))
        open(os.path.join(rv, 'repair_log.md'), 'a', encoding='utf8').write(f'- comments containing "{phrase}" removed (`tools/rv/to_note_style.py {vol} --drop-phrase --write`; user decision Nov 12 2026): ' + '; '.join(f'{k} {v}' for k, v in sorted(st.items())) + '. All listed in review/remarks_removed.tsv. Sanskrit block lines and the translation wording are unchanged.\n')
    return t

def main():
    easy = '--easy' in sys.argv; write = '--write' in sys.argv
    if '--drop-phrase' in sys.argv: return drop_phrase(int(sys.argv[1]), write)
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
            if easy: st['remark kept'] += 1; return whole
            return ' ' + note(inner, l[:mm.start()])
        l = re.sub(r'\*\[[^\]]*\]\*|\*\(' + PAR + r'\)\*|\[' + r'[^\[\]]*' + r'\]|\(' + PAR + r'\)', rep, l)
        if not easy: l = re.sub(r'\s*\[sic\]', lambda mm: ' ' + note('[sic]: printed so', l[:mm.start()]), l)
        l = re.sub(r'\s*(?<!`)\[\?\](?!`)', lambda mm: ' ' + note('[?]: doubtful reading', l[:mm.start()]), l)
        if not easy: l = re.sub(r',?\s*as supplied(?=[).,;])', lambda mm: (drop('as supplied', 'bare tag') or ''), l)
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
            elif easy: out.append(l); st['remark kept'] += 1; continue
            elif DECISION.search(rem): out += [note(rem, out[-1] if out else ''), '']
            else: drop(rem, 'other remark')
            if rest: out.append(inline(rest))
            continue
        g = re.match(r'\*\(?Gist(?: \((?:Sāyaṇa|mine)\))?:\*?\s*(.*)$', l)                # '*Gist (Sāyaṇa):* …', '*Gist (mine): ….* …', '*(Gist: "…")*'
        if g:
            x = g.group(1); mm2 = re.match(r'(.*?[.!?"”])\)?\*(\s+.*)?$', x) if not l.startswith('*Gist (Sāyaṇa):*') and not l.startswith('*Gist:*') else None
            gist, rest = (mm2.group(1), (mm2.group(2) or '').strip()) if mm2 else (x, '')
            out.append('*Gist:* ' + inline(gist.strip('"“”'))); st['Gist'] += 1
            if rest: out += ['', inline(rest)]
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
    t = '\n'.join(l if l.startswith('> ') or re.search('[ಀ-೥೰-೿]', l) else l.translate(KD) for l in t.split('\n'))
    # ---- 5: layout
    L = t.split('\n'); o = []; i = 0; sec = None
    while i < len(L):                                                          # transliteration under the bhāṣya block goes
        l = L[i]
        if re.match(r'\*\*[^*]+\*\*\s*$', l): sec = l
        if sec == '**॥ सायणभाष्यम् ॥**' and l.startswith('> *') and l.rstrip().endswith('*'): st['bhāṣya IAST lines removed'] += 1; i += 1; continue
        if l.startswith('#'): sec = None
        o.append(l); i += 1
    t = '\n'.join(o)
    L = t.split('\n'); o = []; i = 0                                           # a Gist written between the bhāṣya label and its block goes after the block
    while i < len(L):
        o.append(L[i])
        if L[i] == '**॥ सायणभाष्यम् ॥**':
            j = i + 1; held = []
            while j < len(L) and not L[j].startswith(('> ', '#', '**')): held.append(L[j]); j += 1
            if j < len(L) and L[j].startswith('> ') and any(h.startswith('*Gist:*') for h in held):
                k = j
                while k < len(L) and (L[k].startswith('> ')): k += 1
                o += [''] + L[j:k] + [''] + [h for h in held] ; st['Gist moved after its block'] += 1; i = k; continue
        i += 1
    t = '\n'.join(o)
    t = re.sub(r'(?m)^\*Gist:\* ([a-z])', lambda mm: '*Gist:* ' + mm.group(1).upper(), t)
    def pratipada(mm):                                                         # one word per line
        items = [x.strip() for x in re.split(r';\s+(?=\S+ \(\*)', mm.group(2)) if x.strip()]
        return mm.group(1) + '\n'.join('- ' + x.rstrip(';.') for x in items) if len(items) > 2 else mm.group(0)
    t = re.sub(r'(\*\*प्रतिपदार्थ \(Pratipadārtha\)\*\*\n\n)((?:(?!\*\*|#|>|\n).+)(?=\n))', pratipada, t)
    t = batch.subheads(t); t, ch = batch.rk_headings(t); st['Ṛk headings changed'] = len(ch)
    t = re.sub(r'(?m)^##### Printed English\s*$', '##### English translation (H. H. Wilson)', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    # ---- report
    d = os.path.join(ROOT, f'vol{vol}', 'trial_easy' if easy else 'trial'); os.makedirs(d, exist_ok=True)
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
    if easy and write:                                                        # apply to the volume: a logged repair; the removed remarks and the NOTE questions go to review/
        import shutil, json
        rv = os.path.join(ROOT, f'vol{vol}', 'review'); os.makedirs(rv, exist_ok=True)
        open(cfg.en, 'w', encoding='utf8').write(t + tail)
        shutil.copy(os.path.join(d, 'remarks_removed.tsv'), os.path.join(rv, 'remarks_removed.tsv'))
        nf = os.path.join(rv, 'notes.tsv')
        if notes: open(nf, 'w', encoding='utf8').write('window\tprinted page\tquestion (what needs a decision or a second look)\twords before the mark in the English text\tdecision\n' + ''.join(f'conversion\t{p}\t{q}\t{c}\t\n' for p, q, c in notes))
        cp = rvlib.cfg_path(vol); c = json.load(open(cp, encoding='utf8')); c.update({'layout': 'subheads', 'no_iast_blocks': ['bhashya'], 'printed_english_label': 'English translation (H. H. Wilson)'})
        open(cp, 'w', encoding='utf8').write(json.dumps(c, indent=1, ensure_ascii=False) + '\n')
        open(os.path.join(rv, 'repair_log.md' if os.path.exists(os.path.join(rv, 'repair_log.md')) else 'repair_log.md'), 'a', encoding='utf8').write(f"\n- layout conversion (`tools/rv/to_note_style.py {vol} --easy --write`): " + '; '.join(f'{k} {v}' for k, v in sorted(st.items())) + ". Removed remarks are listed in review/remarks_removed.tsv; informative remarks, [sic] and the wording of the translation are unchanged; Sanskrit blocks unchanged except that the transliteration under the bhāṣya block is taken out.\n")
        print('written to the volume file; volcfg: layout subheads')
if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    main()
