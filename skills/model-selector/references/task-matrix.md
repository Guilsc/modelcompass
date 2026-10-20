# Task-to-model selection matrix

This matrix deliberately names **candidate families**, not scientifically ranked winners. Check deployed variants, model IDs, capabilities and freshness in provider catalogs before recommending a specific release. Mark assessments E unless independently tested.

| Context | Best-fit candidate | Efficient candidate | Budget direction | Important gate |
|---|---|---|---|---|
| Casual multilingual chat | Strong general conversational model | Mid-tier fast general LLM | Small fast LLM | Language fidelity over marginal savings |
| Repository structure and architecture | Strong reasoning/coding model | Mid-tier coding model, moderate effort | Small coding model for bounded subtask | Dependency fidelity and session continuity |
| Code generation and debugging | Coding-capable reasoning model | Mid-tier coding model | Small coding model with tests | Execution and tests |
| File inventory | Deterministic filesystem tools | Small model interprets metadata | Script only | Do not waste model tokens enumerating files |
| File relevance / classification | Reasoning model for ambiguous judgments | Fast vision/text model where appropriate | Small classifier with escalation | False positives and data privacy |
| Document extraction | Document-capable multimodal model | Efficient OCR/document pipeline | Deterministic extractor + smaller model | Scan quality, source fidelity |
| Large-context research | Grounded long-context research model | Mid-tier long-context model | Retrieval + smaller summarizer | Citation coverage and hallucination |
| Image understanding | Vision-capable model | Efficient multimodal model | Smaller vision model | Vision input capability |
| Image generation/edit | Dedicated image generation/editing model | Fast specialized image model | Lower generation quality setting | Native generation, price per output |
| Video understanding | Native video or frame+audio model | Frame sampling plus audio extraction | Targeted extraction | Temporal understanding |
| Video generation/motion | Dedicated video generation system | Faster/lower-resolution video system | Shorter clips | Native video output and per-second pricing |
| Audio transcription | Speech-to-text model | Fast transcription model | Local ASR if appropriate | Language and diarization |
| Voice or music synthesis | Native generative audio model | Fast voice model | Lower-cost voice settings | Consent, output fidelity |
| Spreadsheet and analytics | Coding/data reasoning model + tools | Mid-tier model with Python/SQL | Script and small model summaries | Formula correctness and repeatability |
| Tool orchestration | Reliable tool-use model | Mid-tier agent-capable model | Small model for bounded calls | Tool schema compliance and recovery |

For explicit release-level recommendations, require dated provider or evaluated evidence. See `model-catalog.md`, `sources.md` and `cost-efficiency.md`.
