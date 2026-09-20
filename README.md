# Flectos

**Behavioral Decision Intelligence for everyday purchase decisions**

Flectos is an applied AI product designed to help users interrupt impulsive purchases, reflect on context and make more deliberate financial decisions.

The platform combines **conversational AI, multimodal processing, deterministic routing, persistent state, behavioral signals and operational guardrails**.

Current status: **closed beta · v15**

---

## Why this project exists

Most financial tools analyze what happened after the money was spent.

Flectos is designed to intervene **before the purchase**.

A typical interaction evaluates signals such as:

- whether the purchase was planned
- emotional context
- urgency
- promotion pressure
- financial exposure
- behavioral history
- whether the user still wants the item after a short pause

The product then guides the user toward a deliberate next action such as waiting, finding an alternative, saving the decision or proceeding consciously.

---

## System architecture

```text
User
  ↓
WhatsApp / PWA
  ↓
API & Workflow Layer
  ↓
Intent Router
  ├── Deterministic rules for critical intents
  └── LLM-assisted classification for ambiguous cases
  ↓
Structured flow engine
  ├── Expense registration
  ├── Income registration
  ├── Purchase decision
  ├── Decision follow-up
  ├── Behavioral insights
  └── Reports / summaries
  ↓
AI services
  ├── Claude
  ├── Claude Vision
  └── OpenAI Whisper
  ↓
PostgreSQL / Supabase
  ├── user state
  ├── financial events
  ├── conversation context
  ├── decision history
  └── behavioral signals
  ↓
Operational layer
  ├── incident logging
  ├── severity classification
  ├── workflow monitoring
  └── internal Ops dashboard
```

---

## AI engineering approach

### Hybrid routing instead of LLM-only routing

Critical intents are not delegated entirely to a language model.

The system first applies deterministic rules for canonical cases such as:

```text
"I spent R$45 on lunch"
"I received R$4,500 salary"
"Can I buy a R$300 jacket?"
"Open my dashboard"
```

Only ambiguous messages are escalated to an LLM-assisted path.

This architecture reduces:

- unnecessary model calls
- latency
- cost
- routing variability
- accidental flow changes

and improves predictability for critical product actions.

---

## Multimodal pipeline

### Text

Natural language is converted into structured financial and behavioral fields.

Examples:

```text
amount
category
description
purchase date
payment method
installments
planned/unplanned
emotional context
```

### Audio

```text
WhatsApp audio
      ↓
media download / decryption
      ↓
OpenAI Whisper
      ↓
normalized text
      ↓
structured extraction
      ↓
workflow
```

### Image

```text
receipt / purchase image
      ↓
media processing
      ↓
Claude Vision
      ↓
structured financial data
      ↓
validation
      ↓
persistence
```

---

## Conversational state

The system maintains context across multi-step interactions.

State is persisted instead of relying exclusively on the current user message.

Examples of state include:

- active flow
- current decision step
- last message variation
- pending purchase decision
- recent conversational context
- previous user actions

This avoids treating each message as an isolated prompt.

---

## Behavioral decision flow

One of the core flows is **"Can I buy this?"**.

A simplified version:

```text
Purchase intent
      ↓
Origin of desire
      ↓
10-second pause
      ↓
Re-evaluate desire
      ↓
Risk/context analysis
      ↓
Behavioral mirror
      ↓
Final decision
      ├── wait 24h
      ├── find alternative
      ├── buy consciously
      ├── save decision
      └── give up purchase
      ↓
Outcome persistence
```

The product is intentionally not designed as a generic chatbot.

The LLM supports structured decision flows rather than replacing them.

---

## Data layer

Main storage technologies:

```text
PostgreSQL
Supabase
JSONB
RLS
PL/pgSQL
```

Representative entities include:

```text
users
expenses
income
installments
decision_events
recent_messages
behavioral_signals
bot_error_logs
message_variations
```

The data model supports both financial history and behavioral context.

---

## Operational reliability

The platform includes an internal operational layer for production support.

Examples:

- incident logging
- severity levels
- recurrent-error fingerprints
- queued/sent notification state
- workflow audits
- user-flow reset tools
- phone normalization checks
- duplicate-user investigation
- service health investigation

This operational layer exists because AI applications still need conventional production engineering.

---

## Cost strategy

The architecture intentionally avoids using an LLM where deterministic logic is sufficient.

Examples:

```text
canonical command → deterministic
structured known flow → deterministic
ambiguous language → LLM
vision task → vision model
audio transcription → speech model
behavioral interpretation → LLM when useful
```

The objective is to maximize product value while keeping inference cost and latency controlled.

---

## Stack

**AI**

`Claude` · `Claude Vision` · `OpenAI Whisper` · `LLM Orchestration` · `Structured Extraction`

**Backend / Data**

`PostgreSQL` · `Supabase` · `PL/pgSQL` · `JSONB`

**Workflow / Integration**

`n8n` · `Evolution API` · `REST APIs` · `Webhooks`

**Frontend**

`Next.js` · `React` · `PWA`

**Operations**

`Linux` · `Docker` · `VPS` · `GitHub` · `Operational Monitoring`

---

## Repository scope

The complete production implementation is intentionally private.

This public repository documents:

- system architecture
- AI engineering decisions
- product flows
- data modeling concepts
- operational patterns
- selected implementation patterns that can be shared safely

It does **not** expose:

- user data
- API credentials
- private infrastructure addresses
- full production workflows
- proprietary prompts
- internal operational data

---

## Engineering principles

1. Use deterministic logic for deterministic problems.
2. Use LLMs where interpretation creates real value.
3. Persist conversational state explicitly.
4. Validate external API payloads before execution.
5. Design fallbacks that are safe and observable.
6. Treat cost and latency as architecture concerns.
7. Keep business-critical workflows testable.
8. Separate product intelligence from transport channels.
9. Make AI behavior observable in production.
10. Build the product so it can evolve without exposing user data or internal infrastructure.

---

## Current evolution

The next public engineering work around Flectos will focus on making more of the architecture reproducible without exposing the private product implementation.

Planned public additions include:

- architecture diagrams
- selected Python service examples
- evaluation datasets
- regression tests
- structured extraction benchmarks
- operational design notes
- AI system decision records

---

**Flectos v15 · closed beta**
