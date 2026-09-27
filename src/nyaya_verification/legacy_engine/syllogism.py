"""
syllogism.py
-------------
Generates:
  * Svartha-anumana -- the private, three-step reasoning process
    ("inference for oneself"), Section 45.
  * Parartha-anumana -- the public, five-membered syllogism
    (Pancavayava), Section 46:
        1. Pratijna  (Proposition)
        2. Hetu      (Reason)
        3. Udaharana (Example / Vyapti)
        4. Upanaya   (Application)
        5. Nigamana  (Conclusion)
"""


class Syllogism:
    def __init__(self, paksha, hetu, sadhya, sapaksha_example):
        self.paksha = paksha
        self.hetu = hetu
        self.sadhya = sadhya
        self.sapaksha_example = sapaksha_example or "a known similar instance"

    def svartha_anumana(self):
        return "\n".join([
            f"1. Vyapti-smarana (recollection): 'Wherever there is "
            f"{self.hetu}, there is {self.sadhya}' (as in "
            f"{self.sapaksha_example}).",
            f"2. Paramarsha (consideration): '{self.paksha} has "
            f"{self.hetu}, which is invariably accompanied by "
            f"{self.sadhya}.'",
            f"3. Anumiti (resulting judgment): '{self.paksha} has "
            f"{self.sadhya}.'",
        ])

    def parartha_anumana(self):
        members = [
            ("1. Pratijna  (Proposition)",
             f"{self.paksha} has {self.sadhya}."),
            ("2. Hetu      (Reason)     ",
             f"Because it has {self.hetu}."),
            ("3. Udaharana (Example)    ",
             f"Whatever has {self.hetu} has {self.sadhya}, as in "
             f"{self.sapaksha_example}."),
            ("4. Upanaya   (Application)",
             f"{self.paksha} has {self.hetu}, which is pervaded by "
             f"{self.sadhya}."),
            ("5. Nigamana  (Conclusion) ",
             f"Therefore, {self.paksha} has {self.sadhya}."),
        ]
        return "\n".join(f"{label}: {text}" for label, text in members)

    def as_dict(self):
        return {
            "paksha": self.paksha, "hetu": self.hetu,
            "sadhya": self.sadhya,
            "sapaksha_example": self.sapaksha_example,
        }

    def __repr__(self):
        return (f"Syllogism({self.paksha} has {self.sadhya} "
                f"because {self.hetu})")
