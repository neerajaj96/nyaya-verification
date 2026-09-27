"""
ontology_data.py
-----------------
Seed knowledge base drawn directly from Annambhatta's Tarkasamgraha:
the nine substances (Section 3, sub-sections 10-18), the twenty-four
qualities (Section 4, sub-sections 19-33), and the five actions
(Section 5).
"""
from padartha import Dravya, Guna, Karma

# ---------------------------------------------------------------------
# The Nine Substances (dravya) -- Section 3 (detailed: Sections 10-18)
# ---------------------------------------------------------------------
DRAVYAS = {
    "Prithvi": Dravya(
        "Prithvi", eternal=True,
        qualities=["rupa", "rasa", "gandha", "sparsha"],
        description="Earth: distinguished by possessing odour (gandhavati). "
                     "Its atoms are eternal; its products (jars, etc.) are "
                     "non-eternal.", section=10),
    "Ap": Dravya(
        "Ap", eternal=True,
        qualities=["rupa", "rasa", "sparsha", "sneha", "gurutva", "dravatva"],
        description="Water: distinguished by cold touch (shita-sparshavati).",
        section=11),
    "Tejas": Dravya(
        "Tejas", eternal=True,
        qualities=["rupa", "sparsha", "dravatva"],
        description="Light/Fire: distinguished by hot touch (ushna-sparshavat).",
        section=12),
    "Vayu": Dravya(
        "Vayu", eternal=True,
        qualities=["sparsha"],
        description="Air: possesses touch without colour (rupa-rahita "
                     "sparshavan); known only by inference (anumana).",
        section=13),
    "Akasha": Dravya(
        "Akasha", eternal=True,
        qualities=["shabda"],
        description="Ether: possesses sound (shabda) as its exclusive "
                     "special quality; one, all-pervading (vibhu), eternal.",
        section=14),
    "Kala": Dravya(
        "Kala", eternal=True,
        qualities=[],
        description="Time: instrumental cause of the usage 'past/present/"
                     "future'; one, all-pervading, eternal.", section=15),
    "Dik": Dravya(
        "Dik", eternal=True,
        qualities=[],
        description="Space/Direction: instrumental cause of the usage "
                     "'east/west' etc.; one, all-pervading, eternal.",
        section=16),
    "Atman": Dravya(
        "Atman", eternal=True,
        qualities=["buddhi", "sukha", "duhkha", "iccha", "dvesha",
                   "prayatna", "dharma", "adharma", "samskara"],
        description="Soul: substratum of cognition (jnanadhikaranam). "
                     "Two kinds -- Paramatman (God, one, omniscient) and "
                     "Jivatman (individual souls, many, all-pervading, "
                     "eternal).", section=17),
    "Manas": Dravya(
        "Manas", eternal=True,
        qualities=[],
        description="Mind: the internal organ (antarindriya) through which "
                     "pleasure, pain, etc. are perceived; atomic (anu), "
                     "eternal, one for each soul.", section=18),
}

# ---------------------------------------------------------------------
# The Twenty-Four Qualities (guna) -- Section 4 (detailed: Sections 19-33)
# ---------------------------------------------------------------------
GUNA_INFO = {
    "rupa":       ("Colour",               ["Prithvi", "Ap", "Tejas"], 19),
    "rasa":       ("Taste/Savour",         ["Prithvi", "Ap"], 20),
    "gandha":     ("Odour",                ["Prithvi"], 21),
    "sparsha":    ("Touch",                ["Prithvi", "Ap", "Tejas", "Vayu"], 22),
    "samkhya":    ("Number",               None, 24),
    "parimana":   ("Dimension/Magnitude",  None, 25),
    "prithaktva": ("Severalty",            None, 26),
    "samyoga":    ("Conjunction",          None, 27),
    "vibhaga":    ("Disjunction",          None, 28),
    "paratva":    ("Posteriority",         ["Prithvi", "Ap", "Tejas", "Vayu", "Manas"], 29),
    "aparatva":   ("Priority",             ["Prithvi", "Ap", "Tejas", "Vayu", "Manas"], 29),
    "gurutva":    ("Gravity/Heaviness",    ["Prithvi", "Ap"], 30),
    "dravatva":   ("Fluidity",             ["Prithvi", "Ap", "Tejas"], 31),
    "sneha":      ("Viscidity",            ["Ap"], 32),
    "shabda":     ("Sound",                ["Akasha"], 33),
    "buddhi":     ("Cognition/Intellect",  ["Atman"], 34),
    "sukha":      ("Pleasure",             ["Atman"], 66),
    "duhkha":     ("Pain",                 ["Atman"], 66),
    "iccha":      ("Desire",               ["Atman"], 66),
    "dvesha":     ("Aversion",             ["Atman"], 66),
    "prayatna":   ("Effort/Volition",      ["Atman"], 66),
    "dharma":     ("Merit",                ["Atman"], 73),
    "adharma":    ("Demerit",              ["Atman"], 73),
    "samskara":   ("Faculty (velocity / mental impression / elasticity)",
                                            ["Prithvi", "Ap", "Tejas", "Vayu", "Manas", "Atman"], 75),
}
_ALL_DRAVYA_NAMES = list(DRAVYAS.keys())
GUNAS = {
    key: Guna(key, resides_in=(info[1] if info[1] else _ALL_DRAVYA_NAMES),
              description=info[0], section=info[2])
    for key, info in GUNA_INFO.items()
}

# ---------------------------------------------------------------------
# The Five Actions (karma) -- Section 5
# ---------------------------------------------------------------------
KARMA_INFO = {
    "utkshepana":  "Tossing / throwing upwards",
    "apakshepana": "Dropping / throwing downwards",
    "akunchana":   "Contraction (pulling nearer)",
    "prasarana":   "Expansion (pushing away)",
    "gamana":      "Going / motion in general",
}
KARMAS = {
    key: Karma(key, resides_in=["Prithvi", "Ap", "Tejas", "Vayu", "Manas"],
               description=desc, section=5)
    for key, desc in KARMA_INFO.items()
}


def describe(name):
    """Look up any padartha (dravya / guna / karma) by name (case
    insensitive) and return the matching object, or None if not found."""
    if not name:
        return None
    key_cap = name.strip().capitalize()
    if key_cap in DRAVYAS:
        return DRAVYAS[key_cap]
    key_low = name.strip().lower()
    if key_low in GUNAS:
        return GUNAS[key_low]
    if key_low in KARMAS:
        return KARMAS[key_low]
    return None


def list_all():
    """Return a human-readable inventory of the whole seeded ontology."""
    lines = ["=== 9 Dravyas (Substances) ==="]
    lines += [f"  - {n}" for n in DRAVYAS]
    lines.append(f"=== {len(GUNAS)} Gunas (Qualities) ===")
    lines += [f"  - {n}" for n in GUNAS]
    lines.append(f"=== {len(KARMAS)} Karmas (Actions) ===")
    lines += [f"  - {n}" for n in KARMAS]
    return "\n".join(lines)


def all_terms():
    """All known term names across dravya/guna/karma, for cross-
    referencing against the ingested Tarkasamgraha source text."""
    return list(DRAVYAS.keys()) + list(GUNAS.keys()) + list(KARMAS.keys())
