# Nyāya Engine — Software Architecture Audit

Scope: read-only audit of `/tmp/opencode/ingest/nyaya_engine.zip` (407 KB,
unpacked to `/tmp/opencode/ingest/nyaya/nyaya_engine/`). No modification.
All 20 files read in full; behaviour claims below are additionally verified by
running the bundled suite (`python -m unittest test_engine -v`: **31 tests,
OK**) and by inspecting `demo.py`'s asserted flows.

## 1. Directory tree (20 files; sizes via `wc -l`)

```
nyaya_engine/
├── README.md               # 233 lines — full spec + "What's new" + grounding docs
├── padartha.py             # 145 lines — 7 padārtha classes + section refs
├── ontology_data.py        # 154 lines — 9 dravya / 24 guṇa / 5 karman seeds + section refs
├── pramana.py              # 67 lines  — Pratyaksha / Upamana / Shabda base classes
├── vyapti.py               # 81 lines  — Vyapti + VyaptiDatabase
├── syllogism.py            # 62 lines  — Svartha + Pañcāvayava generator
├── fallacy.py              # 173 lines — 9-point hetvābhāsa diagnostic
├── embeddings.py           # 117 lines — BoW cosine + optional sentence-transformers
├── nlp_bridge.py           # 205 lines — rule-based NL→(pakṣa,hetu,sādhya) + LLM hook
├── rag_shabda.py           # 128 lines — VectorStore + RAGShabda (threshold 0.22)
├── tarka_corpus.py         # 77 lines  — corpus loader/ingestor/keyword search
├── vision_pratyaksha.py    # 111 lines — VisionBackend + MockVisionBackend + PratyakshaVision
├── upamana_engine.py       # 62 lines  — embedding-similarity Upamana
├── rule_miner.py           # 158 lines — from-scratch Apriori miner → Vyapti teacher
├── engine.py               # 333 lines — WorldModel + TarkaEngine orchestrator
├── interactive_cli.py      # 290 lines — 14-option REPL (incl. corpus grounding [12])
├── demo.py                 # 301 lines — Parts A (symbolic) + B (bridges) + C (grounding)
├── test_engine.py          # 274 lines — 31-test stdlib unittest suite
├── preprocess_corpus.py    # 91 lines  — one-time TXT→JSON chunker
└── data/
    └── tarkasangraha_corpus.json  # 1,227,793 bytes; {"source_name","chunk_count":1121,"chunks":[…]}
```

No packaging metadata, no dependency manifest, no config files; stdlib-only
imports plus one guarded optional import (`sentence_transformers`).

## 2. Entry points

| Entry | Command | Coverage |
|---|---|---|
| `demo.py` | `python demo.py` | A.1 ontology lookup; A.2 valid mountain/smoke/fire; A.3–A.11 all nine diagnostics + vyapti-asiddha; A.12 forward chaining; B.1 NLP (valid + must-reject); B.2 vision; B.3 RAG (accept + reject); B.4 upamāna (classify + refuse); B.5 mining; C grounding of pratyakṣa/anumāna/dravya terms. Every symbolic branch ends in `assert`. |
| `interactive_cli.py` | `python interactive_cli.py` | 14 menu items [1]–[14]; [12] = "Ground a term in the real Tarkasamgraha source text" (`engine.ground_term`, top-3, 300-char excerpts); [13] summary+log; [14] exit. EOF-safe. |
| `test_engine.py` | `python -m unittest test_engine -v` | 31 tests: Ontology (2), Inference incl. all 9 fallacy branches + forward chaining (11), NLP (4), Vision (2), RAG (3), Upamāna (3), Miner (3), Embeddings (2), Corpus grounding (1). All pass offline. |
| Library | `from engine import TarkaEngine` | `TarkaEngine(auto_load_corpus=True, corpus_ingest_limit=None)` auto-ingests the 1,121-chunk corpus into the RAG store at construction (see §7). |

## 3. Modules, classes, APIs (per-file)

### 3.1 `padartha.py` — ontology classes
`Category` (7 enum values); `Padartha(name, category, description, section)` with
`info()` rendering `"name :: category [Sec. N]"`; `Dravya(eternal, qualities,
section=3)`, `Guna(resides_in, section=4)`, `Karma(resides_in, section=5)`,
`Samanya(extent, section=6)`, `Vishesha(section=7)`, `Samavaya(section=8)`,
`Abhava(pratiyogi, anuyogi, abhava_type, section=9)` + `AbhavaType` (4 negations).
Module docstring cites TS §2 and advertises `ground_term()` cross-referencing.

### 3.2 `ontology_data.py` — seed knowledge base
`DRAVYAS` (9, each with `section=` 10–18: Pṛthvī 10, Ap 11, Tejas 12, Vāyu 13 —
noted "known only by inference (anumana)", Ākāśa 14, Kāla 15, Dik 16,
Ātman 17, Manas 18); `GUNA_INFO` (24 named qualities with residence lists and
detail sections 19–33, 34, 66, 73, 75) → `GUNAS`; `KARMA_INFO`/`KARMAS` (5,
section 5). API: `describe(name)` (case-insensitive; dravya-capitalized,
guṇa/karman-lowercase lookup), `list_all()`, `all_terms()`.
Verified: `len(DRAVYAS)==9`, `len(GUNAS)==24` (note: the 24 names skip several
classical guṇas — buddhi through saṃskāra are present but e.g. *saṃyoga* etc.
use residence `None`→all-dravyas fallback), `len(KARMAS)==5` (test asserts).

### 3.3 `pramana.py` — base pramāṇas
`Pratyaksha.perceive(world, locus, prop, value)` (tags `"pratyaksha"`, called
"strongest" in docstring); `Upamana(ref_obj, target_object, shared_props).
analogize(world, resulting_name)` (writes `named:<label>` fact, source
`"upamana"`); `Shabda(speaker, is_trustworthy).testify(world, …)` (refuses
non-apta, else tags `"shabda"`; docstring: apta = *yathārthavaktā*).
These are the *manual* layer; the ML-augmented versions live in
`vision_pratyaksha.py` / `upamana_engine.py` / `rag_shabda.py` and call into
`WorldModel` directly rather than through these classes (upamana/vision no
longer import them — only conceptual layering remains).

### 3.4 `vyapti.py` — rule representation
`Vyapti(hetu, sadhya, sapaksha=None, vipaksha=None, kind="anvaya",
upadhi=None)` + `counterexamples[]`; `is_valid()` ⇔ no counterexamples;
`__repr__` shows valid/BROKEN. `VyaptiDatabase` keyed by `(hetu, sadhya)` with
`add/get/items/all/__len__`; `get(hetu)` without sādhya returns all rules
sharing the hetu (used by the viruddha/satpratipakṣa scans). Docstring cites
TS §44 `"yatra yatra dhūmaḥ tatra tatra vahniḥ"`. `kind` stored but never
branched on; `vipaksha` stored but never read by `diagnose`.

### 3.5 `syllogism.py` — inference representation
`Syllogism(paksha, hetu, sadhya, sapaksha_example)`; `svartha_anumana()` =
3 lines (vyāpti-smaraṇa with sapakṣa citation / parāmarśa / anumiti);
`parartha_anumana()` = 5 labelled members (pratijñā / hetu / udāharaṇa with
"Whatever has hetu has sādhya, as in sapakṣa" / upanaya with "pervaded by" /
nigamana "Therefore…"); `as_dict()`, `__repr__`. Docstring cites §§45–46.

### 3.6 `fallacy.py` — validation (the symbolic firewall)
`PRAMANA_STRENGTH = {pratyaksha:4, shabda:3, upamana:2, anumana:1, assumed:0}`;
`FallacyReport(name, detail)` (truthy, `__repr__`/`__str__` prefixed
`[HETVABHASA: …]`); `diagnose(paksha, hetu, sadhya, vyapti_db, world)` in
fixed order:
1. āśrayasiddha (pakṣa unknown — gagana-aravinda message);
2. svarūpasiddha-absent (`False`) / -unverified (`None`) — tristate logic;
3. bādhita (`not-<sadhya>` recorded `True` with source strength ≥ anumāna;
   message cites fire-cold vs. tactile heat);
4. viruddha (valid `vyapti(hetu → not-sadhya)` on record; kṛtakatva message);
5. satpratipakṣa (any *other* valid `vyapti(h2 → not-sadhya)` with h2 present
   on pakṣa; śrāvaṇatva/kāryatva message);
6. vyapti-asiddha (no `(hetu,sadhya)` entry — the anti-hallucination refusal);
7. savyabhicāra-sādhāraṇa (`not vyapti.is_valid()` — prameyatva/lake message);
8. savyabhicāra-asādhāraṇa (`sapaksha is None` — śabdatva message);
9. vyāpyatvasiddha (`vyapti.upadhi` truthy — vahni→dhūma/ārdrendhana message).
`None` ⇔ sad-hetu. Docstring maps each to TS §§52–57.

### 3.7 `engine.py` — orchestrator + knowledge graph
`WorldModel.facts = {locus: {prop: (value, source)}}` with the six accessors;
`TarkaEngine` owns `vyapti_db, world, nlp, vision, rag, upamana, miner,
corpus, corpus_loaded_chunks, _log`. Knowledge entry: `declare_locus(locus,
source="assumed", **props)`, `perceive` (pratyakṣa), `teach_vyapti`,
`add_counterexample` (raises if no vyāpti yet). Reasoning: `infer` (diagnose
→ reject-log+print or syllogism + forward-chain assert with source
`"anumana"` + log). Bridges: `infer_from_text` (parse → ensure pakṣa exists →
assume hetu if unknown → `infer`); `perceive_image`; `ingest_trusted_document`
/ `query_shabda`; `learn_reference_object` / `classify_by_upamana`;
`discover_vyaptis` (mine → optionally auto-teach). Grounding: `load_corpus`,
`ground_term` (read-only top-k, threshold 0.0), `keyword_search`.
Introspection: `history()`, `summary()` (loci/vyāptis/attempts/docs/
references/backend/corpus counts).

### 3.8 `embeddings.py` — retrieval substrate
`tokenize` (lowercase `[a-zA-Z']+`, stopword strip incl. for/by/at, len>1),
`vectorize` (Counter dict), `cosine_similarity` (sparse, zero-safe);
`Embedder(prefer_dense)` auto-uses `sentence-transformers/all-MiniLM-L6-v2`
iff importable (`backend_name()` reports which); `EmbeddingIndex` with
`add/most_similar(top_k)/__len__`. Tests pin identical-text≈1.0 and
disjoint-text=0.0.

### 3.9 `nlp_bridge.py` — NL parser
`SYNONYMS` (smoke/fire/wetness/rain/clouds/poison/death/heat/cold clusters),
filler/aux/article/demonstrative/connective regexes; `normalize_term`
(exact → substring → last-word fallback); `_find_subject_noun`
(article/demonstrative headword else first word); `RuleBasedParser.parse`
(never raises; requires because/since; handles leading-"Since …, …";
returns `{success, paksha(Capitalized), hetu, sadhya, raw_text,
backend:"rule-based"}` or `{success:False, reason[, partial]}`);
`NyayaNLParser` facade (`set_llm_backend/clear_llm_backend/parse` — LLM tried
first, fallback always). Tests: hill/smoke parses→valid; pond/poison
parses but is rejected (no rule); "" and connective-less inputs fail cleanly.

### 3.10 `rag_shabda.py` — trusted-document śabda
`Document(text, source, section)` with `doc<n>` IDs and `excerpt(160)`;
`VectorStore` (index keyed by doc_id; `add_document/retrieve(top_k)/__len__/
sources()`); `RAGShabda(threshold=0.22)` with `ingest`, `ingest_bulk`
((text[,section]) chunks), `query_and_assert` (empty-store reject; sub-
threshold reject "Not from an Apta"; else assert with source `"shabda"` and
return `{accepted, score, doc, message}`), `query_passages` (non-asserting
read path used by `ground_term`). README documents the 0.15→0.22 retune for
the 1,121-passage corpus.

### 3.11 `tarka_corpus.py` + `preprocess_corpus.py` + `data/`
`TarkaCorpus(path=…/data/tarkasangraha_corpus.json)` with `load()` (reads
`{source_name, chunk_count, chunks}`), `ingest_into(rag, limit)` (bulk ingest
under the corpus's bibliographic `source_name` =
"Tarkasamgraha with the author's own Dipika and Govardhana's Nyaya-Bodhini
(ed. Athalye, trans. Bodas, Bombay Sanskrit Series No. LV, 1930)"),
`keyword_search`. `preprocess_corpus.py :: build_corpus(src, out, source_name,
target_chunk_len=900)` (paragraph-merge → 900-char chunks → sentence-split
oversize → `is_useful` filter ≥40 chars & >50% letters → JSON). The checked-in
JSON holds **1,121 chunks**; test ingests 100 and asserts non-crash grounding.

### 3.12 `vision_pratyaksha.py` — perception bridge
`VisionBackend.detect` interface; `MockVisionBackend` (dict passthrough with
confidence, or keyword-scan of description strings via KEYWORD_MAP:
mountain/hill→loci; smoke/fire/flame/cloud/rain/jar/pot/kitchen→attributes;
else UnknownObject or `[]`); `PratyakshaVision(backend=Mock)`.
`perceive_image(world, image_input, confidence_threshold=0.5)` writes
pratyakṣa facts per accepted detection. Tests: smoke-scene detection; 0.1-
confidence ghost skipped at threshold 0.5.

### 3.13 `upamana_engine.py` — comparison bridge
`UpamanaEngine(threshold=0.25)`; `learn_reference(name, description)`;
`classify_by_similarity(world, target_name, description, resulting_name,
threshold)` (no-references refuse; sub-threshold refuse with candidates;
else assert `resembles:<best>` + `named:<label>` as `"upamana"`). Docstring
cites TS §58 gavaya/cow example; demo/tests use Cow→Gavaya (success) and
Spacecraft@0.6 (refusal).

### 3.14 `rule_miner.py` — vyāpti discovery
`_support`, `apriori(transactions, min_support, max_itemset_size=3)`,
`generate_rules(frequent, transactions, min_confidence)` (antecedent→
consequent with support/confidence, sorted 脳confidence then support),
`make_sample_lookup` (first-transaction label for sapakṣa),
`VyaptiMiner(min_support=0.3, min_confidence=0.85)` with `mine()` and
`teach_engine(engine, rules, sample_id_lookup, verbose)` (teaches only
1→1 rules as binary vyāptis; reports multi-term skips). README maps this to
*bhūyodarśana*. Tests cover apriori support, rule confidence, and an
end-to-end weather-transaction discovery that grows `vyapti_db`.

### 3.15 `demo.py`, `interactive_cli.py`, `README.md`
As in §2; README additionally specifies the neuro-symbolic mapping table
(NLP→anumāna input, embeddings→upamāna, RAG→śabda, CV→pratyakṣa,
Apriori→vyāpti discovery), the firewall principle, swap-in points for real
LLM/CV/embeddings/vector-DB, and the philosophical note (pramāṇas need
scrutiny; anumāna + fallacy gauntlet as protector).

## 4. Configuration / dependencies / documentation

- Configuration: constructor args (`auto_load_corpus`, `corpus_ingest_limit`),
  per-call thresholds (`confidence_threshold`, RAG `threshold`,
  upamāna `threshold`, miner `min_support/min_confidence`); defaults
  0.5 / 0.22 / 0.25 / 0.3+0.85. No config files.
- Dependencies: zero required; optional `sentence-transformers` auto-upgrade;
  documented swap points for real LLM (callable), CV (`VisionBackend`
  subclass), vector DB (same `add_document/retrieve` interface), cleaner
  corpus (re-run preprocessor).
- Documentation: README (233 lines) is accurate to the code as audited
  (file tree, workflow steps 1–9, API example all match).

## 5. Nyāya-related functionality present (checklist against the brief)

Ontology ✓ (7 padārthas, 9/24/5 seeds, §-refs); pramāṇa representation ✓
(4 base classes + 3 augmented bridges + miner-as-vyāptigraha); anumāna ✓
(parāmarśa-equivalent check + svartha trace + pañcāvayava generator);
hetu/sādhya/pakṣa ✓ (WorldModel loci + vyāpti endpoints + tristate hetu);
vyāpti ✓ (DB with sapakṣa/vipakṣa/kind/upādhi/counterexamples);
hetvābhāsa ✓ (9-point diagnostic with stock examples); pañcāvayava ✓
(5 labelled members + per-member prayojana-adjacent strings);
rule representation ✓ (binary hetu→sādhya + kind/upādhi metadata);
inference representation ✓ (`Syllogism` + forward-chained facts);
knowledge graph ✓ (WorldModel + VyaptiDatabase + VectorStore + EmbeddingIndex);
symbolic reasoning ✓ (diagnose→generate→assert→chain); validation ✓
(gauntlet + 31 tests); tests ✓ (all pass offline).
