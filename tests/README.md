# Tests

No new tests exist in Phase 1 — there is no new code to test, and per the
project mandate no tests were written to prefigure a verifier.

- `unit/` — future unit tests for new modules.
- `classical/` — future source-grounding tests (sūtra/example conformance).
- `verification/` — future verifier acceptance tests (BLOCKED on D1–D10).
- `integration/` — future end-to-end tests.

The complete executed-test record for this phase is the BASELINE suite:
`src/nyaya_verification/legacy_engine/test_engine.py`, 31/31 passing —
see `research/software/baseline_test_report.md`. Run it in place; do not
move, modify, or re-target it.
