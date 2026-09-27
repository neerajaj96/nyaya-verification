# Methodology

## The four levels (binding)

Adapted from the project README; repeated here because method is what this
phase produces:

1. **Primary-source claims** — Sanskrit quoted, edition + section cited.
2. **Scholarly interpretation** — marked as such, uncertainty stated.
3. **Engineering abstractions** — verifiable by reading/running code.
4. **Experimental hypotheses** — testable predictions, none run yet.

## Traceability rule

Every future formalization step must extend the existing chain rather than
assert equivalence:

```
PRIMARY TEXT → INTERPRETATION → EXISTING CODE → POSSIBLE COMPUTATIONAL FORMALIZATION
```

with each arrow carrying one of the Phase 0 verdicts (DIRECTLY SUPPORTED /
SUPPORTED WITH INTERPRETATION / WEAKLY SUPPORTED / NOT ESTABLISHED /
CONFLICTING / UNKNOWN). The chain for the 15 examined concepts is frozen in
`research/traceability/classical_to_code.md`; new concepts get new rows, not
edits to old verdicts.

## Standing prohibitions (from the Phase 0 mandate, carried forward)

- Do not "improve" the baseline to look more orthodox (it is frozen).
- Do not invent missing doctrine to fill implementation gaps.
- Do not modernize classical terminology.
- Do not equate Sanskrit concepts with Western logical concepts by surface
  similarity.
- Do not resolve D1–D10 by editing code or prose unilaterally: a decision
  leaves OPEN only via new dated evidence + a recorded ruling, with both
  linked from `OPEN_DECISIONS.md`.
- Do not modify tests to make them pass; report failures openly.

## Evidence handling

- Classical PDFs are not vendored (see `research/PROVENANCE.md`); citations
  use sūtra string + printed §/page + approximate PDF page.
- OCR is quoted with corrections marked (see `anumana_passages.md`
  conventions); uncertain readings stay uncertain.
- Quantitative claims (hit counts, test counts, hashes) are produced by
  executed commands recorded in the report files, never by recollection.
- The baseline is executed, never edited: `cd
  src/nyaya_verification/legacy_engine && python -m unittest test_engine -v`.
