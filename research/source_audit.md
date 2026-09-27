# Source Audit — Classical PDFs

Evidence-gathering only. No implementation, no doctrine invention, no code changes.
Extraction method: `pdftotext -layout` full-text dump + `pdfinfo`; hit counts and
page references below are derived from the extracted text, not from memory.
PDF-page numbers are approximate (±1) because the extractor emits one form-feed
per PDF page and the files open with blank/title pages.

Download register (all via `gdown https://drive.google.com/uc?id=<ID>`):

| Asset | Drive ID | Local file | Size |
|---|---|---|---|
| Classical Text PDF 1 | `1HBtcJA-hzB-jXIls5GaTvdcF9gMSQiDy` | `/tmp/opencode/ingest/pdf1.pdf` | 60.6 MB, 197 PDF pages |
| Classical Text PDF 2 | `1aNZ48GlcOXIJ9zDPO9_e9cjM20gxE1Yf` | `/tmp/opencode/ingest/pdf2.pdf` | 43.2 MB, 466 PDF pages |
| "Tarka AI" | `17HROei7KAaJdyjqz03o7C4SUDJ1Sn_Hr` | `/tmp/opencode/ingest/tarka_ai.zip` | 37.8 KB zip |
| "Nyāya Engine" | `1N2_axoGeEoY_MmfuzA_N4vTcY8kEIxm0` | `/tmp/opencode/ingest/nyaya_engine.zip` | 407 KB zip |

---

## PDF 1 — Virupakshananda edition

1. **Title:** *TARKA-SAMGRAHA With the Dīpikā of Annambhaṭṭa and Notes*
   (title pages render "TARKA SAMGRAHА / TARKA-SAMGRAНА" — the final glyph is
   an OCR misread of Devanagari visarga/anusvāra handling, not a real variant).
2. **Author (root text + auto-commentary):** Annambhaṭṭa (Annambhatta).
3. **Translator / editor:** Swami Virupakshananda.
4. **Edition:** Sri Ramakrishna Math, Mylapore, Madras/Chennai 600 004.
   Second edition, August 1994 (preface page); impression line on the ISBN page
   reads `III-2M 3C-6-2001`, ISBN `81-7120-674-3`. First edition undated in the
   visible front matter ("out of print for some years" before 1994).
5. **Commentary:** Annambhaṭṭa's own *Dīpikā* (Sanskrit, given in Devanāgarī),
   plus the translator's end-notes ("more notes, shifted to the end of the book").
6. **Language/script:** Sanskrit (Devanāgarī) + English translation + English
   exposition. Word-by-word Sanskrit glosses (*pratipadārtha*) are given for
   each sūtra, then a running translation, then Dīpikā in Devanāgarī with
   English rendering.
7. **OCR quality:** Good overall. `pdfinfo`: Creator/Producer `PDFium`,
   197 pages, A4 (595×842 pts). Extracted text = 392,338 chars / 7,719 lines;
   Devanāgarī chars ≈ 11.8%, ASCII letters ≈ 62.4%. Diacritic IAST is largely
   preserved (`vyāpti` 19, `sādhya` 10, `hetvābhāsa` 3, etc.), which makes
   transliteration search productive in this file. Conjuncts are occasionally
   split and the running heads repeat ("TARKA-SAMGRAHA" with variant finals).
8. **Page structure:** Title → imprint/ISBN → 2nd-ed preface → 1st-ed preface →
   introduction/philosophical preface → numbered text sections (SECTION V =
   INFERENCE at PDF p. ~88) with Text / gloss / translation / Dīpikā repeating
   per sūtra → appendices (tail of file lists Nyāya-Sūtra-style items 128–135
   on Gautama's *chala–jāti–nigrahasthāna* etc., i.e. supplementary Nyāya lists,
   not Tarkasaṃgraha proper) → publisher's book list.
9. **Sanskrit + translation both present:** Yes, systematically for every sūtra
   examined (anumāna §§1–28 all have Devanāgarī + gloss + translation + Dīpikā).
10. **Section/verse/sūtra numbering:** Yes. Anumāna runs as numbered Sanskrit
    sentences §§1–28+ (1 anumiti-karaṇam … 2 parāmarśa-janya … 3 parāmarśa …
    4 vyāpti … 5 pakṣadharmatā … 6–8 svārtha/parārtha … 9 pañcāvayava …
    11–13 liṅga-traividhya … 14–16 pakṣa/sapakṣa/vipakṣa … 17–28 hetvābhāsa
    taxonomy). Printed pages 88–116 carry the inference core.
11. **OCR problems recorded:**
    - Title-page glyph garbage (`SAMGRAHА`, `MAKALSINA MA`, Cyrillic-looking
      `АНАЯМА-АЖЯАТ` for what should be imprint text).
    - E-mail line `MEMemail: srkmath@vsnl.com Я па`.
    - Sporadic diacritic noise (`pratyakşa pramăna`, `parămarśa`, `tatha hi`
      split as `tathā hi`/`tathahi`).
    - Hyphenation/line-break splits inside Sanskrit compounds in the gloss.
    - No embedded (machine) section tags — headings are plain text
      ("SECTION V / INFERENCE / 1. Inference (anumānam):"), so passage
      location must be by sūtra string search, not by metadata.

## PDF 2 — Athalye/Bodas edition

1. **Title:** *TARKA-SAMGRAHA OF ANNAMBHАṬṬA, WITH THE AUTHOR'S OWN DIPIKĀ,
   AND GOVARDHANA'S NYĀYA-BODHINĪ*.
2. **Author (root text + first commentary):** Annambhaṭṭa (Tarkasaṃgraha +
   Tarka-Dīpikā). Second commentary: Govardhana's *Nyāya-Bodhinī*.
3. **Editors/translators:** Edited with critical/explanatory notes by the late
   Yashwant Vasudev Athalye; introduction + English translation of the text by
   Mahadev Rajaram Bodas. Revised and enlarged, second edition re-impression
   **1930** (first edition 1897; second 1918; present re-issue 1930),
   *Bombay Sanskrit Series No. LV*, for the Department of Public Instruction,
   Bombay; printed at Bhandarkar Institute Press, Poona; published by the
   Bhandarkar Oriental Research Institute, Poona. Price "Two Rupees and eight
   annas" on the title page.
4. **Commentary:** Two Sanskrit commentaries printed with the mūla
   (Dīpikā + Nyāya-Bodhinī), plus ~300 pages of English critical Notes that
   re-translate each section (translation printed in italics at the head of
   each Note section).
5. **Language/script:** Sanskrit (Devanāgarī, two commentaries) + English
   (Introduction pp. IX–LX, Notes pp. 69–372, Appendices A–C, Index).
6. **OCR quality:** Mixed but usable. `pdfinfo`: `PDFium`, 466 pages,
   359×602 pts. Extracted text = 1,056,295 chars / 20,989 lines; Devanāgarī ≈
   15.3%, ASCII ≈ 54.7%. IAST diacritic search is *unproductive* here
   (`anumāna` 1, `vyāpti` 8 in roman) because the English Notes use older
   transliteration inconsistently and the OCR merges/drop diacritics; the
   Devanāgarī channel is the productive one (व्याप्ति 348, पक्ष 417,
   हेतु 308, साध्य 303, परामर्श 136, हेत्वाभास 22, उपाधि 59).
7. **Page structure (from the printed Contents + extraction):**
   Title → imprint → Contents (Text+Commentaries pp. 1–68; Notes pp. 69–372;
   §§1–81 + Appendices + Index) → Prefaces → Introduction (IX–LX, incl.
   "Annambhatta and his works") → Abbreviations → mūla+commentaries
   (printed pp. 1–68) → Notes §§1–81 (printed pp. 69–372; inference §§42–59
   at printed pp. 211–329; §§44 anumānam p. 233, 45 svārtha/parārtha p. 251,
   46 pañcāvayavāḥ p. 262, 47 parāmarśaḥ p. 279, 48 liṅgam p. 281,
   49 pakṣaḥ / 50 sapakṣaḥ p. 290, 51 vipakṣaḥ, 52 hetvābhāsāḥ p. 293,
   53 savyabhicāraḥ p. 298, 54 viruddhaḥ p. 302, 55 satpratipakṣaḥ p. 303,
   56 asiddhaḥ p. 305, 57 bādhitaḥ p. 315, 58 upamānam p. 327,
   59 śabdaḥ p. 329) → Appendices A–C → Index (p. 380).
8. **Sanskrit + translation both present:** Yes — Sanskrit in the first half,
   English translation embedded per- section in the Notes (explicitly noted in
   the 2nd-ed preface: "a literal translation … printed in italics at the top
   of each section").
9. **Numbering:** Yes — stable section numbers (§§1–81) shared across mūla,
   commentaries, and Notes; the inference/hetvābhāsa run is §§42–59.
10. **OCR problems recorded:**
    - Heavy title-page misreads (`Lublic` for Public, `Bamhay` for Bombay,
      `Yombay Sanskrit Sertts` for Bombay Sanskrit Series, `Frice … annas`).
    - Devanāgarī words frequently fragmented with intruding spaces
      (e.g. `परामर्शजन्यं` split across lines, `व्याप्तिविशिष्ट…` with broken
      conjuncts), so exact-string search must allow for spacing variants;
      counts above use the canonical unsplit forms and therefore *undercount*
      the true occurrences.
    - Footnote sigla (`E and X omis …`, `Q, U, W` manuscript sigla) intrude
      into the text flow.
    - Roman-numeral front matter (V, VII, IX, LX, XXI) collides with
      section-number regexes; "Sect." is sometimes OCR'd "Sect,".

## Joint finding (both PDFs)

- Both files are editions of the **same root work** (Annambhaṭṭa's
  *Tarkasaṃgraha* with his own *Dīpikā*): PDF 1 = Virupakshananda
  (Ramakrishna Math, 1994); PDF 2 = Athalye/Bodas (Bombay Sanskrit Series,
  1930, adding Govardhana's *Nyāya-Bodhinī*). They therefore describe the
  **same conceptual system** (Nyāya–Vaiśeṣika primer) — this is an evidenced
  conclusion, not an assumption: the opening inference sūtras are verbally
  identical across editions (§1 `अनुमितिकरणमनुमानम्`, §3
  `व्याप्तिविशिष्टपक्षधर्मताज्ञानं परामर्शः`, §4
  `यत्र यत्र धूमस्तत्र तत्राग्निरिति साहचर्यनियमो व्याप्तिः`; see
  `classical_sources/anumana_passages.md`).
- Complementary strengths: PDF 1 is the better source for **IAST/English
  search and clean per-sūtra translation**; PDF 2 is the better source for
  **Devanāgarī density, the second commentary, and the long critical Notes**
  (bhūyodarśana/tarka discussion of vyāptigraha, upādhi analysis, kevala-
  anvayi/vyatireki edge cases).
- Neither file has machine-readable structure (no bookmarks/TOC metadata,
  no verse IDs); all citations in this dossier are by **sūtra string +
  printed §/page + approximate PDF page**.
