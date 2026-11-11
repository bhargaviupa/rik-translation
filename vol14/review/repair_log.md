# Repair log — Vol 14


- 2026-11-11 IAST layer added to every Saṃhitā and Pada block that had none, by `publish/tools/translit/add_iast.py --samhita-pada` (lesson 47: the old tool skipped blocks followed by a `**label**` line). Only added lines (blank + `> *iast*`); no existing line changed; bhāṣya blocks stay Devanagari only (user, Nov 11 2026); the IAST is plain (Vedic accent signs removed before transliteration, the Devanagari keeps them); a `[?]` stays on the Devanagari line only.
