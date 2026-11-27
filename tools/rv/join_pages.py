#!/usr/bin/env python3
"""Sentences cut at a page turn of the original (or left hanging on "...") made whole again (user, Nov 26 2026; REQUIREMENTS A4 print rule 4).

  python3 tools/rv/join_pages.py prep N [--batch 20]     lists the places -> volN/review/junctions/batch_XX.json (for a reading model)
  python3 tools/rv/join_pages.py apply N [--write]       carries out volN/review/junctions/out_XX.json; dry run without --write
  python3 tools/rv/join_pages.py reapply N [--write]     the answers refused because the text was edited afterwards: mended again at the break only

A place ("junction") is: (P) a page heading of the working file with the text before it ending in "..." / "…" or the text after it beginning
so; (M) a prose line inside a page that ends in "..." (not a quotation, not Sanskrit).  For each the file gives the last words of the line
before (a_tail), the first words of the line after (b_head) and, where the volume has a Kannada text with page marks, the end and the
beginning of the Kannada pages concerned.  The reader returns a_tail_new / b_head_new: the same words with the dots gone and the join made
readable, changing as little as possible.  `apply` accepts an answer only if every figure and every Devanagari/Kannada letter of the old
words is still there, replaces exactly those words, and logs old -> new in volN/review/junction_repairs.tsv.  The page headings stay
where they are (the print step joins the two halves into one paragraph: publish/printfix.join_page_turns)."""
import os, re, sys, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOTS_END = re.compile(r'(\.\.\.+|…)([*_"“”\'’)\]]*)\s*$'); DOTS_START = re.compile(r'^([>\s*"“(\[]*)(\.\.\.+|…)\s*')
INDIC = re.compile('[ऀ-ॿಀ-೿]')
def files(vol):
    d = os.path.join(ROOT, f'vol{vol}')
    return [os.path.join(d, x) for x in sorted(os.listdir(d)) if x.endswith('English_Translation.md') and '_scan_' not in x]
def kannada_pages(vol):
    for p in (f'vol{vol}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md', f'vol{vol}/kannada/Rigveda_Samhita_Vol{vol}_Kannada_Text.md'):
        p = os.path.join(ROOT, p)
        if os.path.exists(p):
            parts = re.split(r'<!-- printed (\d+) -->', open(p, encoding='utf8').read())
            return {int(parts[k]): parts[k + 1].strip() for k in range(1, len(parts) - 1, 2)}
    return {}
def words(s, n, tail):
    w = s.split(' ')
    return ' '.join(w[-n:] if tail else w[:n])
def find(vol):
    kn = kannada_pages(vol); out = []
    for f in files(vol):
        L = open(f, encoding='utf8').read().split('\n'); page = None
        def nb(i, d):
            j = i + d
            while 0 <= j < len(L) and (not L[j].strip() or L[j].strip() in ('---', '>')): j += d
            return j
        for i, l in enumerate(L):
            m = re.match(r'#{2,4} \[?(?:Printed )?(?:Pages?|p\.) ?(\d+|[ivxlc]+)', l)
            if m:
                page = m.group(1); a, b = nb(i, -1), nb(i, 1)
                if a < 0 or b >= len(L) or L[a].startswith('#') or L[b].startswith('#'): continue
                if not (DOTS_END.search(L[a]) or DOTS_START.match(L[b])): continue
                if INDIC.search(words(L[a], 12, True)) and INDIC.search(words(L[b], 12, False)): continue      # Sanskrit running over the page: not ours to join
                j = {'kind': 'P', 'file': os.path.basename(f), 'a_line': a + 1, 'b_line': b + 1, 'page': page, 'a_tail': words(L[a], 45, True), 'b_head': words(L[b], 45, False)}
                if page.isdigit() and int(page) in kn:
                    j['kannada_end_of_previous_page'] = kn.get(int(page) - 1, '')[-600:]; j['kannada_start_of_this_page'] = kn[int(page)][:600]
                out.append(j)
            elif not l.startswith(('#', '>', '|')) and DOTS_END.search(l) and not INDIC.search(words(l, 12, True)):
                b = nb(i, 1)
                if b < len(L) and re.match(r'#{2,4} \[?(?:Printed )?(?:Pages?|p\.)', L[b]): continue                    # handled as P at the heading
                if l.rstrip().endswith(('"', '”')) or re.match(r'^\*?\(', l): continue                                   # an ellipsis inside a quotation or a note of ours
                out.append({'kind': 'M', 'file': os.path.basename(f), 'a_line': i + 1, 'b_line': b + 1 if b < len(L) else None, 'page': page,
                            'a_tail': words(l, 45, True), 'b_head': words(L[b], 30, False) if b < len(L) else ''})
    for k, j in enumerate(out): j['id'] = k + 1
    return out
def prep(vol, size):
    js = find(vol); d = os.path.join(ROOT, f'vol{vol}', 'review', 'junctions'); os.makedirs(d, exist_ok=True)
    for f in glob.glob(os.path.join(d, 'batch_*.json')): os.remove(f)
    for k in range(0, len(js), size):
        json.dump(js[k:k + size], open(os.path.join(d, f'batch_{k // size + 1:02d}.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(f'{len(js)} junctions (P {sum(j["kind"] == "P" for j in js)}, M {sum(j["kind"] == "M" for j in js)}; with Kannada {sum("kannada_start_of_this_page" in j for j in js)}) -> {os.path.relpath(d, ROOT)}/batch_01..{(len(js) - 1) // size + 1:02d}.json')
def tokens(s): return sorted(re.findall(r'\d+', s)), sorted(INDIC.findall(s))
def edge(old, new, tail):
    """the part of an answer that was really changed: at the end of a_tail (tail=True) or at the beginning of b_head"""
    ow, nw = old.split(' '), new.split(' ')
    if tail:
        k = 0
        while k < min(len(ow), len(nw)) and ow[k] == nw[k]: k += 1
        return ' '.join(ow[k:]), ' '.join(nw[k:]), ' '.join(ow[max(0, k - 6):k])
    k = 0
    while k < min(len(ow), len(nw)) and ow[-1 - k] == nw[-1 - k]: k += 1
    return ' '.join(ow[:len(ow) - k]), ' '.join(nw[:len(nw) - k]), ' '.join(ow[len(ow) - k:len(ow) - k + 6])
def reapply(vol, write):
    """A mended sentence whose surroundings were changed afterwards (the second pass edited words near the break) is mended again:
    only the words the answer really changed, at the very break, are replaced, and only where they still stand in the file exactly,
    in a line that is still the same sentence (the six words next to the change agree, or the whole end is alike >= 80 of 100)."""
    from rapidfuzz import fuzz
    d = os.path.join(ROOT, f'vol{vol}', 'review', 'junctions')
    ans = {a['id']: a for f in sorted(glob.glob(os.path.join(d, 'out_*.json'))) for a in json.load(open(f, encoding='utf8'))}
    js = {j['id']: j for b in sorted(glob.glob(os.path.join(d, 'batch_*.json'))) for j in json.load(open(b, encoding='utf8'))}
    log = os.path.join(ROOT, f'vol{vol}', 'review', 'junction_repairs.tsv')
    refused = [int(l.split('\t')[0]) for l in open(log, encoding='utf8').read().split('\n')[1:] if l.split('\t')[5:6] == ['refused']]
    texts, rows, stat = {}, [], {'applied': 0, 'already whole': 0, 'still refused': 0}
    for jid in refused:
        j, a = js[jid], ans[jid]; an, bn = a.get('a_tail_new', j['a_tail']), a.get('b_head_new', j['b_head'])
        p = os.path.join(ROOT, f'vol{vol}', j['file']); L = texts.setdefault(p, open(p, encoding='utf8').read().split('\n'))
        ao, anw, actx = edge(j['a_tail'], an, True); bo, bnw, bctx = edge(j['b_head'], bn, False)
        if tokens(ao + ' ' + bo) != tokens(anw + ' ' + bnw): stat['still refused'] += 1; rows.append((j, 'refused again', an, bn, 'a figure or an Indic letter differs')); continue
        ia = [k for k, x in enumerate(L) if ao and x.endswith(ao) and (x[:len(x) - len(ao)].rstrip().endswith(actx.strip()) or fuzz.ratio(words(x, 45, True), j['a_tail']) >= 80)] if ao else []
        if ao and len(ia) != 1:
            near = [k for k, x in enumerate(L) if fuzz.ratio(words(x, 45, True), an) >= 90]
            if len(near) == 1: stat['already whole'] += 1; rows.append((j, 'already whole', '', '', 'the sentence stands mended in the file')); continue
            stat['still refused'] += 1; rows.append((j, 'refused again', an, bn, 'the words at the break are not in the file any more')); continue
        ka = ia[0] if ao else next((k for k, x in enumerate(L) if fuzz.ratio(words(x, 45, True), j['a_tail']) >= 85), None)
        kb = None
        if bo:
            if ka is None: stat['still refused'] += 1; rows.append((j, 'refused again', an, bn, 'the place was not found')); continue
            kb = next((k for k in range(ka + 1, min(ka + 12, len(L))) if L[k].startswith(bo)), None)
            if kb is None: stat['still refused'] += 1; rows.append((j, 'refused again', an, bn, 'the words after the break are not in the file any more')); continue
        if ao: L[ka] = L[ka][:len(L[ka]) - len(ao)] + anw
        if bo: L[kb] = bnw + L[kb][len(bo):]
        stat['applied'] += 1; rows.append((j, 'applied (re-applied at the break)', anw, bnw, f'old: {ao!r} | {bo!r}'))
    print(stat)
    if write:
        for p, L in texts.items(): open(p, 'w', encoding='utf8').write('\n'.join(L))
        with open(log, 'a', encoding='utf8') as o:
            for j, st, an, bn, why in rows:
                o.write('\t'.join(str(x).replace('\t', ' ').replace('\n', ' ') for x in (j['id'], j['file'], j['page'], '', '', st, j['a_tail'], j['b_head'], an, bn, why)) + '\n')
        print('written; log:', os.path.relpath(log, ROOT))
    else:
        for j, st, an, bn, why in rows:
            if st != 'applied (re-applied at the break)': print(' ', j['id'], st, '|', why)
def apply(vol, write):
    d = os.path.join(ROOT, f'vol{vol}', 'review', 'junctions'); ans = {}
    for f in sorted(glob.glob(os.path.join(d, 'out_*.json'))):
        for a in json.load(open(f, encoding='utf8')): ans[a['id']] = a
    js = {j['id']: j for b in sorted(glob.glob(os.path.join(d, 'batch_*.json'))) for j in json.load(open(b, encoding='utf8'))}
    texts = {}; rows = []; stat = {'applied': 0, 'unchanged': 0, 'unsure': 0, 'refused': 0, 'no answer': 0}
    for jid, j in sorted(js.items()):
        a = ans.get(jid)
        if not a: stat['no answer'] += 1; continue
        if a.get('status') == 'unsure': stat['unsure'] += 1; rows.append((j, 'unsure', '', '', a.get('reason', ''))); continue
        p = os.path.join(ROOT, f'vol{vol}', j['file']); L = texts.setdefault(p, open(p, encoding='utf8').read().split('\n'))
        an, bn = a.get('a_tail_new', j['a_tail']), a.get('b_head_new', j['b_head'])
        if an == j['a_tail'] and bn == j['b_head']: stat['unchanged'] += 1; continue
        ia = [k for k, x in enumerate(L) if x.endswith(j['a_tail'])]                      # the file may have changed since the list was made: the words decide
        if len(ia) != 1: stat['refused'] += 1; rows.append((j, 'refused', an, bn, 'the words before the break are no longer in the file as listed')); continue
        j = dict(j); j['a_line'] = ia[0] + 1
        if j['b_line']:
            ib = next((k for k in range(ia[0] + 1, min(ia[0] + 12, len(L))) if L[k].startswith(j['b_head'])), None)
            if ib is None and bn != j['b_head']: stat['refused'] += 1; rows.append((j, 'refused', an, bn, 'the words after the break are no longer in the file as listed')); continue
            j['b_line'] = (ib + 1) if ib is not None else None
        la = L[j['a_line'] - 1]; lb = L[j['b_line'] - 1] if j['b_line'] else ''
        why = ''
        if not la.endswith(j['a_tail']) or (j['b_line'] and bn != j['b_head'] and not lb.startswith(j['b_head'])): why = 'the text is no longer as it was when listed'
        elif tokens(j['a_tail'] + ' ' + j['b_head']) != tokens(an + ' ' + bn) and not a.get('dup_ok'): why = 'a figure or an Indic letter differs'     # dup_ok: the same figure stood on both sides of the break
        elif len((an + ' ' + bn).split()) > len((j['a_tail'] + ' ' + j['b_head']).split()) + 25: why = 'more than 25 words added'
        elif not an.strip() and not bn.strip(): why = 'empty answer'
        elif j['kind'] == 'M' and len(an.split()) < len(j['a_tail'].split()) - 2: why = 'words dropped from a line inside a page'
        if why: stat['refused'] += 1; rows.append((j, 'refused', an, bn, why)); continue
        L[j['a_line'] - 1] = la[:len(la) - len(j['a_tail'])] + an
        if j['b_line'] and bn != j['b_head']: L[j['b_line'] - 1] = bn + lb[len(j['b_head']):]
        stat['applied'] += 1; rows.append((j, 'applied', an, bn, a.get('reason', '')))
    print(stat)
    if write:
        for p, L in texts.items(): open(p, 'w', encoding='utf8').write('\n'.join(L))
        f = os.path.join(ROOT, f'vol{vol}', 'review', 'junction_repairs.tsv'); new = not os.path.exists(f)
        with open(f, 'a', encoding='utf8') as o:
            if new: o.write('id\tfile\tpage\tline before\tline after\tstatus\told end\told beginning\tnew end\tnew beginning\tnote\n')
            for j, st, an, bn, why in rows:
                o.write('\t'.join(str(x).replace('\t', ' ').replace('\n', ' ') for x in (j['id'], j['file'], j['page'], j['a_line'], j['b_line'], st, j['a_tail'], j['b_head'], an, bn, why)) + '\n')
        print('written; log:', os.path.relpath(f, ROOT))
    else: print('dry run; --write applies')
if __name__ == '__main__':
    if len(sys.argv) < 3: sys.exit(__doc__)
    vol = int(sys.argv[2])
    if sys.argv[1] == 'prep': prep(vol, int(sys.argv[sys.argv.index('--batch') + 1]) if '--batch' in sys.argv else 20)
    elif sys.argv[1] == 'apply': apply(vol, '--write' in sys.argv)
    elif sys.argv[1] == 'reapply': reapply(vol, '--write' in sys.argv)
