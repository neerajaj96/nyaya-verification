"""
test_engine.py
--------------
Zero-dependency regression test suite (Python stdlib `unittest` only).

Run with:   python -m unittest test_engine -v
       or:  python test_engine.py
"""
import unittest

from engine import TarkaEngine
import ontology_data as OD
from embeddings import cosine_similarity, vectorize
from rule_miner import apriori, generate_rules


class OntologyTests(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(len(OD.DRAVYAS), 9)
        self.assertEqual(len(OD.GUNAS), 24)
        self.assertEqual(len(OD.KARMAS), 5)

    def test_describe_case_insensitive(self):
        self.assertIsNotNone(OD.describe("prithvi"))
        self.assertIsNotNone(OD.describe("PRITHVI"))
        self.assertIsNone(OD.describe("NotARealThing"))


class InferenceTests(unittest.TestCase):
    def setUp(self):
        self.engine = TarkaEngine(auto_load_corpus=False)

    def test_valid_inference(self):
        e = self.engine
        e.declare_locus("Kitchen", smoke=True, fire=True)
        e.declare_locus("Mountain", smoke=True)
        e.teach_vyapti("smoke", "fire", sapaksha="a kitchen")
        result = e.infer("Mountain", "smoke", "fire", verbose=False)
        self.assertTrue(result["valid"])

    def test_ashrayasiddha(self):
        e = self.engine
        e.teach_vyapti("x", "y", sapaksha="z")
        result = e.infer("NoSuchLocus", "x", "y", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Ashrayasiddha", result["result"].name)

    def test_svarupasiddha_absent(self):
        e = self.engine
        e.declare_locus("Sound", ocular=False)
        e.teach_vyapti("ocular", "quality-hood")
        result = e.infer("Sound", "ocular", "quality-hood", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Svarupasiddha", result["result"].name)

    def test_vyapti_asiddha(self):
        e = self.engine
        e.declare_locus("Well", coolness=True)
        result = e.infer("Well", "coolness", "medicine", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Vyapti-asiddha", result["result"].name)

    def test_sadharana_over_wide(self):
        e = self.engine
        e.declare_locus("Lake", knowable=True, fire=False)
        e.declare_locus("Hill", knowable=True)
        e.teach_vyapti("knowable", "fire", sapaksha="a kitchen")
        e.add_counterexample("knowable", "fire", "Lake")
        result = e.infer("Hill", "knowable", "fire", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Sadharana", result["result"].name)

    def test_asadharana_over_narrow(self):
        e = self.engine
        e.declare_locus("Sound2", shabdatva=True)
        e.teach_vyapti("shabdatva", "eternality", sapaksha=None)
        result = e.infer("Sound2", "shabdatva", "eternality", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Asadharana", result["result"].name)

    def test_viruddha(self):
        e = self.engine
        e.declare_locus("Sound3", krtakatva=True)
        e.teach_vyapti("krtakatva", "not-eternality", sapaksha="a jar")
        result = e.infer("Sound3", "krtakatva", "eternality", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Viruddha", result["result"].name)

    def test_satpratipaksha(self):
        e = self.engine
        e.declare_locus("Sound4", shravanatva=True, karyatva=True)
        e.teach_vyapti("shravanatva", "eternality", sapaksha="x")
        e.teach_vyapti("karyatva", "not-eternality", sapaksha="a jar")
        result = e.infer("Sound4", "shravanatva", "eternality", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Satpratipaksha", result["result"].name)

    def test_badhita(self):
        e = self.engine
        e.declare_locus("Fire1", dravyatva=True)
        e.perceive("Fire1", "not-cold", True)
        e.teach_vyapti("dravyatva", "cold", sapaksha="air")
        result = e.infer("Fire1", "dravyatva", "cold", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Badhita", result["result"].name)

    def test_vyapyatvasiddha(self):
        e = self.engine
        e.declare_locus("Mountain3", vahni=True)
        e.teach_vyapti("vahni", "dhuma", sapaksha="a kitchen",
                       upadhi="ardra-indhana-samyoga")
        result = e.infer("Mountain3", "vahni", "dhuma", verbose=False)
        self.assertFalse(result["valid"])
        self.assertIn("Vyapyatvasiddha", result["result"].name)

    def test_forward_chaining(self):
        e = self.engine
        e.declare_locus("Mountain", smoke=True)
        e.declare_locus("Kitchen", smoke=True, fire=True)
        e.teach_vyapti("smoke", "fire", sapaksha="a kitchen")
        e.teach_vyapti("fire", "heat", sapaksha="a kitchen")
        e.infer("Mountain", "smoke", "fire", verbose=False)
        result = e.infer("Mountain", "fire", "heat", verbose=False)
        self.assertTrue(result["valid"])


class NLPBridgeTests(unittest.TestCase):
    def setUp(self):
        self.engine = TarkaEngine(auto_load_corpus=False)
        self.engine.declare_locus("Kitchen", smoke=True, fire=True)
        self.engine.teach_vyapti("smoke", "fire", sapaksha="a kitchen")

    def test_parses_and_infers_valid(self):
        result = self.engine.infer_from_text(
            "That hill must be burning because it's billowing smoke!",
            verbose=False)
        self.assertTrue(result["valid"])

    def test_never_hallucinates_unknown_rule(self):
        result = self.engine.infer_from_text(
            "That pond must be poisoned since the fish are dying.",
            verbose=False)
        self.assertFalse(result["valid"])

    def test_empty_input_fails_gracefully(self):
        result = self.engine.nlp.parse("")
        self.assertFalse(result["success"])

    def test_no_connective_fails_gracefully(self):
        result = self.engine.nlp.parse("The sky is blue today")
        self.assertFalse(result["success"])


class VisionBridgeTests(unittest.TestCase):
    def setUp(self):
        self.engine = TarkaEngine(auto_load_corpus=False)

    def test_string_scene_detection(self):
        detections = self.engine.perceive_image(
            "a mountain with thick smoke rising from its peak",
            verbose=False)
        self.assertTrue(any(a == "smoke" for _, a, _, _ in detections))
        self.assertEqual(self.engine.world.has_property("Mountain", "smoke"),
                          True)

    def test_low_confidence_is_skipped(self):
        self.engine.perceive_image(
            {"Ghost": {"attributes": {"spooky": True}, "confidence": 0.1}},
            confidence_threshold=0.5, verbose=False)
        self.assertIsNone(self.engine.world.has_property("Ghost", "spooky"))


class RAGShabdaTests(unittest.TestCase):
    def setUp(self):
        self.engine = TarkaEngine(auto_load_corpus=False)

    def test_accepts_backed_fact(self):
        self.engine.ingest_trusted_document(
            "Water boils at 100 degrees Celsius at sea level.",
            source_name="Textbook")
        result = self.engine.query_shabda(
            "Water", "boils_at_100C", "does water boil at 100 celsius?",
            verbose=False)
        self.assertTrue(result["accepted"])

    def test_rejects_unbacked_fact(self):
        self.engine.ingest_trusted_document(
            "Water boils at 100 degrees Celsius at sea level.",
            source_name="Textbook")
        result = self.engine.query_shabda(
            "Moon", "made_of_cheese", "is the moon made of cheese?",
            verbose=False)
        self.assertFalse(result["accepted"])

    def test_rejects_with_empty_store(self):
        result = self.engine.query_shabda(
            "X", "y", "anything", verbose=False)
        self.assertFalse(result["accepted"])


class UpamanaTests(unittest.TestCase):
    def setUp(self):
        self.engine = TarkaEngine(auto_load_corpus=False)
        self.engine.learn_reference_object(
            "Cow", "domestic bovine animal four legs horns tail milk")

    def test_classifies_similar_object(self):
        result = self.engine.classify_by_upamana(
            "Gavaya", "wild forest animal four legs horns tail resembling cattle",
            verbose=False)
        self.assertTrue(result["success"])

    def test_refuses_dissimilar_object(self):
        result = self.engine.classify_by_upamana(
            "Spacecraft", "metal vehicle rocket engines orbit",
            threshold=0.6, verbose=False)
        self.assertFalse(result["success"])

    def test_refuses_with_no_references(self):
        engine = TarkaEngine(auto_load_corpus=False)
        result = engine.classify_by_upamana("X", "some description",
                                             verbose=False)
        self.assertFalse(result["success"])


class RuleMinerTests(unittest.TestCase):
    def test_apriori_support(self):
        transactions = [{"a", "b"}, {"a", "b"}, {"a"}, {"b"}]
        freq = apriori(transactions, min_support=0.5)
        self.assertIn(frozenset(["a"]), freq)
        self.assertIn(frozenset(["b"]), freq)

    def test_generate_rules_confidence(self):
        transactions = [{"a", "b"}] * 3 + [{"a"}]
        freq = apriori(transactions, min_support=0.5)
        rules = generate_rules(freq, transactions, min_confidence=0.7)
        self.assertTrue(any(
            r["antecedent"] == frozenset(["a"]) and
            r["consequent"] == frozenset(["b"]) for r in rules))

    def test_end_to_end_discovery(self):
        engine = TarkaEngine(auto_load_corpus=False)
        transactions = [{"heavy_clouds", "high_humidity", "rain"}] * 4 + \
                       [{"clear_sky", "no_rain"}] * 4
        rules = engine.discover_vyaptis(transactions, min_support=0.3,
                                         min_confidence=0.9,
                                         auto_teach=True, verbose=False)
        self.assertGreater(len(rules), 0)
        self.assertGreater(len(engine.vyapti_db), 0)


class EmbeddingTests(unittest.TestCase):
    def test_identical_text_similarity_is_one(self):
        v = vectorize("smoke and fire on the mountain")
        self.assertAlmostEqual(cosine_similarity(v, v), 1.0, places=6)

    def test_disjoint_text_similarity_is_zero(self):
        v1 = vectorize("smoke fire mountain")
        v2 = vectorize("banana spaceship guitar")
        self.assertEqual(cosine_similarity(v1, v2), 0.0)


class CorpusGroundingTests(unittest.TestCase):
    def test_corpus_autoloads_and_grounds(self):
        engine = TarkaEngine(auto_load_corpus=True, corpus_ingest_limit=100)
        self.assertGreater(engine.corpus_loaded_chunks, 0)
        hits = engine.ground_term("perception sense organ contact", top_k=1)
        # With a limited ingest, a hit may or may not clear threshold=0;
        # the call must simply not raise, and return a list.
        self.assertIsInstance(hits, list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
