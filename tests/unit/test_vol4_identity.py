"""Source-identity and traceability-consistency checks for Jha Vol. 4.

Scope (per project mandate): identity, expected SHA-256, metadata, and
referenced-sutra/page-location consistency ONLY. No semantic tests: nothing
here assumes any unresolved interpretation (all D-decisions stay OPEN).
Stdlib unittest only, matching repository conventions.
"""
import json
import os
import re
import unittest

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
IDENTITY = os.path.join(REPO, "research", "classical_sources", "corpus",
                         "VOL4_IDENTITY.json")
ADJUDICATION = os.path.join(REPO, "research", "traceability",
                             "JHA_VOL4_ADJUDICATION.md")

REQUIRED_FIELDS = ["filename", "file_type", "size_bytes", "pdf_pages",
                   "sha256", "translator", "volume", "coverage",
                   "drive_source"]


class Vol4IdentityTests(unittest.TestCase):
    def test_identity_record_valid(self):
        with open(IDENTITY, "r", encoding="utf-8") as f:
            meta = json.load(f)
        for field in REQUIRED_FIELDS:
            self.assertIn(field, meta, f"missing field {field}")
        self.assertEqual(meta["file_type"], "PDF")
        self.assertGreater(meta["size_bytes"], 0)
        self.assertGreater(meta["pdf_pages"], 0)
        self.assertRegex(meta["sha256"], r"^[0-9a-f]{64}$")
        self.assertIn("IV", meta["volume"])
        self.assertIn("edition", meta["coverage"])

    def test_adjudication_file_present(self):
        self.assertTrue(os.path.exists(ADJUDICATION),
                        "JHA_VOL4_ADJUDICATION.md missing")

    def test_referenced_sutra_locations_consistent(self):
        with open(ADJUDICATION, "r", encoding="utf-8") as f:
            text = f.read()
        for sutra in ["4.1.5", "5-1-9", "5-1-14", "5-1-19", "5-1-40",
                      "5-2-1", "5-2-22", "1.2.7", "2.1.37"]:
            self.assertIn(sutra, text, f"sutra ref {sutra} missing")
        for page in ["1438", "1687", "1736", "1769"]:
            self.assertIn(page, text, f"Jha page {page} missing")

    def test_no_resolution_claims(self):
        with open(ADJUDICATION, "r", encoding="utf-8") as f:
            text = f.read()
        self.assertNotRegex(text, r"Status: RESOLVED")
        self.assertIn("remain OPEN", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
