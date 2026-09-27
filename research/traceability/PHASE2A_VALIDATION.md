# Phase 2A Validation

Executed after all pre-gate/constraint additions, before commit.
Research-specification phase: no production code, no adjudication closures,
no engine changes.

## 1. Baseline tests: 31/31

`cd src/nyaya_verification/legacy_engine && python -m unittest test_engine`
→ `Ran 31 tests … OK` (0 failures/errors/skips). Matches all prior records.

## 2. JSON validation

`concept_matrix.json` (untouched this phase): parses; 41 concepts; 12 keys
each. No JSON created or modified — correctly, since 2A produced markdown
specifications and registers, not records.

## 3. Git diff / status

`git status --short` shows ONLY 10 new files under `research/traceability/`:

- D1_PAKSA_PREGATE.md, D5_UPADHI_PREGATE.md, D6_COUNTEREXAMPLE_PREGATE.md,
  D7_VYAPTI_PROMOTION_PREGATE.md
- NYAYA_EARLY_PROMOTION_MODEL.md, HETVABHASA_NONCOLLAPSE_CONSTRAINTS.md,
  STRATUM_SCOPED_SEMANTICS.md, DEFERRED_DECISIONS.md,
  FUTURE_IMPLEMENTATION_CONSTRAINTS.md (incl. NOT DECIDED IN PHASE 2A),
  PHASE2A_VALIDATION.md (this file)

No `M` (modified) entries; no deletions. No tracked Phase 0/1/1.75 file
altered. No code, test, dataset, experiment, or script file touched.

## 4. Legacy SHA-256 verification

All 20 vendored files re-checked against the Phase 1 table: IDENTICAL.
Zero legacy-engine modifications; zero baseline-test modifications.

## 5. No PDFs committed

`find` for `*.pdf`/`*.zip` (excl. `.git/`): EMPTY.

## 6. Source-claim provenance

Every new file uses the §2 evidence labels (NS_EXPLICIT … INSUFFICIENT_
EVIDENCE) per statement or section; every classical claim carries stratum +
locator (sūtra/section/Jha page); OCR-image readings transcribed with
ledger references to the Phase 1.75 targeted files; prohibited
extrapolations listed per pre-gate (D1 P1–P5; D5 §4; D6 N1–N5). No
engineering abstraction is cited as classical evidence (audited: D5 §4 and
D7 frequency sections explicitly forbid the equations). No Buddhist/Navya-
Nyāya position inferred from absence (STRATUM_SCOPED_SEMANTICS marks them
NOT_ACQUIRED throughout).

## 7. Scope prohibitions respected

No VyaptiVerifier/HetvabhasaClassifier/Z3/retrieval/LLM code; no
"algorithm" language where sources give none (D7 + promotion model state
this explicitly); D1/D5/D6/D7 remain OPEN (impact/specification only);
NOT DECIDED list covers all §12 items (vyāpti definition, pakṣatā model,
upādhi proof, counterexample semantics, hetvābhāsa classifier,
reconciliation, NN formalization, state machine, Z3, retrieval semantics).
