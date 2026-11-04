以下为您提供可直接替入 [README.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.md) 与 [README.zh-CN.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.zh-CN.md) 的中英文发布态定稿（按 `v3` 合入 `main` 并固定标签编写），以及 3 条结构编辑建议。

---

### 一、`README.md` 英文可直接插入稿

#### 1. 替换顶部版本栏、导语与演进说明（替换原 [README.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.md#L5-L16) 第 5–16 行）

```markdown
Fixed versions: **[v1](https://github.com/lisresearchgroup/math-rsi/tree/v1)** ([ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v1.zip)) · **[v2](https://github.com/lisresearchgroup/math-rsi/tree/v2)** ([ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v2.zip)) · **[v3](https://github.com/lisresearchgroup/math-rsi/tree/v3)** ([ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v3.zip)). Each tag preserves a complete repository snapshot and stays fixed; `main` tracks the recommended **v3** release. See [v3 changes and runnable checks](docs/V3_CHANGES.md) and [v2 changes](docs/V2_CHANGES.md).

**An agent-executable, self-evolving workflow and domain knowledge harness for rigorous mathematical research.**

MathRSI organizes mathematical research from problem formulation and literature verification to route exploration, proof construction, independent auditing, optional Lean formalization, and reproducible handoff. Structured Markdown skills, domain plugins, cross-model review bridges, and verification contracts let coding agents (Claude Code and Codex) execute research step by step while preserving exact quantifiers and original problem obligations.

### How Research Experience Evolves MathRSI (`v0` → `v3`)

MathRSI evolves through an explicit feedback loop: **completed mathematical investigations expose concrete reasoning or verification bottlenecks $\rightarrow$ [`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md) distills reusable workflow rules into `base/` and domain reductions/checkers into `plugins/` $\rightarrow$ subsequent research inherits the strengthened harness.** Across all versions, `base/` remains a lean core of **10 MathRSI skills** (9 solving workflows + 1 maintenance skill), while domain capability expands to **6 domains and 14 domain skills**.

| Stage | Research Experience Input | Base Workflow Changes (`base/`) | Domain Plugins & Verification Assets (`plugins/`) |
| :--- | :--- | :--- | :--- |
| **v0** *(Pre-harness tools)* | Initial **Property B** ($m(k)$ hypergraph coloring) and first-wave **ECC** ($[43,10,16]$, 172-parent double scans) studied with standalone skills; accumulated raw wikis, failure maps, and proofs before a unified MathRSI harness existed *(not a Git tag)*. | Standalone literature, review, and proof skills without unified stage routing, quantifier tracking, or caller return contracts. | Raw problem workspaces and proof scripts prior to `base / plugin / task` separation. |
| **[v1](https://github.com/lisresearchgroup/math-rsi/tree/v1)** | Synthesis of [six concrete research transitions](development/workflow-redesign/REAL_PROJECT_TRANSITIONS.md) from Property B and initial ECC. | Established the **5 solving subworkflows** (`prepare`, `route-loop`, `prove`, `verify`, `handoff`), 3-layer `base / plugin / task` architecture, separation of adversarial route exploration from full proof acceptance, persistent `research-wiki` return paths, on-demand Lean, and the self-contained dual-host skill bundle. | Complete **[Property B](plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)** plugin (4 skills + knowledge base & archive); initial **ECC** draft plugin. |
| **[v2](https://github.com/lisresearchgroup/math-rsi/tree/v2)** | Historical **Degree–Diameter (DD)** research (153 graphs across 43 $(d,k)$ pairs, 47 concrete-graph Lean proofs). Also absorbs workflow patch PR #7 (dispatch, file delivery, recovery). | Added outer **[`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md)** maintenance skill and [4 base improvements](docs/V2_CHANGES.md): **(1)** public baseline updates prune superseded queue tasks while preserving fixed theorem validity; **(2)** object/field/rule changes separate positive-evidence inheritance from old refutation scope; **(3)** common source-input coverage replaces single-route sufficient gates; **(4)** formal-only targets go directly to `lean-formalize` on actual exports/axioms without forcing TeX first. | Added **[Degree–Diameter](plugins/degree-diameter/README.md)** plugin (4 skills: entry, construction, obstruction certificate, transfer diagnosis + source wiki & archive). |
| **[v3](https://github.com/lisresearchgroup/math-rsi/tree/v3)** *(Current)* | **Erdős 86** ($Q_d$ edge-induced 4-cycles), **Ruskey–Savage $Q_6$** (Hamilton matching extension), second-wave **ECC** (follow-on work using methods/workflow inherited through v1/v2), and **Happy Ending** ($ES(7)$ signotopes). | Added [4 shared evidence-loop actions](development/evolution/v3-20261104/base/BASE_CHANGES.md) (detailed below) across `route-loop`, `prove`, `verify`, and `handoff`, verified via [bounded use cases](development/evolution/v3-20261104/base/USE.md) and two rounds of Gemini 4 + Opus 5.5 [source maintenance review](development/evolution/v3-20261104/reviews/DISPOSITION.md). | Upgraded the existing **[ECC](plugins/ecc/README.md)** plugin (`mathrsi-ecc` + `ecc-certificate`, actual matrices, index-169 parent replay, two Lean reduction projects); added **[Hypercube Extremal](plugins/hypercube-extremal/README.md)**, **[Hypercube Hamilton](plugins/hypercube-hamilton/README.md)**, and **[Happy Ending](plugins/happy-ending/README.md)** plugins + thin Python candidate checkers ([routing map](docs/DOMAIN_ROUTING.md)). |

### Four Shared Workflow Improvements in v3

Each v3 base change addresses a recurring failure mode observed in research and executes inside the existing subworkflows without adding a new orchestrator ([base diff report](development/evolution/v3-20261104/base/BASE_CHANGES.md) · [runnable examples](development/evolution/v3-20261104/base/USE.md)):

| Bottleneck Observed in Research | What v3 Changes in Base Workflows | Owning Subworkflows | Source Case & Plugin Connection |
| :--- | :--- | :--- | :--- |
| **1. Working-set overfitting & lost historical bests**: A candidate scores well on an active subset but violates the full domain, or a later iteration overwrites an earlier verified bound. | Track `restricted` (working-set), `full`-domain, `exploration_best`, and `accepted_best` separately. Feed actual full-domain violating inputs back into candidate generation, and re-verify the final exact object over the full domain before updating `accepted_best`. | [`route-loop`](base/skills/mathrsi-route-loop/SKILL.md), [`verify`](base/skills/mathrsi-verify/SKILL.md), [`handoff`](base/skills/mathrsi-handoff/SKILL.md) | **Erdős 86** active-row pool separation & exact rational PSD check ([`check_q4_candidate.py`](plugins/hypercube-extremal/tools/check_q4_candidate.py)). |
| **2. Untracked roots, targets, or required edges across reductions**: Symmetry quotients, completions, or contractions silently alter which root, partner, or mandatory edge is being proved. | Transport roots, targets, partner maps, and required edges through every transformation, compose the maps, and recover original partners and required edges at the calling obligation. | [`prove`](base/skills/mathrsi-prove/SKILL.md), [`verify`](base/skills/mathrsi-verify/SKILL.md) | **Erdős 86** synchronized rooted $Q_3$ flags; **Ruskey–Savage $Q_6$** root-preserving maximalization; **Happy Ending** leftmost-pivot chart transport. |
| **3. Intractable universal input families & discarded failure pools**: Direct enumeration of all configurations explodes, and subsets failing a sufficient gate are thrown away even when individual instances are valid. | Query the domain plugin for a proved finite basis/rank/coverage bridge to close universal obligations; retain legal objects from sufficient-gate failure pools and route them to per-instance positive certificates. | [`route-loop`](base/skills/mathrsi-route-loop/SKILL.md), [`prove`](base/skills/mathrsi-prove/SKILL.md) | **Ruskey–Savage $Q_6$** 1024-forest $\mathbb{F}_2$ rank bridge ([`check_forest_rank.py`](plugins/hypercube-hamilton/tools/check_forest_rank.py)) and rank-deficient positive certificates. *(Happy Ending common middle matching & bilateral compensation reinforce common-coverage rules in plugin knowledge.)* |
| **4. Hidden mathematical premises in Lean theorem headers**: `#print axioms` reports only standard axioms while an external scan, literature bound, or unverified matrix sits in an explicit `(h : ...)` theorem hypothesis. | Inspect every explicit theorem parameter and unfolded definition alongside `#print axioms`; separate kernel-proved reductions and verified actual data from external literature, classification, or scan assumptions. | [`verify`](base/skills/mathrsi-verify/SKILL.md), [`handoff`](base/skills/mathrsi-handoff/SKILL.md) | **ECC** `ecc43`/`ecc42` Lean audits ([`lean-boundary.md`](plugins/ecc/skills/ecc-certificate/references/lean-boundary.md)) vs. actual generator matrix verification. |

<details>
<summary><strong>Historical v2 architecture diagram</strong> (retained as a v2 visual snapshot; its ECC-draft and future-v3 labels reflect the v2 release)</summary>

![Historical v2 evolution diagram: its ECC draft and future-v3 labels describe that snapshot](figures/mathrsi/01-evolution.png)

See [figure sources and review](figures/mathrsi/README.md).
</details>
```

#### 2. 折叠第 88–90 行的 v2 历史工作流图（替换原 [README.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.md#L88-L90) 第 88–90 行）

```markdown
<details>
<summary><strong>Historical v2 workflow diagram</strong> (the same 5 subworkflows remain in v3; see the tables above and <a href="docs/DOMAIN_ROUTING.md">DOMAIN_ROUTING.md</a> for v3 domain integration)</summary>

![Five solving subworkflows with embedded ARIS, continuous research wiki, optional Lean, and separate mathrsi-meta-evolve maintenance](figures/mathrsi/02-workflows.png)
</details>
```

#### 3. 更新 `### v3 Domain Capabilities` 表以包含新候选核验工具（替换原 [README.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.md#L131-L140) 第 131–140 行）

```markdown
### v3 Domain Capabilities

| Domain Entry & Skills | What the Agent Can Do | Bounded Checks & New-Candidate Tools |
| :--- | :--- | :--- |
| **[ECC](plugins/ecc/README.md)**: [`mathrsi-ecc`](plugins/ecc/skills/mathrsi-ecc/SKILL.md) + [`ecc-certificate`](plugins/ecc/skills/ecc-certificate/SKILL.md) | Binary linear-code reductions, common coset/pair constraints, actual-matrix distance checks (`[42,16,12]` actual / `[42,16,9]` published $E_3$ route; `[45,11,17]` remains open), and explicit Lean premise audits. Upgrades the existing plugin rather than creating an `ecc2` tree. | [172 saved-set readback, index-169 complete parent replay (`replay_one.py`), and actual-matrix checks](plugins/ecc/evidence/IMPLEMENTATION.md) |
| **[Hypercube Extremal](plugins/hypercube-extremal/README.md)**: [`mathrsi-hypercube-extremal`](plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/SKILL.md) | Common $Q_4$ completions, synchronized rooted flags, working-set separation, exact integer Gram PSD certificates, and high-dimensional averaging. | [Full $Q_4$ replay (`verify_final_q4.py`)](plugins/hypercube-extremal/evidence/IMPLEMENTATION.md), new-candidate evaluator [`check_q4_candidate.py`](plugins/hypercube-extremal/tools/check_q4_candidate.py), and [`materialize_search.py`](plugins/hypercube-extremal/tools/materialize_search.py) |
| **[Hypercube Hamilton](plugins/hypercube-hamilton/README.md)**: [`mathrsi-hypercube-hamilton`](plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/SKILL.md) | Root-preserving maximalization, universal forest-rank bridges over $\mathbb{F}_2$, positive certificates on rank-deficient pools, and marked gluing. | [A10 1024-forest replay](plugins/hypercube-hamilton/evidence/IMPLEMENTATION.md) and parameterized geometry/forest checker [`check_forest_rank.py`](plugins/hypercube-hamilton/tools/check_forest_rank.py) |
| **[Happy Ending](plugins/happy-ending/README.md)**: [`mathrsi-happy-ending`](plugins/happy-ending/skills/mathrsi-happy-ending/SKILL.md) + [`happy-ending-certificate`](plugins/happy-ending/skills/happy-ending-certificate/SKILL.md) | Cup/cap and rank-3 signotope models, weak vs. split $k$-gon and abstract vs. geometric distinctions, fixed common $R_5$ matching with bilateral low-predecessor compensation, and scoped witness checks. | Independent stdlib lower-25 checker [`check_lower25.py`](plugins/happy-ending/tools/check_lower25.py) ([result](plugins/happy-ending/evidence/lower25-independent.json)); archived 55-cell SAT imports and unreviewed structural drafts keep their distinct scopes (newly reported 75/76 chat screenshot awaits proof source). |

See **[docs/DOMAIN_ROUTING.md](docs/DOMAIN_ROUTING.md)** for exact stage-by-stage input/return bindings across all **6 domains (14 domain skills)**.
```

---

### 二、`README.zh-CN.md` 中文可直接插入稿

#### 1. 替换顶部版本栏、导语与演进说明（替换原 [README.zh-CN.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.zh-CN.md#L5-L17) 第 5–17 行）

```markdown
固定版本：**[v1](https://github.com/lisresearchgroup/math-rsi/tree/v1)**（[下载 ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v1.zip)）· **[v2](https://github.com/lisresearchgroup/math-rsi/tree/v2)**（[下载 ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v2.zip)）· **[v3](https://github.com/lisresearchgroup/math-rsi/tree/v3)**（[下载 ZIP](https://github.com/lisresearchgroup/math-rsi/archive/refs/tags/v3.zip)）。标签固定完整仓库快照，旧标签不移动；`main` 跟随当前推荐版 **v3**。详见 [v3 具体变化与可运行检查](docs/V3_CHANGES.md) 与 [v2 具体变化](docs/V2_CHANGES.md)。

**面向严谨数学研究、可由 agent 执行并持续自进化的工作流与领域知识框架。** 从文献查漏到严密证明，把问题形式化、路线对抗、推导构造、独立核验、按需形式化与可复现交接连成闭环。

主流程按现有成果选择入口，衔接五组可独立调用的子流程：**问题准备与文献（`prepare`）→ 求解路线迭代（`route-loop`）→ 证明推进（`prove`）→ 装配验证（`verify`）→ 交付沉淀（`handoff`）。** 每阶段由调用者读取实际产物后推进，始终绑定原始量词与主定理义务。

### 研究经验如何驱动版本演进（`v0` → `v3`）

MathRSI 的自演进遵循明确的反馈闭环：**真实数学攻关暴露推理或验证瓶颈 $\rightarrow$ 独立外层 [`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md) 将共性控制动作提炼进 `base/`、将领域归约与核验器沉淀进 `plugins/` $\rightarrow$ 下一轮研究直接复用升级后的工作流。** 历经四代演进，`base/` 始终保持 **10 项 MathRSI 核心技能**（9 项解题技能 + 1 项维护技能），领域扩展至 **6 个数学方向、14 项领域技能**。

| 阶段 | 研究经验来源 | Base 工作流核心演进（`base/`） | 领域插件与核验资源变化（`plugins/`） |
| :--- | :--- | :--- | :--- |
| **v0** *(基础工具阶段)* | 使用独立技能开展 **Property B**（超图二染色下界 $m(k)$）与首波 **ECC**（$[43,10,16]$ 及 172 母码双扫描）研究，积累原始 wiki、失败图谱与证明稿；尚无统一 MathRSI 框架 *(非 Git 标签)*。 | 分散的文献、审阅与证明技能，尚无五阶段总控、量词传递契约与原调用点回流机制。 | 单题研究目录与脚本，尚未做 `base / plugin / task` 三层解耦。 |
| **[v1](https://github.com/lisresearchgroup/math-rsi/tree/v1)** | 提炼 [Property B 与初始 ECC 的六条真实研究转折](development/workflow-redesign/REAL_PROJECT_TRANSITIONS.md)。 | 确立 **5 组可执行解题子工作流**、`base / plugin / task` 三层边界、对抗路线迭代与完整证明验收分离、贯穿式 `research-wiki` 记忆回流、按需 Lean 及双端自包含技能包。 | 建成完整 **[Property B 插件](plugins/propertyb/skills/mathrsi-propertyb/SKILL.md)**（4 项技能 + 独立知识库与归档）；形成初版 **ECC** 草案插件。 |
| **[v2](https://github.com/lisresearchgroup/math-rsi/tree/v2)** | 吸收 **Degree–Diameter（DD）** 历史研究经验（43 组参数 153 张图、47 张具体图 Lean 证明）；并合入现有流程修复补丁 PR #7（分派、文件交付与当前恢复）。 | 新增独立外层维护技能 **[`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md)** 及 [4 项共性改进](docs/V2_CHANGES.md)：**①** 公开基线更新自动清理仅服务旧门槛的待派队列，保留固定定理合法性；**②** 变换对象/域/规则后区分正证据继承与旧否证失效范围；**③** 用同一源输入的共同覆盖替代单路充分门；**④** 纯形式目标直通 `lean-formalize` 核查实际导出与公理，不强制先写 TeX。 | 新增 **[Degree–Diameter 插件](plugins/degree-diameter/README.md)**（4 项技能：主入口、图构造、阻塞证书、迁移诊断 + 源 wiki 与归档）。 |
| **[v3](https://github.com/lisresearchgroup/math-rsi/tree/v3)** *(当前推荐)* | 吸收 **Erdős 86**（$Q_d$ 诱导四圈极值）、**Ruskey–Savage $Q_6$**（Hamilton 匹配延拓）、沿用 v1/v2 方法继续深化的第二波 **ECC**，以及 **Happy Ending**（$ES(7)$ signotope 模型）。 | 在 `route-loop`、`prove`、`verify`、`handoff` 内嵌 [4 项证据闭环动作](development/evolution/v3-20261104/base/BASE_CHANGES.md)（见下表），完成 [受影响行为实测](development/evolution/v3-20261104/base/USE.md) 及 Gemini 4 / Opus 5.5 各两轮 [源码维护审阅](development/evolution/v3-20261104/reviews/DISPOSITION.md)。 | 原位升级 **[ECC 插件](plugins/ecc/README.md)**（`mathrsi-ecc` + `ecc-certificate`、实际矩阵与 169 单母码完整重放、两套 Lean 归约工程）；新增 **[超立方体极值](plugins/hypercube-extremal/README.md)**、**[超立方体 Hamilton 延拓](plugins/hypercube-hamilton/README.md)**、**[Happy Ending](plugins/happy-ending/README.md)** 三个领域插件及薄 Python 新候选核验工具（见 [领域路由表](docs/DOMAIN_ROUTING.md)）。 |

### v3 在现有工作流内增强的四类共性动作

v3 的四项 Base 改动均直接写在原技能的输入、动作与返回点上，不另造第二套调度器（详见 [Base 修改报告](development/evolution/v3-20261104/base/BASE_CHANGES.md) · [真实调用用例](development/evolution/v3-20261104/base/USE.md)）：

| 真实研究中暴露的共性瓶颈 | v3 在 Base 工作流中的实际改动 | 所在子工作流 | 经验来源与插件工具衔接 |
| :--- | :--- | :--- | :--- |
| **1. 活动工作集过拟合与历史最优丢失**：候选在局部工作集（working set）表现良好但在全域违规，或后续迭代覆盖了已验证的更优界。 | 严格分列 `restricted`（工作集）、`full`（全域）、`exploration_best` 与 `accepted_best`；将全域违规的具体输入回流给候选生成，替换已接受最优前必须在完整全域重验最终精确对象。 | [`route-loop`](base/skills/mathrsi-route-loop/SKILL.md)、[`verify`](base/skills/mathrsi-verify/SKILL.md)、[`handoff`](base/skills/mathrsi-handoff/SKILL.md) | **Erdős 86** 活动行池全域分离与精确有理数 Gram 核验（[`check_q4_candidate.py`](plugins/hypercube-extremal/tools/check_q4_candidate.py)）。 |
| **2. 归约变换遗失根、目标或必含边**：商对称、补全或缩边改变了局部标号，导致证明完成的局部结论接不回原调用点的指定根或必含匹配边。 | 变换时同步运输根、目标、配对映射与必含边，复合多层映射，并在返回原调用点时显式恢复原始伙伴与必含边。 | [`prove`](base/skills/mathrsi-prove/SKILL.md)、[`verify`](base/skills/mathrsi-verify/SKILL.md) | **Erdős 86** 同步有根 $Q_3$ 旗；**Ruskey–Savage $Q_6$** 保根极大化；**Happy Ending** 最左枢轴径向图转移。 |
| **3. 全称输入族过大与充分门失败池浪费**：剩余全称域无法暴力枚举；子池未过统一充分门时，内部合法对象被整体丢弃。 | 向领域插件请求已证的有限基／秩／覆盖机制承接全称义务；充分门失败池中的合法对象保留并转入逐实例正证书接口。 | [`route-loop`](base/skills/mathrsi-route-loop/SKILL.md)、[`prove`](base/skills/mathrsi-prove/SKILL.md) | **Ruskey–Savage $Q_6$** 1024 短森林 $\mathbb{F}_2$ 满秩桥（[`check_forest_rank.py`](plugins/hypercube-hamilton/tools/check_forest_rank.py)）与缺秩池转局部正证书。*(Happy Ending 固定共同中间匹配与双向净容量补偿与既有共同覆盖/变换机制一致，直接沉淀为领域方法。)* |
| **4. Lean 显式定理参数隐藏外部数学前提**：`#print axioms` 仅显示标准公理，但未形式化的扫描、分类或文献假设写在定理显式参数 `(h : ...)` 中。 | 除 `#print axioms` 外逐项读取定理全部显式参数并展开定义，严格区分内核已证归约／实际矩阵数据与外部文献、分类或扫描前提。 | [`verify`](base/skills/mathrsi-verify/SKILL.md)、[`handoff`](base/skills/mathrsi-handoff/SKILL.md) | **ECC** `ecc43`/`ecc42` Lean 显式前提审计（[`lean-boundary.md`](plugins/ecc/skills/ecc-certificate/references/lean-boundary.md)）与实际生成矩阵验距。 |

<details>
<summary><strong>查看 v2 历史演进结构图</strong>（保留作为 v2 版本快照，图中 ECC 草案与未来 v3 标注反映当时状态）</summary>

![v2历史演进图，其中ECC草案及未来v3标签属于当时快照](figures/mathrsi/01-evolution.png)

详见 [图源与审阅记录](figures/mathrsi/README.md)。
</details>

本仓以详细可执行 Markdown 为主，结合薄 Python 核验脚本检验具体数学对象与新候选，不另造通用调度平台或证明判分器。
```

#### 2. 折叠第 35–37 行的 v2 历史工作流图（替换原 [README.zh-CN.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.zh-CN.md#L35-L37) 第 35–37 行）

```markdown
<details>
<summary><strong>查看 v2 历史五阶段工作流图</strong>（v3 沿用相同五阶段架构，当前六领域分派见 <a href="docs/DOMAIN_ROUTING.md">DOMAIN_ROUTING.md</a>）</summary>

![五组解题子流程内嵌ARIS、贯穿研究wiki、按需Lean，并与独立外层mathrsi-meta-evolve衔接](figures/mathrsi/02-workflows.png)
</details>
```

#### 3. 更新 `### v3领域能力` 表以包含新候选核验工具（替换原 [README.zh-CN.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.zh-CN.md#L73-L83) 第 73–83 行）

```markdown
### v3 领域能力

| 领域入口与技能 | 实际数学能力 | 有界重放与新候选核验工具 |
| :--- | :--- | :--- |
| **[ECC](plugins/ecc/README.md)**：[`mathrsi-ecc`](plugins/ecc/skills/mathrsi-ecc/SKILL.md) ／ [`ecc-certificate`](plugins/ecc/skills/ecc-certificate/SKILL.md) | 在同一插件上完成第二轮升级（不另建 `ecc2`）：二元线性码归约、共同陪集／pair 约束、实际矩阵验距（`[42,16,12]` 实际矩阵 vs. `[42,16,9]` 2020 已发表 $E_3$ 路线；`[45,11,17]` 仍开放）及两套 Lean 工程显式前提审计。 | [172 母码保存集读回、`index=169` 单母码完整重放（`replay_one.py`）与实际矩阵验距](plugins/ecc/evidence/IMPLEMENTATION.md) |
| **[超立方体极值](plugins/hypercube-extremal/README.md)**：[`mathrsi-hypercube-extremal`](plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/SKILL.md) | 共同 $Q_4$ 补全、同步有根旗、活动池全域分离、精确整数 Gram 半正定证书及高维平均桥接。 | [最终 $Q_4$ 全域重放（`verify_final_q4.py`）](plugins/hypercube-extremal/evidence/IMPLEMENTATION.md)、新候选六块矩阵精确求界器 [`check_q4_candidate.py`](plugins/hypercube-extremal/tools/check_q4_candidate.py) 与搜索目录物化器 [`materialize_search.py`](plugins/hypercube-extremal/tools/materialize_search.py) |
| **[超立方体 Hamilton 延拓](plugins/hypercube-hamilton/README.md)**：[`mathrsi-hypercube-hamilton`](plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/SKILL.md) | 保根极大化、$\mathbb{F}_2$ 全称短森林满秩桥、缺秩子池转局部正证书及带标粘合。 | [A10 1024 森林全部矩阵位与独立 GF(2) 秩重放](plugins/hypercube-hamilton/evidence/IMPLEMENTATION.md)，以及支持新几何输入的 [`check_forest_rank.py`](plugins/hypercube-hamilton/tools/check_forest_rank.py) |
| **[Happy Ending](plugins/happy-ending/README.md)**：[`mathrsi-happy-ending`](plugins/happy-ending/skills/mathrsi-happy-ending/SKILL.md) ／ [`happy-ending-certificate`](plugins/happy-ending/skills/happy-ending-certificate/SKILL.md) | 杯帽与 rank-3 signotope 模型、weak/split $k$-gon 与抽象/几何可实现性区分、先固定单一共同 $R_5$ 匹配再做双向低前驱补偿，以及有界见证核验。 | 纯标准库下界 25 核验器 [`check_lower25.py`](plugins/happy-ending/tools/check_lower25.py)（[结果](plugins/happy-ending/evidence/lower25-independent.json)）；历史 55 格 SAT 进口与未终审结构稿保持各自边界，新聊天截图报告的 75/76 待证明原件。 |

六领域（共 **14 项领域技能**）共用现有五阶段，具体阶段分派与返回契约见 **[docs/DOMAIN_ROUTING.md](docs/DOMAIN_ROUTING.md)**。
```

---

### 三、给 Root 合入与打 Tag 时的 3 条具体编辑建议

1. **用“研究瓶颈 $\rightarrow$ Base 动作 $\rightarrow$ 所在阶段 $\rightarrow$ 来源案例与薄工具”四列结构让读者一眼看懂自演进机制**：
   * 相比单纯罗列版本号，上面第二张表把每一条抽象原则都绑到了**具体踩坑场景**（如工作集过拟合、商变换丢根、全称域爆炸、Lean `(h : ...)` 隐藏前提）和**具体可执行脚本**（`check_q4_candidate.py`、`check_forest_rank.py`、`lean-boundary.md`），读者无需翻阅深层维护记录就能立刻看懂“研究经验是如何变成下一轮可调用能力的”。
2. **将两张 v2 历史大图收进 `<details>` 折叠块，消除首屏图文版本冲突**：
   * 原 `01-evolution.png` 含“ECC 草案”和“未来 v3”字样，原首屏直接展开容易让读者误以为当前仓库仍处于 v2。放进 `<details>` 并让 `v0 → v3` 演进表直接顶上首屏，既保留了 v2 历史图档和链接完整性（`tools/check_links.py` 零改动通过），又让主视觉完全聚焦在 v3 正式版。
3. **打 `v3` 标签前顺手同步 3 处残余的“尚未 tag/push”单句**：
   * 除上述两份 README 顶部已更新为发布态外，合入前只需同步三处单句即可保持全仓口径一致：
     * [README.md](file:///Users/rfy_naiveai/Desktop/MathRSI/README.md#L194) 第 194 行：`The local v3 implementation retains...` $\rightarrow$ `The v3 release retains...`
     * [V3_CHANGES.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/V3_CHANGES.md#L3) 第 3 行与第 98 行：删去 `The current work is on a local development branch; v3 has not been tagged or pushed.` 及末尾 `This branch is still a local implementation, not a published v3 tag.`（改为 `The fixed v1, v2, and v3 tags preserve complete snapshots; main tracks v3.`）。

