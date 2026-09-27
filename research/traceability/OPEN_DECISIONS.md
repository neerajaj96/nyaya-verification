# Open Decisions — Implementation ↔ Source Conflicts

Phase 0 (`traceability/conflicts.md`) recorded 10 disagreements between the
baseline implementation and the primary-source evidence, plus 5 cleared
non-conflicts. Per the Phase 1 rule — do NOT resolve, correct, delete, or
rename — each conflict becomes one decision below. All statuses are OPEN:
Phase 0 established no resolutions.

Format per decision: ID / CURRENT IMPLEMENTATION / SOURCE EVIDENCE /
CONFLICT / WHY IT MATTERS / POSSIBLE INTERPRETATIONS / RESEARCH REQUIRED /
DECISION STATUS.

---

## D1 (from C1). Missing pakṣatā gate

- CURRENT IMPLEMENTATION: `legacy_engine/engine.py :: infer/infer_from_text`
  + `fallacy.py :: diagnose` have no representation of doubt, desire to
  infer, or absence of prior proof. `infer_from_text` assumes hetu-present
  (`source="assumed"`) for unknown properties before inferring.
- SOURCE EVIDENCE: TS §2 Dīpikā — anumiti requires
  *pakṣatā-sahakṛta-parāmarśa*; pakṣatā =
  *siṣādhayiṣāviraha-viśiṣṭa-siddhyabhāvaḥ*; saṃśayottara-pratyakṣa (post-or-
  man doubt → perception) is explicitly excluded from anumiti (P1 PDF ~88–90;
  `classical_sources/anumana_passages.md` §1). TS §14 D answers the manana /
  perceived-fire objections via *uktapakṣatāśrayatva* (PDF ~103–104).
- CONFLICT: the source makes pakṣatā definitional; the code infers without
  it, certifying already-proved sādhyas and conflating perception-after-doubt
  with inference.
- WHY IT MATTERS: control-flow precondition for ANY verifier — decides which
  inferences may even be attempted.
- POSSIBLE INTERPRETATIONS: (a) add a pakṣatā model (doubt + proof-absence +
  desire flags per pakṣa–sādhya pair) as a pre-gate; (b) treat pakṣatā as a
  pragmatic filter outside the logic proper; (c) scope the verifier to
  doubt-cases only and document the restriction.
- RESEARCH REQUIRED: settle the scope of *siṣādhayiṣā* (does desiring to
  infer the perceived count? Dīpikā suggests sometimes yes); decide whether
  "assumed" hetu may ever ground parāmarśa.
- DECISION STATUS: OPEN

## D2 (from C2). Numeric pramāṇa-strength table

- CURRENT IMPLEMENTATION: `fallacy.py :: PRAMANA_STRENGTH`
  (pratyakṣa 4 > śabda 3 > upamāna 2 > anumāna 1 > assumed 0) gates the
  bādhita verdict (check 3, "strength ≥ anumāna").
- SOURCE EVIDENCE: TS §28 — *pramāṇāntareṇa niścitaḥ* with a tactile-
  perception example; no total order, no numbers, no threshold in the
  extracted window (P1 PDF ~115–116).
- CONFLICT: śabda-beats-anumāna and upamāna-beats-anumāna outcomes are
  engineering posits in classical dress.
- WHY IT MATTERS: determines which bādhita verdicts fire; a verifier built
  on this table would claim textual backing it does not have.
- POSSIBLE INTERPRETATIONS: (a) ground a defeat ordering in commentarial
  passages beyond the extracted window; (b) replace with "any *niścita*
  pramāṇāntara absence-ascertainment blocks" + an explicitly engineered
  tie-break policy; (c) make strength configurable per debate context.
- RESEARCH REQUIRED: wider commentarial survey on pramāṇa hierarchy in
  bādha; human doctrinal ruling before any use in a verifier.
- DECISION STATUS: OPEN

## D3 (from C3). Satpratipakṣa without balance (*samatva*)

- CURRENT IMPLEMENTATION: `fallacy.py` check 5 — any other live
  counter-row with h2 present on the pakṣa suffices; no comparison of the
  two hetus' strength or soundness.
- SOURCE EVIDENCE: TS §23 — *sādhyābhāva-sādhakaṃ hetvantaraṃ*, with *sat*
  (balanced/equipollent) as definitional and a stock pair in which BOTH
  sides cite dṛṣṭānta (P1 PDF ~108–109).
- CONFLICT: one-sided storage triggers a verdict the source reserves for
  apparently equal rival reasons → false-positive satpratipakṣa.
- WHY IT MATTERS: a verifier that cries "counterbalanced" at any rival row
  over-rejects; balance is the whole point of the defect.
- POSSIBLE INTERPRETATIONS: (a) require both vyāptis live + both hetus
  pakṣa-present + both sapakṣa-backed; (b) downgrade to a
  "possible-counter-hetu" warning distinct from the classical verdict.
- RESEARCH REQUIRED: define operational *samatva*; check NB/Notes for
  balance criteria.
- DECISION STATUS: OPEN

## D4 (from C4). Anupasaṃhārin conflated with asādhāraṇa

- CURRENT IMPLEMENTATION: single `sapaksha is None` gate (check 8) serves
  both defects; no universal-pakṣa test exists.
- SOURCE EVIDENCE: TS §§20–21 — distinct definitions and diagnostics
  (universal absence-elsewhere vs. universal pakṣa ⇒ no dṛṣṭānta at all)
  (P1 PDF ~106–108).
- CONFLICT: two source defects map to one code branch; "everything is
  pakṣa" is unrepresentable.
- WHY IT MATTERS: a named classical defect has no implementation; future
  evaluation on universal-pakṣa cases would mislabel them.
- RESEARCH REQUIRED: needs a domain model (currently absent) to test
  "pakṣa == domain"; or an explicit documented scope exclusion.
- DECISION STATUS: OPEN

## D5 (from C5). Upādhi thinned to a flag

- CURRENT IMPLEMENTATION: `vyapti.py :: upadhi` free string; check 9 blocks
  whenever truthy, with the ārdrendhana message.
- SOURCE EVIDENCE: TS §27 — upādhi =
  *sādhyavyāpakatve sati sādhanāvyāpakatvam*, proved by exhibiting the double
  pervasion + the ayogolaka counterexample (P1 PDF ~111–112).
- CONFLICT: any attached string blocks, proved or not, well-shaped or not;
  there is no way to prove an upādhi in the system.
- WHY IT MATTERS: HIGH — conditional concomitance is the core of the
  planned vyāpti research direction.
- POSSIBLE INTERPRETATIONS: (a) build an upādhi proof procedure (two
  concomitance checks + exhibited counterexample locus); (b) relabel the
  field `suspected_upadhi` and downgrade blocking to a warning.
- RESEARCH REQUIRED: P2 Notes on §56/upādhi for proof-procedure detail;
  human ruling on candidate-vs-proved upādhi handling.
- DECISION STATUS: OPEN

## D6 (from C6). Counterexample strings vs. *niścita* vipakṣa loci

- CURRENT IMPLEMENTATION: `add_counterexample(instance: str)` appends an
  arbitrary string; `is_valid()` ⇔ empty list.
- SOURCE EVIDENCE: vipakṣa = *niścita-sādhyābhāvavān* (TS §16); vyāpti guard
  is same-substratum absence (TS §4 D) (P1 PDF ~91, ~104).
- CONFLICT: typos break vyāptis as effectively as the lake does in §19 —
  no locus existence, hetu-presence, absence-ascertainment, or substratum
  identity is required.
- WHY IT MATTERS: HIGH — the entire "hetu ∧ ¬sādhya" check rests on this
  admission policy; see `classical_sources/vyapti_complete.md` §12.
- POSSIBLE INTERPRETATIONS: (a) admission criteria (locus known +
  hetu-ascertained + sādhya-absence-ascertained + same-substratum reading);
  (b) explicit "unverified defeater" semantics with weaker force than a
  classical vipakṣa exhibition.
- RESEARCH REQUIRED: what counts as *niścaya* computationally (perception?
  proof? stipulation?) — a human doctrinal ruling.
- DECISION STATUS: OPEN

## D7 (from C7). Miner rules labelled vyāpti without tarka/sāmānya

- CURRENT IMPLEMENTATION: `rule_miner.py :: teach_engine`
  (support/confidence ⇒ `teach_vyapti`).
- SOURCE EVIDENCE: vyāptigraha = sahacāra + vyabhicāra-absence (niścaya AND
  śaṅkā) + tarka/svataḥ + sāmānya-pratyāsatti; the vajra case refutes
  frequency-only induction (TS §7 D, P1 PDF ~93–94).
- CONFLICT: one of four source components is implemented and labelled with
  the source's term.
- WHY IT MATTERS: HIGH — directly concerns the viability of the planned
  vyāpti-learning direction.
- POSSIBLE INTERPRETATIONS: (a) add defeater/tarka/universalization stages
  to any future miner; (b) rename outputs `candidate-concomitance`, promoted
  to vyāpti only after the defeater checks.
- RESEARCH REQUIRED: reconstruct the smoke/fire *tarka*
  (kāryakāraṇabhāva-prasaṅga) in checkable form; survey P2 Notes for further
  tarka patterns.
- DECISION STATUS: OPEN

## D8 (from C8). Dead `kind`/`vipakṣa` fields (kevala blindness)

- CURRENT IMPLEMENTATION: `Vyapti.kind` and `Vyapti.vipaksha` are stored,
  never read; checking is anvaya-only.
- SOURCE EVIDENCE: TS §§11–13 — kevalānvayi/kevalavyatireki with
  no-dṛṣṭānta lemmas (P1 PDF ~99–100).
- CONFLICT: schema gestures at the bivalent/kevala taxonomy while the
  checker silently mishandles kevala reasons (a kevalavyatireki hetu with no
  sapakṣa reads as asādhāraṇa-defective under check 8).
- WHY IT MATTERS: wrong verdicts on a classical edge class; vyatireka has
  no representation at all.
- POSSIBLE INTERPRETATIONS: (a) implement vyatireka checking + kevala
  branches; (b) document kevala reasons as out-of-scope inputs.
- RESEARCH REQUIRED: formalize kevalavyatireki's double-negation pattern
  (`na tathā … tasmān na tathā`) for the proof object.
- DECISION STATUS: OPEN

## D9 (from C9). Similarity-scored chunks presented as Āpta-śabda

- CURRENT IMPLEMENTATION: `tarka_corpus.py` + `RAGShabda(threshold=0.22)` +
  README "Apta source" labelling.
- SOURCE EVIDENCE: śabda = *āpta-vākya* (TS §59); the bundled text is a 1930
  critical edition in paragraph-length OCR chunks with README-admitted loss
  of § mapping.
- CONFLICT: retrieval similarity over chunks is equated with
  credibility-of-speaker doctrine; no sūtra supports thresholds, chunking,
  or edition-as-āpta.
- WHY IT MATTERS: citation UX is genuinely useful, but its doctrinal
  labelling is unattested; a verifier citing "śabda" on this basis would
  overclaim.
- POSSIBLE INTERPRETATIONS: (a) re-chunk by TS § (or admit granularity
  limits) and relabel as source-grounded retrieval; (b) human ruling on what,
  if anything, counts as *āpta* in this system.
- RESEARCH REQUIRED: re-OCR/re-chunk feasibility; śabda-section (§59)
  extraction in a later phase.
- DECISION STATUS: OPEN

## D10 (from C10). Linear check order vs. two-level blocking theory

- CURRENT IMPLEMENTATION: fixed `diagnose` sequence 1→9, first-hit-wins.
- SOURCE EVIDENCE: D on §28 (P1 p. 116) — bādhita/satpratipakṣa block
  *anumiti directly*; the rest block *parāmarśa* via distinct sub-routes
  (absence-of-concomitance vs. doubt-raising vs. pakṣadharmatā-blocking).
- CONFLICT: priority between co-occurring defects is an engineering choice
  with no cited basis; route distinctions are flattened into one label
  stream.
- WHY IT MATTERS: verdicts mostly coincide, but explanations and
  multi-defect cases diverge from the Dīpikā's architecture.
- POSSIBLE INTERPRETATIONS: (a) adopt two-level reporting
  (parāmarśa-blockers vs. anumiti-blockers); (b) justify a priority order
  from commentarial material or declare it engineering policy.
- RESEARCH REQUIRED: collect multi-defect stock cases, if any, from the
  Notes; human ruling on report semantics.
- DECISION STATUS: OPEN

---

## Cleared non-conflicts (no decision needed; recorded so they are not reopened)

N1 fivefold list + subtypes + stock examples match 1:1. N2 pañcāvayava slots
+ order + stock content match. N3 svārtha sequence matches. N4 vyāpti mūla +
Dīpikā definition quoted correctly in code docstrings (implementation gap is
D6/D7, not misquotation). N5 the two code snapshots are one project, not
rival implementations. (Source: `traceability/conflicts.md`.)
