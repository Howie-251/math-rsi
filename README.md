# MathRSI

[中文说明](README.zh-CN.md) · [Quick start](docs/QUICKSTART.md) · [Try a proof repair](examples/proof-repair/README.md) · [Property B case study](case-studies/property-b/README.md)

Fixed versions: **[v1](https://github.com/lisresearchgroup/math-rsi/tree/v1)** ([ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v1.zip)) · **[v2](https://github.com/lisresearchgroup/math-rsi/tree/v2)** ([ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v2.zip)). Each tag preserves a complete repository snapshot and stays fixed; `main` follows the current recommended version. v2 adds meta-evolve, the degree–diameter plugin, and workflow improvements to v1.

**An agent-executable, self-evolving workflow and domain knowledge harness for rigorous mathematical research.**

MathRSI organizes mathematical research from problem formulation and literature verification to route exploration, proof construction, independent auditing, optional Lean formalization, and reproducible handoff. MathRSI provides structured Markdown skills, domain plugins, cross-model review bridges, and verification contracts that coding agents (Claude Code and Codex) execute step by step while preserving exact quantifiers and original problem obligations.

![v0 basic research tools inform MathRSI v1; independent DD history informs current v2, followed by future v3 and later evolution](figures/mathrsi/01-evolution.png)

The v0 stage represents basic research tools, including the standalone ARIS skills used in Property B and ECC research. Those experiences informed the unified v1 workflow. Independent DD research evidence then informed the current incremental v2: outer maintenance, workflow improvements, and a DD plugin. The v3 → … continuation indicates future evolution. ECC remains a draft. [Figure sources and review](figures/mathrsi/README.md).

---

## Why MathRSI

- **Enter at the current evidence stage**: Start from a raw problem statement, resume an in-progress proof workspace, or jump directly to auditing and repairing a complete candidate proof.
- **Keep lemmas bound to the original problem**: Intermediate reductions, conditional lemmas, and computational certificates are tracked against their actual callers so the agent can check whether a local result actually closes the main theorem.
- **Self-contained dual-host ARIS bundle**: Ships with **10 MathRSI skills** (9 solving skills plus the outer maintenance skill), **32 bundled ARIS skills** in both Claude Code (`base/skills/`) and Codex (`base/skills/skills-codex/`) layouts, **53 helper scripts** (`base/tools/`), **4 MCP reviewer bridge servers** (`mcp-servers/`), and **Property B** (`plugins/propertyb/`) and **degree–diameter** (`plugins/degree-diameter/`) domain plugins. No external ARIS checkout or global installer is required.
- **Clean separation of core, domain, and workspace**: Running a task or domain plugin updates only the problem's task workspace. Reusable domain tools are curated into plugins, and general workflow lessons are distilled into the next base iteration through the separate [`mathrsi-meta-evolve` skill](base/skills/mathrsi-meta-evolve/SKILL.md), within the maintenance scope already authorized by the user.

---

## Quick Start

See **[docs/QUICKSTART.md](docs/QUICKSTART.md)** for step-by-step setup and **[examples/proof-repair/README.md](examples/proof-repair/README.md)** for a self-contained walkthrough that audits, repairs, and hands off a flawed candidate proof.

### 1. Clone and verify the local bundle

Clone with an account that has access to the group repository. The local checks below use Python 3.9+ and its standard library:

```bash
git clone https://github.com/lisresearchgroup/math-rsi.git
cd math-rsi

python3 tools/check_links.py
python3 examples/proof-repair/replay.py
```

### 2. Run a mathematical task in your agent

Start Codex or Claude Code in the clone, with access to your task directory. The agent executes the Markdown workflows; Python provides helpers and reviewer bridges. Configure the reviewer CLIs and MCP services you plan to use through the [reviewer setup guide](docs/REVIEWER_MCP.md).

- **Direct path (works immediately in any supported agent session)**:
  ```text
  Read /absolute/path/to/math-rsi/base/skills/mathrsi-research/SKILL.md
  (and /absolute/path/to/math-rsi/plugins/propertyb/skills/mathrsi-propertyb/SKILL.md if working on Property B).
  In workspace /absolute/path/to/my-task, study <problem statement or candidate proof>.
  Restore any existing spec, wiki, and state; select the appropriate subworkflow
  (prepare, route-loop, prove, verify, or handoff), execute it, read the resulting
  artifacts, and continue the next authorized step.
  Use helpers from /absolute/path/to/math-rsi/base/tools (ARIS_REPO=/absolute/path/to/math-rsi/base).
  ```
- **Repo-relative skill aliases** (when your agent session is rooted in this clone):
  - **Claude Code** (`.claude/skills/`): `/mathrsi-research`, `/mathrsi-prepare`, `/mathrsi-route-loop`, `/mathrsi-prove`, `/mathrsi-verify`, `/mathrsi-handoff`
  - **Codex** (`.agents/skills/`): `$mathrsi-research`, `$mathrsi-prepare`, `$mathrsi-route-loop`, `$mathrsi-prove`, `$mathrsi-verify`, `$mathrsi-handoff`

---

## Maintain the existing MathRSI version

Read [`base/skills/mathrsi-meta-evolve/SKILL.md`](base/skills/mathrsi-meta-evolve/SKILL.md) with the research source, current maintenance record, and allowed change scope. It classifies evidence into base behavior, domain knowledge, task state, or deferred proposals, implements supported changes, and uses the affected behavior. Invoke `/mathrsi-meta-evolve` in Claude Code or `$mathrsi-meta-evolve` in Codex; both aliases share the same body. See the [evolution guide](docs/EVOLUTION_WORKFLOW.md) for a copyable request.

The bundled ARIS `meta-optimize` and `meta-apply` have separate host-specific aliases and retain their original contracts; they are not alternate names for this mathematical adaptation. The [v2 changes](docs/V2_CHANGES.md) use DD research evidence to incrementally revise the existing v1 workflows and add the DD plugin. The [maintenance record](development/evolution/dd-v2-20261102/EVOLUTION.md) tracks actual use, review, and adoption; archived DD results are historical sources, not outcomes produced by MathRSI v1 or v2.

---

## Three-Layer Architecture

| Layer | Location | Role |
| :--- | :--- | :--- |
| **Base Core** | `base/` | 9 MathRSI solving skills plus `mathrsi-meta-evolve`, 32 dual-host ARIS skills, shared verification contracts, and `base/tools/` helpers (`ARIS_REPO=<clone>/base`). |
| **Domain Plugins** | `plugins/` | Domain reductions, proved lemmas, counterexample maps, and domain checkers. Includes the complete **Property B** plugin (`plugins/propertyb/`, 4 skills + archive), the **degree–diameter** plugin (`plugins/degree-diameter/`, 4 skills + source wiki and supporting archive), and a draft **ECC** plugin (`plugins/ecc/`). |
| **Task Workspace** | User task dir | Problem-specific `FORMAL_SPEC.md`, `research-wiki/`, proof drafts, computational logs, `VERIFICATION.md`, and `NEXT_SESSION.md`. |

As defined in the [Plugin Contract](docs/PLUGIN_CONTRACT.md), plugins receive the active mathematical obligation and return scoped evidence to the calling stage. Plugins never mutate `base/` or weaken the original acceptance criteria during a problem-solving run.

---

## Five Executable Subworkflows

The top-level orchestrator ([`mathrsi-research`](base/skills/mathrsi-research/SKILL.md)) owns stage transitions. It inspects existing workspace evidence, delegates one subworkflow scope at a time, reads the returned artifacts and remaining obligations, and dispatches the next step.

![Five solving subworkflows with embedded ARIS, continuous research wiki, optional Lean, and separate mathrsi-meta-evolve maintenance](figures/mathrsi/02-workflows.png)

Research memory spans all five stages, with targeted returns for literature, route revision, and proof repair. The separate outer `mathrsi-meta-evolve` classifies evidence: Base and Plugin changes proceed through implementation, review, use, and adoption; Task and Defer remain in the wiki or backlog.

| Subworkflow | What It Does | Embedded ARIS Skills Used | Primary Outputs |
| :--- | :--- | :--- | :--- |
| **1. [`mathrsi-prepare`](base/skills/mathrsi-prepare/SKILL.md)** | Chains [`mathrsi-specify`](base/skills/mathrsi-specify/SKILL.md) (preliminary) $\rightarrow$ [`mathrsi-survey`](base/skills/mathrsi-survey/SKILL.md) (broad alias/citation/errata search & primary-source verification) $\rightarrow$ `mathrsi-specify` (final). | `research-lit`, `research-wiki`, `wiki-enrich` | `FORMAL_SPEC.md`, `LITERATURE.md`, updated wiki entities |
| **2. [`mathrsi-route-loop`](base/skills/mathrsi-route-loop/SKILL.md)** | Mathematical adaptation of ARIS `auto-review-loop`: proposes a proof route, runs adversarial review, executes informative math/compute probes, revises the route, and rechecks with persistent reviewer memory. | `auto-review-loop` *(math adaptation)*, `research-review` *(composed)* | `ROUTE_REPORT.md` with first concrete proof obligations & reviewer traces |
| **3. [`mathrsi-prove`](base/skills/mathrsi-prove/SKILL.md)** | Stabilizes objects and derivations, drafts lemmas, runs domain computations or parallel workers with exclusive write scopes, and binds results back to the original problem caller. | `formula-derivation`, `proof-writer`, `proof-orchestrator` *(optional)* | `PROOF_DRAFT.md`, computational certificates, or exact blocking gaps |
| **4. [`mathrsi-verify`](base/skills/mathrsi-verify/SKILL.md)** | For a natural-language proof, assembles scattered pieces and performs the applicable checks and `proof-checker` repair loop. A formal-only goal goes directly to `lean-formalize`, checking the actual export, definitions, build, and axioms without requiring TeX first. | `proof-writer` *(via assemble)*, `proof-checker`, `lean-formalize` *(optional)* | `PROOF.md` / `PROOF.tex`, `VERIFICATION.md`, `PROOF_AUDIT.md` |
| **5. [`mathrsi-handoff`](base/skills/mathrsi-handoff/SKILL.md)** | Packages the readable proof, standalone reproduction inputs/commands, citation checks, optional HTML/PDF views, updated wiki state, and resumption notes. | `render-html`, `citation-audit` / `paper-compile` *(when requested)* | `HANDOFF.md`, `NEXT_SESSION.md`, reproducible bundle |

### Targeted Return Paths, Wiki Memory, and Adversarial Review

- **Persistent Research Wiki**: `research-wiki` and `wiki-enrich` run across all stages to accumulate verified imports, proved conditional lemmas, and failed routes. Agents read full entity pages—not just auto-generated `query_pack.md` summaries—when resuming or checking conditions.
- **Targeted Literature Lookup (`route-loop` / `prove` $\rightarrow$ `survey`)**: When a new import question or suspected counterexample arises mid-proof, the caller invokes `mathrsi-survey` for an incremental source check and returns directly to the active obligation without resetting `FORMAL_SPEC.md`.
- **Local Verification Return (`prove` $\leftrightarrow$ `verify`)**: High-risk sub-lemmas or domain certificates can be verified early; a local pass returns to the parent `prove` caller to complete downstream steps rather than triggering full-problem `handoff`.
- **Repair vs. Route Rethink**: Proof gaps, index errors, or checker fixes return from `verify` to `prove`. If the route fails or repeated work stops producing useful information, the orchestrator returns from `prove` to `route-loop` to reconsider the method.
- **Cross-Model Review & Optional Lean**: `mathrsi-route-loop` and `mathrsi-verify` use bundled MCP bridges (`mcp-servers/` for Grok, Antigravity/Gemini, Codex, and Claude-review; see [docs/REVIEWER_MCP.md](docs/REVIEWER_MCP.md)). Model agreement never substitutes for a mathematical proof. `lean-formalize` is invoked on demand when formal verification is requested or high-leverage for a specific obligation.

---

## Domain Plugins

### Property B (`plugins/propertyb/`) — Accepted v1 Plugin

Provides a self-contained knowledge base (`plugins/propertyb/knowledge/`) and four specialized skills for uniform hypergraph 2-coloring lower bounds $m(k)$:

| Skill | Stage Integration & Responsibility |
| :--- | :--- |
| **[`mathrsi-propertyb`](plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)** | Domain entrypoint: maps hypergraph coloring problems to reduction, trace, repair, or asymptotic routes. |
| **[`propertyb-literature`](plugins/propertyb/skills/propertyb-literature/SKILL.md)** | Integrates with `prepare/survey` for hypergraph coloring aliases, citation chains, historical errata, and Radhakrishnan–Srinivasan baselines. |
| **[`propertyb-bound-lab`](plugins/propertyb/skills/propertyb-bound-lab/SKILL.md)** | Integrates with `route-loop` (failure diagnosis & probes) and `prove` (lock selection, actual traces, common bad pairs, signed repair gates, general-$k$ bounds). |
| **[`propertyb-certificate`](plugins/propertyb/skills/propertyb-certificate/SKILL.md)** | Integrates with `verify` for domain coverage checks, exact rational arithmetic replay, and binding local certificates to the global coloring statement. |

### Degree–Diameter (`plugins/degree-diameter/`) — v2 Addition

The [domain entry](plugins/degree-diameter/skills/mathrsi-degree-diameter/SKILL.md) connects to the existing five workflows. [`dd-construction`](plugins/degree-diameter/skills/dd-construction/SKILL.md) develops current-graph coverage, frozen-source clones, and algebraic routes; [`dd-obstruction-certificate`](plugins/degree-diameter/skills/dd-obstruction-certificate/SKILL.md) binds scoped exclusions, exact certificates, and Lean exports to the actual graph; [`dd-transfer-diagnosis`](plugins/degree-diameter/skills/dd-transfer-diagnosis/SKILL.md) rechecks inherited evidence when the source, rule, field, or public baseline changes. Each returns to its calling stage.

The [plugin guide](plugins/degree-diameter/README.md) includes the source research wiki, proofs, programs, failures, reviews, and formalization archive. New tasks write their own workspace wiki. Historical validity, comparison dates, and verification scopes stay separate; copying an archive neither resumes its Goal nor reruns its proofs.

### Error-Correcting Codes (`plugins/ecc/`) — Draft

Retains an initial draft ([`mathrsi-ecc`](plugins/ecc/skills/mathrsi-ecc/SKILL.md)) and read-only historical handoff snapshots ([`development/context/ecc-source/`](development/context/ecc-source/README.md)) that informed MathRSI's workflow transitions. It is not yet accepted to the Property B standard and is excluded from default skill discovery.

---

## Research Case: Property B

**Individual lower bounds for k = 5–12 and a uniform theorem for every k ≥ 12.** The general theorem and the earlier five-uniform bounds 33 and 34 have end-to-end Lean proofs; the individual bounds have their own paper and computational verification scopes, detailed in the [case study](case-studies/property-b/README.md).

[![Property B lower-bound improvements](case-studies/property-b/assets/delta.png)](case-studies/property-b/README.md)

These studies were carried out with **ARIS**, then distilled into MathRSI's workflows and Property B plugin. The case includes full offline proof readers, formal source, direct evidence links, and the lessons that shaped the harness. New tasks can evaluate the selected MathRSI revision itself.

**[Read the case](case-studies/property-b/README.md)** · [Full proof HTML](case-studies/property-b/readers/PROPERTY_B_GENERAL_BOUND.html) · [Lean reader](case-studies/property-b/readers/PROPERTY_B_GENERAL_LEAN.html). Clone or download the repository and open `case-studies/property-b/index.html` to read the HTML locally.

---

## Documentation Index

*(Note: Detailed reference guides under `docs/` and `base/skills/` are currently written in Chinese.)*

- **[Quick Start Guide](docs/QUICKSTART.md)** — Cloning, environment setup, and running your first task.
- **[Proof Repair Example](examples/proof-repair/README.md)** — Walkthrough of an end-to-end verification, counterexample check, union-bound repair, and handoff on a flawed candidate proof.
- **[Workflow & Orchestration Guide](docs/WORKFLOWS.md)** — Detailed stage inputs, ARIS skill handoffs, return paths, and copyable task prompts.
- **[ARIS Reuse Reference](docs/ARIS_REUSE.md)** — Dual-host layout (`base/skills/` vs. `base/skills/skills-codex/`), helper bindings, and external runtime dependencies.
- **[Reviewer MCP Setup](docs/REVIEWER_MCP.md)** — Registering and invoking the bundled `grok-exec`, `antigravity-exec`, `codex-exec`, and `claude-review` MCP servers.
- **[Plugin Contract](docs/PLUGIN_CONTRACT.md)** — How domain plugins interface with the five subworkflows without mutating the base core.
- **[Workspace Conventions](docs/WORKSPACE.md)** — Artifact layout, `research-wiki` usage, and session recovery via `NEXT_SESSION.md`.
- **[v2 Changes](docs/V2_CHANGES.md)** — Concrete changes to v1, DD stage integration, and evidence boundaries.
- **[Evolution Guide](docs/EVOLUTION_WORKFLOW.md)** — Human entry to [`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md), which maintains the executable process for improving the existing base and plugins from research evidence.
- **[Architecture Figures](figures/mathrsi/README.md)** — High-resolution diagrams, generation prompts, and visual alignment review records.

---

## Validation & Current Version Scope

The v1 implementation has been exercised through isolated bundle tests, targeted workflow trials, and real domain-checker replays. [Validation records](development/VALIDATION.md) retain the commands, review responses, and precise scope.

| Evidence | What it establishes |
| --- | --- |
| Relocated ARIS bundle checks | Original resource completeness, wiki operations, reviewer configuration parsing, and both HTML templates work from the bundled copy. |
| 61 offline MCP tests | Protocol behavior of the four bundled bridges. Live bundled Gemini continuation also succeeded; the latest bundled Grok first call timed out on the test host. |
| [Proof-repair trial](development/figure-workflow-check-20261101/REPORT.md) | A fresh agent found false independence of overlapping-edge events, repaired the proof using a union bound, preserved the theorem, and completed fresh source reviews and handoff. Review was same-family/provisional. PDF compilation remains pending because the test machine lacked TeX. |
| Property B replays and local workflow trial | Selected exact certificate checks run from the bundled resources; early local verification returns to its original proof obligation. See the records for each parameter's coverage. |

ECC remains a draft plugin. The v2 implementation keeps the v1 workflow and adds the DD plugin, direct formal-target verification, and more explicit consumption of changed baselines, changed objects, and shared coverage. [v2 changes](docs/V2_CHANGES.md) distinguish implemented behavior from the current adoption and review record. A complete new long research task and systematic efficiency or recursive self-improvement benchmarks remain to be evaluated.

Model CLIs and accounts, search access, and optional TeX/Lean environments are supplied by the user. The repository includes the workflow and bridge source, not these services or toolchains. Use the task's pinned Lean dependencies when formalizing an existing project.

---

## Provenance & License

MathRSI's workflow and bundled ARIS skill adaptations build on **[ARIS (Auto-claude-code-research-in-sleep)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** (snapshot commit `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`, Copyright (c) 2026 wanshuiyin) and research artifacts from the Property B, ECC, and degree–diameter projects. See **[docs/PROVENANCE.md](docs/PROVENANCE.md)**, [`base/ARIS_SNAPSHOT.json`](base/ARIS_SNAPSHOT.json), and [`mcp-servers/SOURCE.md`](mcp-servers/SOURCE.md) for exact file-level provenance.

- The MathRSI workflow, scripts, and bundled ARIS components are licensed under the **[MIT License](LICENSE)**.
- Archived academic papers, preprints, and third-party historical reference materials under `plugins/` and `development/` retain their original authors' and publishers' copyrights; the repository's MIT license does not relicense those third-party works.
