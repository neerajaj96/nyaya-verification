# Navya-Nyaya Neuro-Symbolic Reasoning Engine

Based on Annambhatta's *Tarkasamgraha* & *Dipika* — with the full
English *Tarkasamgraha-with-Dipika* source text (Athalye/Bodas edition,
Bombay Sanskrit Series No. LV, 1930) integrated as the engine's live
Shabda ("verbal testimony") knowledge corpus.

## Project Overview

This project is a computational formalization of ancient Indian
epistemology and logic. It translates the deterministic, rule-based
reasoning of the Nyaya-Vaisheshika school into a modern Symbolic AI
(Expert System) core, and then extends it into a Hybrid Neuro-Symbolic
AI by mapping specific Machine-Learning techniques onto the four
classical Pramanas (Means of Knowledge).

The symbolic core never hallucinates: every accepted conclusion is
backed by an explicit, inspectable five-membered syllogism, and every
proposed fact or rule — whether typed by a human, produced by an ML
component, or retrieved from the ingested source text — is passed
through the Hetvabhasa (fallacy) gauntlet before it can be used.

**Zero cost, zero required dependencies.** Every module has a
100%-dependency-free, deterministic default implementation (pure
Python 3 standard library). `embeddings.py` will *automatically*
upgrade to `sentence-transformers` dense embeddings if that package
happens to already be installed — but it is never required, and
nothing in this repo needs a paid API key, GPU, or network call.

## Theoretical Framework

**Ontology (The 7 Padarthas).** The universe of discourse is strictly
categorized: Dravya (Substance), Guna (Quality), Karma (Action),
Samanya (Generality), Vishesha (Particularity), Samavaya (Inherence),
Abhava (Negation).

**Epistemology (The 4 Pramanas).** Knowledge must be grounded in valid
proofs: Pratyaksha (Perception), Anumana (Inference), Upamana
(Comparison), Shabda (Verbal Testimony).

**Logic (Pancavayava & Hetvabhasa).** Inference requires a
five-membered syllogism (Pratijna, Hetu, Udaharana, Upanaya,
Nigamana). Any flaw is caught by checking for the five Hetvabhasas
(and their sub-varieties), run as a 9-point diagnostic:

1. Ashrayasiddha (unreal locus)
2. Svarupasiddha (hetu absent/unverified in the paksha)
3. Badhita (negation of sadhya already proven more strongly)
4. Viruddha (hetu proves the opposite of sadhya)
5. Satpratipaksha (an equally strong opposing hetu exists)
6. Vyapti-asiddha (no rule on record at all)
7. Savyabhichara–Sadharana (over-wide reason, broken by a counterexample)
8. Savyabhichara–Asadharana (over-narrow reason, no supporting instance)
9. Vyapyatvasiddha (concomitance depends on a hidden condition/upadhi)

## Neuro-Symbolic Extension

| # | ML Technique | Classical Pramana | Module |
|---|---|---|---|
| 1 | Rule-based NLP parser (pluggable real-LLM hook) | Anumana (input formatting) | `nlp_bridge.py` |
| 2 | Vector embeddings + cosine similarity | Upamana (comparison) | `embeddings.py`, `upamana_engine.py` |
| 3 | Retrieval-Augmented Generation over an in-memory vector store | Shabda (verbal testimony) | `rag_shabda.py`, `tarka_corpus.py` |
| 4 | Pluggable Computer-Vision backend (mock by default) | Pratyaksha (perception) | `vision_pratyaksha.py` |
| 5 | Apriori association-rule mining | Vyapti discovery (bhuyodarshana) | `rule_miner.py` |

**Design principle — the "neuro-symbolic firewall":** every one of the
five bridges above only ever *proposes* candidate facts, rules, or
parsed terms. None of them can directly assert a conclusion. Every
proposal must still pass through `fallacy.py`'s 9-point diagnostic
before the engine will accept it. This is exactly how the system
prevents ML hallucination — or a misleading retrieved passage — from
becoming "sound" logic.

## What's new in this upgrade

* **Full-text grounding (`tarka_corpus.py`).** The entire uploaded
  English Tarkasamgraha-with-Dipika text is pre-processed
  (`preprocess_corpus.py`) into ~1,100 cleaned passages
  (`data/tarkasangraha_corpus.json`) and auto-ingested into the
  RAG/Shabda trusted-document store on every `TarkaEngine()` startup.
  Any ontology term or free-text question can now be grounded against
  the *real* source text via `engine.ground_term(...)`, with a
  similarity score and an excerpt for every hit — not a paraphrase
  from the model's memory.
* **Section-referenced ontology.** `padartha.py` / `ontology_data.py`
  now carry a `section` number on every seeded Dravya/Guna/Karma,
  matching the Tarkasamgraha's own section numbering (e.g. Prithvi =
  Sec. 10, Pratyaksha = Sec. 42).
* **Corrected, fully working code.** All 14 modules were rewritten
  from scratch to be syntactically valid, internally consistent
  Python 3 (the previous draft had multiple broken constructors and
  missing methods) and are covered by an automated test suite.
* **31-test, zero-dependency `unittest` suite** (`test_engine.py`)
  covering the ontology, all 9 fallacy diagnostics, all 5 ML bridges,
  and the corpus-grounding layer.
* **Tuned RAG threshold.** With ~1,100 real passages now in the
  trusted-document store, the Shabda acceptance threshold was raised
  (0.15 → 0.22) to keep the "reject if not backed by an Apta source"
  guarantee robust against a larger, denser corpus.
* **CLI option 12**: "Ground a term in the real Tarkasamgraha source
  text" — ask any question and see the actual passages the engine
  found, with similarity scores.

## System Architecture & Directory Structure

```
nyaya_engine/
├── padartha.py             # OO base classes for the 7 categories
├── ontology_data.py         # Seeds: 9 substances, 24 qualities, 5 actions
├── pramana.py                # Base proofs: Pratyaksha, Upamana, Shabda
├── vyapti.py                  # Invariable-concomitance rule database
├── syllogism.py                # Svartha- and Parartha-Anumana generator
├── fallacy.py                   # The 9-point Hetvabhasa diagnostic
│
├── embeddings.py                 # Vector embeddings (pure-python + optional ST)
├── nlp_bridge.py                  # NL -> (paksha, hetu, sadhya) parser
├── rag_shabda.py                   # RAG-backed trusted-document Shabda
├── tarka_corpus.py                  # Loads & ingests the real source text
├── vision_pratyaksha.py              # CV backend -> Pratyaksha facts
├── upamana_engine.py                  # Embedding-similarity Upamana
├── rule_miner.py                       # Apriori Vyapti discovery
│
├── engine.py                            # TarkaEngine: master orchestrator
├── interactive_cli.py                    # REPL exposing every feature
├── demo.py                                # Automated end-to-end demo
├── test_engine.py                          # 31-test unittest suite
├── preprocess_corpus.py                     # One-time corpus builder
├── data/tarkasangraha_corpus.json            # Pre-built source-text corpus
└── README.md
```

## Execution Workflow

When an inference is requested (e.g. "Does the mountain have fire
because of smoke?"):

1. **Locus Verification** — does "Mountain" exist in the WorldModel? (else → Ashrayasiddha)
2. **Hetu Verification** — does "smoke" actually hold on the mountain? (else → Svarupasiddha)
3. **Badhita check** — is not-fire already perceptually proven?
4. **Viruddha check** — does smoke actually entail not-fire?
5. **Satpratipaksha check** — is there an equally strong opposing hetu?
6. **Rule Retrieval** — look up the Vyapti linking smoke to fire (else → Vyapti-asiddha)
7. **Sadharana / Asadharana checks** — is the concomitance broken by a counterexample, or unsupported by any positive example at all?
8. **Vyapyatvasiddha check** — does the rule depend on a hidden condition (upadhi)?
9. **Syllogism Generation** — if every check passes, return a `Syllogism` object containing the generated Pratijna, Hetu, Udaharana, Upanaya and Nigamana (plus the private Svartha-Anumana trace).

Each of the five ML bridges simply produces inputs to steps 1–2 (a
candidate locus/fact) or step 6 (a candidate rule, or a cited passage
for Shabda) — the gauntlet above still runs in full every time.

## How to Run

Requires only the Python 3 standard library — zero installation needed.

```bash
# Automated demonstration of every symbolic + neuro-symbolic feature:
python demo.py

# Full test suite:
python -m unittest test_engine -v

# Interactive REPL:
python interactive_cli.py
```

### Quick API example

```python
from engine import TarkaEngine
engine = TarkaEngine()   # auto-ingests ~1,100 passages of the real source text

# --- symbolic core ---
engine.declare_locus("Kitchen", smoke=True, fire=True)
engine.declare_locus("Mountain", smoke=True)
engine.teach_vyapti(hetu="smoke", sadhya="fire", sapaksha="a kitchen")
engine.infer(paksha="Mountain", hetu="smoke", sadhya="fire")

# --- neuro-symbolic bridges ---
engine.infer_from_text("That hill must be burning because it's billowing smoke!")
engine.perceive_image("a mountain with thick smoke rising from its peak")
engine.ingest_trusted_document("Water boils at 100C.", source_name="Textbook")
engine.query_shabda("Water", "boils_at_100C", "does water boil at 100C?")
engine.learn_reference_object("Cow", "bovine, four legs, horns, milk")
engine.classify_by_upamana("Gavaya", "wild ox resembling cattle")
engine.discover_vyaptis([{"heavy_clouds", "rain"}] * 5, min_support=0.2)

# --- textual grounding, new in this upgrade ---
for doc, score in engine.ground_term("what is pratyaksha perception"):
    print(score, doc.excerpt())
```

## Extending With Real ML Models

Every bridge is a thin, swappable interface:

* **Real LLM:** `engine.nlp.set_llm_backend(your_llm_call_fn)` where
  `your_llm_call_fn(text) -> {"success": True, "paksha":..., "hetu":..., "sadhya":...}`.
* **Real Computer Vision:** subclass `VisionBackend` in
  `vision_pratyaksha.py`, implement `.detect(image)`, and pass an
  instance to `PratyakshaVision(backend=your_backend)`.
* **Real dense embeddings:** `pip install sentence-transformers` —
  `embeddings.py` will detect and use it automatically, upgrading
  Upamana and RAG-Shabda (including the Tarkasamgraha corpus search)
  without any code changes.
* **Real vector DB (RAG):** swap `VectorStore` in `rag_shabda.py` for
  a ChromaDB/FAISS-backed implementation with the same
  `add_document` / `retrieve` interface.
* **Richer corpus segmentation:** `preprocess_corpus.py` currently
  chunks the source text by paragraph/sentence boundaries (OCR text
  has no reliable machine-parseable section markers). If you have a
  cleaner or re-OCR'd edition, re-run it to rebuild
  `data/tarkasangraha_corpus.json` with true per-Section chunks.

## License & Source-Text Note

All code in this repository is provided for the user's own,
zero-cost, local use. The ingested Tarkasamgraha-with-Dipika text is
the user's own uploaded document (the 1930 Athalye/Bodas edition);
it is stored locally in `data/tarkasangraha_corpus.json` for use as
this engine's own Shabda knowledge base and is not redistributed by
this project.

## Philosophical Note

This engine intentionally keeps the ML layer subordinate to the
symbolic layer, mirroring the Nyaya epistemological stance that a
pramana is only valid knowledge if it survives scrutiny (here,
`fallacy.py`'s Hetvabhasa gauntlet) — sensation, comparison, and
testimony are all real sources of knowledge, but none of them are
self-certifying. The classical Naiyayika would recognize this
architecture immediately: perception, comparison, and word are all
useful pramanas, but reasoning (anumana) — and, in the end,
common-sense scrutiny — is what protects the system from error.
