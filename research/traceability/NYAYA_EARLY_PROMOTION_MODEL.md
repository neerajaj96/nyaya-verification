# Early-Nyāya Promotion Sketch (Conceptual State Machine — NOT Implementation)

READ FIRST: this is a READING AID for NS-stratum evidence, not a design, not
pseudocode, not executable semantics. State names are lowercase precisely to
avoid collision with any future CANDIDATE/SUPPORTED/VIOLATED vocabulary,
which the evidence does NOT support (no such terms in NS strata). Every
transition carries source + passage + interpretation + confidence +
unresolved issue. Stratum tags are part of every state.

## States (NS-mode only; TS-mode states are NOT modelled here)

- `exhibited`: qualified co-occurrence exhibited at a named locus
  (kitchen smoke/fire; foam-marked rise; calm hosts; ṣaḍja scream).
- `scrutinized`: survived alternative-interpretation pressure (cause-effect
  texture accepted over mere relation — 1.1.5 Vārttika).
- `challenged`: exhibited defeater on record (dam/nest/mimic — 2.1.37).
- `requalified`: finer qualification exhibited that the defeater does not
  touch (foam/hosts/ṣaḍja — 2.1.38).
- `displayable`: stateable in five factors (1.1.32) with the qualified
  probans; "infallible" exhibited (serpents).
- `rejected`: charger shown unproved (asiddha-turn — 2.1.38 Vārttika) or
  scope-mismatched (all-vs-some attack).

## Transitions

1. `exhibited → scrutinized`
   Source/passage: Vārttika on 1-1-5 (Bauddha trilemma; cause-effect
   accepted). Interpretation: candidacy requires interpretation-survival,
   not mere exhibition. Confidence: VARTTIKA_SUPPORTED. Unresolved: full
   trilemma-exhaustion rule (only smoke/fire worked through).
2. `scrutinized → challenged`
   Source/passage: NS 2.1.37 (dam/nest/mimic). Interpretation: ANY exhibited
   stock is challengeable by finer exhibits; challenge is normal, not
   terminal. Confidence: NS_EXPLICIT. Unresolved: standing of unexhibited
   (suspected) challenges — no śaṅkā doctrine at this stratum.
3. `challenged → requalified`
   Source/passage: NS 2.1.38 Bhāṣya (viśeṣaṇa triple). Interpretation:
   meet exhibits with finer exhibits; fault attaches to the inferrer's
   vague probans. Confidence: NS_EXPLICIT (Bhāṣya) + BHASHYA_SUPPORTED
   detail. Unresolved: sufficiency rule for qualifications (exhibited
   infallibility, never derived).
4. `requalified → displayable`
   Source/passage: NS 1.1.32 (five factors) + 2.1.38 "infallible" exhibits.
   Interpretation: displayability is the promotion criterion — a relation
   that cannot be five-factor-stated with the qualified probans is not
   promoted. Confidence: CROSS_STRATUM_SYNTHESIS (32 + 38 combined; flagged
   as synthesis, not single-passage claim). Unresolved: whether display is
   constitutive or merely presentational at this stratum.
5. `challenged → rejected` (charger-side)
   Source/passage: 2.1.38 Vārttika (asiddha-turn; quantifier attack).
   Interpretation: unproved or scope-mismatched chargers are REJECTED, not
   weighed — no "weak defeater" state exists. Confidence:
   VARTTIKA_SUPPORTED. Unresolved: proof-standard for chargers (same as
   for stocks? unstated).
6. `exhibited → challenged` via double-non-finding is FORBIDDEN as defeat:
   1.2.7 Vārttika (neutralising ≠ defeating; admitted-locus conditions).
   Confidence: VARTTIKA_SUPPORTED. This is a NON-transition constraint.

## Why this is NOT an algorithm

No passage gives ordered steps, termination conditions, or decision
procedures — only exhibited moves and their evaluations. Turning the above
into control flow would be ENGINEERING_ABSTRACTION (permitted later, with
labelling — never as "the NS procedure").

## TS-mode contrast (not modelled, for orientation only)

TS promotion would need pakṣatā-context, niścaya/śaṅkā-discharge, tarka/
sāmānya stages, and blocking-theory clearance — a DIFFERENT machine sharing
only state-names by analogy. Building it requires G-UD-01 + tarka-pattern
survey (DEFERRED).
