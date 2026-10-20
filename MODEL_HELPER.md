# MODEL_HELPER.md — V2.1 FINAL

> **Status:** Final consolidated specification and living selection reference (design frozen; model data versioned). **Reviewed:** 2026-10-20.  
> **Purpose:** Match a human or agent's *actual work* to a capable, reliable, cost-efficient model. Independent of IDE, agent framework, router, provider, and subscription.  
> **Evidence key:** **D** documented by provider; **E** editorial/inferred practical recommendation; **T** independently task-tested (do not label T without test data); **U** pricing/capability not yet verified.  
> **Warning:** Recommendations marked E are candidates, not proven head-to-head winners. Provider pricing and names change. Verify current billing before material spending.

## Governing principles and authority

1. **User choice is authoritative.** A specified model, vendor, reasoning level, or deployment constraint is a preference/requirement, not something to secretly override. Ask before changing it, unless the user explicitly delegates model selection.
2. **Recommend, do not enforce.** Suggest a different option only when capability, quality, reliability, cost, privacy, or end-to-end efficiency could improve *materially*. Never turn a tiny possible saving into a negotiation.
3. **Optimize per complete outcome.** Include context transfer, latency, retries, human review, tool cost, and work already completed. Do not change models just because the task moves from inventory to analysis to file moves.
4. **Keep quality floors and safety constraints.** Cheap but unstable answers, wrong-language drift, broken references, or unverified file deletion fail the quality gate.
5. **Be honest about control.** An agent may recommend a change but must not claim a model or reasoning mode was switched unless its host actually changed it. If changing requires a new session, explain that.
6. **Distinguish evidence.** Provider claims establish features, not comparative leadership; rankings are editorial until measured on representative workloads.

## Read me first — the 60-second selector

1. **What is the output?** Text/code, understanding images/video/audio, generating/editing images, generating video, voice/music, extraction, embeddings, or deterministic file operations. Do not confuse *understanding* with *generation*.
2. **What is the job?** Select a row in the task matrix. Keep the *whole workflow* in view; don't change models merely because its next step has a different label.
3. **Any must-haves?** Minimum language accuracy, instruction fidelity, native modality, context, tool access, file safety, data/privacy limits, budget, output format.
4. **Choose one of four options:** Best Fit (quality-first), Best Value (quality per total work), Budget (only above quality floor), Fallback (if unavailable or failed).
5. **Prefer the existing capable model** if switching requires restating context or jeopardizes consistency. Switch on a *meaningful phase boundary* or after an evidenced failure, not for every microtask.
6. **Pick reasoning effort separately** and validate with real checks. `medium` is a reasonable general starting point for complex, revisable engineering work; escalation requires a concrete reason.

### End-to-end rule (important)

**Optimize expected cost of a validated result**, not cheapest tokens and not the best per-microtask benchmark. A single balanced model can be more efficient than three specialized LLMs if handoff/context costs exceed specialization benefits. For file moves, scripts are preferable to having a model manually manipulate every file.

## Advisory, Grill Me, and explicit user override protocol

**Default mode: Advisory.** For a user-selected capable model, proceed unless there is a *material* downside. If another choice would noticeably improve cost or quality, offer it **once** with a concise reason and continue according to the user's decision. Never quietly override a specified model, reasoning effort, paid tier, privacy requirement, or tool limit.

| Mode | Trigger and behavior | Model changes allowed? |
|---|---|---|
| **Advisory** (default) | Respect explicit choices; surface only meaningful improvements or capability mismatches. One brief decision, not constant interruptions. | Only if approved or pre-delegated |
| **Grill Me** (on request) | Ask targeted questions about goal, quality, budget, sensitivity, modalities, session continuity; compare 2–4 concrete options and tradeoffs. | User chooses |
| **Strict preference** | Honor the selected model/settings, suppress optimization nudges. Warn only for impossibility, safety, or nonnegotiable incompatibility. | No implicit change |
| **Auto-select** (explicit delegation only) | Agent selects within the user's approved budget, provider, privacy, quality and switch boundaries; logs its choice. | Yes, within delegation |

### Recommendation triggers and non-triggers

**Offer an alternative** when a selected model cannot produce the required modality; repeated validated failures show unreliable language/instruction compliance; a much cheaper capable option provides a meaningful *whole-workflow* saving; the chosen effort level adds measurable latency/tokens without benefit; or privacy, budget, tooling, availability, or context limits require a different plan.

**Do not interrupt** when the user explicitly says they prefer a model, the selected model works, the benefit is speculative/marginal, a model switch would discard valuable context, or the user already declined that proposal for this task. Prefer a new proposal only if material new evidence appears.

### The one-time selection prompt

> **Current choice:** [model, reasoning effort, platform]. **Recommendation:** [model, effort]. **Reason:** [1–2 sentences describing concrete quality, cost, or capability difference]. **Switching overhead:** [none / checkpoint or new session]. **Confidence:** [documented / editorial / tested]. Would you like to **(A) use the recommendation, (B) keep your choice, or (C) compare options / Grill Me**?

If the user answers **B**, proceed with their choice and don't re-litigate. If **C**, compare alternatives with evidence and ask only missing questions that could change the decision. If **A**, apply only if this environment supports switching; otherwise provide exact instructions for the user's tool. If no model was specified, provide a default with a short rationale and continue when permitted.

### Model preference scope

- **One action:** choice applies to this step, unless the user says otherwise.
- **One workflow/session:** preserve choice for related steps and checkpoints; avoid repeatedly asking.
- **Project-wide policy:** only apply if the user explicitly asks; do not assume a one-time choice persists forever.
- **Strict constraints:** a user prohibition on providers, data sharing, spending, or external actions is a hard gate, never an advisory override.

### Reasoning-effort challenge example

**User:** "Restructure my folders with GPT-6.1 Sol, Extreme." **Assistant:** "That model is suitable. Medium is likely sufficient for the inventory, classification and proposed moves; Extreme may raise usage and latency without improving validated results. I recommend staying on Sol at Medium, using scripts for mechanical moves. Keep Extreme, switch to Medium, or compare?" After the answer, do not ask again without a concrete changed circumstance. **Extreme** is not assumed to be an official API effort label; verify what the specific product exposes.

### If advice conflicts with user's request

A user-chosen model may be suboptimal yet acceptable. Follow it after communicating a meaningful tradeoff once. If it *cannot* perform the requested output (e.g., a text-only model required to return native video), explain the incompatibility and present the minimum necessary alternative. Do not silently route to another paid service.

## Matrix A — human/task selection

*B = Best Fit; V = Best Value; $ = candidate Budget; F = fallback. Every recommendation is E unless otherwise noted. Models listed are initial candidates; availability may vary across surfaces.*

| Context / objective | B | V | $ | F | What proves completion |
|---|---|---|---|---|---|
| Casual chat, explain ideas, multilingual continuity | GPT-6.1 Sol Low/Medium | GPT-6.1 Sol Low | GPT-6 Luna *if language quality holds* | Claude Sonnet 5.5 | Stable requested language, useful answer, few corrections |
| Brainstorm with nuance and tradeoffs | GPT-6 Astra Medium | GPT-6.1 Sol Medium | Gemini 3.8 Flash | Claude Sonnet 5.5 | Specific alternatives, constraints, counterarguments |
| Folder structure / codebase architecture | GPT-6 Astra Medium/High for high-stakes work | **GPT-6.1 Sol Medium** | Gemini 3.8 Flash | Claude Sonnet 5.5 | Agreed boundaries, no broken imports, reproducible rationale |
| Audit filesystem, find orphans and duplicate files | GPT-6.1 Sol Medium | Scripts + GPT-6.1 Sol Low/Medium | Scripts + GPT-6 Luna | Gemini 3.8 Flash | Inventory and hashes; evidence before deletion |
| Assess relevant vs junk vs shared agent resources | GPT-6.1 Sol Medium | **Keep same model throughout audit** | Gemini 3.8 Flash for bounded classification | Claude Sonnet 5.5 | Classification with reasons, confidence, safe quarantine |
| Plan and execute refactor | Claude Opus 5.5 for difficult agentic code | GPT-6.1 Sol Medium or Claude Sonnet 5.5 | GPT-6 Luna on tiny explicit patches | Gemini 3.8 Flash | Tests, typecheck, references, behavior unchanged |
| Vibe coding / implement feature | Claude Sonnet 5.5 | GPT-6.1 Sol Medium | DeepSeek V4.1 Flash *pilot before trusting* | Gemini 3.8 Flash | Working app, code review, tests |
| Debug nondeterministic bug | GPT-6 Astra High | GPT-6.1 Sol Medium/High | DeepSeek V4 Pro (evaluate) | Claude Opus 5.5 | Minimal reproducer and regression test |
| Huge multi-file code/document understanding | Gemini 4 Argon | Gemini 3.8 Flash | Gemini 3.5 Flash-Lite for small extraction | GPT-6.1 Sol | Quotes/paths traceable, no omitted dependencies |
| Bulk extraction, tags, inventory classification | Quality-tested specialized extraction model | GPT-6 Luna / Claude Haiku 5.5 | Gemini 3.5 Flash-Lite | Gemini 3.8 Flash | Sample accuracy, recall, structured schema |
| Documents / PDF reasoning | GPT-6 Astra | GPT-6.1 Sol Medium | Gemini 3.8 Flash | Claude Sonnet 5.5 | Cite pages, distinguish extracted text from inference |
| Spreadsheet cleanup, SQL, business analysis | GPT-6.1 Sol Medium + executable calculations | Gemini 3.8 Flash + code | GPT-6 Luna for known templates | Claude Sonnet 5.5 | Recomputed totals, tested formulas/queries |
| Deep multi-source research | GPT-6 Astra + retrieval | GPT-6.1 Sol + sources | Gemini 3.8 Flash + retrieval | Claude Opus 5.5 | Current sources, evidence strength, uncertainty |
| Agentic tool-use and long task planning | Claude Opus 5.5 / GPT-6 Astra | GPT-6.1 Sol Medium | DeepSeek V4 Pro (pilot) | Gemini 4 Argon | Tool success, recoverable checkpoints |
| Image understanding / categorize photos | GPT-6 Astra for complex visual reasoning | Gemini 3.8 Flash | DeepSeek Flash (verify vision and accuracy) | GPT-6.1 Sol | Evaluated labels, ambiguity handled |
| **Create premium still images** | **GPT-Image-2.5 Sunburst** | GPT-Image-2.5 Flare | Nano Banana 2 Lite (compare cost/image) | Nano Banana Pro | Native generated image, prompt match, quality check |
| **Edit existing images** / consistency | GPT-Image-2.5 Sunburst | GPT-Image-2.5 Flare | Test lower-cost image endpoint | Nano Banana Pro | Preservation of requested unchanged elements |
| Image text/typography, graphic design | Evaluate Sunburst vs Imagen/Nano Banana Pro on examples | GPT-Image-2.5 Flare | Lower-cost image endpoint after samples | Ideogram family (verify current model) | Readable text, layout, no artifacts |
| Video *understanding* (clips) | Gemini 4 Argon | Gemini 3.8 Flash | Short clipped content + economical model | Specialist video-understanding endpoint | Timestamps, temporal consistency |
| Video *generation* / image-to-video / motion | Veo / Sora / Runway / Kling / Seedance (compare per shot) | Task-and-length-dependent creative endpoint | Lower-resolution/shorter clips if available | Another dedicated video engine | Playable clip, motion quality, cost per usable second |
| Transcription / subtitles | Specialized speech-to-text model | Gemini Transcribe / OpenAI transcription | Batch STT where cheaper | Voxtral transcription | Word/timestamp error rate, languages |
| Voice conversation | Realtime/live speech model | GPT-Realtime mini / Gemini Live | Lower-latency economy voice model | Another native speech agent | Turn-taking, language, interruption handling |
| TTS / expressive voice | Gemini 3.8 Flash TTS / native TTS service | Lower-cost TTS variant | Mini TTS | Voxtral TTS | Voice naturalness, clarity, cost/audio minute |
| Music generation | Dedicated music model (e.g. Lyria) | Compare music endpoints | Short/low-cost sample | Alternative music model | Rights, musical quality, duration |
| Embeddings / semantic retrieval | Retrieval-tuned embedding model | Economical embedding model | Smaller embedding model | Reranker + embeddings | Retrieval precision/recall, index cost |
| OCR / document layout extraction | Specialized OCR 4.1 / document AI | OCR + balanced model only for exceptions | Deterministic OCR if layout simple | Multimodal general model | Field-level accuracy, bounding boxes |
| Multilingual translation with domain terminology | High-fidelity multilingual model | GPT-6.1 Sol / Claude Sonnet 5.5 | Gemini 3.8 Flash | Specialist translation model | Terminology, meaning, no language drift |
| Security-sensitive architecture review | GPT-6 Astra + testing/human review | GPT-6.1 Sol High | None without adequate checks | Claude Opus 5.5 | Threat model, tests, human sign-off |

**Important:** The image/video/music entries are *model or service families* in several cases, not claims that a text model itself renders the media. Exact endpoints, constraints, licenses, and prices must be checked for a purchase. Claude's vision input is not proof of native image generation. “Motion” in an application may be an integrated workflow/tool rather than a Claude model capability.

## Matrix B — capability and confidence by model/family

| Provider / model | Role | Best-fit context | Relative efficiency | Evidence | Price reference |
|---|---|---|---|---|---|
| OpenAI GPT-6 Astra `gpt-6-astra` | Flagship reasoning | High-stakes planning, coding, research, tool work | High task quality; costly tokens | D/E | $10 input / $50 output per 1M text tokens, standard short-context API |
| OpenAI GPT-6.1 Sol `gpt-6.1-sol` | Balanced reasoning | Architecture, complex daily engineering, professional work | **Strong default** | D/E | $2 / $10 |
| OpenAI GPT-6 Luna `gpt-6-luna` | High-throughput | Routine scoped tasks, triage, extraction | Very cost efficient **if** quality floor met | D/E | $0.10 / $0.50 |
| Claude Fable 5.1 | Frontier specialized | Demanding long-horizon reasoning/agent work | Premium, use selectively | D/E | Check Anthropic pricing |
| Claude Opus 5.5 | Flagship agentic | Complicated codebase work and engineering | Quality-first, higher cost | D/E | Check Anthropic pricing |
| Claude Sonnet 5.5 | Balanced | Daily coding, code review, writing | Strong engineering value | D/E | Check Anthropic pricing |
| Claude Haiku 5.5 | High-throughput | Classification, extraction, routing | Economy candidate with QA | D/E | Check Anthropic pricing |
| Gemini 4 Argon `gemini-4-argon` | Frontier multimodal understanding | Complex coding, long-context, video understanding | Premium; excellent fit where multimodal input needed | D/E | Check Google pricing |
| Gemini 3.8 Flash `gemini-3.8-flash` | Balanced multimodal | Coding agents, huge documents, vision, routine research | Strong throughput/value candidate | D/E | Check Google pricing |
| Gemini 3.5 Flash-Lite | Economical | Simple classification/extraction | Budget candidate | D/E | Check Google pricing |
| DeepSeek V4 Pro `deepseek-v4-pro` | Reasoning / agents | Code and structured tasks | Low API sticker price; test stability | D/E | Peak $1.32 / $3.96 per 1M, cache-miss input / output; off-peak half |
| DeepSeek V4.1 Flash `deepseek-flash` | Throughput / vision | Scoped tasks and multimodal classification | Low API sticker price; pilot language reliability | D/E | Peak $0.30 / $1.20; off-peak half |
| Qwen current family | Open-weight / hosted alternatives | Coding, multilingual work, budget deployment | Hardware/API dependent | U/E | Verify specific model and endpoint |
| Kimi current family | Hosted alternatives | Agentic coding, long-context workflows | Subscription and API differ | D/E | Verify model and pricing |
| Grok current family | Hosted text + Imagine | Research and tool workflows; dedicated image/video | Endpoint-specific | D/E | Verify API price |
| Mistral Large 4 | Open-weight general multimodal | Private deployment, broad multimodal | Hosting dependent | D/E | Verify hosted/compute cost |
| Mistral Small 4 | Hybrid efficient | Budget reasoning and code | Deployment dependent | D/E | Verify pricing |
| Llama current open-weight family | Self-hosted | Privacy, custom tuning, offline processing | Depends on hardware, licenses, operations | U/E | GPU + operating costs |
| Z.ai GLM family | Open-weight and hosted | Coding/reasoning alternatives | Depends on tested model | U/E | Verify current provider listing |
| Image: GPT-Image-2.5 Sunburst / Flare | **Generation/editing** | Quality-first / value-first still images | Compare **cost per usable image**, not tokens alone | D/E | Verify size/quality pricing |
| Image: Nano Banana Pro / 2 / Lite | **Generation/editing** | Multimodal image workflows | Cost / quality setting dependent | D/E | Verify per-image API price |
| Video: Sora, Veo, Runway, Kling, Seedance | **Generation/editing** | Motion, cinematic clips, reference consistency | Compare per usable second and retry rate | U/E | Endpoint/length/resolution pricing varies |
| Audio: OpenAI Live/Realtime, Gemini Live/TTS/Transcribe, Voxtral | **Voice/audio** | Speech understanding, live voice, TTS | Compare per minute, latency, and error rate | D/E | Modality-specific prices |

**Verified Claude base API pricing on 2026-10-20** (USD per 1M input/output tokens; excludes caching and special tiers): Fable 5.1 **$10/$50**, Opus 5.5 **$4/$20**, Sonnet 5.5 **$2/$10**. See [Anthropic's pricing](https://platform.claude.com/docs/en/about-claude/pricing). Google Gemini 4 Argon standard pricing is **$2/$10 through November 30, 2026**, with an announced increase effective December 1, 2026; check [Google's current tier-specific price table](https://ai.google.dev/gemini-api/docs/pricing) before purchasing. No universal dollar-equivalent for subscription quotas is implied.

**Verified API pricing on 2026-10-20:** OpenAI GPT-6 standard short-context input/output (above); DeepSeek peak/off-peak rates (above). **Do not infer** that these prices equal subscription quotas. Google and Anthropic official price catalogs are linked below, but their exact per-model price rows are intentionally not asserted without auditing the corresponding tier and cache settings.

## Decision tree

```text
START
  |
  +-- Can a deterministic tool fully do the job? -- YES --> Use script / parser / hash / tests; AI only for judgment.
  |
  +-- Does the output need to BE an image, video, speech or music?
  |      +-- YES --> Native creative / speech model for THAT output (not a general chat model).
  |      +-- NO  --> Continue.
  |
  +-- Is input multimodal (images/video/audio/PDF)?
  |      +-- YES --> Require genuine input support; shortlist Gemini/GPT/Claude or specialized extractors.
  |
  +-- Is the work ambiguous, architectural, long-horizon, or risky?
  |      +-- YES --> Balanced model at Medium; flagship if proven need.
  |      +-- NO  --> Economical model IF quality threshold is met.
  |
  +-- Is the current model succeeding on the larger workflow?
  |      +-- YES --> STAY on it; save/compact context rather than hopping.
  |      +-- NO  --> Identify exact failure; escalate reasoning OR model, one variable at a time.
  |
  +-- Validate results; estimate end-to-end cost; record what worked.
```

## Reasoning effort — independent of model

| Effort | When | When not |
|---|---|---|
| None/Low | Brief chat, inventory summaries, extraction, simple changes | Unclear architecture or cross-module dependency work |
| **Medium** | **Default for substantive design, folder structure, code planning, refactoring** | Don't increase without a known problem |
| High | Difficult debugging, many tradeoffs, complex migrations or contradictions | Routine file moves and predictable transformations |
| Extra High / Max | Particularly difficult reasoning where a trial shows improved *validated* success | Do not use solely because a bigger number looks better |

Names and supported settings vary. On GPT-6.1 Sol the official API offers `low`, `medium`, `high`, `xhigh`, `max`; “Extreme” may be a product UI label rather than an API value. Higher effort may increase thinking tokens/latency; **cannot assume it improves correctness in all tasks**. Compare the same representative task and score output quality, retries, wall time, and usage.

## Switching models, sessions, and total cost

### Primary rule: one workflow, one lead model (unless evidence says otherwise)

Keep one lead model for **inventory -> understand contents -> classify relevance/shared use -> propose structure -> approve moves -> validate**. Use scripts for mechanical steps and a new specialist only when modality or capabilities demand it.

A switch is justified if: (1) current model lacks required modality/tools; (2) confirmed repeat failure in quality/instruction adherence; (3) distinct batch phase is large enough to amortize handoff; (4) context limit makes continuing impractical; (5) a task-specific benchmark shows superior total completion economics.

Avoid switching if: you are moving to the next microstep, the current model already has the relevant context, the cheaper model may ignore language/format, or the switch would require retelling a long project history.

### Effective cost of a completed task

```text
expected_total_cost =
  inference_input_cost + inference_output_cost + tool_and_media_fees
  + retry_cost + duplicated_context_or_handoff_cost
  + validation_cost + human_rework_cost

quality-adjusted efficiency = acceptable validated completions / expected_total_cost
```

The last two terms may be nonmonetary; track them in time if dollars are unavailable. Reasoning tokens, cache hit/miss, long-context premiums, tool calls and retries matter. A very cheap but drifting model is not efficient.

### Session / language integrity safeguards

- Preserve task objective, repository invariants, language preference, accepted folder design, files already processed, actions performed, and open exceptions in a **short checkpoint**.
- Freeze an approved plan before destructive operations. Prefer `git mv` where appropriate, `git status`, reference searches, tests, checksums, and backups for high-risk moves.
- Classify `KEEP`, `MOVE`, `SHARED`, `ARCHIVE`, `QUARANTINE`, `DELETE-CANDIDATE`; never auto-delete low-confidence candidates.
- Treat language drift, invented tool outputs, missed constraints, invalid edits, or repeated format failures as **hard quality failures**. Retry with a concise correction once; then change effort/model or break up the task.
- Use exact model IDs only after checking the model is offered by the current platform; hosted names, product labels, and API IDs differ.

### Example: file-structure overhaul

1. **Deterministic discovery:** tree, extension distribution, sizes, ownership, duplicate hashes, references, manifests. No LLM token spend for this.
2. **Single lead model:** GPT-6.1 Sol Medium (E) reviews representative content, dependency boundaries, relevance, shared agent resources, and creates a move manifest.
3. **Approval / safety boundary:** no deletion based on hallucinated relevance; archive uncertain assets.
4. **Deterministic execution:** scripts make changes using manifest; keep git history and move logs.
5. **Validation:** build/tests/typecheck/path resolution, hash checks, and review exceptional diffs using the **same model**.
6. **Escalate only** for genuinely difficult architecture or unexpected regressions; provide a short checkpoint to the next model.

## Scoring: quality gates first, then task-specific weights

### Hard gates

- Native ability to **produce the needed output**, not merely describe it
- Tool, platform and data residency/rights requirements
- Tested language/instruction consistency
- Minimum acceptable output quality and safe operation
- Availability within allowed spend or subscription quota

### Editable weights (heuristics, not provider benchmarks)

| Task type | Quality | Reliability | Cost | Speed | Context/workflow |
|---|---:|---:|---:|---:|---:|
| Engineering | 40% | 30% | 15% | 10% | 5% |
| Images | 55% | 20% | 15% | 5% | 5% |
| Everyday chat | 25% | 35% | 20% | 15% | 5% |
| Bulk inventory | 20% | 30% | 30% | 10% | 10% |

Do **not** assign 9.8/10 scores without controlled measurement. Mark confidence `D / E / T / U`. Test five to twenty representative cases before declaring a cross-provider champion, retaining task inputs, costs, retry counts, and validator outcomes.

### Recommendation format (repeat for any new task row)

```yaml
id: FS-STRUCTURE-01
context: "Repository reorganization and relevance/shared-resource assessment"
required_output: "Approved move manifest + validated working tree"
constraints: ["preserve behavior", "stay in user language", "no unapproved deletion"]
quality_floor: "Pass tests/build, no broken references, review uncertain files"
best_fit: "GPT-6 Astra Medium/High for exceptionally complex dependencies"
best_value: "GPT-6.1 Sol Medium"
budget: "Use scripts for inventory; economical model only for bounded tagging"
fallback: "Claude Sonnet 5.5"
keep_same_model_across_steps: true
switch_only_if: "tool/modality mismatch, validated failure, long distinct batch, or superior measured end-to-end efficiency"
evidence: "D capabilities + E selection; comparative T not established"
price_as_of: "2026-10-20"
```

## Source index / maintenance

*Read provider pages for current actual IDs, pricing tiers, input/output modalities, context windows, rate limits, model retirement and terms. Product subscription usage is **not** API token pricing.*

- OpenAI catalog: https://developers.openai.com/api/docs/models/all
- OpenAI selection / reasoning: https://developers.openai.com/api/docs/guides/model-selection
- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- Anthropic models: https://platform.claude.com/docs/en/models/overview
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Google Gemini model catalog: https://ai.google.dev/gemini-api/docs/models
- Google Gemini prices: https://ai.google.dev/gemini-api/docs/pricing
- DeepSeek model and price catalog: https://api-docs.deepseek.com/quick_start/pricing/
- Kimi API guide: https://www.kimi.ai/help/kimi-api/api-overview
- xAI Grok & Imagine catalog: https://docs.x.ai/developers/models
- Mistral models: https://docs.mistral.ai/models
- Alibaba Qwen (verify model + hosted offer): https://help.aliyun.com/zh/model-studio/
- Meta Llama: https://www.llama.com/
- Additional specialty video/image providers (Sora, Veo, Runway, Kling, Seedance, Ideogram, FLUX): verify model IDs, native editing support, pricing, license, video length and current availability before ranking them.

**Model and endpoint verification rule:** Names and feature descriptions may differ among API catalogs, app menus, integrations and third-party routing services. Never infer an API ID from a product display name. If a model lacks an official accessible price or current endpoint, mark `Unverified` and link the provider catalog. Non-native features (e.g. app motion tools or creative studios) must appear as tools/services rather than claiming the chat model alone generates media.

**Maintenance:** monthly review or after a major model release; record change date and proof; retire stale IDs; separate published data from practical preference; retest examples when pricing, interface, reasoning options or model versions change. The file is a snapshot, **not** a continuously updating model router.

---

**Design freeze:** V2.1 final, 2026-10-20 (architecture frozen, evidence and pricing maintainable). Agreed decisions: expanded providers; official documentation plus explicitly labeled editorial recommendations; task matrix **and** decision tree; whole-workflow/session efficiency; reliability floor; no automatic cheap-first policy; one lead model for tightly coupled multi-step work; exact reasoning escalation only when evidence warrants it; advisory/Grill Me/strict preference modes; explicit user overrides and no silent switching.