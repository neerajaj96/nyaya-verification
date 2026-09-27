"""
pramana.py
----------
The four valid means of knowledge (pramana) recognised by Annambhatta:

    Pratyaksha (Perception)        -- Section 42
    Anumana    (Inference)         -- Sections 44-57 (see syllogism.py,
                                       fallacy.py, engine.py)
    Upamana    (Comparison)        -- Section 58
    Shabda     (Verbal testimony)  -- Section 59

These base classes are intentionally simple/manual. The ML-augmented
versions (embedding-based Upamana, RAG-based Shabda, CV-based
Pratyaksha) are layered on top of these in upamana_engine.py,
rag_shabda.py and vision_pratyaksha.py respectively -- they do not
replace these classes, they call them.
"""


class Pratyaksha:
    """Perception: knowledge produced by direct sense-object contact
    (indriyartha-sannikarsha), Section 42. Perception is treated as the
    strongest pramana -- facts it establishes can defeat (badhita) a
    contrary inference."""

    @staticmethod
    def perceive(world, locus, prop, value=True):
        world.set_fact(locus, prop, value, source="pratyaksha")
        verb = "possesses" if value else "lacks"
        return f"[Pratyaksha] Directly perceived that '{locus}' {verb} '{prop}'."


class Upamana:
    """Comparison/Analogy: knowledge of the relation between a name and
    an object via a perceived similarity (Section 58) -- e.g. learning
    what a 'gavaya' (gayal) is by being told it resembles a cow, then
    perceiving that similarity."""

    def __init__(self, ref_obj, target_object, shared_props):
        self.ref_obj = ref_obj
        self.target_object = target_object
        self.shared_props = list(shared_props)

    def analogize(self, world, resulting_name):
        world.set_fact(self.target_object, f"named:{resulting_name}",
                        True, source="upamana")
        return (f"[Upamana] '{self.target_object}' resembles "
                f"'{self.ref_obj}' (shared: {', '.join(self.shared_props)}), "
                f"thus named/classified as '{resulting_name}'.")


class Shabda:
    """Verbal testimony (shabda): knowledge from the statement of a
    credible source (apta), Section 59. An apta is "one who speaks the
    truth" (yatharthavakta)."""

    def __init__(self, speaker, is_trustworthy=True):
        self.speaker = speaker
        self.is_trustworthy = is_trustworthy

    def testify(self, world, locus, prop, value=True):
        if not self.is_trustworthy:
            return (f"[Shabda] REJECTED: '{self.speaker}' is not an Apta "
                    f"(credible source); testimony not accepted.")
        world.set_fact(locus, prop, value, source="shabda")
        return (f"[Shabda] Accepted testimony from Apta '{self.speaker}': "
                f"'{locus}' has '{prop}'={value}.")
