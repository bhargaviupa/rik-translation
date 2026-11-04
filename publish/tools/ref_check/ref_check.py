#!/usr/bin/env python3
"""Pilot: propose fixes for [?] in Devanagari lines of a volume .md, using a separate Sanskrit reference text.

Never edits the volume file. Writes a report (markdown + jsonl) for human review.
  pip install rapidfuzz anthropic indic_transliteration
  python3 ref_check.py --md vol1/Rigveda_Samhita_Vol1_English_Translation.md --ref REF.txt --dry-run
  export ANTHROPIC_API_KEY=...   then drop --dry-run, add --limit 10
REF.txt: IAST or Devanagari, any noise level (e.g. the page text you pasted).
"""
import argparse, json, os, re, sys, unicodedata
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "translit"))
from add_iast import deva_to_iast          # repo's Devanagari -> IAST
from rapidfuzz import fuzz

DEV = re.compile(r"[ऀ-ॿ]")

def fold(text):
    """Loose skeleton: Latin letters only, diacritics stripped. Returns (folded, idx) idx[i]=position in text."""
    out, idx = [], []
    for i, ch in enumerate(text):
        d = unicodedata.normalize("NFD", ch)
        b = "".join(c for c in d if not unicodedata.combining(c)).lower()
        for c in b:
            if "a" <= c <= "z":
                out.append({"w": "v"}.get(c, c)); idx.append(i)   # v/w merge (OCR); keep the rest
    return "".join(out), idx

def load_ref(path):
    raw = Path(path).read_text(encoding="utf8")
    if DEV.search(raw):                       # Devanagari reference -> IAST first
        raw = "\n".join(deva_to_iast(l) for l in raw.split("\n"))
    f, idx = fold(raw)
    return raw, f, idx

def targets(md, scan_all, page_filter):
    page = None
    for n, line in enumerate(Path(md).read_text(encoding="utf8").split("\n"), 1):
        m = re.match(r"#+\s*Page\s+(\d+)", line)
        if m: page = int(m.group(1))
        if not DEV.search(line) or line.lstrip("> ").startswith("*"): continue
        if "[?]" not in line and not scan_all: continue
        if page_filter and page != page_filter: continue
        yield n, page, line

SYS = """You compare a line of Sanskrit (Devanagari) from a transcription with a separate reference text.
The transcription has doubtful readings marked [?] (a word or a character the transcriber could not read).
The reference is noisy OCR in romanization: wrong letters, wrong word breaks, garbled words are common, so it is
only a hint. Propose a replacement for a [?] ONLY if the reference text clearly supports it; otherwise say none.
Never complete a word from your own memory of the passage. status: replace = the reference clearly gives the missing/corrected reading (give the whole corrected word incl. sandhi, one proposal per word, not per character); confirmed = the reference reads the same word the line has, so the [?] looks unnecessary; unsupported = the reference is silent or garbled; contradicted = the reference clearly differs from the line. Numerals (sutra numbers) in the reference OCR are very unreliable: do not replace a numeral unless the reference digits are unmistakable. Answer with JSON only:
{"items":[{"n":1,"context":"words around the [?]","status":"replace|confirmed|unsupported|contradicted","proposal":"Devanagari or null","reference_reading":"quote from the reference or null",
 "confidence":"high|medium|low|none","note":"short"}],
 "other_differences":["short notes on words where the line and the reference disagree, if any"],
 "aligned":true|false}
Set aligned=false if the reference passage is not the same text as the line."""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", default="vol1/Rigveda_Samhita_Vol1_English_Translation.md")
    ap.add_argument("--ref", required=True)
    ap.add_argument("--out", default="ref_check_report")
    ap.add_argument("--min-score", type=float, default=80, help="fuzzy match score (0-100) needed to call the API")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--page", type=int)
    ap.add_argument("--from-line", type=int, default=0, help="only md lines >= this (e.g. start of a Sukta)")
    ap.add_argument("--to-line", type=int, default=10**9)
    ap.add_argument("--sukta", type=int, help="only this Sukta (found from the '## Sūkta N' headings); replaces --from-line/--to-line")
    ap.add_argument("--scan-all", action="store_true", help="also lines without [?] (to test matching/disagreements)")
    ap.add_argument("--dry-run", action="store_true", help="matching only, no API calls")
    ap.add_argument("--model", default="claude-sonnet-5-5")
    a = ap.parse_args()

    if a.sukta:
        heads = [(i, int(m.group(1))) for i, l in enumerate(Path(a.md).read_text(encoding="utf8").split("\n"), 1)
                 if (m := re.match(r"##\s+S[uū]kta\s+(\d+)", l))]
        pos = [i for i, n in heads if n == a.sukta]
        if not pos: sys.exit(f"No heading for Sukta {a.sukta} in {a.md}. Headings found: {[n for _, n in heads]}")
        a.from_line = pos[0]
        later = [i for i, n in heads if i > pos[0]]
        a.to_line = (later[0] - 1) if later else 10**9
        print(f"Sukta {a.sukta}: md lines {a.from_line}-{a.to_line if later else 'end'}")
    raw, rf, ridx = load_ref(a.ref)
    client = None
    if not a.dry_run:
        import anthropic
        key = os.environ.get("RIK_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
        if not key: sys.exit("Set RIK_API_KEY (or ANTHROPIC_API_KEY) first.")
        client = anthropic.Anthropic(api_key=key)
    rows = []
    for n, page, line in [t for t in targets(a.md, a.scan_all, a.page) if a.from_line <= t[0] <= a.to_line][: a.limit]:
        q = line.lstrip("> ").replace("[?]", " ")
        qf, _ = fold(deva_to_iast(q))
        if len(qf) < 12: continue
        al = fuzz.partial_ratio_alignment(qf, rf)
        row = dict(line_no=n, page=page, line=line.lstrip("> "), score=round(al.score, 1))
        s, e = ridx[max(al.dest_start - 20, 0)], ridx[min(al.dest_end + 20, len(ridx) - 1)]
        row["ref_window"] = raw[s:e + 1].replace("\n", " ")
        if a.dry_run or al.score < a.min_score:
            row["result"] = "dry-run" if a.dry_run else "no match above threshold"
        else:
            msg = f"LINE (Devanagari):\n{row['line']}\n\nREFERENCE (noisy romanization):\n{row['ref_window']}\n"
            try:
                r = client.messages.create(model=a.model, max_tokens=6000, system=SYS,
                                           messages=[{"role": "user", "content": msg}])
            except Exception as ex:
                print(f"\nAPI ERROR ({type(ex).__name__}): {ex}\n(model used: {a.model}; try --model to change it)")
                sys.exit(1)
            txt = "".join(b.text for b in r.content if getattr(b, "type", "") == "text")
            try: row["result"] = json.loads(txt[txt.find("{"): txt.rfind("}") + 1])
            except Exception: row["result"] = {"raw": txt}
            row["tokens"] = [r.usage.input_tokens, r.usage.output_tokens]
        rows.append(row)
        print(f"line {n} p.{page} score {row['score']}: {str(row['result'])[:110]}")
    Path(a.out + ".jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows), encoding="utf8")
    with open(a.out + ".md", "w", encoding="utf8") as f:
        for r in rows:
            f.write(f"## line {r['line_no']} (page {r['page']}) match {r['score']}\n\n{r['line']}\n\nREF: {r['ref_window']}\n\n")
            f.write("```json\n" + json.dumps(r["result"], ensure_ascii=False, indent=1) + "\n```\n\n")
    print("wrote", a.out + ".md", "and .jsonl; the volume file was not touched")

if __name__ == "__main__":
    main()
