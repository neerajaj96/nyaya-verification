# Datasets

- `external/` — third-party or primary-source-derived data used as-is.
  NOTE: the baseline's vendored source-text corpus
  (`src/nyaya_verification/legacy_engine/data/tarkasangraha_corpus.json`,
  1,121 chunks of the 1930 Athalye/Bodas edition) is NOT duplicated here;
  it stays with the frozen baseline. Any re-chunked (e.g. TS-§-aligned)
  corpus built in a later phase belongs here with its build script in
  `scripts/corpus/` and provenance recorded.
- `generated/` — machine-generated artifacts (git-ignored by default; see
  `.gitignore`). Do not commit large outputs.
- `evaluation/` — frozen evaluation sets (none exist yet in Phase 1).
