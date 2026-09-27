# Representation Stress Test (Minimum Core + Navya-Nyāya + Dignāga)

Core under test (from brief Part VI — tested, not adopted):
`claim_id, source_provenance, tradition_scope, paksha, sadhya, hetu,
hetu_qualifier, anvaya_evidence[], vyatireka_evidence[],
candidate_counterexample, interpretation_provenance`

## A. Nyāya inference — REPRESENTABLE (with indexed semantics)

NS 2.1.38-style case fits: paksha=mountain/river, hetu + viśeṣaṇa-string in
hetu_qualifier (foam/hosts/ṣaḍja), anvaya_evidence[] = kitchen exhibits,
vyatireka_evidence[] = lake/ayogolaka exhibits, candidate_counterexample =
TYPED S5-record. TS case fits with guard-citations in interpretation_
provenance. Verdict: CAPABLE, provided every field except claim_id carries
stratum tags (NS-mode vs TS-mode per STRATUM_SCOPED_SEMANTICS.md).

## B. Navya-Nyāya inference — NOT HOLDABLE without flattening (failure catalog)

Test proposition (maṅgala-vāda shape): pakṣatā delimited by
pakṣatāvacchedaka over a dharma-complex with vyadhikaraṇa relations.
Failures of the core:
- F-B1: `paksha` (flat string) cannot hold avacchedaka-delimited loci —
  requires nested delimitation structure (NOT designed here).
- F-B2: `hetu_qualifier` (string) cannot hold vyadhikaraṇa-dharmāvacchinna-
  abhāva relations or counterpart-qualification (Book II pp. 23–24 shapes) —
  requires relation objects with locus-indexed counterparts.
- F-B3: `anvaya_evidence[]/vyatireka_evidence[]` cannot hold kevalānvayi
  viṣayatā-debates (TC L14325: avṛtti-unavailability disputes) — absence of
  loci breaks list semantics; needs absence-structure representation.
- F-B4: `candidate_counterexample` (singular) cannot hold the
  suspected-vs-real (jñāna vs vastugatyā) distinction — needs the D5
  3-state structure, not a slot.
- F-B5: upādhi-vāda shapes (sādhanāvacchinna-sādhya-vyāpakatva) need
  pervasion-over-delimited-domains, unrepresentable in flat fields.
Verdict: core INCAPABLE for NN-root shapes. REQUIRED (not designed):
nested qualification, delimitation, locus-indexed absence, relation
direction, 3-state defeater — as RESEARCH HYPOTHESIS H3 (constituent
structures, dispute-indexed). Explicitly NOT concluded: "NN is a knowledge
graph / type theory / formal logic" — no source supports such claims here.

## C. Dignāga's structure — UNTESTABLE with supplied volume (honest failure)

Ch. II absent; Tibetan body unreadable; restoration un-OCR'd. The core can
hold NOTHING Dig-specific beyond foreword-level chapter topics. Attempting
the fit would fabricate. Verdict: UNRESOLVED pending G-DG-01 witness.

## Dignāga stress proposition

"Nyāya vyāpti and Dignāga trairūpya can be represented by the same
computational object." — Verdict: UNRESOLVED (not even PARTIALLY SUPPORTED:
zero trairūpya wording in corpus; zero Dig content beyond chapter
headings). Why: (1) trairūpya unknown in wording, let alone semantics;
(2) vyāpti itself stratum-split (NS-practice vs TS-term vs NN-pending);
(3) equation would need A/B/C/D-graded evidence for BOTH relata — Dig side
entirely D. The equation stays FORBIDDEN (rule 9) until G-DG-01.

## Field disposition (from brief Part VI questions)

- Remain valid cross-traditionally: claim_id, source_provenance,
  tradition_scope, interpretation_provenance (all provenance/status slots).
- Must become tradition-indexed: paksha, sadhya, hetu (role-split).
- Must become stratum-indexed: hetu_qualifier, anvaya/vyatireka_evidence[],
  candidate_counterexample (→ typed S5 records).
- Too Nyāya-specific as bare strings: all semantic nouns (see invariants).
- Missing: nested qualification/delimitation; locus-indexed absence;
  defeater 3-state; doubt-track (S1/CINTĀ) linkage; opponent-move typing.
- Must NOT be introduced yet: `vyapti_status` (rule 15); trairūpya object;
  confidence/probability fields (rule 14); unified hetu-validity predicate.
