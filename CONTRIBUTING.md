# Contributing

Thanks for helping make model advice more evidence-driven. Contributions should improve real task outcomes, not promote a vendor.

## Good first contributions

- Fix unclear model names or outdated links with primary-source citations and verification dates.
- Add task scenarios to `tests/evaluation-cases.json` with explicit quality floors.
- Report genuine installation behavior (agent, OS, runtime, version, commands, observed result).
- Propose a model recommendation with comparable task outputs, latency, full cost, retries, and caveats.

## Change policy

- Do **not** silently change frozen V2.1 user-control rules. Propose any policy change separately first.
- Mark evidence `D`, `E`, `T`, or `U` accurately. `T` requires a reproducible outcome, not a provider's marketing benchmark.
- No invented performance scores, unlimited-context claims, prices, subscription quotas, or unavailable model IDs.
- Keep `skills/model-selector/SKILL.md` compact; load details on demand.
- Do not commit API keys, private source code, user data, model provider output without rights, or benchmark data with unclear licensing.
- Run `python tests/validate_package.py`, `python tests/run_evaluations.py`, and
  `python -m unittest discover -s tests -p 'test_*.py'` before proposing changes.

## Source-reported benchmark updates

Follow [`references/benchmarks.md`](skills/model-selector/references/benchmarks.md)
when updating `skills/model-selector/data/benchmarks.json`. Keep each source's
metric, version, settings, category, units, excerpt and dates distinct. Preserve
estimated classifications, null scores and missing reasons. Do not average
leaderboards or treat BenchLM's upstream evidence as independent corroboration.
The optional offline inspector uses Python 3.11+ and no dependencies or API keys.

Never run paid provider inference merely to validate the repository. Existing
policy fixtures are structural checks, not measured recommendation accuracy.

## Proposed benchmark record

Record task ID, model/provider/version, date, reasoning setting, tool availability, dataset and reproduction method, output quality criteria, pass/fail evidence, retries, wall time, input/output tokens where available, media generation units, actual billing basis, and privacy restrictions. Keep uncertainty explicit.

By contributing, you agree to publish your original contributions under the MIT license.