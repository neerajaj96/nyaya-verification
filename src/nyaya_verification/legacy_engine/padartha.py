"""
padartha.py
-----------
Core ontology of the Nyaya-Vaisheshika "seven categories" (sapta-padarthah)
as enumerated in Annambhatta's Tarkasamgraha, Section 2:

    Dravya (Substance), Guna (Quality), Karma (Action),
    Samanya (Generality), Vishesha (Particularity),
    Samavaya (Inherence), Abhava (Negation)

Grounding: every class below carries a `section` reference to the
Tarkasamgraha section that defines it, and can be cross-referenced
against the ingested source text via TarkaEngine.ground_term().
"""
from enum import Enum


class Category(Enum):
    DRAVYA = "Dravya (Substance)"
    GUNA = "Guna (Quality)"
    KARMA = "Karma (Action)"
    SAMANYA = "Samanya (Generality)"
    VISHESHA = "Vishesha (Particularity)"
    SAMAVAYA = "Samavaya (Inherence)"
    ABHAVA = "Abhava (Negation)"


class Padartha:
    """Base class: anything nameable / knowable (abhidheyatva)."""

    def __init__(self, name, category, description="", section=None):
        self.name = name
        self.category = category
        self.description = description
        self.section = section  # Tarkasamgraha section number, if known

    def info(self):
        sec = f" [Sec. {self.section}]" if self.section else ""
        return f"{self.name} :: {self.category.value}{sec}\n  {self.description}"

    def __repr__(self):
        return f"<{self.category.value}: {self.name}>"


class Dravya(Padartha):
    """A substance -- substratum in which qualities/actions inhere
    (Section 3)."""

    def __init__(self, name, eternal=False, qualities=None, description="",
                 section=3):
        super().__init__(name, Category.DRAVYA, description, section)
        self.eternal = eternal
        self.qualities = list(qualities) if qualities else []

    def add_quality(self, guna_name):
        if guna_name not in self.qualities:
            self.qualities.append(guna_name)

    def info(self):
        base = super().info()
        eternity = "Nitya (eternal)" if self.eternal else "Anitya (non-eternal)"
        quals = ", ".join(self.qualities) if self.qualities else "None listed"
        return f"{base}\n  Eternality: {eternity}\n  Qualities: {quals}"


class Guna(Padartha):
    """A quality inhering in one or more substances (Section 4)."""

    def __init__(self, name, resides_in=None, description="", section=4):
        super().__init__(name, Category.GUNA, description, section)
        self.resides_in = list(resides_in) if resides_in else []

    def info(self):
        base = super().info()
        hosts = ", ".join(self.resides_in) if self.resides_in else "none"
        return f"{base}\n  Resides in: {hosts}"


class Karma(Padartha):
    """Action / motion (Section 5)."""

    def __init__(self, name, resides_in=None, description="", section=5):
        super().__init__(name, Category.KARMA, description, section)
        self.resides_in = list(resides_in) if resides_in else []

    def info(self):
        base = super().info()
        hosts = ", ".join(self.resides_in) if self.resides_in else "none"
        return f"{base}\n  Resides in: {hosts}"


class Samanya(Padartha):
    """Universal / genus, e.g. ghatatva -- Section 6."""

    def __init__(self, name, extent="apara", description="", section=6):
        super().__init__(name, Category.SAMANYA, description, section)
        self.extent = extent  # 'para' (wider, e.g. satta) or 'apara'

    def info(self):
        base = super().info()
        return f"{base}\n  Extent: {self.extent}"


class Vishesha(Padartha):
    """Ultimate particularity distinguishing eternal substances --
    Section 7."""

    def __init__(self, name, description="", section=7):
        super().__init__(name, Category.VISHESHA, description, section)


class Samavaya(Padartha):
    """The single, eternal relation of inherence -- Section 8."""

    def __init__(self, description="The one, eternal relation of inherence "
                                     "(e.g. between a cloth and its threads).",
                 section=8):
        super().__init__("Samavaya", Category.SAMAVAYA, description, section)


class AbhavaType(Enum):
    PRAGABHAVA = "Pragabhava (antecedent negation)"
    PRADHVAMSA = "Pradhvamsabhava (consequent negation / destruction)"
    ATYANTABHAVA = "Atyantabhava (absolute negation)"
    ANYONYABHAVA = "Anyonyabhava (mutual/reciprocal negation)"


class Abhava(Padartha):
    """Negation -- the four kinds described in Section 9 / defined in
    Section 80."""

    def __init__(self, pratiyogi, anuyogi=None,
                 abhava_type=AbhavaType.ATYANTABHAVA, description="",
                 section=9):
        name = f"{abhava_type.name}({pratiyogi})"
        super().__init__(name, Category.ABHAVA, description, section)
        self.pratiyogi = pratiyogi   # the counter-entity being negated
        self.anuyogi = anuyogi       # the locus on which the negation rests
        self.abhava_type = abhava_type

    def info(self):
        base = super().info()
        return (f"{base}\n  Pratiyogi (negated entity): {self.pratiyogi}"
                f"\n  Anuyogi (locus): {self.anuyogi or 'unspecified'}"
                f"\n  Type: {self.abhava_type.value}")
