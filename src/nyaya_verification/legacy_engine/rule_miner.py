"""
rule_miner.py
-------------
Unsupervised association-rule mining (a from-scratch Apriori algorithm)
used to discover new Vyaptis (universal concomitances) from repeated
observation (bhuyodarshana) -- the classical method (Section 44/45) by
which a Vyapti such as "wherever smoke, fire" is first learned, e.g.
from many observations of kitchens.

This is a pure-Python implementation (no external ML dependencies) so
the whole engine remains dependency-free and 100% reproducible.
"""
from itertools import combinations


def _support(itemset, transactions):
    itemset = frozenset(itemset)
    if not transactions:
        return 0.0
    count = sum(1 for t in transactions if itemset.issubset(t))
    return count / len(transactions)


def apriori(transactions, min_support=0.5, max_itemset_size=3):
    """
    transactions: list of iterables, each a set of 'items' (boolean
                  attributes) true for that record, e.g.
                  [{"heavy_clouds", "high_humidity", "rain"}, ...]
    Returns: dict {frozenset(items): support}
    """
    transactions = [frozenset(t) for t in transactions]
    if not transactions:
        return {}
    items = set()
    for t in transactions:
        items.update(t)

    frequent = {}
    current_level = []
    for item in items:
        fs = frozenset([item])
        sup = _support(fs, transactions)
        if sup >= min_support:
            frequent[fs] = sup
            current_level.append(fs)

    k = 2
    while current_level and k <= max_itemset_size:
        candidates = set()
        for a, b in combinations(current_level, 2):
            union = a | b
            if len(union) == k:
                candidates.add(union)
        next_level = []
        for cand in candidates:
            sup = _support(cand, transactions)
            if sup >= min_support:
                frequent[cand] = sup
                next_level.append(cand)
        current_level = next_level
        k += 1
    return frequent


def generate_rules(frequent_itemsets, transactions, min_confidence=0.8):
    """
    Generates rules antecedent -> consequent (disjoint frozensets whose
    union is a frequent itemset), with:
        confidence(A -> B) = support(A union B) / support(A)
    Returns a list of dicts: {antecedent, consequent, support, confidence}
    """
    transactions = [frozenset(t) for t in transactions]
    rules = []
    for itemset, itemset_support in frequent_itemsets.items():
        if len(itemset) < 2:
            continue
        items = list(itemset)
        for r in range(1, len(items)):
            for antecedent_tuple in combinations(items, r):
                antecedent = frozenset(antecedent_tuple)
                consequent = itemset - antecedent
                if not consequent:
                    continue
                ant_support = _support(antecedent, transactions)
                if ant_support == 0:
                    continue
                confidence = itemset_support / ant_support
                if confidence >= min_confidence:
                    rules.append({
                        "antecedent": antecedent,
                        "consequent": consequent,
                        "support": itemset_support,
                        "confidence": confidence,
                    })
    rules.sort(key=lambda r: (-r["confidence"], -r["support"]))
    return rules


def make_sample_lookup(transactions, labels=None):
    """Utility: build a callable that, given a set of items, returns a
    human-readable label for the first transaction containing all of
    them (for use as a Vyapti's sapaksha)."""
    transactions = [frozenset(t) for t in transactions]
    labels = labels or [f"record #{i + 1}" for i in range(len(transactions))]

    def lookup(item_set):
        for t, label in zip(transactions, labels):
            if item_set.issubset(t):
                return label
        return None
    return lookup


class VyaptiMiner:
    """High-level wrapper: mine transactions for candidate Vyaptis and
    (optionally) automatically teach them to a TarkaEngine."""

    def __init__(self, min_support=0.3, min_confidence=0.85):
        self.min_support = min_support
        self.min_confidence = min_confidence

    def mine(self, transactions, min_support=None, min_confidence=None):
        min_support = self.min_support if min_support is None else min_support
        min_confidence = (self.min_confidence if min_confidence is None
                           else min_confidence)
        frequent = apriori(transactions, min_support=min_support)
        rules = generate_rules(frequent, transactions,
                                min_confidence=min_confidence)
        return rules

    def teach_engine(self, engine, rules, sample_id_lookup=None,
                      verbose=True):
        """Teach single-hetu -> single-sadhya rules (the shape a Nyaya
        Vyapti needs) to the given TarkaEngine. Multi-antecedent /
        multi-consequent rules are reported but not auto-taught, since
        a Vyapti in this engine is strictly binary (one hetu, one
        sadhya)."""
        taught = []
        for rule in rules:
            ant, cons = rule["antecedent"], rule["consequent"]
            if len(ant) == 1 and len(cons) == 1:
                hetu = next(iter(ant))
                sadhya = next(iter(cons))
                sapaksha = (sample_id_lookup(ant | cons)
                            if sample_id_lookup else None)
                engine.teach_vyapti(hetu, sadhya, sapaksha=sapaksha)
                taught.append((hetu, sadhya))
                if verbose:
                    print(f"[Vyapti-Miner] Taught new Vyapti: "
                          f"'{hetu}' -> '{sadhya}' "
                          f"(support={rule['support']:.2f}, "
                          f"confidence={rule['confidence']:.2f}, "
                          f"sapaksha={sapaksha}).")
            elif verbose:
                print(f"[Vyapti-Miner] Skipped multi-term rule "
                      f"{set(ant)} -> {set(cons)} (not a binary Vyapti "
                      f"shape).")
        return taught
