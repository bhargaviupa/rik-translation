# publish/out — releases only

Only release PDFs live here (REQUIREMENTS A1, F16): a volume that has passed the release gate. None exists yet.
Review copies are written to `volN/review/` by every builder (`publish/volbook.py`, the legacy `build*.py`, `publish/bhashya_book.py`, `python3 -m rv print`). The `.html` a build leaves here is a build step and is not kept (`.gitignore`).
