#!/usr/bin/env python3
"""Second pass for file rows that stayed NOT FOUND: match them to md numerals using a rough ENGLISH rendering of the file's Kannada context
(column E, translated by agents: TSV id<TAB>english) against the md text around each numeral (all md numerals on pages P-1..P+1, aligned or not).
  python3 numeral_notfound_match.py --md MD --num XLSX --nf NOTFOUND_INDEX.json --gloss out0.tsv out1.tsv ... --out XLSX
Score = 0.5 context (rapidfuzz token_set_ratio of English gloss vs md window, Latin words folded) + 0.35 digits + 0.15 reference-type hint.
Report only: proposals with score >= 0.6 are listed as PROPOSE, the rest as WEAK/NONE."""
import argparse, re, json, collections, unicodedata
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from rapidfuzz import fuzz
D2A = str.maketrans("०१२३४५६७८९", "0123456789")
REF = re.compile(r"(?<![\d\-.])[०-९0-9]+(?:\s*[-–.]\s*[०-९0-9]+)+|(?<![\d\-.])[०-९0-9]+(?:\s*-\s*[०-९0-9]+)*\s*-\s*\?+")
def fold(t):
    t = unicodedata.normalize("NFD", t.lower()); return re.sub(r"[^a-z ]", " ", "".join(c for c in t if not unicodedata.combining(c)))
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, c in enumerate(a, 1):
        q = [i]
        for j, e in enumerate(b, 1): q.append(min(q[-1] + 1, p[j] + 1, p[j - 1] + (c != e)))
        p = q
    return p[-1]
ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--nf", required=True); ap.add_argument("--gloss", nargs="+", required=True)
ap.add_argument("--ctx", required=True, help="TSV id page value kannada"); ap.add_argument("--out", required=True); a = ap.parse_args()
nf = json.load(open(a.nf)); gl = {}
for g in a.gloss:
    for l in open(g, encoding="utf8"):
        if "\t" in l: i, e = l.rstrip("\n").split("\t", 1); gl[int(i)] = e
kan = {}
for c in a.ctx.split(","):
    for l in open(c, encoding="utf8"): p = l.rstrip("\n").split("\t"); kan[int(p[0])] = p[3] if len(p) > 3 else ""
md = collections.defaultdict(list); cur = None; printed = None
L = open(a.md, encoding="utf8").read().split("\n")
for n, l in enumerate(L, 1):
    m = re.match(r"#+\s*(?:Page|Printed p\.)\s+(\w+)\s*\(PDF\s*(\d+)", l)
    if m: printed, cur = m.group(1), int(m.group(2))
    if cur is None or l.startswith(("|", "#")): continue
    for m in REF.finditer(l):
        tok = m.group(0); v = "-".join(re.findall(r"\d+|\?", tok.translate(D2A)))
        win = " ".join(L[max(0, n - 2): n + 1])[max(0, m.start() - 200): m.end() + 200] if False else l[max(0, m.start() - 220): m.end() + 120]
        md[cur].append(dict(line=n, printed=printed, val=v, tok=tok, ctx=fold(re.sub(r"[ऀ-ॿ]+", " ", win))))
def digs(fv, mv):
    if mv.endswith("-?"):
        kn = mv[:-2].split("-"); f = fv.split("-")
        if len(f) <= len(kn): return 0.0
        x, y = "-".join(kn), "-".join(f[:len(kn)])
        return max(0, 1 - lev(x, y) / max(len(x), len(y))) - 0.05
    pa, pb = fv.split("-"), mv.split("-"); s, t = fv, mv
    return max(0.0, 1 - lev(s, t) / max(len(s), len(t))) - (0.15 if len(pa) != len(pb) else 0)
KIND = [(r"nirukta|\bni\b", r"\bni\.?\b|nirukta"), (r"p[aā][nṇ]ini|sutra|k[aā][sś]ik", r"p[aā]\.|sūtra|sutra|k[aā]\.|aṣṭ|ast")]
rows = []
for idx, (P, line, v) in enumerate(nf):
    g = gl.get(idx, ""); ge = fold(g)
    best = []
    for p in (P - 1, P, P + 1):
        for m in md.get(p, []):
            c = fuzz.token_set_ratio(ge, m["ctx"]) / 100 if ge and g != "GARBAGE" else 0
            d = digs(v, m["val"])
            kh = 0.0
            if re.search(r"nirukta", ge) and re.search(r"\bni\b|nirukta", m["ctx"]): kh = 1.0
            if re.search(r"p[aā]nini|sutra|kasika|kasik", ge) and re.search(r"\bp[aā]\b|sutra|\bsu\b|p[aā]ṇini", m["ctx"]): kh = 1.0
            best.append((0.5 * c + 0.35 * d + 0.15 * kh, c, d, m))
    best.sort(key=lambda t: -t[0])
    rows.append((idx, P, line, v, g, kan.get(idx, ""), best[:3]))
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "not found, second pass"
ws.append(["id", "PDF page", "file line", "FILE value", "decision", "score", "md line", "MD value", "md token", "digit sim", "context sim", "English gloss of file context", "Kannada context (col E)", "2nd candidate (score | md value)", "YOUR ANSWER"])
cnt = collections.Counter()
for idx, P, line, v, g, k, best in rows:
    if not best: dec = "NONE"; ws.append([idx, P, line, v, dec, "", "", "", "", "", "", g, k[:90], "", ""]); cnt[dec] += 1; continue
    s, c, d, m = best[0]
    dec = "PROPOSE" if s >= 0.6 and c >= 0.5 and d >= 0.5 else ("WEAK" if s >= 0.45 else "NONE")
    if dec == "PROPOSE" and m["val"] == v: dec = "PROPOSE (md already equals file)"
    cnt[dec] += 1
    sec = f"{best[1][0]:.2f} | {best[1][3]['val']}" if len(best) > 1 else ""
    ws.append([idx, P, line, v, dec, round(s, 2), m["line"], m["val"], m["tok"], round(d, 2), round(c, 2), g, k[:90], sec, ""])
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="305496"); c.alignment = Alignment(wrap_text=True, vertical="top")
for i, w in enumerate([6, 8, 8, 14, 22, 7, 8, 14, 14, 8, 8, 50, 40, 16, 14]): ws.column_dimensions["ABCDEFGHIJKLMNO"[i]].width = w
ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
wb.save(a.out); print(dict(cnt))
