#!/usr/bin/env python3
"""Replace the Saṃhitā lines of Ṛks that differ from the accented reference by the reference's lines (user decision, Vol 2, Nov 17 2026).

  python3 publish/tools/accents/accent_replace.py VOL --sukta A B [--mandala M] [--write]

For every block that accent_compare.py classes ACCENT_DIFF or LETTER_DIFF: our lines (`> …`) are replaced by the reference verse, cut at its dandas into
as many lines as ours has; each line but the last ends ` ।`, the last ends with our own ` ॥N॥`; accent marks standing before a visarga/anusvāra are moved after it (project rule, as accents.transfer does); a trailing `[accent ?]` tag goes (its question is answered by the
reference). Equal blocks are never touched. Where the number of reference halves differs from our line count, nothing is changed and the place is listed.
Log: volN/review/verse_corrections.tsv (line, Ṛk, class, old lines, new lines)."""
import os, re, sys, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import accent_compare as ac
acc, av, ROOT, AC = ac.acc, ac.av, ac.ROOT, ac.AC
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('vol', type=int); ap.add_argument('--sukta', nargs=2, type=int, required=True); ap.add_argument('--mandala', type=int, default=1); ap.add_argument('--write', action='store_true'); a = ap.parse_args()
    REF = av.read_ref(os.path.join(ROOT, 'refs', 'mandala', f'rv_mandala{a.mandala}.html'))
    ref = collections.OrderedDict()
    for rid, line in REF:
        if rid[0] == a.mandala and a.sukta[0] <= rid[1] <= a.sukta[1]: ref.setdefault(rid, []).append(line)
    keys = list(ref); vf = av.vol_file(a.vol); L = open(vf, encoding='utf8').read().split('\n'); bl = ac.blocks(L)
    assert len(bl) == len(keys), 'verse count differs from the reference'
    log = []; skipped = []; changed = 0
    for n, (hi, idx, num) in enumerate(bl):
        rid = keys[n]
        assert num == rid[2], ('number mismatch', hi + 1, num, rid)
        ours = ' '.join(re.sub(r'\s*\[accent \?\]\s*$', '', L[m][2:]) for m in idx); r = ' '.join(ref[rid])
        if ac.body(ours) == ac.body(r): continue
        r = re.sub('(?<![१३])([' + AC + '])([ःं])', r'\2\1', r)     # project rule: the mark stands after visarga/anusvāra
        halves = [h.strip() for h in re.split('[।॥]', r) if h.strip()]
        if len(halves) != len(idx): skipped.append((hi + 1, rid, len(halves), len(idx))); continue
        tail = re.search(r'(॥\s*[०-९0-9]+\s*॥)', L[idx[-1]]).group(1)
        new = [h + ' ।' for h in halves[:-1]] + [halves[-1] + ' ' + tail]
        old = [L[m] for m in idx]
        log.append((idx[0] + 1, f'{rid[1]}.{rid[2]}', 'LETTER_DIFF' if ac.body(acc.strip_ac(ours)) != ac.body(acc.strip_ac(r)) else 'ACCENT_DIFF', ' ⏎ '.join(o[2:] for o in old), ' ⏎ '.join(new)))
        for m, t in zip(idx, new): L[m] = '> ' + t
        changed += 1
    print(f'replaced {changed} Ṛks; not changed (reference halves != our lines): {skipped}')
    if a.write:
        open(vf, 'w', encoding='utf8').write('\n'.join(L))
        rd = os.path.join(ROOT, f'vol{a.vol}', 'review')
        with open(os.path.join(rd, 'verse_corrections.tsv'), 'w', encoding='utf8') as o:
            o.write('line\trik\tclass\told lines\tnew lines\n')
            for r in log: o.write('\t'.join(map(str, r)) + '\n')
        for s in skipped: print('SKIPPED', s)
if __name__ == '__main__': main()
