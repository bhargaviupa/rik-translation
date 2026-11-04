#!/usr/bin/env python3
"""Leftover entries + context. For each page P: file entries on page P not used by an exact md match are candidates; each
doubtful md numeral is scored against them by CONTEXT (Sanskrit/Latin words before the numeral vs the file's Raw Line Context,
Kannada -> Latin, folded) plus a small digit-similarity term; best pair first, one-to-one.
  python3 numeral_leftover2.py --md MD --num XLSX --out TSV"""
import argparse, re, sys, collections, unicodedata
from pathlib import Path
import openpyxl
from rapidfuzz import fuzz
from indic_transliteration.sanscript import transliterate
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "translit"))
from add_iast import deva_to_iast
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); K2A = str.maketrans("೦೧೨೩೪೫೬೭೮೯", "0123456789"); DEV = re.compile(r"[ऀ-ॿ]")
def fold(t):
    return "".join("v" if c == "w" else c for c in (ch.lower() for ch in unicodedata.normalize("NFD", t) if not unicodedata.combining(ch)) if "a" <= c <= "z")
def lev(x, y):
    d = list(range(len(y) + 1))
    for i, c in enumerate(x, 1):
        p, d[0] = d[0], i
        for j, e in enumerate(y, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (c != e))
    return d[-1]
parts = lambda s: re.findall(r"\d+", s.translate(D2A))
def ctx_of(line, pos):
    seg = line[max(0, pos - 130): pos]
    seg = re.sub(r"(Pā|Ni|Āś|Āśv|Ā|Ai|Tai|Uṇ|Kā|पा|नि|आ|ऐ|तै|उ|का)\.[^\w]*$", "", seg)
    lat = deva_to_iast(seg) if DEV.search(seg) else seg
    return fold(lat)[-48:]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--md", required=True); ap.add_argument("--num", required=True); ap.add_argument("--out", default="leftover2.tsv")
    ap.add_argument("--minctx", type=float, default=68); ap.add_argument("--margin", type=float, default=6)
    a = ap.parse_args()
    rows = collections.defaultdict(list)
    for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
        if isinstance(r[0], int) and r[4]:
            v = "-".join(parts(str(r[3])))
            if len(v.split("-")) < 2: continue
            try: lat = transliterate(str(r[4]).translate(K2A), "kannada", "iast")
            except Exception: lat = ""
            rows[r[0]].append(dict(v=v, f=fold(lat), line=r[1], raw=str(r[4])[:100]))
    pages = collections.defaultdict(lambda: {"ex": [], "q": []}); page = None
    for n, l in enumerate(open(a.md, encoding="utf8").read().split("\n"), 1):
        m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
        if m: page = int(m.group(1))
        if page is None or l.lstrip().startswith("*") or not DEV.search(l): continue
        lt = l.translate(D2A)
        for m in re.finditer(r"(\[?\d+\]?(?:\s*[-–.,]\s*\[?\d+\]?)+)(\s*\[\?\])?", lt):
            ps = parts(m.group(1))
            if len(ps) >= 2:
                if m.group(2): pages[page]["q"].append((n, ps, True, m.group(0).strip(), ctx_of(lt, m.start())))
                else: pages[page]["ex"].append("-".join(ps))
        for m in re.finditer(r"(\d+(?:\s*-\s*\d+)*)\s*-\s*\[\?\]|\[(\d+)\s*-\s*\?\]\s*\[\?\]", lt):
            pages[page]["q"].append((n, parts(m.group(0)), False, m.group(0).strip(), ctx_of(lt, m.start())))
    out = []
    for P, d in sorted(pages.items()):
        cands = list(rows.get(P, []))
        for v in d["ex"]:
            k = next((i for i, c in enumerate(cands) if c["v"] == v), None)
            if k is not None: cands.pop(k)
        U = []
        for t in d["q"]:
            n, ps, comp, tok, cx = t
            k = next((i for i, c in enumerate(cands) if comp and c["v"] == "-".join(ps)), None)
            if k is not None: cands.pop(k)
            else: U.append(t)
        sc = []
        for i, (n, ps, comp, tok, cx) in enumerate(U):
            for j, c in enumerate(cands):
                if len(cx) < 12 or not c["f"]: continue
                cs = fuzz.partial_ratio(cx, c["f"])
                dg = lev("-".join(ps), "-".join(c["v"].split("-")[: len(ps)] if not comp else [c["v"]])) if True else 0
                sc.append((cs - 1.5 * min(dg, 6), cs, i, j))
        sc.sort(reverse=True); ui, uj = set(), set()
        for tot, cs, i, j in sc:
            if cs < a.minctx or i in ui or j in uj: continue
            rest = [s for s in sc if s[2] == i and s[3] != j and s[3] not in uj]
            if rest and tot - max(r[0] for r in rest) < a.margin: continue
            ui.add(i); uj.add(j); n, ps, comp, tok, cx = U[i]
            out.append((n, P, tok, "-".join(ps), cands[j]["v"], round(cs), round(tot), len(U), len(cands), cands[j]["raw"][:60]))
    with open(a.out, "w", encoding="utf8") as f:
        f.write("md_line\tPDF\tmd_token\tmd_digits\tfile_entry\tcontext_score\ttotal\tdoubtful_on_page\tunused_on_page\tfile_context\n")
        for o in out: f.write("\t".join(map(str, o)) + "\n")
    print(len(out), "pairings")
main()
