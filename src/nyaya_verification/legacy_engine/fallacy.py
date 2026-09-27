"""
fallacy.py
----------
Implements the five Hetvabhasas (fallacious reasons) of Tarkasamgraha
Sections 52-57, run as a 9-point diagnostic gauntlet, in the order a
Naiyayika would naturally test them:

    1. Ashrayasiddha    (Asiddha subtype, Sec. 56) -- paksha is unreal.
    2. Svarupasiddha    (Asiddha subtype, Sec. 56) -- hetu absent/unverified.
    3. Badhita          (Sec. 57) -- negation of sadhya already proven
                                     by an equal-or-stronger pramana.
    4. Viruddha         (Sec. 54) -- hetu is pervaded by NOT-sadhya.
    5. Satpratipaksha   (Sec. 55) -- an equally strong opposing hetu
                                     proves NOT-sadhya.
    6. Vyapti-asiddha                -- no concomitance on record at all.
    7. Sadharana        (Savyabhichara subtype, Sec. 53) -- over-wide.
    8. Asadharana       (Savyabhichara subtype, Sec. 53) -- over-narrow.
    9. Vyapyatvasiddha  (Asiddha subtype, Sec. 56) -- hidden condition
                                     (upadhi) makes the concomitance
                                     merely conditional.

If none of these defects is found, the hetu is a "sad-hetu" (sound
reason) and diagnose() returns None.
"""

# Rough authority ordering of the pramanas, used to decide whether a
# contrary fact recorded elsewhere is strong enough to make the
# current inference "badhita" (contradicted).
PRAMANA_STRENGTH = {
    "pratyaksha": 4,   # perception -- strongest
    "shabda": 3,       # verbal testimony / scripture
    "upamana": 2,       # analogy
    "anumana": 1,       # inference
    "assumed": 0,       # a bare stipulated fact
}


class FallacyReport:
    """Represents a detected Hetvabhasa (fallacious reason)."""

    def __init__(self, name, detail):
        self.name = name
        self.detail = detail

    def __repr__(self):
        return f"[HETVABHASA: {self.name}]\n  {self.detail}"

    def __str__(self):
        return self.__repr__()

    def __bool__(self):
        return True  # a FallacyReport always signals "a defect exists"


def diagnose(paksha, hetu, sadhya, vyapti_db, world):
    """
    Check whether "<paksha> has <sadhya>, because it has <hetu>" is
    sound, given the current VyaptiDatabase and WorldModel.

    Returns a FallacyReport if a defect is found, else None (meaning
    the hetu is a sad-hetu / valid reason).
    """
    # ---- 1. Ashrayasiddha: the paksha itself is unreal ------------------
    if not world.locus_exists(paksha):
        return FallacyReport(
            "Ashrayasiddha (unreal locus)",
            f"The paksha '{paksha}' does not exist at all -- like a "
            f"sky-lotus (gagana-aravinda). The inference has no real "
            f"substratum to rest on."
        )

    # ---- 2. Svarupasiddha: the hetu does not reside in the paksha -------
    hetu_present = world.has_property(paksha, hetu)
    if hetu_present is False:
        return FallacyReport(
            "Svarupasiddha (non-existent reason)",
            f"The hetu '{hetu}' is not actually present in '{paksha}' "
            f"(e.g. 'Sound is a quality because it is visible' -- Sound "
            f"is not in fact visible)."
        )
    if hetu_present is None:
        return FallacyReport(
            "Svarupasiddha (unverified reason)",
            f"It has not been established that '{paksha}' possesses "
            f"'{hetu}'; the reason's presence on the paksha is unknown."
        )

    # ---- 3. Badhita: negation of sadhya already proven more strongly ----
    neg_key = f"not-{sadhya}"
    neg_val = world.has_property(paksha, neg_key)
    if neg_val is True:
        src = world.source_of(paksha, neg_key)
        if PRAMANA_STRENGTH.get(src, 0) >= PRAMANA_STRENGTH["anumana"]:
            return FallacyReport(
                "Badhita (contradicted / futile reason)",
                f"The negation of '{sadhya}' on '{paksha}' is already "
                f"established by {src}, at least as strong as inference "
                f"-- e.g. 'Fire is cold, because it is a substance' is "
                f"contradicted by the tactile perception (pratyaksha) of "
                f"its heat."
            )

    # ---- 4. Viruddha: the hetu is pervaded by NOT-sadhya, not sadhya ----
    contrary_vyapti = vyapti_db.get(hetu, neg_key)
    if contrary_vyapti is not None and contrary_vyapti.is_valid():
        return FallacyReport(
            "Viruddha (contrary reason)",
            f"'{hetu}' is invariably concomitant with the negation of "
            f"'{sadhya}', not with '{sadhya}' itself -- e.g. 'Sound is "
            f"eternal, because it is artificial (krtakatva)': "
            f"artificiality actually proves non-eternity."
        )

    # ---- 5. Satpratipaksha: an equally valid opposing hetu exists -------
    for (h2, s2), v2 in vyapti_db.items():
        if s2 == neg_key and h2 != hetu and v2.is_valid():
            if world.has_property(paksha, h2):
                return FallacyReport(
                    "Satpratipaksha (counterbalanced reason)",
                    f"An equally valid, opposing hetu '{h2}' proves "
                    f"'not-{sadhya}' on the very same paksha -- e.g. "
                    f"'Sound is eternal, because it is audible "
                    f"(shravanatva)' is exactly counterbalanced by "
                    f"'Sound is non-eternal, because it is artificial "
                    f"(karyatva)'."
                )

    # ---- 6. Retrieve the primary vyapti ----------------------------------
    vyapti = vyapti_db.get(hetu, sadhya)
    if vyapti is None:
        return FallacyReport(
            "Vyapti-asiddha (no concomitance on record)",
            f"No invariable concomitance (vyapti) between '{hetu}' and "
            f"'{sadhya}' has been taught to the engine; the inference "
            f"cannot proceed (this is exactly how the engine refuses to "
            f"'hallucinate' a rule it was never given)."
        )

    # ---- 7. Savyabhichara - Sadharana (over-wide reason) ----------------
    if not vyapti.is_valid():
        return FallacyReport(
            "Savyabhichara - Sadharana (over-wide / common reason)",
            f"'{hetu}' occurs both where '{sadhya}' is present "
            f"(sapaksha: {vyapti.sapaksha}) and where '{sadhya}' is "
            f"absent (counter-instance: {vyapti.counterexamples[0]}); "
            f"the concomitance is broken (vyabhicara), e.g. 'The "
            f"mountain is fiery, because it is knowable (prameyatva)' "
            f"-- knowability is also found on a lake, which has no fire."
        )

    # ---- 8. Savyabhichara - Asadharana (over-narrow / peculiar reason) --
    if vyapti.sapaksha is None:
        return FallacyReport(
            "Savyabhichara - Asadharana (over-narrow / peculiar reason)",
            f"'{hetu}' is found nowhere else but in '{paksha}' -- there "
            f"is no supporting instance (sapaksha) anywhere, e.g. "
            f"'Sound is eternal, because it has the nature of sound "
            f"(shabdatva)'."
        )

    # ---- 9. Vyapyatvasiddha: hidden condition (upadhi) ------------------
    if vyapti.upadhi:
        return FallacyReport(
            "Vyapyatvasiddha (conditional reason / upadhi present)",
            f"The concomitance between '{hetu}' and '{sadhya}' holds "
            f"only conditionally, given the hidden condition "
            f"'{vyapti.upadhi}' -- e.g. 'The mountain is smoky, because "
            f"it has fire' holds only given contact with wet fuel "
            f"(ardra-indhana-samyoga); fire alone (e.g. a red-hot iron "
            f"ball) need not produce smoke."
        )

    return None
