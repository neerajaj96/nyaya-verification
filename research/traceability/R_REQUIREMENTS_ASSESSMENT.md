# R1–R15 Assessment Against the New Corpus

Procedural fact: the external draft `computational-requirements-v1.md` is
NOT in this repository (verified absent 2026-09-27; cf. JHA_VOL4_
ADJUDICATION reconciliation section). The R-descriptions below are the
brief's own Part-V glosses, assessed against the three new volumes. Each
R-item: status (UNCHANGED / STRENGTHENED / WEAKENED / BLOCKED / NEW
CONSTRAINT / UNASSESSED) + necessary?/sufficient?/revision? Recording the
assessment here does NOT adopt any requirement — adoption needs the draft
in-repo + per-item evidence review.

| # | Requirement (brief gloss) | New evidence | Stratum | Status | Necessary? | Sufficient? | Revision? |
|---|---|---|---|---|---|---|---|
| R1 | source provenance | 3 new source IDs + hashes; Tibetan/Devanagari readability splits | method | STRENGTHENED | yes | no (needs readability + reconstruction-dependence fields — NEW CONSTRAINT) | YES: provenance records must include readability + reconstruction-dependence |
| R2 | historical stratification | TC ROOT vs Rahasya vs Vidyābhūṣaṇa vs Bhattacharya layers; PS restoration-vs-xylograph split | method | STRENGTHENED but INSUFFICIENT (see below) | yes | NO — see R2/R3/R12 test | YES (below) |
| R3 | semantic non-collapse | hetucakra-ninefold vs TS-five vs NS-five now three named taxonomies; viśeṣaṇa≠avacchedaka | method | STRENGTHENED | yes | NO — see below | YES (below) |
| R4 | epistemic status | L7070 jñānatva/niścayatva split; niścaya/saṃśaya currency; no grades | TC ROOT + TS | STRENGTHENED | yes | no | add jñāna-vs-niścaya split to status design space |
| R5 | counterexample status | odorous/earth + iron-ball + tri-temporal (prior); S5a/b/c typing stands; no new admission rule | NS/TS/TC-usage | UNCHANGED | yes | no | none |
| R6 | vyāpti representation | pañcaka + grahopāya-siddhānta at exposition level; root siddhānta missing; PS-Ch.II missing | HIST_STUDY | STRENGTHENED (pattern corroborated) but BLOCKED as root spec | yes | no | NONE until Anumāna-khaṇḍa root + PS Ch. II |
| R7 | anvaya/vyatireka independence | kevalānvayi currency (TC); purely-negative probans debate (Book II); vyatireka-practice (Vol. III) | multi | STRENGTHENED | yes | no | elevate kevala handling from TS-only to cross-stratum concern |
| R8 | purely-negative inference | Book II negative-hetu exposition (kitchen/lake); odorous/earth; kevalavyatireki SHAPE only | HIST_STUDY + practice | STRENGTHENED as concern; BLOCKED as spec | yes | no | NONE until kevalavyatireki root treatment sourced |
| R9 | upādhi/defeater | TC ROOT suspected-vs-real + uccheda warning (upgrades D5 cap to doctrine-backed) | TC ROOT | STRENGTHENED | yes | no | suspected/proved/exhibited 3-state is now REQUIRED shape (was prudent option) |
| R10 | qualification | avacchedaka 21 + vyadhikaraṇa-abhāva shapes; viśeṣaṇa≠avacchedaka | TC ROOT + Book II | NEW CONSTRAINT | yes | no | nested qualification/delimitation structures REQUIRED as open research (H3); flat qualifier fields non-conforming for NN shapes |
| R11 | hetvābhāsa | three named taxonomies; non-collapse guards hold; NN taxonomy missing | multi | STRENGTHENED | yes | no | taxonomy parameter must accept ≥3 values (NS-A / TS-C / hetucakra-pending) |
| R12 | provenance-stratum terminology | Tibetan-unreadable + restoration-unOCR'd + root/Rahasya-interwoven + exposition-vs-root splits | method | STRENGTHENED but INSUFFICIENT | yes | NO — see below | YES (below) |
| R13 | machine-checkability | NOTHING new is decision-procedure-shaped (reaffirmed: F2 procedure-like ≠ procedure; tarka illustration is dialectical, not algorithmic) | — | UNCHANGED | deferred | no | none (checkability claims stay forbidden pre-adjudication) |
| R14 | NL/Sanskrit front end | Devanagari GOOD in TC (searchable); Tibetan unreadable; transliteration noisy | corpus fact | NEW CONSTRAINT | yes | no | front end must declare per-language readability + must not silently romanize technical terms (rule: no silent normalization) |
| R15 | uncertainty | niścaya/saṃśaya currency WITHOUT grades anywhere new; doubt-sources enumerated (upādhi-suspicion + NS-2.1.6-language) | TC + Book II | STRENGTHENED (doubt-source taxonomy) but BLOCKED as graded spec | yes | no | doubt-source typing required; graded fields stay forbidden |

## R2/R3/R12 sufficiency test (brief's special question)

INSUFFICIENT as currently framed. Three gaps the new corpus exposes:
1. **Readability gap**: R2/R12 assume stratum-tagged terms are READABLE.
   Tibetan body (unreadable here) and un-OCR'd restoration prove readability
   itself must be a provenance field, or tags will certify unread content.
2. **Reconstruction gap**: R2 has no reconstruction-dependence status (PS
   root is restored-from-Tibetan; every Dig claim inherits it).
3. **Exposition-vs-root gap**: R3/R12 do not separate MODERN scholarly
   exposition (Vidyābhūṣaṇa Book II — extensive, accurate-seeming, but
   secondary) from root doctrine. Without this split, Book II content will
   leak into "Navya-Nyāya positions" as if Gaṅgeśa said them in these words.
Proposed revision (C-status hypothesis, not adopted): R2 → R2* (stratification
+ readability + reconstruction-dependence); R3 → R3* (+ exposition/root firewall
+ interwoven-commentary attribution caution); R12 → R12* (+ per-language
readability declaration + no-silent-normalization rule). Adoption requires the
draft in-repo.
