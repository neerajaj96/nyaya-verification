# Methodology — Research (Phase 1.5 extension)

Companion to `docs/methodology.md` (project method) and
`docs/research-question.md`. This file adds the Phase 1.5 four-way
distinction REQUIRED by the corpus expansion. From here on, every research
claim in this repository must carry exactly one of these labels:

## 1. Classical claim

What a specific source actually asserts — with stratum + layer + locator
(e.g. "SOURCE_VĀRTTIKA, NS 1-1-5 Vārttika, Jha Vol. 1 p.175: concomitance
alternatives trilemma"). Verifiable by opening the cited text. Uses the
seven SOURCE_* layer labels (`classical_sources/CORPUS_ARCHITECTURE.md`).

## 2. Cross-text synthesis

A conclusion obtained by COMPARING multiple sources — e.g. "the asiddha
threefold appears first-evidenced in the Pariśuddhi fragment and adopted in
TS §§24–27." A synthesis must name every source compared, quote each side,
and state what is retained/changed/introduced/disputed (cf. the transition
ledgers in `anumana_historical_development.md`). Syntheses are defeasible:
new acquisitions (e.g. G-UD-01) can overturn them. NEVER present a synthesis
as a classical claim of any single text.

## 3. Engineering abstraction

A computational representation introduced for experimental purposes — e.g.
`(hetu, sadhya)` keying, `PRAMANA_STRENGTH`, cosine thresholds. Abstractions
are judged by utility + honesty of labelling, never by antiquity. Every
abstraction must record the stratum it approximates (if any) and the
differences it introduces (the 15-row map in
`traceability/classical_to_code.md` is the current record).

## 4. Formal equivalence (strong claim — never assumed)

The claim that a computational representation FAITHFULLY captures a source
concept. This requires explicit argument: (a) the source passage, (b) the
formal definition, (c) a proof or systematic test-suite showing co-
extensiveness on stock cases AND edge cases (kevala, universal-pakṣa,
upādhi-conditional), (d) adjudicated open decisions it depends on. NOTHING
in this repository currently holds formal-equivalence status — including the
baseline's nine checks, whose verdicts are at most Supported-with-
Interpretation (see `traceability/classical_to_code.md`).

## Working rules

- New fields in `concept_matrix.json` must follow the corpus-only rule
  (empty = unacquired, never filled from general knowledge).
- New historical claims follow the transition-ledger format
  (retained/changed/introduced/disputed per transition).
- Disagreements are preserved (see `SCHOOL_DISAGREEMENTS.md`), never
  adjudicated silently; multi-theory preservation is a design constraint.
- D1–D10 stay OPEN until corpus-complete adjudication (see
  `traceability/CORPUS_IMPACT_ON_DECISIONS.md`).
