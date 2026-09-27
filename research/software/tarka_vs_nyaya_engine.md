# Tarka AI vs. Nyāya Engine — Comparison

Method: MD5 + line-diff of all shared files (`difflib`, context 0), plus
feature inventory from the two architecture audits. No merge, no edit, no
architecture decision — per the brief, §10 below stays open.

## 1. Headline: versions, not rivals

Both zips deliver the **same project** (`nyaya_engine/` package, same module
set, same class names, same 9-point `diagnose` order, same demo narrative).
"Tarka AI" (37.8 KB, 16 `.py`, 0 data, 0 tests) is the **older snapshot**;
"Nyāya Engine" (407 KB, 20 files incl. 1.2 MB corpus JSON) is the **newer
upgrade**. Every one of the 16 shared files diffs incrementally (largest:
README 174→233, engine 294→333, ontology_data +5 lines of `section=` kwargs);
no shared file was rewritten from scratch and no module exists only in the
older snapshot.

## 2. Duplicated functionality (identical in both)

- `WorldModel` tristate fact store + all six accessors.
- `Vyapti` / `VyaptiDatabase` data model and `(hetu,sadhya)` keying
  (byte-identical logic; comment-underline only).
- `diagnose()` 9-check order, `PRAMANA_STRENGTH` values, tristate
  svarūpasiddha split, stock-example messages (one emphasis-markup tweak).
- `Syllogism` svartha (3-step) + parartha (5-member) generation.
- `TarkaEngine.infer` pipeline (diagnose → syllogism → forward-chain assert
  as `"anumana"` → log), `infer_from_text` assume-hetu-then-infer pattern,
  all five bridge wirings (NLP/vision/RAG/upamāna/miner method names match).
- Apriori core (`apriori`, `generate_rules`, support/confidence semantics),
  BoW embeddings + cosine + guarded dense upgrade, `MockVisionBackend`
  KEYWORD_MAP, padārtha class hierarchy + 9/24/5 seed counts.

## 3. Complementary functionality (only in the newer Nyāya Engine)

1. `data/tarkasangraha_corpus.json` — 1,121 prebuilt chunks of the Athalye/
   Bodas (1930) edition, the engine's default Āpta corpus.
2. `tarka_corpus.py` — loader + bulk ingestor + keyword search.
3. `preprocess_corpus.py` — documented one-time rebuild script.
4. `test_engine.py` — 31-test offline suite (all pass; older snapshot has
   zero tests, so its demo flows were unverified).
5. `RAGShabda.query_passages` + `ingest_bulk` + `Document.excerpt/section` +
   `VectorStore.sources()` — the read/citation path behind `ground_term`.
6. `TarkaEngine.load_corpus/ground_term/keyword_search` + `corpus_loaded_
   chunks` + constructor auto-ingest flags.
7. Per-term `section=` references across `padartha.py`/`ontology_data.py`
   (older: coarse header comments only).
8. CLI option [12] (ground-term) + Part C of `demo.py` (grounding demo) +
   A.11 vyapti-asiddha demo (older demo jumps A.10→A.12 numbering).
9. Tuned RAG threshold 0.15→0.22 with documented rationale (denser corpus).
10. Minor robustness: `"backend"` tags on parse results, EOF-safe CLI input,
    early-return on empty vision detections, direct upamāna fact writes,
    single-term-only miner teaching (older allowed `only_single_term=False`
    multi-term `a+b` teaching).

## 4. Incompatible abstractions

None structural. The closest candidates, all judged **compatible evolutions**,
not forks:
- `Shabda.assert_fact` → `testify` (rename; same contract).
- `Upamana(target_obj)` → `(target_object)` + engine bypassing `analogize`
  (same resulting facts).
- `rule_miner.teach_engine(only_single_term=True)` → always-single-term
  (narrowing, documented as classical binary-vyāpti shape).
- `Document` gaining `section`, IDs `doc_<n>`→`doc<n>` (cosmetic).
- RAG threshold 0.15→0.22 (tuning, documented).

## 5. Reusable components (newer superset; older adds nothing)

The newer checkout is a strict functional superset: every capability of the
older snapshot exists there in equal-or-better form (tested, section-tagged,
corpus-grounded). Reuse recommendation is therefore "adopt the newer
snapshot as the baseline" — with the caveat in §10 that reuse ≠ doctrinal
correctness (see `traceability/conflicts.md`).

## 6. Dependencies

Identical: zero required (stdlib only), one optional auto-upgrade
(`sentence-transformers`), documented manual swap points (LLM callable, CV
backend, vector DB). No new dependency was introduced by the upgrade; the
corpus is vendored JSON, not a package.

## 7. Data-model conflicts

- None between the snapshots (all stores share schemas; additions are
  additive `section=`/`excerpt` fields).
- Latent model-vs-source tensions (e.g. `kind`/`vipaksha` stored-but-unread;
  tristate vs. `niścaya`; threshold-gated śabda vs. apta doctrine) are
  **common to both** and belong in `traceability/conflicts.md`, not here.

## 8. Likely integration boundaries (if work proceeds past Phase 0)

- `engine.py` (orchestrator) — single seam for any verifier work.
- `fallacy.py :: diagnose` — single validation seam; order and predicates are
  the natural unit of doctrinal review.
- `vyapti.py` — rule-schema seam (binary vs. qualified vs. kevala shapes).
- `syllogism.py` — proof-object seam (5 slots + svartha trace).
- `rag_shabda.py` + `tarka_corpus.py` — śabda/grounding seam (threshold,
  chunking, citation granularity).
- `nlp_bridge / vision_pratyaksha / upamana_engine / rule_miner /
  embeddings` — five proposal-only seams behind the firewall; safe to extend
  without touching the symbolic core.

## 9. Components that should remain independent

- Proposal (bridges, miner, corpus retrieval) vs. disposal (`diagnose` +
  `infer`): the firewall is the architecture's load-bearing wall; collapsing
  it (e.g. letting RAG/miner assert directly) would void the hello-hallucination
  guarantee both READMEs promise.
- Ontology seeds (`ontology_data.py`) vs. WorldModel facts vs. corpus text:
  three different epistemic kinds (lexical seed, asserted fact, cited passage)
  that the newer engine already keeps in separate stores — keep them separate.
- `preprocess_corpus.py` (build-time) vs. `tarka_corpus.py` (run-time):
  rebuilding the corpus must stay an explicit offline step.

## 10. Components whose meaning is unclear and require human review

1. Whether the 1,121-chunk paragraph-merged segmentation (no true § mapping;
   README admits "no reliable machine-parseable section markers") is an
   acceptable citation granularity for śabda-grounding, or whether a
   re-chunk by TS § is required before any claim of "source-backed" holds.
2. Whether the RAG 0.22 cosine threshold (BoW fallback) has any doctrinal
   standing as an *āpta* test, or is purely an engineering knob.
3. Whether miner-discovered 1→1 association rules may be called *vyāpti*
   without the source's tarka/sāmānya steps (both snapshots do so; the
   source's vyāptigraha account suggests not — see
   `classical_sources/vyapti_complete.md`).
4. Whether `kind` ("anvaya"/"vyatireka"/"both") and `vipaksha` should become
   live fields (kevala년까지 cases) or be dropped; both snapshots store-but-
   ignore them.
5. Whether the older snapshot needs any further attention at all (audit
   suggests no — it is fully subsumed), or should be archived as-is for
   provenance.
6. Final architecture is **expressly not decided here** per the brief.
