#!/usr/bin/env python3
"""Check built PDFs against the print rules that can be counted (REQUIREMENTS A4, B2.5, B4, D19).

  python3 publish/pdf_check.py N [N…]        every PDF named *_full*.pdf or *review_copy*.pdf in volN/review/
  python3 publish/pdf_check.py FILE.pdf

Per PDF: pages; FAIL lines (dotted circle; 'original p.' left in the body; a body page without the footer 'Kannada edition p.' /
'REVIEW COPY') and COUNT lines (what a release may not contain and a review copy still shows: [?], [sic], 'as printed', 'as supplied',
NOTE, GLOSS, words of the translating session).  Exit 1 if any PDF has a FAIL.  Needs pdftotext (poppler).
Text copied out of a PDF garbles Devanagari conjuncts, so nothing here compares Sanskrit: that is done on the .md files."""
import re, subprocess, sys, pathlib, glob
ROOT = pathlib.Path(__file__).resolve().parent.parent
COUNTS = [('[?]', r'\[\?\]'), ('[sic]', r'\[sic\b'), ('as printed', r'\bas printed\b'), ('as supplied', r'\bas supplied\b|supplied text'), ('NOTE', r'\bNOTE\b'),
          ('GLOSS', r'\bGLOSS\b'), ('session words', r'better scan|numeral pass|600 dpi|\b(this|next) (batch|session)\b|best-effort|lower-confidence|mine and tentative|PDF pages? \d')]
def check(pdf):
    pages = subprocess.run(['pdftotext', '-layout', str(pdf), '-'], capture_output=True, text=True).stdout.split('\f')
    pages = pages[:-1] if pages and not pages[-1].strip() else pages
    n = len(pages); text = '\n'.join(pages); fails = []
    circ = text.count('◌'); orig = len(re.findall(r'\boriginal pp?\. ?\d', text))
    foot = sum(1 for p in pages if 'Kannada edition p' in p); rev = sum(1 for p in pages if 'REVIEW COPY' in p)
    if circ: fails.append(f'dotted circle ◌: {circ}')
    if orig: fails.append(f"'original p. N' in the body: {orig}")
    if foot < 0.9 * n: fails.append(f"footer 'Kannada edition p.' on {foot} of {n} pages")
    if rev < 0.9 * n: fails.append(f"'REVIEW COPY' on {rev} of {n} pages")
    print(f'{pdf.relative_to(ROOT) if pdf.is_relative_to(ROOT) else pdf}: {n} pages')
    for f in fails: print('  FAIL  ' + f)
    print('  COUNT ' + '; '.join(f'{k} {len(re.findall(rx, text))}' for k, rx in COUNTS) + '   (lines of the PDF text; 0 wanted for a release)')
    return not fails
def main():
    pdfs = []
    for a in sys.argv[1:]:
        if a.isdigit(): pdfs += sorted(pathlib.Path(x) for x in glob.glob(str(ROOT / f'vol{a}' / 'review' / '*.pdf')) if re.search(r'_full|review_copy', x))
        else: pdfs.append(pathlib.Path(a).resolve())
    if not pdfs: sys.exit(__doc__)
    ok = [check(p) for p in pdfs]
    sys.exit(0 if all(ok) else 1)
if __name__ == '__main__': main()
