# Evidence and maintenance

Sources are reference entry points, **not proof of a specific current model ranking**. Recheck before quoting exact API IDs, pricing, quotas, capabilities or performance.

- OpenAI models: https://platform.openai.com/docs/models
- OpenAI pricing: https://openai.com/api/pricing/
- Anthropic models: https://docs.anthropic.com/en/docs/about-claude/models/overview
- Anthropic pricing: https://www.anthropic.com/pricing
- Google Gemini models: https://ai.google.dev/gemini-api/docs/models
- Google Gemini pricing: https://ai.google.dev/gemini-api/docs/pricing
- OpenRouter models: https://openrouter.ai/models
- LiteLLM catalog: https://github.com/BerriAI/litellm
- Artificial Analysis model comparisons: https://artificialanalysis.ai/models
- Arena category leaderboards: https://arena.ai/leaderboard
- BenchLM aggregate and estimated rankings: https://benchlm.ai/
- LiveBench versioned benchmark: https://livebench.ai/

A partial dated snapshot from these four sites lives in `../data/benchmarks.json`.
See [benchmark policy](benchmarks.md) before using it. Source-reported performance
is not automatically task-specific **T** evidence; BenchLM may reuse upstream
evidence. Missing scores remain null and unrelated metrics stay separate.

- Agent Skills standard: https://agentskills.io/specification

Evidence tags: **D** directly documented; **T** independently tested for this specific task; **E** editorial estimate; **U** unknown/unverified. Every exact commercial datum needs provider, model ID, currency/unit, measured or published timestamp, source URL, and limitations. Avoid stale leaderboards masquerading as benchmarks.
