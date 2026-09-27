# Tarka AI — Software Architecture Audit

Scope: read-only audit of `/tmp/opencode/ingest/tarka_ai.zip` (37.8 KB).
No modification, no merge, no execution beyond static reading (plus a hash-diff
against the Nyāya Engine checkout for §E).

## 0. Identity finding (important)

The "Tarka AI" asset is **not an independent second system**. Its zip contains
a single top-level directory `nyaya_engine/` with **16 `.py` files** that are
line-for-line the earlier revision of the *same* `nyaya_engine` project
delivered as the "Nyāya Engine" asset (which has 20 files). File-by-file MD5
comparison shows every shared file differs only incrementally (docstring
touches, renames, threshold change, added corpus layer); there are **zero**
files unique to "Tarka AI" and **four** files unique to the newer checkout
(`data/tarkasangraha_corpus.json`, `preprocess_corpus.py`, `tarka_corpus.py`,
`test_engine.py`). The label "Tarka AI" therefore denotes the *older snapshot*,
not a complementary codebase. All structural claims below are verified by
reading each file; line counts are from `wc -l`.

## 1. Directory tree

```
nyaya_engine/                  # 16 files, no data/, no tests
├── README.md                  # 174 lines
├── padartha.py                # 133 lines
├── ontology_data.py           # 149 lines
├── pramana.py                 # 68 lines
├── vyapti.py                  # 81 lines
├── syllogism.py               # 61 lines
├── fallacy.py                 # 175 lines
├── embeddings.py              # 119 lines
├── nlp_bridge.py              # 210 lines
├── rag_shabda.py              # 104 lines
├── upamana_engine.py          # 68 lines
├── rule_miner.py              # 161 lines
├── vision_pratyaksha.py       # 114 lines
├── engine.py                  # 294 lines
├── interactive_cli.py         # 279 lines (shebang + sys import)
└── demo.py                    # 278 lines (shebang)
+ __pycache__/                # stale bytecode, ignored
```

No `requirements.txt`, `setup.py`, `pyproject.toml`, config files, or CI.
Pure standard-library Python 3 (imports observed: `re`, `math`, `enum`,
`collections`, `itertools`, `json`/`os`/`sys` in CLI/demo only).

## 2. Entry points

| Entry | File | Behaviour |
|---|---|---|
| Automated demo | `demo.py :: main()` | Parts A (ontology + 1 valid inference + fallacy gauntlet minus vyapti-asiddha) and B (5 ML bridges); ends with session summary + inference log. No Part C (no corpus layer exists here). |
| Interactive REPL | `interactive_cli.py :: main()` | Menu options [1]–[11],[13],[14]: teach vyapti, state fact, infer, NLP infer, vision, RAG ingest/query, upamana learn/classify, vyapti-miner, ontology lookup, summary/log, exit. **No option [12]** (ground-term-in-source-text) — that menu item only exists in the newer checkout. EOF-safe `ask()` variant without the later `try/except EOFError` hardening. |
| Library API | `engine.py :: TarkaEngine` | `TarkaEngine()` takes **no arguments** (no `auto_load_corpus`); all orchestration methods described in §5. |

## 3. Modules, classes, APIs

### 3.1 Ontology — `padartha.py`, `ontology_data.py`
- `Category` enum (7 padārthas), `Padartha(name, category, description)` —
  **no `section` field** (the newer checkout adds `section` everywhere).
  Subclasses `Dravya(eternal, qualities)`, `Guna(resides_in)`,
  `Karma(resides_in)`, `Samanya(extent)`, `Vishesha`, `Samavaya`,
  `Abhava(pratiyogi, anuyogi, abhava_type)` with `AbhavaType` 4-way enum.
- `ontology_data.py`: 9 `DRAVYAS` (no per-entry `section=` kwargs; header
  comment says only "Section 3 / Section 4 / Section 5" coarsely), 24-entry
  `GUNA_INFO` → `GUNAS`, 5-entry `KARMA_INFO` → `KARMAS`; `describe()`
  (case-insensitive), `list_all()`, `all_terms()`.

### 3.2 Epistemology — `pramana.py`
- `Pratyaksha.perceive(world, locus, prop, value)` (static; source tag
  `"pratyaksha"`).
- `Upamana(ref_obj, target_obj, shared_props)` — note parameter name
  `target_obj` (renamed to `target_object` in newer checkout);
  `analogize(world, resulting_name)`.
- `Shabda(speaker, is_trustworthy)` with `assert_fact(world, …)` — note method
  name `assert_fact` (renamed to `testify` in newer checkout) and slightly
  different message strings.

### 3.3 Inference core — `vyapti.py`, `syllogism.py`, `fallacy.py`, `engine.py`
- `Vyapti(hetu, sadhya, sapaksha, vipaksha, kind="anvaya", upadhi)` +
  `counterexamples[]`, `add_counterexample()`, `is_valid()`
  (broken iff counterexamples non-empty); `VyaptiDatabase.add/get/items/all/
  __len__`. Docstring cites TS §44 smoke/fire formula. **Identical logic** to
  newer checkout (only the underline style differs).
- `Syllogism(paksha, hetu, sadhya, sapaksha_example)` with
  `svartha_anumana()` (3-step: vyāpti-smaraṇa / parāmarśa / anumiti) and
  `parartha_anumana()` (5 members). `__repr__` here is
  `"Syllogism({paksha} / {hetu} -> {sadhya})"` (newer: "… has … because …").
- `fallacy.py :: diagnose(paksha, hetu, sadhya, vyapti_db, world)` — the same
  **9-point gauntlet** (āśrayasiddha → svarūpasiddha → bādhita → viruddha →
  satpratipakṣa → vyapti-asiddha → sadhāraṇa → asādhāraṇa → vyāpyatvasiddha),
  same `PRAMANA_STRENGTH` table (pratyakṣa 4 > śabda 3 > upamāna 2 > anumāna 1
  > assumed 0), same `FallacyReport(name, detail)`. Only cosmetic diffs
  (one emphasis markup, one dropped end-comment).
- `engine.py :: WorldModel` (`facts[locus][prop] = (value, source)`,
  `set_fact/get_fact/has_property/source_of/locus_exists/describe_locus`) and
  `:: TarkaEngine` with `declare_locus/perceive/teach_vyapti/
  add_counterexample/infer/infer_from_text/perceive_image/
  ingest_trusted_document/query_shabda/learn_reference_object/
  classify_by_upamana/discover_vyaptis/history/summary`. **Missing vs. newer:**
  no `tarka_corpus` import, no `corpus` attribute, no `load_corpus/
  ground_term/keyword_search`, constructor takes no args.

### 3.4 Neuro-symbolic bridges
| Bridge | File | Mechanism in this snapshot |
|---|---|---|
| NL → anumāna | `nlp_bridge.py` (210 ln) | `RuleBasedParser` (because/since splitter, synonym table, article-strip, subject-noun heuristic) + `NyayaNLParser` facade with pluggable `llm_backend`. Result dicts here **lack** the `"backend": "rule-based"` tag the newer version adds; regexes use escaped `\-` inside classes; claim-clause noun strip covers only that/this (newer adds the/a/an). Logic otherwise identical. |
| Embeddings | `embeddings.py` (119 ln) | Bag-of-words `tokenize/vectorize/cosine_similarity` + guarded `sentence-transformers` upgrade + `Embedder` + `EmbeddingIndex(name→(desc,vec))`. Stopwords lack for/by/at (added later); `__len__` defined at class end rather than after `add`. |
| RAG → śabda | `rag_shabda.py` (104 ln) | `Document(text, source)` — **no `section`, no `excerpt()`**; doc IDs `doc_<n>` (newer: `doc<n>`); `VectorStore` without `sources()`; `RAGShabda(threshold=0.15)` — newer raises to **0.22**; `ingest(text, source_name)` without section; **no `ingest_bulk`, no `query_passages`**. |
| Upamāna | `upamana_engine.py` (68 ln) | Imports `Upamana` from `pramana` and **delegates assertion through `Upamana(...).analogize()`** (newer writes the two `world.set_fact` calls directly and returns `resulting_name`). Threshold default 0.25 both versions. Return keys differ (`matched_reference`/`similarity` here). |
| Vision → pratyakṣa | `vision_pratyaksha.py` (114 ln) | Imports `Pratyaksha` from `pramana` (import dropped later as unused at module level); `MockVisionBackend` with same KEYWORD_MAP; `perceive_image` low-confidence branch prints "Ignored low-confidence…" and keeps looping (newer early-returns on empty + "Skipping …" wording). `VisionBackend` interface identical. |
| Miner → vyāpti | `rule_miner.py` (161 ln) | From-scratch Apriori (`apriori`, `generate_rules` with support/confidence), `make_sample_lookup`, `VyaptiMiner(min_support, min_confidence)` with `mine()` + `teach_engine(engine, rules, only_single_term=True, …)` — the flag and joined `"+".join(...)` multi-term teaching path were **removed** in the newer version (single-term-only, always). |

## 4. Data models

- WorldModel facts: `{locus: {prop: (bool|None, source_str)}}`; tristate hetu
  presence (`True/False/None`) drives the two svarūpasiddha sub-branches.
- Vyāpti records: `(hetu, sadhya) → {sapaksha, vipaksha, kind, upadhi,
  counterexamples[]}`; `kind` is stored but **never read** by `diagnose`
  (dead field in both snapshots).
- RAG store: `{doc_id: Document}` + embedding index keyed by doc_id over raw
  passage text; retrieval = top-k cosine, threshold-gated assert.
- Upamāna index: `{name: (description, vector)}`; classification writes
  `resembles:<ref>` + `named:<label>` facts (via `Upamana.analogize` here).
- No persistence, no schema files, no migrations.

## 5. Reasoning pipeline (`TarkaEngine.infer`)

Identical 9-step gauntlet + syllogism generation + forward-chaining assert
(`world.set_fact(paksha, sadhya, True, source="anumana")`) + `_log` of
`("VALID"/"REJECTED", paksha, hetu, sadhya, tag)` as in the newer checkout,
minus corpus grounding. `infer_from_text` auto-declares unknown pakṣa and
assumes hetu-present (`source="assumed"`) before calling `infer` — same
"parser proposes, gauntlet disposes" firewall.

## 6. LLM integration

No real LLM calls, keys, or network code. `NyayaNLParser.set_llm_backend(fn)`
/ `clear_llm_backend()` hook only; default path is the deterministic
rule-based parser. Same in both snapshots.

## 7. Retrieval / knowledge representation

Ontology (padārtha objects) + WorldModel (locus facts) + VyaptiDatabase
(rules) + VectorStore (trusted docs, manually ingested only — **no bundled
corpus**, no `tarka_corpus.py`, no `preprocess_corpus.py`).

## 8. Tests / configuration / dependencies / documentation

- Tests: **none** in this snapshot (`test_engine.py` does not exist).
- Configuration: none (thresholds hard-coded: RAG 0.15, upamāna 0.25,
  miner defaults 0.3/0.85).
- Dependencies: **zero required** (stdlib only; `sentence-transformers` used
  only if already installed).
- Documentation: `README.md` (174 lines) — same project story (symbolic core
  + 5 bridges + firewall) but **without** the "What's new" corpus section,
  without the `tarka_corpus/preprocess/test_engine/data` rows in the tree,
  and with the older numbered-section layout ("## 1. …", "## 2. …").

## 9. Existing Nyāya-related functionality (summary)

Full anumāna pipeline (vyāpti DB → parāmarśa-equivalent hetu+rule check →
pañcāvayava generator with svartha trace), 9-point hetvābhāsa diagnostic with
classical stock examples in message strings, 7-padārtha ontology (9 dravya /
24 guṇa / 5 karman seeds), 4-pramāṇa scaffolding with 5 ML bridges mapped
onto pramāṇas/vyāpti-discovery, forward chaining, session log/summary.
Not present: corpus grounding/citation, per-term section refs, bulk ingest,
similarity-threshold 0.22 tuning, automated tests.
