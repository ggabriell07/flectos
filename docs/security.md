# Security Boundaries

This public repository is intentionally separated from production secrets and user data.

## Never published

- API keys and access tokens
- database credentials
- private hostnames or internal network addresses
- real user phone numbers
- production payloads containing personal data
- proprietary production prompts
- production workflow exports containing credentials
- operational logs with user-identifying information

## Engineering principles

- secrets belong in secret stores or protected environment configuration
- external payloads must be validated before downstream actions
- sensitive tokens should not be persisted in plaintext
- public examples should use synthetic data
- debugging information must not leak user data
- operational tooling should be auditable

The files under `examples/` are sanitized reference implementations. They demonstrate engineering patterns and are not direct exports of the production system.
