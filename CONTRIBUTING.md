# Contributing

Aétios Muse Systemic Matrix (AMSM)  
Silence-First Framework (SSF)

Status: Public reference repository  
Last update: 2026

---

## 1. Scope

This repository is the canonical SSF reference.

Contributions are welcome, but SSF must remain:

- minimal,
- causal (pre-inference),
- auditable,
- reproducible,
- content-agnostic.

---

## 2. Before Opening a PR

Please ensure:

- the change is small and justified,
- the intent is clearly described,
- no new dependencies are introduced without necessity,
- no telemetry, tracking, or fingerprinting is added,
- no content-based filtering logic is introduced.

SSF is a gate, not a judge.

---

## 3. PR Requirements

A PR must include:

- a short description of the problem,
- what changed,
- why it is safe,
- how to reproduce.

If behavior changes, include a test or a minimal benchmark.

---

## 4. Commit Style

No strict format is required.

However, prefer:

- short commits,
- explicit messages,
- one change per commit.

---

## 5. Review Process

- PRs may be accepted, modified, or rejected.
- Silence is a valid outcome.
- No timeline is guaranteed.

---

## 6. Canonical Integrity

Forks are welcome.

But PRs that alter SSF semantics without strong justification will be rejected.

Core invariants must remain stable:

- Φ, Φ_c, Ω
- L = (Φ_c · π) / Ω
- SSF gate: divergence threshold ε

---

## 7. Security Issues

Do not open public issues for vulnerabilities.

Use GitHub Security Advisories (preferred).
See `SECURITY.md`.

---

© Aétios Muse Systemic Matrix — Open Research Initiative


