# Flectos System Architecture

This document describes the public, sanitized architecture of Flectos. It intentionally omits credentials, private infrastructure addresses, production workflow exports, proprietary prompts and user data.

## Architectural goal

Flectos is designed as a behavioral decision system rather than a generic chatbot. The architecture therefore separates transport, routing, domain flows, AI inference, persistence and operations.

```text
Channels
  ├── WhatsApp
  └── PWA
        ↓
Transport / Webhook Layer
        ↓
Conversation State Resolver
        ↓
Intent Routing
  ├── deterministic rules
  └── LLM-assisted classification for ambiguous inputs
        ↓
Domain Flow Engine
  ├── expense registration
  ├── income registration
  ├── purchase decision
  ├── decision follow-up
  └── behavioral insight generation
        ↓
AI Services
  ├── text interpretation
  ├── speech transcription
  └── image understanding
        ↓
PostgreSQL / Supabase
        ↓
Operational Layer
  ├── incident logs
  ├── audits
  ├── recovery tools
  └── internal Ops UI
```

## Architectural boundaries

### Transport

The product should not depend on a single messaging channel. WhatsApp and the PWA are transports, not the location of product intelligence.

### Routing

Canonical intents are resolved deterministically whenever possible. Ambiguous language can be escalated to an LLM-assisted classifier.

### Domain flows

Important user journeys are represented as explicit stateful flows. This keeps product behavior predictable and testable.

### AI services

Model calls are treated as capabilities with latency, cost, availability and failure modes. They are not the controller of the entire application.

### Persistence

Conversation state, financial events, decision outcomes and behavioral signals are stored explicitly so a user interaction does not depend on model memory.

### Operations

AI systems still require conventional production engineering. Incident logging, severity, retries, auditability and recovery are part of the product architecture.
