# Baseline Engine Record — `legacy_engine/`

## What this directory is

`legacy_engine/` is a **verbatim vendored copy** of the pre-existing Nyāya
Engine as delivered (zip asset, all payload files stamped `2026-07-21 08:30`,
no VCS history). Its purpose is a **reproducible baseline, not a rewrite**:
pin the exact behavior Phase 0 audited so later research phases can measure
against it.

## Non-modification guarantee

- All 20 files (19 Python + 1 JSON corpus) are **byte-identical** to the
  source archive (SHA-256 verified file-by-file at import; see
  `research/software/baseline_test_report.md` for the hash table).
- No `__init__.py` was added inside this directory and no import was
  rewritten: the baseline is a flat, package-less module set (siblings import
  each other as top-level modules, e.g. `from vyapti import VyaptiDatabase`).
  Repackaging it would modify the artifact under study, so it is deliberately
  left unpackaged and excluded from the build (`pyproject.toml` packages only
  `nyaya_verification`, and this directory has no `__init__.py`, so the
  baseline ships as data, not as an installed package).
- Stale `__pycache__/` bytecode from the source location was NOT copied.
- The baseline's own `README.md` is preserved inside this directory and
  remains its user documentation; this file is only the provenance wrapper.

## How to run the baseline (read-only usage)

```bash
cd src/nyaya_verification/legacy_engine
python -m unittest test_engine -v   # expect 31/31 OK (stdlib only)
python demo.py                       # end-to-end demonstration
python interactive_cli.py            # 14-option REPL
```

Do not edit files here to fix behavior. If a conflict from
`research/traceability/OPEN_DECISIONS.md` is ever resolved toward a code
change, the change belongs in a NEW module outside this directory, with the
baseline kept intact for comparison.

## Recorded baseline facts

- baseline_engine_revision: zip asset `nyaya_engine.zip` (Drive ID
  `1N2_axoGeEoY_MmfuzA_N4vTcY8kEIxm0`); no git history exists upstream;
  per-file SHA-256 in `research/software/baseline_test_report.md`.
- baseline_test_count: 31; baseline_tests_passed: 31 (verified pre- and
  post-import on Python 3.14.6).
- baseline_dependencies: zero required (stdlib only); one optional guarded
  import (`sentence-transformers`, not installed — BoW fallback active).
- baseline_source_location: original zip retained outside this repo
  (`/tmp/opencode/ingest/nyaya_engine.zip` at import time); provenance chain
  in `research/PROVENANCE.md`.
