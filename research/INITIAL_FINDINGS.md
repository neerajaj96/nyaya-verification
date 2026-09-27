# INITIAL FINDINGS (Phase 0 close-out)

Read this first, then follow the cited files. Every bullet below is backed by
the audit files; no implementation was done, no code modified, no doctrine
invented.

## 1. What the classical sources actually contain

Two editions of **one work** — Annambhaṭṭa's *Tarkasaṃgraha* with his own
*Dīpikā* (Nyāya–Vaiśeṣika primer): P1 = Virupakshananda/Ramakrishna Math 1994
(197 pp, best for IAST/English search and clean per-sūtra translation); P2 =
Athalye–Bodas/Bombay Sanskrit Series 1930 (466 pp, adds Govardhana's
*Nyāya-Bodhinī* + ~300 pp critical Notes, best for Devanāgarī density and
vyāptigraha/upādhi depth). Inference core: TS §§1–28 (P1 printed 88–116;
P2 Notes §§42–59). Full inventory: `source_audit.md`,
`classical_sources/anumana_passages.md`. The system is stable across editions
(opening sūtras verbatim identical): anumāna = *anumiti-karaṇa* (§1); anumiti
= *pakṣatā-sahakṛta-parāmarśa-janya* (§2+D); parāmarśa = *vyāpti-viśiṣṭa-
pakṣadharmatā-jñāna* with fixed mountain/smoke/fire example (§3);
vyāpti = *sāhacarya-niyama* technically
*hetusamānādhikaraṇātyantābhāvāpratiyogi-sādhyasāmānādhikaraṇya* (§4);
svārtha/parārtha + pañcāvayava with per-member glosses and prayojanas
(§§6–9); liṅga-traividhya with kevala edge cases (§§11–13); pakṣa/sapakṣa/
vipakṣa with *sandigdha/niścita* qualifiers + pakṣatā refinement (§§14–16, §2
D); five hetvābhāsas with full subtypes, stock examples, and a two-level
blocking theory (§§17–28, D p. 116); vyāptigraha = bhūyodarśana +
vyabhicāra-absence (niścaya + śaṅkā) + tarka/svataḥ + sāmānya-pratyāsatti
(§7 D, incl. the vajra counterexample to frequency-only induction).

## 2. What Tarka AI actually implements

The **older snapshot** of the `nyaya_engine` package (16 `.py`, no data, no
tests): full anumāna pipeline (WorldModel tristate facts → 9-point
`diagnose` → `Syllogism` svartha+pañcāvayava → forward-chain assert), 7-
padārtha ontology (9/24/5 seeds, coarse § comments), 4-pramāṇa base classes,
five proposal-only ML bridges (rule-NLP, BoW-embeddings, threshold-0.15 RAG,
keyword-mock vision, Apriori miner with multi-term option), demo + REPL
menus [1]–[11]. Details: `software/tarka_ai_architecture.md`.

## 3. What the Nyāya Engine actually implements

The **newer superset snapshot** (20 files + 1,121-chunk vendored Athalye/Bodas
corpus): everything in §2, plus corpus-as-default-Āpta (`tarka_corpus.py`,
`preprocess_corpus.py`, auto-ingest at construction), read/citation path
(`query_passages`, `ground_term`, `excerpt`, `sources()`), per-term `section=`
refs, RAG retune 0.15→0.22, CLI [12] + demo Part C, single-term-only miner
teaching, parse-result backend tags, EOF-safe CLI — all covered by a **31-test
stdlib suite that passes offline** (verified by execution). Details:
`software/nyaya_engine_architecture.md`.

## 4. Where they overlap

They are the same project at two revisions: identical WorldModel/Vyāpti/
`diagnose`-order/`Syllogism`/bridge architecture; every shared file diffs
incrementally; zero files unique to the older snapshot. See
`software/tarka_vs_nyaya_engine.md` (duplicate/complementary/incompatible
analysis + verified diff stats).

## 5. Where they differ

Only additively in the newer snapshot: corpus layer (4 new files), section
refs, threshold tuning, test suite, demo/CLI grounding options, and small
robustness renames (`assert_fact→testify`, `target_obj→target_object`,
`doc_<n>→doc<n>`, direct upamāna writes, early-return vision loop). No fork,
no rival abstractions, no data-model conflict between snapshots.

## 6. What appears reusable

As *engineering*: the newer snapshot wholesale — package structure, firewall
(proposal vs. disposal separation), 9-gate pipeline shape, proof-object
generator, bridge seams, corpus tooling, tests. As *doctrine*: the taxonomy,
stock examples, five-slot/five-gloss pañcāvayava, svārtha sequence, upādhi
formula wording, blocking-theory vocabulary — all directly supported and safe
to quote. Per-item verdicts: `traceability/classical_to_code.md` (T1–T15).

## 7. What appears incorrect or uncertain

Ten recorded conflicts (nothing silently fixed):
C1 pakṣatā gate missing (high); C2 numeric pramāṇa strengths unattested
(medium); C3 satpratipakṣa without balance (medium); C4 anupasaṃhārin erased
(medium); C5 upādhi-as-flag (high); C6 counterexample strings vs. *niścita*
vipakṣa (high); C7 miner rules called vyāpti without tarka/sāmānya (high);
C8 dead `kind`/`vipakṣa` + kevala blindness (medium); C9 cosine-as-āpta
(medium); C10 linear order vs. two-level blocking theory (low–medium).
Full texts: `traceability/conflicts.md`. The "hetu ∧ ¬sādhya" search is
**partially supported** (valid sādhāraṇa/anvaya-violation fragment) but an
**oversimplification** stand-alone (no vyatireka half, no kevala tolerance,
no *niścita*/substratum qualifiers, no tarka/sāmānya establishment):
`classical_sources/vyapti_complete.md` §12.

## 8. What cannot yet be determined

(a) Full cell-by-cell verification of the 24-guṇa residence/section table
(spot-checked only); (b) whether P2's Notes contain additional tarka/upādhi
detail beyond the extracted window that would sharpen C5/C7; (c) what should
count as *niścaya*/*āpta*/balance in computational terms (all three need
human doctrinal rulings, not more code reading); (d) acceptable citation
granularity for śabda-grounding (paragraph chunks vs. TS-§ chunks); (e) the
intended semantics of the stored-but-dead `kind`/`vipakṣa` fields; (f) final
verifier architecture — expressly deferred per the brief.

## 9. Which classical passages are most important (priority order for the architect)

1. §4 vyāpti mūla + D technical definition (formalization target).
2. §3 parāmarśa + §5 pakṣadharmatā + §2 pakṣatā D (inference gate).
3. §7 svārtha + §7 D vyāptigraha/tarka/sāmānya/vajra (learning procedure).
4. §§11–13 liṅga-traividhya + kevala proofs (edge-case requirements).
5. §§14–16 pakṣa/sapakṣa/vipakṣa + §14 D (epistemic qualifiers).
6. §9 pañcāvayava + member glosses/prayojanas (proof-object spec).
7. §§17–28 hetvābhāsa subtypes + D p. 116 blocking theory (checker spec).
8. §27 upādhi definition + ayogolaka (conditional-vyāpti spec).
9. §28 bādhita + sparśana-pratyakṣa (defeat spec).
10. §23 satpratipakṣa pair + §22 viruddha (one-vs-two hetu architecture).
All are quoted with PDF/printed locations in
`classical_sources/anumana_passages.md`.

## 10. What should be investigated next (for ChatGPT, the next architect)

1. Rule on pakṣatā modelling (C1) before any verifier control flow.
2. Rule on counterexample admission + substratum representation (C6) before
   trusting any "hetu ∧ ¬sādhya" verdicts.
3. Rule on upādhi proof procedure (C5) and miner promotion criteria (C7) —
   these two jointly decide whether the vyāpti research direction is viable.
4. Decide kevala scope (C8) and anupasaṃhārin handling (C4) explicitly
   (implement vs. documented exclusion).
5. Replace or ground the pramāṇa-strength table (C2) and the balance test
   (C3); adopt the two-level blocking vocabulary in reports (C10).
6. Re-chunk or re-OCR the corpus by TS § and relabel cosine-retrieval as
   retrieval (C9); finish the 24-guṇa cell audit.
7. Keep the firewall (proposal/disposal split) and the newer snapshot as the
   baseline; archive the older "Tarka AI" snapshot for provenance only.
8. Do not design the final verifier until 1–6 are ruled — the traceability
   map (`PRIMARY TEXT → INTERPRETATION → EXISTING CODE → POSSIBLE
   COMPUTATIONAL FORMALIZATION`) with per-step verdicts is built for exactly
   that sequencing.
