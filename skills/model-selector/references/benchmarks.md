# Benchmark evidence policy

`data/benchmarks.json` is a deliberately partial, manually transcribed snapshot of
public page text retrieved on 2026-11-03. It is not a complete leaderboard. Its
source-reported numbers have not been reproduced by ModelCompass. Run
`scripts/benchmarks.py` relative to the skill directory to inspect evidence offline.
Python 3.11+ is needed only for that optional script, not for reading the skill.

## Use in an advisory response

1. Apply the existing capability, privacy and availability gates first.
2. Find exact source labels/settings relevant to the task. Unknown labels or
   settings mean missing evidence, not permission to merge model variants.
3. Cite source URL, metric, category, version, observation date and known publication
   date. Explain the source's limitations. Unknown publication is not freshness.
4. Keep every source in its own metric space. Do not average, normalize, add ranks,
   or count BenchLM and its upstream sources as independent confirmations.
5. Relate the metric to the actual task. Broad overall performance does not prove
   tool reliability, safety, language fidelity or native modality support.
6. Retain user authority. Evidence inspection never switches models or configures
   routing. Missing or stale evidence calls for verification or lower confidence,
   not a fabricated recommendation.

The local snapshot includes one observation per source, intentionally not enough
for a full within-source ranking. Arena's extracted agent percentage has no clear
metric definition in the captured text, so `score` is null and the listing remains
a quote only. Do not silently relabel it as chat Elo or preference win rate.
Artificial Analysis v5.0 and LiveBench 2.0 are versioned composites as described by
the pages at retrieval time; do not substitute an older suite's methodology.
BenchLM's captured entry is explicitly estimated-ranked.

## Evidence tags

`source_reported` means a number transcribed from that source, **not** a locally
reproduced measurement or automatic **T** evidence for this task. `estimated`
retains the source's estimate classification and is at most **E** in the advisory
protocol. `unverified` is **U**, with a null score and a reason. Promote to **T** only
with independent testing relevant to the specific task and documented settings.
Provider documentation (**D**) is separate from these benchmark observations.

## Updating the snapshot

- Inspect the exact public source and methodology; respect licensing and access
  restrictions. No provider inference or paid API call is needed for this file.
- Preserve exact display labels, reasoning settings and variants. Do not invent an
  API ID or fill an unknown configuration with a default.
- Register each source URL, check date, capture method and limitations. Each row
  must reference that registered URL and include an excerpt supporting its value.
- Record metric, category, version, unit and direction. Use `not reported` when
  version or configuration cannot be established. If the metric itself is unclear,
  retain the quote only and leave `score` null with `missing_reason`.
- Record `observed_at` and nullable `published_at` separately; retrieval dates are
  not publication or measurement dates. Explicitly preserve missing scores as null.
- Keep source-estimated entries `estimated`; never imply independent replication.
  Do not import prices into the benchmark score field.
- Run all checks in the root README. Review the source content as well as the
  schema: validation cannot establish that a transcribed claim is true.

## Inspector contract

The script reads only local JSON (default: sibling `data/benchmarks.json`), validates
it, then emits source metadata and observations. `--data PATH` inspects a different
snapshot with the same schema. `--source` is an exact registry key; unknown keys
fail. `--model` matches an exact case-sensitive display label; no match succeeds
with `no_observations`. There is no combined score or automated ranking.

Freshness uses publication age when available, otherwise observation age. A row
older than `--max-age-days` is `stale`; within the window it is `within_window`
only with a publication date, otherwise `publication_unknown`. This is an age
warning, not assurance of valid measurement. Future observations, negative age
windows, invalid dates, duplicate identities, nonfinite/bool scores, missing
provenance and unverified numeric claims fail validation or reporting. Error
messages go to stderr with nonzero exit; valid JSON goes to stdout.
