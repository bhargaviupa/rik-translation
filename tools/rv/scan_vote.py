#!/usr/bin/env python3
"""Vote over the readings of each doubtful number/word of a scan-made volume (shared tool; Vol 25 first). No API.

  python3 tools/rv/scan_vote.py VOL [--write]
Readers per question: the first reader (the token before the `[?]`), crop pass A and B (volN/review/crops_read/A_*.tsv, B_*.tsv: id, answer, confidence, note;
`unreadable` counts as no vote), and the OCR (volN/review/ocr_numbers.tsv: the numbers on the best-matching printed line; no vote if the line match is under 0.6).
Digits are compared as Latin digits, dashes unified, spaces removed. Rule (two independent readings must agree):
  1. A and B agree (neither unreadable)            → that value
  2. else the first reader agrees with A or B       → the first reader's token (the mark is simply cleared)
  3. else the OCR agrees with A or B                → that value
  4. else open: volN/review/votes_open.tsv (all readings side by side)
`--words`: the word passes (WA_*.tsv, WB_*.tsv; no OCR vote). `--write` writes volN/review/reread/ans_votes.tsv (rows `certain`, with the `expect` column that scan_reread.py apply requires) and the open list."""
import os, re, sys, csv, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KD = str.maketrans('೦೧೨೩೪೫೬೭೮೯', '0123456789')
def norm(s): return re.sub(r'[\s]|\[\?\]|\u200c|\u200d', '', s.translate(KD).replace('–', '-').replace('—', '-').replace('−', '-'))
def main():
    a = sys.argv[1:]; vol = a[0]; write = '--write' in a; words = '--words' in a; R = lambda *p: os.path.join(ROOT, f'vol{vol}', *p)
    Q = {q['id']: q for q in csv.DictReader(open(R('review', 'questions.tsv'), encoding='utf8'), delimiter='\t')}
    def load(pat):
        D = {}
        for f in glob.glob(R('review', 'crops_read', pat)):
            for r in csv.reader(open(f, encoding='utf8'), delimiter='\t'):
                if r and r[0].startswith('Q') and len(r) >= 3: D[r[0]] = (r[1].strip(), r[2].strip().lower(), r[3] if len(r) > 3 else '')
        return D
    A, B = (load('WA_*.tsv'), load('WB_*.tsv')) if words else (load('A_*.tsv'), load('B_*.tsv')); O = {}
    if not words and os.path.exists(R('review', 'ocr_numbers.tsv')):
        for r in csv.DictReader(open(R('review', 'ocr_numbers.tsv'), encoding='utf8'), delimiter='\t'):
            if float(r['line_match']) >= 0.6: O[r['id']] = [t for t in r['ocr_numbers_on_line'].split() if t]
    done = []; opn = []; why = {1: 0, 2: 0, 3: 0}
    for i in sorted(set(A) | set(B)):
        if i not in Q: continue
        q = Q[i]; first = q['reading'][:-3]; f = norm(first)
        va = A.get(i); vb = B.get(i)
        ra = norm(va[0]) if va and va[1] != 'unreadable' else None; rb = norm(vb[0]) if vb and vb[1] != 'unreadable' else None
        ocr = O.get(i, [])
        val = None
        if ra and rb and ra == rb: val = (va[0] if ra == norm(va[0]) else vb[0]); rule = 1
        elif f and f in (ra, rb): val = first; rule = 2
        elif any(x and x in (ra, rb) for x in [norm(t) for t in ocr]): val = (va[0] if ra and ra in [norm(t) for t in ocr] else vb[0]); rule = 3
        if val is not None and re.fullmatch(r'[೦-೯0-9\-–,.\s]+', val) or (val is not None and q['kind'] == 'word'):
            done.append((i, val, rule, first, q)); why[rule] += 1
        else: opn.append((i, q, first, va, vb, ocr))
    print(f'{len(done)} settled (rule 1 A=B: {why[1]}, rule 2 first reader backed: {why[2]}, rule 3 OCR backed: {why[3]}); {len(opn)} open')
    if write:
        with open(R('review', 'reread', 'ans_votes_words.tsv' if words else 'ans_votes.tsv'), 'w', encoding='utf8') as o:
            for i, val, rule, first, q in done: o.write(f'{i}\t{val}\tcertain\tvote rule {rule}\t{q["reading"]}\n')
        with open(R('review', 'votes_open_words.tsv' if words else 'votes_open.tsv'), 'w', encoding='utf8') as o:
            o.write('id\tpdf_page\tkind\tfirst_reader\tpass_A\tpass_B\tocr_numbers\tcontext\n')
            for i, q, first, va, vb, ocr in opn:
                o.write('\t'.join([i, q['pdf_page'], q['kind'], first, f'{va[0]} ({va[1]})' if va else '', f'{vb[0]} ({vb[1]})' if vb else '', ' '.join(ocr), q['context'][:90]]) + '\n')
        print('written ans_votes.tsv and votes_open.tsv')
main()
