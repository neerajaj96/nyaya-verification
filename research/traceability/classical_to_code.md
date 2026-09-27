# Classical Text ↔ Code Traceability

Rule: every row maps CODE CONCEPT → implementation → documentation → classical
source → exact passage → interpretation, then classifies the mapping.
No silent equivalence. "Newer" = Nyāya Engine checkout (superset); where the
older Tarka AI snapshot differs, it is noted.

Scale: DIRECTLY SUPPORTED / SUPPORTED WITH INTERPRETATION / WEAKLY SUPPORTED /
NOT ESTABLISHED / CONFLICTING / UNKNOWN.

## T1. Vyāpti as stored rule (hetu→sādhya + sapakṣa/vipakṣa/kind/upādhi)

- Code: `vyapti.py :: Vyapti(hetu, sadhya, sapaksha, vipaksha, kind, upadhi)`
  + `VyaptiDatabase` keyed `(hetu,sadhya)`; `engine.teach_vyapti/add_counterexample`.
- Docs: README "major premise / general rule"; `vyapti.py` docstring cites
  TS §44 smoke/fire.
- Source: TS §4 `यत्र यत्र धूमस्तत्र तत्राग्निरिति साहचर्यनियमो व्याप्तिः` + D
  `हेतुसमानाधिकरणात्यन्ताभावाप्रतियोगिसाध्यसामानाधिकरण्यं व्याप्तिः`
  (P1 PDF ~91 / printed 91; P2 §44).
- Interpretation: the code stores the *relata* (hetu, sādhya) and the stock
  example roles correctly, but stores the concomitance itself as an opaque
  taught pair, whereas the source defines it as quantified same-locus
  co-occurrence with an absence-guard.
- Verdict: **SUPPORTED WITH INTERPRETATION** (relata + example slots match;
  logical content of vyāpti is assumed, not represented).

## T2. Parāmarśa as hetu-presence + vyāpti recall

- Code: `engine.infer` requires `world.has_property(paksha,hetu)` truthy
  (checks 1–2) plus a live `vyapti_db.get(hetu,sadhya)` (check 6);
  `Syllogism.svartha_anumana` prints vyāpti-smaraṇa → parāmarśa → anumiti.
- Docs: README workflow steps 1–2 + 6; `syllogism.py` cites §§45–46.
- Source: TS §3 `व्याप्तिविशिष्टपक्षधर्मताज्ञानं परामर्शः` + D
  `व्याप्तिविषयकं यत्पक्षधर्मताज्ञानं स परामर्शः` (P1 PDF ~90).
- Interpretation: the code enforces the two *components* across two stores but
  never forms the single fused cognition the Dīpikā requires
  (*vyāptiviṣayaka pakṣadharmatājñāna*); the svartha trace *prints* the fusion
  without *checking* it (e.g. no check that the recalled vyāpti is the one
  qualifying the hetu-cognition, no pakṣatā gate).
- Verdict: **SUPPORTED WITH INTERPRETATION** (components present; fusion +
  pakṣatā absent — see C1).

## T3. Pañcāvayava five-slot proof object

- Code: `Syllogism.parartha_anumana` — pratijñā / hetu / udāharaṇa
  ("Whatever has hetu has sādhya, as in sapakṣa") / upanaya ("has hetu, which
  is pervaded by sādhya") / nigamana ("Therefore…").
- Docs: README "five-membered syllogism"; `syllogism.py` cites §46.
- Source: TS §9 full pañcāvayava sūtra + per-member D glosses and prayojanas
  (P1 PDF ~95–97 / printed 96–97; P2 §46).
- Interpretation: slot count, order, stock mountain/hearth content, and the
  upanaya-as-qualified-restatement all match; the code does not enforce the
  D's grammatical/semantic refinements (ablative hetu, udāharaṇa must state
  vyāpti, nigamana shows abādhitattva) nor the per-member prayojanas.
- Verdict: **DIRECTLY SUPPORTED** for structure; **SUPPORTED WITH
  INTERPRETATION** for member semantics (minor gaps, no contradictions).

## T4. Pakṣa / sapakṣa / vipakṣa

- Code: pakṣa = `WorldModel` locus (existence check); sapakṣa = optional
  string on `Vyapti` (None ⇒ asādhāraṇa); vipakṣa = stored-but-unread field;
  `add_counterexample(instance)` appends a string.
- Docs: `engine` docstrings ("paksha/sapaksha/vipaksha instances").
- Source: TS §§14–16 (`सन्दिग्धसाध्यवान् पक्षः` / `निश्चितसाध्यवान् सपक्षः` /
  `निश्चितसाध्याऽभाववान् विपक्षः`) + §2 pakṣatā refinement + §14 D (manana and
  perceived-fire objections) (P1 PDF ~103–104).
- Interpretation: sapakṣa-as-string matches the "hearth" role loosely, but the
  code drops the source's epistemic qualifiers (*sandigdha* vs. *niścita*),
  the pakṣatā substratum doctrine, and any use of vipakṣa; counterexamples are
  free strings, not ascertained vipakṣa loci.
- Verdict: **SUPPORTED WITH INTERPRETATION** for pakṣa/sapakṣa roles;
  **WEAKLY SUPPORTED** for vipakṣa (field exists, semantics unused);
  pakṣatā mapping is **NOT ESTABLISHED** (see C1).

## T5. Anvaya / vyatireka (both concomitances, kevala cases)

- Code: `Vyapti.kind` in {"anvaya","vyatireka","both"} (default "anvaya");
  never branched on in `diagnose`, `infer`, tests, or demo.
- Docs: `vyapti.py` docstring names the three kinds; nothing else.
- Source: TS §§11–13 liṅga-traividhya with full anvaya-vyāpti + vyatireka-
  vyāpti formulae, kevalānvayi (jar/nameable, §12) and kevalavyatireki
  (earth/odour, §13) proofs, and the no-dṛṣṭānta lemmas (P1 PDF ~99–100).
- Interpretation: the code *names* the distinction but implements only the
  anvaya-violation half (counterexample = hetu-present/sādhya-absent); it
  cannot represent, check, or generate vyatireka-vyāpti or either kevala case.
- Verdict: **WEAKLY SUPPORTED** (vocabulary without mechanism); kevala
  handling **NOT ESTABLISHED**.

## T6. Hetvābhāsa fivefold taxonomy + stock examples

- Code: 9-check `diagnose` with classical messages (prameyatva/lake,
  śabdatva, kṛtakatva, śrāvaṇatva/kāryatva, gagana-aravinda, cākṣuṣatva,
  ārdrendhana, vahni-anuṣṇa).
- Docs: README maps checks to TS §§52–57; `fallacy.py` docstring same.
- Source: TS §§17–28 full taxonomy with identical stock examples (P1 PDF
  ~105–116). Names line up 1:1 (sādhāraṇa/asādhāraṇa/anupasaṃhārin under
  savyabhicāra; āśraya/svarūpa/vyāpyatva under asiddha; viruddha;
  satpratipakṣa; bādhita).
- Interpretation: the taxonomy and examples are faithfully carried over; the
  *blocking theory* (bādhita/satpratipakṣa block anumiti directly, the rest
  block parāmarśa — P1 p. 116) is not reflected in the linear reject order,
  and anupasaṃhārin has no dedicated check (see C4).
- Verdict: **DIRECTLY SUPPORTED** for taxonomy + examples;
  **SUPPORTED WITH INTERPRETATION** for diagnostic mechanics.

## T7. Upādhi / vyāpyatvāsiddha

- Code: `Vyapti.upadhi` string; check 9 rejects whenever truthy, with the
  ārdrendhana message.
- Docs: README step 8; `engine` CLI prompts for upādhi.
- Source: TS §27 full upādhi definition (sādhya-pervading ∧ hetu-non-
  pervading, iron-ball counterexample) (P1 PDF ~111–112).
- Interpretation: stock example and gate position match, but the code's
  "any non-empty string blocks" is far stronger than the source, which
  requires *proving* the double-pervasion fact about the candidate upādhi.
- Verdict: **SUPPORTED WITH INTERPRETATION** (example right, criterion
  thinned to a flag).

## T8. Bādhita (pramāṇa-strength-gated defeat)

- Code: check 3 — `not-sadhya` recorded `True` with source strength ≥ anumāna
  (table: pratyakṣa 4 > śabda 3 > upamāna 2 > anumāna 1 > assumed 0).
- Docs: README step 3.
- Source: TS §28 (`प्रमाणान्तरेण निश्चितः`, tactile-perception example) (P1
  PDF ~115); blocking-theory note p. 116.
- Interpretation: "another pramāṇa ascertains sādhya-absence" and the worked
  example match; the 4>3>2>1>0 numeric ranking is an engineering posit with
  no cited sūtra/Dīpikā basis (the source says *pramāṇāntara*, not a total
  order — and whether anumāna-vs-anumāna or śabda-vs-anumāna defeat holds is
  exactly what §55/§28 discussion complicates).
- Verdict: **SUPPORTED WITH INTERPRETATION** for the defeat shape;
  **NOT ESTABLISHED** for the numeric strength table (see C2).

## T9. Viruddha / satpratipakṣa as vyāpti-DB scans

- Code: check 4 (live `vyapti(hetu→not-sadhya)`) and check 5 (any other live
  `vyapti(h2→not-sadhya)` with h2 present on pakṣa).
- Docs: README steps 4–5.
- Source: TS §22 (`साध्याभावव्याप्तो हेतुः`) and §23
  (`साध्याभावसाधकं हेत्वन्तरं विद्यते`) with the sound-eternality stock cases
  (P1 PDF ~108–109).
- Interpretation: the DB-scan operationalization is a reasonable rendering of
  "pervaded by absence" / "another proving hetu exists", but the source
  hem: viruddha needs the *vyāpti* hetu→sādhyābhāva (not just a stored row),
  and satpratipakṣa needs *equal strength* (*sat* — balanced) opposing
  reasons, which the code never compares (any stored row suffices).
- Verdict: **SUPPORTED WITH INTERPRETATION** (both; satpratipakṣa's *samatva*
  dropped — see C3).

## T10. Savyabhicāra subtypes (sādhāraṇa / asādhāraṇa / anupasaṃhārin)

- Code: check 7 (broken vyāpti via `counterexamples`) / check 8
  (`sapaksha is None`) / (no anupasaṃhārin check).
- Docs: README steps 7–8.
- Source: TS §§18–21 (P1 PDF ~105–108).
- Interpretation: sādhāraṇa and asādhāraṇa map onto the sūtras' definitions
  closely (presence-where-absent; only-in-pakṣa); anupasaṃhārin
  (*anvayavyatirekadṛṣṭāntarahita*, "everything is pakṣa so no example")
  has no code counterpart — `sapaksha=None` fires for it too, conflating two
  distinct defects.
- Verdict: sādhāraṇa **DIRECTLY SUPPORTED**; asādhāraṇa **SUPPORTED WITH
  INTERPRETATION** (no sapakṣa/vipakṣa-absence scan, just None-test);
  anupasaṃhārin **NOT ESTABLISHED** (see C4).

## T11. Asiddha subtypes (āśraya / svarūpa / vyāpyatva)

- Code: checks 1 (locus unknown), 2 (hetu False / hetu None), 9 (upādhi flag).
- Docs: README steps 1–2 + 8; docstring cites §56.
- Source: TS §§24–27 (sky-lotus; sound-visible; sopādhika) (P1 PDF ~109–112).
- Interpretation: examples and gate positions match; the code's
  "None = unverified = defect" rendering of svarūpa is broader than the
  sūtra's occurrence-failure (`शब्दे चाक्षुषत्वं नास्ति`) — absence of
  information is treated as asiddha, which the source does not state; the
  vyāpyatva thinning is as in T7.
- Verdict: āśrayasiddha **DIRECTLY SUPPORTED**; svarūpasiddha **SUPPORTED
  WITH INTERPRETATION** (absent-case exact; unverified-case extension);
  vyāpyatvāsiddha per T7.

## T12. Vyāpti-asiddha ("no rule on record" refusal)

- Code: check 6 rejects when `vyapti_db.get(hetu,sadhya)` is None
  ("refuses to hallucinate").
- Docs: README firewall story.
- Source: no TS sūtra states "absence of a taught row is a hetvābhāsa";
  the fivefold list (§17) is exhaustive without it. The *function* (blocking
  inference without vyāpti) follows trivially from §§3–4 (no vyāpti ⇒ no
  parāmarśa ⇒ no anumiti), but the reification as a sixth named defect is
  the engineers', not the text's.
- Verdict: **SUPPORTED WITH INTERPRETATION** as a corollary-gate;
  **NOT** a classical hetvābhāsa (do not cite it as §-backed).

## T13. Pramāṇa→ML mapping (NLP→anumāna-input, embeddings→upamāna, RAG→śabda, CV→pratyakṣa, Apriori→vyāptigraha)

- Code: five bridges, all proposal-only behind `diagnose`.
- Docs: README mapping table + firewall principle.
- Source: pramāṇa definitions live outside the extracted inference run
  (pratyakṣa §42; upamāna §58; śabda §59 — P2 printed pp. 211/327/329);
  vyāptigraha = bhūyodarśana + vyabhicāra-absence + tarka + sāmānya (§7 D).
  The *firewall idea* (scrutiny before acceptance) echoes the Dīpikā's
  blocking theory (p. 116) at motto level only.
- Interpretation: the mapping is an avowed modern design analogy, not a
  textual derivation; the Apriori leg additionally drops tarka/sāmānya (see
  G §11).
- Verdict: **NOT ESTABLISHED** as classical claims (engineering analogies;
  keep labelled as such). The firewall *slogan* is **WEAKLY SUPPORTED** at
  best.

## T14. Ontology seeds (9 dravya / 24 guṇa / 5 karman + § refs)

- Code: `ontology_data.py` + `padartha.py` with per-entry `section=`.
- Docs: README "Section-referenced ontology".
- Source: TS §§2–9 + detail §§10–33 (dravya lakṣaṇas, guṇa residences).
  Spot-checks pass (Pṛthvī-gandhavatī §10; Ap-śīta §11; Tejas-uṣṇa §12;
  Vāyu anumeya §13; Ākāśa-śabda §14; Kāla/Dik §15–16; Ātman jñānādhikaraṇa
  §17; Manas aṇu §18; rūpa→pṛthvī/ap/tejas §19 etc.).
- Interpretation: seeds and § numbers are broadly right, but the 24-guṇa
  table compresses residences (several `None`→all-dravyas fallbacks) and the
  newer snapshot's claim of exact "sub-sections 19–33" mapping was not
  exhaustively verified here.
- Verdict: **SUPPORTED WITH INTERPRETATION** (spot-verified; full
  cell-by-cell audit deferred — see INITIAL_FINDINGS §8).

## T15. Corpus-as-Āpta-śabda (1,121 chunks, threshold 0.22, `ground_term`)

- Code: `tarka_corpus.py` + `data/*.json` + `RAGShabda(0.22)`.
- Docs: README "Full-text grounding", "Tuned RAG threshold".
- Source: śabda = *āpta-vākya* (credible-speaker utterance; TS §59); the
  bundled text is the Athalye/Bodas edition of TS+D+NB (a modern critical
  edition, not an *āpta* in the classical sense).
- Interpretation: treating a paragraph-chunked OCR corpus + BoW cosine ≥ 0.22
  as an *āpta* test is an engineering stipulation; no sūtra/Dīpikā passage
  supports thresholds, chunking, or edition-as-āpta.
- Verdict: **NOT ESTABLISHED** as a classical representation (useful
  retrieval tooling; not a pramāṇa formalization).
