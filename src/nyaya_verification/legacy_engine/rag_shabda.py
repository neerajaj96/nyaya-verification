"""
rag_shabda.py
-------------
Retrieval-Augmented Generation (RAG) support for Shabda (Sec. 59):
verbal testimony is only valid pramana when it comes from an Apta
(a credible / trustworthy source). Here, "credible" is operationalised
as: "found in a trusted, ingested document."

Design (mirrors the neuro-symbolic specification):
  1. Trusted documents (e.g. textbook passages, manuals, scripture)
     are ingested into an in-memory vector store.
  2. When the engine needs a fact it doesn't already know, it queries
     the store. If a sufficiently similar passage is found, the fact
     is asserted via Shabda (tagged with the source document).
  3. If nothing sufficiently similar is found, the fact is REJECTED
     with the reason "Not from an Apta" -- this is exactly how the
     system prevents an untrusted / hallucinated claim from entering
     the knowledge base.
"""
from embeddings import EmbeddingIndex


class Document:
    _counter = 0

    def __init__(self, text, source, section=None):
        Document._counter += 1
        self.doc_id = f"doc{Document._counter}"
        self.text = text
        self.source = source
        self.section = section

    def __repr__(self):
        return f"<Document {self.doc_id} from '{self.source}'>"

    def excerpt(self, max_chars=160):
        t = " ".join(self.text.split())
        return t if len(t) <= max_chars else t[:max_chars].rstrip() + "..."


class VectorStore:
    """A minimal in-memory 'vector database' (stand-in for ChromaDB /
    FAISS) built on the pure-python embeddings module."""

    def __init__(self):
        self._index = EmbeddingIndex()
        self._docs = {}

    def add_document(self, text, source, section=None):
        doc = Document(text, source, section)
        self._docs[doc.doc_id] = doc
        self._index.add(doc.doc_id, text)
        return doc

    def retrieve(self, query, top_k=3):
        hits = self._index.most_similar(query, top_k=top_k)
        return [(self._docs[doc_id], score) for doc_id, score, _desc in hits]

    def __len__(self):
        return len(self._docs)

    def sources(self):
        return sorted({d.source for d in self._docs.values()})


class RAGShabda:
    """Combines a VectorStore of trusted documents with the Shabda
    pramana. Facts are only accepted if backed by a retrieved trusted
    passage above threshold similarity."""

    def __init__(self, threshold=0.22):
        self.store = VectorStore()
        self.threshold = threshold

    def ingest(self, text, source_name, section=None):
        """Load a trusted document (e.g. a textbook paragraph) into the
        vector database."""
        doc = self.store.add_document(text, source_name, section)
        return (f"[RAG] Ingested passage from apta source '{source_name}' "
                f"({doc.doc_id}).")

    def ingest_bulk(self, chunks, source_name):
        """Ingest many (text[, section]) chunks in one call. Each chunk
        may be a plain string or a (text, section) tuple."""
        count = 0
        for chunk in chunks:
            if isinstance(chunk, (tuple, list)):
                text, section = chunk[0], (chunk[1] if len(chunk) > 1 else None)
            else:
                text, section = chunk, None
            if text and text.strip():
                self.store.add_document(text, source_name, section)
                count += 1
        return count

    def query_and_assert(self, world, locus, prop, query_text, value=True,
                          threshold=None):
        """Retrieve the most relevant trusted passage for query_text;
        if similar enough, assert (locus, prop, value) via Shabda,
        tagging provenance. Otherwise reject the claim."""
        threshold = self.threshold if threshold is None else threshold
        if len(self.store) == 0:
            return {"accepted": False,
                     "message": "[RAG->Shabda] No trusted documents have "
                                "been ingested. REJECTED: Not from an Apta."}
        hits = self.store.retrieve(query_text, top_k=1)
        if not hits or hits[0][1] < threshold:
            best = f"{hits[0][1]:.3f}" if hits else "n/a"
            return {"accepted": False,
                     "message": f"[RAG->Shabda] No trusted passage is "
                                f"similar enough to '{query_text}' "
                                f"(best similarity={best} < {threshold}). "
                                f"REJECTED: Not from an Apta."}
        doc, score = hits[0]
        world.set_fact(locus, prop, value, source="shabda")
        return {"accepted": True, "score": score, "doc": doc,
                 "message": f"[RAG->Shabda] Accepted: '{locus}' has "
                            f"'{prop}'={value}, backed by apta source "
                            f"'{doc.source}' (similarity={score:.3f}). "
                            f"Excerpt: \"{doc.excerpt()}\""}

    def query_passages(self, query_text, top_k=3, threshold=None):
        """Non-asserting retrieval: just return the top matching
        trusted passages for a query, for inspection/citation
        purposes (does not touch the WorldModel)."""
        threshold = self.threshold if threshold is None else threshold
        hits = self.store.retrieve(query_text, top_k=top_k)
        return [(doc, score) for doc, score in hits if score >= threshold]
