# Acquisition Record — Phase 1.75 (G-NS-01, G-UD-01)

Methods used only the exact user-supplied source information plus already-
authorized locations. No authentication bypassed, no content fabricated, no
substitute edition passed off as the target.

## G-NS-01 — Nyāya-sūtra Vol. 3 (Jha set, Adhyāyas III–V presumed)

- Target: Drive file `15exfrXy9VRb554fuzL4rZGCoJlX-6sn-` (Vol. 3 of the Jha
  Motilal Banarsidass set; presumed Adhyāyas III–V — presumption flagged,
  contents UNVERIFIED and unclaimed).
- Intended source: same edition as acquired Vols. 1–2 (record in
  `corpus/VOLUMES.md`).
- Attempts (2026-09-27, 01:53–01:54 UTC): (1) `gdown uc?id=` form → "Gdown
  can't. Please check connections and permissions." (2) `gdown file/d/…
  /view` form → identical failure. (3) Direct HTTPS GET → HTTP 200,
  916,544 bytes, body = Google sign-in page (auth wall, not content; byte
  count matches Phase 1.5's 916,639 sign-in page signature).
- Result: FAILURE. Failure mode: AUTHENTICATION (resource not publicly
  shared), not network, not missing-file (Drive acknowledges the ID by
  redirecting to sign-in), not transient (identical across Phase 1.5 and
  Phase 1.75, two weeks apart in cache terms but same signature).
- Provenance/integrity: nothing acquired → nothing to hash; no file written
  (retry stubs deleted).
- Legitimate alternative identified? NO. No other authorized location holds
  this volume. Web-search substitutes are explicitly out of bounds (would be
  a different source masquerading as the target).
- Remaining gap: G-NS-01 stays OPEN. Blocked dependents: Adhyāya V
  jāti/nigrahasthāna detail (D3-part, D4-part), 2.1.38-adjacent siddhānta
  parallels in later books, Adhyāya III–IV ātman/duḥkha inference contexts.
  Action: request public sharing from the source owner.

## G-UD-01 — Udayana material (Tātparya-Pariśuddhi per acquisition matrix)

- Target (matrix definition): Udayana's *Tātparya-Pariśuddhi* — the text
  behind the load-bearing asiddha-threefold and two-factor-anumāna fragments
  quoted in Jha's notes (1-2-8/9 region; 2.1.37).
- Specificity check: the matrix specifies WORK (Pariśuddhi) but no EDITION,
  no Drive ID, no authorized location. Per the brief, an underspecified
  target is marked UNRESOLVED rather than guessed at.
- Availability audit: supplied Drive material = three Jha volumes only (Vol. 3
  itself inaccessible). Already-authorized locations (repo, ingest scratch)
  hold NO independent Udayana text — only the Jha-note fragments already
  extracted (see `targeted/ns_1_2_7_prakaranasama.md` Tātparya gloss;
  `concept_matrix.json` vyāpti/hetvābhāsa entries).
- Result: UNRESOLVED — no acquisition attempted beyond the audit, because any
  download (e.g. a web-found Pariśuddhi edition) would substitute an
  unauthorized, unvetted source without user direction. This is deliberate
  restraint, not an omission.
- Remaining gap: G-UD-01 stays OPEN with sharpened scope: needed specifically
  for (a) asiddha-threefold origin (innovation vs transmission), (b) two-
  factor formula wording, (c) any pakṣatā-precursor doctrine (D1-critical),
  (d) upādhi-formula origins (D5-critical). Action: request a specified
  edition (title/editor/year or Drive link) before any download.
