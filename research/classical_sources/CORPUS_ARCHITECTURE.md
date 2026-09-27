# Corpus Architecture — Classical Sources in Layers

Binding change of scope (Phase 1.5): the research target is NOT "implement
Tarkasaṃgraha". It is: determine which inferential, epistemological,
debate-theoretic, and logical concepts from the Indian logical traditions can
be faithfully represented and mechanically verified — **preserving
differences** between texts, commentators, schools, historical periods, and
engineering abstractions. Tarkasaṃgraha is one important late pedagogical
synthesis (Tier 6), not the sole doctrinal authority.

## Source-layer labels (mandatory on every extracted passage)

- SOURCE_ROOT_TEXT — the mūla/sūtra stratum (Gautama; Annambhaṭṭa's mūla).
- SOURCE_BHĀṢYA — Vātsyāyana's Bhāṣya (Tier 1 commentary, full in Jha).
- SOURCE_VĀRTTIKA — Uddyotakara's Vārttika (Tier 1 sub-commentary, full).
- SOURCE_ṬĪKĀ — Vācaspati Miśra's Nyāya-Vārttika-Tātparyaṭīkā (Tier 2;
  fragments via Jha's notes only — no independent text acquired).
- SOURCE_LATER_COMMENTARY — Udayana's Tātparya-Pariśuddhi, Raghuttama's
  Bhāṣyachandra, "modern Logicians" (Navya-Nyāya) positions (fragments via
  Jha's notes only).
- SOURCE_TRANSLATOR_NOTE — Ganganatha Jha's / Virupakshananda's / Bodas's
  own observations, parallels, and caveats (never doctrine).
- SOURCE_ENGINEERING_INTERPRETATION — what baseline code does (never
  doctrine; lives in `traceability/`, not in source files).

Never collapse layers into "Nyāya says X."

## Tier 0 — Foundational Nyāya ✅ ACQUIRED

- Gautama, *Nyāya-sūtra*: Adhyāyas I–II in full via Jha Vols. 1–2
  (transliterated sūtra + English). Adhyāyas III–V: GAP (Vol. 3
  inaccessible; G-NS-01). Sūtra-level anchors verified in-corpus: 1.1.1
  (sixteen padārthas), 1.1.4–7 (four pramāṇas), 1.1.5 (trividha anumāna:
  pūrvavat/śeṣavat/sāmānyatodṛṣṭa), 1.1.32 (pañca avayavāḥ), 1.2.1–3
  (vāda/jalpa/vitaṇḍā), 1.2.4–9 (hetvābhāsa group incl. kalātīta 1.2.9),
  1.2.10+ (chala/jāti/nigrahasthāna openings), 2.1.1–7 (saṃśaya), 2.1.37–38
  (inference pūrvapakṣa/siddhānta), 2.2.1–12 (pramāṇa-saṃkhyā with
  aitihya/arthāpatti/sambhava/abhāva objector), 2.2 sound/word sections,
  vyakti/ākṛti/jāti + apoha debate at close of Adhyāya II.

## Tier 1 — Early Nyāya commentary ✅ ACQUIRED (in full, via translation)

- Vātsyāyana, *Nyāya-bhāṣya* (on I–II): complete in Jha (e.g. 1-1-5 Bhashya:
  *tatpūrvaka* = perception of probans–probandum relation + remembrance;
  pūrvavat/śeṣavat/sāmānyatodṛṣṭa exemplified: clouds→rain, river-full→
  rained-upstream, ants-with-eggs→coming-rain; 2-1-37 Bhashya: the three
  stock objections — obstruction/dam, demolition/nest, resemblance/mimic).
- Uddyotakara, *Nyāya-vārttika* (on I–II): complete in Jha (e.g. 1-1-5
  Vārttika: Bauddha smoke/fire invariable-concomitance alternatives —
  cause-effect vs. same-substratum-inherence vs. mere relation; peacock-scream
  reinterpreted as cloud-inference for past/present/future symmetry).

## Tier 2 — Classical systematic development ⚠️ FRAGMENTS ONLY

- Vācaspati Miśra (*Tātparyaṭīkā*): quoted in Jha notes (e.g. 2-1-37
  Tātparya gloss on *apramāṇam*; apoha-debate note on vyakti/ākṛti/jāti).
  No independent text acquired → Gap G-TT-01.
- Udayana (*Tātparya-Pariśuddhi*): quoted in Jha notes — load-bearing
  fragment: the **threefold asiddha** (āśraya/svarūpa/vyāpyatva by
  unknown-subject/probans/concomitance) at 1-2-8/9, the taxonomy TS later
  adopts. Also 2-1-37 notes. No independent text → Gap G-UD-01.
- Jayanta (*Nyāyamañjarī*), Bhāsarvajña (*Nyāyabhūṣaṇa*/*Nyāyasāra*):
  named in the Vol. 1 tail advertisement (Potter EIP contents) only; no
  material acquired → Gaps G-JY-01, G-BH-01. Relevance: independent
  classical systematizations whose hetvābhāsa/pramāṇa treatments must be
  checked before any cross-period synthesis.

## Tier 3 — Vaiśeṣika ⚠️ NOT ACQUIRED

- Kaṇāda, *Vaiśeṣika-sūtra*; Praśastapāda, *Padārthadharmasaṃgraha*: no
  material in the acquired corpus. The TS ontology (dravya/guṇa/karman…)
  presupposes this stratum, but nothing here may be cited for Vaiśeṣika
  positions. Gaps G-VS-01, G-PR-01 (priority P1: the baseline's ontology
  seeds can only be validated against TS itself until then).

## Tier 4 — Buddhist logic ⚠️ INCIDENTAL-ONLY (no independent texts)

Relevance established in-corpus, texts NOT acquired:
- Dignāga ("Diimlga"/Dinnaga in OCR): pratyakṣa definition
  (*kalpanāpoḍha*) refuted at length in 1-1-4 discussion (Vol. 1);
  trairūpya-adjacent pakṣa/sapakṣa strictures ("subsistence in sapakṣa
  only") cited at 1-1-5/hetvābhāsa passages.
- Dharmakīrti: not distinctly isolated in the extracted window (Bauddha
  objectors generally); do NOT attribute specific Dharmakīrti theses.
- Apoha doctrine: Bauddha "negation of the contrary" as word-denotation,
  debated at length vs. Nyāya vyakti/ākṛti/jāti (Vol. 2, close of Adhyāya II).
- Anumāna-for-oneself/two-factor Parisuddhi-adjacent formulations appear in
  debate with Bauddha positions on smoke/fire concomitance (1-1-5 Vārttika).
Gaps G-DG-01 (Dignāga), G-DK-01 (Dharmakīrti): priority P1 — Buddhist
trairūpya is the obvious comparator for any vyāpti formalization, and it
must be sourced, not reconstructed.

## Tier 5 — Navya-Nyāya ⚠️ INCIDENTAL-ONLY

- Gaṅgeśa (*Tattvacintāmaṇi*): no text acquired. The Vol. 1 tail
  advertisement (Potter EIP Vol. II note) places coverage "up to the time of
  Gangesa (c. 1350 A.D.)" — cited as publisher's dating, not established fact.
- Later Navya-Nyāya technical literature: present only as Jha's "modern
  Logicians" (e.g. Jāti redefined as bare similarity/dissimilarity without
  invariable concomitance, Vol. 1 jāti section). Gaps G-GG-01, G-NN-01
  (priority P2; the vyāpti *vyāpāra*/avacchedaka machinery lives here and
  matters for D5/D7, but after Buddhist and Vaiśeṣika gaps).

## Tier 6 — Pedagogical synthesis ✅ ACQUIRED (retained in full)

- Annambhaṭṭa, *Tarkasaṃgraha* + *Dīpikā* (two editions: Virupakshananda 1994,
  Athalye/Bodas 1930) + Govardhana's *Nyāya-Bodhinī* (in the 1930 ed.).
  Status unchanged from Phase 0; now explicitly ONE tier among seven, and
  the *latest* systematic voice in the acquired corpus — its formulations
  (e.g. the fivefold hetvābhāsa list, the guarded vyāpti definition) must be
  read as synthesis, with older strata (Tier 0–1 lists, Udayana fragments)
  preserved alongside rather than overwritten.

## Gap register (summary; detail in CORPUS_ACQUISITION_MATRIX.md)

G-NS-01 (Jha Vol. 3 / NS III–V) · G-TT-01 (Tātparyaṭīkā) · G-UD-01 (Pariśuddhi)
· G-JY-01 (Nyāyamañjarī) · G-BH-01 (Bhāsarvajña) · G-VS-01 (Vaiśeṣika-sūtra) ·
G-PR-01 (Praśastapāda) · G-DG-01 (Dignāga) · G-DK-01 (Dharmakīrti) ·
G-GG-01 (Gaṅgeśa) · G-NN-01 (later Navya-Nyāya). Acquisition rule: download
or cite only actually available sources; never invent contents for gaps.
