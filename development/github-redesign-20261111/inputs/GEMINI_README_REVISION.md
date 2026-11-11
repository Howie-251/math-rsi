threadId: f7da0d0f-54dd-42a7-9244-b8cca40c5a29

### 设计决策说明（中文）

弃用电路图式旧配图与拥挤的多列大表，全文仅保留一张三列五阶段表。首屏聚焦品牌与六大数学前沿（每题两句内交代结论、关键状态与证据链接），紧接 Quick Start。核心架构对应白底深墨单蓝强调的三层横带（`Base` / `Domain plugins` / `Task workspace`），配图用 `[diagram]` 占位，历史快照收束于折叠区与链接。

---

### 英文 `README.md` 完整正文草稿

```markdown
<div align="center">

# MathRSI

*SII MathRSI Team*

**Research advances. The workflow learns.**
An agent-executable, self-evolving workflow and domain knowledge harness for rigorous mathematical research.

[中文说明](README.zh-CN.md) · [Results](#six-mathematical-frontiers) · [Quick Start](#quick-start) · [Architecture & Workflow](#three-layer-architecture--workflow) · [v4 & Evolution](#evolution-v4--main) · [Documentation](#documentation--provenance)

</div>

MathRSI organizes mathematical research from problem formulation and literature verification to adversarial route exploration, proof construction, independent auditing, optional Lean formalization, and reproducible handoff. Coding agents (**Claude Code** and **Codex**) execute structured Markdown skills while preserving exact quantifiers and original proof obligations.

---

## Six Mathematical Frontiers

Research across six domains both produces mathematical results and feeds reusable methods back into MathRSI. To explore the interactive bilingual visual reader locally after cloning, open `development/homepage-redesign-20261105/site/index.html` in a browser.

- **Property B** *(Hypergraph 2-coloring)* — Establishes eight lower bounds on $m(k)$ for $k = 5\text{–}12$ ($35, 67, 131, 267, 543, 1112, 2275, 4664$) and a uniform improvement over the specified RS budget for all $k \ge 12$. Established in pre-harness ARIS studies and distilled into `v1`; $m(5) \ge 33, 34$ and the uniform theorem have end-to-end Lean proofs, while $m(5) \ge 35$ has a complete written candidate with incomplete Lean ([case study](case-studies/property-b/README.md) · [plugin](plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)).
- **Error-Correcting Codes** *(Binary linear code distances)* — Settles four exact optimal distances: $d_2(43,10)=16$, $d_2(44,10)=17$, and $d_2(44,11)=16$ from a complete 172-parent exclusion, plus $d_2(42,16)=12$ applying a published 2020 theorem. Lean reductions keep explicit external premises; $16 \le d_2(45,11) \le 17$ remains open, and the `[72,36,≥16]` A/B/C split is a workflow organization example rather than a solved parameter ([plugin](plugins/ecc/skills/mathrsi-ecc/SKILL.md) · [evidence](plugins/ecc/evidence/IMPLEMENTATION.md)).
- **Degree–Diameter** *(Largest graphs for given degree and diameter)* — Produces a 2,567-vertex $(10,4)$ graph exceeding the Comellas entry of 2,566 (checked 2026-11-05), alongside earlier dated table improvements at $(11,5)$, $(12,5)$, and $(16,4)$. The $(10,4)$ graph was constructed in a `v2` + DD run (with the PR #7 handoff repair) and preserves all-roots BFS and `Fin 2567` Lean assembly receipts, with external formal C review still incomplete ([case study](case-studies/degree-diameter/README.md) · [plugin](plugins/degree-diameter/README.md)).
- **Erdős Problem 86** *(Square-free hypercube subgraphs)* — Lowers the asymptotic edge-density upper bound for $C_4$-free subgraphs of $Q_n$ from $0.60318$ to $< 0.59155154$ toward the conjectured $1/2$. Verified by an exact rational Gram certificate replay across all $13,150,453$ legal $Q_4$ completions and analytic high-dimensional averaging, with no Lean formalization ([plugin](plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/SKILL.md) · [evidence](plugins/hypercube-extremal/evidence/IMPLEMENTATION.md)).
- **Ruskey–Savage $Q_6$** *(Hypercube Hamilton extension)* — Proves that every matching in $Q_6$ extends to a Hamilton cycle, and with imported results covers matchings using at most six directions in any $Q_n$. A finite computational certificate verifies rank $1024$ across $1024$ forests ($1,048,576$ connectivity bits); the whole-proof audit is same-family/provisional with no Lean ([plugin](plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/SKILL.md) · [evidence](plugins/hypercube-hamilton/evidence/IMPLEMENTATION.md)).
- **Happy Ending** *(Erdős–Szekeres for convex heptagons)* — Incorporates working structural proofs for $N(7,6,7) \le 75$ and $N(7,7,7) \le 76$, lowering the geometric threshold bound to $\mathrm{ES}(7) \le 77$ (from 78). These manuscripts remain same-session, unreviewed, and unaccepted (using restricted capacity 25 with historical SAT acceptance; $\le 74$ holds only on specified subclasses), while bounded Python checks independently verify the 25-point abstract lower witness and 10/11-point strategy counterexamples ([plugin](plugins/happy-ending/skills/mathrsi-happy-ending/SKILL.md) · [v4 record](development/evolution/v4-20261108/HAPPY_ENDING.md)).

---

## Quick Start

See **[docs/QUICKSTART.md](docs/QUICKSTART.md)** for full environment setup and **[examples/proof-repair/README.md](examples/proof-repair/README.md)** for a self-contained walkthrough using Python 3.9+ standard library.

```bash
git clone https://github.com/lisresearchgroup/math-rsi.git
cd math-rsi
python3 tools/check_links.py
python3 examples/proof-repair/replay.py
```

Launch **Claude Code** or **Codex** in the clone (see **[docs/REVIEWER_MCP.md](docs/REVIEWER_MCP.md)** for optional cross-model reviewer setup). Invoke `/mathrsi-research` (Claude Code `.claude/skills/`) or `$mathrsi-research` (Codex `.agents/skills/`), or paste a direct prompt:

```text
Read /abs/path/to/math-rsi/base/skills/mathrsi-research/SKILL.md
(and /abs/path/to/math-rsi/plugins/<domain>/skills/<domain-entry>/SKILL.md if applicable).
In workspace /abs/path/to/my-task, study <problem statement or candidate proof>.
Restore any existing spec, NEXT_SESSION.md, and research-wiki; enter at the stage
supported by current evidence, read returned artifacts before dispatching the next step,
and use helpers from /abs/path/to/math-rsi/base/tools (ARIS_REPO=/abs/path/to/math-rsi/base).
```

---

## Three-Layer Architecture & Workflow

<!-- [diagram] Placeholder: simplified 3-layer architecture figure (white background, deep ink, single blue accent showing Base / Domain plugins / Task workspace) -->
**[diagram: Three-layer architecture — Base Core, Domain Plugins, and Task Workspace]**

MathRSI strictly separates general orchestration, domain mathematics, and per-problem state (**[Plugin Contract](docs/PLUGIN_CONTRACT.md)**):
1. **Base Core (`base/`)**: 10 MathRSI skills (9 solving skills plus [`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md)), 32 bundled dual-host ARIS skills, verification contracts, and 53 Python helpers (`base/tools/`).
2. **Domain Plugins (`plugins/`)**: 6 domains and 14 domain skills supplying specialized reductions, proved lemmas, failure maps, and callable checkers without mutating `base/`.
3. **Task Workspace (`<task-dir>/`)**: Problem-specific `FORMAL_SPEC.md`, continuous `research-wiki/`, proof drafts, certificates, `VERIFICATION.md`, and `NEXT_SESSION.md` (**[Workspace Guide](docs/WORKSPACE.md)**).

The top-level orchestrator ([`mathrsi-research`](base/skills/mathrsi-research/SKILL.md)) routes problems across five adaptive stages while reading and updating `<W>/research-wiki/` at every step (**[Workflow Details](docs/WORKFLOWS.md)** · **[Domain Routing](docs/DOMAIN_ROUTING.md)**):

| Stage | Role & Return Path | Continuous Wiki & Primary Outputs |
| :--- | :--- | :--- |
| **1. [`prepare`](base/skills/mathrsi-prepare/SKILL.md)** | Chains `specify` $\rightarrow$ `survey` (literature/errata search) $\rightarrow$ final `specify`. | Reads prior imports/failures; writes verified paper conditions, `FORMAL_SPEC.md`, `LITERATURE.md`. |
| **2. [`route-loop`](base/skills/mathrsi-route-loop/SKILL.md)** | Adversarial route critique (`mcp-servers/`), informative probes, and global progress checks. | Reads failed domains; writes route changes, counterexamples, and `ROUTE_REPORT.md`. |
| **3. [`prove`](base/skills/mathrsi-prove/SKILL.md)** | Drafts lemmas, dispatches domain checkers or scoped workers, and binds results to the original caller. | Reads active lemma/failure pages; writes conditional lemmas, certificates, and `PROOF_DRAFT.md`. |
| **4. [`verify`](base/skills/mathrsi-verify/SKILL.md)** | Runs `proof-checker` repair loops, exact certificate replays, or `lean-formalize` with premise audits; returns local checks to `prove`. | Reads import premises; writes checked scopes, `PROOF.md`/`.tex`, and `VERIFICATION.md`. |
| **5. [`handoff`](base/skills/mathrsi-handoff/SKILL.md)** | Packages readable proofs, standalone reproduction commands, and resumption pointers. | Syncs adopted results; writes `HANDOFF.md`, `NEXT_SESSION.md`, and reproducible bundle. |

---

## Evolution: `v4` & `main`

<!-- [diagram] Placeholder: v0 -> v4 evolution summary figure -->
**[diagram: MathRSI evolution across Base workflow and Domain plugins (`v0` → `v4` + `main`)]**

Through the outer [`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md) workflow, research bottlenecks strengthen the shared base while mathematical methods deepen domain plugins in place (**[v4 Changes](docs/V4_CHANGES.md)**):

- **Shared Base Improvements (`v4` + `main`)**:
  1. *Tight integer equality to compatible witness (`v4`)*: When an integer bound misses by one, `route-loop`, `prove`, and `verify` trace the same inequality chain to recover simultaneous zero-slack conditions, perform a legal equal-size exchange, force a witness from capacity, and verify endpoint/marked compatibility at the caller ([reference](base/skills/mathrsi-prove/references/critical-equality.md)).
  2. *Mandatory global progress reassessment (`main`)*: At checkpoints or when consecutive batches leave the core bottleneck unchanged, two independent read-only agents evaluate whether a valid reduction reduces a key mathematical obstacle or total completion cost, allowing Root to switch routes, close connections, or authorize bounded exploration under an explicit budget ([protocol](base/skills/mathrsi-research/references/global-reassessment.md)).
- **Domain Plugin Deepening (`v4` + `main`)**:
  - *Happy Ending (`v4`)*: Absorbs equality-exchange references and 10/11-point strategy counterexample checkers ([reference](plugins/happy-ending/skills/mathrsi-happy-ending/references/equality-exchange.md)).
  - *Degree–Diameter (`v4`)*: Adds saturated matching-cut vertex insertion, old-only switches, and portable 10-graph edit replay ([reference](plugins/degree-diameter/references/saturated-insertion-and-replay.md)).
  - *ECC Node Protocol (`main`)*: Tracks stable `node_id` and `task_id` records to reuse exclusions, dispatch shared computations once, and require full parent coverage ([protocol](plugins/ecc/skills/mathrsi-ecc/references/node-research.md)).

<details>
<summary><strong>Release snapshots & version history (v1 – v4)</strong></summary>

`main` carries the current `v4` release plus subsequent maintenance; fixed Git tags preserve complete repository snapshots: **[v1](https://github.com/lisresearchgroup/math-rsi/tree/v1)** · **[v2](https://github.com/lisresearchgroup/math-rsi/tree/v2)** ([changes](docs/V2_CHANGES.md)) · **[v3](https://github.com/lisresearchgroup/math-rsi/tree/v3)** ([changes](docs/V3_CHANGES.md)) · **[v4](https://github.com/lisresearchgroup/math-rsi/tree/v4)** ([changes](docs/V4_CHANGES.md)). See **[Evolution Guide](docs/EVOLUTION_WORKFLOW.md)** and **[Architecture Figures](figures/mathrsi/README.md)** for historical diagrams and maintenance records.
</details>

---

## Documentation & Provenance

- **Reference Guides** *(detailed guides in `docs/` are primarily in Chinese)*: [Quick Start](docs/QUICKSTART.md) · [Workflows](docs/WORKFLOWS.md) · [Domain Routing](docs/DOMAIN_ROUTING.md) · [Workspace & Wiki](docs/WORKSPACE.md) · [Plugin Contract](docs/PLUGIN_CONTRACT.md) · [ARIS Reuse](docs/ARIS_REUSE.md) · [Reviewer MCP](docs/REVIEWER_MCP.md) · [Validation Scope](development/VALIDATION.md)
- **Provenance & License**: Built on **[ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** (commit `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`, Copyright (c) 2026 wanshuiyin) and research artifacts in `plugins/` and `case-studies/` (**[docs/PROVENANCE.md](docs/PROVENANCE.md)** · [`base/ARIS_SNAPSHOT.json`](base/ARIS_SNAPSHOT.json) · [`mcp-servers/SOURCE.md`](mcp-servers/SOURCE.md)). Workflow and scripts are **[MIT Licensed](LICENSE)**; archived papers and third-party materials retain their original copyrights.
```
