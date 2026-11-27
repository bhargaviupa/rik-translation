#!/usr/bin/env python3
"""Remove the translator's remarks from a legacy volume's English file, one KIND at a time (Vol 2 clean-up, user, Nov 17 2026).

  python3 tools/rv/cleanup_remarks.py VOL KIND [--write] [--file NAME.md]     (--file: another English file of the volume, e.g. Vol 1's Gaps file)

KINDs: oldnotes   old mid-file progress/target notes and the closing progress notes (-> one trailing progress note)
       notes      whole-line italic notes *( ... )* in which EVERY sentence is a process remark (mixed notes stay; listed in review/notes_kept.tsv)
       paren      (Vol 1, Nov 25 2026) inside any parenthesis ( … ), *( … )* or bracket [ … ]: the clauses that are only a process remark
                  ("re-read from the better scan in the [?] pass", "as printed", "gloss mine and tentative", "best-effort reading" …) go;
                  clauses that carry content (a quotation, a reference number, Sanskrit, a figure, a `[?]`) stay; an emptied parenthesis goes whole.
                  Unlike the other kinds it also works at the end of Sanskrit lines (the parenthesis itself must be free of Devanagari).
       session    whole paragraphs in which the translating session talks (Progress, Target for next session, Pacing/Honesty/Confidence notes,
                  Caveats, flag lists "- p. N — …", Superseded notes)
       twin       (Vol 1) a Sanskrit quotation given twice in Devanagari: as printed, then again with the words set apart, then the
                  transliteration.  The second Devanagari line goes (user, Nov 25 2026: "retain only the first lines"); only where the two lines
                  are the same text (letters compared through the transliteration, >= 93 of 100) and the transliteration follows.
       all        the kinds every volume gets before a PDF is built (REQUIREMENTS B4.6, B2.6): session, paren, ownnote, twin, leaders, in that order, on
                  EVERY English file of the volume; then `marks`.  Dry run: one line of counts per file and kind.  --write: applies, logs each
                  removal in review/removed_remarks.tsv and one line in review/repair_log.md.  Afterwards rebuild the PDF and compare its
                  chapter/sūkta count with the build before (a removed note may be a marker the builder needs: Vol 1, LESSONS).
       ownnote    whole-line notes of ours, *( … )* or *[ … ]* (and plain italic lines that name the PDF or the file), that speak about the making:
                  the page, the scan, the print, the source, what was transcribed, rendered, omitted or continues (user, Nov 26 2026: "we said
                  we remove own comments").  Notes of at most 450 characters only; a note without such words (a summary of the Sanskrit,
                  a gloss) stays, and so does a long one: both are listed by `marks`-style review, not removed.
       leaders    rows of dots typed before a page number ('title ........ p. 4') become ' — p. 4'
       marks      no change: writes volN/review/open_readings.tsv, every `[?]` and `[sic]` left in the file (file, page, line, mark, context)
Dry run by default: prints counts, damage checks and 30 before/after samples.  --write applies, appends to volN/review/removed_remarks.tsv
(kind, page, line, text removed, line before, line after) so that any removal can be undone, and prints the damage report.
Never touches lines with Devanagari/Kannada, `[?]`, `[sic]` (user decision); whole remarks only, never half a sentence."""
import os, re, sys, random
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ABBR = re.compile(r'(?:^|[\s(*"“])(?:[^\W\d]{1,3}|Ṛ|Pā|Nir|Saṃ|Brā|Ai|Sū|Ni|cf|Dr|Śrī)$')
def sentences(s):
    out = []; cur = 0
    for m in re.finditer(r'\.["”)\]*]*\s+(?=["“(\[*]?[A-ZĀŚṚṢ])', s):
        if ABBR.search(s[cur:m.start()]): continue
        out.append(s[cur:m.end()]); cur = m.end()
    out.append(s[cur:]); return [x.strip() for x in out if x.strip()]
# A clause is a process remark only in these exact forms (user, Nov 17 2026: remove process remarks, keep notes that carry content).
CLAUSE = [re.compile(x, re.I) for x in (
    r'^Page headers?\b.*$',
    r'^Saṃhitā accents as printed$', r'^Pada unaccented(\s*[—-].*)?$', r'^Saṃhitā accents as printed; Pada unaccented.*$',
    r'^English( words| text)? as printed$', r'^(Kannada prose translated|grammar characterized|Grammar characterized|characterized)$',
    r'^(Grammar )?characterized,? sūtras kept$', r'^sūtras kept$',
    r'^.{0,110}\bre-?read from the better scan.{0,60}$', r'^.{0,60}\bfrom the better scan.{0,60}$',
    r'^.{0,160}\(Oct 2026 numeral pass.{0,60}\)$', r'^.{0,160}\bnumeral pass\b.{0,40}$',
    r'^[^"“]{0,90}\bas printed$', r'^Characterized\b[^.]{0,40}$', r'^Pp?\. [\d–-]+$', r'^Page headers? p\. \d+.*$',
    r'^(The )?glosses? [^"“]{0,60}\b(mine|my own)\b[^"“]{0,40}\btentative\b[^"“]{0,80}$',
    r'^(The )?glosses? (on the verses |on the parallel verse )?(are |is )?(mine|of my own)[,;]? (and )?tentative.{0,60}$', r'^(The )?glosses? (on the verses |on the parallel verse )?(are |is )?mine$',
    r'^Printed references (on this page|at the head|in the grammar).*$',
)]
def process_sentence(s):
    s = s.strip().rstrip('.').strip()
    return bool(s) and all(any(c.match(cl.strip()) for c in CLAUSE) for cl in re.split(r';\s*', s) if cl.strip())
KEEPNOTE = re.compile(r':\s*$')            # lead-in to a list: stays
NOTE = re.compile(r'(\s*>?\s*)\*\((.*)\)\*\s*$')
def load(vol):
    name = sys.argv[sys.argv.index('--file') + 1] if '--file' in sys.argv else f'Rigveda_Samhita_Vol{vol}_English_Translation.md'
    p = os.path.join(ROOT, f'vol{vol}', name)
    return p, open(p, encoding='utf8').read().split('\n')
def pages(L):
    pg = 0; out = []
    for l in L:
        m = re.match(r'#{2,4} (?:Printed )?(?:Pages?|pp?\.) ?(\d+)', l)
        if m: pg = int(m.group(1))
        out.append(pg)
    return out
def is_process_note(l):
    m = NOTE.fullmatch(l)
    if not m or re.search('[ऀ-ॿಀ-೿]', l) or '[?]' in l or '[sic]' in l or '**' in m.group(2): return False
    body = m.group(2)
    if KEEPNOTE.search(body) or '*(' in body or ')*' in body: return False
    ss = sentences(body)
    return bool(ss) and all(process_sentence(x) for x in ss)
def kind_notes(L):
    return {i: None for i, l in enumerate(L) if is_process_note(l)}
def kind_oldnotes(L):
    rm = {}
    for i, l in enumerate(L):
        if re.match(r'\*\*(Progress: Through|Target for next session)', l): rm[i] = None
    n = len(L)
    # closing block: from "*(The scan ends here" to end
    for i, l in enumerate(L):
        if l.startswith('*(The scan ends here'):
            for j in range(i, n):
                if L[j].strip(): rm[j] = None
            rm[n - 1] = None
            rm['last'] = '**Progress note:** Done through printed p. 808'
            break
    return rm
def kind_clauses(L):
    # mixed notes: take out whole sentences of exact process forms, keep the rest of the note
    rm = {}
    for i, l in enumerate(L):
        m = NOTE.fullmatch(l)
        if not m or is_process_note(l) or re.search('[\u0900-\u097f\u0c80-\u0cff]', l) or '[?]' in l or '[sic]' in l or '*(' in m.group(2): continue
        body = m.group(2)
        if KEEPNOTE.search(body) or '**' in body or ')*' in body: continue
        ss = sentences(body)
        keep = [x for x in ss if not process_sentence(x)]
        if keep and len(keep) < len(ss):
            nb = ' '.join(keep)
            rm[i] = m.group(1) + '*(' + nb + ')*'
    return rm
TENT = [
    (re.compile(r'\bGloss \(mine[;,] tentative(?:; [^)]*)?\):'), 'Gloss:'),
    (re.compile(r'\s*\[tentative(?:;[^\]]*)?\]'), ''),                       # Gloss: "…" [tentative; …]
    (re.compile(r'(?<=[\"”])\s*[—:-]\s*mine and tentative\.?(?=\)\*?$|\)\*?\s)'), ''), # ("…" — mine and tentative.)  ("…": mine and tentative.)
    (re.compile(r'(?<=\()gloss mine and tentative: '), ''),                  # *(gloss mine and tentative: "…")*
    (re.compile(r'(?<=\*\()gloss mine and tentative: '), ''),
]
def sub_tent(l):
    n = l
    for rx, rep in TENT: n = rx.sub(rep, n)
    return n
def kind_tentative(L):
    rm = {}
    for i, l in enumerate(L):
        if 'tentative' not in l: continue
        n = sub_tent(l)
        if n != l: rm[i] = n
    return rm
def kind_asprinted(L):
    rm = {}
    for i, l in enumerate(L):
        if '[as printed]' in l: rm[i] = re.sub(r'\s?\[as printed\]', '', l)
    return rm
FP = re.compile(r"\b(I|my|mine|me|myself)\b|\bof my own\b")
REMARKW = re.compile(r'print|read|reading|scan|flag|reference|digit|spelling|transcrib|attempt|render|sure|unclear|hard|doubt|guess|tentative|note|correct|marks?\b|confiden|illegible|not (give|translate)', re.I)
def fp_remark(sent):
    out = re.sub(r'"[^"]*"|“[^”]*”|\*[^*]*\*', '', sent)       # words inside quotations / italics are the text's, not ours
    return bool(FP.search(out)) and bool(REMARKW.search(out))
def kind_firstperson(L):
    rm = {}
    for i, l in enumerate(L):
        m = NOTE.fullmatch(l)
        if not m or 'tentative' in l: continue
        body = m.group(2)
        if '*(' in body or ')*' in body or '**' in body: continue
        ss = sentences(body)
        keep = [x for x in ss if not fp_remark(x)]
        if len(keep) == len(ss): continue
        rm[i] = None if not keep else m.group(1) + '*(' + ' '.join(keep) + ')*'
    return rm
ASP = re.compile(r'\s?\[[^\[\]\n]{0,220}?as printed[^\[\]\n]{0,220}?\]')
def kind_asprinted2(L):
    rm = {}
    for i, l in enumerate(L):
        if 'as printed' not in l: continue
        n = ASP.sub(lambda m: m.group(0) if re.search('[\u0900-\u097f*]|sic|^\\s?\\[\\?', m.group(0)) else '', l)
        if n != l: rm[i] = n
    return rm
# ---- kind paren: process clauses inside parentheses and brackets
PROC = re.compile(r're-?(read|rendered|checked|transcribed|verified)\b|better scan|600 dpi|numeral pass|\[\?\] pass|\bas printed\b|\bas legible\b|'
                  r'\btentative\b|\bgloss(es)? (is |are )?(mine|my own)\b|\b(translation|rendering|sense)( of [a-z ]{0,30})? (is )?(mine|editorial)\b|best-effort|lower-confidence|'
                  r'\bmisreading\b|\bearlier (text|rendering|heading|reading)\b|\btranscribed (from|as|letter)|\bSuperseded\b|\bread by me\b|\bnot corrected\b', re.I)
CONTENT = re.compile(r'["“”‘’*=:]|[\u0900-\u097f\u0c80-\u0cff]|\d+-\d+|\[\?\]|\[sic\]')
HARD = re.compile(r'\bmisreading\b|\bearlier (text|rendering|heading|reading)\b|\bread by me\b|\bwith the user\b|\b(was|were) missing\b|^Missing before\b|\bmatch(es)? the print\b|'
                  r'\bas the print reads\b|\buser\'s reading\b|^Caveat\b|\bthis project\b|\bresidual uncertainty\b|\bcompleted by me\b|\bI see\b|\bThe user typed\b|'
                  r'\bordinary resolution\b|footnote block appears\b', re.I)      # ours whatever else the clause holds
MASK = [('[?] pass', '\x01'), ('[?]', '\x02'), ('[sic]', '\x03'), ('(?)', '\x04')]
def mask(t):
    for a, b in MASK: t = t.replace(a, b)
    return t
def unmask(t):
    for a, b in MASK: t = t.replace(b, a)
    return t
GROUP = re.compile(r'(\s?)(\*?)([(\[])([^()\[\]\n]{1,900})([)\]])(\*?)')        # innermost groups only ([?], [sic], (?) are masked first)
def proc_clause(c):
    c = unmask(c).strip()
    if not c or len(c) > 260: return False
    if HARD.search(c): return True
    if not PROC.search(c) or CONTENT.search(c.replace('[?] pass', 'pass')): return False
    weak = re.sub(r'\bas (printed|legible)\b', '', c, flags=re.I)                 # 'as printed' alone marks a remark only in a short clause
    return bool(PROC.search(weak)) or len(c) <= 60
def clean_group(inner):
    """inner text of a parenthesis -> (new inner or '' when nothing is left, changed?)"""
    u = unmask(inner)
    if re.search('[ऀ-ॿಀ-೿]', u) or not (PROC.search(u) or HARD.search(u)): return inner, False
    keep_s = []; changed = False
    for snt in sentences(u):
        end = re.search(r'[.!?]["”)\]*]*\s*$', snt); body = snt[:end.start()] if end else snt
        cl = re.split(r';\s+', body); keep = [c for c in cl if not proc_clause(c)]
        if len(keep) < len(cl): changed = True
        if keep:
            t = '; '.join(keep)
            if len(keep) < len(cl) and t[:1].islower() and body[:1].isupper(): t = t[:1].upper() + t[1:]
            keep_s.append(t + (snt[end.start():].rstrip() if end else ''))
    return mask(' '.join(keep_s)), changed
def sub_paren(l):
    def rep(m):
        sp, a1, o, inner, c, a2 = m.groups()
        if (o == '(') != (c == ')') or bool(a1) != bool(a2): return m.group(0)
        new, ch = clean_group(inner)
        if not ch: return m.group(0)
        if not new.strip(): return ''
        return sp + a1 + o + new + c + a2
    t = mask(l)
    for _ in range(3):
        n = GROUP.sub(rep, t)
        if n == t: break
        t = n
    return unmask(t)
def kind_paren(L):
    rm = {}
    for i, l in enumerate(L):
        if l.startswith('#') or not (PROC.search(l) or HARD.search(l)): continue
        n = sub_paren(re.sub(r',\s+as printed(?=\s*[;)\]])', '', l))             # '(Jai. Sū. 2-1-8, as printed)' -> '(Jai. Sū. 2-1-8)'
        if n == l: continue
        n = re.sub(r'\s+$', '', n)
        rm[i] = None if not n.strip() or n.strip() in ('>', '> *', '**') else n
    return rm
# (the notes '⚠ Note on a deliberate skip' / 'alphabetical rishi-index' of Vol 1 stay: publish/vol1_clean.py puts the Gaps translation in their place)
# ---- kind session: whole paragraphs that are the translating session talking (progress, targets, pacing/honesty/confidence notes, flag lists)
SESSION_LABEL = re.compile(r'^(?:>\s*)?\*\*(?:[⚠🎉] ?)?(Progress\b|MILESTONE|Known issues|Note on a source scanning|Target (for next session|reached)|Pacing note|Honesty notes?|Confidence notes?|Caveats?:|This batch (established|completed)|'
                           r'Also completed this batch|The genuine highlight of this batch|IMPORTANT STRUCTURAL FLAG|Structural note|Notes on gaps)', re.I)
SESSION_WORD = re.compile(r'\b(this|next|previous|last|earlier) (batch|session)\b|\bPROCESS INCIDENT\b|how you\'d like|\bPDF pages? \d+', re.I)
def kind_session(L):
    rm = {}
    for i, l in enumerate(L):
        if l.startswith('#') or re.search('[\u0900-\u097f\u0c80-\u0cff]', l) or 'Note on a deliberate skip' in l or 'alphabetical rishi-index' in l: continue
        if SESSION_LABEL.match(l) or re.match(r'^(?:>\s*)?\*\((Superseded|Caveat|No outstanding issues|To be continued)\b.*\)\*\s*$', l) or re.match(r'^(?:>\s*)?- p\.\s?\d+', l) \
           or (SESSION_WORD.search(l) and re.match(r'^(?:>\s*)?(\*\*|\*\(|\d+\. \*\*)', l)):
            rm[i] = None
    return rm
def kind_twin(L):
    sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit'))
    from add_iast import deva_to_iast
    from rapidfuzz import fuzz
    DV = re.compile('[\u0900-\u097f]')
    def key(l):
        l = re.sub(r'\([^()]*\)', '', re.sub(r'^>\s*', '', l))
        return re.sub('[^a-zāīūṛṝḷṃḥśṣṇṭḍñṅ]', '', deva_to_iast(''.join(ch for ch in l if DV.match(ch) or ch == ' ')).lower())
    rm = {}
    for i, a in enumerate(L):
        if not (a.startswith('>') and DV.search(a)) or i in rm: continue
        j = i + 1
        while j < len(L) and L[j].strip() == '>': j += 1
        if j == i + 1 or j + 1 >= len(L): continue
        b = L[j]
        if not (b.startswith('>') and DV.search(b)) or b.lstrip('> ').startswith('*') or not L[j + 1].lstrip('> ').startswith('*'): continue
        ka, kb = key(a), key(b)
        if len(ka) >= 12 and fuzz.ratio(ka, kb) >= 93: rm[j] = None
    # the same over several lines: the verse as printed (lines of Devanagari), an empty quote line, then every line again with the words set
    # apart, each followed by its transliteration
    i = 0
    while i < len(L):
        if not (L[i].startswith('>') and DV.search(L[i]) and '*' not in L[i]): i += 1; continue
        a0 = i
        while i < len(L) and L[i].startswith('>') and DV.search(L[i]) and '*' not in L[i]: i += 1
        if not (i < len(L) and L[i].strip() == '>'): continue
        j = i + 1; deva, ia = [], 0
        while j < len(L) and L[j].startswith('>') and L[j].strip() != '>':
            t = L[j].lstrip('> ')
            if t.startswith('*') and not DV.search(t): ia += 1
            elif DV.search(t) and '*' not in t: deva.append(j)
            else: deva = []; break
            j += 1
        if len(deva) >= 1 and ia >= 1 and not any(d in rm for d in deva):
            ka, kb = key(' '.join(L[a0:i])), key(' '.join(L[d] for d in deva))
            if len(ka) >= 12 and fuzz.ratio(ka, kb) >= 93:
                for d in deva: rm[d] = None
        i = j
    return rm
MAKING = re.compile(r'\bPDF\b|\bscan|\bthe (print|source|original)\b|\bprinted\b|\bprints\b|\btranscrib|\blegib|\brendered\b|\btranslat(ed|ion)\b|\bthis (page|file|section|passage|table|chapter)\b|'
                    r'\b(next|previous|following|preceding) pages?\b|\bcontinu(es|ed|ing)\b|\bomitted\b|\bnot reproduced\b|\bgiven here\b|\bre-?read\b|\bcolumn|\bfigures?\b|\bp\. ?\d|\bpages? \d|'
                    r'\bsessions?\b|\bfirst-pass\b|\bnumeral (pass|review)\b', re.I)
def kind_ownnote(L):
    rm = {}
    for i, l in enumerate(L):
        t = re.sub(r'^>\s*', '', l).strip()
        if 'Note on a deliberate skip' in l or 'alphabetical rishi-index' in l or len(t) > 450: continue
        if re.fullmatch(r'\*[(\[].*[)\]]\*', t) and '*' not in t[2:-2].replace('\\*', '') and MAKING.search(t): rm[i] = None
        elif re.fullmatch(r'\*[^*]+\*', t) and not re.search('[\u0900-\u097f\u0c80-\u0cff]', t) and re.search(r'\bPDF\b|this file\b|first-pass', t): rm[i] = None
    return rm
def kind_leaders(L):
    # '…title ................................. p. 4' (dots typed to imitate the leader of a printed contents page) -> '…title — p. 4'
    rm = {}
    for i, l in enumerate(L):
        n = re.sub(r'\s*\.{5,}\s*(?=pp?\. ?[0-9ivxlc])', ' — ', l)
        if n != l: rm[i] = n
    return rm
KINDS = {'leaders': kind_leaders, 'ownnote': kind_ownnote, 'twin': kind_twin, 'session': kind_session, 'paren': kind_paren, 'firstperson': kind_firstperson, 'asprinted2': kind_asprinted2, 'asprinted': kind_asprinted, 'tentative': kind_tentative, 'clauses': kind_clauses, 'notes': kind_notes, 'oldnotes': kind_oldnotes}
def apply(L, rm):
    last = rm.pop('last', None)
    out = []; gap = False
    for i, l in enumerate(L):
        if i in rm and rm[i] is not None:
            gap = False; out.append(rm[i]); continue
        if i in rm:
            gap = True; continue
        if gap and l == '' and out and out[-1] == '': gap = False; continue   # no doubled blank line where a remark stood
        gap = False; out.append(l)
    while out and out[-1] == '': out.pop()
    if last:
        while out and out[-1] in ('', '---'): out.pop()
        out += ['', '---', '', last]
    return out + ['']
def damage(L):
    bad = []
    pats = [(r'\*\(\s*\)\*', 'empty note'), (r' [,.;:]', 'space before punct'), (r';;', ';;'), (r'\( ', '( '), (r'\n\n\n', '')]
    for i, l in enumerate(L):
        if '  ' in l.strip() and not l.lstrip().startswith(('|', '>')) and '|' not in l: bad.append((i + 1, 'double space', l[:100]))
    for i in range(2, len(L)):
        if L[i] == L[i - 1] == L[i - 2] == '': bad.append((i + 1, 'triple blank', ''))
    return bad
def list_marks(vol):
    d = os.path.join(ROOT, f'vol{vol}'); rows = []
    for name in english_files(vol):
        L = open(os.path.join(d, name), encoding='utf8').read().split('\n'); pg = pages(L)
        for i, l in enumerate(L):
            for m in re.finditer(r'\[\?\]|\[sic\b[^\]]*\]', l):
                rows.append((name.replace(f'Rigveda_Samhita_Vol{vol}_', '').replace('.md', ''), str(pg[i]), str(i + 1), m.group(0)[:5] + (']' if len(m.group(0)) > 5 else ''),
                             ('…' if m.start() > 110 else '') + l[max(0, m.start() - 110):m.end() + 60].replace('\t', ' ')))
    f = os.path.join(d, 'review', 'open_readings.tsv')
    open(f, 'w', encoding='utf8').write('file\tprinted page\tline\tmark\tcontext\n' + ''.join('\t'.join(r) + '\n' for r in rows))
    print(f'{len(rows)} marks -> {os.path.relpath(f, ROOT)}')
def english_files(vol):
    d = os.path.join(ROOT, f'vol{vol}')
    return sorted(x for x in os.listdir(d) if x.endswith('English_Translation.md') and '_scan_' not in x)
def run_all(vol, write):
    import datetime
    d = os.path.join(ROOT, f'vol{vol}'); total = {}
    for name in english_files(vol):
        p = os.path.join(d, name)
        for kind in ('session', 'paren', 'ownnote', 'twin', 'leaders'):
            L = open(p, encoding='utf8').read().split('\n'); pg = pages(L)
            rm = KINDS[kind](L); idx = sorted(k for k in rm if k != 'last')
            print(f'{name}: {kind} {len(idx)}'); total[kind] = total.get(kind, 0) + len(idx)
            if not write or not idx: continue
            new = apply(L, dict(rm)); rd = os.path.join(d, 'review'); os.makedirs(rd, exist_ok=True)
            f = os.path.join(rd, 'removed_remarks.tsv'); new_file = not os.path.exists(f)
            with open(f, 'a', encoding='utf8') as o:
                if new_file: o.write('kind\tpage\tline\ttext removed\tline before\tline after\n')
                for i in idx:
                    o.write('\t'.join([kind, str(pg[i]), str(i + 1), L[i].replace('\t', ' ') + ('' if rm[i] is None else '  ==>  ' + rm[i]), (L[i-1] if i else '')[:150], (L[i+1] if i+1 < len(L) else '')[:150]]) + '\n')
            open(p, 'w', encoding='utf8').write('\n'.join(new))
    if write and sum(total.values()):
        with open(os.path.join(d, 'review', 'repair_log.md'), 'a', encoding='utf8') as o:
            o.write(f"\n- {datetime.date.today()}: tools/rv/cleanup_remarks.py {vol} all --write (REQUIREMENTS B4.6, B2.6): " + ', '.join(f'{k} {v}' for k, v in total.items()) + ' lines; every removal is a row of review/removed_remarks.tsv.\n')
    if write: list_marks(vol)
    else: print('dry run; --write applies')
def main():
    vol, kind = int(sys.argv[1]), sys.argv[2]; write = '--write' in sys.argv
    if kind == 'marks': return list_marks(vol)
    if kind == 'all': return run_all(vol, write)
    p, L = load(vol); pg = pages(L)
    rm = KINDS[kind](L); lastset = rm.get('last')
    idx = sorted(k for k in rm if k != 'last')
    print(f'kind {kind}: {len(idx)} lines to remove'); 
    new = apply(L, dict(rm))
    d0 = len(damage(L)); d1 = damage(new)
    print('damage before/after (double spaces, triple blanks):', d0, len(d1))
    random.seed(7)
    for i in random.sample(idx, min(30, len(idx))):
        print(f'--- p{pg[i]} L{i+1}\n  BEFORE-1: {L[i-1][:90] if i else ""}\n  REMOVE  : {L[i][:200]}\n  NEW     : {rm[i][:200] if rm[i] else None}\n  AFTER+1 : {L[i+1][:90] if i+1<len(L) else ""}')
    if write:
        d = os.path.join(ROOT, f'vol{vol}', 'review'); os.makedirs(d, exist_ok=True)
        f = os.path.join(d, 'removed_remarks.tsv'); new_file = not os.path.exists(f)
        with open(f, 'a', encoding='utf8') as o:
            if new_file: o.write('kind\tpage\tline\ttext removed\tline before\tline after\n')
            for i in idx:
                o.write('\t'.join([kind, str(pg[i]), str(i + 1), L[i].replace('\t', ' ') + ('' if rm[i] is None else '  ==>  ' + rm[i]), (L[i-1] if i else '')[:150], (L[i+1] if i+1 < len(L) else '')[:150]]) + '\n')
        open(p, 'w', encoding='utf8').write('\n'.join(new))
        print('written', p, 'lines', len(L), '->', len(new))
if __name__ == '__main__': main()
