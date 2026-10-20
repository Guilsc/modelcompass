---
name: model-selector
description: Recommend context-appropriate AI models, reasoning effort, and cost-quality tradeoffs for human or agent tasks. Use when the user asks which model to choose, compares settings, or explicitly requests model selection guidance. Respect selected models and ask before switching.
---

# Model Selector

Select models by **whole-task outcome**, not individual microsteps or cheapest token. This skill is **advisory**: it does not imply you can actually switch the underlying model.

## Procedure

1. Identify the full workflow, required output modality, quality floor, privacy restrictions, available platform/models, budget, session continuity, and whether the user has already selected a model.
2. Apply hard eligibility gates: native generation vs understanding, tool availability, language/format fidelity, context capacity, safe operation, and authorized spending. Exclude unqualified candidates before ranking.
3. Read only relevant modules from `references/`: `task-matrix.md` for a matched task; `model-catalog.md` for model capabilities; `reasoning-levels.md` for effort; `cost-efficiency.md` for sessions and cost; `sources.md` to check freshness. Use `data/` only for a machine-readable shortlist, never assume it is exhaustive.
4. Present **Best Fit**, **Best Value**, **Budget**, **Fallback** as justified candidates with evidence tags: **D** provider documented, **E** editorial assessment, **T** independently tested, **U** unverified. Do not invent rankings, tokens, API IDs, prices, or benchmark scores.
5. Prefer one capable lead model across tightly coupled phases when handoffs waste context. Use deterministic utilities for inventory, hashes, moves, builds, tests and validation where possible. Escalate reasoning effort only for concrete unresolved difficulty; do not assume maximum effort is optimal.
6. If the user explicitly specified a capable model or effort, **respect it**. In default **Advisory** mode, suggest an alternative only if materially beneficial, at most once for the same circumstances. Ask whether to use the recommendation, keep their choice, or enter **Grill Me** comparison mode. **Strict preference** suppresses cost nudges. **Auto-select** requires explicit delegation and must obey scope and constraints.
7. Never claim a switch was made unless the host supports it and confirms it. Never delete, move, transmit sensitive data, or incur costs without appropriate authorization. When user rejects an alternative, stop pressing unless facts materially change.

## Existing selectors and routers

If the host already uses a model selector (`/model`, platform picker) or an intelligent router (for example, OmniRouter / OmniRoute, OpenRouter Auto Router, LiteLLM, RouteLLM or Not Diamond), operate as an **advisory layer** and preserve its execution authority. Prefer Observe, Advise, or Defer coexistence modes; these are policies, not API integrations. Check actual selected-model metadata where supported, and do not confuse provider fallback with model selection. Do not install competing automatic policy hooks, silently change routing tables, or claim to have selected a provider when the router may pick or fall back elsewhere. If the user has delegated model selection to the router, do not second-guess every request; offer a second opinion only when explicitly requested or when a meaningful quality/cost issue is evident. Factor in prompt-cache resets and context-transfer costs before suggesting a mid-session switch.

## Response format

**Task / quality floor:** ...
**Current choice (if any):** ...
**Best Fit / Best Value / Budget / Fallback:** ...
**Why and caveats:** quality, reliability, total cost (including switching, retries and context), modalities, evidence/confidence, price freshness.
**Action:** proceed with user preference, suggest a single switch, or ask only an essential missing constraint.

## References

- `references/decision-rules.md`: gates, decision tree, scoring and selection policy.
- `references/task-matrix.md`: initial context-to-model candidates.
- `references/model-catalog.md`: providers and capability notes.
- `references/reasoning-levels.md`: effort guidance.
- `references/cost-efficiency.md`: complete-outcome efficiency.
- `references/advisory-protocol.md`: user override, Grill Me, strict mode.
- `references/sources.md`: source URLs and maintenance requirements.
- `references/router-interoperability.md`: coexistence with model pickers, gateways and intelligent routers.

If the host cannot resolve `references/`, package those files alongside this skill in an installable directory and adjust paths. Full portable specification: `MODEL_HELPER.md`.
