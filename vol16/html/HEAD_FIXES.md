# Vol 16 supplied text: merged file and the three running-head numbers corrected

`rig_16.md` = `rig_16_1.md` + `rig_16_2.md` (as supplied; the converter's first line of the 2nd file dropped, as `tools/rv/merge_md.py` does), the inputs removed from the working tree (history keeps them, and the user's unmodified originals with all images are in the commit history of `vol16/rig_16.md`, commit "the two supplied markdown files merged").

Three running-head page numbers were misread by the converter and made pages 344, 347 and 348 invisible to the page splitter (the pages were filed as 844 and 847, and 348 was written with Kannada digits). They were corrected from the sequence (neighbours 343/345, 346/348, 347/349, running head "Maṃ. 3 A. 2 Sū. 16-17" unchanged). Only the page number in the head line was changed; no other character.

| line (merged file) | supplied | now |
|---|---|---|
| 15649 | `844 ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ [ ಮಂ. ೩ ಅ. ೨ ಸೂ. ೧೬.` | `344 …` |
| 15780 | `… ಋಗ್ವೇದಸಂಹಿತಾ. 847` | `… 347` |
| 15823 | `೩೪೮ ಸಾಯಣಭಾಷ್ಯಸಹಿತಾ [ಮಂ. ೩. ಅ. ೨. ಸೂ. ೧೭` | `348 …` |

Seam: the last page of file 1 (head read 423) was labelled 422 when file 1 was split alone (edge effect); in the merged file it is correctly page 423 (page 422 had no running head and is merged into 421). Pages without a running head stay merged into the page before them (e.g. 439, 460, 461).
