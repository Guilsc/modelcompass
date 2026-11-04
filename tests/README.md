# Tests

From the repository root, with Python 3.11+ and no third-party dependencies:

```bash
python tests/validate_package.py
python tests/run_evaluations.py
python -m unittest discover -s tests -p 'test_*.py'
```

- `validate_package.py`: required files, skill frontmatter markers, JSON parsing.
- `run_evaluations.py`: six policy fixtures have unique IDs, tasks and expectations.
  It does not execute those expectations against an advisor.
- `test_benchmarks.py`: source registry, exact-label filtering, missing evidence,
  source-estimated classifications, provenance validation, invalid numeric scores,
  duplicate observations, dates, age windows and offline CLI behavior.

All checks run offline; no model inference or provider credentials are required.
They are not model performance benchmarks, production integrations or proof that
all hosts install the skill correctly. Synthetic invalid records in unit tests are
validation inputs, not published model measurements. Source snapshot accuracy
still requires a human review of the cited page and its methodology.
