# Traceability Conflicts — Code vs. Primary Texts

Standing rule: code does not overrule the text. Each entry records the
disagreement, the exact source passage, the exact code location, severity for
any future verifier work, and what would be needed to resolve it. Nothing is
silently fixed.

## C1. Pakṣatā gate missing (inference fires without doubt/desire/proof-absence)

- Code: `engine.py :: infer/infer_from_text` + `fallacy.py :: diagnose` —
  no representation of *saṃśaya* (doubt), *siṣādhayiṣā* (desire to infer),
  or *siddhyabhāva* (absence of prior ascertainment). `infer_from_text`
  additionally *assumes* hetu-present for unknown properties
  (`source="assumed"`), i.e. infers precisely where the source demands
  pakṣatā scrutiny.
- Source: TS §2 D (*pakṣatā-sahakṛta-parāmarśa-janya* requirement;
  *siṣādhayiṣāviraha-viśiṣṭa-siddhyabhāvaḥ = pakṣatā*; saṃśayottara-pratyakṣa
  exclusion) + §14 D (manana/perceived-fire objections answered by
  *uktapakṣatāśrayatva*) (P1 PDF ~88–90, ~103–104).
- Disagreement: the source makes pakṣatā a *definitional* precondition of
  anumiti; the code has no such precondition, so it certifies inferences the
  source would withhold (already-proved sādhya) and conflates perception-
  after-doubt with inference.
- Severity: high (control-flow precondition, not a corner case).
- Resolution needs: human decision on a pakṣatā model (doubt flag +
  proof-absence flag + desire flag per pakṣa–sādhya pair) and on whether
  "assumed" hetu may ever ground parāmarśa.

## C2. Numeric pramāṇa-strength table unattested

- Code: `fallacy.py :: PRAMANA_STRENGTH` (4/3/2/1/0) gating bādhita.
- Source: TS §28 says *pramāṇāntareṇa niścitaḥ* with a pratyakṣa example;
  no total order of pramāṇas, no numbers, no "≥ anumāna" rule in the
  extracted window (P1 PDF ~115–116).
- Disagreement: strength comparisons (śabda 3 beats anumāna 1; upamāna 2
  beats anumāna 1) are engineering posits presented in classical dress.
- Severity: medium (affects which bādhita verdicts fire).
- Resolution needs: human ruling — either ground a defeat ordering in
  commentarial passages beyond the extracted window, or replace the table
  with "any *niścita* pramāṇāntara absence ascertainment blocks" (closer to
  the sūtra) plus explicit tie-breaking policy labelled as engineering.

## C3. Satpratipakṣa without *samatva* (balance)

- Code: `fallacy.py` check 5 — any other live counter-row with h2 present
  suffices; no strength/soundness comparison between the two hetus.
- Source: TS §23 (*sādhyābhāva-sādhakaṃ hetvantaraṃ*) read with the
  *sat* (balanced/equipollent) qualifier and the stock pair where *both*
  sides cite dṛṣṭānta (soundness; jar) (P1 PDF ~108–109).
- Disagreement: code flags counterbalanced-ness from one-sided storage; the
  source requires apparent equal soundness on both sides.
- Severity: medium (false-positive satpratipakṣa verdicts).
- Resolution needs: definition of balance (both vyāptis live + both hetus
  pakṣa-present + both sapakṣa-backed?) or explicit downgrade to
  "possible-counter-hetu warning".

## C4. Anupasaṃhārin erased (conflated with asādhāraṇa)

- Code: single `sapaksha is None` gate serves both; no universal-pakṣa test.
- Source: TS §§20–21 are distinct defects with distinct diags (universal
  absence-elsewhere vs. universal pakṣa ⇒ no dṛṣṭānta) (P1 PDF ~106–108).
- Disagreement: two source defects map to one code branch; the
  "everything is pakṣa" diagnosis is unrepresentable.
- Severity: medium (one named classical defect has no implementation).
- Resolution needs: separate `domain == pakṣa` detection (requires a domain
  model the code currently lacks) or documented scope exclusion.

## C5. Upādhi thinned to a flag

- Code: `vyapti.py :: upadhi` string + `fallacy.py` check 9 (truthy ⇒
  vyāpyatvāsiddha).
- Source: TS §27 double-pervasion definition + proof obligation + ayogolaka
  counterexample (P1 PDF ~111–112).
- Disagreement: source requires exhibiting a sādhya-pervading/hetu-non-
  pervading property; code blocks on any attached string, including
  unproved or mis-shaped ones, and provides no way to *prove* an upādhi.
- Severity: high for any verifier touching conditional concomitance
  (the research direction's core).
- Resolution needs: upādhi proof procedure (two concomitance checks +
  exhibited counterexample locus) or relabelling the field
  `suspected_upadhi: str` with blocking downgraded to warning.

## C6. Counterexample strings vs. *niścita* vipakṣa loci

- Code: `add_counterexample(instance: str)` + `is_valid()` ⇔ empty list.
- Source: vipakṣa = *niścita-sādhyābhāvavān* (ascertained absence); vyāpti
  guard is same-substratum absence (P1 PDF ~91, ~104).
- Disagreement: code accepts arbitrary strings (no locus existence, no
  hetu-presence, no absence-ascertainment, no substratum identity); a typo
  breaks a vyāpti as effectively as the lake does in §19.
- Severity: high (the "hetu ∧ ¬sādhya" check's entire weight rests here).
- Resolution needs: counterexample admission criteria (locus known +
  hetu-present-ascertained + sādhya-absent-ascertained + same-substratum
  reading) or explicit "unverified defeater" semantics.

## C7. Miner rules called vyāpti without tarka/sāmānya/śaṅkā-discharge

- Code: `rule_miner.py :: teach_engine` (support/confidence ⇒ `teach_vyapti`).
- Source: vyāptigraha = sahacāra + vyabhicāra-absence (niścaya *and* śaṅkā)
  + tarka/svataḥ + sāmānya-pratyāsatti; vajra case refutes frequency-only
  induction (P1 PDF ~93–94).
- Disagreement: the code's induction implements one of four source
  components and labels the output with the source's term.
- Severity: high (directly concerns the proposed vyāpti-learning direction).
- Resolution needs: human decision — either add defeater/tarka/universaliza-
  tion stages to the miner, or rename outputs `candidate-concomitance` and
  route them through the defeater checks before promotion to vyāpti.

## C8. `kind`/`vipakṣa` stored but dead (kevala blindness)

- Code: `Vyapti.kind`, `Vyapti.vipaksha` written, never read.
- Source: §§11–13 kevalānvayi/kevalavyatireki with no-dṛṣṭānta lemmas (P1
  PDF ~99–100).
- Disagreement: the schema gestures at the source's bivalent/kevala
  taxonomy while the checker implements anvaya-only logic; kevala reasons
  are silently mishandled (a kevalavyatireki hetu with no sapakṣa reads as
  asādhāraṇa-defective by check 8).
- Severity: medium (wrong verdicts on a classical edge class).
- Resolution needs: either implement vyatireka checking + kevala branches or
  document kevala reasons as out-of-scope inputs.

## C9. Corpus chunks + cosine threshold presented as Āpta-śabda

- Code: `tarka_corpus.py` + `rag_shabda.py (0.22)` + README "Apta source".
- Source: śabda = *āpta-vākya* (TS §59); the bundled text is a 1930 critical
  edition, chunked by paragraph length with README-admitted loss of § mapping.
- Disagreement: a retrieval-similarity score over OCR chunks is equated with
  credibility-of-speaker doctrine; no sūtra supports thresholds, chunking, or
  edition-as-āpta.
- Severity: medium (citationUX is genuinely useful; doctrinal labelling is not
  established). Low risk if relabelled "source-grounded retrieval".
- Resolution needs: re-chunk by TS § (or admit granularity limits) and
  relabel the mechanism; human ruling on what, if anything, counts as *āpta*
  in this system.

## C10. Linear 9-check order vs. two-level blocking theory

- Code: fixed sequence 1→9, first-hit-wins `FallacyReport`.
- Source: D p. 116 two-level theory (bādhita/satpratipakṣa block anumiti
  directly; the rest block parāmarśa via distinct sub-routes).
- Disagreement: order effects are unstated (e.g. a case that is both viruddha
  and bādhita reports whichever comes first — viruddha at 4 before bādhita
  at 3? actually bādhita is 3, viruddha 4 — but vs. satpratipakṣa at 5, or
  vs. vyāpyatva at 9, priority is an engineering choice with no cited basis);
  the Dīpikā's route distinctions (absence-of-concomitance vs. doubt-raising
  vs. pakṣadharmatā-blocking) are flattened to one label stream.
- Severity: low–medium (verdicts mostly coincide; explanations/priority do not).
- Resolution needs: human decision on report priority and on whether
  parāmarśa-blockers vs. anumiti-blockers should be distinguished in output.

## Non-conflicts explicitly cleared (do NOT file as disagreements)

- N1. Fivefold hetvābhāsa list, all subtype definitions, all stock examples:
  match 1:1 (§17–28).
- N2. Pañcāvayava five slots + order + stock content: match (§9).
- N3. Svārtha sequence (bhūyodarśana → smaraṇa → parāmarśa → anumiti):
  match (§7).
- N4. Vyāpti mūla + Dīpikā technical definition: quoted verbatim in both
  editions; code docstrings cite them correctly (even though the code does
  not implement the guard's logic — that gap is C6/C7, not a misquotation).
- N5. "Tarka AI" vs. "Nyāya Engine" are not rival doctrinal implementations:
  same project, two snapshots (see `software/tarka_vs_nyaya_engine.md`).
