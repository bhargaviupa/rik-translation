#!/usr/bin/env python3
"""Second reading of the `[?]` marks of a scan-made volume by agents (shared tool; Vol 25 first). No API.

  python3 tools/rv/scan_reread.py plan VOL [--pages N] [--kinds head,number,word] [--only P1,P2,..]
        writes volN/review/reread/job_NNN.md (the questions of N pages, with the image files) from volN/review/questions.tsv
  python3 tools/rv/scan_reread.py check VOL
        every job has an answer file volN/review/reread/ans_NNN.tsv; every question answered; reports counts of certain/likely/unreadable
  python3 tools/rv/scan_reread.py apply VOL [--write]
        for answers marked `certain`: in volN/work/scan_pages/pNNNN.md replaces the Nth `[?]` of the line (the mark and the token before it)
        by the answer; prints each change (preview without --write); logs to volN/review/reread_applied.tsv; fills questions.tsv `answer` and `source`.
        `likely` and `unreadable` stay in the pages and go to the user (questions.tsv rows without an answer)."""
import os, re, sys, csv, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
def qs(vol): return list(csv.DictReader(open(os.path.join(ROOT, f'vol{vol}', 'review', 'questions.tsv'), encoding='utf8'), delimiter='\t'))
def plan(vol, n, kinds, only):
    R = [q for q in qs(vol) if q['kind'] in kinds and (not only or int(q['pdf_page']) in only)]
    pages = sorted({int(q['pdf_page']) for q in R}); d = os.path.join(ROOT, f'vol{vol}', 'review', 'reread'); os.makedirs(d, exist_ok=True)
    for old in glob.glob(os.path.join(d, 'job_*.md')): os.remove(old)
    for j in range(0, len(pages), n):
        grp = pages[j:j + n]; k = j // n + 1; L = [f'# Job {k:03d}: PDF pages {", ".join(map(str, grp))}\n']
        for pg in grp:
            L.append(f'## Page {pg}: images vol{vol}/work/scan_pilot/p-{pg:04d}a.jpg (top half) and p-{pg:04d}b.jpg (bottom half); text file vol{vol}/work/scan_pages/p{pg:04d}.md\n')
            L.append('id\tline\tnth_mark\timage\tkind\ttoken_before_mark\tline_text')
            for q in R:
                if int(q['pdf_page']) == pg: L.append('\t'.join([q['id'], q['line'], q['nth_mark'], q['image'], q['kind'], q['reading'], q['context']]))
            L.append('')
        open(os.path.join(d, f'job_{k:03d}.md'), 'w', encoding='utf8').write('\n'.join(L))
    print(f'{len(R)} questions on {len(pages)} pages → {(len(pages) + n - 1) // n} jobs in {d}')
def answers(vol):
    A = {}
    for f in sorted(glob.glob(os.path.join(ROOT, f'vol{vol}', 'review', 'reread', 'ans_*.tsv'))):
        for r in csv.reader(open(f, encoding='utf8'), delimiter='\t'):
            if r and r[0].startswith('Q') and len(r) >= 3: A[r[0]] = (r[1].strip(), r[2].strip().lower(), r[3].strip() if len(r) > 3 else '', r[4].strip() if len(r) > 4 else None)
    return A
def check(vol):
    A = answers(vol); Q = qs(vol); jobs = glob.glob(os.path.join(ROOT, f'vol{vol}', 'review', 'reread', 'job_*.md'))
    want = set(re.findall(r'^(Q\d{4})\t', ''.join(open(j, encoding='utf8').read() for j in jobs), re.M)); miss = sorted(want - set(A))
    from collections import Counter
    print(f'{len(A)} answers for {len(want)} questions in jobs; missing {len(miss)}', miss[:10], dict(Counter(a[1] for a in A.values())))
    return not miss
def apply(vol, write):
    A = answers(vol); Q = {q['id']: q for q in qs(vol)}; log = []; byp = {}
    for i, (new, conf, note, expect) in A.items():
        if conf == 'certain' and i in Q and expect is not None and Q[i]['reading'] == expect: byp.setdefault(int(Q[i]['pdf_page']), []).append(i)
        elif conf == 'certain': print('REFUSED (answer row has no matching expect column; question ids change when questions.tsv is rebuilt)', i)
    for pg, ids in sorted(byp.items()):
        f = os.path.join(ROOT, f'vol{vol}', 'work', 'scan_pages', f'p{pg:04d}.md'); L = open(f, encoding='utf8').read().split('\n'); ch = False
        # latest mark first, so earlier positions stay valid
        for i in sorted(ids, key=lambda x: (int(Q[x]['line']), int(Q[x]['nth_mark'])), reverse=True):
            q = Q[i]; ln = int(q['line']) - 1; marks = [m.start() for m in re.finditer(r'\[\?\]', L[ln])]; k = int(q['nth_mark']) - 1
            if k >= len(marks): print('SKIP (mark gone)', i); continue
            e = marks[k]; before = L[ln][:e]; tok = q['reading'][:-3]
            if not before.endswith(tok): print('SKIP (token differs)', i, repr(tok), repr(before[-12:])); continue
            new = A[i][0]; L[ln] = before[:len(before) - len(tok)] + new + L[ln][e + 3:]; ch = True
            log.append((i, pg, q['line'], q['reading'], new, A[i][2])); print(f'{i} p{pg} l{q["line"]}: {q["reading"]} → {new}')
        if ch and write: open(f, 'w', encoding='utf8').write('\n'.join(L))
    if write and log:
        lf = os.path.join(ROOT, f'vol{vol}', 'review', 'reread_applied.tsv'); new = not os.path.exists(lf)
        with open(lf, 'a', encoding='utf8') as o:
            if new: o.write('id\tpdf_page\tline\twas\tnow\tnote\n')
            for r in log: o.write('\t'.join(map(str, r)) + '\n')
        done = {r[0]: r for r in log}; rows = list(csv.reader(open(os.path.join(ROOT, f'vol{vol}', 'review', 'questions.tsv'), encoding='utf8'), delimiter='\t'))
        for r in rows[1:]:
            if r[0] in done: r[8] = done[r[0]][4]; r[9] = 'agent re-read (certain)'
        csv.writer(open(os.path.join(ROOT, f'vol{vol}', 'review', 'questions.tsv'), 'w', encoding='utf8', newline=''), delimiter='\t', lineterminator='\n').writerows(rows)
    print(f'{len(log)} changes' + ('' if write else ' (preview; --write to apply)'))
if __name__ == '__main__':
    a = sys.argv[1:]; cmd, vol = a[0], a[1]; kw = {}
    for f in ('--pages', '--kinds', '--only'):
        if f in a: kw[f] = a[a.index(f) + 1]
    if cmd == 'plan': plan(vol, int(kw.get('--pages', 3)), kw.get('--kinds', 'head,number,word').split(','), {int(x) for x in kw['--only'].split(',')} if '--only' in kw else None)
    elif cmd == 'check': sys.exit(0 if check(vol) else 1)
    elif cmd == 'apply': apply(vol, '--write' in a)
