"""
engine.py
---------
Navya-Nyaya Neuro-Symbolic Reasoning Engine
Based on Annambhatta's Tarkasamgraha & Dipika

TarkaEngine: the top-level orchestrator combining
    * the ontology of the seven categories       (padartha.py, ontology_data.py)
    * a WorldModel of known facts about specific
      loci (paksha/sapaksha/vipaksha instances),
      each tagged with the pramana that established it
    * a VyaptiDatabase of general rules            (vyapti.py)
    * the Pancavayava syllogism generator           (syllogism.py)
    * the Hetvabhasa (fallacy) checker               (fallacy.py)
    * a TarkaCorpus grounding the whole system in the
      real, ingested Tarkasamgraha-with-Dipika source text
      (tarka_corpus.py)

...plus five neuro-symbolic ML bridges, each mapped onto a classical
Pramana exactly as described in the design specification:

    1. nlp_bridge.py         -- LLM-style NL parsing feeds Anumana
    2. embeddings.py /
       upamana_engine.py     -- vector similarity powers Upamana
    3. rag_shabda.py         -- RAG over trusted documents powers Shabda
    4. vision_pratyaksha.py  -- Computer Vision powers Pratyaksha
    5. rule_miner.py         -- Association-rule mining discovers Vyaptis

In every case, the ML component only ever proposes facts or parses
text; the symbolic core (fallacy.py) is what actually validates or
rejects them. This is the "neuro-symbolic firewall" that stops any ML
hallucination from becoming an accepted logical conclusion.
"""
from vyapti import VyaptiDatabase
from syllogism import Syllogism
from fallacy import diagnose
import ontology_data as OD
from nlp_bridge import NyayaNLParser
from vision_pratyaksha import PratyakshaVision
from rag_shabda import RAGShabda
from upamana_engine import UpamanaEngine
from rule_miner import VyaptiMiner
from tarka_corpus import TarkaCorpus


class WorldModel:
    """Tracks known facts about specific loci, each tagged with the
    pramana (means of knowledge) that established it.

    self.facts = { locus_name: { property_name: (value, source) } }
    """

    def __init__(self):
        self.facts = {}

    def set_fact(self, locus, prop, value, source="assumed"):
        self.facts.setdefault(locus, {})[prop] = (value, source)

    def get_fact(self, locus, prop):
        return self.facts.get(locus, {}).get(prop, (None, None))

    def has_property(self, locus, prop):
        value, _source = self.get_fact(locus, prop)
        return value

    def source_of(self, locus, prop):
        _value, source = self.get_fact(locus, prop)
        return source

    def locus_exists(self, locus):
        return locus in self.facts

    def describe_locus(self, locus):
        if not self.locus_exists(locus):
            return f"'{locus}' is not a known locus."
        lines = [f"Known facts about '{locus}':"]
        for prop, (value, source) in self.facts[locus].items():
            lines.append(f"  - {prop} = {value}  (via {source})")
        return "\n".join(lines)


class TarkaEngine:
    """The main reasoning engine. Instantiate one TarkaEngine per
    'session' / debate."""

    def __init__(self, auto_load_corpus=True, corpus_ingest_limit=None):
        self.vyapti_db = VyaptiDatabase()
        self.world = WorldModel()
        self._log = []
        # -- neuro-symbolic bridges -----------------------------------
        self.nlp = NyayaNLParser()
        self.vision = PratyakshaVision()
        self.rag = RAGShabda()
        self.upamana = UpamanaEngine()
        self.miner = VyaptiMiner()
        # -- textual grounding (the real Tarkasamgraha source text) ---
        self.corpus = TarkaCorpus()
        self.corpus_loaded_chunks = 0
        if auto_load_corpus:
            self.load_corpus(limit=corpus_ingest_limit)

    # ------------------------------------------------------------------
    # Corpus / grounding
    # ------------------------------------------------------------------
    def load_corpus(self, limit=None):
        """Ingest the full Tarkasamgraha-with-Dipika source text (from
        data/tarkasangraha_corpus.json) into the RAG-Shabda trusted
        document store, so every Shabda query and every ontology term
        can be grounded in / cited against the real text."""
        n = self.corpus.ingest_into(self.rag, limit=limit)
        self.corpus_loaded_chunks = n
        return n

    def ground_term(self, term, top_k=3):
        """Return the most relevant passages of the real source text
        for a given Nyaya term (e.g. 'pratyaksha', 'dravya', 'gunas'),
        for citation/verification purposes. Read-only: does not touch
        the WorldModel."""
        return self.rag.query_passages(term, top_k=top_k, threshold=0.0)

    def keyword_search(self, term, max_hits=5):
        """Cheap raw-text substring search over the ingested corpus."""
        return self.corpus.keyword_search(term, max_hits=max_hits)

    # ------------------------------------------------------------------
    # Ontology (Padartha) queries
    # ------------------------------------------------------------------
    def classify(self, name):
        """Return the Tarkasamgraha classification of a named entity
        (a Dravya, Guna or Karma object), or None if unknown."""
        return OD.describe(name)

    def ontology_summary(self):
        return OD.list_all()

    # ------------------------------------------------------------------
    # Knowledge entry (manual / symbolic)
    # ------------------------------------------------------------------
    def declare_locus(self, locus, source="assumed", **properties):
        """Declare a subject (paksha/sapaksha/vipaksha) together with
        any already-known facts about it."""
        if not properties:
            self.world.facts.setdefault(locus, {})
        for prop, value in properties.items():
            self.world.set_fact(locus, prop, value, source=source)

    def perceive(self, locus, prop, value=True):
        """Record a directly-perceived fact (the strongest pramana)."""
        self.world.set_fact(locus, prop, value, source="pratyaksha")

    def teach_vyapti(self, hetu, sadhya, sapaksha=None, vipaksha=None,
                      upadhi=None):
        """Add a general rule (vyapti) to the knowledge base."""
        return self.vyapti_db.add(hetu, sadhya, sapaksha, vipaksha,
                                   upadhi=upadhi)

    def add_counterexample(self, hetu, sadhya, instance):
        """Register an instance that breaks a previously-taught vyapti
        (hetu present, sadhya absent) -- exposes a savyabhichara hetu."""
        v = self.vyapti_db.get(hetu, sadhya)
        if v is None:
            raise ValueError(
                f"No vyapti({hetu} -> {sadhya}) has been taught yet; "
                f"call teach_vyapti() first."
            )
        v.add_counterexample(instance)
        return v

    # ------------------------------------------------------------------
    # Reasoning (Anumana) -- the symbolic core
    # ------------------------------------------------------------------
    def infer(self, paksha, hetu, sadhya, verbose=True):
        """
        Attempt the inference: "<paksha> has <sadhya>, because it has
        <hetu>."

        Returns a dict:
            {"valid": bool,
             "result": Syllogism (if valid) or FallacyReport (if not)}
        """
        report = diagnose(paksha, hetu, sadhya, self.vyapti_db, self.world)
        if report is not None:
            self._log.append(("REJECTED", paksha, hetu, sadhya, report.name))
            if verbose:
                print(f"\n>>> Inference attempted: '{paksha}' has "
                      f"'{sadhya}' because '{hetu}'.")
                print(">>> REJECTED.")
                print(report)
            return {"valid": False, "result": report}

        vyapti = self.vyapti_db.get(hetu, sadhya)
        example = vyapti.sapaksha or "a known instance"
        syl = Syllogism(paksha, hetu, sadhya, example)
        # Forward-chaining: the newly-established fact becomes
        # available for further inferences.
        self.world.set_fact(paksha, sadhya, True, source="anumana")
        self._log.append(("VALID", paksha, hetu, sadhya, "sad-hetu"))
        if verbose:
            print(f"\n>>> Inference attempted: '{paksha}' has "
                  f"'{sadhya}' because '{hetu}'.")
            print(">>> VALID (sad-hetu). Generating proof...\n")
            print("--- Svartha-anumana (reasoning for oneself) ---")
            print(syl.svartha_anumana())
            print("\n--- Parartha-anumana (five-membered syllogism) ---")
            print(syl.parartha_anumana())
        return {"valid": True, "result": syl}

    # ------------------------------------------------------------------
    # Neuro-Symbolic Bridge #1: LLM / NLP -> Anumana
    # ------------------------------------------------------------------
    def infer_from_text(self, text, verbose=True):
        """Parse a natural-language argument into (paksha, hetu,
        sadhya) using self.nlp, then run it through the ordinary
        symbolic inference pipeline. The parser never decides
        validity -- only fallacy.py does -- so no hallucinated logic
        can slip through."""
        parsed = self.nlp.parse(text)
        if not parsed.get("success"):
            if verbose:
                print(f"\n[NLP-Bridge] Could not parse: \"{text}\"")
                print(f"  Reason: {parsed.get('reason')}")
            return {"valid": False, "result": parsed}

        paksha, hetu, sadhya = parsed["paksha"], parsed["hetu"], parsed["sadhya"]
        if verbose:
            print(f"\n[NLP-Bridge ({parsed.get('backend')})] \"{text}\"")
            print(f"  -> paksha='{paksha}', hetu='{hetu}', sadhya='{sadhya}'")

        # Treat the parser's extraction as an (as yet unverified by any
        # stronger pramana) observed property -- exactly like a
        # perception report -- so the fallacy gauntlet can still run.
        if not self.world.locus_exists(paksha):
            self.declare_locus(paksha)
        if self.world.has_property(paksha, hetu) is None:
            self.world.set_fact(paksha, hetu, True, source="assumed")
        return self.infer(paksha, hetu, sadhya, verbose=verbose)

    # ------------------------------------------------------------------
    # Neuro-Symbolic Bridge #2: Computer Vision -> Pratyaksha
    # ------------------------------------------------------------------
    def perceive_image(self, image_input, confidence_threshold=0.5,
                        verbose=True):
        """Run a (mock or real) computer-vision backend and load its
        detections into the WorldModel as Pratyaksha facts."""
        return self.vision.perceive_image(self.world, image_input,
                                           confidence_threshold, verbose)

    # ------------------------------------------------------------------
    # Neuro-Symbolic Bridge #3: RAG -> Shabda
    # ------------------------------------------------------------------
    def ingest_trusted_document(self, text, source_name):
        """Add a passage to the RAG-backed Shabda knowledge store."""
        msg = self.rag.ingest(text, source_name)
        print(msg)
        return msg

    def query_shabda(self, locus, prop, query_text, value=True,
                      threshold=None, verbose=True):
        """Retrieve the most relevant trusted passage and assert the
        fact via Shabda if -- and only if -- it is backed by an
        ingested Apta source."""
        if not self.world.locus_exists(locus):
            self.declare_locus(locus)
        result = self.rag.query_and_assert(self.world, locus, prop,
                                            query_text, value=value,
                                            threshold=threshold)
        if verbose:
            print(result["message"])
        return result

    # ------------------------------------------------------------------
    # Neuro-Symbolic Bridge #4: Embeddings -> Upamana
    # ------------------------------------------------------------------
    def learn_reference_object(self, name, description):
        """Teach the Upamana engine a known reference object."""
        self.upamana.learn_reference(name, description)

    def classify_by_upamana(self, target_name, description,
                             resulting_name=None, threshold=None,
                             verbose=True):
        """Classify an unknown object by embedding-similarity to known
        reference objects."""
        result = self.upamana.classify_by_similarity(
            self.world, target_name, description, resulting_name, threshold
        )
        if verbose:
            print(result["message"])
        return result

    # ------------------------------------------------------------------
    # Neuro-Symbolic Bridge #5: Association-Rule Mining -> Vyapti
    # ------------------------------------------------------------------
    def discover_vyaptis(self, transactions, min_support=0.3,
                          min_confidence=0.85, auto_teach=True,
                          sample_id_lookup=None, verbose=True):
        """Mine a dataset of past observations (bhuyodarshana) for
        association rules and, optionally, teach the qualifying ones to
        the engine as new Vyaptis."""
        rules = self.miner.mine(transactions, min_support, min_confidence)
        if verbose:
            print(f"[Vyapti-Miner] Found {len(rules)} candidate rule(s) "
                  f"at support>={min_support}, confidence>={min_confidence}.")
        if auto_teach:
            self.miner.teach_engine(self, rules,
                                     sample_id_lookup=sample_id_lookup,
                                     verbose=verbose)
        return rules

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------
    def history(self):
        """Return the log of every inference attempted this session."""
        return list(self._log)

    def summary(self):
        valid = sum(1 for e in self._log if e[0] == "VALID")
        rejected = sum(1 for e in self._log if e[0] == "REJECTED")
        embed_backend = self.upamana.index.embedder.backend_name()
        lines = [
            "=== TarkaEngine Session Summary ===",
            f"Loci known to WorldModel : {len(self.world.facts)}",
            f"Vyaptis in database      : {len(self.vyapti_db)}",
            f"Inferences attempted     : {len(self._log)} "
            f"({valid} valid / {rejected} rejected)",
            f"Trusted (Shabda) docs    : {len(self.rag.store)} "
            f"across sources: {', '.join(self.rag.store.sources()) or '(none)'}",
            f"Upamana references known : {len(self.upamana.known_references())}",
            f"Embedding backend        : {embed_backend}",
            f"Tarkasamgraha corpus     : {self.corpus_loaded_chunks} "
            f"passages ingested as Apta source",
        ]
        return "\n".join(lines)
