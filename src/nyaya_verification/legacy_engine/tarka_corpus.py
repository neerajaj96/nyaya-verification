"""
tarka_corpus.py
----------------
Integrates the full English Tarkasamgraha-with-Dipika text (Athalye/
Bodas edition, Bombay Sanskrit Series No. LV, 1930) into the engine as
a searchable, ingestible corpus.

This is the concrete Shabda "Apta" source for the whole engine: rather
than only accepting a couple of manually-typed trusted sentences, the
engine can ground its ontology terms and answer free-text queries
against the real source text, with every claim traceable to a specific
passage -- exactly the "no hallucination without a citation" design
principle applied to Shabda.

Data file: data/tarkasangraha_corpus.json -- a list of cleaned,
paragraph-merged text chunks produced from the user's own uploaded
source document (see preprocess_corpus.py for the one-time build
script). No network access or paid service is required; this module
is 100% local and dependency-free.
"""
import json
import os

DEFAULT_CORPUS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data",
    "tarkasangraha_corpus.json"
)


class TarkaCorpus:
    """Loads the chunked source-text corpus and exposes it for (a)
    bulk ingestion into a RAGShabda store, and (b) direct keyword /
    similarity search for grounding/citation purposes."""

    def __init__(self, path=DEFAULT_CORPUS_PATH):
        self.path = path
        self.source_name = None
        self.chunks = []
        self._loaded = False

    def load(self):
        if self._loaded:
            return True
        if not os.path.exists(self.path):
            return False
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.source_name = data.get("source_name", "Tarkasamgraha (source text)")
        self.chunks = data.get("chunks", [])
        self._loaded = True
        return True

    def __len__(self):
        return len(self.chunks)

    def ingest_into(self, rag_shabda, limit=None):
        """Bulk-load every chunk into a RAGShabda's trusted-document
        store, tagged with the real bibliographic source name."""
        if not self._loaded and not self.load():
            return 0
        chunks = self.chunks if limit is None else self.chunks[:limit]
        return rag_shabda.ingest_bulk(chunks, source_name=self.source_name)

    def keyword_search(self, term, max_hits=5):
        """Cheap, dependency-free substring search over the raw
        corpus -- useful for a quick 'does the source text mention
        this term at all' check, independent of the embedding index."""
        if not self._loaded and not self.load():
            return []
        term_low = term.lower()
        hits = []
        for chunk in self.chunks:
            if term_low in chunk.lower():
                hits.append(chunk)
                if len(hits) >= max_hits:
                    break
        return hits
