"""Builds vol28/contents_en.json: one English row per block of the parsed contents (src = line of contents_kn.md).
Sūkta and nirukta rows take their Sanskrit incipit from the Kannada line by script (inside ⟦ ⟧); nothing Sanskrit is typed here.
Run from the repository root: python3 vol28/contents_src/make_contents_en.py"""
import json, subprocess, sys, pathlib, tempfile
ROOT = pathlib.Path(__file__).resolve().parents[2]
tmp = pathlib.Path(tempfile.mkdtemp()) / 'c28.json'
subprocess.run([sys.executable, str(ROOT / 'publish/tools/frontmatter/contents_parse.py'), str(ROOT / 'vol28/contents_src/contents_kn.md'),
                '--end', 'ವಿಷಯಾನುಕ್ರಮಣಿಕೆ ಸಮಾಪ್ತವು', '--out', str(tmp)], check=True, capture_output=True)
B = json.load(open(tmp)); BY = {b['src']: b for b in B}
O = dict(zip(range(41, 72), '''forty-first forty-second forty-third forty-fourth forty-fifth forty-sixth forty-seventh forty-eighth forty-ninth fiftieth
fifty-first fifty-second fifty-third fifty-fourth fifty-fifth fifty-sixth fifty-seventh fifty-eighth fifty-ninth sixtieth
sixty-first sixty-second sixty-third sixty-fourth sixty-fifth sixty-sixth sixty-seventh sixty-eighth sixty-ninth seventieth seventy-first'''.split()))
KD = dict(zip('೦೧೨೩೪೫೬೭೮೯', '0123456789'))
def inc(src): return BY[src]['text'].split(' ಎಂಬ ')[0].strip()
def S(src):
    n = int(''.join(KD[c] for c in BY[src]['no']))
    return f'{n}. The {O[n]} sūkta, beginning ⟦{inc(src)}⟧'
def N(src): return f'The Nirukta of the Ṛk ⟦{inc(src)}⟧.'
E = {}
def a(src, en): E[src] = en
a(3, 'The Eighth Adhyāya in the Seventh Aṣṭaka.'); a(4, 'Sūktas of the Tenth Maṇḍala.')
a(5, S(5)); a(6, 'Introduction to the sūkta.')
a(7, S(7)); a(8, S(8)); a(9, 'Explanation of the meaning of the word ⟦ಶ್ವಘ್ನೀ⟧, etc.')
a(10, S(10)); a(11, S(11)); a(12, 'The three kinds of Agni.'); a(13, 'The origin of Agni in the heavenly world.')
a(14, 'Praise of the lightning-Agni of the atmosphere.'); a(15, 'The greatness of the earthly Agni.')
a(16, 'The various Agnis: Jātavedas, Vaiśvānara, Draviṇodas, etc.'); a(17, 'Description of the great qualities of Agni, etc.')
a(18, 'Discussion of the deathlessness of Agni, etc.')
a(19, 'Here ends the Eighth Adhyāya in the Seventh Aṣṭaka.'); a(20, 'The First Adhyāya in the Eighth Aṣṭaka.')
a(21, S(21)); a(22, 'Introduction to the sūkta—the greatness of the sūktas seen by the seer Vatsapri.')
a(23, 'How Bhṛgu and other seers found Agni.'); a(24, 'How Mātariśvan brought Agni from the atmosphere.')
a(25, 'How Bṛhaspati found Agni.'); a(26, 'The relation between the Aṅgirasa seers and Agni.'); a(27, 'Discussion of matters concerning Trita Āptya.')
a(28, S(28)); a(29, S(29)); a(30, 'Introduction to the sūkta—why Indra is called Mahānindra.')
a(31, N(31)); a(32, 'Explanation of the meaning of the word ⟦ಖಲ⟧.')
a(33, 'The formation of the words ⟦ಏಕ⟧, ⟦ದ್ವಾ⟧, ⟦ತ್ರಯಃ⟧, ⟦ಚತುರ್ಥ⟧, etc.')
a(34, S(34)); a(35, 'Introduction to the sūkta—the daring deeds of Indra—description of the slaying of the asura Vṛtra.')
a(36, 'The story of the goddess Prāsahā.'); a(37, 'Why Indra has the name Marutvān.'); a(38, 'The killing of the rākṣasa Namuci by Indra.')
a(39, 'Why Indra has the name Ṛjīṣī.'); a(40, 'The killing of the asura Varāha by Indra.'); a(41, 'The killing of Viśvarūpa by Indra.')
a(42, 'How Indra incurred the guilt of killing a Brāhmaṇa, and the efforts he made to remove it.')
a(44, "The subject of Indra's Vaikuṇṭha."); a(45, 'The subject of Kavi Uśanā.'); a(46, 'The subject of Kutsa.'); a(47, 'The subject of the asura Śuṣṇa.')
a(48, 'Explanation of the meaning of the word ⟦ದಸ್ಯು⟧.'); a(49, 'Explanation of the word ⟦ವೇತಸೂನ್⟧.'); a(50, 'The subject of Turvaśa and Yadu.')
a(51, S(51)); a(52, 'The subject of the oblations (or deities) called Devasuvas.'); a(53, 'The subject of the Brahmodya discussed at the sacrifice.')
a(54, S(54)); a(55, 'Introduction to the sūkta.'); a(56, 'The deeds of Agni.'); a(57, 'How Agni hid in the water.')
a(58, 'The conversation between the gods and Agni on this matter.'); a(59, 'The account of this matter in the Bṛhaddevatā.')
a(60, "Yāska's explanation of the oblations called Prayājas and Anuyājas.")
a(61, S(61)); a(62, 'Introduction to the sūkta.'); a(63, 'Discussion of the Viśvedevas.')
a(64, 'Names of the seers who saw sūktas addressed to the Viśvedevas, and the sūktas.')
a(65, 'The deities who are occasionally praised in sūktas addressed to the Viśvedevas.'); a(66, 'Discussion of the number of the gods.')
a(67, S(67)); a(68, 'Who the five peoples (pañcajanas) are.'); a(69, 'The special application (viniyoga) of the Ṛk ⟦ತಂತುಂ ತನ್ವನ್⟧.')
a(70, S(70)); a(71, S(71)); a(72, S(72)); a(73, 'The subject of the threefold debt.')
a(74, S(74)); a(75, 'Introduction to the sūkta—the story of the seer Subandhu.')
a(76, 'The ancient legend told in the Śāṭyāyana Brāhmaṇa about Subandhu.')
a(77, S(77)); a(78, S(78)); a(79, N(79)); a(80, S(80)); a(81, 'The explanation in the Śāṭyāyana Brāhmaṇa of the Ṛk ⟦ಅಯಂ ಮಾತಾಯಂ⟧.')
a(82, S(82)); a(83, 'Introduction to the sūkta.')
a(84, 'The subject of the seer Nābhānediṣṭha—how Manu gave his sons their shares of the inheritance.')
a(86, 'How Prajāpati became enamoured of his own daughter.'); a(87, 'The origin of Āditya, Bhṛgu and the Aṅgirases.')
a(88, 'Here ends the First Adhyāya in the Eighth Aṣṭaka.'); a(89, 'The Second Adhyāya.')
a(90, S(90)); a(91, 'Introduction to the sūkta.'); a(92, 'The formation of the word ⟦ಅಂಗಿರಾಃ⟧.')
a(93, S(93)); a(94, N(94)); a(95, S(95)); a(96, 'The subject of the deity Narāśaṃsa.')
a(97, 'Explanation of the word ⟦ಅದಿತಿ⟧, and the Nirukta of the Ṛk ⟦ದಕ್ಷಸ್ಯ ವಾದಿತೇ⟧.'); a(98, 'The names of the seven Soma-guardians, etc.')
a(99, S(99)); a(100, 'Introduction to the sūkta.'); a(101, 'The subject of the deities Mitra, Varuṇa and Aryamā.')
a(102, S(102)); a(103, S(103)); a(104, 'Introduction to the sūkta.'); a(105, 'The subject of the deity Bṛhaspati.')
a(106, 'How Bṛhaspati brought back the cows of the gods that Vala had carried off.'); a(107, 'Why the Aṅgirases are called Varāhas.')
a(108, S(108)); a(109, S(109)); a(110, S(110))
a(111, 'Introduction to the sūkta—the subject of the Āprī sūktas.')
a(112, 'Samiddha (Agni).'); a(113, 'Narāśaṃsa.'); a(114, 'Iḷā.'); a(115, 'Barhis.'); a(116, 'The Divine Doors.'); a(117, 'Night and Dawn.')
a(118, 'The Two Divine Hotṛs.'); a(119, 'The three goddesses (Sarasvatī, Iḷā and Bhāratī).'); a(120, 'Tvaṣṭṛ.'); a(121, 'Vanaspati.'); a(122, 'Svāhākṛti.')
a(123, S(123)); a(124, 'Introduction to the sūkta.')
a(125, N(125)); a(126, N(126)); a(127, N(127)); a(128, N(128)); a(129, N(129))
a(130, 'Here ends the Second Adhyāya in the Eighth Aṣṭaka.')
miss = [b['src'] for b in B if b['src'] not in E]
extra = [k for k in E if k not in BY]
assert not miss and not extra, (miss, extra)
out = [{'src': b['src'], 'en': E[b['src']]} for b in B]
(ROOT / 'vol28/contents_en.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf8')
print(len(out), 'rows')
