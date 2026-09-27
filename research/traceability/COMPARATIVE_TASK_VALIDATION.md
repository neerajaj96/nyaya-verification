# Comparative-Task Validation (Dignāga + Navya-Nyāya Adjudication)

Executed before commit. Research-only: no implementation, no closures.

## 1. Baseline tests

- Legacy suite (cwd `src/nyaya_verification/legacy_engine`):
  `python -m unittest test_engine` → 31/31 OK (re-run at validation;
  0 failures/errors/skips).
- New identity tests: none added this task (Vol. 4 tests stand, unmodified).
  (A comparative-task test file is NOT added: there is no new executable
  claim to check — case-selection spec is explicitly unrunnable.)

## 2. JSON validation

`concept_matrix.json` untouched: parses; 41 concepts. No JSON created.

## 3. Baseline hash verification

All 20 vendored files vs Phase 1 table: IDENTICAL (method as prior phases).
Zero legacy-engine / baseline-test modifications.

## 4. Git diff / status

New files only (no `M` except append-only PROVENANCE.md, history-preserving
matrix/deferred edits — additions, no deletions):
- research/classical_sources/comparative/ (6 files: PRAMANASAMUCCAYA_,
  TATVACINTAMANI_, HISTORY_NAVYA_NYAYA_BENGAL_ADJUDICATION,
  CROSS_TRADITION_COMPARISON, COMPUTATIONAL_INVARIANTS,
  REPRESENTATION_STRESS_TEST)
- research/traceability/COMPARATIVE_D1_D10_IMPACT.md,
  R_REQUIREMENTS_ASSESSMENT.md, MINIMUM_NEXT_EXPERIMENT.md,
  ARCHITECTURE_COMPARISON_NOTES.md, COMPARATIVE_TASK_VALIDATION.md (this)
- Modified: CORPUS_ACQUISITION_MATRIX.md (3 rows, history in-cell),
  DEFERRED_DECISIONS.md + PROVENANCE.md (appends)

## 5. No unauthorized PDFs committed

`find` for `*.pdf`/`*.zip` (excl. `.git/`): EMPTY. All three PDFs outside
repo; hashes/URLs only.

## 6. Safety checklist (brief FINAL SAFETY CHECK)

- [x] No D1–D10 silently CLOSED (all OPEN; impact files state statuses).
- [x] No `vyapti_status` introduced (grep-verified absent; rule restated).
- [x] No Dignāga concept equated with Nyāya (trairūpya UNRESOLVED; hetucakra content D).
- [x] No Navya-Nyāya reduced to predicate logic/KG/type-theory (failures F-B1–B5 catalogued; H3 hypothesis-labelled).
- [x] Historical vs philosophical claims separated (firewall file + F1–F4).
- [x] Translation vs root claims separated (restoration/Tibetan/roman issues recorded; my Sanskrit parsings marked provisional).
- [x] Strata preserved (7–8 labels incl. HISTORICAL_STUDY; Rahasya-attribution caution).
- [x] Engineering readings labelled (H1/H2/H3 + N-requirements as hypotheses).
- [x] No algorithmic claim attributed classically (F2 procedure-like ≠ procedure; tarka illustration dialectical).
- [x] No implementation code added (diff is docs-only).
- [x] Tests unmodified (legacy suite + Vol.4 tests untouched).
- [x] Legacy engine untouched (hashes).
- [x] Provenance on important conclusions (evidence tables per file with source/page/section).
- [x] Uncertainty preserved (D-statuses, UNVERIFIED/UNRESOLVED markings, BLOCKED slots).
