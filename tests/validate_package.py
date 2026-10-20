from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
skill = root / "skills/model-selector"
assert (root/"README.md").exists()
s = (skill/"SKILL.md").read_text(encoding="utf8")
assert s.startswith("---\n") and "name: model-selector" in s
for f in ("model-catalog.md","task-matrix.md","decision-rules.md","reasoning-levels.md","cost-efficiency.md","advisory-protocol.md","sources.md","router-interoperability.md"):
    assert (skill/"references"/f).is_file(), f
for f in ("models.json","tasks.json","recommendations.json","pricing.json"):
    json.loads((skill/"data"/f).read_text(encoding="utf8"))
assert "strict" in s.lower() and "router" in s.lower()
print("PASS: ModelCompass layout and machine-readable resources")
