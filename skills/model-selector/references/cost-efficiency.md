# Quality-adjusted efficiency and costs

**Primary measure:** total cost per *acceptable completed outcome*, not cheapest output token.

Include input/output tokens, cached-input charges, tool calls, time, image/video/audio units, failed attempts, human review, switching overhead, re-uploaded context and prompt-cache resets. Pricing may differ between API and subscriptions; never pretend subscription limits equal a fixed dollar/token price.

`effective_cost = first_attempt_cost + retries + tools + reloaded_context + switch_overhead + review_cost`

Unverified prices are **unknown** rather than zero. Prefer dated primary provider pricing sources; links in `sources.md`. For media, compare equivalent resolution, duration, quality and rights. High end-user satisfaction and instruction adherence can justify higher nominal costs.

Avoid switching between every inventory, interpretation, planning, move and validation step. Use deterministic utilities for cheap reproducible operations and one model for dependent judgments. Switch when a required capability is absent or expected quality improvement outweighs handoff and cache losses.
