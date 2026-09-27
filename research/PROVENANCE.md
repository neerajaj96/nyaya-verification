# Provenance — Phase 0 → Repository Migration

The substantive research files in this directory were produced during Phase 0
(reconnaissance, September 2026) and migrated into this repository WITHOUT
changes to their findings: no rewriting, no re-interpretation, no silent
correction. `diff` of each migrated file against its Phase 0 original is
empty (verified at import).

## Phase 0 originals

Location at migration time: `/root/research/` (outside any VCS).

| Repository path | Phase 0 source | Status |
|---|---|---|
| research/source_audit.md | /root/research/source_audit.md | byte-identical |
| research/INITIAL_FINDINGS.md | /root/research/INITIAL_FINDINGS.md | byte-identical |
| research/classical_sources/anumana_passages.md | /root/research/classical_sources/anumana_passages.md | byte-identical |
| research/classical_sources/vyapti_complete.md | /root/research/classical_sources/vyapti_complete.md | byte-identical |
| research/classical_sources/hetvabhasa_complete.md | /root/research/classical_sources/hetvabhasa_complete.md | byte-identical |
| research/software/tarka_ai_architecture.md | /root/research/software/tarka_ai_architecture.md | byte-identical |
| research/software/nyaya_engine_architecture.md | /root/research/software/nyaya_engine_architecture.md | byte-identical |
| research/software/tarka_vs_nyaya_engine.md | /root/research/software/tarka_vs_nyaya_engine.md | byte-identical |
| research/software/baseline_inventory.md | /root/research/software/baseline_inventory.md | byte-identical |
| research/traceability/classical_to_code.md | /root/research/traceability/classical_to_code.md | byte-identical |
| research/traceability/conflicts.md | /root/research/traceability/conflicts.md | byte-identical |

## Files created during repository bootstrap (Phase 1, new — not Phase 0)

- research/software/baseline_test_report.md — pre/post-import 31/31 run log
  + hash table.
- research/traceability/OPEN_DECISIONS.md — the 10 conflicts from
  `conflicts.md` restated as OPEN decisions (D1–D10); no resolutions.
- research/PROVENANCE.md — this file.

## Baseline code provenance

`src/nyaya_verification/legacy_engine/` — verbatim copy of the Nyāya Engine
zip asset (Drive ID `1N2_axoGeEoY_MmfuzA_N4vTcY8kEIxm0`; payload files stamped
2026-07-21 08:30; no upstream VCS history). SHA-256 verified file-by-file at
import; see `software/baseline_test_report.md`. Original retained outside the
repo at `/tmp/opencode/ingest/nyaya_engine.zip` at import time.

## Classical source provenance

The PDFs themselves are NOT vendored in this repository (size + rights).
Bibliographic records sufficient to re-obtain them are in
`research/source_audit.md`:
(1) Annambhaṭṭa, *Tarka-Saṃgraha with Dīpikā*, tr. Swami Virupakshananda,
Sri Ramakrishna Math, Mylapore/Chennai, 2nd ed. 1994 (repr. 2001),
ISBN 81-7120-674-3;
(2) Annambhaṭṭa, *Tarka-Saṃgraha with Dīpikā and Govardhana's Nyāya-Bodhinī*,
ed. Y. V. Athalye, tr. M. R. Bodas, Bombay Sanskrit Series No. LV,
Bhandarkar Oriental Research Institute, Poona, 2nd ed. re-impression 1930.
Extraction method (`pdftotext -layout`) is documented in `source_audit.md`.

## Phase 1.5 additions (corpus expansion, 2026-09-27)

- `research/classical_sources/corpus/VOLUMES.md` — acquisition record for
  three Nyāya-sūtra volumes (Jha translation set): Vol. 1 ACQUIRED (SHA-256
  `2fb53c2e…f78`, Adhyāya I complete), Vol. 2 ACQUIRED (SHA-256
  `41b5ad47…376`, Adhyaya II complete), Vol. 3 NOT ACQUIRED (auth-walled;
  Gap G-NS-01). Working-text extractions live outside the repo.
- New research artifacts (all created in Phase 1.5, none modifying Phase 0
  files): `CORPUS_ARCHITECTURE.md`, `CORPUS_ACQUISITION_MATRIX.md`,
  `concept_matrix.json` (41 concepts, corpus-only rule), 
  `anumana_historical_development.md`, `vyapti_historical_development.md`,
  `hetvabhasa_historical_development.md`, `SCHOOL_DISAGREEMENTS.md`,
  `research/methodology.md` (four-way distinction),
  `traceability/CORPUS_IMPACT_ON_DECISIONS.md` (D1–D10 re-evaluation, none
  closed), `traceability/PHASE1_5_VALIDATION.md`.
- PDFs are NOT vendored (see `corpus/VOLUMES.md` + validation report).

## Phase 2B additions (targeted acquisition round 2, 2026-09-27)

- Jha Vol. III (Adhyāya III) via archive.org DLI open scan
  (`https://archive.org/download/in.ernet.dli.2015.461557/...Vol-3.pdf`,
  26,778,493 bytes, SHA-256
  `6d5004fc36af69a1e60134f663ba782d85e1d5c9eb77f180340477ea014d2115`,
  361 pages) + OCR derivative `_djvu.txt`. Identity verified same-edition-
  family (imprint/stamps/continuous pagination). Drive G-NS-01 file itself
  still ungapped and unclaimed. PDF kept OUTSIDE the repo.
- No Pariśuddhi/Dignāga files acquired (BLOCKED / NOT_SPECIFIED per
  `corpus/ACQUISITION_PHASE_2B.md`); comparison/extraction files for them
  deliberately not created.

## Vol. 4 addition (Phase 2B+1, 2026-09-27)

- Jha Vol. IV via Drive (link above; 35,673,655 bytes, SHA-256
  `13febcfe…f90f0f`, 354 pages). Adhyāyas IV–V complete, I–V coverage now
  whole same-edition. Adjudication: `traceability/JHA_VOL4_ADJUDICATION.md`.
  PDF kept OUTSIDE the repo (`/tmp/opencode/ingest/phase15/vol4.pdf`).
