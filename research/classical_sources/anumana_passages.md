# Classical Material Extraction — Inference & Fallacy Passages

Method: systematic string search over both `pdftotext -layout` dumps for the
term list in the brief (roman IAST + plain + Devanāgarī, allowing OCR spacing
variants in PDF 2). Every passage below was read in context; Sanskrit and
translation are quoted from the PDFs, not reconstructed. PDF pages are
approximate (±1). Printed references are as printed in each edition
(PDF 1 = running translation pages 88–116; PDF 2 = Note sections §§42–59,
printed pp. 211–329).

Abbreviations: P1 = PDF 1 (Virupakshananda, 1994); P2 = PDF 2 (Athalye/Bodas,
1930). TS = Tarkasaṃgraha mūla; D = Annambhaṭṭa's Dīpikā; NB = Govardhana's
Nyāya-Bodhinī (P2 only); N = Athalye/Bodas Notes (P2).

Corpus-scale hit counts (raw, unsplit forms only — true counts are higher,
especially in P2 where Devanāgarī spacing fragments words):

| Term | P1 roman | P1 Devanāgarī | P2 roman | P2 Devanāgarī |
|---|---|---|---|---|
| anumāna / anumiti | 8 / 14 | अनुमान 9 / अनुमिति 7 | 1 / 2 | अनुमान 67 / अनुमिति 81 |
| pramāṇa | 3 | प्रमाण 39 | 1 | प्रमाण 81 |
| pakṣa / sādhya / hetu | 21 / 24 / 44 | पक्ष 36 / साध्य 40 / हेतु 34 | 3 / 0 / 5 | पक्ष 417 / साध्य 303 / हेतु 308 |
| vyāpti / vyāptigraha | 40 | व्याप्ति 78 / व्याप्तिग्रह 1 | 10 | व्याप्ति 348 / व्याप्तिग्रह 3 |
| anvaya / vyatireka | 15 / 10 | अन्वय 12 / व्यतिरेक 20 | 3 / 2 | अन्वय 51 / व्यतिरेक 90 |
| dṛṣṭānta / udāharaṇa / upanaya / nigamana | — / 1 / 2 / 1 | दृष्टान्त 7 / उदाहरण 2 / उपनय 2 / निगमन 4 | — / — / 1 / 1 | दृष्टान्त 73 / उदाहरण 41 / उपनय 23 / निगमन 19 |
| pañcāvayava | 1 | 0 (पश्चावयवः spelling) | 1 | 1+ |
| hetvābhāsa | 3 | हेत्वाभास 2 | 0 | हेत्वाभास 22 |
| asiddha / viruddha | 9 / 15 | असिद्ध 3 / विरुद्ध 6 | 4 / 1 | असिद्ध 35 / विरुद्ध 34 |
| savyabhicāra / anaikāntika | 6 / 2 | सव्यभिचार 4 / अनैकान्तिक 2 | 1 / 1 | सव्यभिचार 31 / अनैकान्तिक ~30 |
| satpratipakṣa / bādhita | 0 / 3 | सत्प्रतिपक्ष 4 / बाधित 6 | 1 / 1 | सत्प्रतिपक्ष 26 / बाधित 38 |
| parāmarśa / liṅga / pratijñā | 14 / 26 / — | परामर्श 20 / लिङ्ग 15 / प्रतिज्ञा 8 | — / 2 / 1 | परामर्श 136 / लिङ्ग 88 / प्रतिज्ञा 44 |
| upādhi | 18 | उपाधि 6 | 6 | उपाधि 59 |

---

## 1. anumāna (inference) and anumiti (inferential cognition)

**P1, PDF p. ~88, printed p. 88 (SECTION V, §§1–2).**
- Exact Sanskrit (mūla): `अनुमितिकरणमनुमानम् ॥ १ ॥` ; `परामर्शजन्यं ज्ञानमनुमितिः ॥ २ ॥`
- OCR text: as above (clean).
- Transliteration: *anumitikaraṇam anumānam*; *parāmarśajanyaṃ jñānam anumitiḥ*.
- Translation (P1): "1. Inference is the special cause of inferential
  knowledge." / "2. Inferential knowledge is the knowledge born of
  subsumptive reflection."
- Commentary (D, P1): defines anumāna via *karaṇa* (special/instrumental
  cause); anticipates the *saṃśayottara-pratyakṣa* objection (post-or-man
  doubt followed by perception "this is a man" after parāmarśa about hands)
  and replies by building **pakṣatā** into the definition: only
  *pakṣatā-sahakṛta-parāmarśa-janya* cognition counts as anumiti.
  Pakṣatā = *siṣādhayiṣāviraha-viśiṣṭa-siddhyabhāvaḥ* (absence of ascertainment
  of the sādhya, qualified by absence of desire to prove the already proved);
  established sādhya blocks (*pratibandhikā*) inference, with the
  mani/uttejaka-mani analogy for enabling/triggering absences.
- Source-level claim: inference is not any parāmarśa-following cognition; it
  is the *karaṇa*-type cause, and anumiti is parāmarśa-born cognition **under
  pakṣatā**.
- Computational relevance: any formalization must represent pakṣatā
  (doubt + absence of prior proof + desire to infer) as a precondition, not
  just hetu-presence; perception-after-doubt is explicitly *excluded* from
  anumiti by the source.
- Uncertainty: low on the sūtras; medium on the exact scope of
  *siṣādhayiṣā* (desire-to-infer-the-unproved vs. desire-to-infer-at-all) —
  the Dīpikā allows inference of even the perceived given the desire
  ("anuminiṣyām… anumitidarśanāt").

**P2, PDF p. ~111, printed §44 (p. 233 Notes; mūla p. 35).**
Same sūtras verbatim (`अनुमितिकरणमनुमानम् । परामर्शजन्यं ज्ञानमनुमितिः`),
with D + NB. NB adds the karaṇa-vyāpāra-phala schema: *vyāptijñāna* is karaṇa,
*parāmarśa* is vyāpāra (operation), *anumiti* is phala — i.e. vyāpti-cognition
is the instrumental cause operating *through* parāmarśa. Confirms P1 reading.

## 2. parāmarśa, pakṣadharmatā

**P1, PDF p. ~90, printed pp. 90–91 (§3, §5).**
- Sanskrit: `व्याप्तिविशिष्टपक्षधर्मताज्ञानं परामर्शः। यथा वह्निव्याप्यधूमवानयं पर्वत इति ज्ञानं परामर्शः। तज्जन्यं पर्वतो वह्निमानिति ज्ञानमनुमितिः ॥ ३ ॥`
  + `व्याप्यस्य पर्वतादिवृत्तित्वं पक्षधर्मता ॥ ५ ॥`
- Transliteration: *vyāptiviśiṣṭapakṣadharmatājñānaṃ parāmarśaḥ …
  vahnivyāpyadhūmavān ayaṃ parvataḥ … tajjanyaṃ parvato vahnimān …*;
  *vyāpyasya parvatādivṛttitvaṃ pakṣadharmatā*.
- Translation (P1): "Subsumptive reflection is the knowledge of reason
  existing in the subject accompanied by invariable concomitance (of sādhya),
  e.g. … this mountain has smoke which is invariably pervaded by fire …
  the cognition … the mountain is fiery is the inferential knowledge."
  "The presence of an invariably concomitant thing in an object like a
  mountain makes it [pakṣadharmatā]."
- D: *vyāptiviṣayakaṃ yat pakṣadharmatājñānaṃ sa parāmarśaḥ* — parāmarśa is
  pakṣadharmatā-cognition *whose object includes vyāpti*.
- Claims: (a) parāmarśa has two fused components — hetu-in-pakṣa +
  vyāpti-awareness; (b) pakṣadharmatā is the *vṛttitva* (occurrence) of the
  vyāpya (pervaded hetu) on the pakṣa; (c) the stock example is fixed:
  mountain/smoke/fire.
- Computational relevance: parāmarśa is a *conjunction* node
  (hetu(pakṣa) ∧ vyāpti(hetu→sādhya) co-present in one cognition), not a
  two-step rule application; pakṣadharmatā is occurrence, not mere
  set-membership.
- Uncertainty: low.

## 3. vyāpti — definition and full formula

**P1, PDF p. ~91, printed p. 91 (§4).**
- Sanskrit: `यत्र यत्र धूमस्तत्र तत्राग्निरिति साहचर्यनियमो व्याप्तिः ॥ ४ ॥`
- Transliteration: *yatra yatra dhūmas tatra tatrāgnir iti
  sāhacaryaniyamo vyāptiḥ*.
- Translation: "Invariable concomitance is the certainty of co-existence
  like, wherever there is smoke there is fire."
- D (P1) full definition: `हेतुसमानाधिकरणात्यन्ताभावाप्रतियोगिसाध्यसामानाधिकरण्यं व्याप्तिरित्यर्थः`
  (*hetusamānādhikaraṇātyantābhāvāpratiyogi-sādhyasāmānādhikaraṇyaṃ vyāptiḥ*):
  vyāpti = co-occurrence with the sādhya **which is not the counter-entity
  (pratiyogin) of an absolute negation co-located with the hetu**.
  Gloss: *sāhacarya = sāmānādhikaraṇya* (same-substratum co-existence);
  *niyama* = invariability.
- Claims: (a) illustrative form is universal-affirmative co-location;
  (b) technical form is double-negation-proofed co-occurrence
  (hetu-locus must lack *atyantābhāva* of sādhya).
- Computational relevance: the Dīpikā definition is a **universally quantified
  same-locus co-occurrence with an absence-of-absence guard** — closest
  classical anchor for any "search for hetu ∧ ¬sādhya" check, but framed as
  *sāmānādhikaraṇya + atyantābhāva-apratiyogitva*, not as database row scan
  (see `vyapti_complete.md` for the support verdict).
- Uncertainty: low on wording; high on how to operationalize
  *sāmānādhikaraṇya* (substratum identity) computationally.

**P2** has the identical sūtra + D definition at PDF p. ~111 (mūla p. 35, §44
Notes p. 233+), confirming stability across editions.

## 4. vyāptigraha (grasping vyāpti): bhūyodarśana + tarka + sāmānya-pratyāsatti

**P1, PDF pp. ~92–94, printed pp. 93–94 (§7 svartha + D).**
- Sanskrit (mūla §7): `तत्र स्वार्थं स्वानुमितिहेतुः, तथाहि, स्वयमेव भूयोदर्शनन यत्र यत्र धूमस्तत्र तत्राग्निरिति महानसादौ व्याप्तिं गृहीत्वा …`
  (*svayam eva bhūyodarśanena … mahānasādau vyāptiṃ gṛhītvā* — having grasped
  vyāpti in kitchen etc. by repeated observation oneself).
- D objections/replies (P1, pp. 93–94):
  1. *Pārthivatva/lohalekhyatva vs. vajra* counterexample: a hundred
     co-observations still admit *vyabhicāra* (diamond is earth yet not
     scratchable). Reply: *vyabhicārajñānaviraha-sahakṛta-sahacārajñānasya
     vyāptigrāhakatvāt* — what grasps vyāpti is co-observation **aided by
     absence of vyabhicāra-cognition** (absence of both *niścaya* and
     *śaṅkā* of counterexamples); that absence is established sometimes by
     *tarka*, sometimes *svataḥ* (self-evidently).
     For smoke/fire the remover is *kāryakāraṇabhāva-prasaṅga-lakṣaṇas tarka*
     (if smoke without fire, the effect–cause relation breaks).
  2. *Asannikarṣa* objection: not all smokes/fires are perceived. Reply:
     *vahni-tva/dhūmatva-rūpa-sāmānya-pratyāsattyā sakala-vahni-dhūma-jñāna-
     sambhavāt* — generic attributes (*sāmānya*) mediate cognition of all
     instances (sāmānya-pratyāsatti).
- Claims: vyāptigraha = repeated co-observation **+** no-counterexample
  condition **+** (when needed) tarka **+** universal-mediated extension.
- Computational relevance: directly licenses a two-component learner
  (frequency + defeater-absence) with an optional consistency/tarka check and
  a class-level generalization step; pure support/confidence thresholds alone
  omit the tarka and sāmānya components.
- Uncertainty: medium — the exact logic of the smoke/fire *tarka* is
  compressed; P2 Notes expand it (see vyapti_complete.md).

## 5. anvaya / vyatireka, liṅga-traividhya, dṛṣṭānta

**P1, PDF pp. ~99–100, printed pp. 99–100 (§§11–13).**
- Sanskrit §11: `लिङ्गं त्रिविधम् । अन्वयव्यतिरेकि, केवलान्वयि, केवलव्यतिरेकि चेति । अन्वयेन व्यतिरेकेण च व्याप्तिमदन्वयव्यतिरेकि । यथा वह्नौ साध्ये धूमवत्त्वम् । यत्र धूमस्तत्राग्निर्यथा महानस इत्यन्वयव्याप्तिः । यत्र वह्निर्नास्ति तत्र धूमोऽपि नास्ति यथा महाहृद इति व्यतिरेकव्याप्तिः ॥ ११ ॥`
- Translation: threefold liṅga — (a) anvaya-vyatireki (both concomitances;
  smoke→fire with hearth/lake examples); (b) kevalānvayi (§12:
  `अन्वयमात्रव्याप्तिकं केवलान्वयि । यथा घटः अभिधेयः प्रमेयत्वात् पटवत् ।
  अत्र प्रमेयत्वाभिधेयत्वयोः व्यतिरेकव्याप्तिर्नास्ति, सर्वस्यापि प्रमेयत्वात्
  अभिधेयत्वाच्च` — jar is nameable because knowable; no vyatireka-vyāpti
  since everything is knowable/nameable); (c) kevalavyatireki (§13:
  `व्यतिरेकमात्रव्याप्तिकं केवलव्यतिरेकि, यथा पृथिवीतरेभ्यो भिद्यते
  गन्धवत्त्वात् । यदितरेभ्यो न भिद्यते न तद्गन्धवत् यथा जलम् … अत्र
  यद्गन्धवत् तदितरभिन्नम् इत्यन्वयदृष्टान्तो नास्ति, पृथिवीमात्रस्य पक्षत्वात्`
  — earth differs from others because odorous; no anvaya-dṛṣṭānta since the
  whole of earth is pakṣa).
- D: *hetusādhyayoḥ aptir anvayavyāptiḥ, tadabhāvayor aptir vyatirekavyāptiḥ*.
- Claims: vyāpti is bivalent (anvaya = hetu–sādhya co-presence;
  vyatireka = absence–absence); some valid reasons have only one; dṛṣṭānta
  (hearth/lake, cloth, water) instantiates the concomitance; kevala cases
  prove vyatireka-only/anvaya-only reasons are legitimate.
- Computational relevance: a complete checker needs **both** concomitance
  directions and must handle kevala edge cases (universal pakṣa ⇒ no
  dṛṣṭānta available — cf. anupasamhārin below); "hetu ∧ ¬sādhya" search
  covers only the anvaya-violation half.
- Uncertainty: low on taxonomy; medium on whether kevalavyatireki's
  `na tathā … tasmān na tathā` double-negation inference pattern is fully
  captured by the five-membered template.

## 6. svārtha / parārtha, pañcāvayava (pratijñā–hetu–udāharaṇa–upanaya–nigamana)

**P1, PDF pp. ~92–97, printed pp. 92–97 (§§6–9).**
- Sanskrit §6: `अनुमानं द्विविधं स्वार्थं परार्थं च ॥ ६ ॥`
- Svārtha (§7, quoted above): self-sequence bhūyodarśana → vyāptismaraṇa
  (`यत्र यत्र धूमस्तत्र तत्राग्निः इति`) → `वह्निव्याप्यधूमवानयं पर्वतः`
  (liṅgaparāmarśa) → `पर्वतो वह्निमान्` (anumiti).
- Parārtha (§8): `यत्तु स्वयं धूमादग्निमनुमाय परं प्रतिबोधयितुं पञ्चावयववाक्यं प्रयुज्यते तत् परार्थानुमानम् । यथा पर्वतो वह्निमान्, धूमवत्त्वात्, यो यो धूमवान् स वह्निमान् यथा महानसः, तथा चायम्, तस्मात्तथेति । अनेन प्रतिपादितात् लिङ्गात् परोऽप्यग्निं प्रतिपद्यते ॥ ८ ॥`
- Pañcāvayava (§9): `प्रतिज्ञा हेतु उदाहरण उपनय निगमनानि पञ्चावयवाः ।
  पर्वतो वह्निमानिति प्रतिज्ञा । धूमवत्त्वात् इति हेतुः । यो यो धूमवान् स वह्निमान् यथा महानस इत्युदाहरणम् । तथा चायमिति उपनयः । तस्मात्तथेति निगमनम् ॥ ९ ॥`
- D functional glosses (§9): *sādhyavattayā pakṣavacanaṃ pratijñā*
  (proposition = pakṣa stated as possessing sādhya); *pañcamyantaṃ
  liṅgapratipādakaṃ hetuḥ* (reason = mark stated in ablative);
  *vyāptipratipādakam udāharaṇam*; *vyāptiviśiṣṭaliṅgapratipādakaṃ vacanam
  upanayaḥ*; *hetusādhyavattayā pakṣapratipādakaṃ vacanaṃ nigamanam*.
  Prayojanas: pratijñā → *sādhyasaṃśaya-jñāna*; hetu → pakṣadharmatā-jñāna;
  udāharaṇa → vyāpti-jñāna; upanaya → pakṣadharmatā-jñāna (as qualified);
  nigamana → pakṣe sādhyasattā-jñāna (with *abādhitattvādikaṃ
  niganamaprayojanam*).
- Claims: parārtha is not a different logic but the *verbal demonstration*
  (pañcāvayava-vākya) causing another's cognition *through the expounded
  liṅga*; each member has a distinct epistemic job.
- Computational relevance: fixes the five-slot proof object and its
  per-slot semantics (udāharaṇa must state vyāpti + dṛṣṭānta; upanaya must
  restate liṅga *as vyāpti-qualified*; hetu should be ablative-marked).
- Uncertainty: low.

## 7. pakṣa / sapakṣa / vipakṣa

**P1, PDF pp. ~103–104, printed pp. 103–104 (§§14–16).**
- Sanskrit: §14 `सन्दिग्धसाध्यवान् पक्षः । यथा धूमवत्त्वे हेतौ पर्वतः ॥ १४ ॥`
  §15 `निश्चितसाध्यवान् सपक्षः, यथा तत्रैव महानसम् ॥ १५ ॥`
  §16 `निश्चितसाध्याऽभाववान् विपक्षः । यथा तत्रैव महाहृदः ॥ १६ ॥`
- Translation: pakṣa = locus where sādhya is *doubted*; sapakṣa = locus where
  sādhya is *ascertained present* (hearth); vipakṣa = locus where sādhya's
  absence is *ascertained* (lake).
- D on §14 handles two avyāpti objections: (a) *manana* after śravaṇa (soul
  already ascertained, no doubt) and (b) inferring even the perceived fire —
  reply: *uktapakṣatāśrayatvasya pakṣalakṣaṇatvāt* (the real definiens is
  being the substratum of pakṣatā as defined in §2, not bare doubt).
- Claims: the doubt-formula is exoteric; the operative notion is pakṣatā
  (siddhyabhāva + siṣādhayiṣā structure). Sapakṣa/vipakṣa require
  *niścita* (ascertained) presence/absence — mere suspicion does not qualify.
- Computational relevance: pakṣa/sapakṣa/vipakṣa are **epistemic statuses**
  (doubted / ascertained-present / ascertained-absent), not bare sets; a
  checker needs a certainty flag per locus-property, and must implement the
  §2 pakṣatā refinement, not just the §14 doubt slogan.
- Uncertainty: low on definitions; medium on *niścaya* threshold (what counts
  as ascertained — perception? proof? stipulation?).

## 8. hetvābhāsa taxonomy (pañca) + full subtype definitions

**P1, PDF pp. ~105–116, printed pp. 105–116 (§§17–28).**
- §17 mūla: `सव्यभिचारविरुद्धसत्प्रतिपक्षासिद्धबाधिताः पञ्च हेत्वाभासाः ॥ १७ ॥`
  (straying, adverse, antithetical, unestablished, stultified).
  D: *anumitipratibandhaka-yathārthajñāna-viṣayatvaṃ hetvābhāsatvam* —
  hetvābhāsa = being the object of veridical cognition that blocks anumiti.
- §18: `सव्यभिचारः अनैकान्तिकः । स त्रिविधः साधारणासाधारणानुपसंहारिभेदात् ॥`
  (savyabhicāra = anaikāntika; threefold).
- §19 sādhāraṇa: `तत्र साध्याभाववद्वृत्तिः साधारणः अनैकान्तिकः, यथा पर्वतो वह्निमान् प्रमेयत्वात् इति । प्रमेयत्वस्य वह्न्यभाववति ह्रदे विद्यमानत्वात् ॥`
  (present where sādhya is absent; mountain-fiery-because-knowable; knowability
  also in the fireless lake).
- §20 asādhāraṇa: `सर्वसपक्षविपक्षव्यावृत्तः पक्षमात्रवृत्तिः असाधारणः । यथा शब्दो नित्यः शब्दत्वात् इति ॥`
  (absent from all sapakṣa and vipakṣa, present only in pakṣa; sound-eternal-
  because-soundness).
- §21 anupasaṃhārin: `अन्वयव्यतिरेकदृष्टान्तरहितोऽनुपसंहारी । यथा सर्वमनित्यं प्रमेयत्वादिति । अत्र सर्वस्यापि पक्षत्वात् दृष्टान्तो नास्ति ॥`
  (no anvaya or vyatireka dṛṣṭānta; everything-non-eternal-because-knowable;
  everything is pakṣa so no example exists).
- §22 viruddha: `साध्याभावव्याप्तो हेतुर्विरुद्धः । यथा शब्दो नित्यः कृतकत्वादिति । कृतकत्वं हि नित्यत्वाभावेनाऽनित्यत्वेन व्याप्तम् ॥`
  (pervaded by sādhya-absence; sound-eternal-because-produced; producedness
  pervades non-eternality).
- §23 satpratipakṣa: `यस्य साध्याभावसाधकं हेत्वन्तरं विद्यते स सत्प्रतिपक्षः । यथा शब्दो नित्यः श्रावणत्वात् शब्दत्ववत् । शब्दोऽनित्यः कार्यत्वात् घटवत् ॥`
  (a second hetu proving sādhya-absence exists; audible→eternal vs.
  product→non-eternal on sound).
- §24 asiddha-traividhya: `असिद्धस्त्रिविधः — आश्रयासिद्धः, स्वरूपासिद्धो व्याप्यत्वासिद्धश्चेति ॥`
- §25 āśrayāsiddha: `आश्रयासिद्धो यथा गगनारविन्दं सुरभि अरविन्दत्वात् सरोजारविन्दवत् । अत्र गगनारविन्दमाश्रयः स च नास्त्येव ॥`
  (sky-lotus fragrant because lotus-like; substratum nonexistent).
- §26 svarūpāsiddha: `स्वरूपासिद्धो यथा शब्दो गुणश्चाक्षुषत्वात् । अत्र चाक्षुषत्वं शब्दे नास्ति शब्दस्य श्रावणत्वात् ॥`
  (sound is a quality because visible; visibility absent in sound).
- §27 vyāpyatvāsiddha/sopādhika (full text in §9 below) — hetu with upādhi.
- §28 bādhita: `यस्य साध्याभावः प्रमाणान्तरेण निश्चितः स बाधितः । यथा वह्निरनुष्णो द्रव्यत्वात् जलवत् । अत्रानुष्णत्वं साध्यं तदभाव उष्णत्वं स्पर्शनप्रत्यक्षेण गृह्यत इति बाधितत्वम् ॥`
  (sādhya-absence ascertained by another pramāṇa; fire-non-hot-because-
  substance; hotness grasped by tactile perception).
- D meta-theory (P1 p. 116, on §28): *bādhasya grāhyābhāva-niścayatvena,
  satpratipakṣasya virodhijñāna-sāmagrītvana sākṣād-anumiti-pratibandhakatvam;
  itareṣāṃ tu parāmarśa-pratibandhakatvam* — bādhita and satpratipakṣa block
  *anumiti directly*; the rest block *parāmarśa*. Within the latter:
  sādhāraṇa via *avyabhicārābhāva-rūpatayā*, viruddha via
  *sāmānādhikaraṇyābhāvatayā*, vyāpyatvāsiddha via *viśiṣṭavyāptyabhāvatayā*,
  asādhāraṇa/anupasaṃhārin via *vyāptisaṃśayādhāyakatvena* (doubt-raising),
  āśrayāsiddha/svarūpāsiddha via *pakṣadharmatājñāna-pratibandhakatvam*;
  *upādhis tu vyabhicārajñānadvārā vyāptijñānapratibandhakaḥ*.
- P2 confirms each subtype (vyāpti 348 hits; hetvābhāsa 22; §§52–57 at
  printed pp. 293–315; satpratipakṣa 26, bādhita 38 in Devanāgarī).
- Computational relevance: fixes the canonical five (+ sub-varieties:
  3 savyabhicāra + 3 asiddha = 9 checkable conditions in the code's terms)
  with exact stock examples and the two-level blocking theory
  (anumiti-blockers vs. parāmarśa-blockers).
- Uncertainty: low on definitions/examples; medium on mapping the Dīpikā's
  blocking-mechanism taxonomy onto a linear check order.

## 9. upādhi (adventitious condition) and vyāpyatvāsiddha

**P1, PDF p. ~111–112, printed pp. 111–112 (§27).**
- Sanskrit: `सोपाधिको हेतुः व्याप्यत्वासिद्धः । साध्यव्यापकत्वे सति साधनाव्यापकत्वं उपाधिः । साध्यसमानाधिकरणात्यन्ताभावाप्रतियोगित्वं साध्यव्यापकत्वम् । साधनवन्निष्ठात्यन्ताभावप्रतियोगित्वं साधनाव्यापकत्वम् । पर्वतो धूमवान् वह्निमत्त्वादित्यत्र आर्द्रेन्धनसंयोग उपाधिः । तथाहि । यत्र धूमस्तत्रार्द्रेन्धनसंयोग इति साध्यव्यापकता । यत्र वह्निस्तत्रार्द्रेन्धनसंयोगो नास्ति अयोगोलके आर्द्रेन्धनसंयोगाभावादिति साधनाव्यापकता । एवं साध्यव्यापकत्वे सति साधनाव्यापकत्वादार्द्रेन्धनसंयोग उपाधिः । सोपाधिकत्वात् वह्निमत्त्वं व्याप्यत्वासिद्धम् ॥ २७ ॥`
- Translation (P1): sopādhika hetu = vyāpyatvāsiddha; upādhi = pervading the
  sādhya while not pervading the sādhana (hetu); stock case mountain-smoky-
  because-fiery with *ārdrendhana-saṃyoga* (contact with wet fuel): wherever
  smoke there wet-fuel-contact (sādhya-vyāpakatā); but where fire there need
  not be wet-fuel-contact (red-hot iron ball lacks it) (sādhana-avyāpakatā).
- Claims: upādhi has a precise double-quantifier definition in the same
  atyantābhāva idiom as vyāpti; the hetu→sādhya here is fire→smoke (reverse
  of the §3 example), showing vyāpti is direction-sensitive.
- Computational relevance: upādhi is **not** "any hidden confounder" — it is
  the specific (sādhya-pervading ∧ hetu-non-pervading) property; detection
  requires exhibiting such a property with the iron-ball counterexample.
- Uncertainty: low.

## 10. udāharaṇa / dṛṣṭānta, upanaya, nigamana (member semantics)

Covered in §6 above (§9 sūtra + D glosses + prayojanas). Supplementary:
- Udāharaṇa must state vyāpti (*vyāptipratipādakam*), standardly with dṛṣṭānta
  (`यो यो धूमवान् स वह्निमान् यथा महानसः`).
- Upanaya restates the liṅga as vyāpti-qualified (`तथा चायम्` = mountain has
  vyāpti-qualified smoke).
- Nigamana restates pakṣa with hetu+sādhya (`तस्मात्तथेति`); its prayojana
  includes demonstrating *abādhitattva* (freedom from contradiction).
- P2 §§46–47 (printed pp. 262–279) carry the same five members with NB's
  parallel glosses; no conflicting member list was found in either edition.

## 11. pramāṇa frame (pratyakṣa, upamāna, śabda as cited inside anumāna)

- Pratyakṣa as *bādhaka*: §28 example uses *sparśana-pratyakṣa* (tactile
  perception of heat) to defeat "fire is non-hot" — perception outranks the
  inference in that stock case.
- Upamāna/śabda are defined outside the inference run (P1 §§ post-28; P2
  §§58–59, printed pp. 327–329) and are invoked in D discussions
  (e.g. śabda/aptaprāmāṇya in manana objections). No separate extraction
  needed for Phase 0 beyond noting their section addresses for later grounding
  checks.
- Pakṣatā/siṣādhayiṣā material (§2 D, §14 D) is the main "desire/doubt"
  doctrine relevant to inference control flow (see §1 above).

## 12. Passages explicitly searched but NOT found (negative results)

- `hetūdāharaṇopanayanigamanāni` as one compound: absent in P1 extraction
  (members listed with spaces, §9); present in P2 (3 hits) — orthographic,
  not doctrinal, difference.
- `yatra yatra dhūmas tatra tatrāgniḥ` with visarga variants: P1 has the
  sūtra form (§4); P2 matches it in mūla p. 35 but several Note occurrences
  are spacing-fragmented (`यत्र धूमस्तत्राभिरिति` for *tatrāgniriti*).
- No second, rival definition of vyāpti or rival hetvābhāsa list was found in
  either file; the fivefold list (§17) is stable. Anupasaṃhārin (§21) is the
  only subtype whose *name* is absent from the mūla's §17 line but present in
  §18/§21 — consistent, not conflicting.
