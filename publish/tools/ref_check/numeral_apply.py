#!/usr/bin/env python3
"""Apply the user's numeral file to numeral [?] in a volume md (Vol 13 rule: prefer the list over a glyph guess).
Default = PREVIEW (writes a TSV, touches nothing). --apply rewrites the md and writes a log.
Filters (to avoid false matches): context score >= --min-score, file page - PDF in {-2,-1,0}, the best row beats the
runner-up by >= 5 points, and the file value has the same number of parts as the md value (or md has none).
"""
import argparse, re, sys, unicodedata, collections
from pathlib import Path
import openpyxl
from rapidfuzz import fuzz
from indic_transliteration.sanscript import transliterate
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "translit"))
from add_iast import deva_to_iast
DEV = re.compile(r"[ऀ-ॿ]")
D2A = str.maketrans("०१२३४५६७८९", "0123456789"); A2D = str.maketrans("0123456789", "०१२३४५६७८९")
K2A = str.maketrans("೦೧೨೩೪೫೬೭೮೯", "0123456789")
NUMTOK = re.compile(r"([०-९0-9\[\]]+(?:[-–.,][ ]?[०-९0-9\[\]]+)*)\s*\[\?\]")

def fold(t):
    return "".join("v" if c == "w" else c for c in (ch.lower() for ch in unicodedata.normalize("NFD", t) if not unicodedata.combining(ch)) if "a" <= c <= "z")

def parts(s): return re.findall(r"\d+", s.translate(D2A))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True); ap.add_argument("--num", required=True)
    ap.add_argument("--out", default="numeral_apply_preview.tsv")
    ap.add_argument("--min-score", type=float, default=82); ap.add_argument("--apply", action="store_true"); ap.add_argument("--only-lines", default="", help="comma list of md line numbers to apply"); ap.add_argument("--only-agree", action="store_true", help="apply only rows whose digits equal the md digits (just drops [?])")
    ap.add_argument("--from-line", type=int, default=0); ap.add_argument("--to-line", type=int, default=10**9)
    a = ap.parse_args()
    lines = Path(a.md).read_text(encoding="utf8").split("\n")
    rows = collections.defaultdict(list)
    for r in list(openpyxl.load_workbook(a.num, read_only=True).active.iter_rows(values_only=True))[1:]:
        pg, ln, pat, eng, ctx = r[:5]
        if not isinstance(pg, int) or not ctx: continue
        try: lat = transliterate(str(ctx).translate(K2A), "kannada", "iast")
        except Exception: lat = ""
        rows[pg].append(dict(page=pg, eng=re.sub(r"[.]", "-", str(eng)), f=fold(lat)))
    page = None; changes = []
    for n, l in enumerate(lines, 1):
        m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
        if m: page = int(m.group(1))
        if n < a.from_line or n > a.to_line or page is None or "[?]" not in l or not DEV.search(l): continue
        for idx, m in enumerate(NUMTOK.finditer(l)):
            tok = m.group(1)
            if not re.search(r"[०-९0-9]", tok): continue
            dpre = "".join(re.findall(r"[ऀ-ॿ]+", l[max(0, m.start() - 120): m.start()]))
            q = fold(deva_to_iast(dpre))[-40:]
            if len(q) < 12: continue
            sc = []
            for pg in range(page - 2, page + 1):
                for r in rows.get(pg, []):
                    if r["f"]: sc.append((fuzz.partial_ratio(q, r["f"]), r))
            sc.sort(key=lambda x: -x[0])
            if not sc or sc[0][0] < a.min_score: continue
            best = sc[0]
            if len(sc) > 1 and sc[1][1]["eng"] != best[1]["eng"] and best[0] - sc[1][0] < 5: continue
            cand = best[1]["eng"]; mp, cp = parts(tok), parts(cand)
            if any(int(x) == 0 for x in cp): continue                 # e.g. 2-0-0, 0-00: not a citation, wrong row
            if mp and len(mp) != len(cp): continue
            same = (mp == cp)
            changes.append(dict(line=n, idx=idx, page=page, tok=tok, cand=cand, score=round(best[0]), fpage=best[1]["page"], same=same, start=m.start(), end=m.end()))
    with open(a.out, "w", encoding="utf8") as f:
        f.write("md_line\tPDF\tmd_token\tfile_value\tscore\tfile_page\tresult\tcontext\n")
        for c in changes:
            f.write(f"{c['line']}\t{c['page']}\t{c['tok']}\t{c['cand']}\t{c['score']}\t{c['fpage']}\t{'AGREE (drop [?])' if c['same'] else 'REPLACE'}\t{lines[c['line']-1][max(0,c['start']-50):c['start']].strip()}\n")
    print(len(changes), "candidates;", sum(c["same"] for c in changes), "agree,", sum(not c["same"] for c in changes), "replace; wrote", a.out)
    if not a.apply: return
    if a.only_lines: keep = {int(x) for x in a.only_lines.split(",")}; changes = [c for c in changes if c["line"] in keep]
    if a.only_agree: changes = [c for c in changes if c["same"]]
    byline = collections.defaultdict(list)
    for c in changes: byline[c["line"]].append(c)
    for n, cs in byline.items():
        l = lines[n - 1]; dev_line = bool(re.match(r"\s*>?\s*[^*]*[ऀ-ॿ]", l)) and not l.lstrip("> ").startswith("*")
        for c in sorted(cs, key=lambda c: -c["start"]):                 # right to left keeps offsets valid
            new = c["cand"].translate(A2D) if re.search(r"[०-९]", c["tok"]) else c["cand"]
            l = l[:c["start"]] + new + l[c["end"]:]
        lines[n - 1] = l
        # IAST twin: next non-blank line starting with '*' or '> *'
        j = n
        while j < len(lines) and lines[j].strip() == "": j += 1
        if j < len(lines) and lines[j].lstrip().startswith(("*", "> *")) and l.lstrip().startswith(">"):
            t = lines[j]
            for c in cs:
                ps = parts(c["tok"]); rx = re.compile(r"\[?" + r"[-–.,\s\[\]]*".join(ps) + r"\]?\s*\[\?\]")
                t = rx.sub(c["cand"], t, count=1)
            lines[j] = t
    Path(a.md).write_text("\n".join(lines), encoding="utf8")
    with open(Path(a.out).with_suffix(".applied.tsv"), "w", encoding="utf8") as f:
        for c in changes: f.write(f"{c['line']}\t{c['tok']}\t{c['cand']}\n")
    print("applied to", a.md)

main()
