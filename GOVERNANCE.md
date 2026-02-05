# Governance

Aétios Muse Systemic Matrix (AMSM)  
Silence-First Framework (SSF)

Status: Public reference repository  
Last update: 2026

---

## 1. Purpose

This repository provides the **canonical reference implementation**
of the Silence-First Framework (SSF).

SSF is a pre-inference causal regulator:
it decides **when** a system is allowed to compute,
not **what** it should output.

---

## 2. Canonical Definition

In this repository, SSF is defined by:

- the invariant:
  L = (Φ_c · π) / Ω
- the causal phase variable Φ and its filtered form Φ_c
- the Silence-First gate logic
- the preprint in `paper/` (formal baseline)

This repository is the canonical reference.

Forks are expected.
Alternative implementations are welcome.
However, they must not be presented as the SSF reference kernel
if they diverge in behavior.

---

## 3. Contribution Principles

Contributions are welcome if they preserve:

- conceptual minimalism,
- deterministic behavior (when possible),
- auditability,
- reproducibility,
- absence of content-based rules.

SSF is not an alignment layer.
SSF is not a classifier.
SSF is not a policy engine.

---

## 4. What Will Be Accepted

Typical accepted contributions:

- bug fixes,
- performance improvements (without changing semantics),
- documentation improvements,
- reproducible benchmarks and stress-tests,
- reference integrations (LLM, tool-use, pipelines),
- test harnesses and CI improvements.

---

## 5. What Will Not Be Accepted

Typical rejected contributions:

- content moderation rules,
- model-specific alignment policies,
- hidden heuristics that inspect meaning or intent,
- telemetry / tracking,
- user fingerprinting mechanisms,
- "always-on" inference behavior.

SSF must remain a causal gate.
Not a behavioral judge.

---

## 6. Review Standard

All changes must satisfy:

- clear rationale,
- minimal surface area,
- reproducible behavior,
- readable code,
- explicit tests when behavior changes.

---

## 7. Versioning

SSF follows semantic versioning:

- MAJOR: conceptual or API changes,
- MINOR: new features that preserve core semantics,
- PATCH: bug fixes and documentation.

---

## 8. Academic Reference

Citations should refer to:

- this repository (canonical),
- the preprint in `paper/`,
- the `CITATION.cff` file.

If you publish a derivative SSF implementation,
use a distinct name to avoid confusion with the reference kernel.

---

## 9. Decision Authority

This repository is currently maintained by the original author
under an open research initiative.

There is no formal foundation or legal entity at this time.

---

## 10. Summary

- This repo is the canonical SSF reference.
- Forks are welcome.
- Contributions are welcome if SSF remains minimal, causal, and auditable.
- SSF is a gate, not a judge.

---

© Aétios Muse Systemic Matrix — Open Research Initiative
