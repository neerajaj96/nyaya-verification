# Hetvābhāsa Non-Collapse Constraints (Implementation Guards)

Purpose: prevent any future implementation from collapsing historically
distinct hetvābhāsa categories. Sources: `targeted/ns_1_2_7_prakaranasama.md`
(non-collapse table) + `hetvabhasa_historical_development.md` (ledger).
Status: CONSTRAINTS, not adjudication; D3/D4/D8/D10 remain OPEN.

## C-NC1. Prakaraṇasama ≠ satpratipakṣa (mandatory separation)

- NS 1.2.7 (BHASHYA_SUPPORTED + VARTTIKA_SUPPORTED): ONE-hetu suspense-
  generator; trigger = double non-finding outside admitted loci; diagnosis
  via admitted-by-both-parties conditions; Tātparya equal-strength gloss.
- TS §23 (TARKASANGRAHA_SUPPORTED): TWO-hetu balance; trigger = exhibited
  rival hetu proving absence; diagnosis via *samatva* (itself unresolved, D3).
- Guard: no verdict label, superclass, or evaluation gold-label may identify
  the two. A shared "inconclusive outcome" is an outcome-taxonomy
  (ENGINEERING_ABSTRACTION if built), never evidence of identity.

## C-NC2. Old fivefold ≠ new fivefold (list-level)

- NS 1.2.4–9 (NS_EXPLICIT): savyabhicāra/viruddha/prakaraṇasama/sādhyasama/
  kālātīta. TS §§17–28 (TARKASANGRAHA_SUPPORTED): savyabhicāra/viruddha/
  satpratipakṣa/asiddha/bādhita.
- Guard: the classifier's taxonomy MUST be a constructor parameter
  (A-mode vs C-mode minimum). Name-reuse (savyabhicāra, viruddha) does NOT
  license content-reuse: A-savyabhicāra (Maitra-child accidentalism) vs
  C-savyabhicāra (vipakṣa-vṛtti + subdivisions) stay distinct rows.
- Prakaraṇasama/sādhyasama/kālātīta inputs in C-mode: REJECT as
  out-of-taxonomy (do not coerce). Satpratipakṣa/bādhita/asiddha-group
  inputs in A-mode: likewise.

## C-NC3. Inconclusive ≠ Neutralised (Vārttika-internal)

- 1.2.7 Vārttika (VARTTIKA_SUPPORTED): Inconclusive requires the non-finding
  to be known-at-an-admitted-locus; Neutralised is mere double non-finding
  neutralising itself. Collapsing them voids the Vārttika's central
  distinction and its admitted-locus admission rule (D6-relevant).
- Guard: preserve both as separate verdicts in A-mode with the admitted-
  locus condition attached to Inconclusive only.

## C-NC4. Unknown ≠ Neutralised (Vārttika reply preserved)

- 1.2.7 Vārttika objection+reply (VARTTIKA_SUPPORTED): Unknown =
  as-unknown-as-probandum; Neutralised = doubt/suspense-generating.
- Guard: asiddha-paths and prakaraṇasama-paths must diverge in A-mode
  reporting (cf. D p.116's distinct blocking routes in C-mode — parallel
  noted, not equated: CROSS_STRATUM_SYNTHESIS).

## C-NC5. Asādhāraṇa ≠ anupasaṃhārin (TS-internal, carried forward)

- TS §§20–21 (TARKASANGRAHA_SUPPORTED): universal-absence-elsewhere vs
  universal-pakṣa/no-dṛṣṭānta. Baseline check 8 conflates them (D4).
- Guard: any future check must test "pakṣa == domain" separately from
  "hetu unique to pakṣa" (domain model required — DEFERRED if absent).

## C-NC6. Engineering superclasses allowed — with provenance

- IF a common superclass (e.g. `InconclusiveOutcome`) becomes useful, it
  MUST be labelled ENGINEERING_ABSTRACTION, carry per-verdict source tags,
  and MUST NOT be cited as a classical category. Superclass membership
  changes NO verdict semantics (C-NC1–C5 still enforced at the leaf level).

## C-NC7. Gold-label hygiene for evaluation sets

- Cross-stratum evaluation MUST NOT mix A-mode and C-mode gold labels in one
  undifferentiated column. Mixed evaluation is a documented category error,
  not a result.
