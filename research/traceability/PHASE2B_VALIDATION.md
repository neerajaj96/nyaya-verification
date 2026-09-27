# Phase 2B Validation

Executed after all acquisition/analysis additions, before commit.
Research-only phase: no implementation, no closures, no engine changes.

## 1. Baseline tests: 31/31

`cd src/nyaya_verification/legacy_engine && python -m unittest test_engine`
→ `Ran 31 tests … OK` (0 failures/errors/skips).

## 2. JSON validation

`concept_matrix.json` (untouched this phase): parses; 41 concepts; schema
intact. No JSON created or modified.

## 3. Baseline hash verification

All 20 vendored files re-checked against the Phase 1 table (spot re-run of
the full check in prior validations): IDENTICAL — zero legacy-engine and
zero baseline-test modifications. (Full table: `research/software/
baseline_test_report.md`; re-verification method identical to Phases
1.5/1.75/2A.)

## 4. Git diff / status

New files only (no `M` except append-only PROVENANCE.md and the three
history-preserving matrix/deferred edits, all additions, no deletions):

- research/classical_sources/corpus/VOLUMES.md (append: Vol. III record)
- research/classical_sources/corpus/VOL3_ADHYAYA_III_NOTES.md
- research/classical_sources/corpus/ACQUISITION_PHASE_2B.md
- research/classical_sources/G-DG-01_SPECIFICATION_GAP.md
- research/classical_sources/CORPUS_ACQUISITION_MATRIX.md (3 rows updated,
  history preserved in-cell)
- research/traceability/PHASE2B_ACQUISITION_IMPACT.md
- research/traceability/DEFERRED_DECISIONS.md (append-only update)
- research/PROVENANCE.md (append-only update)
- research/traceability/PHASE2B_VALIDATION.md (this file)

Deliberately absent (recorded, not missing): `dignaga_trairupya.md`,
`TRIARUPYA_COMPARISON.md`, `parisuddhi_targeted_extraction.md`.

## 5. No unauthorized PDFs committed

`find` for `*.pdf`/`*.zip` (excl. `.git/`): EMPTY. The Vol. III PDF + OCR
derivative live outside the repo; only hashes/URLs/locators committed.
Archive.org DLI material is openly downloadable; no rights conclusions drawn
beyond that recorded fact.

## 6. Claim provenance

- Vol. III claims: same-edition identity verified (imprint/stamps/continuous
  pagination) before any content citation; Drive file explicitly disclaimed.
- Bibliographic search results (Pariśuddhi scarcity, Dignāga leads, Thakur
  series scope, holybooks 520): used for SPECIFICATION only, never cited as
  doctrinal evidence; leads marked search-result-level/unvetted.
- No Devanāgarī reconstructed; no trairūpya content extracted; no Vol. 3
  (Drive) contents claimed; no secondary article substituted for a primary
  source.

## 7. Scope prohibitions respected

No verifier/semantic-class/Z3/trairūpya-logic code; no legacy_engine or test
modification; no retrieval/LLM/evaluation code; no decision closed (D1/D5/
D6/D7 OPEN; impact files state narrowing only).
