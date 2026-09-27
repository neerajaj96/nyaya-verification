"""
interactive_cli.py
-------------------
Interactive Command Line Interface for the Navya-Nyaya Reasoning Engine.

Exposes both the pure symbolic core (teach a rule / state a fact /
formulate an inference) and all five neuro-symbolic ML bridges
(NLP parsing, Computer Vision perception, RAG-backed Shabda, Upamana by
embedding-similarity, and Vyapti discovery via association-rule mining)
plus the textual-grounding layer over the real, auto-ingested
Tarkasamgraha source text.

Run with:   python interactive_cli.py
"""
from engine import TarkaEngine
from rule_miner import make_sample_lookup

SAMPLE_WEATHER_TRANSACTIONS = [
    {"heavy_clouds", "high_humidity", "rain"},
    {"heavy_clouds", "high_humidity", "rain"},
    {"heavy_clouds", "high_humidity", "rain"},
    {"heavy_clouds", "low_humidity", "no_rain"},
    {"clear_sky", "low_humidity", "no_rain"},
    {"clear_sky", "low_humidity", "no_rain"},
    {"heavy_clouds", "high_humidity", "rain"},
    {"clear_sky", "high_humidity", "no_rain"},
]


def print_header(text):
    print(f"\n{'-' * 60}\n{text}\n{'-' * 60}")


def ask(prompt, default=None):
    """input() wrapper that treats a blank line as default and never
    raises on EOF (so the CLI can also be driven by piped input)."""
    try:
        raw = input(prompt)
    except EOFError:
        return default
    raw = raw.strip()
    return raw if raw else default


def menu_teach_vyapti(engine):
    print_header("TEACH A RULE (VYAPTI)")
    hetu = ask("Enter the Hetu (Reason, e.g. 'smoke'): ")
    sadhya = ask("Enter the Sadhya (What it proves, e.g. 'fire'): ")
    sapaksha = ask("Enter a Sapaksha (known example, e.g. 'kitchen') "
                   "[optional]: ")
    upadhi = ask("Enter an Upadhi (hidden condition, e.g. 'wet fuel') "
                 "[optional]: ")
    if not hetu or not sadhya:
        print("\n[Error] Hetu and Sadhya are both required.")
        return
    engine.teach_vyapti(hetu, sadhya, sapaksha=sapaksha, upadhi=upadhi)
    if upadhi:
        print(f"\n[Learned] Conditional rule: wherever there is '{hetu}', "
              f"there is '{sadhya}', PROVIDED there is '{upadhi}'.")
    else:
        print(f"\n[Learned] Universal rule: wherever there is '{hetu}', "
              f"there is '{sadhya}'.")


def menu_state_fact(engine):
    print_header("STATE A FACT (PRATYAKSHA)")
    locus = ask("Enter the Locus (subject, e.g. 'Mountain'): ")
    prop = ask("Enter the property present on it (e.g. 'smoke'): ")
    if not locus or not prop:
        print("\n[Error] Locus and property are both required.")
        return
    engine.declare_locus(locus, **{prop: True})
    print(f"\n[Recorded] Fact established: '{locus}' possesses '{prop}'.")


def menu_infer(engine):
    print_header("FORMULATE AN INFERENCE (ANUMANA)")
    paksha = ask("Enter the Paksha (subject, e.g. 'Mountain'): ")
    hetu = ask("Enter the Hetu (reason, e.g. 'smoke'): ")
    sadhya = ask("Enter the Sadhya (to prove, e.g. 'fire'): ")
    if not paksha or not hetu or not sadhya:
        print("\n[Error] Paksha, Hetu and Sadhya are all required.")
        return
    print("\nProcessing Tarkasamgraha Logic...")
    engine.infer(paksha, hetu, sadhya, verbose=True)


def menu_nlp_infer(engine):
    print_header("NLP BRIDGE: INFER FROM A NATURAL-LANGUAGE SENTENCE")
    print("Example: \"That hill must be burning because it's billowing "
          "smoke!\"")
    text = ask("Enter your argument in plain English: ")
    if not text:
        print("\n[Error] Please type a sentence.")
        return
    engine.infer_from_text(text, verbose=True)


def menu_vision(engine):
    print_header("VISION BRIDGE: PERCEIVE FROM AN 'IMAGE'")
    print("This is a MOCK vision backend (no real image files needed).")
    print("Type a short scene description, e.g.:")
    print("  'a mountain with thick smoke rising from its peak'")
    text = ask("Scene description: ")
    if not text:
        print("\n[Error] Please type a description.")
        return
    engine.perceive_image(text, confidence_threshold=0.5, verbose=True)


def menu_rag_ingest(engine):
    print_header("SHABDA/RAG: INGEST A TRUSTED DOCUMENT")
    source = ask("Source name (e.g. 'Physics Textbook Ch.4'): ",
                 default="Anonymous Source")
    text = ask("Paste the trusted passage text: ")
    if not text:
        print("\n[Error] Please provide passage text.")
        return
    engine.ingest_trusted_document(text, source)


def menu_rag_query(engine):
    print_header("SHABDA/RAG: QUERY & ASSERT A FACT")
    locus = ask("Locus to attach the fact to (e.g. 'Water'): ")
    prop = ask("Property to assert (e.g. 'boils_at_100C'): ")
    query = ask("Question / query text to search the trusted documents "
                "with: ")
    if not (locus and prop and query):
        print("\n[Error] Locus, property and query are all required.")
        return
    engine.query_shabda(locus, prop, query, verbose=True)


def menu_upamana_learn(engine):
    print_header("UPAMANA: TEACH A REFERENCE OBJECT")
    name = ask("Reference object name (e.g. 'Cow'): ")
    desc = ask("Short description (e.g. 'domestic bovine, four legs, "
               "horns, gives milk'): ")
    if not (name and desc):
        print("\n[Error] Name and description are both required.")
        return
    engine.learn_reference_object(name, desc)
    print(f"\n[Learned] Reference object '{name}' registered for Upamana.")


def menu_upamana_classify(engine):
    print_header("UPAMANA: CLASSIFY AN UNKNOWN OBJECT BY SIMILARITY")
    known = engine.upamana.known_references()
    print(f"Known reference objects: {known if known else '(none yet)'}")
    name = ask("Unknown object name (e.g. 'Gavaya'): ")
    desc = ask("Short description of it (e.g. 'wild ox resembling a "
               "cow, four legs, horns'): ")
    if not (name and desc):
        print("\n[Error] Name and description are both required.")
        return
    engine.classify_by_upamana(name, desc, verbose=True)


def menu_discover_vyapti(engine):
    print_header("VYAPTI-MINER: DISCOVER RULES FROM OBSERVED DATA")
    print("Using a small built-in weather dataset "
          "({heavy_clouds, high_humidity} -> {rain}).")
    min_support = ask("Minimum support (0-1) [default 0.3]: ",
                       default="0.3")
    min_conf = ask("Minimum confidence (0-1) [default 0.85]: ",
                   default="0.85")
    try:
        min_support = float(min_support)
        min_conf = float(min_conf)
    except ValueError:
        print("\n[Error] Support/confidence must be numbers.")
        return
    lookup = make_sample_lookup(SAMPLE_WEATHER_TRANSACTIONS)
    engine.discover_vyaptis(SAMPLE_WEATHER_TRANSACTIONS,
                             min_support=min_support,
                             min_confidence=min_conf,
                             auto_teach=True,
                             sample_id_lookup=lookup,
                             verbose=True)


def menu_ontology(engine):
    print_header("ONTOLOGY LOOKUP (PADARTHA)")
    name = ask("Enter a term (e.g. 'Prithvi', 'shabda', 'gamana'): ")
    if not name:
        print("\n[Error] Please type a term.")
        return
    result = engine.classify(name)
    if result is None:
        print(f"\n'{name}' was not found in the seeded ontology.")
    else:
        print("\n" + result.info())


def menu_ground_term(engine):
    print_header("GROUND A TERM IN THE REAL TARKASAMGRAHA SOURCE TEXT")
    term = ask("Enter a term or short question (e.g. 'what is pratyaksha'): ")
    if not term:
        print("\n[Error] Please type a term or question.")
        return
    hits = engine.ground_term(term, top_k=3)
    if not hits:
        print("\nNo sufficiently similar passage was found in the "
              "ingested source text.")
        return
    print(f"\nTop passages from '{engine.corpus.source_name}':")
    for i, (doc, score) in enumerate(hits, 1):
        print(f"\n[{i}] similarity={score:.3f}\n    {doc.excerpt(300)}")


MENU = """
Available Commands:
  [1]  Teach a Universal Rule (Vyapti)
  [2]  State an Observed Fact (Pratyaksha)
  [3]  Formulate an Inference (Anumana)
  [4]  NLP Bridge: Infer from a natural-language sentence
  [5]  Vision Bridge: Perceive from a mock 'image' description
  [6]  Shabda/RAG: Ingest a trusted document
  [7]  Shabda/RAG: Query trusted documents & assert a fact
  [8]  Upamana: Teach a reference object
  [9]  Upamana: Classify an unknown object by similarity
  [10] Vyapti-Miner: Discover rules from observed data (Apriori)
  [11] Ontology Lookup (Padartha info)
  [12] Ground a term in the real Tarkasamgraha source text
  [13] Show session summary & inference log
  [14] Exit
"""

HANDLERS = {
    "1": menu_teach_vyapti,
    "2": menu_state_fact,
    "3": menu_infer,
    "4": menu_nlp_infer,
    "5": menu_vision,
    "6": menu_rag_ingest,
    "7": menu_rag_query,
    "8": menu_upamana_learn,
    "9": menu_upamana_classify,
    "10": menu_discover_vyapti,
    "11": menu_ontology,
    "12": menu_ground_term,
}


def main():
    engine = TarkaEngine()
    print("=" * 60)
    print(" NAVYA-NYAYA NEURO-SYMBOLIC REASONING ENGINE")
    print("=" * 60)
    print("Welcome! Teach the engine rules, state facts, and test logic")
    print("-- including the LLM/Vision/RAG/Embedding/Mining ML bridges.")
    print(f"({engine.corpus_loaded_chunks} passages of the real "
          f"Tarkasamgraha source text have been auto-loaded as the "
          f"default Apta/Shabda corpus.)")
    try:
        while True:
            print(MENU)
            choice = ask("Select an option (1-14): ", default="")
            if choice == "13":
                print_header("SESSION SUMMARY")
                print(engine.summary())
                print("\nFull inference log:")
                for entry in engine.history():
                    status, paksha, hetu, sadhya, tag = entry
                    print(f"  [{status:8s}] {paksha:12s} | hetu={hetu:15s} "
                          f"| sadhya={sadhya:15s} | {tag}")
                continue
            if choice == "14" or choice == "":
                print_header("SESSION SUMMARY")
                print(engine.summary())
                print("Exiting engine. Namaste!")
                return
            handler = HANDLERS.get(choice)
            if handler is None:
                print("\n[Error] Invalid choice. Please enter a number "
                      "between 1 and 14.")
                continue
            try:
                handler(engine)
            except Exception as exc:   # pragma: no cover - safety net
                print(f"\n[Error] Something went wrong while processing "
                      f"that command: {exc}")
    except (EOFError, KeyboardInterrupt):
        print("\n\n[Session ended]")
        print(engine.summary())
        print("Namaste!")


if __name__ == "__main__":
    main()
