# Architecture

## Phase-1 architecture: baseline + evidence, no verifier

This repository is at Phase 0/1: **reproducible baseline plus research
record**. The only executable logic is the frozen baseline; the only active
record is the evidence. Later phases may add a verifier — nothing here
prefigures its design.

```
nyaya-verification/
├── README.md / LICENSE / CITATION.cff / pyproject.toml / .gitignore
├── docs/            # question, this file, foundations, methodology
├── research/        # frozen Phase 0 evidence + baseline records + D1–D10
├── src/nyaya_verification/
│   ├── __init__.py  # package marker + scope guard (no logic)
│   ├── BASELINE.md  # provenance wrapper (no logic)
│   └── legacy_engine/   # VERBATIM baseline (do not modify; not packaged)
├── tests/{unit,classical,verification,integration}/  # placeholders only
├── datasets/{external,generated,evaluation}/         # empty scaffolding
├── experiments/{vyapti_probe,baselines,results}/    # empty scaffolding
└── scripts/{corpus,evaluation,experiments}/          # empty scaffolding
```

## Baseline placement rationale

The baseline is a flat, package-less module set (siblings import each other
as top-level modules; no `__init__.py` upstream). Repackaging it into the
`nyaya_verification` namespace would require rewriting its imports — i.e.
modifying the artifact under study. It is therefore vendored verbatim under
`legacy_engine/` (isolated namespace, excluded from the build) and run
in-place. See `src/nyaya_verification/BASELINE.md`.

## Load-bearing boundaries (carried over from the baseline's own design)

- **Proposal vs. disposal.** Bridges/miner/retrieval may only *propose*
  facts, parses, or rules; only the fallacy diagnostic disposes. Any future
  verifier must preserve this firewall or justify breaking it in an
  OPEN_DECISIONS update — never silently.
- **Ontology seeds vs. asserted facts vs. cited passages.** Three epistemic
  kinds, three stores; do not merge them.
- **Build-time vs. run-time corpus work.** Re-chunking/re-OCR is an explicit
  offline step (`scripts/corpus/`), never an ambient side effect of inference.

## What must NOT be created yet (binding)

No `VyaptiVerifier`, `HetvabhasaClassifier`, counter-instance search,
generate-verify-correct loop, Z3 integration, LLM generation layer, or new
retrieval algorithm. The `tests/verification/`, `experiments/vyapti_probe/`,
and `scripts/` trees exist as addressed scaffolding so later phases have
somewhere to go — they contain no implementation and no experiment has been
run. Creating verifier-shaped code in this phase would violate the
"reproducible baseline, not immediate rewrite" mandate and is blocked until
D1–D10 are adjudicated.
