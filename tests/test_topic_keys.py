#!/usr/bin/env python3
"""Unit tests for tools/topic_keys.py, tools/url_norm.py, and
tools/update_reports_index.py. Uses stdlib unittest so no pytest dependency.

Run from the project root:
    python3 -m unittest tests.test_topic_keys -v
or:
    python3 tests/test_topic_keys.py
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "tools"))

from tools import topic_keys  # noqa: E402
from tools.topic_keys import topic_key, load_rules, annotate_envelope  # noqa: E402
try:
    from tools.topic_keys import make_bill_key, session_to_year  # noqa: E402
except ImportError:
    make_bill_key = None
    session_to_year = None
try:
    from tools.bill_processor import bill_key  # noqa: E402
except ImportError:
    bill_key = None
from tools.url_norm import normalize_url  # noqa: E402
from tools import update_reports_index as uri  # noqa: E402


class TopicKeyStateBillTests(unittest.TestCase):
    """State bill topic key generation — short forms, long forms, edge cases."""

    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()

    def _mk(self, title, jurisdiction, date="2026-04-10", summary="", dev_type="legislation"):
        return {
            "title": title,
            "summary": summary,
            "jurisdiction": jurisdiction,
            "date": date,
            "development_type": dev_type,
            "source": "",
        }

    def test_short_form_hb(self):
        key, conf, typ = topic_key(self._mk("Illinois HB 3069 Advances", "Illinois"), self.rules)
        self.assertEqual(key, "IL-HB-3069-2026")
        self.assertEqual(conf, "high")
        self.assertEqual(typ, "state_bill")

    def test_short_form_sb(self):
        key, conf, typ = topic_key(self._mk("Oregon SB 1546 Introduced", "Oregon"), self.rules)
        self.assertEqual(key, "OR-SB-1546-2026")
        self.assertEqual(conf, "high")

    def test_short_form_ab(self):
        key, conf, _ = topic_key(self._mk("California AB 3048 Browser Controls", "California"), self.rules)
        self.assertEqual(key, "CA-AB-3048-2026")
        self.assertEqual(conf, "high")

    def test_long_form_house_bill(self):
        # "House Bill 351" should map to HB
        key, conf, _ = topic_key(
            self._mk(
                "Alabama set to add variation",
                "Alabama",
                summary="House Bill 351 cleared the state legislature",
            ),
            self.rules,
        )
        self.assertEqual(key, "AL-HB-351-2026")
        self.assertEqual(conf, "high")

    def test_long_form_senate_bill(self):
        key, conf, _ = topic_key(
            self._mk(
                "Oklahoma privacy bill advances",
                "Oklahoma",
                summary="Senate Bill 1972 unanimously passed committee",
            ),
            self.rules,
        )
        self.assertEqual(key, "OK-SB-1972-2026")
        self.assertEqual(conf, "high")

    def test_long_form_legislative_document(self):
        # Maine uses LD prefix
        key, conf, _ = topic_key(
            self._mk(
                "Maine privacy bill fails",
                "Maine",
                summary="Legislative Document 1822 voted down on concurrence",
            ),
            self.rules,
        )
        self.assertEqual(key, "ME-LD-1822-2026")
        self.assertEqual(conf, "high")

    def test_long_form_legislative_bill_nebraska(self):
        key, conf, _ = topic_key(
            self._mk(
                "Nebraska AI bill",
                "Nebraska",
                summary="Legislative Bill 1175 targets AI companion chatbots",
            ),
            self.rules,
        )
        self.assertEqual(key, "NE-LB-1175-2026")
        self.assertEqual(conf, "high")

    def test_non_us_legislation_routes_to_other(self):
        # Nigeria is not a US state — should NOT be state_bill
        key, conf, typ = topic_key(
            self._mk("Nigeria AI regulation", "Nigeria"),
            self.rules,
        )
        self.assertEqual(typ, "other")
        # Fallback gives low confidence hash key
        self.assertEqual(conf, "low")
        self.assertTrue(key.startswith("nigeria-"))

    def test_missing_date_defaults_to_current_year(self):
        # No date field → topic_keys defaults to current UTC year
        finding = self._mk("Texas HB 42 introduced", "Texas", date="")
        finding.pop("date")
        key, _, _ = topic_key(finding, self.rules)
        from datetime import datetime, timezone
        current_year = str(datetime.now(timezone.utc).year)
        self.assertEqual(key, f"TX-HB-42-{current_year}")


class TopicKeyEnforcementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()

    def _mk(self, title, source, summary="", jurisdiction="Federal", dev_type="enforcement"):
        return {
            "title": title,
            "summary": summary,
            "source": source,
            "jurisdiction": jurisdiction,
            "development_type": dev_type,
            "date": "2026-04-10",
        }

    def test_ftc_with_target(self):
        key, conf, typ = topic_key(
            self._mk("FTC Settles With Disney for $2.75 Million", "Federal Trade Commission"),
            self.rules,
        )
        self.assertEqual(key, "FTC-DISNEY-2026")
        self.assertEqual(conf, "high")
        self.assertEqual(typ, "enforcement")

    def test_ca_ag_enforcement(self):
        key, conf, _ = topic_key(
            self._mk(
                "California AG Bonta Announces Record Settlement With Disney",
                "California Attorney General",
            ),
            self.rules,
        )
        self.assertEqual(key, "CAAG-DISNEY-2026")
        self.assertEqual(conf, "high")

    def test_no_regulator_falls_back(self):
        key, conf, _ = topic_key(
            self._mk("Generic enforcement action", "Private blog"),
            self.rules,
        )
        self.assertEqual(conf, "low")
        self.assertTrue("-" in key)


class TopicKeyRulemakingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()

    def test_ftc_rulemaking_with_docket(self):
        finding = {
            "title": "FTC Final Rule Amending COPPA, Docket No. P-205404",
            "summary": "",
            "source": "FTC",
            "jurisdiction": "Federal",
            "development_type": "regulation",
            "date": "2026-04-10",
        }
        key, conf, typ = topic_key(finding, self.rules)
        self.assertEqual(typ, "rulemaking")
        self.assertEqual(key, "FTC-P-205404")
        self.assertEqual(conf, "high")


class TopicKeyGuidanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()

    def test_nist_guidance_strips_org_from_slug(self):
        finding = {
            "title": "NIST Releases GenAI Profile NIST AI 600-1",
            "source": "NIST",
            "jurisdiction": "Federal",
            "development_type": "guidance",
            "date": "2026-04-10",
            "summary": "",
        }
        key, conf, typ = topic_key(finding, self.rules)
        self.assertEqual(typ, "guidance")
        self.assertTrue(key.startswith("NIST-"))
        self.assertNotIn("NIST-NIST", key)  # stripped
        self.assertEqual(conf, "medium")


class DeterminismTests(unittest.TestCase):
    """Same input → same output, regardless of call count or ordering."""

    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()

    def test_same_finding_same_key(self):
        finding = {
            "title": "Illinois HB 3069",
            "summary": "",
            "jurisdiction": "Illinois",
            "development_type": "legislation",
            "date": "2026-04-10",
            "source": "",
        }
        k1 = topic_key(finding, self.rules)
        k2 = topic_key(finding, self.rules)
        self.assertEqual(k1, k2)

    def test_field_order_insensitive(self):
        f1 = {
            "title": "Florida SB 1722",
            "jurisdiction": "Florida",
            "development_type": "legislation",
            "date": "2026-04-10",
            "summary": "",
            "source": "",
        }
        f2 = {
            "source": "",
            "date": "2026-04-10",
            "summary": "",
            "development_type": "legislation",
            "jurisdiction": "Florida",
            "title": "Florida SB 1722",
        }
        self.assertEqual(topic_key(f1, self.rules), topic_key(f2, self.rules))


class AnnotateIdempotencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()

    def test_annotate_twice_identical(self):
        envelope = {
            "schema_version": "1.0",
            "timestamp": "2026-04-10T14:00:00Z",
            "data": {
                "findings": [
                    {"id": "SCAN-1", "title": "Illinois HB 3069", "summary": "",
                     "jurisdiction": "Illinois", "development_type": "legislation",
                     "date": "2026-04-10", "source": "", "source_url": "https://example.com/1"},
                    {"id": "SCAN-2", "title": "FTC Settles With Disney", "summary": "",
                     "jurisdiction": "Federal", "development_type": "enforcement",
                     "date": "2026-04-10", "source": "Federal Trade Commission",
                     "source_url": "https://example.com/2"},
                ],
            },
        }
        import copy
        e1 = copy.deepcopy(envelope)
        e2 = copy.deepcopy(envelope)
        annotate_envelope(e1, self.rules)
        annotate_envelope(e2, self.rules)
        self.assertEqual(
            json.dumps(e1, sort_keys=True),
            json.dumps(e2, sort_keys=True),
        )

    def test_annotate_preserves_existing_keys(self):
        envelope = {
            "schema_version": "1.0",
            "timestamp": "2026-04-10T14:00:00Z",
            "data": {
                "findings": [
                    {"id": "SCAN-1", "title": "Illinois HB 3069",
                     "jurisdiction": "Illinois", "development_type": "legislation",
                     "date": "2026-04-10",
                     "topic_key": "PRE-EXISTING-KEY-2026",
                     "topic_type": "state_bill",
                     "topic_key_confidence": "high"},
                ],
            },
        }
        annotate_envelope(envelope, self.rules)
        self.assertEqual(
            envelope["data"]["findings"][0]["topic_key"],
            "PRE-EXISTING-KEY-2026",
        )


class UrlNormTests(unittest.TestCase):
    def test_http_to_https(self):
        self.assertEqual(normalize_url("http://example.com/"), "https://example.com")

    def test_strip_utm(self):
        self.assertEqual(
            normalize_url("https://a.com/b?utm_source=x&utm_medium=y"),
            "https://a.com/b",
        )

    def test_strip_lexology_g_param(self):
        self.assertEqual(
            normalize_url("https://lexology.com/library/detail.aspx?g=abc123"),
            "https://lexology.com/library/detail.aspx",
        )

    def test_drop_trailing_slash_and_q(self):
        self.assertEqual(normalize_url("https://a.com/b/"), "https://a.com/b")
        self.assertEqual(normalize_url("https://a.com/b?"), "https://a.com/b")

    def test_empty_input(self):
        self.assertEqual(normalize_url(""), "")
        self.assertEqual(normalize_url(None or ""), "")

    def test_identical_across_callers(self):
        # Verify the bash shim and Python import produce the same result
        import subprocess
        url = "http://example.com/x?utm_source=n&g=t"
        py_result = normalize_url(url)
        shell_result = subprocess.check_output(
            ["python3", str(PROJECT_ROOT / "tools/url_norm.py"), url],
            text=True,
        ).strip()
        self.assertEqual(py_result, shell_result)


class CrossIndexMergeTests(unittest.TestCase):
    """I1: FPF bill cross-index must not clobber pre-existing Lexology entries."""

    def test_fpf_does_not_overwrite_lexology_report_path(self):
        from tools import bill_processor
        index = {
            "schema_version": "1.0",
            "reports": {
                "KY-HB-692-2026": {
                    "topic_key": "KY-HB-692-2026",
                    "topic_type": "state_bill",
                    "report_path": "reports/privacy/kentucky-hb692-real-report.md",
                    "title": "Kentucky HB 692 Real Lexology Report",
                    "category": "privacy",
                    "subcategory": "state-comprehensive-laws",
                    "source_urls": ["https://existing.example.com/ky-hb692"],
                    "first_reported": "2026-04-07",
                    "last_updated": "2026-04-07",
                    "current_status": "introduced",
                    "status_history": [],
                    "finding_ids": ["SCAN-20260407-009"],
                },
            },
            "url_index": {"https://existing.example.com/ky-hb692": "KY-HB-692-2026"},
        }
        bill = {
            "state_abbrev": "KY", "state": "Kentucky",
            "bill_identifier": "HB 692",
            "title": "KCDPA Amendment: ACR Sensitive Data",
            "category": ["privacy"],
            "bill_text_url": "https://apps.legislature.ky.gov/record/26rs/hb692.html",
            "status": "passed-committee",
        }
        bill_processor._cross_index_bill_to_reports(
            index,
            entry={"bill_dir": "bills/kentucky/HB-692"},
            key="KY-HB-692-2026",
            bill=bill,
            run_id="test-run",
        )
        updated = index["reports"]["KY-HB-692-2026"]
        # Lexology report_path preserved
        self.assertEqual(updated["report_path"], "reports/privacy/kentucky-hb692-real-report.md")
        self.assertEqual(updated["subcategory"], "state-comprehensive-laws")
        # Bill URL merged in
        self.assertIn("https://apps.legislature.ky.gov/record/26rs/hb692.html", updated["source_urls"])
        self.assertIn("https://existing.example.com/ky-hb692", updated["source_urls"])
        # Status updated from FPF
        self.assertEqual(updated["current_status"], "passed-committee")
        # Finding ID appended
        self.assertIn("FPF-test-run", updated["finding_ids"])
        self.assertIn("SCAN-20260407-009", updated["finding_ids"])


class ReportsIndexAtomicWriteTests(unittest.TestCase):
    def setUp(self):
        # Work in a temp directory so we don't touch the real reports/index.json
        self.tmp = tempfile.mkdtemp()
        self.index_path = Path(self.tmp) / "index.json"

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp)

    def test_add_new_entry(self):
        index = uri.load_index(self.index_path)
        uri.add_entry(index, {
            "topic_key": "TEST-BILL-1-2026",
            "topic_type": "state_bill",
            "topic_key_confidence": "high",
            "report_path": "reports/privacy/test-bill-1.md",
            "title": "Test Bill 1",
            "category": "privacy",
            "source_urls": ["https://example.com/1"],
        })
        uri.save_index(index, self.index_path)
        self.assertTrue(self.index_path.exists())
        loaded = json.loads(self.index_path.read_text())
        self.assertIn("TEST-BILL-1-2026", loaded["reports"])
        self.assertEqual(
            loaded["url_index"]["https://example.com/1"],
            "TEST-BILL-1-2026",
        )

    def test_add_existing_merges_urls(self):
        index = uri.load_index(self.index_path)
        uri.add_entry(index, {
            "topic_key": "TEST-BILL-1-2026",
            "topic_type": "state_bill",
            "report_path": "reports/privacy/test-bill-1.md",
            "title": "Test Bill 1",
            "category": "privacy",
            "source_urls": ["https://example.com/1"],
        })
        uri.add_entry(index, {
            "topic_key": "TEST-BILL-1-2026",
            "topic_type": "state_bill",
            "report_path": "reports/privacy/test-bill-1.md",
            "title": "Test Bill 1",
            "category": "privacy",
            "source_urls": ["https://example.com/2"],
        })
        entry = index["reports"]["TEST-BILL-1-2026"]
        self.assertIn("https://example.com/1", entry["source_urls"])
        self.assertIn("https://example.com/2", entry["source_urls"])

    def test_append_status_increments_update_count(self):
        index = uri.load_index(self.index_path)
        uri.add_entry(index, {
            "topic_key": "TEST-BILL-1-2026",
            "topic_type": "state_bill",
            "report_path": "reports/privacy/test-bill-1.md",
            "title": "Test Bill 1",
            "category": "privacy",
            "source_urls": [],
        })
        uri.append_status(
            index,
            key="TEST-BILL-1-2026",
            status="passed-committee",
            date="2026-04-11",
            finding_id="SCAN-999",
            run_id="test-run",
        )
        entry = index["reports"]["TEST-BILL-1-2026"]
        self.assertEqual(entry["update_count"], 1)
        self.assertEqual(entry["current_status"], "passed-committee")
        self.assertEqual(len(entry["status_history"]), 1)


class UnifiedBillKeyTests(unittest.TestCase):
    """Task 11: unified bill key builder — make_bill_key, session_to_year, federal bills as US-*."""

    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()

    def test_federal_bill_gets_us_key(self):
        finding = {
            "title": "Congress passes HB 1234 on AI safety",
            "jurisdiction": "Federal",
            "development_type": "legislation",
            "date": "2026-03-01",
        }
        key, confidence, topic_type = topic_key(finding, self.rules)
        self.assertEqual(topic_type, "federal_bill")
        self.assertEqual(key, "US-HB-1234-2026")
        self.assertEqual(confidence, "high")

    def test_state_bill_key_unchanged(self):
        finding = {
            "title": "Virginia SB 338 advances",
            "jurisdiction": "Virginia",
            "development_type": "legislation",
            "date": "2026-02-01",
        }
        key, _, _ = topic_key(finding, self.rules)
        self.assertEqual(key, "VA-SB-338-2026")

    def test_session_to_year_plain(self):
        self.assertEqual(session_to_year("2026"), "2026")

    def test_session_to_year_range(self):
        self.assertEqual(session_to_year("2025-2026"), "2026")

    def test_session_to_year_empty(self):
        self.assertEqual(session_to_year(""), "")

    def test_bill_processor_and_topic_keys_agree_state(self):
        self.assertEqual(bill_key("VA", "SB 338", "2026"), "VA-SB-338-2026")

    def test_bill_processor_and_topic_keys_agree_federal(self):
        self.assertEqual(bill_key("US", "HB 1234", "2025-2026"), "US-HB-1234-2026")

    def test_make_bill_key_dot_forms(self):
        self.assertEqual(make_bill_key("VA", "S.B.", "338", "2026"), "VA-SB-338-2026")

    def test_make_bill_key_preserves_bill_number_case(self):
        # Name-slug tracker entries (e.g. "US-AI-Guardrails-2026") depend on
        # bill_number keeping its persisted mixed case.
        self.assertEqual(
            make_bill_key("US", "HR", "AI-Guardrails", "2026"),
            "US-HR-AI-Guardrails-2026",
        )
        # state_abbrev is always uppercased.
        self.assertEqual(make_bill_key("us", "HB", "1234", "2026"), "US-HB-1234-2026")

    def test_make_bill_key_preserves_bill_type_case(self):
        # Name-slug tracker entries where parts[0] is a mixed-case word
        # (e.g. "Lofgren Comprehensive Privacy Bill" -> "US-Lofgren-Comprehensive-2026")
        # depend on bill_type case being preserved too. Genuine bill types are
        # already uppercased by the scanner path before reaching make_bill_key.
        self.assertEqual(
            bill_key("US", "Lofgren Comprehensive Privacy Bill (Discussion Draft)", "2026"),
            "US-Lofgren-Comprehensive-2026",
        )
        self.assertEqual(
            bill_key("US", "The GUARD Act", "2026"),
            "US-The-GUARD-2026",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
