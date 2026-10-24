"""Numeral corrections for Vol 11 PDF 1-24 from the user's review (docs/numeral_review/edits_PDF1-24.txt). Most edits confirmed
the files; the title page (PDF 1) and contents pages (PDF 13-18) are not transcribed. Two changes, both checked on the printed line."""
import sys
sys.path.insert(0,'publish/tools/verify11')
from fx import en,kn
kn(11,[('(ಪೇಜು ೨೨೧ ರಿಂದ ೨೮೬)','(ಪೇಜು ೨೨೨ ರಿಂದ ೨೮೬)'),('ರಜಾಂಸಿ** ಋ. ಸಂ. (೧-೧೫೪-೧)','ರಜಾಂಸಿ** ಋ. ಸಂ. (೧-೫೪-೧)')])
en(11,[('(pp. 221 to 286)','(pp. 222 to 286)'),('vimame rajāṃsi*" (Ṛ. Saṃ. 1-154-1)','vimame rajāṃsi*" (Ṛ. Saṃ. 1-54-1 [as printed])')])
