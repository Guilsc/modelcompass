"""Offline checks; synthetic records below are not published model scores."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/model-selector/scripts/benchmarks.py"
spec = importlib.util.spec_from_file_location("benchmarks", SCRIPT)
benchmarks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(benchmarks)


class BenchmarkTests(unittest.TestCase):
    def test_packaged_sources_stay_distinct(self):
        data = benchmarks.load_data()
        self.assertEqual(set(data["sources"]), {"artificial_analysis", "arena", "benchlm", "livebench"})
        report = benchmarks.report(data, source="arena", as_of="2026-11-03")
        self.assertTrue(report["observations"])
        self.assertTrue(all(row["source"] == "arena" for row in report["observations"]))
        self.assertNotIn("combined_score", report)

    def test_absent_model_is_missing_evidence_not_a_zero_score(self):
        result = benchmarks.report(benchmarks.load_data(), model="not-in-snapshot", as_of="2026-11-03")
        self.assertEqual(result["status"], "no_observations")
        self.assertEqual(result["observations"], [])

    def test_missing_score_remains_null_with_reason(self):
        result = benchmarks.report(benchmarks.load_data(), source="arena", as_of="2026-11-03")
        self.assertIsNone(result["observations"][0]["score"])
        self.assertTrue(result["observations"][0]["missing_reason"])

    def test_unknown_publication_is_not_fresh_measurement(self):
        result = benchmarks.report(benchmarks.load_data(), source="livebench", as_of="2026-11-03")
        self.assertEqual(result["observations"][0]["freshness"], "publication_unknown")
        stale = benchmarks.report(benchmarks.load_data(), source="livebench", as_of="2027-01-01")
        self.assertEqual(stale["observations"][0]["freshness"], "stale")

    def test_age_uses_publication_and_window_boundary(self):
        data = benchmarks.load_data()
        for as_of, expected in (("2026-11-28", "within_window"), ("2026-11-29", "stale")):
            with self.subTest(as_of=as_of):
                result = benchmarks.report(data, source="benchlm", as_of=as_of)
                self.assertEqual(result["observations"][0]["freshness"], expected)

    def test_invalid_provenance_and_scores_are_rejected(self):
        for field, value in (("score", True), ("score", float("nan")), ("score", float("inf")),
                             ("score", "59"), ("source", "unknown"), ("source_url", "https://example.org/"),
                             ("published_at", "2027-01-01"), ("observed_at", "bad-date"),
                             ("evidence_kind", "independently_tested"), ("metric", "")):
            with self.subTest(field=field, value=value):
                data = benchmarks.load_data()
                data["observations"][0][field] = value
                with self.assertRaises(ValueError):
                    benchmarks.validate(data)

    def test_duplicate_observations_are_rejected(self):
        data = benchmarks.load_data()
        data["observations"].append(dict(data["observations"][0]))
        with self.assertRaises(ValueError):
            benchmarks.validate(data)

    def test_missing_score_without_reason_is_rejected(self):
        data = benchmarks.load_data()
        data["observations"][1]["missing_reason"] = None
        with self.assertRaises(ValueError):
            benchmarks.validate(data)

    def test_estimated_source_is_not_promoted_to_independent_evidence(self):
        result = benchmarks.report(benchmarks.load_data(), source="benchlm", as_of="2026-11-03")
        self.assertEqual(result["observations"][0]["evidence_kind"], "estimated")

    def test_no_alias_guessing(self):
        result = benchmarks.report(benchmarks.load_data(), model="Gemini 4 Carbon", as_of="2026-11-03")
        self.assertEqual([row["source"] for row in result["observations"]], ["benchlm"])

    def test_invalid_query_is_rejected(self):
        for kwargs in ({"source": "typo"}, {"max_age_days": -1}, {"as_of": "2020-01-01"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                benchmarks.report(benchmarks.load_data(), **kwargs)

    def test_invalid_container_shapes_fail_cleanly(self):
        for data in ([], {"schema_version": 1, "sources": {"broken": []}},
                     {"schema_version": True, "sources": {}}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                benchmarks.validate(data)
        data = benchmarks.load_data()
        data["observations"] = [None]
        with self.assertRaises(ValueError):
            benchmarks.validate(data)


if __name__ == "__main__":
    unittest.main()
