from pathlib import Path
import json
p = Path(__file__).parent / "evaluation-cases.json"
cases = json.loads(p.read_text(encoding="utf8"))
assert len(cases)>=6 and len({x["id"] for x in cases})==len(cases)
assert all(x.get("task") and x.get("expect") for x in cases)
print(f"PASS: {len(cases)} policy fixtures present (not live model benchmarks)")
