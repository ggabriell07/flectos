# Observability

Flectos treats AI behavior as production behavior that must be observable.

## Operational signals

Representative signals include:

- workflow success and failure rate
- deterministic routing rate
- LLM escalation rate
- restricted fallback rate
- external API latency
- model latency
- incident severity
- recurring error fingerprints
- notification delivery state
- flow completion rate
- recovery actions

## Incident model

Operational incidents use a severity model:

```text
low
medium
high
urgent
```

A recurring failure should preserve a stable fingerprint so repeated errors can be grouped rather than treated as unrelated events.

## Why this matters

Without operational telemetry, an AI product can appear healthy while silently producing higher fallback rates, slower responses, malformed structured outputs or incomplete user flows.

The objective is to make both infrastructure failures and AI-behavior regressions measurable.
