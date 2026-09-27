# D5 — Upādhi Pre-Gate (Provisional Specification)

Status: pre-gate SPECIFICATION, not adjudication. D5 remains OPEN. This
document MUST NOT be read as a final computational proof rule for upādhi.
Legacy components (read-only): `vyapti.py :: Vyapti.upadhi` (free string),
`fallacy.py` check 9 (truthy ⇒ Vyapyatvasiddha), `engine.py ::
teach_vyapti(..., upadhi=...)`, CLI upādhi prompt.

## 1. Three evidentiary buckets (do not mix)

### Bucket A — Early-Nyāya evidence (NS/Bhāṣya/Vārttika; no upādhi-term)

- A1 [NS_EXPLICIT — NS 2.1.38 Bhāṣya]: only QUALIFIED particulars count as
  probans (rain-augmented water with foam/velocity/flotsam; calm ant-hosts;
  ṣaḍja-pitched scream). Fault of misfire lies with the inferrer, not
  inference. (`targeted/ns_2_1_38_inference.md`)
- A2 [VARTTIKA_SUPPORTED — Vārttika on 2.1.38]: qualified premisses are
  falsity-free: "cannot be brought about by any other cause save rain";
  "never found unconcomitant with coming rain."
- A3 [VARTTIKA_SUPPORTED — Vārttika on 1.1.5]: smoke/fire concomitance
  accepted AS cause-effect textured (effect→material-cause) against the
  Bauddha mere-relation option.
- A4 [BHASHYA_SUPPORTED — Bhāṣya on 2.2.1]: *sambhava* defined via
  "invariably concomitant" cognition; *abhāva* used substantively
  (presence/absence contrast as cognition-source).

### Bucket B — Tarkasaṃgraha machinery (late, terminologized)

- B1 [TARKASANGRAHA_SUPPORTED — TS §27]: upādhi =
  *sādhyavyāpakatve sati sādhanāvyāpakatvam*, exhibited by
  ārdrendhana-saṃyoga + ayogolaka counterexample; sopādhika hetu =
  vyāpyatvāsiddha. (`classical_sources/anumana_passages.md` §9)
- B2 [TARKASANGRAHA_SUPPORTED — D p.116]: upādhi operates
  *vyabhicārajñānadvārā vyāptijñānapratibandhakaḥ* (via defeater-cognition
  against concomitance-cognition).

### Bucket C — Later formalization (deferred; must NOT be used yet)

- Trairūpya-framed upādhi analysis, Gaṅgeśa/Navya-Nyāya avacchedaka
  machinery, any "H ∧ U → S" conditional rendering: all DEFERRED
  (G-DG-01, G-GG-01, G-NN-01 open; see DEFERRED_DECISIONS.md).

## 2. Minimum representation that does not overclaim

A future record may carry AT MOST (all ENGINEERING_ABSTRACTION):
  - `qualification`: the viśeṣaṇa-string narrowing the hetu (Bucket A
    practice; e.g. "rain-augmented rise");
  - `suspected_condition`: a free-text candidate conditioner, EXPLICITLY
    labelled suspected — NEVER `upadhi` (that name asserts Bucket B status);
  - `exhibited_defeater`: pointer to an exhibited locus where hetu holds
    without sādhya under the suspected condition (ayogolaka-pattern).
`suspected_condition` MUST NOT block inference (downgrade to annotation);
blocking requires a proved record (Bucket B), which NO current evidence
procedure can produce (proof procedure itself DEFERRED).

## 3. Evidence required before accepting an upādhi (necessary, not sufficient)

For TS-mode acceptance, ALL of (from B1, TARKASANGRAHA_SUPPORTED):
  (U1) exhibition of sādhya-pervasion by the candidate (wherever
       smoke... the condition);
  (U2) exhibition of hetu-non-pervasion (fire without the condition —
       ayogolaka pattern);
  (U3) same-substratum readings for both (TS §4 D idiom; cf. D6).
For NS-mode, the check is A1–A2 shaped (qualify-until-undefeated +
"no-other-cause" + "never-unconcomitant" locutions) with NO pervasion
proof and NO blocking force beyond the exhibited case.
U1–U3 have NEVER been executed in any acquired stratum as a procedure —
they are exhibited, not derived. Hence NO proof rule is specified here.

## 4. What cannot currently be inferred

- From a suspected condition to a proved upādhi (no procedure).
- From "H ∧ U → S" (even if true as material conditional) to "U is the
  upādhi of H→S" — the conditional rendering is ENGINEERING_ABSTRACTION
  until the corpus establishes equivalence; PER BRIEF §4 it MUST NOT be
  auto-encoded as the classical meaning.
- From NS viśeṣaṇa-practice to TS upādhi-proof (different strata, different
  force).

## 5. Source acquisition required to finalize

- G-UD-01 (Pariśuddhi): formula origins, proof-procedure detail.
- P2 Notes on TS §56/upādhi: commentarial elaboration (Phase 0 flagged).
- G-DG-01: Buddhist occurrence-discipline comparator (blocks adopting any
  pervasion-test as "the" rule).
- G-NS-01 (Vol. 3): any Adhyāya III–V conditional-concomitance material.
