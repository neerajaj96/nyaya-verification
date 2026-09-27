# Jha Vol. III Source Identity (Part I)

## Drive acquisition (documented failure first)

- Drive source: `https://drive.google.com/file/d/15exfrXy9VRb554fuzL4rZGCoJlX-6sn-/view?usp=drivesdk`
- Attempts 2026-09-27: gdown uc-form → permission failure; gdown view-form →
  permission failure; direct HTTPS → HTTP 200, 916,471 bytes, Google sign-in
  page (auth wall, same signature as Phases 1.5/1.75/2B). No bypass attempted.
- The Drive file's identity/contents remain UNVERIFIED — nothing below is
  claimed about that file. All Vol. III evidence comes from the verified
  same-edition alternate (Phase 2B provenance, re-verified below).

## Alternate source actually used (re-verified this phase)

- archive.org DLI scan `in.ernet.dli.2015.461557`
  (`2015.461557.The-Nyaya-sutras-Of-Goutama-Vol-3.pdf`), 26,778,493 bytes,
  SHA-256 `6d5004fc36af69a1e60134f663ba782d85e1d5c9eb77f180340477ea014d2115`
  (recomputed 2026-09-27, matches Phase 2B record), 361 PDF pages
  (ScanFix 2015). OCR derivative `_djvu.txt` (773,257 chars) as working text.
- Kept OUTSIDE the repo (`/tmp/opencode/ingest/phase15/`); hashes only committed.

## Title / publication (image-verified, PDF pp. 1–2)

- Title page: "THE NYĀYA-SŪTRAS OF GAUTAMA / WITH THE BHĀṢYA OF VĀTSYĀYANA
  AND THE VĀRTTIKA OF UDDYOTAKARA / Translated into English / With notes
  from Vāchaspati Mishra's 'Nyāya-Vārttika-Tātparyaṭīkā', Udayana's
  'Pariśuddhi' and Raghuttama's Bhāṣyachandra / by MAHAMAHOPADHYAYA
  GAṄGĀNĀTHA JHĀ / Vol. III / MOTILAL BANARSIDASS / Delhi Varanasi Patna
  Madras".
- Imprint page: "First published: in Indian Thought, 1912-1919. Reprint:
  Delhi, 1984. Printed in India by Shantilal Jain, at Shri Jainendra Press,
  A-45 Phase I, Naraina, New Delhi 110028 and published by Narendra Prakash
  Jain for Motilal Banarsidass, Delhi 110007."
- Closing verified (PDF pp. 360–361): "Thus ends the Bhāṣya on Adhyāya III"
  + Vārttika on Sū. 72 (akṛtyabhyupagama gloss) + six-item recap (Soul,
  Body, Instrument, Objects, Apprehension, Mind); p. 361 blank.

## Edition comparison (Part II)

Same edition/reprint family as Vols. I, II, IV: identical translator,
series apparatus (running heads "BHĀṢYA-VĀRTTIKA 3-x-y", [P./L.] locators,
footnote sigla, Tātparya/Pariśuddhi/Bhāṣyachandra notes), press, ISBN
family, library-stamp provenance (Asiatic Society pattern). Typography
matches (same page geometry class as Vol. II: ABBYY-series scans).
Pagination CONTINUOUS across volumes: Vol. II closed Jha p. 1066 →
Vol. III opens Discourse III (Jha p. 1067; PDF p. ~5) → Vol. III closes
(~p. 1428) → Vol. IV opens Discourse IV (p. 1429). No duplicates, no gaps,
no anomalous sections detected at the joints. Commentary present throughout
(Bhāṣya + Vārttika in full per-section; Tātparya/Pariśuddhi/Bhāṣyachandra/
Vivaraṇa fragments in notes; one EDITOR_NOTE-level decision: on 3.1.8–11
Jha places the whole Vārttika AFTER the Bhāṣya owing to Bhāṣya↔Vārttika
disagreement — stratification documented, not smoothed).

## Coverage table (Part III; PDF pp. approximate from form-feeds)

| Adhyāya | Āhnika | Sūtra range | Printed pp. | Present? |
|---|---|---|---|---|
| III | 1 (Daily Lesson I) | 3.1.1–3.1.71 (§§1–9: soul vs senses/body/mind; eternity; body; sense materiality; organs one/many; objects) | 1067–~1290 | YES, full + Bhāṣya/Vārttika/notes |
| III | 2 (Daily Lesson II) | 3.2.1–3.2.72 (§§1–7: buddhi transience; momentariness; buddhi-as-soul-quality; evanescence; not-body; mind; adṛṣṭa) | ~1290–1428 | YES, full + Bhāṣya/Vārttika/notes |

D-relevant material located: 3.1.1–3 negative concomitance (D7/D5);
3.1.1 designation-doubt (D1-adjacent); 3.1.8–11 Bhāṣya↔Vārttika disagreement
(stratification); 3.2 momentariness premiss-triage asiddha/viruddha (D-heter);
3.2.4 contradictory-probans (D6-adjacent); buddhi/soul ascertaining debate
(D6-adjacent); doubtful-premiss→fallacious line (D6). Absent: pakṣatā-terms
(11 "paksa" hits ALL pūrvapakṣa fragments — bounded NON-EVIDENCE for D1);
hetu/sādhya/vyāpti/anvaya/vyatireka/upādhi roman terms (Jha uses
probans/probandum/concomitance idiom here); kevala/anupasaṃhārin terms;
kalātīta-fallacy (1 "belated" hit is ordinary-language FALSE POSITIVE);
jāti-as-futility (0; "jāti" hits are universals/momentariness-adjacent).

## OCR characteristics

Roman-transliteration OCR (Devanagari 0 extractable; footnotes scan-image
only — same series convention). English argument-structure HIGH trust
(spot image-matches: title, 3.1.1 opening, closing colophon); transliterated
compounds MEDIUM (use English glosses primarily). Page images rendered for:
title (pp. 1–2), 3.1.1 opening, closing (360–361); readings transcribed,
images outside repo.
