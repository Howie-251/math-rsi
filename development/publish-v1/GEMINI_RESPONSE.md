threadId: 883091cc-2a08-433e-a3a5-a3163258fa05

### Part 1: Presentation Strategy & Concrete Risks for v1 Publication

To make `lisresearchgroup/math-rsi` immediately usable for group members while keeping technical claims accurate:

1. **Lead with Operational Value, Not Disclaimers**:
   * Open with what a researcher actually gets: an agent-executable mathematical research harness that takes a problem at any stage (a raw statement, a stalled proof draft, or a candidate proof needing verification) and connects literature checks, adversarial route probing, derivation/computation, independent proof auditing, and reproducible handoff while preserving exact quantifiers and caller bindings.
   * Consolidate all validation boundaries, environmental dependencies (`pdflatex`, `lean`, model CLIs), and the status of `base-v2` / `ECC (draft)` into **one dedicated Validation & Current Scope section** near the bottom so the main workflow sections read as clear operational instructions.

2. **Concrete Presentation & Onboarding Risks to Watch**:
   * **Risk 1 — "Where is the CLI entrypoint?" confusion**: Readers accustomed to Python packages may look for a top-level `python main.py` autonomous runner. The README must state upfront that MathRSI is an **agent-executed skill harness**: you start by pointing Claude Code or Codex at [base/skills/mathrsi-research/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md) (or using the repo-relative `.claude/skills/` and `.agents/skills/` aliases) and passing a task workspace path.
   * **Risk 2 — `ARIS_REPO` path binding for helpers**: Because bundled ARIS skills invoke Python helpers (`research_wiki.py`, `reviewer_route.py`, etc.), group members running helpers manually or from an external workspace directory need to know that `ARIS_REPO` points to `<clone>/base` (so `$ARIS_REPO/tools/...` resolves inside this repository without needing an external `~/.aris` checkout).
   * **Risk 3 — Cross-language link expectations**: While the top-level `README.md`, `figures/mathrsi/README.md`, `docs/QUICKSTART.md`, and `examples/proof-repair/README.md` will be in English (or bilingual-friendly), the detailed workflow/contract docs ([docs/WORKFLOWS.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/WORKFLOWS.md), [docs/REVIEWER_MCP.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/REVIEWER_MCP.md)) and MathRSI `SKILL.md` files are currently written in Chinese. Noting this briefly in the documentation index prevents surprise for readers navigating from the English README into `docs/` and `base/skills/`.
   * **Risk 4 — Pending files (`docs/QUICKSTART.md` and `examples/proof-repair/README.md`)**: If `tools/check_links.py` is run before pushing, ensure `docs/QUICKSTART.md` and `examples/proof-repair/README.md` are created before the final link check so `README.md` has zero broken local links.

---

### Part 2: English `README.md` Draft

````markdown
# MathRSI

**An agent-executable workflow and domain knowledge harness for rigorous mathematical research, built on a self-contained adaptation of [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep).**

MathRSI organizes mathematical research from problem formulation and literature verification to route exploration, proof construction, independent auditing, optional Lean formalization, and reproducible handoff. Instead of reducing research to a rigid state machine or a single prompt, MathRSI provides structured Markdown skills, domain plugins, cross-model review bridges, and verification contracts that coding agents (Claude Code and Codex) execute step by step while preserving exact quantifiers and original problem obligations.

![MathRSI: specialize, learn, evolve](figures/mathrsi/01-evolution.png)

---

## Why MathRSI

- **Enter at the current evidence stage**: Start from a raw problem statement, resume an in-progress proof workspace, or jump directly to auditing and repairing a complete candidate proof.
- **Keep lemmas bound to the original problem**: Intermediate reductions, conditional lemmas, and computational certificates are tracked against their actual callers so a local result or relaxed probe is never mistaken for a proof of the main theorem.
- **Self-contained dual-host ARIS bundle**: Ships with **9 MathRSI workflow skills**, **30 bundled ARIS skills** in both Claude Code (`base/skills/`) and Codex (`base/skills/skills-codex/`) layouts, **53 helper scripts** (`base/tools/`), **4 MCP reviewer bridge servers** (`mcp-servers/`), and the **Property B domain plugin** (`plugins/propertyb/`). No external ARIS checkout or global installer is required.
- **Clean separation of core, domain, and workspace**: Running a task or domain plugin updates only the problem's task workspace. Reusable domain tools are curated into plugins, and general workflow lessons are distilled into the next base iteration through a separate, human-authorized [evolution workflow](docs/EVOLUTION_WORKFLOW.md).

---

## Quick Start

See **[docs/QUICKSTART.md](docs/QUICKSTART.md)** for step-by-step setup and **[examples/proof-repair/README.md](examples/proof-repair/README.md)** for a self-contained walkthrough that audits, repairs, and hands off a flawed candidate proof.

### 1. Clone and verify the local bundle

Requires Python 3.9+ (standard library only for bundled helpers and offline tests):

```bash
git clone https://github.com/lisresearchgroup/math-rsi.git
cd math-rsi

python3 tools/check_links.py
python3 -B base/tests/smoke_bundle.py --help
python3 -m unittest discover -s mcp-servers/tests -p 'test_*.py' -v
```

### 2. Run a mathematical task in your agent

MathRSI has no monolithic Python scheduler; the workflow is executed directly by your file-reading coding agent.

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

## Three-Layer Architecture

| Layer | Location | Role |
| :--- | :--- | :--- |
| **Base Core** | `base/` | 9 MathRSI orchestration & subworkflow skills, 30 dual-host ARIS skills, shared verification contracts, and `base/tools/` helpers (`ARIS_REPO=<clone>/base`). |
| **Domain Plugins** | `plugins/` | Domain reductions, proved lemmas, counterexample maps, and domain checkers. Includes the complete **Property B** plugin (`plugins/propertyb/`, 4 skills + archive) and a draft **ECC** plugin (`plugins/ecc/`). |
| **Task Workspace** | User task dir | Problem-specific `FORMAL_SPEC.md`, `research-wiki/`, proof drafts, computational logs, `VERIFICATION.md`, and `NEXT_SESSION.md`. |

As defined in the [Plugin Contract](docs/PLUGIN_CONTRACT.md), plugins receive the active mathematical obligation and return scoped evidence to the calling stage. Plugins never mutate `base/` or weaken the original acceptance criteria during a problem-solving run.

---

## Five Executable Subworkflows

The top-level orchestrator ([`mathrsi-research`](base/skills/mathrsi-research/SKILL.md)) owns stage transitions. It inspects existing workspace evidence, delegates one subworkflow scope at a time, reads the returned artifacts and remaining obligations, and dispatches the next step.

![Inside MathRSI Base: five adaptive subworkflows](figures/mathrsi/02-workflows.png)

| Subworkflow | What It Does | Embedded ARIS Skills Used | Primary Outputs |
| :--- | :--- | :--- | :--- |
| **1. [`mathrsi-prepare`](base/skills/mathrsi-prepare/SKILL.md)** | Chains [`mathrsi-specify`](base/skills/mathrsi-specify/SKILL.md) (preliminary) $\rightarrow$ [`mathrsi-survey`](base/skills/mathrsi-survey/SKILL.md) (broad alias/citation/errata search & primary-source verification) $\rightarrow$ `mathrsi-specify` (final). | `research-lit`, `research-wiki`, `wiki-enrich` | `FORMAL_SPEC.md`, `LITERATURE.md`, updated wiki entities |
| **2. [`mathrsi-route-loop`](base/skills/mathrsi-route-loop/SKILL.md)** | Mathematical adaptation of ARIS `auto-review-loop`: proposes a proof route, runs adversarial review, executes informative math/compute probes, revises the route, and rechecks with persistent reviewer memory. | `auto-review-loop` *(math adaptation)*, `research-review` *(composed)* | `ROUTE_REPORT.md` with first concrete proof obligations & reviewer traces |
| **3. [`mathrsi-prove`](base/skills/mathrsi-prove/SKILL.md)** | Stabilizes objects and derivations, drafts lemmas, runs domain computations or parallel workers with exclusive write scopes, and binds results back to the original problem caller. | `formula-derivation`, `proof-writer`, `proof-orchestrator` *(optional)* | `PROOF_DRAFT.md`, computational certificates, or exact blocking gaps |
| **4. [`mathrsi-verify`](base/skills/mathrsi-verify/SKILL.md)** | Calls [`mathrsi-assemble`](base/skills/mathrsi-assemble/SKILL.md) when pieces are scattered, checks domain coverage and independent exact arithmetic, runs the ARIS `proof-checker` audit-and-repair loop, and connects optional Lean formalization. | `proof-writer` *(via assemble)*, `proof-checker`, `lean-formalize` *(optional)* | `PROOF.md` / `PROOF.tex`, `VERIFICATION.md`, `PROOF_AUDIT.md` |
| **5. [`mathrsi-handoff`](base/skills/mathrsi-handoff/SKILL.md)** | Packages the readable proof, standalone reproduction inputs/commands, citation checks, optional HTML/PDF views, updated wiki state, and resumption notes. | `render-html`, `citation-audit` / `paper-compile` *(when requested)* | `HANDOFF.md`, `NEXT_SESSION.md`, reproducible bundle |

### Targeted Return Paths, Wiki Memory, and Adversarial Review

- **Persistent Research Wiki**: `research-wiki` and `wiki-enrich` run across all stages to accumulate verified imports, proved conditional lemmas, and failed routes. Agents read full entity pages—not just auto-generated `query_pack.md` summaries—when resuming or checking conditions.
- **Targeted Literature Lookup (`route-loop` / `prove` $\rightarrow$ `survey`)**: When a new import question or suspected counterexample arises mid-proof, the caller invokes `mathrsi-survey` for an incremental source check and returns directly to the active obligation without resetting `FORMAL_SPEC.md`.
- **Local Verification Return (`prove` $\leftrightarrow$ `verify`)**: High-risk sub-lemmas or domain certificates can be verified early; a local pass returns to the parent `prove` caller to complete downstream steps rather than triggering full-problem `handoff`.
- **Repair vs. Route Rethink**: Proof gaps, index errors, or checker fixes return from `verify` to `prove`. Only when a counterexample refutes a core lemma or representation does the orchestrator return from `prove` to `route-loop`.
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

### Error-Correcting Codes (`plugins/ecc/`) — Draft

Retains an initial draft ([`mathrsi-ecc`](plugins/ecc/skills/mathrsi-ecc/SKILL.md)) and read-only historical handoff snapshots ([`development/context/ecc-source/`](development/context/ecc-source/README.md)) that informed MathRSI's workflow transitions. It is not yet accepted to the Property B standard and is excluded from default skill discovery.

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
- **[Evolution Workflow](docs/EVOLUTION_WORKFLOW.md)** — Standalone maintenance workflow for distilling, reviewing, and testing general workflow lessons for the next base iteration.
- **[Architecture Figures](figures/mathrsi/README.md)** — High-resolution diagrams, generation prompts, and visual alignment review records.

---

## Validation & Current v1 Scope

Full verification records are maintained in **[development/VALIDATION.md](development/VALIDATION.md)** and **[development/figure-workflow-check-20261101/REPORT.md](development/figure-workflow-check-20261101/REPORT.md)**:

- **Repository & bundle integrity**: All 61 core/plugin documents and 983 local link targets pass `tools/check_links.py`. `base/tests/smoke_bundle.py` verifies the 30 dual-host ARIS skills, shared references, and `research_wiki.py` / `reviewer_route.py` / `render_html.py` execution inside an isolated copy.
- **End-to-end proof-repair trial**: Tested on an independent agent handed a problem specification and a flawed candidate TeX proof without hints ([report](development/figure-workflow-check-20261101/REPORT.md), [example](examples/proof-repair/README.md)). The agent routed `mathrsi-research → mathrsi-verify → proof-checker → mathrsi-handoff`, identified a false edge-event independence step, verified a 5-vertex 32-coloring counterexample (marginal bad probability $1/8$, joint $1/16 \neq 1/64$), repaired the proof via an indicator-function union bound preserving the exact theorem statement ($\ge 1/8$ for 4-uniform hypergraphs with $\le 7$ edges), and passed fresh and blind re-reviews (`acceptance_status=provisional`, same-family native reviewer). Because the test machine had no local TeX installation (`pdflatex` exit 127), `details.workflow_complete=false` is recorded with PDF compilation pending.
- **Targeted workflow & domain trials**: Verified local `prove → verify → caller` return behavior ([trial report](development/workflow-redesign/behavioral-trial/REPORT.md)), standalone `research-wiki` forward use, and independent replays of bundled Property B checkers (`m(6)`, `m(7)`, `m(8)/m(9)`, `k=12` instances).
- **MCP reviewer bridges**: 61 offline unit tests (`mcp-servers/tests/`) pass across all four bundled Python servers. In live bundled server checks ([live report](development/review-loop-integration/LIVE_MCP_EXECUTION.md)), Antigravity/Gemini cross-process session continuation succeeded, while a bundled Grok first-round call timed out at 600s without auto-retry on that host session.
- **Known boundaries**:
  - `mathrsi-base-v2` in Figure 1 depicts the planned evolution target governed by [docs/EVOLUTION_WORKFLOW.md](docs/EVOLUTION_WORKFLOW.md), not a released version or a benchmark claim of automated recursive self-improvement.
  - External model CLIs/credentials, LaTeX (`pdflatex`/`latexmk`), and Lean 4 (`elan`/`lake`) are environmental dependencies not bundled in git.
  - While individual subworkflows, domain checkers, and the proof-repair loop have been executed, an end-to-end run on a brand-new long open mathematical problem from initial web literature search through full multi-round `route-loop` A–E cycles and new Lean formalization remains future validation.

---

## Provenance & License

MathRSI's workflow and bundled ARIS skill adaptations build on **[ARIS (Auto-claude-code-research-in-sleep)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** (snapshot commit `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`, Copyright (c) 2026 wanshuiyin) and research artifacts from the Property B and ECC projects. See **[docs/PROVENANCE.md](docs/PROVENANCE.md)**, [`base/ARIS_SNAPSHOT.json`](base/ARIS_SNAPSHOT.json), and [`mcp-servers/SOURCE.md`](mcp-servers/SOURCE.md) for exact file-level provenance.

- The MathRSI workflow, scripts, and bundled ARIS components are licensed under the **[MIT License](LICENSE)**.
- Archived academic papers, preprints, and third-party historical reference materials under `plugins/` and `development/` retain their original authors' and publishers' copyrights; the repository's MIT license does not relicense those third-party works.
````

