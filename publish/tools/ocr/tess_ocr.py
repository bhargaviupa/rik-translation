#!/usr/bin/env python3
"""Offline OCR of a scanned PDF (Kannada/Sanskrit) with Tesseract. No internet, no cost.

Setup (once):
  1. Install Tesseract OCR and add the languages Kannada (kan), Sanskrit (san), English (eng).
       Windows: installer from https://github.com/UB-Mannheim/tesseract/wiki (tick Kannada, Sanskrit in 'Additional language data').
       macOS:   brew install tesseract tesseract-lang
       Ubuntu:  sudo apt install tesseract-ocr tesseract-ocr-kan tesseract-ocr-san
  2. pip install pymupdf pytesseract pillow

Run:
  python tess_ocr.py MYFILE.pdf OUTFOLDER            # all pages
  python tess_ocr.py MYFILE.pdf OUTFOLDER 5 12       # pages 5..12 only (1-based)
Writes OUTFOLDER/page_001.txt ... and OUTFOLDER/all.txt (pages separated by '=== PDF page N ===').
On Windows, if tesseract is not found, set TESSERACT_CMD, e.g.  set TESSERACT_CMD=C:\\Program Files\\Tesseract-OCR\\tesseract.exe
"""
import os, sys, io
import fitz                      # PyMuPDF
import pytesseract
from PIL import Image

if os.environ.get('TESSERACT_CMD'):
    pytesseract.pytesseract.tesseract_cmd = os.environ['TESSERACT_CMD']

def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    pdf, out = sys.argv[1], sys.argv[2]
    doc = fitz.open(pdf)
    a = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    b = int(sys.argv[4]) if len(sys.argv) > 4 else len(doc)
    os.makedirs(out, exist_ok=True)
    allp = []
    for n in range(a, b + 1):
        pix = doc[n - 1].get_pixmap(dpi=300, colorspace=fitz.csGRAY)
        img = Image.open(io.BytesIO(pix.tobytes('png')))
        txt = pytesseract.image_to_string(img, lang='kan+san+eng', config='--psm 6')
        open(os.path.join(out, 'page_%03d.txt' % n), 'w', encoding='utf-8').write(txt)
        allp.append('=== PDF page %d ===\n%s' % (n, txt))
        print('page', n, 'done', flush=True)
    open(os.path.join(out, 'all.txt'), 'w', encoding='utf-8').write('\n'.join(allp))

if __name__ == '__main__':
    main()
