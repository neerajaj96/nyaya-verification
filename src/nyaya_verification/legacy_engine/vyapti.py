"""
vyapti.py
---------
Vyapti = invariable concomitance between a Hetu (reason / middle term)
and a Sadhya (thing to be proved), as defined in Tarkasamgraha Section 44:

    "yatra yatra dhumah tatra tatra vahnih"
    (Wherever there is smoke, there is fire.)

This is the "major premise" / general rule of Nyaya reasoning.
"""


class Vyapti:
    def __init__(self, hetu, sadhya, sapaksha=None, vipaksha=None,
                 kind="anvaya", upadhi=None):
        """
        hetu      : the reason / middle term, e.g. 'smoke'
        sadhya    : the thing to be proved, e.g. 'fire'
        sapaksha  : a known instance where hetu & sadhya co-exist
                    (e.g. 'a kitchen')
        vipaksha  : a known instance where both are absent (e.g. 'a lake')
        kind      : 'anvaya' (positive concomitance), 'vyatireka'
                    (negative concomitance), or 'both'
        upadhi    : an optional hidden condition (Section 56) on which
                    the concomitance actually depends -- if set, the
                    reason is only conditionally valid
                    (vyapyatvasiddha).
        """
        self.hetu = hetu
        self.sadhya = sadhya
        self.sapaksha = sapaksha
        self.vipaksha = vipaksha
        self.kind = kind
        self.upadhi = upadhi
        # instances registered as breaking the concomitance (hetu
        # present, sadhya absent) -- makes the hetu "vyabhicarin".
        self.counterexamples = []

    def add_counterexample(self, instance):
        if instance not in self.counterexamples:
            self.counterexamples.append(instance)

    def is_valid(self):
        """A vyapti is broken (vyabhicara) if any counterexample
        exists."""
        return len(self.counterexamples) == 0

    def __repr__(self):
        status = "valid" if self.is_valid() else "BROKEN (vyabhicara)"
        return f"Vyapti({self.hetu} -> {self.sadhya}, {status})"


class VyaptiDatabase:
    """A store of known Vyaptis, keyed by (hetu, sadhya)."""

    def __init__(self):
        self._store = {}

    def add(self, hetu, sadhya, sapaksha=None, vipaksha=None,
            kind="anvaya", upadhi=None):
        key = (hetu, sadhya)
        v = Vyapti(hetu, sadhya, sapaksha, vipaksha, kind, upadhi)
        self._store[key] = v
        return v

    def get(self, hetu, sadhya=None):
        """If sadhya given, return the exact Vyapti (or None); else
        return the list of all Vyaptis with this hetu."""
        if sadhya is not None:
            return self._store.get((hetu, sadhya))
        return [v for (h, _s), v in self._store.items() if h == hetu]

    def items(self):
        return list(self._store.items())

    def all(self):
        return list(self._store.values())

    def __len__(self):
        return len(self._store)
