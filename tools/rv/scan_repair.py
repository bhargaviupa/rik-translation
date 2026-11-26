#!/usr/bin/env python3
"""One runner for the repair of a scan-made volume's `[?]` marks (shared tool; Vol 25/26 first). Wraps the scan_* scripts in their order; reads volN/scan_config.json.

  python3 tools/rv/scan_repair.py init VOL --pdf PDF --first F --last L --offset O [--base B] [--first-printed P] [--body-from N] [--start M.S] [--tail PAGEFILE:PDF] [--raw PATH] [--final PATH] (config keys splice_into / splice_start: a part of a volume replaces its own section inside the volume's full file)
        writes volN/scan_config.json (F..L = page-file numbers pNNNN; O = page-file number minus printed page; B = page-file number minus PDF page, 0 if equal)
  python3 tools/rv/scan_repair.py status VOL            counts of the open `[?]` by kind (head / number / word)
  python3 tools/rv/scan_repair.py step1 VOL             free steps, in order: OCR of every page (Tesseract) → questions.tsv → words against the Wikisource text (scan_wordfix --apply)
                                                        → running heads (scan_heads --apply) → numbers/heads backed by the OCR (cleared) → questions.tsv again
  python3 tools/rv/scan_repair.py crops VOL             enlarged crops of the open numbers/heads and words (mosaics volN/work/crops/mosaic_*), the reader prompts copied to
                                                        volN/review/crops_read/ and the Agent calls to send (one reader per ~6 mosaics, pass A, then pass B)
  python3 tools/rv/scan_repair.py vote VOL              votes over the answer files (numbers: A, B, OCR; words: WA, WB) → apply → questions.tsv   (DO NOT rebuild questions.tsv between the crops and the vote:
                                                        the crop ids must still match; scan_questions ids are stable now, but check `status`)
  python3 tools/rv/scan_repair.py rebuild VOL           assemble the page files (raw, volN/work/rig_N_raw.md, not committed) and fill the Sanskrit blocks from the Wikisource index → the final file volN/html/rig_N.md (+ volN/work/pages_map.tsv)
See docs/SCAN_PIPELINE.md for the whole process and the lessons (what a first transcription must do so that none of this is needed)."""
import os, sys, json, subprocess, re, glob, shutil
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); T = os.path.dirname(os.path.abspath(__file__))
def cfgp(v): return os.path.join(ROOT, f'vol{v}', 'scan_config.json')
def run(*a, env=None):
    print('$', ' '.join(map(str, a))); r = subprocess.run([sys.executable] + [str(x) for x in a], cwd=ROOT, env=dict(os.environ, OMP_THREAD_LIMIT='1', **(env or {}))); 
    if r.returncode: sys.exit(f'step failed: {a}')
def load(v):
    if not os.path.exists(cfgp(v)): sys.exit(f'no {cfgp(v)}: run `scan_repair.py init {v} ...` first')
    return json.load(open(cfgp(v)))
def opt(a, k, d=None): return a[a.index(k) + 1] if k in a else d
def qcount(v):
    f = os.path.join(ROOT, f'vol{v}', 'review', 'questions.tsv')
    if not os.path.exists(f): return {}
    from collections import Counter
    return dict(Counter(l.split('\t')[6] for l in open(f, encoding='utf8').read().split('\n')[1:] if l.strip()))
def questions(v, c): run(f'{T}/scan_questions.py', v, c['first'], c['last'], '--offset', c['offset'])
def main():
    a = sys.argv[1:]; cmd, v = a[0], a[1]
    if cmd == 'init':
        c = {'pdf': opt(a, '--pdf'), 'first': int(opt(a, '--first')), 'last': int(opt(a, '--last')), 'offset': int(opt(a, '--offset')), 'base': int(opt(a, '--base', 0)),
             'first_printed': int(opt(a, '--first-printed', 1)), 'body_from': opt(a, '--body-from'), 'start': opt(a, '--start'), 'tail': opt(a, '--tail'), 'raw': opt(a, '--raw'), 'final': opt(a, '--final')}
        json.dump(c, open(cfgp(v), 'w'), indent=1); print('written', cfgp(v)); return
    c = load(v)
    if cmd == 'status': print(qcount(v)); return
    if cmd == 'step1':
        run(f'{T}/scan_ocr.py', 'run', v, c['pdf'], c['first'], c['last'], '--base', c['base'], '--jobs', 4)
        questions(v, c); run(f'{T}/scan_wordfix.py', v, '--apply'); run(f'{T}/scan_heads.py', v, '--apply'); questions(v, c)
        run(f'{T}/scan_ocr.py', 'numbers', v, c['first'], c['last'])
        import csv
        rr = os.path.join(ROOT, f'vol{v}', 'review'); os.makedirs(os.path.join(rr, 'reread', 'done'), exist_ok=True)
        Q = {q['id']: q for q in csv.DictReader(open(os.path.join(rr, 'questions.tsv'), encoding='utf8'), delimiter='\t')}
        n = 0
        with open(os.path.join(rr, 'reread', 'ans_ocr.tsv'), 'w', encoding='utf8') as o:
            for x in csv.DictReader(open(os.path.join(rr, 'ocr_numbers.tsv'), encoding='utf8'), delimiter='\t'):
                if x['vote'] == 'agree' and float(x['line_match']) >= 0.7 and len(re.findall(r'[೦-೯0-9]', x['reading'])) >= 2 and x['id'] in Q:
                    o.write(f"{x['id']}\t{x['reading'][:-3]}\tcertain\tconfirmed by Tesseract OCR (line match {x['line_match']})\t{Q[x['id']]['reading']}\n"); n += 1
        run(f'{T}/scan_reread.py', 'apply', v, '--write'); shutil.move(os.path.join(rr, 'reread', 'ans_ocr.tsv'), os.path.join(rr, 'reread', 'done', 'ans_ocr.txt'))
        questions(v, c); print('after step1:', qcount(v)); return
    if cmd == 'crops':
        pdf = ['--pdf', c['pdf'], '--base', c['base']] + (['--tail', c['tail']] if c['tail'] else [])
        run(f'{T}/scan_crops.py', v, '--kinds', 'number,head', '--per', 10, *pdf); run(f'{T}/scan_crops.py', v, '--kinds', 'word', '--per', 12, *pdf)
        d = os.path.join(ROOT, f'vol{v}', 'review', 'crops_read'); os.makedirs(d, exist_ok=True)
        for k in ('NUM', 'WORD', 'PAGE'):
            open(os.path.join(d, f'PROMPT_{k}.md'), 'w', encoding='utf8').write(open(os.path.join(T, 'scan_prompts', f'{k}.md'), encoding='utf8').read().replace('{VOL}', v))
        for kind, pre, ans in (('num', 'mosaic_num_', 'A'), ('word', 'mosaic_word_', 'WA')):
            M = sorted(glob.glob(os.path.join(ROOT, f'vol{v}', 'work', 'crops', pre + '*.png'))); k = len(M)
            print(f'\n{kind}: {k} mosaics. Send pass {ans} (and then a second, independent pass {"B" if kind == "num" else "WB"}) as Agent calls (sonnet, background), ~6 mosaics each, e.g.:')
            for j in range(0, k, 6):
                print(f'  "Read vol{v}/review/crops_read/PROMPT_{"NUM" if kind == "num" else "WORD"}.md and follow it exactly. Your mosaics: {pre}{j + 1:03d} … {pre}{min(j + 6, k):03d} (png and tsv in vol{v}/work/crops/). Answer file: vol{v}/review/crops_read/{ans}_{j + 1:03d}-{min(j + 6, k):03d}.tsv."')
        print('\nThe words that the first reader and pass WA read differently go into a second word pass (scan_crops.py --ids FILE --tag wordB); marks whose crop could not be found (nomatch_*.tsv) go to page-level jobs: scan_reread.py plan VOL --pages 4 --kinds head,number and PROMPT_PAGE.md.'); return
    if cmd == 'vote':
        run(f'{T}/scan_vote.py', v, '--write'); rr = os.path.join(ROOT, f'vol{v}', 'review'); run(f'{T}/scan_reread.py', 'apply', v, '--write')
        f = os.path.join(rr, 'reread', 'ans_votes.tsv')
        if os.path.exists(f): shutil.move(f, os.path.join(rr, 'reread', 'done', 'ans_votes_numbers.txt'))
        print('words: run `scan_vote.py VOL --words --write` after the WA/WB files exist, then apply; certain/likely rules are in docs/SCAN_PIPELINE.md'); questions(v, c); print(qcount(v)); return
    if cmd == 'rebuild':
        raw = c.get('raw') or f'vol{v}/work/rig_{v}_raw.md'; final = c.get('final') or f'vol{v}/html/rig_{v}.md'   # raw (blocks as markers) stays in work/ (not committed); the final file is the filled text
        os.makedirs(os.path.join(ROOT, os.path.dirname(raw)), exist_ok=True)
        asm = [f'{T}/scan_assemble.py', v, c['first'], c['last'], '--first-printed', c['first_printed']] + (['--body-from', c['body_from']] if c['body_from'] else []) + ['--out', raw]
        run(*asm)
        fill = [f'{T}/ws_fill.py', v, '--src', raw, '--out', final] + (['--start', c['start']] if c['start'] else []) + ['--write']
        run(*fill)
        # the Wikisource bhāṣya of the last Ṛk of an aṣṭaka ends with the colophon that the print also carries after the English: keep the printed one
        f = os.path.join(ROOT, final); L = open(f, encoding='utf8').read().split('\n')
        i = next((k for k, l in enumerate(L) if l.startswith('ವೇದಾರ್ಥಸ್ಯ ಪ್ರಕಾಶೇನ') and k + 3 < len(L) and L[k + 3].startswith('ಸಮಾಪ್ತಂ ಚ') and k + 6 < len(L) and 'ಇತಿ ಶ್ರೀಮದ್' in L[k + 2]), None)
        if i is not None:
            printed = any(l.startswith('ವೇದಾರ್ಥಸ್ಯ ಪ್ರಕಾಶೇನ') for l in L[i + 4:])
            if printed: del L[i:i + 4]; open(f, 'w', encoding='utf8').write('\n'.join(L)); print('removed the duplicate Wikisource colophon (the printed one stays)')
        print('final file:', final)
        if c.get('splice_into'):   # the volume's one full file was made from machine-read pages + this scan part: replace that part inside it
            tgt = os.path.join(ROOT, c['splice_into']); T2 = open(tgt, encoding='utf8').read().split('\n'); part = open(f, encoding='utf8').read().rstrip('\n').split('\n')
            if part and part[0].startswith('<!-- page'): part = part[1:]
            k = next((i for i, l in enumerate(T2) if l.startswith(c['splice_start'])), None)
            if k is None: sys.exit('splice_start not found in ' + c['splice_into'])
            open(tgt, 'w', encoding='utf8').write('\n'.join(T2[:k] + part) + '\n'); print(f'spliced {len(part)} lines into {c["splice_into"]} from line {k + 1}')
        return
    sys.exit(__doc__)
main()
