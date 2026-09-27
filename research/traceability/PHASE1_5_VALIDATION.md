# Phase 1.5 Validation

Executed 2026-09-27 after all research additions, before commit. No
implementation exists in this phase; validation concerns non-modification,
test stability, format validity, and licensing hygiene.

## 1. Baseline tests: 31/31

`cd src/nyaya_verification/legacy_engine && python -m unittest test_engine`
→ `Ran 31 tests … OK` (0 failures, 0 errors, 0 skips). Matches the Phase 1
record (`research/software/baseline_test_report.md`).

## 2. Legacy engine unchanged

SHA-256[:16] of all 20 vendored files re-checked against the Phase 1 table:
all IDENTICAL (see command log in §6). No file added, removed, or edited
under `src/nyaya_verification/legacy_engine/`; no `__init__.py` introduced;
no baseline test touched.

## 3. Baseline hashes unchanged — confirmed (§2).

## 4. JSON valid

`concept_matrix.json`: parses cleanly; 41 concepts; every entry carries all
12 required keys; every `source_passages`/`definitions` item carries
{layer, locator, text}. Builder script retained outside the repo
(`/tmp/opencode/ingest/phase15/concept_builder.py`, not committed).

## 5. No source files committed against licensing

`find` for `*.pdf`/`*.zip` under the repo (excluding `.git/`): EMPTY. The
three Nyāya-sūtra volumes + two Tarkasaṃgraha editions + engine zips live
outside the repo; only SHA-256 hashes, bibliographic records, and short
quoted passages (fair-use research excerpts with locators) are committed —
see `classical_sources/corpus/VOLUMES.md` and `research/PROVENANCE.md`.

## 6. Provenance recorded

`research/PROVENANCE.md` extended with a Phase 1.5 section (append-only;
Phase 0 rows untouched). Per-volume provenance (Drive IDs, hashes, coverage,
OCR, layers) in `classical_sources/corpus/VOLUMES.md`.

## 7. Git diff review (intended additions only)

`git status --short` shows ONLY: 12 new research files + PROVENANCE.md
modification (append). No modified code, no modified Phase 0 research, no
deleted files:

- research/classical_sources/corpus/VOLUMES.md
- research/classical_sources/CORPUS_ARCHITECTURE.md
- research/classical_sources/CORPUS_ACQUISITION_MATRIX.md
- research/classical_sources/concept_matrix.json
- research/classical_sources/anumana_historical_development.md
- research/classical_sources/vyapti_historical_development.md
- research/classical_sources/hetvabhasa_historical_development.md
- research/classical_sources/SCHOOL_DISAGREEMENTS.md
- research/methodology.md
- research/traceability/CORPUS_IMPACT_ON_DECISIONS.md
- research/traceability/PHASE1_5_VALIDATION.md (this file)
- research/PROVENANCE.md (append-only extension)

## 8. Scope prohibitions respected

No VyaptiVerifier, HetvabhasaClassifier, Z3, legacy_engine alteration,
baseline-test alteration, LLM loop, retrieval code, or silent conclusion
revision. D1–D10 all remain OPEN (see CORPUS_IMPACT_ON_DECISIONS.md: 7
affected/reframed, 1 unaffected, 0 closed).
