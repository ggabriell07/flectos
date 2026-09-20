# Cost Strategy

Flectos uses a simple architecture principle:

> Use model inference only when interpretation creates enough value to justify its latency and cost.

## Decision examples

```text
exact command            → deterministic
known state transition   → deterministic
canonical intent         → deterministic
ambiguous language       → LLM-assisted
audio transcription      → speech model
image understanding      → vision model
behavioral interpretation→ LLM when useful
```

## Cost controls

The public design considers:

- deterministic routing before model escalation
- model selection by task complexity
- structured outputs to reduce retries
- explicit fallback behavior
- bounded conversation context
- instrumentation for token usage and latency

The goal is not to minimize AI usage at any cost. The goal is to spend inference budget where it improves the product.
