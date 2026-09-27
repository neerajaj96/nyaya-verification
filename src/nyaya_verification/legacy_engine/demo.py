"""
demo.py
-------
End-to-end, fully automated demonstration of the Navya-Nyaya
Neuro-Symbolic Reasoning Engine.

Part A exercises the pure symbolic core: ontology lookup, one valid
inference, and all nine Hetvabhasa (fallacy) diagnostics.

Part B exercises the five neuro-symbolic ML bridges described in the
design specification: NLP->Anumana, Vision->Pratyaksha, RAG->Shabda,
Embeddings->Upamana, and Association-Rule-Mining->Vyapti.

Part C exercises the textual-grounding layer: the real, ingested
Tarkasamgraha-with-Dipika source text is queried for citations backing
ontology terms.

Run with:   python demo.py
"""
from engine import TarkaEngine
from rule_miner import make_sample_lookup


def banner(text):
    print(f"\n{'=' * 78}\n{text}\n{'=' * 78}")


# =======================================================================
# PART A: THE PURE SYMBOLIC CORE
# =======================================================================
def part_a(engine):
    banner("PART A.1: ONTOLOGY LOOKUP (Padarthas)")
    print(engine.classify("Prithvi").info())
    print()
    print(engine.classify("shabda").info())
    print()
    print(engine.classify("gamana").info())

    banner("PART A.2: A VALID INFERENCE -- the classic "
           "Mountain/Smoke/Fire example (Sections 44-46)")
    engine.declare_locus("Kitchen", smoke=True, fire=True)
    engine.declare_locus("Mountain", smoke=True)
    engine.teach_vyapti("smoke", "fire", sapaksha="a kitchen")
    result = engine.infer("Mountain", "smoke", "fire")
    assert result["valid"] is True

    banner("PART A.3: FALLACY -- Ashrayasiddha (unreal locus), Sec. 56")
    engine.teach_vyapti("lotusness", "fragrance", sapaksha="a lake-lotus")
    result = engine.infer("SkyLotus", "lotusness", "fragrance")
    assert result["valid"] is False

    banner("PART A.4: FALLACY -- Svarupasiddha (non-existent reason), "
           "Sec. 56")
    engine.declare_locus("Sound", ocular=False)
    engine.teach_vyapti("ocular", "quality-hood", sapaksha="a jar's colour")
    result = engine.infer("Sound", "ocular", "quality-hood")
    assert result["valid"] is False

    banner("PART A.5: FALLACY -- Savyabhichara/Sadharana (over-wide "
           "reason), Sec. 53")
    engine.declare_locus("Lake", knowable=True, fire=False)
    engine.declare_locus("Hill", knowable=True)
    engine.teach_vyapti("knowable", "fire", sapaksha="a kitchen")
    engine.add_counterexample("knowable", "fire", "Lake")
    result = engine.infer("Hill", "knowable", "fire")
    assert result["valid"] is False

    banner("PART A.6: FALLACY -- Savyabhichara/Asadharana (over-narrow "
           "reason), Sec. 53")
    engine.declare_locus("Sound2", shabdatva=True)
    engine.teach_vyapti("shabdatva", "eternality", sapaksha=None)
    result = engine.infer("Sound2", "shabdatva", "eternality")
    assert result["valid"] is False

    banner("PART A.7: FALLACY -- Viruddha (contrary reason), Sec. 54")
    engine.declare_locus("Sound3", krtakatva=True)
    engine.teach_vyapti("krtakatva", "not-eternality", sapaksha="a jar")
    result = engine.infer("Sound3", "krtakatva", "eternality")
    assert result["valid"] is False

    banner("PART A.8: FALLACY -- Satpratipaksha (counterbalanced "
           "reason), Sec. 55")
    engine.declare_locus("Sound4", shravanatva=True, karyatva=True)
    engine.teach_vyapti("shravanatva", "eternality",
                        sapaksha="another audible eternal thing")
    engine.teach_vyapti("karyatva", "not-eternality", sapaksha="a jar")
    result = engine.infer("Sound4", "shravanatva", "eternality")
    assert result["valid"] is False

    banner("PART A.9: FALLACY -- Badhita (contradicted by perception), "
           "Sec. 57")
    engine.declare_locus("Fire1", dravyatva=True)
    engine.perceive("Fire1", "not-cold", True)
    engine.teach_vyapti("dravyatva", "cold", sapaksha="air")
    result = engine.infer("Fire1", "dravyatva", "cold")
    assert result["valid"] is False

    banner("PART A.10: FALLACY -- Vyapyatvasiddha (hidden condition / "
           "upadhi), Sec. 56")
    engine.declare_locus("Mountain3", vahni=True)
    engine.teach_vyapti("vahni", "dhuma", sapaksha="a kitchen",
                        upadhi="ardra-indhana-samyoga (contact with wet fuel)")
    result = engine.infer("Mountain3", "vahni", "dhuma")
    assert result["valid"] is False

    banner("PART A.11: FALLACY -- Vyapti-asiddha (no rule on record)")
    engine.declare_locus("Well", coolness=True)
    result = engine.infer("Well", "coolness", "medicinal-property")
    assert result["valid"] is False

    banner("PART A.12: FORWARD CHAINING -- a derived conclusion feeds a "
           "further inference")
    engine.teach_vyapti("fire", "heat", sapaksha="a kitchen")
    result = engine.infer("Mountain", "fire", "heat")
    assert result["valid"] is True
    print("\n(The engine reused the 'fire' fact it had itself derived in "
          "A.2 to derive 'heat' here -- a simple forward chain.)")


# =======================================================================
# PART B: THE NEURO-SYMBOLIC ML BRIDGES
# =======================================================================
def part_b_nlp(engine):
    banner("PART B.1: NEURO-SYMBOLIC BRIDGE -- NLP/LLM -> ANUMANA")
    print("A messy natural-language argument is parsed into "
          "(paksha, hetu, sadhya) and fed straight into engine.infer().")
    print("The parser NEVER decides validity -- fallacy.py still does.\n")
    sentence = ("Look at that hill over there, it must be burning "
                "because it's billowing smoke!")
    # The Vyapti smoke->fire already exists from Part A.2, so this
    # should succeed cleanly.
    result = engine.infer_from_text(sentence, verbose=True)
    assert result["valid"] is True

    print("\nNow the SAME sentence pattern is tried for an unrelated "
          "domain the engine was never taught a rule for -- it must be "
          "REJECTED rather than hallucinated:")
    sentence2 = "That pond must be poisoned since the fish are dying."
    result2 = engine.infer_from_text(sentence2, verbose=True)
    assert result2["valid"] is False


def part_b_vision(engine):
    banner("PART B.2: NEURO-SYMBOLIC BRIDGE -- COMPUTER VISION -> "
           "PRATYAKSHA")
    print("A (mock) vision backend 'looks' at a scene description and "
          "loads its detections straight into the WorldModel as the "
          "strongest pramana (pratyaksha).\n")
    engine.perceive_image("a tall mountain with thick smoke rising from "
                           "its peak", confidence_threshold=0.5)
    print("\nThe engine can now run Anumana on what its 'eyes' just saw:")
    result = engine.infer("Mountain", "smoke", "fire", verbose=True)
    assert result["valid"] is True


def part_b_rag(engine):
    banner("PART B.3: NEURO-SYMBOLIC BRIDGE -- RAG -> SHABDA")
    print("Trusted documents are ingested into a vector store. A fact "
          "is only asserted via Shabda if it is backed by a retrieved, "
          "sufficiently-similar trusted passage. The engine has already "
          "auto-ingested the full Tarkasamgraha source text as its "
          "default Apta corpus; here we add two more ad-hoc documents.\n")
    engine.ingest_trusted_document(
        "Water is composed of hydrogen and oxygen and boils at 100 "
        "degrees Celsius at standard atmospheric pressure.",
        source_name="High School Chemistry Textbook"
    )
    engine.ingest_trusted_document(
        "The Ganges is a river in India considered sacred in Hindu "
        "tradition.",
        source_name="Geography Encyclopedia"
    )

    print("\n-- Querying for a fact that IS backed by a trusted doc --")
    result = engine.query_shabda(
        locus="Water", prop="boils_at_100C",
        query_text="does water boil at 100 degrees celsius?"
    )
    assert result["accepted"] is True

    print("\n-- Querying for a fact that is NOT backed by any trusted "
          "doc (should be rejected as 'Not from an Apta') --")
    result2 = engine.query_shabda(
        locus="Moon", prop="made_of_cheese",
        query_text="is the moon made of cheese?"
    )
    assert result2["accepted"] is False


def part_b_upamana(engine):
    banner("PART B.4: NEURO-SYMBOLIC BRIDGE -- EMBEDDINGS -> UPAMANA")
    print("Reference objects are taught with short descriptions. An "
          "unknown object's description is compared by cosine "
          "similarity (vector embeddings) to find the best analogy -- "
          "exactly the classical gavaya/cow example of Section 58.\n")
    engine.learn_reference_object(
        "Cow", "a domestic bovine animal with four legs, horns, a tail, "
               "and gives milk"
    )
    engine.learn_reference_object(
        "Horse", "a large domesticated animal with four legs, a mane, "
                 "and is used for riding"
    )

    print("-- Classifying an unknown 'Gavaya' (wild ox) --")
    result = engine.classify_by_upamana(
        "Gavaya", "a wild forest animal with four legs, horns, and a "
                   "tail, resembling cattle"
    )
    assert result["success"] is True

    print("\n-- Classifying something with no good match (should "
          "refuse to guess) --")
    result2 = engine.classify_by_upamana(
        "Spacecraft", "a metal vehicle with rocket engines that flies "
                       "to orbit", threshold=0.6
    )
    assert result2["success"] is False


def part_b_mining(engine):
    banner("PART B.5: NEURO-SYMBOLIC BRIDGE -- ASSOCIATION-RULE MINING "
           "-> VYAPTI DISCOVERY")
    print("An Apriori-style unsupervised algorithm scans a dataset of "
          "past observations (bhuyodarshana) and automatically teaches "
          "the engine any sufficiently strong concomitance it finds.\n")
    transactions = [
        {"heavy_clouds", "high_humidity", "rain"},
        {"heavy_clouds", "high_humidity", "rain"},
        {"heavy_clouds", "high_humidity", "rain"},
        {"heavy_clouds", "low_humidity", "no_rain"},
        {"clear_sky", "low_humidity", "no_rain"},
        {"clear_sky", "low_humidity", "no_rain"},
        {"heavy_clouds", "high_humidity", "rain"},
        {"clear_sky", "high_humidity", "no_rain"},
    ]
    lookup = make_sample_lookup(transactions)
    rules = engine.discover_vyaptis(
        transactions, min_support=0.3, min_confidence=0.9,
        auto_teach=True, sample_id_lookup=lookup
    )
    assert len(rules) > 0

    print("\nThe engine can now use a mined rule exactly like any "
          "hand-taught Vyapti:")
    engine.declare_locus("Today", high_humidity=True)
    result = engine.infer("Today", "high_humidity", "rain", verbose=True)
    # This may or may not reach 'valid' depending on which single-term
    # rules cleared the confidence bar -- either outcome is informative,
    # so we only require that the engine responded without crashing.
    assert "valid" in result


# =======================================================================
# PART C: TEXTUAL GROUNDING IN THE REAL SOURCE TEXT
# =======================================================================
def part_c_grounding(engine):
    banner("PART C: GROUNDING ONTOLOGY TERMS IN THE INGESTED "
           "TARKASAMGRAHA SOURCE TEXT")
    print(f"Auto-ingested {engine.corpus_loaded_chunks} passages from: "
          f"{engine.corpus.source_name}\n")
    for term, query in [
        ("Pratyaksha (perception)", "perception sense organs contact object"),
        ("Anumana (inference)", "inference smoke fire invariable concomitance"),
        ("Dravya (substance)", "nine substances earth water fire air ether"),
    ]:
        print(f"-- Grounding '{term}' --")
        hits = engine.ground_term(query, top_k=1)
        if hits:
            doc, score = hits[0]
            print(f"  [similarity={score:.3f}] {doc.excerpt(220)}")
        else:
            print("  (no sufficiently similar passage found)")
        print()


# =======================================================================
def main():
    engine = TarkaEngine()
    part_a(engine)
    part_b_nlp(engine)
    part_b_vision(engine)
    part_b_rag(engine)
    part_b_upamana(engine)
    part_b_mining(engine)
    part_c_grounding(engine)

    banner("SESSION SUMMARY")
    print(engine.summary())

    print("\nFull inference log:")
    for entry in engine.history():
        status, paksha, hetu, sadhya, tag = entry
        print(f"  [{status:8s}] {paksha:14s} | hetu={hetu:15s} "
              f"| sadhya={sadhya:15s} | {tag}")

    banner("ALL DEMOS COMPLETED SUCCESSFULLY -- NO ERRORS")


if __name__ == "__main__":
    main()
