"""
embeddings.py
-------------
Lightweight vector embeddings used to implement Upamana (Comparison,
Sec. 58) and to back the RAG-based Shabda pipeline (rag_shabda.py).

By default this module uses a dependency-free bag-of-words vectoriser
plus cosine similarity (pure Python, always available, zero install
risk). If the optional sentence-transformers package happens to be
installed, a much stronger dense-embedding backend is used automatically
instead. The import is guarded, so the whole engine works perfectly
even with zero extra packages installed.
"""
import re
import math
from collections import Counter

_TOKEN_RE = re.compile(r"[a-zA-Z']+")
_STOPWORDS = {
    "a", "an", "the", "is", "are", "of", "to", "and", "or", "with",
    "it", "its", "in", "on", "that", "this", "as", "was", "were",
    "be", "has", "have", "had", "for", "by", "at",
}


def tokenize(text):
    tokens = [t.lower() for t in _TOKEN_RE.findall(text or "")]
    return [t for t in tokens if t not in _STOPWORDS and len(t) > 1]


def vectorize(text):
    """Return a sparse bag-of-words vector as a dict {token: count}."""
    return dict(Counter(tokenize(text)))


def cosine_similarity(vec1, vec2):
    """Cosine similarity between two sparse dict-vectors (pure python
    fallback path)."""
    if not vec1 or not vec2:
        return 0.0
    common = set(vec1) & set(vec2)
    dot = sum(vec1[k] * vec2[k] for k in common)
    mag1 = math.sqrt(sum(v * v for v in vec1.values()))
    mag2 = math.sqrt(sum(v * v for v in vec2.values()))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)


# ---------------------------------------------------------------------
# Optional, dependency-gated upgrade. Guarded so the module works with
# zero installed dependencies.
# ---------------------------------------------------------------------
_ST_AVAILABLE = False
try:                                          # pragma: no cover
    from sentence_transformers import SentenceTransformer, util as _st_util
    _ST_AVAILABLE = True
except Exception:
    _ST_AVAILABLE = False

_ST_MODEL = None


def _get_st_model():
    global _ST_MODEL
    if _ST_MODEL is None and _ST_AVAILABLE:
        _ST_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    return _ST_MODEL


class Embedder:
    """Encodes text into a vector and compares vectors. Automatically
    uses sentence-transformers if available, otherwise falls back to
    the built-in bag-of-words cosine model."""

    def __init__(self, prefer_dense=True):
        self.use_dense = bool(prefer_dense and _ST_AVAILABLE)
        self.model = _get_st_model() if self.use_dense else None

    def encode(self, text):
        if self.use_dense:
            return self.model.encode(text, convert_to_tensor=True)
        return vectorize(text)

    def similarity(self, vec1, vec2):
        if self.use_dense:
            return float(_st_util.cos_sim(vec1, vec2))
        return cosine_similarity(vec1, vec2)

    def backend_name(self):
        return ("sentence-transformers(all-MiniLM-L6-v2)" if self.use_dense
                else "bag-of-words-cosine (pure-python fallback)")


class EmbeddingIndex:
    """A small in-memory index over (name -> description) pairs,
    supporting nearest-neighbour ('most similar') lookup."""

    def __init__(self, embedder=None):
        self.embedder = embedder or Embedder()
        self._items = {}  # name -> (description, vector)

    def add(self, name, description):
        vec = self.embedder.encode(description)
        self._items[name] = (description, vec)

    def __len__(self):
        return len(self._items)

    def most_similar(self, query_text, top_k=3):
        qvec = self.embedder.encode(query_text)
        scored = []
        for name, (desc, vec) in self._items.items():
            score = self.embedder.similarity(qvec, vec)
            scored.append((name, score, desc))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]
