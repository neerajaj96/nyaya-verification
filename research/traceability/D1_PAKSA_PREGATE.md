# D1 — Pakṣa / Saṃśaya Pre-Gate (Provisional Specification)

Status: pre-gate SPECIFICATION, not adjudication. D1 remains OPEN.
Labels used per statement: NS_EXPLICIT / BHASHYA_SUPPORTED /
VARTTIKA_SUPPORTED / LATER_COMMENTARY_SUPPORTED / TARKASANGRAHA_SUPPORTED /
CROSS_STRATUM_SYNTHESIS / ENGINEERING_ABSTRACTION / DEFERRED / INSUFFICIENT_EVIDENCE.

Corresponding legacy components (read-only inspection, unmodified):
`engine.py :: infer/infer_from_text` (assumes hetu-present,
`source="assumed"`, no doubt/desire/proof-absence checks);
`fallacy.py :: diagnose` checks 1–2 (locus-exists, hetu True/False/None).

## 1. Evidence (labelled)

- E1 [NS_EXPLICIT — NS 2.1.6, `targeted/ns_2_1_1_7_samsaya.md`]: doubt arises
  ONLY from cognition presenting a common property WITHOUT apprehending the
  distinctive feature (1-1-23 restriction); doubt ceases on feature-perception.
- E2 [NS_EXPLICIT — NS 2.1.1–5 pūrvapakṣa + BHASHYA_SUPPORTED replies]:
  doubt does NOT arise from bare presence, one-thing cognition, mere
  diversity-of-opinion, mere uncertainty-as-fact, or cross-thing (colour→
  touch) projection; conviction (*adhyavasāya*) excludes doubt by definition.
- E3 [VARTTIKA_SUPPORTED — Vārttika on 2.1.1/2.1.7]: doubt necessary for
  ENQUIRY, not for definitive cognition; learned parties may be certain;
  denial-of-doubt is itself a disputational move to be answered.
- E4 [NS_EXPLICIT — NS 2.1.7 + LATER_COMMENTARY_SUPPORTED (Bhāṣyachandra
  verses, Vivaraṇa, Pariśuddhi)]: doubt-first Q&A is the universal
  investigation protocol, generalizing across categories (e.g. pramāṇa-number
  doubt).
- E5 [BHASHYA_SUPPORTED — Bhāṣya on 1.2.7]: *cintā* = desire-to-ascertain
  process running doubt → definitive cognition (desire-like element, tied to
  suspense, not to inference-licensing).
- E6 [TARKASANGRAHA_SUPPORTED — TS §2 D, §14 D]: pakṣatā =
  *siṣādhayiṣāviraha-viśiṣṭa-siddhyabhāvaḥ*; parāmarśa must be pakṣatā-aided;
  saṃśayottara-pratyakṣa excluded from anumiti.
- E7 [INSUFFICIENT_EVIDENCE]: siṣādhayiṣā and siddhyabhāva have NO verified
  occurrence in acquired NS/Bhāṣya/Vārttika; no Tier-2 bridge acquired
  (G-UD-01 open).

## 2. Provisional rule (narrowest computationally useful statement)

A locus–sādhya pair may enter the enquiry track (ENGINEERING_ABSTRACTION —
labelled, not classical) ONLY IF all three hold:
  (R1) a common property is cognized on the locus WITHOUT its distinctive
       feature being apprehended [NS_EXPLICIT, E1];
  (R2) two-sided alternatives are live (neither side definitely ascertained)
       [NS_EXPLICIT, E1 + BHASHYA_SUPPORTED 1.2.7 *prakaraṇam* gloss];
  (R3) no *adhyavasāya* (certain conviction) of the sādhya's presence or
       absence is on record for the locus [BHASHYA_SUPPORTED, E2].
If R3 fails (conviction present), the pair is NOT in doubt — it may still be
assented to, but NOT via the enquiry track [VARTTIKA_SUPPORTED, E3].
This rule is deliberately NOT called "pakṣatā semantics": it formalizes NS
doubt-conditions only, and pakṣatā additionally requires E7 items.

## 3. Exact textual scope

- Applies to: NS-stratum doubt-gating (2.1.1–7 + 1.2.7 *prakaraṇam*/*cintā*).
- Does NOT extend to: TS pakṣatā (siṣādhayiṣā/siddhyabhāva — DEFERRED);
  perceived-fire/manana cases (TS §14 D — TARKASANGRAHA_SUPPORTED only);
  Buddhist sapakṣa-disciplines (NOT_ACQUIRED, G-DG-01).

## 4. Prohibited extrapolations

- P1: Do NOT invent a siṣādhayiṣā gate (desire-to-infer flag) — E7.
- P2: Do NOT treat R1–R3 as necessary for ALL inference (Vārttika: definitive
  cognition need not follow doubt — E3); the rule gates ENQUIRY, not assent.
- P3: Do NOT equate "assumed" facts (`source="assumed"`) with doubt-
  resolution — the corpus gives assumed facts NO doubt-resolving power.
- P4: Do NOT grade doubt (no degrees/thresholds anywhere in E1–E5).
- P5: Do NOT back-project TS pakṣatā vocabulary onto NS passages.

## 5. Deferred questions (move to DEFERRED_DECISIONS.md)

- Q1: siṣādhayiṣā origin and scope (G-UD-01).
- Q2: siddhyabhāva operationalization (what counts as absence of prior
  proof — perception? debate-record? stipulation?).
- Q3: enquiry-mode vs assent-mode architecture (VARTTIKA_SUPPORTED split,
  no implementation shape yet).
- Q4: student-vs-learned certainty relativity (Tātparya gloss — party-
  indexed doubt, DEFERRED).
