# Corpus Provenance — Nyāya-Sūtra Volumes (Phase 1.5)

The PDFs themselves are NOT vendored in this repository (size + rights).
This file records what was acquired, from where, and with what fidelity, so
any claim citing these volumes is checkable. All statistics below were
produced by executed commands (`pdfinfo`, `pdftotext -layout`, SHA-256),
not by recollection. No web search was used as a substitute for the supplied
files; the one reported fact about inaccessibility was established by three
failed download attempts (gdown ×2 with distinct URL forms, curl, requests,
Drive page fetch → HTTP 401 / sign-in redirect).

## Volume 1 — ACQUIRED

- Drive ID: `13gfyi0OKNNM3mneQxNxcJDW1xFA_XV40`
- Local (outside repo, extraction only): `/tmp/opencode/ingest/phase15/vol1.pdf`
- SHA-256:
  `2fb53c2e45e31663daae430e2aa4ac03769bc37b5015fe8a2339bcefb23ebf78`
- Size: 42.7 MB (41 MiB on disk); 618 PDF pages (`pdfinfo`: PDFium).
- Edition (from title/imprint pages): *The Nyāya-Sūtras of Gautama, with the
  Bhāṣya of Vātsyāyana and the Vārttika of Uddyotakara*, translated into
  English with notes from Vācaspati Miśra's *Nyāya-Vārttika-Tātparyaṭīkā*,
  Udayana's *Tātparya-Parishuddhi* and Raghuttama's *Bhāṣyachandra*, by
  Mahāmahopādhyāya Ganganatha Jha. Vol. I. Motilal Banarsidass, Delhi,
  reprint 1984 (first published serially in *Indian Thought*, Vols. IV–XI,
  1912–1919). Four-volume set ("FOR FOUR VOLUMES"; preface: ~1800 print
  pages total). Copy carries holybooks.com reprint stamp + Asiatic Society,
  Calcutta library stamps.
- Textual coverage (verified by sutra-marker scan + tail read): front matter
  → Introduction ("Varttika-introductory") → **Adhyāya I complete**:
  Discourse I / Daily Lesson I (NS 1.1.1 through 1.1.41: pramāṇa/prameya
  enumeration, pratyakṣa, anumāna 1.1.5, upamāna, śabda, avayavas 1.1.32,
  tarka/nirṇaya) + Daily Lesson II (NS 1.2.1–1.2.20: vāda/jalpa/vitaṇḍā,
  hetvābhāsa, chala, jāti, nigrahasthāna; last marker 1-2-20 at 99.4% of
  extracted text) → publisher advertisements (no further translation).
- Sanskrit/Devanāgarī: **0 Devanāgarī characters in 1,493,268 extracted
  chars**. Sanskrit appears only as unmarked roman transliteration inside the
  English (often OCR-degraded: `$`/`1`/`~` for ś/ṣ/i, e.g. `BHX$YA`,
  `proban/probandum` for probans/probandum, `Diimlga` for Dignāga).
- Transliteration: present but noisy (see above); IAST diacritics largely
  lost — search must be OCR-tolerant.
- English translation: YES — full (sūtra + Bhāṣya + Vārttika + notes).
- Commentary layers present: SOURCE_ROOT_TEXT (Gautama sūtras, transliterated
  + translated) / SOURCE_BHĀṢYA (Vātsyāyana, in full) / SOURCE_VĀRTTIKA
  (Uddyotakara, in full) / SOURCE_TĪKĀ fragments (Vācaspati's Tātparyaṭīkā
  via Jha's notes) / SOURCE_LATER_COMMENTARY fragments (Udayana's
  Pariśuddhi, Raghuttama's Bhāṣyachandra, "modern Logicians"/Navya-Nyāya
  positions) / SOURCE_TRANSLATOR_NOTE (Jha's footnotes, marked `* ° †`,
  incl. Buddhist/Mīmāṃsā parallels and untranslated-Vārttika caveats).
- OCR quality: usable-with-care. Structure markers survive
  (`BHASYA 1-1-1`, `VARTIKA 1-1-1`, printed page nos., `[P. x, L. y]`
  source locators); running heads repeat; holybooks.com stamps intrude.

## Volume 2 — ACQUIRED

- Drive ID: `17HuPUCvyNXNTcoq7lOmOA9W1WMGqT-Zi`
- Local: `/tmp/opencode/ingest/phase15/vol2.pdf`
- SHA-256:
  `41b5ad4729de06a38e47906b471b0a768fa4c8ffab8f877e27be36c9270ee376`
- Size: 38.1 MB; 489 PDF pages (`pdfinfo`: ABBYY FineReader, 2009-01-30 —
  i.e. this volume is an OCRed scan, cleaner than Vol. 1).
- Edition: same Jha / Motilal Banarsidass 1984 set, Vol. II (same imprint
  page, ISBN 0-89581-754-3).
- Textual coverage (verified by contents page + tail colophon): **Adhyāya II
  complete** — Discourse II / Daily Lesson I: doubt (2.1.1–7), pramāṇas in
  general, perception, composite wholes, **inference 2.1.37–38** (pūrvavat/
  śeṣavat/sāmānyatodṛṣṭa objections: obstruction/demolition/resemblance +
  reply), time (esp. present), upamāna; Daily Lesson II (śabda discourse):
  word in general/particular, **exact number of pramāṇas 2.2.1–12**
  (aitihya/arthāpatti/sambhava/abhāva objector), non-eternality of words,
  sound modifications, word potencies, vyakti/ākṛti/jāti denotation +
  Bauddha **apoha** objections; ends "END OF DISCOURSE II" + chapter
  colophon (four cow-universality inferences).
- Sanskrit/Devanāgarī: **0 Devanāgarī in 1,123,206 chars** (same roman-only
  convention; cleaner OCR than Vol. 1: `BHĀSYA`, `Vārtika`, `Sūtra` mostly
  intact).
- Translation/commentary layers: same six layers as Vol. 1 (root + Bhāṣya +
  Vārttika in full; Tātparya/Parishuddhi/Bhāṣyachandra fragments in notes;
  Jha footnotes). Layer density is high: e.g. the 2.1.37 passage carries
  Bhāṣya + Vārttika + Tātparya + Pariśuddhi + Bhāṣyachandra voices on one page.
- OCR quality: good. Section headers (`Adhyāya II. Daily Lesson I. Section
  (5). Examination of Inference. [Sutras 37–38.]`), sutra display
  (`jporvafßakm` noise in the transliterated sūtra line — the English
  translation beside it is clean), `[P./L.]` locators intact.

## Volume 3 — NOT ACQUIRED (Gap)

- Drive ID: `15exfrXy9VRb554fuzL4rZGCoJlX-6sn-`
- Status: **inaccessible**. `gdown` (two URL forms + retry): "Gdown can't.
  Please check connections and permissions." Direct HTTPS: HTTP 200 with a
  Google sign-in page (i.e. auth-walled, not public). Drive file page:
  HTTP 401. Expected contents (unverified — do NOT cite): presumably the
  next volume(s) of the same Jha set (Adhyāyas III–V: self/body, suffering,
  and the detailed jāti/nigrahasthāna books). Recorded as Gap G-NS-01 in
  `CORPUS_ACQUISITION_MATRIX.md`. No content claims are made about it.
- Action required: request public sharing or an alternate source; do not
  substitute web-search summaries.

## Handling notes

- Extracted working texts (`vol1.txt` 1.49M chars/24,801 lines; `vol2.txt`
  1.12M chars/19,675 lines) live OUTSIDE the repo (extraction scratch).
  Passages cited in research files carry PDF-page approximations + printed
  Jha page numbers (the stable locator: Jha's pages run continuously across
  volumes, e.g. "p. 798", "pp. 1066") + sūtra numbers, so claims survive
  without the PDFs.
- No copyrighted PDF is committed to the public repository (see
  `traceability/PHASE1_5_VALIDATION.md`).

## Volume III — ACQUIRED VIA ALTERNATE LOCATION (Phase 2B, 2026-09-27)

- Drive file `15exfrXy9VRb554fuzL4rZGCoJlX-6sn-` (G-NS-01 target) REMAINS
  inaccessible (re-attempts 2026-09-27: gdown uc + view forms failed;
  direct HTTPS returns the sign-in page). The Drive file's identity and
  contents are STILL UNVERIFIED — nothing below is claimed about it.
- Acquired instead: SAME EDITION (Jha / Motilal Banarsidass 1984 reprint of
  Indian Thought 1912–19; title, imprint, and Asiatic-Society library stamps
  match Vols. 1–2) via open access:
  `https://archive.org/download/in.ernet.dli.2015.461557/2015.461557.The-Nyaya-sutras-Of-Goutama-Vol-3.pdf`
  (Digital Library of India scan; openly downloadable; PDF kept OUTSIDE the
  repo at `/tmp/opencode/ingest/phase15/vol3_ia.pdf`).
- Integrity: 26,778,493 bytes (matches archive metadata size + md5
  `d0aafbc3da31b1b8909837e4da79f8d3` as listed); SHA-256:
  `6d5004fc36af69a1e60134f663ba782d85e1d5c9eb77f180340477ea014d2115`;
  361 PDF pages (`pdfinfo`: ScanFix Enhanced, 2015-06-25); archive OCR
  derivative `..._djvu.txt` (784,123 bytes per metadata; 773,257 chars
  extracted) used as working text.
- Coverage (verified): Jha Vol. III = **Adhyāya III complete** (Discourse
  III, Jha pp. 1067–1400+, continuous pagination after Vol. II): soul vs
  sense-organs/body/mind; eternity; body/sense-organ materiality and number;
  sense-objects; buddhi transience; momentariness (Bauddha kṣaṇikatva)
  debate; buddhi-as-soul-quality; mind; body/adṛṣṭa. Ends "Thus ends the
  Bhāṣya on Adhyāya III" (3.2.72).
- Layers: same six as Vols. 1–2 (root transliterated + translated; Bhāṣya +
  Vārttika in full; Tātparya/Pariśuddhi/Bhāṣyachandra fragments in notes;
  Jha footnotes). Notable: 3.1.1–3 negative-concomitance debate carries
  Tātparya + Pariśuddhi placement dispute IN-TEXT.
- Sanskrit/Devanāgarī: 0 extractable chars (roman-only + scan-image
  footnotes, same convention as Vols. 1–2).
- Redistribution: openly downloadable from archive.org (DLI open scan);
  holybooks.com likewise lists the same 4-volume set as free PDFs (its
  server returned Cloudflare 520 for Vol. 3 on 2026-09-27 — recorded, not
  retried further). PDF NOT committed to this repo (see validation files).
- Consequence for G-NS-01: split status — Drive file still gapped;
  Adhyāya-III evidence gap CLOSED via verified same-edition alternate;
  Adhyāya IV–V (Jha Vol. IV) still missing. Detail in
  `corpus/ACQUISITION_PHASE_2B.md`.

## Volume 4 — ACQUIRED VIA DRIVE (Phase 2B+1, 2026-09-27)

- Drive source: `https://drive.google.com/file/d/1OYRzPDrwpmw51ZVmwYUVFUfrnTo8EEjP/view?usp=drivesdk`
  (direct gdown download, 100% complete, NO auth wall).
- Local (outside repo): `/tmp/opencode/ingest/phase15/vol4.pdf`.
- SHA-256: `13febcfef76cb4b291d23fd39bf7045d3bf88cf71c86acd9909fea51c8f90f0f`.
- Size: 35,673,655 bytes (35.7 MB); 354 PDF pages (`pdfinfo`: ABBYY
  FineReader 2009-02-03; 360×569.88 pts — series format).
- Edition: Jha / Motilal Banarsidass 1984 reprint (serial 1912–19), Vol. IV,
  ISBN 0-89581-754-3 — title/imprint verified same set as Vols. 1–3.
- Coverage (verified from contents + tail colophons): Jha pp. 1429–1772+ =
  **Adhyāya IV complete** (karma/doṣa/pretyabhāva/phala/duḥkha/apavarga/
  tattvajñāna/avayava/aṇu/bāhyārtha) + **Adhyāya V complete** (5.1:
  24 jātis + six steps; 5.2: 22 nigrahasthānas in seven heads; Bhāṣya +
  Vārttika closing colophons for the whole NS). With Vols. 1–3, NS I–V
  fully covered same-edition.
- Layers: same six (root transliterated+translated; Bhāṣya + Vārttika full;
  Tātparya/Pariśuddhi/Bhāṣyachandra/Vardhamāna/Viśvanātha/
  Nyāyanibandhaprakāśa fragments; Jha notes). New voice attributions:
  "Bodhasiddhi (Udayana)" (Jha fn, 5-1-19 region) — lead only.
- Working text: `pdftotext -layout` (732,769 chars, 354 form-feeds);
  0 Devanāgarī (series convention). OCR: English HIGH (image-matched PDF
  p.317 = Jha p.1736, 5.2.1 list); transliteration MEDIUM.
- Adjudication: `research/traceability/JHA_VOL4_ADJUDICATION.md`. PDF NOT
  committed (hashes + locators only).
