# Vol 18 — printed contents (ವಿಷಯಾನುಕ್ರಮಣಿಕೆ), md lines 683–1081

Parsed by `publish/tools/frontmatter/contents_parse.py vol18/html/rig_18.md --start 'ವಿಷಯಾಸುಕ್ರಮಣಿಕೆ' --fixes vol18/contents_fixes.json` (the heading is misread in the supplied text, hence `--start`): 46 sūkta lines, 201 items; the last pages of the contents were HTML tables in the supplied text (`flatten_tables`).

Fix applied (`vol18/contents_fixes.json`): md line 900 page 389 → **589** (the neighbours are 588 and 590; OCR dropped the 5). No scan was available to compare: this one rests on the sequence.

Not repaired, listed (items printed without a page number in the supplied text, so the English contents shows them without one): md lines 707–711 (one item over several lines, Niṣkevalya-śastra explanation), 762, 961, 976, and the headings 795 and 875. Every other item's page was checked only for order (check printed by `--check`: no page goes down).
The English contents (`vol18/contents_en.json`, `vol18/frontmatter_en.json`) is a first translation by `tools/rv/api_frontmatter.py` (cost $0.38), for the editor's reading; entries whose Kannada is garbled carry a `note`.
