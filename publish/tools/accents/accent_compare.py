#!/usr/bin/env python3
"""Compare the Saṃhitā blocks of a volume with the accented reference, Ṛk by Ṛk (report only; changes nothing).

  python3 publish/tools/accents/accent_compare.py VOL --sukta A B [--mandala M] [--html FILE]

Layouts understood: label line `**॥ संहितापाठः ॥**` or `**॥ Saṃhitā-pāṭhaḥ ॥**`, then `> ` Devanagari lines (the block ends at the first line that does not
start with `> ` followed by Devanagari); the Ṛk number is the number in `॥N॥` that ends the block. Sūkta numbers are followed from the first block
(--sukta A) and increase when the Ṛk number falls back to 1. Blocks and reference verses are paired by position and Ṛk number.
Classes per Ṛk (volN/review/accent_report.tsv): EQUAL (same letters and accents), ACCENT_DIFF (same letters, different or missing accents),
LETTER_DIFF (letters differ; subtype NASAL if only anusvāra/nasal-conjunct), NOT_FOUND (no reference verse for the block).
Also counts, by their labels, Pada-pāṭha lines that carry accent marks. The reference file is for personal study: keep it out of public repos."""
import os, re, sys, glob, difflib, argparse, importlib.util, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
def _load(name):
    sp = importlib.util.spec_from_file_location(name, os.path.join(ROOT, 'publish', 'tools', 'accents', name + '.py')); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
acc = _load('accents'); av = _load('accent_volume')
AC = acc.AC
LABEL = re.compile(r'॥\s*(संहितापाठः|Saṃhitā-pāṭhaḥ)\s*॥')
PADA = re.compile(r'॥\s*(पदपाठः|Pada-pāṭhaḥ)\s*॥')
DEVD = str.maketrans('०१२३४५६७८९', '0123456789')
def norm_accents(s):
    s = s.replace('‌', '').replace('‍', '').replace('[?]', '')
    s = re.sub('(?<![१३])([' + AC + '])([ःं])', r'\2\1', s)
    return re.sub(r'\s+', ' ', s).strip()
def body(s):   # without danda, verse number, spaces
    s = re.sub(r'॥\s*[०-९0-9]+\s*॥?', ' ', s)
    return re.sub(r'[।॥\s]+', '', norm_accents(s))
def lk(s):   # letters only, with anusvāra/nasal-conjunct/final-m styles unified
    s = re.sub(r'म्(?=[\s।॥]|$)', 'ं', acc.strip_ac(s)); return acc.canon(s)
def blocks(L):
    """-> [(first_line_index, [indexes], rik_number or None)]"""
    out = []; i = 0
    while i < len(L):
        if L[i].startswith('**') and LABEL.search(L[i]):
            j = i + 1
            while j < len(L) and (not L[j].strip() or L[j].startswith('#') or L[j].strip() == '---' or (L[j].startswith('*') and not L[j].startswith('> '))): j += 1
            k = j
            while k < len(L) and L[k].startswith('> ') and re.search('[ऀ-ॿ]', L[k]) and not L[k].startswith('> *'): k += 1
            idx = list(range(j, k)); num = None
            if idx:
                m = re.search(r'॥\s*([०-९0-9]+)\s*॥\s*(\[accent \?\])?\s*$', L[idx[-1]].strip())
                if m: num = int(m.group(1).translate(DEVD))
            out.append((i, idx, num)); i = max(k, i + 1)
        else: i += 1
    return out
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('vol', type=int); ap.add_argument('--sukta', nargs=2, type=int, required=True); ap.add_argument('--mandala', type=int, default=1); ap.add_argument('--html', nargs='*'); ap.add_argument('--file')
    a = ap.parse_args()
    files = a.html or [os.path.join(ROOT, 'refs', 'mandala', f'rv_mandala{a.mandala}.html')]
    REF = []
    for f in files: REF += av.read_ref(f)
    ref = collections.OrderedDict()
    for rid, line in REF:
        if rid[0] == a.mandala and a.sukta[0] <= rid[1] <= a.sukta[1]: ref.setdefault(rid, []).append(line)
    vf = a.file or av.vol_file(a.vol); L = open(vf, encoding='utf8').read().split('\n')
    bl = blocks(L); print(f'reference: {len(ref)} verses in sūktas {a.sukta[0]}–{a.sukta[1]} of maṇḍala {a.mandala}; file: {len(bl)} Saṃhitā blocks')
    rows = []; counts = collections.Counter(); keys = list(ref); used = 0
    for n, (hi, idx, num) in enumerate(bl):
        rid = keys[n] if n < len(keys) else None
        ours = ' '.join(re.sub(r'\s*\[accent \?\]\s*$', '', L[m][2:]) for m in idx)
        note = '' if (rid is not None and num == rid[2]) else 'NUMBER_MISMATCH(file %s, ref %s)' % (num, rid[2] if rid else None)
        if rid is None: cls = 'NOT_FOUND'; sub = ''
        else:
            r = ' '.join(ref[rid]); used += 1
            if body(ours) == body(r): cls = 'EQUAL'; sub = ''
            elif body(acc.strip_ac(ours)) == body(acc.strip_ac(r)): cls = 'ACCENT_DIFF'; sub = 'unaccented' if not any(c in AC for c in ours) else ''
            else: cls = 'LETTER_DIFF'; sub = 'NASAL' if lk(ours) == lk(r) else ''
        if note: sub = (sub + ' ' + note).strip()
        counts[cls] += 1
        rows.append((hi + 1, f'{rid[1]}.{rid[2]}' if rid else '?', '', cls, sub, ours[:160], ' '.join(ref[rid])[:160] if rid else ''))
    seen = set(keys[:len(bl)])
    missing = [r for r in ref if r not in seen]
    print('file blocks by class:', dict(counts)); print('reference verses without a block in the file:', len(missing), ['%d.%d' % (r[1], r[2]) for r in missing][:20])
    rd = os.path.join(ROOT, f'vol{a.vol}', 'review'); os.makedirs(rd, exist_ok=True)
    with open(os.path.join(rd, 'accent_report.tsv'), 'w', encoding='utf8') as o:
        o.write('line\trik\treference_start\tclass\tsubtype\tours\treference\n')
        for r in rows: o.write('\t'.join(map(str, r)) + '\n')
        for r in missing: o.write(f'\t{r[1]}.{r[2]}\t\tNO_BLOCK_IN_FILE\t\t\t{" ".join(ref[r])[:120]}\n')
    # Pada-pāṭha lines with accents
    n = 0; tot = 0
    for i, l in enumerate(L):
        if l.startswith('**') and PADA.search(l):
            j = i + 1
            while j < len(L) and not L[j].strip(): j += 1
            while j < len(L) and L[j].startswith('> ') and not L[j].startswith('> *'):
                if re.search('[ऀ-ॿ]', L[j]): tot += 1; n += any(c in AC for c in L[j])
                j += 1
    print(f'Pada-pāṭha lines: {tot}, with accent marks: {n}')
if __name__ == '__main__': main()
