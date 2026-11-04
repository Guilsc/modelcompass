"""Inspect curated benchmark evidence offline; never normalize unrelated metrics."""
import argparse
from datetime import date
import json
import math
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data/benchmarks.json"


def load_data(path=DATA):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    validate(data)
    return data


def validate(data):
    if not isinstance(data, dict):
        raise ValueError("Benchmark data must be an object")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ValueError("Unsupported benchmark schema")
    if not isinstance(data.get("sources"), dict) or not data["sources"]:
        raise ValueError("A source registry is required")
    for source in data["sources"].values():
        if not isinstance(source, dict):
            raise ValueError("Each source must be an object")
        for key in ("name", "url", "checked_at", "method", "limitations"):
            if not isinstance(source.get(key), str) or not source[key].strip():
                raise ValueError(f"Missing source {key}")
        if not source["url"].startswith("https://"):
            raise ValueError("Source URL must use HTTPS")
        date.fromisoformat(source["checked_at"])
    if not isinstance(data.get("observations"), list):
        raise ValueError("Observations must be a list")
    seen = set()
    for row in data["observations"]:
        if not isinstance(row, dict):
            raise ValueError("Each observation must be an object")
        for key in ("source", "model_label", "configuration", "metric", "version", "category",
                    "unit", "direction", "observed_at", "source_url", "evidence_kind", "excerpt"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError(f"Missing observation {key}")
        source = data["sources"].get(row["source"])
        if source is None or row["source_url"] != source["url"]:
            raise ValueError("Observation must reference its registered source URL")
        observed = date.fromisoformat(row["observed_at"])
        if observed > date.fromisoformat(source["checked_at"]):
            raise ValueError("Observation is newer than the source check")
        if "published_at" not in row or "score" not in row or "missing_reason" not in row:
            raise ValueError("Explicit published_at, score and missing_reason are required")
        if row["published_at"] is not None:
            if date.fromisoformat(row["published_at"]) > observed:
                raise ValueError("Publication cannot follow observation")
        if row["direction"] not in ("higher", "lower"):
            raise ValueError("Unknown score direction")
        if row["evidence_kind"] not in ("source_reported", "estimated", "unverified"):
            raise ValueError("Unknown evidence kind")
        score = row["score"]
        if score is None:
            if not isinstance(row["missing_reason"], str) or not row["missing_reason"].strip():
                raise ValueError("Missing score needs a reason, never substitute zero")
        elif type(score) not in (int, float) or not math.isfinite(score):
            raise ValueError("Score must be a finite number or null")
        elif row["missing_reason"] is not None or row["evidence_kind"] == "unverified":
            raise ValueError("Unverified or missing evidence cannot carry a numeric score")
        identity = tuple(row[key] for key in ("source", "model_label", "configuration", "metric",
                                               "version", "category", "observed_at"))
        if identity in seen:
            raise ValueError("Duplicate benchmark observation")
        seen.add(identity)


def report(data, source=None, model=None, as_of=None, max_age_days=30):
    """Return exact-label evidence and freshness, not an inferred global ranking."""
    validate(data)
    today = date.fromisoformat(as_of) if as_of else date.today()
    if max_age_days < 0:
        raise ValueError("max_age_days must be nonnegative")
    if source is not None and source not in data["sources"]:
        raise ValueError(f"Unknown source: {source}")
    rows = []
    for row in data["observations"]:
        if source is not None and row["source"] != source:
            continue
        if model is not None and row["model_label"] != model:
            continue
        observed = date.fromisoformat(row["observed_at"])
        if observed > today:
            raise ValueError("Observation is in the future relative to as_of")
        # Publication age is preferable; retrieval alone does not prove measurement freshness.
        age = (today - date.fromisoformat(row["published_at"] or row["observed_at"])).days
        rows.append({**row, "age_days": age,
                     "freshness": "stale" if age > max_age_days else (
                         "publication_unknown" if row["published_at"] is None else "within_window")})
    return {"as_of": today.isoformat(), "max_age_days": max_age_days,
            "status": "observations_present" if rows else "no_observations",
            "notice": "Partial source-reported evidence only. No cross-source ranking; missing is not zero. Exact labels are not API IDs.",
            "sources": {key: value for key, value in data["sources"].items()
                        if source is None or source == key}, "observations": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DATA)
    parser.add_argument("--source")
    parser.add_argument("--model", help="Exact source model label; no alias guessing")
    parser.add_argument("--as-of", help="ISO date (defaults to today)")
    parser.add_argument("--max-age-days", type=int, default=30)
    args = parser.parse_args()
    try:
        result = report(load_data(args.data), args.source, args.model, args.as_of, args.max_age_days)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))


if __name__ == "__main__":
    main()
