# Research Question

These are the questions established in Phase 0
(`research/INITIAL_FINDINGS.md` §10), reproduced here without invention.
Each maps to open decisions in `research/traceability/OPEN_DECISIONS.md`.

## Primary question

Can inference — especially *vyāpti* (invariable concomitance) and
*hetvābhāsa* (fallacy) analysis — be **mechanically verified** by a symbolic
system whose every abstraction is traceable to primary-source evidence
(primary text → interpretation → existing code → possible formalization)?

## Sub-questions

1. **Pakṣatā gate (D1).** How should doubt (*saṃśaya*), absence of prior
   proof (*siddhyabhāva*), and desire to infer (*siṣādhayiṣā*) gate a
   verifier's control flow? The source makes pakṣatā definitional of anumiti
   (TS §2 D); the baseline has no such gate.
2. **Counterexample semantics (D6).** What may count as a counterexample, and
   what do *niścaya* (ascertainment) and same-substratum
   (*sāmānādhikaraṇya*) mean computationally? Phase 0 verdict: a naïve
   "hetu(x) ∧ ¬sādhya(x)" search is only a partial operationalization of
   vyāpti (`classical_sources/vyapti_complete.md` §12).
3. **Conditional concomitance and rule promotion (D5, D7).** What proves an
   *upādhi* (TS §27 double-pervasion + ayogolaka), and what promotes a mined
   concomitance to *vyāpti* given the source's tarka/sāmānya/śaṅkā-discharge
   requirements (TS §7 D, vajra case)? These jointly decide whether the
   vyāpti-learning direction is viable.
4. **Edge-case scope (D8, D4).** Kevala-only reasons and universal-pakṣa
   (anupasaṃhārin) cases: implement or explicitly exclude?
5. **Defeat and balance (D2, D3, D10).** What defeat ordering replaces the
   unattested pramāṇa-strength table, what test captures *samatva* for
   satpratipakṣa, and should reports distinguish parāmarśa-blockers from
   anumiti-blockers (D p. 116)?
6. **Honest grounding (D9).** What citation granularity (TS-§ chunks vs.
   paragraph chunks) and what mechanism make source-grounded retrieval an
   honest śabda-adjacent tool rather than an overclaimed *āpta* test?

## Non-questions (out of scope for the verification inquiry)

- Rewriting or "modernizing" the classical terminology.
- Equating Sanskrit concepts with Western logical concepts by surface
  similarity.
- Improving baseline code for its own sake (baseline is frozen; see
  `src/nyaya_verification/BASELINE.md`).
