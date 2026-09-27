# Baseline Test Report

No test was modified to obtain these results. The baseline suite is executed
exactly as shipped, from inside the vendored directory (its flat imports
require that working directory).

## Runs

| Run | Location | Command | Python | Result |
|---|---|---|---|---|
| Pre-import (source archive unpacked) | `/tmp/opencode/ingest/nyaya/nyaya_engine/` | `python -m unittest test_engine -v` | 3.14.6 | **31 ran, 31 passed, 0 failed, 0 skipped, 0 errors** (~0.06 s) |
| Post-import (vendored baseline) | `src/nyaya_verification/legacy_engine/` | `python -m unittest test_engine -v` | 3.14.6 | **31 ran, 31 passed, 0 failed, 0 skipped, 0 errors** (~0.07 s) |

## Per-test listing (post-import run; identical pre-import)

OntologyTests (2): test_counts, test_describe_case_insensitive.
InferenceTests (11): test_valid_inference, test_ashrayasiddha,
test_svarupasiddha_absent, test_vyapti_asiddha, test_sadharana_over_wide,
test_asadharana_over_narrow, test_viruddha, test_satpratipaksha,
test_badhita, test_vyapyatvasiddha, test_forward_chaining.
NLPBridgeTests (4): test_parses_and_infers_valid,
test_never_hallucinates_unknown_rule, test_empty_input_fails_gracefully,
test_no_connective_fails_gracefully.
VisionBridgeTests (2): test_string_scene_detection,
test_low_confidence_is_skipped.
RAGShabdaTests (3): test_accepts_backed_fact, test_rejects_unbacked_fact,
test_rejects_with_empty_store.
UpamanaTests (3): test_classifies_similar_object,
test_refuses_dissimilar_object, test_refuses_with_no_references.
RuleMinerTests (3): test_apriori_support, test_generate_rules_confidence,
test_end_to_end_discovery.
EmbeddingTests (2): test_identical_text_similarity_is_one,
test_disjoint_text_similarity_is_zero.
CorpusGroundingTests (1): test_corpus_autoloads_and_grounds (limit=100).

Note: two informational `[RAG] Ingested passage … (doc101/doc102)` lines are
printed by the RAG tests' own fixture calls; they are not warnings or failures.

## Other test layers in this repository

`tests/{unit,classical,verification,integration}/` contain only placeholders
in this phase: there is no new verifier code to test, and per the Phase 1
scope no new tests were written. The baseline suite above is the complete
executed-test record.

## Baseline file hashes (post-import verification, SHA-256[:16], all IDENTICAL to source)

README.md 06cc43e3c677870e; demo.py c25934fe194b5a1b; embeddings.py
5cf68adb5b25fe26; engine.py b3a455178395e97a; fallacy.py a2bfdc70f83c3bfb;
interactive_cli.py e5d7c181e28dba36; nlp_bridge.py 443dce3c257a550a;
ontology_data.py 78235baff792ab69; padartha.py 7579ebec27e1459b; pramana.py
3ddfca73c7e33be8; preprocess_corpus.py 722cf719d585c3a9; rag_shabda.py
4a40437eb96f5b2d; rule_miner.py cf6842acd72c4fb8; syllogism.py
89e54806bb113d0a; tarka_corpus.py 30000edb92c6cfe0; test_engine.py
394ef6a1943339de; upamana_engine.py 7edc088ee18bc21f;
vision_pratyaksha.py 0708c40d52ec219f; vyapti.py 0cd3c85d769c8f15;
data/tarkasangraha_corpus.json 7f6a11b173a62d6c.

## Failures

None. There was nothing to hide and nothing hidden.
