# Baseline Inventory — Existing Nyāya Engine (pre-import inspection)

Inspection-only. The existing implementation was NOT modified. All claims were
established by reading the 20 delivered files, hashing them, and executing the
bundled test suite. See also `nyaya_engine_architecture.md` (full audit) and
`tarka_vs_nyaya_engine.md` (relation to the older Tarka AI snapshot).

## 1. Complete engine under inspection

Source location: `/tmp/opencode/ingest/nyaya_engine.zip` (407 KB, Drive ID
`1N2_axoGeEoY_MmfuzA_N4vTcY8kEIxm0`), unpacked read-only to
`/tmp/opencode/ingest/nyaya/nyaya_engine/`. The older "Tarka AI" zip
(`17HROei7KAaJdyjqz03o7C4SUDJ1Sn_Hr`, 37.8 KB) is a strictly older snapshot
of the same package and is NOT the baseline; it contributes zero unique files.

## 2. Git history

NONE. The asset is a zip archive, not a git checkout: no `.git` directory,
no commit hashes, no tags, no author metadata. All 20 payload files carry zip
timestamps `2026-07-21 08:30` (uniform — likely repack time, not authorship
time). There is therefore no "current stable revision" in version-control
terms. The reproducible baseline identifier adopted for this project is the
combination below (§3); it is recorded in every downstream artifact instead
of a commit hash.

## 3. Stable-revision identifier (adopted, since no VCS history exists)

- Archive: `nyaya_engine.zip`, 407 KB (1,353,877 bytes payload, 22 zip entries).
- Payload: 19 Python files + 1 JSON corpus + 2 directory entries.
- SHA-256 (first 16 hex) per file, computed 2026-09-27:

| File | SHA-256[:16] |
|---|---|
| README.md | 06cc43e3c677870e (captured post-import; content verified by full read) |
| demo.py | c25934fe194b5a1b |
| embeddings.py | 5cf68adb5b25fe26 |
| engine.py | b3a455178395e97a |
| fallacy.py | a2bfdc70f83c3bfb |
| interactive_cli.py | e5d7c181e28dba36 |
| nlp_bridge.py | 443dce3c257a550a |
| ontology_data.py | 78235baff792ab69 |
| padartha.py | 7579ebec27e1459b |
| pramana.py | 3ddfca73c7e33be8 |
| preprocess_corpus.py | 722cf719d585c3a9 |
| rag_shabda.py | 4a40437eb96f5b2d |
| rule_miner.py | cf6842acd72c4fb8 |
| syllogism.py | 89e54806bb113d0a |
| tarka_corpus.py | 30000edb92c6cfe0 |
| test_engine.py | 394ef6a1943339de |
| upamana_engine.py | 7edc088ee18bc21f |
| vision_pratyaksha.py | 0708c40d52ec219f |
| vyapti.py | 0cd3c85d769c8f15 |
| data/tarkasangraha_corpus.json | 7f6a11b173a62d6c |

Note: README.md hash was not captured in the pre-import pass (content verified
by full read; hash captured post-import in the migration log). Stale
`__pycache__/` bytecode present in the unpacked dir was excluded from the
baseline (regenerable artifact, not source). The README.md hash above was
captured during the post-import hash-verification pass (all 20 files
byte-identical after migration).

## 4. Test status (pre-import, executed)

Command: `python -m unittest test_engine -v` with cwd =
`/tmp/opencode/ingest/nyaya/nyaya_engine/`, Python 3.14.6.
Result: **31/31 passed (OK)**, in ~0.06 s. Breakdown: Ontology 2, Inference
11 (valid + 9 fallacy branches + forward chaining), NLP 4, Vision 2, RAG 3,
Upamāna 3, Miner 3, Embeddings 2, Corpus grounding 1. No failures, no skips,
no errors. Full per-test listing is preserved in `baseline_test_report.md`.

## 5. Package/module structure

Flat single-package layout, NO packaging metadata (`setup.py`,
`pyproject.toml`, `requirements.txt` all absent), NO `__init__.py` (modules
import each other as top-level siblings, e.g. `from vyapti import
VyaptiDatabase`, `import ontology_data as OD`). This flat, package-less shape
is WHY the baseline must be vendored verbatim into an isolated directory
rather than rewired into a package: adding imports or `__init__.py` files
would modify the artifact under study.

| Module | Lines | Role |
|---|---|---|
| padartha.py | 145 | 7 padārtha classes + `section` refs |
| ontology_data.py | 154 | 9 dravya / 24 guṇa / 5 karman seeds |
| pramana.py | 67 | Pratyaksha / Upamana / Shabda base classes |
| vyapti.py | 81 | Vyapti + VyaptiDatabase |
| syllogism.py | 62 | Svartha + Pañcāvayava generator |
| fallacy.py | 173 | 9-point hetvābhāsa diagnostic |
| embeddings.py | 117 | BoW cosine + optional dense upgrade |
| nlp_bridge.py | 205 | Rule-based NL→(pakṣa,hetu,sādhya) + LLM hook |
| rag_shabda.py | 128 | VectorStore + RAGShabda (threshold 0.22) |
| tarka_corpus.py | 77 | Corpus loader/ingestor/keyword search |
| vision_pratyaksha.py | 111 | VisionBackend + mock + PratyakshaVision |
| upamana_engine.py | 62 | Embedding-similarity Upamana |
| rule_miner.py | 158 | Apriori miner → Vyapti teacher |
| engine.py | 333 | WorldModel + TarkaEngine orchestrator |
| interactive_cli.py | 290 | 14-option REPL |
| demo.py | 301 | Parts A (symbolic) + B (bridges) + C (grounding) |
| test_engine.py | 274 | 31-test unittest suite |
| preprocess_corpus.py | 91 | One-time TXT→JSON chunker |
| data/tarkasangraha_corpus.json | 1,227,793 B | 1,121 prebuilt source-text chunks |
| README.md | 233 | Spec + mapping table + run docs |

## 6. Public APIs (top-level)

- `engine.py`: `WorldModel` (`set_fact/get_fact/has_property/source_of/
  locus_exists/describe_locus`); `TarkaEngine(auto_load_corpus=True,
  corpus_ingest_limit=None)` with `load_corpus/ground_term/keyword_search/
  classify/ontology_summary/declare_locus/perceive/teach_vyapti/
  add_counterexample/infer/infer_from_text/perceive_image/
  ingest_trusted_document/query_shabda/learn_reference_object/
  classify_by_upamana/discover_vyaptis/history/summary`.
- `fallacy.py`: `FallacyReport(name, detail)`; `diagnose(paksha, hetu, sadhya,
  vyapti_db, world)` → `FallacyReport | None`; `PRAMANA_STRENGTH` table.
- `vyapti.py`: `Vyapti(hetu, sadhya, sapaksha, vipaksha, kind="anvaya",
  upadhi)` + `add_counterexample/is_valid`; `VyaptiDatabase(add/get/items/
  all/__len__)`.
- `syllogism.py`: `Syllogism(paksha, hetu, sadhya, sapaksha_example)` +
  `svartha_anumana/parartha_anumana/as_dict`.
- Bridges: `NyayaNLParser(set_llm_backend/clear_llm_backend/parse)`;
  `Embedder(encode/similarity/backend_name)`, `EmbeddingIndex(add/
  most_similar/__len__)`; `RAGShabda(ingest/ingest_bulk/query_and_assert/
  query_passages)`; `TarkaCorpus(load/ingest_into/keyword_search)`;
  `PratyakshaVision(perceive_image)` / `MockVisionBackend(detect)`;
  `UpamanaEngine(learn_reference/classify_by_similarity/
  known_references)`; `VyaptiMiner(mine/teach_engine)` + `apriori/
  generate_rules/make_sample_lookup`.
- Entry points: `python demo.py`, `python interactive_cli.py`,
  `python -m unittest test_engine -v`.

## 7. Production dependencies

ZERO required. Imports across all 18 non-test modules are Python standard
library only (`re`, `math`, `enum`, `collections`, `itertools`, `json`, `os`,
`sys`) plus intra-project sibling imports. ONE optional, guarded dependency:
`sentence-transformers` (`all-MiniLM-L6-v2`) inside `embeddings.py`, wrapped
in `try/except` — verified NOT installed in this environment
(`import sentence_transformers` → `ModuleNotFoundError`), so the engine runs
exclusively on its pure-Python bag-of-words fallback. No network calls, no
API keys, no GPU, no vector DB, no LLM calls (hook only).

## 8. Test dependencies

ZERO beyond the standard library: `test_engine.py` imports `unittest` only
(plus the engine modules under test). `numpy 2.4.4` is present in the
environment but is NOT imported by any engine file.

## 9. Data/corpus dependencies

- `data/tarkasangraha_corpus.json` (1,227,793 bytes): `{"source_name",
  "chunk_count": 1121, "chunks": [...]}` — paragraph-merged chunks of the
  Athalye/Bodas 1930 edition, auto-ingested into the RAG store on every
  `TarkaEngine()` construction (overridable via `auto_load_corpus=False`,
  as the test suite does except for one grounding test with `limit=100`).
- Rebuild path: `preprocess_corpus.py` expects the raw source text at the
  hard-coded default `/mnt/user-data/uploads/
  Tarkasangraha_with_dipika_english.txt` (NOT shipped; rebuild is optional
  and was not run — the checked-in JSON is the dependency).
- No external datasets, no downloads at runtime.

## 10. Files implicated by `research/traceability/conflicts.md`

| Conflict | File(s) | Symbol(s) |
|---|---|---|
| C1 pakṣatā gate missing | engine.py, fallacy.py | `TarkaEngine.infer`, `infer_from_text`, `diagnose` |
| C2 numeric pramāṇa strengths | fallacy.py | `PRAMANA_STRENGTH`, bādhita branch (check 3) |
| C3 satpratipakṣa without balance | fallacy.py | check 5 loop over `vyapti_db.items()` |
| C4 anupasaṃhārin conflated | fallacy.py | check 8 (`sapaksha is None`) |
| C5 upādhi as flag | vyapti.py, fallacy.py | `Vyapti.upadhi`, check 9 |
| C6 counterexample strings | vyapti.py, engine.py | `counterexamples[]`, `is_valid`, `add_counterexample` |
| C7 miner rules as vyāpti | rule_miner.py, engine.py | `teach_engine`, `discover_vyaptis` |
| C8 dead `kind`/`vipakṣa` | vyapti.py, fallacy.py | `Vyapti.kind`, `Vyapti.vipaksha` |
| C9 cosine-as-āpta | rag_shabda.py, tarka_corpus.py, engine.py, preprocess_corpus.py | `RAGShabda.threshold`, `ingest_bulk`, `ground_term`, `build_corpus` |
| C10 linear check order | fallacy.py, engine.py | `diagnose` sequence 1→9, `infer` logging |
| Ontology cell audit (deferred) | ontology_data.py, padartha.py | `GUNA_INFO`, `DRAVYAS`, `section=` kwargs |

None of these files was modified during inspection. Resolutions are
explicitly OUT OF SCOPE for the repository-bootstrap phase; each conflict
becomes one OPEN decision in `research/traceability/OPEN_DECISIONS.md`.
