# Phase 1.75 Validation

Executed 2026-09-27 after all extraction/analysis additions, before commit.
Research-only phase: no implementation, no adjudication, no engine changes.

## 1. Baseline tests: 31/31

`cd src/nyaya_verification/legacy_engine && python -m unittest test_engine`
→ `Ran 31 tests … OK` (0 failures/errors/skips). Matches Phase 1 and 1.5 records.

## 2. Baseline hashes: UNCHANGED

All 20 vendored files re-verified against the Phase 1 SHA-256 table —
IDENTICAL. No legacy-engine change, no baseline-test change.

## 3. JSON: valid, unmodified

`concept_matrix.json` re-validated (41 concepts, 12 keys each); untouched
this phase (no JSON created or modified — correctly, since Task A produced
markdown extractions and Task C produced analysis, not records).

## 4. Repository diff: research additions only

`git status` shows ONLY new files (no `M` entries except PROVENANCE.md's
Phase 1.5 append, already committed in 7fb60c4 — this phase touches no
tracked file):

- research/classical_sources/targeted/ (4 passages + index)
- research/classical_sources/corpus/ACQUISITION_PHASE_1_75.md
- research/classical_sources/CROSS_STRATUM_EVIDENCE.md
- research/traceability/PHASE1_75_DECISION_IMPACT.md
- research/traceability/D6_EPISTEMIC_STATUS_NOTES.md
- research/traceability/D7_VYAPTI_PROMOTION_EVIDENCE.md
- research/traceability/PHASE1_75_VALIDATION.md (this file)

## 5. No copyrighted PDFs committed

`find` for `*.pdf`/`*.zip` (excl. `.git/`): EMPTY. Page images
(`img_*.png`) remain outside the repo; their readings are transcribed in the
targeted files. Vol. 3 was not acquired (nothing to leak).

## 6. No unsupported source claims

Every new file carries layer labels, locators, OCR-integrity notes, and a
mandatory does-NOT-establish section (targeted files) or explicit
non-adjudication framing (decision files). Spot-checks: no Devanāgarī
reconstructed from memory; no trairūpya reconstructed; no Vol. 3 contents
claimed; G-UD-01 marked unresolved (not substituted); prakaraṇasama ↔
satpratipakṣa mapping refused with a non-collapse table.

## 7. Provenance for new files

Covered by: `corpus/VOLUMES.md` (Phases 1.5, pre-existing) +
`corpus/ACQUISITION_PHASE_1_75.md` (new attempts with UTC timestamps) +
`targeted/TARGETED_EXTRACTION_INDEX.md` (OCR-integrity summary). A
PROVENANCE.md Phase 1.75 append is NOT added (no new vendored artifacts, no
PDFs acquired — nothing to register beyond the acquisition file itself).

## 8. Scope prohibitions respected

No verifier/classifier/Z3/LLM/retrieval code; no legacy_engine or test
modification; no semantic-decision changes (all prior verdicts untouched);
D1/D5/D6/D7 remain OPEN (impact-only analysis).
