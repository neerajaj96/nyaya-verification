# Hetvābhāsa — Complete Source Investigation

Source base: TS §§17–28 + Dīpikā as in P1 (PDF ~105–116 / printed 105–116),
confirmed against P2 §§52–57 (printed pp. 293–315; Devanāgarī densities:
hetvābhāsa 22, savyabhicāra 31, viruddha 34, satpratipakṣa 26, asiddha 35,
bādhita 38). Full Sanskrit + translation in `anumana_passages.md` §8;
this file adds per-category analysis and the source-vs-engineering split.

General definition (D on §17): *anumitipratibandhaka-yathārthajñāna-
viṣayatvaṃ hetvābhāsatvam* — a hetvābhāsa is what is objectified by veridical
cognition that blocks anumiti. Mūla enumeration (§17):
`सव्यभिचारविरुद्धसत्प्रतिपक्षासिद्धबाधिताः पञ्च हेत्वाभासाः`.

Blocking architecture (D on §28, P1 p. 116 — load-bearing for any checker
design): *bādhasya grāhyābhāva-niścayatvena, satpratipakṣasya
virodhijñāna-sāmagrītvena sākṣād-anumiti-pratibandhakatvam; itareṣāṃ tu
parāmarśa-pratibandhakatvam* — bādhita and satpratipakṣa block **anumiti
directly**; all others block **parāmarśa**. Sub-mechanisms: sādhāraṇa by
*avyabhicārābhāva-rūpatayā*; viruddha by *sāmānādhikaraṇyābhāvatayā*;
vyāpyatvāsiddha by *viśiṣṭavyāptyabhāvatayā*; asādhāraṇa/anupasaṃhārin by
*vyāptisaṃśayādhāyakatvena* (raising doubt about vyāpti);
āśrayāsiddha/svarūpāsiddha by *pakṣadharmatājñāna-pratibandhakatvam*;
*upādhis tu vyabhicārajñānadvārā vyāptijñānapratibandhakaḥ*.

---

## 1. Savyabhicāra / anaikāntika — threefold (§§18–21)

Mūla §18: `सव्यभिचारः अनैकान्तिकः । स त्रिविधः साधारणासाधारणानुपसंहारिभेदात्`.

### 1a. Sādhāraṇa (common strayer, §19)

- Sanskrit: `तत्र साध्याभाववद्वृत्तिः साधारणः अनैकान्तिकः, यथा पर्वतो वह्निमान् प्रमेयत्वात् इति । प्रमेयत्वस्य वह्न्यभाववति ह्रदे विद्यमानत्वात्`.
- Translation: reason present where sādhya is absent; mountain-fiery-because-
  knowable; knowability also in the fireless lake.
- Conditions: hetu occurs in a (ascertained) vipakṣa locus.
- Defeating condition for the *defect* (i.e. what would save the hetu):
  showing the alleged vipakṣa occurrence fails (lake not really fireless, or
  knowability not really there) — not discussed as a separate procedure; the
  defect stands on exhibition of the vipakṣa-vṛtti.
- Relation to vyāpti: breaks anvaya (avyabhicāra absent).
- Relation to pakṣa/sādhya: pakṣa hill, sādhya fire; defect located in
  hetu's over-extension beyond sādhya.
- Dīpikā clarification: defines via the §19 formula; no extra subtlety in
  the extracted window beyond the lake exhibition.
- Computational interpretation (source-derived part): exhibited
  hetu(x) ∧ niścita-¬sādhya(x) with same-locus reading. Engineering
  interpretation (code's): any appended `counterexamples[0]` string breaks
  the vyāpti (drops *niścita* and *sāmānādhikaraṇya*; see conflicts C6).

### 1b. Asādhāraṇa (uncommon strayer, §20)

- Sanskrit: `सर्वसपक्षविपक्षव्यावृत्तः पक्षमात्रवृत्तिः असाधारणः । यथा शब्दो नित्यः शब्दत्वात् इति । शब्दत्वं हि सर्वेभ्यो नित्येभ्योऽनित्येभ्यश्च व्यावृत्तं शब्दमात्रवृत्तिः`.
- Translation: absent from *all* sapakṣa and vipakṣa, present only in pakṣa;
  sound-eternal-because-soundness.
- Conditions: universal absence elsewhere + sole pakṣa presence.
- Defeating condition: producing even one genuine sapakṣa/vipakṣa occurrence
  (or showing pakṣa-absence) dissolves it.
- Relations: vyāpti-doubt-raiser (no positive or negative instance to fix
  concomitance); pakṣa = sound, sādhya = eternality.
- Computational split: source requires a *universal* absence scan over
  sapakṣa+vipakṣa; code tests only `sapaksha is None` (one missing string).
  Verdict: shape right, quantifier dropped.

### 1c. Anupasaṃhārin (non-exclusive, §21)

- Sanskrit: `अन्वयव्यतिरेकदृष्टान्तरहितोऽनुपसंहारी । यथा सर्वमनित्यं प्रमेयत्वादिति । अत्र सर्वस्यापि पक्षत्वात् दृष्टान्तो नास्ति`.
- Translation: has neither anvaya nor vyatireka dṛṣṭānta; everything-non-
  eternal-because-knowable; everything is pakṣa so no example exists.
- Conditions: universal pakṣa (no comparison class) ⇒ no dṛṣṭānta possible.
- Relations: the limit case of vyāpti-doubt; connects to kevalānvayi
  discussion (§12) by contrast (there a positive-only reason still proves;
  here *no* example at all is available).
- Computational split: **no code counterpart** — the engine conflates it with
  asādhāraṇa via the same `sapaksha is None` gate, losing the
  universal-pakṣa diagnosis. Any future checker must test
  "pakṣa == domain" separately from "hetu unique to pakṣa".

## 2. Viruddha (§22)

- Sanskrit: `साध्याभावव्याप्तो हेतुर्विरुद्धः । यथा शब्दो नित्यः कृतकत्वादिति । कृतकत्वं हि नित्यत्वाभावेनाऽनित्यत्वेन व्याप्तम्`.
- Translation: hetu pervaded by sādhya-absence; sound-eternal-because-
  produced; producedness pervades non-eternality (the negation of eternality).
- Conditions: live vyāpti hetu→sādhyābhāva.
- Defeating condition: breaking that contrary vyāpti (showing kṛtakatva
  without anityatva somewhere ascertained).
- Relations: vyāpti present but *pointing the wrong way* (absence of
  sāmānādhikaraṇya with sādhya); pakṣa sound, sādhya eternality.
- Computational split: source needs the contrary *vyāpti*; code checks a
  stored contrary *row* (`vyapti(hetu→not-sadhya).is_valid()`), inheriting the
  row-vs-vyāpti gap (T9). Stock example preserved exactly.

## 3. Satpratipakṣa (§23)

- Sanskrit: `यस्य साध्याभावसाधकं हेत्वन्तरं विद्यते स सत्प्रतिपक्षः । यथा शब्दो नित्यः श्रावणत्वात् शब्दत्ववत् । शब्दोऽनित्यः कार्यत्वात् घटवत्`.
- Translation: a *second* hetu proving sādhya-absence exists; audible→eternal
  (cf. soundness) vs. product→non-eternal (cf. jar) on sound.
- Conditions: two apparently sound hetus, same pakṣa, contradictory
  sādhyas, each with sapakṣa/dṛṣṭānta (soundness; jar).
- Defeating condition: defeating either hetu (showing śrāvaṇatva or kāryatva
  itself defective) resolves the balance — the D's *sākṣād-anumiti-
  pratibandhaka* note implies resolution is at the anumiti level, not by
  preferring one parāmarśa.
- Relations: only hetvābhāsa essentially involving *two* hetus; *sat*
  (balanced/equipollent) is definitional — an obviously weaker counter-hetu
  does not qualify.
- Computational split: code drops *samatva* (any stored counter-row with h2
  present suffices) and drops the dṛṣṭānta/sapakṣa requirements on both
  sides. Stock pair preserved exactly.

## 4. Asiddha — threefold (§§24–27)

Mūla §24: `असिद्धस्त्रिविधः — आश्रयासिद्धः, स्वरूपासिद्धो व्याप्यत्वासिद्धश्चेति`.

### 4a. Āśrayāsiddha (§25)

- Sanskrit: `आश्रयासिद्धो यथा गगनारविन्दं सुरभि अरविन्दत्वात् सरोजारविन्दवत् । अत्र गगनारविन्दमाश्रयः स च नास्त्येव`.
- Sky-lotus fragrant because lotus-like; substratum simply nonexistent.
- Blocks pakṣadharmatā-jñāna (no locus for occurrence). Code check 1
  (locus unknown) matches directly; message cites gagana-aravinda verbatim.

### 4b. Svarūpasiddha (§26)

- Sanskrit: `स्वरूपासिद्धो यथा शब्दो गुणश्चाक्षुषत्वात् । अत्र चाक्षुषत्वं शब्दे नास्ति शब्दस्य श्रावणत्वात्`.
- Sound-is-quality-because-visible; visibility *absent* in sound (only
  audibility there).
- Blocks pakṣadharmatā-jñāna. Code's absent-branch (`False`) matches;
  code's unverified-branch (`None` ⇒ defect) extends beyond the sūtra
  (absence-of-information treated as asiddha). Verdict: half direct, half
  engineering extension (conflicts C1-adjacent).

### 4c. Vyāpyatvāsiddha / sopādhika (§27)

- Full Sanskrit in `anumana_passages.md` §9: `सोपाधिको हेतुः व्याप्यत्वासिद्धः…`
  with the *sādhyavyāpakatve sati sādhanāvyāpakatvam = upādhi* definition,
  the fire→smoke stock case, *ārdrendhana-saṃyoga*, and the ayogolaka
  counterexample.
- Blocks via *viśiṣṭavyāptyabhāva* (absence of the qualified concomitance);
  upādhi operates *through* vyabhicāra-cognition on vyāpti-cognition.
- Computational split: source demands proof of the double-pervasion fact;
  code accepts any non-empty `upadhi` string as blocking. Stock case and gate
  position match; criterion thinned (conflicts C5).

## 5. Bādhita (§28)

- Sanskrit: `यस्य साध्याभावः प्रमाणान्तरेण निश्चितः स बाधितः । यथा वह्निरनुष्णो द्रव्यत्वात् जलवत् । अत्रानुष्णत्वं साध्यं तदभाव उष्णत्वं स्पर्शनप्रत्यक्षेण गृह्यत इति बाधितत्वम्`.
- Fire-non-hot-because-substance (cf. water); hotness grasped by tactile
  perception — *pramāṇāntareṇa niścitaḥ*.
- Blocks *anumiti directly* via *grāhyābhāva-niścaya* (ascertainment of the
  absence of what was to be proved). Note the D'susah comparison with
  satpratipakṣa (both direct blockers, different mechanisms).
- Computational split: defeat shape + example match; code's numeric
  pramāṇa-strength table (4/3/2/1/0) is unattested in the extracted window
  (the sūtra says *pramāṇāntara*, and the example happens to be pratyakṣa —
  no total order is stated). Verdict: shape supported, ranking not
  established (conflicts C2).

## 6. Cross-hetvābhāsa relations (source-derived)

- Sādhāraṇa vs. upādhi: both involve vyabhicāra, but sādhāraṇa *exhibits* the
  deviating locus while upādhi *explains* deviation via the conditioning
  property (D p. 116 separates their blocking routes).
- Viruddha vs. satpratipakṣa: viruddha is one hetu proving the opposite;
  satpratipakṣa is two hetus proving opposites — the code's checks 4/5
  preserve this one-vs-two architecture correctly.
- Asādhāraṇa vs. anupasaṃhārin: both are vyāpti-doubt-raisers, but
  asādhāraṇa has a populated comparison class the hetu avoids, while
  anupasaṃhārin has *no* comparison class at all — the code's single gate
  erases this distinction (conflicts C4).
- Bādhita vs. satpratipakṣa: both direct anumiti-blockers; bādhita needs a
  *pramāṇāntara-niścaya* of absence, satpratipakṣa a rival *hetu*; the code
  preserves the two routes but formalizes "pramāṇāntara" as a strength number
  and drops "hetu must be *sat* (balanced)".

## 7. Source-derived vs. engineering-interpretation ledger

Source-derived (safe to build on): fivefold list + both threefold
subdivisions; all Sanskrit definitions; all stock examples (lake, soundness,
omni-pakṣa, kṛtakatva, śrāvaṇatva/kāryatva, sky-lotus, visibility,
wet-fuel/iron-ball, fire-cold); two-level blocking theory; upādhi double-
pervasion formula; niścita qualifier on sapakṣa/vipakṣa; vyāpti-doubt route
for asādhāraṇa/anupasaṃhārin; pakṣadharmatā route for āśraya/svarūpa.

Engineering interpretations (do not cite as classical): 9-linear-check order;
numeric pramāṇa strengths; None-means-svarūpasiddha; any-string-upādhi;
counterexample-string breaking; sapakṣa-None covering anupasaṃhārin;
vyāpti-asiddha as a sixth defect; 1→1 Apriori rules called vyāpti; BoW-cosine
as āpta test. Each is recorded with its conflict ID in `conflicts.md`.
