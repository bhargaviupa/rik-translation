#!/usr/bin/env python3
"""Go through the user's numeral file row by row (page, line, value, column E Kannada context) and align it with the md numerals
irrespective of [?]: per file page, monotone alignment (reading order kept) of file rows to md numerals (md pages P-1..P+1),
score = digit similarity + context similarity (column E transliterated vs the text before the md numeral) + reference-type hint.
Report only (xlsx); the md is never changed.
  python3 numeral_align_all.py --md MD --num XLSX --out XLSX"""
import argparse, re, sys, unicodedata, collections
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from rapidfuzz import fuzz
from indic_transliteration.sanscript import transliterate
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "translit"))
from add_iast import deva_to_iast
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); K2A = str.maketrans("೦೧೨೩೪೫೬೭೮೯", "0123456789"); DEV = re.compile(r"[ऀ-ॿ]")
REF = re.compile(r"(\[?[०-९0-9]+\]?(?:[ ]?[-–.,][ ]?\[?[०-९0-9]+\]?)+)(\s*\[\?\])?")
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
def fold(t):
    return "".join("v" if c == "w" else c for c in (ch.lower() for ch in unicodedata.normalize("NFD", t) if not unicodedata.combining(ch)) if "a" <= c <= "z")
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
def digsim(a, b):
    if b.endswith("-?"):   # incomplete md token '4-?' : known prefix against the file's first parts; the file must have more parts
        kn = b[:-2].split("-"); fv = a.split("-")
        if len(fv) <= len(kn): return 0.0
        x, y = "-".join(kn), "-".join(fv[:len(kn)])
        return max(0.0, 1 - lev(x, y) / max(len(x), len(y))) - 0.05
    pa, pb = a.split("-"), b.split("-"); s = "-".join(pa); t = "-".join(pb)
    return max(0.0, 1 - lev(s, t) / max(len(s), len(t))) - (0.15 if len(pa) != len(pb) else 0)
# reference-type hints: file context (Kannada) vs md text before the numeral
KT = [("ನಿ.", "ni"), ("ಪಾ.", "pa"), ("ಸೂ", "su"), ("ಉಣಾ", "un"), ("ಖು", "r"), ("ಋ", "r"), ("ಐ.", "ai")]
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
frows = collections.defaultdict(list)
for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
    pg, ln, pat, eng, ctx = r[:5]
    v = "-".join(parts(str(eng)))
    if not isinstance(pg, int) or len(v.split("-")) < 2: continue
    k = str(ctx or "").translate(K2A)
    try: lat = fold(transliterate(k, "kannada", "iast"))
    except Exception: lat = ""
    frows[pg].append(dict(page=pg, line=ln, val=v, raw=str(eng), ctx=str(ctx or ""), f=lat))
# Adjacent plain numbers ("೧೧೯, ೧೨೪, ೧೨೫", "೫ ಮತ್ತು ೬") are not listed as rows in the user's file: extract them from the Kannada context (column E)
ADJ = re.compile(r"(?<![\d\-.])\d+(?:\s*(?:,|ಮತ್ತು|ಹಾಗೂ|ಅಥವಾ)\s*\d+)+(?![\d\-.])")
seen_ctx = {}
for pg, rl in list(frows.items()):
    for f in rl: seen_ctx.setdefault((pg, f["line"]), f)
extra = 0
for (pg, ln), f in seen_ctx.items():
    have = {x["val"] for x in frows[pg] if x["line"] == ln}
    for m in ADJ.finditer(f["ctx"].translate(K2A)):
        v = "-".join(re.findall(r"\d+", m.group(0)))
        if len(v.split("-")) >= 2 and v not in have:
            have.add(v); extra += 1
            frows[pg].append(dict(page=pg, line=ln, val=v, raw=m.group(0), ctx=f["ctx"], f=f["f"], adj=True))
EXT = re.compile(r"(\d+(?:[-.]\d+)+)((?:\s*(?:,|ಮತ್ತು|ಹಾಗೂ)\s*\d+(?![\d\-.]))+)")
ext = 0
for (pg, ln), f in seen_ctx.items():
    have = {x["val"] for x in frows[pg] if x["line"] == ln}
    for m in EXT.finditer(f["ctx"].translate(K2A)):
        base = re.findall(r"\d+", m.group(1))
        for t in re.findall(r"\d+", m.group(2)):
            v = "-".join(base[:-1] + [t])
            if v not in have and len(base) >= 2:
                have.add(v); ext += 1
                frows[pg].append(dict(page=pg, line=ln, val=v, raw=m.group(0), ctx=f["ctx"], f=f["f"], adj=True))
print("extra file rows from adjacent plain numbers in column E:", extra, "; from 'ref, N' / 'ref ಮತ್ತು N' extensions:", ext)
mrows = collections.defaultdict(list); cur = None; printed = None; seq = 0
for n, l in enumerate(open(a.md, encoding="utf8").read().split("\n"), 1):
    m = re.match(r"#+\s*(?:Page|Printed p\.)\s+(\w+)\s*\(PDF\s*(\d+)", l)
    if m: printed, cur = m.group(1), int(m.group(2))
    if cur is None or l.startswith("|") or l.startswith("#"): continue
    segs = []
    for m in REF.finditer(l):
        full = m.group(1)
        if re.search(r",\s", full):   # comma list of references ('3-54-20, 5-69-3'): one token per segment with >= 2 parts
            off = 0
            segl = re.split(r",\s+", full)
            if all(len(parts(sg)) == 1 for sg in segl): segs.append((m.start(), full, m.group(2), m)); continue   # plain list "119, 124, 125": one token
            for seg in segl:
                if len(parts(seg)) >= 2: segs.append((m.start() + full.index(seg, off), seg, m.group(2) if seg is full.split(",")[-1] else None, m))
                off += len(seg)
        else: segs.append((m.start(), full, m.group(2), m))
    EXTM = re.compile(r"^((?:\s*(?:,|and|&)\s*\[?\d+\]?(?![\d\-.]))+)")
    more = []
    for st, tokt, qq, m in segs:
        if len(parts(tokt)) >= 2 and "," not in tokt:
            tail = EXTM.match(l[st + len(tokt):])
            if tail:
                base = parts(tokt)
                for t in re.findall(r"\d+", tail.group(1)): more.append((st, "-".join(base[:-1] + [t]), None, m))
    segs += more
    INCT = re.compile(r"(?<![\d\-.])([०-९0-9]+(?:\s*-\s*[०-९0-9]+)*)\s*-\s*\?+")
    for mi in INCT.finditer(l):
        if not any(sg[0] <= mi.start() < sg[0] + len(sg[1]) for sg in segs): segs.append((mi.start(), mi.group(0), None, mi, True))
    segs = [sg if len(sg) == 5 else sg + (False,) for sg in segs]
    segs.sort(key=lambda sg: sg[0])
    for st, tokt, qq, m, inc in segs:
        ps = parts(tokt)
        if inc: ps = ps + ["?"]
        elif len(ps) < 2: continue
        pre = l[max(0, st - 110): st]; post = l[st + len(tokt): st + len(tokt) + 40]
        try: lat = fold(deva_to_iast(pre + " " + post))
        except Exception: lat = fold(pre + post)
        v = "-".join(ps)
        dup = next((k for k in reversed(mrows[cur][-12:]) if k["val"] == v and n - k["last"] <= 8), None)
        if dup:   # same reference repeated on the IAST twin / English rendering: count once
            dup["last"] = n; dup["q"] = dup["q"] or bool(qq); dup["occ"] += 1; continue
        seq += 1
        mrows[cur].append(dict(last=n, occ=1, seq=seq, line=n, printed=printed, val="-".join(ps), q=bool(qq), tok=tokt.strip() + (" [?]" if qq else ""), f=lat))
def score(f, m):
    d = digsim(f["val"], m["val"])
    c = fuzz.partial_ratio(f["f"][-60:], m["f"]) / 100 if f["f"] and m["f"] else 0
    pos = max(0.0, 1 - abs(f["rank"] - m["rank"]))   # approximate line position: rank on the page (0..1); neighbour pages sit outside 0..1
    return 0.55 * d + 0.30 * c + 0.15 * pos, d, c
res = []; mmap = {}; pageM = {}; pageF = {}
for P in sorted(frows):
    F = sorted(frows[P], key=lambda r: r["line"]); M = []
    for k, f in enumerate(F): f["rank"] = (k + 0.5) / len(F)
    for p in (P - 1, P, P + 1):
        mp = mrows.get(p, [])
        for k, m in enumerate(mp): m["rank"] = (k + 0.5) / len(mp) + (p - P)
        M += mp
    M.sort(key=lambda m: m["seq"])
    n, mm = len(F), len(M); S = [[score(F[i], M[j]) for j in range(mm)] for i in range(n)]
    TH = 0.5
    dp = [[0.0] * (mm + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(mm - 1, -1, -1):
            s = S[i][j][0]
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1], (s + dp[i + 1][j + 1]) if s >= TH else -1)
    i = j = 0; al = {}
    while i < n and j < mm:
        s = S[i][j][0]
        if s >= TH and abs(dp[i][j] - (s + dp[i + 1][j + 1])) < 1e-9: al[i] = j; i += 1; j += 1
        elif abs(dp[i][j] - dp[i + 1][j]) < 1e-9: i += 1
        else: j += 1
    pageM[P] = M; pageF[P] = [F[i] for i in range(n) if i not in al]
    for i, f in enumerate(F):
        if i in al:
            mmap.setdefault(id(M[al[i]]), (f, S[i][al[i]]))
            m = M[al[i]]; s, d, c = S[i][al[i]]
            st = "SAME" if f["val"] == m["val"] and not m["q"] else ("SAME but md has [?]" if f["val"] == m["val"] else "DIFFERENT")
            res.append((P, f, m, st, round(s, 2), round(c, 2)))
        else: res.append((P, f, None, "NOT FOUND in md", 0, 0))
cnt = collections.Counter(r[3] for r in res); print(len(res), "file rows;", dict(cnt))
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "file rows vs md"
ws.append(["PDF page", "file line", "FILE value (correct)", "md printed page", "md line", "MD value", "md token", "status", "score", "context score", "file context (col E)", "YOUR ANSWER"])
for P, f, m, st, s, c in res:
    ws.append([P, f["line"], f["val"], m["printed"] if m else "", m["line"] if m else "", m["val"] if m else "", m["tok"] if m else "", st, s, c, f["ctx"][:100], ""])
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496"); c.alignment = Alignment(wrap_text=True, vertical="top")
for i, w in enumerate([8, 8, 16, 8, 8, 16, 18, 20, 7, 8, 60, 20]): ws.column_dimensions["ABCDEFGHIJKL"[i]].width = w
ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
ws2 = wb.create_sheet("md numerals vs file")
ws2.append(["PDF page", "printed", "md line", "MD value", "md token", "status", "FILE value", "file line", "score", "context", "closest UNMATCHED file rows on this page (value | line)", "text in md", "YOUR ANSWER"])
nst = collections.Counter()
for P in sorted(mrows):
    for m in mrows[P]:
        hit = mmap.get(id(m)); near = ""
        if hit:
            f, (sc, d, c) = hit
            st = "SAME" if f["val"] == m["val"] and not m["q"] else ("SAME but md has [?]" if f["val"] == m["val"] else "DIFFERENT")
            row = [f["val"], f["line"], round(sc, 2), round(c, 2)]
        else:
            st = "NOT IN FILE (no row aligned)" + (" [?]" if m["q"] else ""); row = ["", "", "", ""]
            cands = sorted(pageF.get(P, []) + pageF.get(P - 1, []) + pageF.get(P + 1, []), key=lambda f: lev(m["val"], f["val"]))[:3]
            near = "\n".join(f'{f["val"]}  |  line {f["line"]}' for f in cands)
        nst[st] += 1
        ws2.append([P, m["printed"], m["line"], m["val"], m["tok"], st] + row + [near, "", ""])
for c in ws2[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496"); c.alignment = Alignment(wrap_text=True, vertical="top")
for i, w in enumerate([8, 8, 8, 16, 18, 24, 16, 8, 7, 8, 30, 10, 14]): ws2.column_dimensions["ABCDEFGHIJKLM"[i]].width = w
ws2.freeze_panes = "A2"; ws2.auto_filter.ref = ws2.dimensions
print("md-side:", dict(nst))
wb.save(a.out)
