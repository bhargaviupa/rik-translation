- front matter: the volume's preface (translated by tools/rv/api_front.py) inserted before printed p. 1 in the English and the Kannada file; 1 NOTE rows added at the top of review/notes.tsv.
# Vol 11 repair log

- Nov 12 2026, preface (`work/preface/en.md`, hand edit before install): (1) the verse of Ṛk 1-139-9 stood in kn.md on two lines; the model had written the whole text plus `~~` inside ⟦ ⟧; changed to `⟦first~~last⟧` (letters of the supplied text unchanged); (2) the remark "printed as ಬೃ. ಜೇ." (Kannada script) removed from the reference "(Bṛ. De. 4-16)"; the question stays in the **NOTE** (review/notes.tsv). (3) The API call's cost was not logged (tool bug: `vol11/parts/` did not exist; fixed in `api_front.py`, makedirs); usage of that call was not recorded.
