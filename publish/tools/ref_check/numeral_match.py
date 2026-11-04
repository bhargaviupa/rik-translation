#!/usr/bin/env python3
"""Match the md's numeral [?] to rows of a user-supplied numeral file by CONTEXT (not page number).
Free (no API). Writes a TSV for review; never edits the md.
  python3 numeral_match.py --md vol7/Rigveda_Samhita_Vol7_English_Translation.md --num vol7/numerals/FILE.xlsx --out numeral_candidates.tsv [--sukta N | --from-line A --to-line B]
Idea: the file's 'Raw Line Context' (Kannada OCR) is transliterated to Latin and folded; so is the Devanagari/IAST text
just before each [?] in the md. The best fuzzy match among rows within +-WINDOW pages gives the candidate digits.
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
D2A = str.maketrans("०१२३४५६७८९", "0123456789")
K2A = str.maketrans("೦೧೨೩೪೫೬೭೮೯", "0123456789")

def fold(t):
    out = []
    for ch in unicodedata.normalize("NFD", t):
        if unicodedata.combining(ch): continue
        c = ch.lower()
        if "a" <= c <= "z": out.append("v" if c == "w" else c)
    return "".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True); ap.add_argument("--num", required=True)
    ap.add_argument("--out", default="numeral_candidates.tsv")
    ap.add_argument("--window", type=int, default=2, help="+- PDF pages around the md page")
    ap.add_argument("--min-score", type=float, default=70)
    ap.add_argument("--sukta", type=int); ap.add_argument("--from-line", type=int, default=0)
    ap.add_argument("--to-line", type=int, default=10**9)
    a = ap.parse_args()
    md = Path(a.md).read_text(encoding="utf8").split("\n")
    if a.sukta:
        heads = [(i, int(m.group(1))) for i, l in enumerate(md, 1) if (m := re.match(r"##\s+S[uū]kta\s+(\d+)", l))]
        pos = [i for i, n in heads if n == a.sukta]
        if not pos: sys.exit("no such Sukta heading")
        later = [i for i, n in heads if i > pos[0]]
        if not a.from_line: a.from_line = pos[0]
        if a.to_line == 10**9 and later: a.to_line = later[0] - 1
    rows = collections.defaultdict(list)
    ws = openpyxl.load_workbook(a.num, read_only=True).active
    for r in list(ws.iter_rows(values_only=True))[1:]:
        pg, ln, pat, eng, ctx = r[:5]
        if not isinstance(pg, int) or not ctx: continue
        k = str(ctx).translate(K2A)
        try: lat = transliterate(k, "kannada", "iast")
        except Exception: lat = ""
        rows[pg].append(dict(page=pg, eng=str(eng), pat=str(pat), ctx=str(ctx), f=fold(lat)))
    page = None; out = []
    for n, l in enumerate(md, 1):
        m = re.match(r"#+\s*Page\s+\d+\s*\(PDF\s*(\d+)", l)
        if m: page = int(m.group(1))
        if n < a.from_line or n > a.to_line or page is None or "[?]" not in l or not DEV.search(l): continue
        for m in re.finditer(r"\[\?\]", l):
            pre = l[max(0, m.start() - 70): m.start()]
            if not re.search(r"[०-९0-9\]]", pre[-9:]): continue          # numeral-type [?] only
            mdnum = "-".join(re.findall(r"\d+", pre[-14:].translate(D2A)))
            dpre = "".join(re.findall(r"[\u0900-\u097f]+", l[max(0, m.start() - 120): m.start()]))   # Sanskrit words only
            q = fold(deva_to_iast(dpre))[-40:]
            if len(q) < 12: continue
            best = (0, None)
            for pg in range(page - a.window, page + a.window + 1):
                for r in rows.get(pg, []):
                    s = fuzz.partial_ratio(q, r["f"]) if r["f"] else 0
                    if s > best[0]: best = (s, r)
            s, r = best
            cand = r["eng"] if r and s >= a.min_score else ""
            flag = ("AGREE" if cand and mdnum and cand.replace(".", "-").endswith(mdnum.split("-")[-1]) and mdnum in cand.replace(".", "-")
                    else "DIFF" if cand else "none")
            out.append([n, page, pre.strip()[-40:].replace("\t", " "), mdnum, cand, round(s), (r["page"] - page) if r else "", flag])
    with open(a.out, "w", encoding="utf8") as f:
        f.write("md_line\tPDF\tmd_text_before\tmd_digits\tfile_candidate\tscore\tfile_page-PDF\tflag\n")
        for o in out: f.write("\t".join(map(str, o)) + "\n")
    c = collections.Counter(o[-1] for o in out)
    print(f"{len(out)} numeral [?] examined; {dict(c)}; wrote {a.out}")
    offs = collections.Counter(o[6] for o in out if o[7] != "none")
    print("file_page - PDF among matches:", dict(sorted(offs.items())))
main()
