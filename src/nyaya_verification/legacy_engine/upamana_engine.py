"""
upamana_engine.py
------------------
Similarity-based Upamana (Comparison, Sec. 58) using vector embeddings.

Classical example: someone learns what a 'gavaya' (gayal / wild ox) is
by being told it resembles a cow, and then perceives that resemblance
in the forest. Here this is generalised: given a bank of KNOWN
reference objects (each with a short description), an UNKNOWN object's
description is embedded and compared (cosine similarity) against every
known reference. If the best match clears a similarity threshold,
Upamana fires and the unknown object is classified/named after the
reference. If not, the engine explicitly refuses to guess.
"""
from embeddings import EmbeddingIndex


class UpamanaEngine:
    def __init__(self, threshold=0.25):
        self.index = EmbeddingIndex()
        self.threshold = threshold

    def learn_reference(self, name, description):
        """Teach a known reference object, e.g.
        learn_reference("Cow", "a domestic bovine animal with horns, "
                                "four legs, a tail, and gives milk")."""
        self.index.add(name, description)

    def known_references(self):
        return list(self.index._items.keys())

    def classify_by_similarity(self, world, target_name, description,
                                resulting_name=None, threshold=None):
        """Attempt Upamana: compare description of target_name
        against all learnt references. If the top match clears the
        threshold, assert the classification into the WorldModel via
        Upamana; otherwise report failure (no guessing)."""
        threshold = self.threshold if threshold is None else threshold
        if len(self.index) == 0:
            return {"success": False,
                     "message": "[Upamana] No reference objects known yet; "
                                "cannot compare by similarity. Use "
                                "learn_reference_object() first."}
        matches = self.index.most_similar(description, top_k=3)
        best_name, best_score, _best_desc = matches[0]
        if best_score < threshold:
            return {"success": False,
                     "message": (f"[Upamana] Best match '{best_name}' "
                                 f"scored only {best_score:.3f} "
                                 f"(< threshold {threshold}); refusing to "
                                 f"classify '{target_name}' by analogy "
                                 f"(no hallucinated guess)."),
                     "candidates": matches}
        label = resulting_name or best_name
        world.set_fact(target_name, f"resembles:{best_name}", True,
                        source="upamana")
        world.set_fact(target_name, f"named:{label}", True, source="upamana")
        return {"success": True,
                 "message": (f"[Upamana] '{target_name}' resembles "
                             f"'{best_name}' (similarity={best_score:.3f}); "
                             f"classified as '{label}'."),
                 "candidates": matches, "resulting_name": label}
