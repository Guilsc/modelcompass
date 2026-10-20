# Existing routers and model pickers

ModelCompass is an **advisor, not an inference gateway, auto-router, execution engine, or replacement for built-in model selection**.

Examples: Hermes `/model`, OmniRouter/OmniRoute, OpenRouter Auto Router, LiteLLM, RouteLLM, Not Diamond and future systems. Exact availability, model controls, and features must be checked at use time.

- **Observe:** Explain actual selection when the host exposes it; don't invent routed-model identity.
- **Advise:** Offer a second opinion on model fit, quality floor, effort or routing constraints; ask permission before making changes.
- **Defer:** Let an existing automatic router manage selection; avoid competing policy hooks or repeated advice.

The model recommended by this skill may not be the model ultimately executed by a router. Model selection, aliases, fallback and provider routing can be separate. Switching mid-session can invalidate prompt caches and duplicate context. Always evaluate whole-workflow cost. No live router API integration is bundled or claimed.
