"""
preprocess_corpus.py
---------------------
One-time build script: converts the raw uploaded Tarkasamgraha-with-
Dipika English text into a cleaned, paragraph-merged JSON corpus
(data/tarkasangraha_corpus.json) for tarka_corpus.py to load.

Re-run this if you replace the source text with a cleaner OCR pass or
a different edition. 100% pure Python, no dependencies.

Usage:
    python preprocess_corpus.py /path/to/source.txt
"""
import re
import json
import sys
import os

DEFAULT_SRC = "/mnt/user-data/uploads/Tarkasangraha_with_dipika_english.txt"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data",
                    "tarkasangraha_corpus.json")
SOURCE_NAME = ("Tarkasamgraha with the author's own Dipika and "
               "Govardhana's Nyaya-Bodhini (ed. Athalye, trans. Bodas, "
               "Bombay Sanskrit Series No. LV, 1930)")


def is_useful(chunk):
    letters = sum(ch.isalpha() for ch in chunk)
    return len(chunk) >= 40 and letters / max(len(chunk), 1) > 0.5


def build_corpus(src_path, out_path=OUT, source_name=SOURCE_NAME,
                  target_chunk_len=900):
    with open(src_path, "r", encoding="utf-8", errors="replace") as f:
        raw = f.read()
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    lines = raw.split("\n")

    paragraphs = []
    buf = []
    for ln in lines:
        if ln.strip() == "":
            if buf:
                paragraphs.append(" ".join(buf).strip())
                buf = []
        else:
            buf.append(ln.strip())
    if buf:
        paragraphs.append(" ".join(buf).strip())

    chunks = []
    cur = ""
    for p in paragraphs:
        p = re.sub(r"\s+", " ", p).strip()
        if not p:
            continue
        if len(cur) + len(p) + 1 <= target_chunk_len:
            cur = (cur + " " + p).strip()
        else:
            if cur:
                chunks.append(cur)
            if len(p) > target_chunk_len:
                sentences = re.split(r"(?<=[.;])\s+", p)
                sub = ""
                for s in sentences:
                    if len(sub) + len(s) + 1 <= target_chunk_len:
                        sub = (sub + " " + s).strip()
                    else:
                        if sub:
                            chunks.append(sub)
                        sub = s
                cur = sub
            else:
                cur = p
    if cur:
        chunks.append(cur)

    chunks = [c for c in chunks if is_useful(c)]

    data = {"source_name": source_name, "chunk_count": len(chunks),
            "chunks": chunks}
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    return len(chunks)


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC
    n = build_corpus(src)
    print(f"Wrote {OUT} ({n} chunks) from source: {src}")
