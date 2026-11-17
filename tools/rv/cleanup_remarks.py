#!/usr/bin/env python3
"""Remove the translator's remarks from a legacy volume's English file, one KIND at a time (Vol 2 clean-up, user, Nov 17 2026).

  python3 tools/rv/cleanup_remarks.py VOL KIND [--write]

KINDs: oldnotes   old mid-file progress/target notes and the closing progress notes (-> one trailing progress note)
       notes      whole-line italic notes *( ... )* in which EVERY sentence is a process remark (mixed notes stay; listed in review/notes_kept.tsv)
Dry run by default: prints counts, damage checks and 30 before/after samples.  --write applies, appends to volN/review/removed_remarks.tsv
(kind, page, line, text removed, line before, line after) so that any removal can be undone, and prints the damage report.
Never touches lines with Devanagari/Kannada, `[?]`, `[sic]` (user decision); whole remarks only, never half a sentence."""
import os, re, sys, random
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ABBR = re.compile(r'(?:^|[\s(*"“])(?:\w{1,3}|Ṛ|Pā|Nir|Saṃ|Brā|Ai|Sū|Ni|cf|Dr|Śrī)$')
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
    r'^Printed references (on this page|at the head|in the grammar).*$',
)]
def process_sentence(s):
    s = s.strip().rstrip('.').strip()
    return bool(s) and all(any(c.match(cl.strip()) for c in CLAUSE) for cl in re.split(r';\s*', s) if cl.strip())
KEEPNOTE = re.compile(r':\s*$')            # lead-in to a list: stays
NOTE = re.compile(r'(\s*>?\s*)\*\((.*)\)\*\s*$')
def load(vol):
    p = os.path.join(ROOT, f'vol{vol}', f'Rigveda_Samhita_Vol{vol}_English_Translation.md')
    return p, open(p, encoding='utf8').read().split('\n')
def pages(L):
    pg = 0; out = []
    for l in L:
        m = re.match(r'### Pages? (\d+)', l)
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
KINDS = {'notes': kind_notes, 'oldnotes': kind_oldnotes}
def apply(L, rm):
    last = rm.pop('last', None)
    out = []; gap = False
    for i, l in enumerate(L):
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
def main():
    vol, kind = int(sys.argv[1]), sys.argv[2]; write = '--write' in sys.argv
    p, L = load(vol); pg = pages(L)
    rm = KINDS[kind](L); lastset = rm.get('last')
    idx = sorted(k for k in rm if k != 'last')
    print(f'kind {kind}: {len(idx)} lines to remove'); 
    new = apply(L, dict(rm))
    d0 = len(damage(L)); d1 = damage(new)
    print('damage before/after (double spaces, triple blanks):', d0, len(d1))
    random.seed(7)
    for i in random.sample(idx, min(30, len(idx))):
        print(f'--- p{pg[i]} L{i+1}\n  BEFORE-1: {L[i-1][:90] if i else ""}\n  REMOVE  : {L[i][:200]}\n  AFTER+1 : {L[i+1][:90] if i+1<len(L) else ""}')
    if write:
        d = os.path.join(ROOT, f'vol{vol}', 'review'); os.makedirs(d, exist_ok=True)
        f = os.path.join(d, 'removed_remarks.tsv'); new_file = not os.path.exists(f)
        with open(f, 'a', encoding='utf8') as o:
            if new_file: o.write('kind\tpage\tline\ttext removed\tline before\tline after\n')
            for i in idx:
                o.write('\t'.join([kind, str(pg[i]), str(i + 1), L[i].replace('\t', ' '), (L[i-1] if i else '')[:150], (L[i+1] if i+1 < len(L) else '')[:150]]) + '\n')
        open(p, 'w', encoding='utf8').write('\n'.join(new))
        print('written', p, 'lines', len(L), '->', len(new))
if __name__ == '__main__': main()
