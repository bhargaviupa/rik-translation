#!/usr/bin/env python3
"""The ONLY way the re-check agents edit a legacy volume's English file: one repair, one log line.

  python3 tools/rv/recheck_fix.py VOL PAGE --text OLD NEW --why "reason" [--qmark-kept] [--meaning]      plain text (digits, Latin words, `[?]`)
  python3 tools/rv/recheck_fix.py VOL PAGE --kn OLD_KN NEW_KN --why "reason" [--meaning]                  Sanskrit: both strings in KANNADA script, copied from the supplied text

--text: OLD must occur exactly once in the page's section of the English file (`### Page PAGE`), in the Latin-script text (not inside a Devanagari line).
--kn:   the Kannada strings are converted to Devanagari by script (publish/tools/translit/kannada_to_deva.py); every Devanagari line of the page that contains the
        old reading gets the new one; an IAST line is regenerated (deva_to_iast) only when it is exactly what the script makes from the Devanagari line above it,
        otherwise it is left and reported ('IAST not updated'). Nobody types Devanagari or IAST.
Every successful call appends  | page | old -> new | why |  to VOL/review/repair_log.md (created with a header). --dry-run shows the change without writing.
--meaning: the change alters the meaning, so the English sentence that depends on it needs an edit too: the log line says so (edit it afterwards with --text)."""
import re, sys, os, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'publish', 'tools', 'translit'))
from kannada_to_deva import kn2deva
from add_iast import deva_to_iast, DEV

def locate(vol, page):
    for p in (f'vol{vol}/Rigveda_Samhita_Vol{vol}_English_Translation.md', f'vol{vol}/Rigveda_Samhita_Vol{vol}_Gaps_English_Translation.md'):
        if not os.path.exists(p): continue
        t = open(p, encoding='utf8').read()
        m = re.search(r'(?m)^### Page %s(?=[\s—:]|$)[^\n]*\n' % re.escape(str(page)), t)
        if m:
            n = re.search(r'(?m)^### Page ', t[m.end():]); e = m.end() + n.start() if n else len(t)
            return p, t, m.end(), e
    sys.exit(f'REFUSED: no "### Page {page}" in the English files of Vol {vol}')

def spaceless(line, od, nd):
    """the old reading found in a line whose words are separated by spaces/hyphens (the sandhi-split reading): the span is replaced by the new reading;
    None when it is not there (e.g. the split reading differs at a sandhi boundary)"""
    idx = [i for i, ch in enumerate(line) if ch not in ' -\u200c\u200d']
    flat = ''.join(line[i] for i in idx); j = flat.find(od)
    if j < 0 or flat.count(od) != 1: return None
    a, b = idx[j], idx[j + len(od) - 1] + 1
    return line[:a] + nd + line[b:]

def log(vol, page, old, new, why, meaning):
    p = f'vol{vol}/review/repair_log.md'; os.makedirs(os.path.dirname(p), exist_ok=True)
    if not os.path.exists(p): open(p, 'w', encoding='utf8').write('# Vol %s repair log (re-check against the supplied text)\n\nOne line per repair of the closed English file: page, old -> new, why. Made by tools/rv/recheck_fix.py.\n\n| page | old → new | why |\n|---|---|---|\n' % vol)
    cell = lambda x: x.replace('|', '\\|').replace('\n', ' ')
    open(p, 'a', encoding='utf8').write(f'| {page} | `{cell(old)}` → `{cell(new)}` | {cell(why)}{" **(meaning changed: the English sentence that depends on it needs its own edit)**" if meaning else ""} |\n')

def main():
    a = sys.argv[1:]
    if len(a) < 4: sys.exit(__doc__)
    vol, page = a[0], a[1]; dry = '--dry-run' in a
    why = a[a.index('--why') + 1] if '--why' in a else sys.exit('REFUSED: --why "reason" is required')
    meaning = '--meaning' in a
    path, t, s, e = locate(vol, page); sec = t[s:e]
    if '--text' in a:
        i = a.index('--text'); old, new = a[i + 1], a[i + 2]
        if re.search(DEV, old) or re.search(DEV, new): sys.exit('REFUSED: no Devanagari in --text; use --kn with Kannada-script strings')
        if re.search('[\u0c80-\u0cff]', new): sys.exit('REFUSED: no Kannada script in the English text (Sanskrit goes through --kn)')
        if sec.count(old) != 1: sys.exit(f'REFUSED: "{old}" occurs {sec.count(old)} times in the section of page {page} (must be exactly 1: add context)')
        if any(old in l for l in sec.split('\n') if len(re.findall(DEV, l)) >= 3): sys.exit('REFUSED: that text is inside a Devanagari line; use --kn')
        sec2 = sec.replace(old, new); note = ''
    elif '--kn' in a:
        i = a.index('--kn'); old_kn, new_kn = a[i + 1], a[i + 2]
        od, nd = kn2deva(old_kn), kn2deva(new_kn); oi, ni = deva_to_iast(od), deva_to_iast(nd)
        lines = sec.split('\n'); hit = 0; split_fixed = 0; iast_done = 0; iast_skip = []; last_dev = None
        for k, l in enumerate(lines):
            if len(re.findall(DEV, l)) >= 3:
                if od in l: lines[k] = l.replace(od, nd); hit += 1
                elif spaceless(l, od, nd) is not None: lines[k] = spaceless(l, od, nd); hit += 1; split_fixed += 1      # sandhi-split line: spaces and hyphens ignored in the match
                last_dev = (k, l); continue
            if last_dev and re.match(r'^>\s*\*[^*(].*\*\s*$', l):
                src = last_dev[1].lstrip('> ').strip(); mach = '> *' + deva_to_iast(src) + '*'
                if od in last_dev[1]:
                    if re.sub(r'\s+', ' ', l.strip()) == re.sub(r'\s+', ' ', mach.strip()): lines[k] = '> *' + deva_to_iast(src.replace(od, nd)) + '*'; iast_done += 1
                    elif oi in l: lines[k] = l.replace(oi, ni); iast_done += 1
                    else: iast_skip.append(k)
        runs, cur = [], []                                   # blockquote runs: a hit line and the other Devanagari lines of its run (the sandhi-split reading) are reported
        for k, l in enumerate(sec.split('\n') + ['']):
            if l.startswith('>'): cur.append(k)
            else:
                if cur: runs.append(cur)
                cur = []
        other = sum(1 for r in runs if any(od in sec.split('\n')[k] for k in r) for k in r if len(re.findall(DEV, sec.split('\n')[k])) >= 3 and od not in sec.split('\n')[k])
        if not hit: sys.exit(f'REFUSED: the old reading (Devanagari {od}) is in no Devanagari line of page {page}; no change made')
        sec2 = '\n'.join(lines); old, new = old_kn + ' = ' + od, new_kn + ' = ' + nd
        note = f'{hit} Devanagari line(s) changed' + (f' ({split_fixed} sandhi-split)' if split_fixed else '') + f'; IAST line(s) updated: {iast_done}' + (f'; IAST NOT updated for {len(iast_skip)} line(s): check by hand' if iast_skip else '') + (f'; {other} other Devanagari line(s) of the same block do not contain the old reading (sandhi-split form?) and were NOT changed' if other else '')
    else: sys.exit(__doc__)
    print(('DRY RUN: ' if dry else '') + f'page {page}: {old} -> {new}. {note}')
    if dry: return
    open(path, 'w', encoding='utf8').write(t[:s] + sec2 + t[e:])
    log(vol, page, old, new, why + (' [' + note + ']' if note else ''), meaning)

if __name__ == '__main__': main()
