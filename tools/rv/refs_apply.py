#!/usr/bin/env python3
"""Carry out the decided reference forms of the one list in every volume and in every script (user, Nov 18 2026: uniform in the English,
the Sanskrit lines and the Kannada text).  The list decides; this script only applies it.  Run by the agent `reference-corrector`
(.claude/agents/reference-corrector.md).

  python3 tools/rv/refs_apply.py                 preview for all volumes (nothing is changed): volN/review/refs_preview.tsv + summary
  python3 tools/rv/refs_apply.py 7 14            only these volumes
  python3 tools/rv/refs_apply.py 14 --write      apply to Vol 14 (English and Kannada file), rows added to volN/review/refs_applied.tsv, line in repair_log.md
  python3 tools/rv/refs_apply.py --questions     reference numbers still marked doubtful ([?], 4-?) per volume, and whether a numerals file is there
  options: --list FILE (default rv/references.tsv) · --places FILE (default rv/reference_places.tsv) · --scripts latin,deva,kannada
           --hold "Vā.;sā." forms left alone in this run · --no-suffix (do not read a known form after an unknown first word)

What is changed: only the NAME of a work that stands directly before a reference number of two or more parts (found by the rules of
tools/rv/crossrefs.py).  The number, and every other letter, stays as it is.  A name is changed only when the list has it as a decided
mistake ("→ form" without "?"):
  Latin name          -> the list's English form                                   (Ma. Saṃ. 3-54-7  -> Ṛ. Saṃ. 3-54-7)
  Latin, lower case   -> the transliteration of the Devanagari form (it is the     (ma. saṃ. 3-54-7  -> ṛ. saṃ. 3-54-7)
                         script-made twin of a Sanskrit line, not English)
  Devanagari name     -> the list's form in Devanagari, made by script             (म. सं. ३-५४-७   -> ऋ. सं. ३-५४-७)
  Kannada name        -> the list's Kannada form                                   (ಮ. ಸಂ. ೩-೫೪-೭   -> ಋ. ಸಂ. ೩-೫೪-೭)
Indic names are recognised by their letters (transliterated, compared with the Latin rows) and by the Devanagari rows of
rv/reference_approvals.tsv.  Forms without a decision, forms the list retains (Maṃ., VII.) and forms held in the list are not touched.
A name that stands right after an opening quotation mark (printed "ಮ. ಸಂ. ೮-೧೦೨-೧೧") is a record of the print and is left alone.
Column `check` of the preview names what a reader must look at before --write: `one-word` (a name of one short word in Indic script),
`suffix` (known form after a daṇḍa or "Cf."), `dotless` (first word of the name printed without its dot), `remark` (an "as printed"/[sic] remark stands next to a name that is now corrected).
Place-by-place decisions (rv/reference_places.tsv: vol, file en|kn, line, old, new, by) are applied where `old` stands exactly once in
that line (or in exactly one line within 40 lines of it); otherwise they are reported and nothing changes.
Proof built in: a volume is written only if every digit and every "?" of both files stands exactly as before and no line is added or lost.
Numbers are corrected elsewhere: from the user's numerals file, by publish/tools/ref_check/ (NUMERAL_FILE_LESSONS.md)."""
import re, sys, os, csv, datetime, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import crossrefs as X
from crossrefs import deva_to_iast
from indic_transliteration import sanscript
DEV, KAN = '[ऀ-ॿ]', '[ಀ-೿]'
REMARK_IN = re.compile(r'\s*\[(?:sic|printed|so printed|as printed|as supplied)[^\]]*\]')
REMARK_NEAR = re.compile(r'\[sic|book prints|abbreviation|misread|"[^"\d]{1,16}\."|\[(?:reference )?as (?:printed|supplied)\]|(?:printed|supplied:?) "\D')     # a remark that speaks of the NAME (not of the number)
LET = r'A-Za-zĀāĪīŪūṚṛṢṣṆṇṬṭḌḍŚśṃḥṄṅñ\u0900-\u0963\u0970-\u097f\u0c80-\u0ce5\u0cf0-\u0cff'                       # letters of the three scripts (no digits, no daṇḍa)
PREV = re.compile('([' + LET + ']+)[ .,–-]{1,3}$')
def script_of(s): return 'deva' if re.search(DEV, s) else 'kannada' if re.search(KAN, s) else 'latin'
def to_deva(en):                                         # the Devanagari form of a list form, made from its IAST letters (as tools/rv/refs_three.py)
    return re.sub(r'(\S)्\.', r'\1.', sanscript.transliterate(en, sanscript.IAST, sanscript.DEVANAGARI))
def kn_to_deva(s): return sanscript.transliterate(s, sanscript.KANNADA, sanscript.DEVANAGARI)
def deva_to_kn(s): return sanscript.transliterate(s, sanscript.DEVANAGARI, sanscript.KANNADA)
def key(lab): return X.key(kn_to_deva(lab) if re.search(KAN, lab) else lab)

class Rules:
    def __init__(self, listfile, hold=(), suffix=True):
        rows = list(csv.DictReader(open(listfile, encoding='utf8'), delimiter='\t'))
        self.good, self.kn_of, self.mist, self.held, self.suffix = set(), {}, {}, [], suffix
        for r in rows:
            if r['status'] in ('legend', 'extra'):
                en = [f.strip() for f in r['english'].split(' or ')]; kn = [f.strip() for f in re.split(r'\s+ಅಥವಾ\s+', r['kannada'] or '')]
                for i, f in enumerate(en):
                    self.good.add(f)
                    if kn and script_of(kn[0]) == 'kannada': self.kn_of[f] = X.normlab(kn[min(i, len(kn) - 1)])
        hold = {X.normlab(h) for h in hold}
        self.hold = hold                                  # a written label named in --hold is also left alone where it is only recognised by its letters (e.g. a Kannada ಪಾ.)
        for r in rows:
            if r['status'] != 'mistake': continue
            t = r['work'].replace('→', '').strip()
            if not r['work'].startswith('→') or '?' in r['work'] or t not in self.good or X.normlab(r['english']) in hold:
                self.held.append((r['english'], r['work'])); continue
            self.mist[X.normlab(r['english'])] = t
            if r['kannada'].strip(): self.mist[X.normlab(r['kannada'])] = t
        ap = os.path.join(os.path.dirname(listfile), 'reference_approvals.tsv')        # Devanagari forms the user approved a meaning for
        if os.path.exists(ap):
            for r in csv.DictReader(open(ap, encoding='utf8'), delimiter='\t'):
                f, t = X.normlab(r['form as written']), r['approved form'].strip()
                if r['script'].startswith('Devanagari') and t in self.good and f not in hold and f not in self.mist: self.mist[f] = t
        # by letters: the key of a mistake row (and of a correct form) -> the form to use; a key that reads two ways is used by nobody
        km = collections.defaultdict(set)
        for f in self.good: km[key(f)].add(f)
        for f, t in self.mist.items(): km[key(f)].add(t)
        self.bykey = {k: next(iter(v)) for k, v in km.items() if len(v) == 1}
        self.two_ways = {k: sorted(v) for k, v in km.items() if len(v) > 1}
        self.goodkeys = {key(f) for f in self.good}
        self.tails = {key(w) for f in self.good for w in f.split()[1:]}          # Saṃ., Sū., Brā., U., Ā. …: last words of names; alone they are a name only if no other word stands before them
    def form(self, target, script, lower):
        if script == 'latin': return deva_to_iast(to_deva(target)).strip() if lower else target
        d = to_deva(target)
        if script == 'deva': return d
        return self.kn_of.get(target) or deva_to_kn(d)
    def look(self, lab):
        """lab = a regular name ('Ma. Saṃ.'); returns (new name, rule) or None"""
        sc = script_of(lab); lower = sc == 'latin' and lab == lab.lower()
        t = self.mist.get(lab); rule = 'list'
        if t is None and (sc != 'latin' or lower): t = self.bykey.get(key(lab)); rule = 'letters'
        if t is None: return None
        new = self.form(t, sc, lower)
        if X.normlab(new) == lab: return None
        if sc != 'latin' and key(new) == key(lab): return None          # only dots or spacing differ in an Indic name: left as printed
        return new, rule
    def known(self, lab):
        return lab in self.good or lab in self.mist or ((script_of(lab) != 'latin' or lab == lab.lower()) and key(lab) in self.goodkeys)

def refs_in(line):
    """every reference of the line: (start, end of the name in `line`, the name as written, number as written), by the rules of crossrefs.py"""
    cut = []; parts = []; pos = 0
    for m in REMARK_IN.finditer(line): parts.append(line[pos:m.start()]); cut.append((sum(map(len, parts)), m.end() - m.start())); pos = m.end()
    parts.append(line[pos:]); l = ''.join(parts)
    def orig(i, end=False):                              # index in the stripped line -> index in the line as it stands
        return i + sum(n for at, n in cut if at < i or (at == i and not end))
    ms = [m for m in X.REFB.finditer(l) if m.group(1) or re.match(X.DEVW, m.group(2)).group() in X.FIRSTW]
    starts = {m.start(3) for m in ms}
    out = [(m.start(2), m.end(2), m.group(2), m.group(3), m.start(3)) for m in ms]
    out += [(m.start(1), m.end(1), m.group(1), m.group(2), m.start(2)) for m in X.REF.finditer(l) if m.start(2) not in starts]
    for rx in (X.REFL, X.REFV):
        if rx is X.REFL: extra = [(m.start(1), m.end(2), m.group(1) + '. ' + m.group(2), m.group(3), m.start(3)) for m in rx.finditer(l)]
        else: extra = [(m.start(1), m.end(1), m.group(1), m.group(2), m.start(2)) for m in rx.finditer(l)]
        taken = {x[4] for x in extra}; out = [t for t in out if t[4] not in taken] + extra
    res = []
    for a, b, name, num, ns in sorted(out, key=lambda t: t[4]):
        b = a + len(l[a:b].rstrip())                     # the name ends at its last dot; what stands between it and the number is kept
        a0 = a
        while a > 0 and re.match('[' + LET + ']', l[a - 1]) and script_of(l[a - 1]) == script_of(l[a]): a -= 1      # the rule cut a long word ("ಮುಗ್ವಿಧಾನ."): read it whole
        if a < a0: name = l[a:a0] + name
        dg = [m.end() for m in re.finditer(r'[0-9०-९೦-೯][^' + LET + r']*', l[a:b])]       # "೫. ಸಂ.": a number is no part of a name (the rule for Kannada takes digits as letters)
        if dg: a += dg[-1]; name = l[a:b]
        if not name.strip(): continue
        res.append((orig(a), orig(b, True), l[a:b], name, num, orig(ns)))
    return res

HEAD_KN = re.compile(r'(?:ಮಂ|मं|Maṃ)\.?\s*[0-9०-९೦-೯]')        # "[ಮಂ. ೩. ಅ ೫. ಸೂ. ೫.೫]": a running head; its ಸೂ. is the sūkta
def fix_line(line, R, scripts, prev=''):
    """returns (new line, [changes]); a change = (script, as written, number, becomes, rule, check); prev = the line before (a name can be cut by the line end)"""
    if re.search(r'Running head|\(Header:|Page header', line) or HEAD_KN.search(line): return line, []
    ch = []; out = line; shift = 0
    for a, b, raw, name, num, ns in refs_in(line):
        lab = X.normlab(name)
        if not lab or X.key(lab) in X.STOP and len(lab.split()) == 1: continue
        if re.search(r'["“]\s?$', line[:a]): continue    # "…" opened just before the name: a remark quoting what the print has; it stays as the record
        check = []; words = lab.split(); skip = 0
        if len(words) == 1 and key(lab) in R.tails:      # "ma saṃ. 10-85-26", "Kāṭhaka Saṃ. 21-2": the word before it (without a dot) belongs to the name
            pm = PREV.search(line[:a])
            if re.search(r'[0-9०-९೦-೯][.)]?\s*$', line[:a]): continue                     # "೫. ಸಂ. ೫-೨೫": a misread first word; not a bare name
            if not line[:a].strip(' >(*[') and re.search('[' + LET + r']\.?\s*$', prev): continue      # the name began on the line before ("(ಪಾ." / "ಸೂ. ೫-೪-೫೬)")
            if pm:
                lab2 = X.normlab(pm.group(1) + '. ' + name)
                if not (R.known(lab2) or R.look(lab2)): continue          # a name the list does not have: not ours to change
                a = pm.start(1); raw = line[a:b]; lab = lab2; words = lab.split(); check.append('dotless')
        hit = R.look(lab)
        if hit is None and R.suffix and not R.known(lab) and '[' not in line[a:b]:
            for i in range(1, len(words)):               # a known name after words that are not a name: a daṇḍa or "Cf." ("वा. ।. पा. 3-4-83", "Cf. Ma. Saṃ. …")
                if not (re.fullmatch(r'[।॥]\.', words[i - 1]) or X.key(words[i - 1]) in X.STOP): continue
                sub = ' '.join(words[i:])
                if len(words) - i == 1 and key(sub) in R.tails: break
                if R.known(sub) or R.look(sub): hit = R.look(sub); skip = i; check.append('suffix')
                break
        if hit is not None and lab in R.hold: hit = None
        if hit is None: continue
        new, rule = hit; sc = script_of(lab)
        if sc not in scripts: continue
        if skip:                                         # keep the first word(s) as they stand
            m = re.match(r'(?:\S+\s*){%d}' % skip, line[a:b]);
            if not m: continue
            a += m.end(); raw = line[a:b]
        if sc != 'latin' and len(words) - skip == 1 and len(X.key(' '.join(words[skip:]))) <= 2: check.append('one-word')
        if REMARK_NEAR.search(line[max(0, a - 40):ns + 90]) or '[' in raw: check.append('remark')
        out = out[:a + shift] + new + out[b + shift:]; shift += len(new) - (b - a)
        ch.append((sc + ('-twin' if sc == 'latin' and lab == lab.lower() else ''), raw, num, new, rule, ' '.join(check)))
    return out, ch

def files_of(v):
    d = os.path.join(ROOT, f'vol{v}')
    return [(k, p) for k, p in (('en', os.path.join(d, f'Rigveda_Samhita_Vol{v}_English_Translation.md')), ('kn', os.path.join(d, f'Rigveda_Samhita_Vol{v}_Kannada_Text.md'))) if os.path.exists(p)]

def places(v, placefile, texts):
    """place-by-place decisions for this volume; texts = {'en': [lines], 'kn': [lines]} changed in place; returns report rows"""
    rep = []
    if not os.path.exists(placefile): return rep
    for r in csv.DictReader(open(placefile, encoding='utf8'), delimiter='\t'):
        if not (r.get('vol') or '').strip().isdigit() or int(r['vol']) != v: continue
        k = r['file'].strip(); L = texts.get(k); old, new = r['old'], r['new']
        if L is None or not old or old == new: rep.append((k, r['line'], 'place', old, '', new, 'NOT APPLIED: no such file or empty row', '')); continue
        n = int(r['line']) - 1 if r['line'].strip().isdigit() else -1
        cand = [n] if 0 <= n < len(L) and L[n].count(old) == 1 else [i for i in range(max(0, n - 40), min(len(L), n + 41)) if L[i].count(old) == 1] if n >= 0 else [i for i, x in enumerate(L) if old in x]
        if len(cand) != 1 or L[cand[0]].count(old) != 1:
            done = n >= 0 and any(new in L[i] for i in range(max(0, n - 40), min(len(L), n + 41)))
            rep.append((k, r['line'], 'place', old, '', new, 'already as decided' if done else f'NOT APPLIED: "old" found in {len(cand)} lines', '')); continue
        i = cand[0]; L[i] = L[i].replace(old, new); rep.append((k, i + 1, 'place', old, '', new, 'place: ' + r.get('by', ''), ''))
    return rep

def run(vols, R, placefile, scripts, write):
    total = collections.Counter(); today = datetime.date.today().isoformat()
    for v in vols:
        fs = files_of(v)
        if not fs: continue
        texts = {k: open(p, encoding='utf8').read().split('\n') for k, p in fs}; before = {k: list(L) for k, L in texts.items()}
        rows = []; c = collections.Counter(); pair = {'en': collections.Counter(), 'kn': collections.Counter()}
        for k, L in texts.items():
            for i, l in enumerate(L):
                if l.startswith('#') or '**Progress note:**' in l: continue
                n, ch = fix_line(l, R, scripts, L[i - 1] if i else '')
                for sc, raw, num, new, rule, check in ch:
                    ctx = re.sub(r'\s+', ' ', l[max(0, l.find(raw) - 60):l.find(raw) + len(raw) + 70])
                    rows.append((k, i + 1, sc, raw, num, new, rule, check, ctx)); c[k + ' ' + sc] += 1; c['check'] += bool(check)
                    if (k == 'kn') == (sc == 'kannada') and not sc.endswith('twin'): pair[k][(R.bykey.get(key(X.normlab(new)), new), re.sub(r'\D+', '-', num.translate(X.DIG)))] += 1
                L[i] = n
        prow = places(v, placefile, texts); rows += [r + ('',) for r in prow]; c['places'] += sum(1 for r in prow if r[6].startswith('place'))
        notp = [r for r in prow if r[6].startswith('NOT APPLIED')]
        # a reference of the Kannada file stands in the English file too (in Devanagari in a Sanskrit line, in Latin in the English): how many change on one side only
        odd = sorted((pair['kn'] - pair['en']).items()) if 'kn' in texts else []
        rev = os.path.join(ROOT, f'vol{v}', 'review'); os.makedirs(rev, exist_ok=True); prev = os.path.join(rev, 'refs_preview.tsv')
        head = 'file\tline\tscript\tas written\tnumber\tbecomes\trule\tcheck\ttext'
        digits = lambda L: re.sub(r'[^0-9०-९೦-೯?]', '', '\n'.join(L))
        bad = [k for k in texts if len(texts[k]) != len(before[k]) or digits(texts[k]) != digits(before[k])]
        if bad:                                          # proof on every run: not one digit or question mark is added, lost or moved, and no line is added or lost
            print(f'Vol {v}: STOPPED, nothing written: the digits of the {"/".join(bad)} file would change (a place decision that touches a number? numbers come only from the numerals file)'); continue
        if write:
            if rows:
                for k, p in fs:
                    if texts[k] != before[k]: open(p, 'w', encoding='utf8').write('\n'.join(texts[k]))
                ap = os.path.join(rev, 'refs_applied.tsv'); new_file = not os.path.exists(ap)
                with open(ap, 'a', encoding='utf8') as f:
                    if new_file: f.write('date\t' + head + '\n')
                    for r in rows: f.write(today + '\t' + '\t'.join(map(str, r)) + '\n')
                with open(os.path.join(rev, 'repair_log.md'), 'a', encoding='utf8') as g:
                    g.write(f'- {today}: tools/rv/refs_apply.py: reference names made uniform by the one list ({os.path.relpath(R.listfile, ROOT)}), numbers untouched: '
                            + ', '.join(f'{k} {n}' for k, n in sorted(c.items()) if k != 'check' and n) + f'; every change is a row of review/refs_applied.tsv.\n')
            if os.path.exists(prev): os.remove(prev)
            fxp = os.path.join(ROOT, f'vol{v}', 'data', 'import_fixes.json')         # a volume with unit data: its stored repairs quote the text as it was; they follow the change
            if rows and os.path.exists(fxp):
                import json
                fx = json.load(open(fxp, encoding='utf8')); nfx = 0
                for kk in ('replace_en', 'replace_sub'):
                    for rp in fx.get(kk, []):
                        for f_ in ('old', 'new'):
                            if isinstance(rp.get(f_), str):
                                n_ = '\n'.join(fix_line(x, R, scripts)[0] for x in rp[f_].split('\n'))
                                if n_ != rp[f_]: rp[f_] = n_; nfx += 1
                if nfx: json.dump(fx, open(fxp, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
                print(f'   Vol {v} has unit data: {nfx} quoted texts of data/import_fixes.json follow the change; now run `python3 -m rv structure {v} --mandalas …` and `python3 -m rv import {v}` (the two proofs of import_report.md must read as before)')
            elif rows and os.path.exists(os.path.join(ROOT, f'vol{v}', 'data', 'units.jsonl')):
                print(f'   Vol {v} has unit data: now run `python3 -m rv structure {v} --mandalas …` and `python3 -m rv import {v}`')
        elif not rows:
            if os.path.exists(prev): os.remove(prev)
        else:                                            # the preview is working paper (in .gitignore): it is never committed and does not disturb the audit
            with open(prev, 'w', encoding='utf8') as f:
                f.write(head + '\n')
                for r in rows: f.write('\t'.join(map(str, r)) + '\n')
        print(f'Vol {v}: ' + (', '.join(f'{k} {n}' for k, n in sorted(c.items()) if n) or 'nothing to change') + ('  [written]' if write and rows else ''))
        if odd: print(f'   changed in the Kannada file with no matching change in the English file: {sum(x for _, x in odd)} references (the English already had the right form, or reads the number differently), e.g. ' + '; '.join(f'{t} {n}' for (t, n), x in odd[:4]))
        for r in notp: print(f'   place {r[0]} line {r[1]}: {r[3]!r} {r[6]}')
        total.update(c)
    print('ALL: ' + (', '.join(f'{k} {n}' for k, n in sorted(total.items()) if n) or 'nothing to change'))

QMARK = re.compile(r'^[^A-Za-z(]{0,12}(?:\(?as read\)?\s*)?\[\?\]|^\S*\?')
def questions(vols):
    """reference numbers still marked doubtful in the English file, per volume (REFERENCES_OPEN_NUMBERS.tsv)"""
    out = []; print('vol\tdoubtful reference numbers\tnumerals files (volN/numerals/*.xlsx)')
    for v in vols:
        fs = dict(files_of(v))
        if 'en' not in fs: continue
        n = 0
        for i, l in enumerate(open(fs['en'], encoding='utf8').read().split('\n')):
            if '?' not in l: continue
            got = []
            for a, b, raw, name, num, ns in refs_in(l):
                tail = l[ns + len(num):ns + len(num) + 30]; qm = QMARK.match(tail)
                if qm: out.append((v, i + 1, X.normlab(name), num + qm.group(), re.sub(r'\s+', ' ', l[max(0, a - 50):ns + 60]))); n += 1; got.append((ns, ns + len(num) + qm.end()))
            for m in re.finditer(r'(?<![\d-])\d+(?:-\d+)*-\?+', l):
                if any(x <= m.start() < y for x, y in got): continue
                out.append((v, i + 1, '', m.group(), re.sub(r'\s+', ' ', l[max(0, m.start() - 50):m.end() + 40]))); n += 1
        d = os.path.join(ROOT, f'vol{v}', 'numerals'); x = sorted(f for f in os.listdir(d) if f.endswith('.xlsx') and 'Numerals' in f) if os.path.isdir(d) else []
        print(f'{v}\t{n}\t{len(x)}' + (': ' + ', '.join(x[:3]) + (' …' if len(x) > 3 else '') if x else ''))
    with open(os.path.join(ROOT, 'REFERENCES_OPEN_NUMBERS.tsv'), 'w', encoding='utf8') as f:
        f.write('vol\tline\twork\tnumber as it stands\ttext\n')
        for r in out: f.write('\t'.join(map(str, r)) + '\n')
    print(f'{len(out)} places written to REFERENCES_OPEN_NUMBERS.tsv')

if __name__ == '__main__':
    a = sys.argv[1:]; opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    vals = {a[i + 1] for i, x in enumerate(a[:-1]) if x in ('--list', '--places', '--scripts', '--hold')}
    vols = [int(x) for x in a if x.isdigit() and x not in vals] or list(range(1, 30))
    if '--questions' in a: questions(vols); sys.exit()
    lf = os.path.abspath(opt('--list', os.path.join(ROOT, 'rv', 'references.tsv')))
    R = Rules(lf, hold=[h for h in (opt('--hold') or '').split(';') if h.strip()], suffix='--no-suffix' not in a); R.listfile = lf
    print(f'list {os.path.relpath(lf, ROOT)}: {len(R.good)} forms to use, {len(R.mist)} decided mistakes'
          + (f'; not applied (no decision, "?" or target not in the list): {len(R.held)}' if R.held else '')
          + (f'; letters that read two ways (used only where the form is written exactly as in the list): ' + ', '.join(f'{k}={"/".join(v)}' for k, v in sorted(R.two_ways.items())) if R.two_ways else ''))
    run(vols, R, os.path.abspath(opt('--places', os.path.join(ROOT, 'rv', 'reference_places.tsv'))), set((opt('--scripts') or 'latin,deva,kannada').split(',')), '--write' in a)
