#!/usr/bin/env python3
"""Script-only pass for numbers and references of a legacy volume (user, Nov 11 2026: "numbers and references: the supplied text is taken").

  python3 tools/rv/recheck_numbers.py VOL [--pages A-B] [--kinds refs|plain|all] [--apply]

Dry run by default: writes VOL/review/recheck/numbers_candidates.tsv and prints counts. A correction is proposed only when it is unambiguous:
  * a reference with separators (8-69-12; the English may write I-32-6 or 1.32.6) of the English page that the supplied pages (printed N-1, N, N+1) do not have,
    and exactly ONE supplied reference of those pages that the English page lacks, with the same number of parts and ONE digit different (substituted, added or lost);
  * the same for plain numbers of 2+ digits (--kinds plain|all), same length, one digit substituted.
The digits of the differing part are replaced in the English token (separators and Roman first parts are kept; a difference in a Roman first part is only listed).
--apply edits the English file (every occurrence of that token on the page) and logs each repair in VOL/review/repair_log.md with the tag NUMBER.
Everything that is not unambiguous stays in the list as 'manual' for the editor or the agent: the script never guesses.
Digits are what a machine reads best and what the scan reading got wrong most; but the supplied number can be impossible where it stands (a verse number
out of sequence...): this script cannot see that, so check the list's 'verse/page sequence' cases (marked seq?) before applying."""
import re, sys, os, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recheck as R, recheck_fix as F

REF = re.compile(r'(?<![0-9A-Za-z.])((?:[IVXLC]{1,5}|[0-9]+)(?:\s?[-.:–]\s?[0-9]+)+)(?![0-9])')
KD = R.KD

def parts(tok): return re.split(r'\s?[-.:–]\s?', tok)
def norm_parts(tok):
    p = parts(tok)
    if p[0].isalpha(): p[0] = R._roman(p[0])
    return p

def one_digit(a, b):
    """a, b strings of digits: one substituted, added or lost digit"""
    if len(a) == len(b): return sum(x != y for x, y in zip(a, b)) == 1
    if abs(len(a) - len(b)) == 1:
        s, l = (a, b) if len(a) < len(b) else (b, a)
        return any(l[:i] + l[i + 1:] == s for i in range(len(l)))
    return False

def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    vol = a[0]; d = f'vol{vol}'; apply = '--apply' in a
    kinds = a[a.index('--kinds') + 1] if '--kinds' in a else 'refs'
    rng = a[a.index('--pages') + 1] if '--pages' in a else None; lo, hi = (map(int, rng.split('-')) if rng else (0, 10 ** 6))
    en_files = [p for p in (f'{d}/Rigveda_Samhita_Vol{vol}_English_Translation.md', f'{d}/Rigveda_Samhita_Vol{vol}_Gaps_English_Translation.md') if os.path.exists(p)]
    kn_file = next(p for p in (f'{d}/kannada/Rigveda_Samhita_Vol{vol}_Kannada_Text.md', f'{d}/Rigveda_Samhita_Vol{vol}_Kannada_Text.md') if os.path.exists(p))
    EN = R.read_en(en_files); KN, NOTIN = R.read_kn(kn_file)
    rows = []; todo = []
    for k in sorted(x for x in EN if isinstance(x, int) and lo <= x <= hi):
        if k not in KN or k in NOTIN: continue
        kraw = '\n'.join(KN[x] for x in (k - 1, k, k + 1) if x in KN and x not in NOTIN)
        en = EN[k]
        # --- references
        kr, kp = R.numbers(kraw, True); er, ep = R.numbers(en)
        if kinds in ('refs', 'all'):
            # position anchor: the references of the English page and of the supplied page k, in reading order, are aligned; a 1:1 replacement that
            # differs in one digit is proposed only when the reference before or after it is identical in both (or it is the only one on both pages)
            rawe = [(sorted(R.numbers(m.group(0))[0])[0], '–' in m.group(1)) for m in REF.finditer(en) if R.numbers(m.group(0))[0]]
            seq_e = [x for x, _ in rawe]; dash = {x for x, d in rawe if d}      # an en-dash token is usually a range (Mandalas 2–7): it needs a matching neighbour, never 'alone'
            seq_k = [sorted(R.numbers(m.group(0), True)[0])[0] for m in re.finditer(r'[೦-೯0-9]+(?:\s?[-.:–]\s?[೦-೯0-9]+)+', KN[k]) if R.numbers(m.group(0), True)[0]]
            sm = difflib.SequenceMatcher(None, seq_e, seq_k, autojunk=False); ops = sm.get_opcodes(); proposed = set()
            for n, (tag, i1, i2, j1, j2) in enumerate(ops):
                if tag != 'replace' or i2 - i1 != j2 - j1: continue
                before = n > 0 and ops[n - 1][0] == 'equal'; after = n + 1 < len(ops) and ops[n + 1][0] == 'equal'
                alone = len(seq_e) == 1 == len(seq_k)
                for x, y in zip(seq_e[i1:i2], seq_k[j1:j2]):
                    xp, yp = x.split('-'), y.split('-')
                    if len(xp) == len(yp) and sum(u != v for u, v in zip(xp, yp)) == 1 and all(u == v or one_digit(u, v) for u, v in zip(xp, yp)) and (before or after or (alone and x not in dash)):
                        todo.append((k, 'ref', x, y)); proposed.add(x)
            for e in sorted(er - kr):
                if e not in proposed: rows.append((k, 'ref', e, '', 'manual: no anchored one-digit candidate'))
        if kinds in ('plain', 'all'):
            miss = sorted(ep - kp); extra = sorted(kp - ep)
            for e in miss:
                cands = [c for c in extra if len(c) == len(e) and one_digit(e, c)]
                if len(cands) == 1: todo.append((k, 'plain', e, cands[0]))
                else: rows.append((k, 'plain', e, ','.join(cands), 'manual: ' + ('no one-digit candidate' if not cands else 'ambiguous')))
    out = f'{d}/review/recheck/numbers_candidates.tsv'
    with open(out, 'w', encoding='utf8') as f:
        f.write('page\tkind\tenglish\tsupplied\tstatus\n')
        for k, kind, e, c in todo: f.write(f'{k}\t{kind}\t{e}\t{c}\tproposed\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    print(f'{len(todo)} unambiguous corrections proposed ({sum(1 for t in todo if t[1]=="ref")} references, {sum(1 for t in todo if t[1]=="plain")} plain numbers); {len(rows)} left manual; list: {out}')
    if not apply: return
    done = 0
    for k, kind, e, c in todo:
        path, t, s, en_ = F.locate(vol, k); sec = t[s:en_]; n = 0
        if kind == 'ref':
            def sub(m):
                tok = m.group(1)
                if m.string[m.end():m.end() + 1] == '?': return tok              # '8-2-1?': garbled in the English, left for the editor
                ptoks = parts(tok); np_ = norm_parts(tok); target = c.split('-')
                if np_ == e.split('-'):
                    seps = re.findall(r'\s?[-.:–]\s?', tok); new = ''
                    for i, p in enumerate(ptoks):
                        if i == 0 and p.isalpha():
                            if p and R._roman(p) != target[0]: return tok            # a Roman first part that differs: manual
                            new += p
                        else: new += target[i]
                        if i < len(seps): new += seps[i]
                    nonlocal_n[0] += 1
                    return new
                return tok
            nonlocal_n = [0]; sec2 = REF.sub(sub, sec)
        else:
            nonlocal_n = [0]; sec2 = re.sub(r'(?<![0-9-])' + re.escape(e) + r'(?![0-9-])', lambda m: (nonlocal_n.__setitem__(0, nonlocal_n[0] + 1) or c), sec)
        if sec2 == sec: continue
        open(path, 'w', encoding='utf8').write(t[:s] + sec2 + t[en_:])
        F.log(vol, k, e, c, f'NUMBER the supplied text reads {c} (one digit differs; no other candidate on pages {k-1}-{k+1}); {nonlocal_n[0]} occurrence(s) on the page', False)
        done += 1
    print(f'applied: {done} corrections')

if __name__ == '__main__': main()
