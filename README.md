# Nyāya Verification

Research project repository for mechanically grounded verification of
inference in the Nyāya tradition — especially *vyāpti* (invariable
concomitance) and *hetvābhāsa* (fallacious reasons) — using a symbolic
system grounded in primary-source analysis.

## Research objective

Investigate mechanically grounded verification of inference, especially
vyāpti and hetvābhāsa, using a symbolic system grounded in primary-source
analysis. The work proceeds from Annambhaṭṭa's *Tarkasaṃgraha* with *Dīpikā*
(two editions audited in Phase 0) through a preserved software baseline
toward — in later phases only — a source-traceable verifier.

## Methodological distinction (binding on all work in this repo)

This project does NOT claim that its computational abstractions are identical
to the complete historical/philosophical doctrines. Every claim must be
labelled as one of:

1. **Primary-source claims** — what the mūla / Dīpikā / commentaries state
   (Sanskrit quoted, edition + section cited).
2. **Scholarly interpretation** — what a reading of the sources takes them to
   mean (marked as interpretation, with uncertainty stated).
3. **Engineering abstractions** — what the code actually implements
   (verifiable by reading and running it).
4. **Experimental hypotheses** — what a future experiment would test
   (not yet run in Phase 0/1).

Conflating levels — e.g. presenting a threshold, flag, or search procedure as
doctrine — is the exact failure this repository is built to prevent. See
`docs/methodology.md` and `research/traceability/OPEN_DECISIONS.md`.

## Current status: Phase 0 — reconnaissance complete

**No new verifier has yet been implemented.** There is no `VyaptiVerifier`,
no `HetvabhasaClassifier`, no counter-instance search, no generate-verify-
correct loop, no Z3 integration, no LLM generation layer, no new retrieval
algorithm in this repository — by design (see `docs/architecture.md`).
Phase 1 establishes only the reproducible baseline below plus the research
record. Start with `research/INITIAL_FINDINGS.md`.

## Existing baseline

`src/nyaya_verification/legacy_engine/` preserves the pre-existing Nyāya
Engine **verbatim** (byte-identical, SHA-256 verified; provenance and hashes
in `research/PROVENANCE.md` and `research/software/baseline_test_report.md`).
It is the newer of the two audited snapshots and the functional superset of
the older "Tarka AI" snapshot (`research/software/tarka_vs_nyaya_engine.md`).

- Baseline revision: zip asset `nyaya_engine.zip` (payload 2026-07-21; no
  upstream git history exists — per-file hashes serve as the revision ID).
- Test status: **31/31 passing** (`python -m unittest test_engine -v`, stdlib
  only), verified before AND after migration. Full log:
  `research/software/baseline_test_report.md`.
- Dependencies: zero required (Python standard library); one optional
  guarded import (`sentence-transformers`, not installed — pure-Python
  fallback active). No network, keys, GPU, or services.
- Run it (read-only): `cd src/nyaya_verification/legacy_engine &&
  python -m unittest test_engine -v`. Do not edit it; see `src/nyaya_verification/BASELINE.md`.

## Research questions (established in Phase 0 — not invented here)

From `research/INITIAL_FINDINGS.md` §10, restated in `docs/research-question.md`:

1. How should *pakṣatā* (doubt + proof-absence + desire to infer) gate a
   verifier's control flow? (D1)
2. What may count as a counterexample, and what does *niścaya* /
   same-substratum (*sāmānādhikaraṇya*) mean computationally? (D6)
3. What proves an *upādhi*, and what promotes a mined concomitance to
   *vyāpti* — i.e. is the vyāpti research direction viable, and with which
   tarka/sāmānya stages? (D5, D7)
4. What is the scope for kevala/anupasaṃhārin reasons — implement or
   explicitly exclude? (D8, D4)
5. What defeat ordering and balance test replace the unattested strength
   table and one-sided satpratipakṣa check? (D2, D3, D10)
6. What citation granularity makes source-grounded retrieval honest? (D9)

## Repository map

- `docs/` — research question, architecture, classical foundations, methodology.
- `research/` — Phase 0 evidence (frozen) + baseline inventory/test report +
  open decisions (D1–D10, all OPEN).
- `src/nyaya_verification/legacy_engine/` — verbatim baseline (do not modify).
- `tests/{unit,classical,verification,integration}/` — placeholders; no new
  tests exist yet because no new code exists yet.
- `datasets/`, `experiments/`, `scripts/` — empty scaffolding for later
  phases (no experiments run in Phase 0/1).

## License and citation

New research-repo files: MIT (see `LICENSE`); the vendored baseline retains
its original local-use terms (quoted in `LICENSE`). Cite via `CITATION.cff`;
classical-source bibliography lives in `research/source_audit.md`.
