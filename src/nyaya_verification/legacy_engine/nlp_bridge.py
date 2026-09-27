"""
nlp_bridge.py
-------------
Natural-Language -> Logic bridge for Anumana (Sections 44-46).

This plays the role the neuro-symbolic design assigns to an LLM: take
a messy natural-language argument and extract the three terms of a
Nyaya inference:

    paksha  (subject / locus)
    hetu    (reason / middle term)
    sadhya  (the thing to be proved)

DESIGN PRINCIPLE ("no hallucination"): this module ONLY translates. It
never invents a Vyapti and never decides whether an argument is
logically valid -- that job belongs exclusively to fallacy.py /
engine.py. If the parser cannot confidently extract all three terms it
reports success=False rather than guessing, and it NEVER raises an
exception out of parse().

Two backends are supported:
  * RuleBasedParser (default) -- zero dependencies, deterministic,
    regex + synonym table.
  * A pluggable llm_backend callable -- e.g. a wrapper around a real
    LLM API call -- can be registered with
    NyayaNLParser.set_llm_backend(fn). If registered, it is tried
    first; the rule-based parser is always kept as an offline fallback.
"""
import re

# ---------------------------------------------------------------------
# Synonym normalisation: colourful natural-language phrases -> the
# canonical vocabulary used elsewhere in the engine.
# ---------------------------------------------------------------------
SYNONYMS = {
    "billowing smoke": "smoke", "thick smoke": "smoke", "black smoke": "smoke",
    "smoke": "smoke", "smoking": "smoke", "smoky": "smoke", "smokey": "smoke",
    "fire": "fire", "burning": "fire", "aflame": "fire", "ablaze": "fire",
    "on fire": "fire", "flames": "fire", "flame": "fire",
    "wet": "wetness", "wetness": "wetness", "damp": "wetness", "soaked": "wetness",
    "rain": "rain", "raining": "rain", "rained": "rain",
    "clouds": "clouds", "cloudy": "clouds", "overcast": "clouds",
    "poisoned": "poison", "poisonous": "poison", "poison": "poison",
    "dying": "death", "dead": "death", "died": "death",
    "hot": "heat", "heat": "heat", "warm": "heat",
    "cold": "cold", "cool": "cold", "chilly": "cold", "freezing": "cold",
}

FILLER_PREFIXES = [
    r"^\s*(look\s+at|look\s+over\s+there,?|see|behold|notice|watch|"
    r"consider)\s+",
]
AUX_SADHYA = [
    r"^(must\s+be|might\s+be|could\s+be|is\s+probably|is|are|"
    r"seems\s+to\s+be|looks\s+like|looks|appears\s+to\s+be)\s+",
]
FILLER_HETU_PREFIX = [
    r"^(it'?s|it\s+is|it\s+has|there\s+is|there'?s|of|being)\s+",
]
_ARTICLE_RE = re.compile(r"^(the|a|an|that|this|those|these)\s+",
                          re.IGNORECASE)
_DEMONSTRATIVE_NOUN_RE = re.compile(
    r"\b(?:the|a|an|that|this)\s+([a-zA-Z][a-zA-Z-]*)", re.IGNORECASE
)
_CONNECTIVE_RE = re.compile(r"\bbecause\b|\bsince\b", re.IGNORECASE)


def _strip_patterns(text, patterns):
    for pat in patterns:
        text = re.sub(pat, "", text, flags=re.IGNORECASE).strip()
    return text


def normalize_term(phrase):
    """Reduce a noisy natural-language phrase to a canonical single-
    word Nyaya term, using exact match first, then substring match
    against the synonym table."""
    phrase = (phrase or "").strip().strip(".,!?;: ").lower()
    phrase = _ARTICLE_RE.sub("", phrase).strip()
    if not phrase:
        return None
    if phrase in SYNONYMS:
        return SYNONYMS[phrase]
    for key, canon in SYNONYMS.items():
        if key in phrase:
            return canon
    # last resort: return the final content word of the phrase
    words = re.findall(r"[a-zA-Z]+", phrase)
    return words[-1] if words else None


def _find_subject_noun(text):
    """Tiny 'named entity' extractor: returns the first noun-phrase
    headword introduced by an article/demonstrative, e.g.
    'that hill' -> 'hill'."""
    match = _DEMONSTRATIVE_NOUN_RE.search(text)
    if match:
        return match.group(1).lower()
    words = re.findall(r"[a-zA-Z][a-zA-Z-]*", text)
    return words[0].lower() if words else None


class RuleBasedParser:
    """Deterministic, dependency-free NL -> (paksha, hetu, sadhya)
    extractor. Stands in for the 'LLM' described in the design doc.
    Never raises -- always returns a result dict."""

    def parse(self, text):
        original = (text or "").strip()
        if not original:
            return {"success": False, "reason": "Empty input.",
                     "raw_text": original, "backend": "rule-based"}
        try:
            working = _strip_patterns(original, FILLER_PREFIXES)
            conn_match = _CONNECTIVE_RE.search(working)
            if not conn_match:
                return {"success": False,
                         "reason": "No 'because' / 'since' connective "
                                   "found; cannot separate reason from "
                                   "claim.",
                         "raw_text": original, "backend": "rule-based"}
            conn_word = conn_match.group(0).lower()
            before = working[:conn_match.start()].strip().rstrip(",").strip()
            after = working[conn_match.end():].strip()

            if conn_word == "since" and conn_match.start() == 0:
                # "Since <reason>, <claim>"
                parts = after.split(",", 1)
                if len(parts) == 2:
                    reason_clause, claim_clause = parts[0].strip(), parts[1].strip()
                else:
                    reason_clause, claim_clause = after, before
            else:
                # "<claim> because/since <reason>"
                claim_clause, reason_clause = before, after

            if not claim_clause or not reason_clause:
                return {"success": False,
                         "reason": "Could not split the sentence into a "
                                   "claim clause and a reason clause.",
                         "raw_text": original, "backend": "rule-based"}

            paksha = (_find_subject_noun(claim_clause)
                      or _find_subject_noun(reason_clause)
                      or _find_subject_noun(original))

            sadhya_phrase = re.sub(
                r"\b(?:the|a|an|that|this)\s+[a-zA-Z-]+\b", "", claim_clause,
                count=1, flags=re.IGNORECASE
            ).strip()
            sadhya_phrase = _strip_patterns(sadhya_phrase, FILLER_HETU_PREFIX)
            sadhya_phrase = _strip_patterns(sadhya_phrase, AUX_SADHYA)
            sadhya = normalize_term(sadhya_phrase) if sadhya_phrase else None
            if sadhya is None:
                sadhya = normalize_term(claim_clause)

            hetu_phrase = _strip_patterns(reason_clause, FILLER_HETU_PREFIX)
            hetu = normalize_term(hetu_phrase) if hetu_phrase else None

            if not (paksha and hetu and sadhya):
                return {"success": False,
                         "reason": "Could not confidently isolate all "
                                   "three terms (paksha / hetu / sadhya).",
                         "partial": {"paksha": paksha, "hetu": hetu,
                                     "sadhya": sadhya},
                         "raw_text": original, "backend": "rule-based"}

            return {"success": True, "paksha": paksha.capitalize(),
                     "hetu": hetu, "sadhya": sadhya, "raw_text": original,
                     "backend": "rule-based"}
        except Exception as exc:   # pragma: no cover - safety net
            return {"success": False, "reason": f"Parser error: {exc}",
                     "raw_text": original, "backend": "rule-based"}


class NyayaNLParser:
    """Public facade. Tries a registered LLM backend first (if any),
    then falls back to the deterministic RuleBasedParser -- mirroring
    the 'LLM restricted to translation only' design."""

    def __init__(self):
        self._llm_backend = None
        self._fallback = RuleBasedParser()

    def set_llm_backend(self, fn):
        """Register a callable fn(text) -> dict (same contract as
        RuleBasedParser.parse) wrapping a real LLM call."""
        self._llm_backend = fn

    def clear_llm_backend(self):
        self._llm_backend = None

    def parse(self, text):
        if self._llm_backend is not None:
            try:
                result = self._llm_backend(text)
                if result and result.get("success"):
                    result.setdefault("backend", "llm")
                    return result
            except Exception as exc:   # pragma: no cover - safety net
                return {"success": False,
                         "reason": f"LLM backend raised an error: {exc}; "
                                   f"falling back.",
                         "raw_text": text, "backend": "llm-error"}
        return self._fallback.parse(text)
