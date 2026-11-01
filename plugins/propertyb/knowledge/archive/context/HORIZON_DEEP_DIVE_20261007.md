# Archon-Horizon 数学与 Lean 执行能力深读

2026-10-07。只读源码核查及小规模搜索测试；没有安装 Horizon 平台、启动服务、调用外部模型、修改全局配置或本项目数学工程。

**结论：本地 ARIS 草案已经覆盖 Horizon 最重要的命题对齐与证明闭合原则。现在值得补充的是 Lean 工作时的具体操作：分层搜索、真实调用试编、按错误机制修复、表示方案的最小实验，以及区分等待、导入和证明展开的性能诊断。Horizon 确有运行代码，不只是提示词；但这些代码主要落实构建、索引与 Lean 接口审计，没有自动解决纸面数学到 Lean 的语义一致性。**

## 1. 实际版本与阅读范围

本轮在 `ref/software/Archon-Horizon/` 浅克隆，实际 HEAD 为：

```text
0df5571f81aae29130c8ec621c9fe7419ca28d6a
2026-10-06T14:54:37+08:00
Pipeline redesign: replace the legacy Horizon runtime (#13)
```

这与旧 [ARCHON_HORIZON_ASSESSMENT.md](ARCHON_HORIZON_ASSESSMENT.md) 的 API 核查提交相同。当前源码是 **0.2.0 alpha**，PostgreSQL 控制平面、`/api/v3` 和 `/pipeline`；网页缓存中 0.1.x、`workspace/config.yaml`、`horizon check` 等例子不作为本轮当前接口证据。[当前 README](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/README.md#L1-L31)

阅读范围：

| 范围 | 本轮实际工作 |
|---|---|
| 本地基线 | 读取项目 `AGENTS.md`、旧 Horizon 评估；完整读取本轮开始时 `lean-formalize/SKILL.md`、`adversarial-review.md`、`verification-and-handoff.md`。以下对照指这份 641 行的初始草案，不预先把主代理随后修订计入已有能力。 |
| 数学与 Lean 技能 | 读取 12 个 `skills/lean/*/SKILL.md`：formalization、cycle、check、search、proof-repair、tactics、counterexample、library-engineering、refactor、performance、simplifier、proof-golf；深入其搜索、诊断、策略、表示实验、重构、性能、重写规范等相关参考。 |
| 语义与证明审阅 | 读取 statement-alignment、semantic-probes、proof-review、trust-and-closure、definition-quality、representation-experiments；读取 mathematical-fidelity、decomposition、graph-planner、lean-worker、debug、build-checker 描述。 |
| 协作与文献 | 读取 horizon-pipeline、horizon-delegation、source-research；核对 graph contracts、milestones 中的接口与证据约定。 |
| 执行代码 | 逐段核对 `worker/lean_build.py`、`build_engine.py` 的构建路径，`milestone_verify.py` 的审计和 Comparator 路径；查看 `milestones.py` 的状态接受条件、`worker/provider.py` 的 CLI 适配、`daemon.py` 的 scratch/环境注入位置。 |
| 搜索代码 | 读取 `search/index.py` 的抽取、名称/类型/文本检索实现，`search/workspace.py` 和 `search/mcp_server.py`；查看 pipeline 搜索的固定仓库版本和后台索引入口。没有审计搜索服务全部安全与缓存分支。 |
| 测试 | 读取相关搜索、Lean 构建和里程碑测试；实际执行 8 个无需新增依赖的上游搜索测试，及本地固定 Mathlib 单文件检索。没有执行 Horizon 全套测试、PostgreSQL 测试、真实 managed build 或 Comparator。 |

当前源码树没有作为数学库交付的 `.lean` 文件；Python 测试和审计器中有生成 Lean 源码的字符串。不能将“无独立 `.lean` 文件”推断成“没有实际 Lean 工具支持”。README 声称用于 Poincaré 项目协调，本轮未复核该项目的数学完成范围；这不是 Horizon 数学能力的性能或正确性测评。

## 2. 它怎样组织数学求解

### 2.1 数学拆解并非单纯加任务节点

`graph-planner` 要求说明子结果如何在真实假设下推出目标，区分缺失的 producer、缺失推理与已存在结果；不允许给未知结论换一个 certificate 名称就算拆解。当路线不确定时先做能决定路线的最小实验。`decomposition` 进一步要求检查接口是否能组合、循环依赖、不同表示及共享接口所有权。它明确反对按固定数量制造里程碑。[graph-planner:9–35](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/subagents/planning/graph-planner.md#L9-L35)、[decomposition:21–60](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/subagents/reviewers/decomposition.md#L21-L60)

这些是数学工作指导，不是自动产生有效分解的算法。运行时可以强制任务归属、节点无环、阶段审阅和证据状态，却不能从一条 graph edge 判定数学蕴含成立。本地草案中“任意原输入 → 实际 producer → 条件接口 → 最终消费者”已经吸收这项核心。

### 2.2 证明循环的终点是新信息

`lean-cycle` 的一个循环须产生已检查代码、缩小的障碍、被否定的路线或具体依赖。相同原因反复失败后，应区分缺引理、表示不匹配、命题为假、缺 producer、资源不足；不靠反复更换 tactic 字符串推进。它没有强制每隔固定分钟评审或固定次数重试。[lean-cycle:11–47](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-cycle/SKILL.md#L11-L47)

这是 ARIS 当前简要 implementation loop 可具体化的地方：每次失败保存一条“实际 goal/context、第一条因果错误、尝试的假说、结果、下一分支”。复用已有 continuation note 即可，无需专门的 attempt 数据库。

### 2.3 文献与数学推导的边界

`source-research` 要求检查原始论文/书籍/TeX 的精确版本、定理位置与周围定义；公式关键处看 PDF 渲染而非只信 OCR。其作用是恢复真实假设与对象，不能把引用或综述当成所需蕴含的证明。`lean-tactics` 则把量词、见证拆解与数学内容分开：先提供所需中间事实，再选符合领域的自动化。[source-research:21–45](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/operations/source-research/SKILL.md#L21-L45)、[lean-tactics:11–33](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-tactics/SKILL.md#L11-L33)

没有发现专门的符号数学推导引擎或自动判断新引理真假的实现；数学发现仍由执行模型、已有库和 Lean 反馈完成。

## 3. 具体 Lean 实践中值得借用的部分

### 3.1 搜索须以实际 goal 为起点

Horizon 的顺序是：附近项目声明 → 已安装且固定版本的依赖 → 更强/等价表述或标准抽象 → 检查完整类型与 import → 在当前 goal 中应用。名称搜索没有结果时看相邻文件和 use sites，不能据空索引宣称 Mathlib 没有该概念。探索可用 `exact?`、`apply?`、`rw?`、`simp?`，但应在当前版本确认可用，并保留清楚的稳定结果。[lean-search:14–33,47–54](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-search/SKILL.md#L14-L54)、[search-routes:15–40](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-search/references/search-routes.md#L15-L40)

本地草案已说“搜索固定库，用 `#check`”，可增加短参考说明名称、类型形状、概念与抽象分别怎么查。无需装上 Horizon 搜索器才能遵循该方法。

### 3.2 大改表示前，先证明一个真实消费者

`definition-quality` 用实际构造与消费者评价 bundling、definitional equality、强制转换、实例选择与 API。`representation-experiments` 比较原表示和候选表示的构造、操作、化简与一个下游定理；如果一条 bridge lemma 足够，就避免整体重写。`lean-refactor` 要求先完成真实输入到公共结果的最小一段，再传播新 API。[definition-quality:10–47](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/definition-quality/SKILL.md#L10-L47)、[representation-experiments:47–57](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/definition-quality/references/representation-experiments.md#L47-L57)、[extraction-and-migration:38–55](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-refactor/references/extraction-and-migration.md#L38-L55)

对 ARIS 有实际价值的增量是把“代表性 consumer”写成一个可编译临时 `example`，暴露隐式参数、coercion、实例和额外前提；不是再做一个只证明 `Certificate → Desired` 的孤立接口。临时代码放 scratch，不进入正式定理依赖。

### 3.3 错误修复按机制分流

具体诊断表区分 unknown identifier、application mismatch、typeclass synthesis、rewrite mismatch、simp 后缺数学事实、heartbeats、仅在消费者失败。修第一条因果错误；类型不匹配读完整 `@declaration`，重写失败看实际 elaborated expression，实例失败看相同 carrier 上究竟选了哪个 structure。修改后若同一障碍没有新信息，就缩小例子或改论证。[lean-proof-repair:21–42](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-proof-repair/SKILL.md#L21-L42)、[diagnostics:5–38](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-proof-repair/references/diagnostics.md#L5-L38)

尤其值得补充：改 imported module 后先构建它，再依赖 `lake env lean Scratch.lean` 的结果。后者读取已有 imports，不保证重新编译修改过的依赖。Horizon 当前说明明确区分这两种检查。[lean-check:20–33](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-check/SKILL.md#L20-L33)

### 3.4 目标形状决定 tactic，化简后重新看目标

策略参考将 `rfl/change`、`ext`、`ring`、带非零前提的 `field_simp`、`omega`、`linarith/nlinarith`、monotonicity 等放在各自适用的目标形状下。对 finite sums/cardinality 先查 Finset API，避免重新展开 insert/erase 归纳。执行 `simp` 后 `calc` 应从新显示的表达式开始，不能对旧草稿继续硬改写。[strategy-patterns:5–53](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-tactics/references/strategy-patterns.md#L5-L53)

`lean-simplifier` 的重点是局部 `rw`/`simp only` 与全局 `@[simp]` 的区别；一个局部失败不能自动证明需要扩大全局规则集。给 `lean-formalize` 增加简短诊断分支足够，不建议复制完整 tactic 百科。[lean-simplifier:11–31](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-simplifier/SKILL.md#L11-L31)

### 3.5 反例和性能有不同的证据要求

反例调查区分候选 witness、带未验证形式步骤的 witness、Lean 检查的否定；认证否定要独立检查全部前提和自身公理链，避免借用已 admitted 的原目标推出矛盾。ARIS 已覆盖候选反例核实，可补上“独立命名 scratch 反例与否定公理检查”的短提示。[lean-counterexample:11–38](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-counterexample/SKILL.md#L11-L38)

性能上先区分等待构建槽、依赖下载、导入、elaboration、kernel checking 与 native compilation。仅局部启用当前 Lean 支持的 profiler/trace；placeholder 只用于隔离 signature 和 proof-body 成本，不成为证明证据。先找实例循环、表达式推断或过大的 simp 输入，才考虑局部资源上限。[profiling-and-repair:3–20,39–49](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-performance/references/profiling-and-repair.md#L3-L49)

## 4. 搜索工具的真实实现与零安装测试

### 4.1 当前没有旧 `horizon search` 根命令

当前 `horizon`、`horizon-pipeline` 都进入 pipeline CLI。其 parser 定义没有 `search`、`check`、`attempt save` 或 `tmp clean` 子命令。CHANGELOG 中出现这些字符串是历史能力记录，不能直接当作 0.2.0 使用指南。[cli.py:20–107](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/cli.py#L20-L107)

仍存在两条搜索实现：

- `archon_horizon.search`：本地源码声明抽取、name/type/text/header 模式，独立 stdio MCP 暴露 `lean_search`。本地发现会遍历 checkout、嵌套 Lake 项目、已取回 `.lake/packages` 与路径依赖。[mcp_server.py:20–73](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/search/mcp_server.py#L20-L73)、[workspace.py:21–81](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/search/workspace.py#L21-L81)
- pipeline 搜索管理器：对授权仓库的明确 commit 准备后台索引，返回固定来源；这是跨项目服务能力，本轮没有启动。[pipeline/search.py:1–45](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/search.py#L1-L45)

抽取器明确是 heuristic，不运行 Lean parser/elaborator；名称搜索是字符串排名；`search_type` 将签名模式变成有界正则，不进行 Lean 的类型合一或定义等价判断。文本/模块标题模式用 BM25，不是证明相关性保证。[index.py:123–193](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/search/index.py#L123-L193)、[index.py:468–528](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/search/index.py#L468-L528)

例如本次 `card_sdiff` 返回的源码签名中 `s,t` 未作为本行 binders 出现，它们来自周围 section；这正说明搜索命中还不是完整 elaborated type。须用 `#check @Finset.card_sdiff` 或实际 use site 确认参数。

### 4.2 实际执行

未新增 Python 包。现有 Python 3.14.6 提供 pytest 与 numpy，缺 bm25s/scipy；因此只执行不依赖 BM25 的抽取、name/type 模式。

对本项目已固定的 Mathlib 提交 `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`，单文件 `Mathlib/Data/Finset/Card.lean` 抽取 135 个声明：

| 查询 | 实际命中 |
|---|---|
| `search_name('card_union_le')` | `Finset.card_union_le`，547 行 |
| `search_name('card_sdiff')` | `Finset.card_sdiff`，560 行；还有两条相关结果 |
| `search_type('Disjoint ?a ?b')` | `Finset.card_union_eq_card_add_card`，549 行 |

原始结果见 [search-smoke.json](horizon-deep-dive-20261007/search-smoke.json)。该结果是搜索执行证据，不是本次重新形式验证了这些定理或其调用。真实 caller 试编由本轮主代理另行执行。

从本项目根目录可复用如下零安装方式；路径只对本次 checkout 有效，不建议硬编码进通用 ARIS skill：

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=ref/software/Archon-Horizon/src python3 - <<'PY'
from pathlib import Path
from archon_horizon.search.index import LeanSearchIndex, extract_declarations
p = Path('formal/.lake/packages/mathlib/Mathlib/Data/Finset/Card.lean')
index = LeanSearchIndex(extract_declarations(
    p.read_text(), library='mathlib', file=str(p)))
for hit in index.search_name('card_union_le'):
    print(hit.declaration.name, hit.declaration.signature, hit.declaration.line)
for hit in index.search_type('Disjoint ?a ?b'):
    print(hit.declaration.name, hit.declaration.signature, hit.declaration.line)
PY
```

另外实际执行上游 8 项测试：具名参数赋值中的 `:=`、跨行签名、namespace/doc 抽取、名称 exact/近似区分、类型通配符、空模式和长签名界限，全部通过，pytest 输出 `8 passed in 0.05s`。[测试记录](horizon-deep-dive-20261007/search-tests.txt)、[对应上游测试](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/tests/test_search.py#L43-L147)

## 5. Lean runtime：实现了什么

### 5.1 真正运行编译器的 managed helper

当前命令是 `horizon-lean-check Module.Name`，或 `python -m archon_horizon.pipeline.worker.lean_build Module.Name`；`--lean Relative/File.lean` 走单文件检查，`--probe` 检查 Lake target 当前是否无需构建即已就绪。需要宿主配置 `HORIZON_LEAN_BUILD`；普通本地 ARIS 项目仍用已有 `lake build`/`lake env lean`。[lean_build.py:168–189](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/lean_build.py#L168-L189)

`build_engine.run_check` 实际执行 `lake build …` 或 `lake env lean …`，对 checkout/path dependencies 加锁，分配宿主编译槽；新鲜 targets 的 `lake --no-build build` 检查成功时不占编译槽。依赖缺失时按 manifest 精确 commit 准备 Git checkout，保留既有依赖目录与修改，不调用 `lake update`。[build_engine.py:112–124](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/build_engine.py#L112-L124)、[206–271](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/build_engine.py#L206-L271)、[489–586](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/build_engine.py#L489-L586)

JSON 区分 passed、failed、deferred、timed_out、cancelled，分别保留状态、命令、目标、诊断与 wait/prepare/build 时间。75 表示暂缓、124 超时、130 取消；不会把繁忙自动说成数学错误。检查前后源码身份不同会将原本成功的构建降为 deferred；`snapshot_verified=false` 不能说明验证了一个稳定的完整快照。[lean_build.py:68–95,138–164](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/lean_build.py#L68-L164)

这些对共享机器、多 worktree、大 Mathlib 缓存有明确用途。ARIS 单项目当前没有必要为这种能力迁移平台或引入源码哈希系统；可以直接借用准确区分失败原因、限制无信息重试、按目标编译等执行原则。

### 5.2 scratch 与 attempt 的当前含义

worker 为每个 execution 建独立 scratch 目录，向模型进程设置 `TMPDIR/TMP/TEMP`；这是真实工作目录隔离支持。失败路线的数学总结与临时代码保存仍靠 agent 的技能流程，当前没有旧 `horizon attempt save` 那套 CLI。运行时的 attempt/journal 主要指 provider 执行、API intent、Git checkpoint 和重连恢复，不能混称自动保存/选择数学证明策略。[daemon.py:755–758](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/daemon.py#L755-L758)、[daemon.py:896–907](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/daemon.py#L896-L907)

### 5.3 LSP 与 provider 的边界

技能倡导“有 LSP 就用 diagnostics/goal inspection”，同时保留 `rg` + elaborator 的 fallback。代码中有离线 `lean_search` MCP server，并不等于 provider 自动装好了 lean-lsp。当前 Claude adapter 明确传空 `mcpServers` 与 strict MCP 配置；Codex adapter 使用 CLI，并没有在该 command builder 里安装或注入 Lean LSP。本轮未验证宿主预配置能力。[provider.py:144–182](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/provider.py#L144-L182)

所以应描述为“可使用宿主已有 LSP；框架另有搜索实现”，不能宣称“当前开箱即有所有 LeanSearch/Loogle/LSP 工具”。

## 6. 语义审阅、自动审计与 Comparator 必须分开

| 层次 | 当前实现 | 保证范围 |
|---|---|---|
| statement-alignment / mathematical-fidelity | Markdown 指导；`reviewer_guidance.py` 读取 descriptor、合并 review contract | 要求模型回译、比较量词、读定义和找反例；没有确定性程序自动证明 prose↔Lean 等价 |
| proof-review | Markdown 指导模型执行 `#print axioms`、追输入与消费者 | 指导本身不执行所有检查；实际结果以执行日志和真实范围为准 |
| managed Lean check | 真正 subprocess 调 Lake/Lean、处理资源/源码范围 | 证明该输入下指定命令的执行结果；编译允许 `sorry`，也不认证纸面含义 |
| milestone audit | 生成 Lean `run_cmd`，调用 `collectAxioms`，读取声明类别/模块与直接 admission | 对配置的 targets、类型依赖、Definitions 模块作真实结构化审计 |
| Comparator proof route | 构建并调用项目提供的 Comparator 与 lean4export，再审计 solution | 条件满足时比较 challenge 与 solution 的 Lean 接口；仍须另外判定 challenge 是否忠于原数学 |

审阅指导装配的源码很短，没有隐藏的数学判定器。[reviewer_guidance.py:18–29](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/reviewer_guidance.py#L18-L29) 高风险盲回译是 statement-alignment 的流程要求，不能因为引用了该 skill 就称它已经执行。[statement-alignment:21–45](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/statement-alignment/SKILL.md#L21-L45)

### 6.1 `milestone_verify.py` 的具体机器检查

它不是仅解析 grep 结果。生成的 Lean 审计代码：

1. 取得指定 target 的 `ConstantInfo`，要求其为 theorem；读取所属模块。
2. 对 target 本身运行 `collectAxioms`，并扫描直接 proof term 是否出现 `sorryAx`。
3. 对 target **类型中使用的常量**再收集公理。
4. 遍历指定 Definitions 模块中的声明，收集其公理。
5. 检查 Definitions 的 imports 不得包含 milestone contract 模块。
6. 输出唯一一份结构化 JSON，由 Python 验证目标覆盖、公理及模块匹配。

源码：[生成的 Lean AUDIT:17–54](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/milestone_verify.py#L17-L54)、[audit:88–121](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/milestone_verify.py#L88-L121)、[调用范围:164–176](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/milestone_verify.py#L164-L176)

它采用本框架里程碑的固定基础 `{propext, Classical.choice, Quot.sound}`；定义与类型不得含额外公理，尚未完成的 theorem body 可以包含 `sorryAx`。这支持先审阅完整可编译接口、再分别证明，而不会把 admitted definition 装成具体对象。

**不应照搬两个专属政策到通用 ARIS：**要求声明必须是 theorem 是 Horizon contract 约定，不表示 `def p : P := ...` 不能提供 P 的证明；固定公理白名单也不是所有任务通用。ARIS 当前按 actual type 与任务 trust basis 判断更合适。

测试中确有真实 Lean skeleton/admitted-definition 案例：用 `shutil.which('lake')` 条件跳过，生成一个小项目，检查合法 skeleton 和隐藏 admitted definition 被拒。它固定示例 toolchain 为 4.33.1。本轮只读该测试，没有运行或安装该版本，不能报告其在本机通过。[test_pipeline_milestones.py:35–50](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/tests/test_pipeline_milestones.py#L35-L50)、[374–416](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/tests/test_pipeline_milestones.py#L374-L416)

### 6.2 Comparator 的调用前提与信任边界

进入 proof route 需提供单独 `solution_root` 与 Comparator 配置。实现核对：

- roadmap 与 solution 都是干净的已提交 checkout。
- 配置的 theorem names 覆盖所有 milestone/endpoint targets，definition names 覆盖已审阅 Definitions 声明。
- solution 中 challenge 源码与审阅的 `milestones/*.lean`、toolchain 完全相同；原 roadmap 的依赖记录在 solution 中保持一致。
- challenge module 与 solution module 不同；先审计 challenge 实际露出的定义和声明所属模块。
- 构建 `@Comparator/comparator`、`@lean4export/lean4export`，执行项目中的 comparator binary 并检查 exit code；之后再审计 solution target 的公理。
- 最后确认工作目录与提交未改变。

源码：[milestone_verify.py:186–234](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/milestone_verify.py#L186-L234)。项目必须自己配置固定 Comparator/lean4export 包与运行依赖；Horizon 此仓库不包含被调用的 Comparator 内核实现。[pipeline-milestones.md:69–76](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/docs/pipeline-milestones.md#L69-L76)

因此，本轮能够确认“调用链与前置检查已经实现”，不能据此声称“外部 Comparator 在本机执行通过”或“完整审计过其比较语义与工具可信性”。也不能从两份 Lean 声明比较通过推出纸面数学无误：若最初 challenge 就是 `(h : P) → P`，接口比较不会替它补上 P 的 producer。

`comparator_passed=true` 也不单独代表完整证明。receipt 保留直接/传递 admission；服务器对 completion claim 再检查对应 targets，直接 hole 不可报完成，无直接 hole 但传递依赖 `sorryAx` 时归为 conditional。[milestones.py:95–115](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/milestones.py#L95-L115)

## 7. 与 ARIS 初始草案的逐项对照

| Horizon 经验 | ARIS 初始草案状态 | 本轮建议 |
|---|---|---|
| 原命题、真实 definitions、盲回译、量词对照 | A 与 adversarial-review 已详细覆盖 | 保持，不增加第四套审阅 |
| producer→接口→consumer、原始输入到最终定理 | 第2节、B/C已覆盖且更贴合本项目经验 | 保持，不复制 milestone/graph 元数据格式 |
| 正常公理不等于正确数学命题 | 第5节与verification参考已覆盖 | 保持 |
| fresh context 与 review范围/失败事实 | A/B/C与续接协议已覆盖 | 保持；Horizon persona 数量不构成额外独立性 |
| 固定库搜索与候选API检查 | 有简短 `#check` 要求，缺具体分流 | 补名称/签名/概念/等价表述检索及真实调用例子 |
| scratch中验证候选表示/真实consumer | 已要求actual use site，尚未具体讲表示实验 | 补一个最小 constructor/consumer 试编后再做迁移 |
| 因果错误、实例、rewrite、缓存等诊断分流 | 有第一错误与缺数学前提区分，操作颗粒度较粗 | 补短诊断表及停止无信息tactic重试的动作 |
| goal-directed tactics、当前simp normal form | 基本未展开 | 补少量典型路线，按需读，不建立完整策略表库 |
| 编译超时的成本分解 | 主要覆盖有限计算变贵与信任边界 | 补等待/依赖/导入/展开区分和局部测量 |
| 反例保持原目标、核实全部前提 | B已有明确要求 | 可补否定自身公理链，不强制每个候选都写Lean |
| 智能构建槽、缓存、公平排队 | 无平台实现，也无当前实际需要 | 仅多项目/共享宿主负载出现再考虑 |
| 固定challenge/solution的自动接口比较 | 本地独立import/原命题wrapper，没有Comparator | 当前不安装；大型多人改动公共契约时再评估 |
| PostgreSQL、missions、Forge/Zulip、durable assignments | 当前不需要 | 不引入；保留现有ledger与本机代理工具 |

ARIS 的 A/B/C 跨家族审阅是本地任务约定；Horizon 描述文件中多个 reviewer 角色不自动保证跨家族模型。这项现有约束应保留。

## 8. 可以直接写入轻量参考的五项操作

1. **按问题搜索，再验证实际应用。** 用 `rg -n` 限定 pinned Mathlib 目录，读邻近声明和 caller；`#check @Candidate` 后在 scratch `example` 中使用它。来源：上文 lean-search/search-routes。`horizon search` 不作为当前命令推荐。
2. **固定数学接口，试一个真实 consumer。** 在昂贵编码/表示重构前，以实际原输入写一个小调用；检查额外前提由谁证明。来源：representation-experiments:47–57、extraction-and-migration:38–55。
3. **修第一条因果错误，每次只验证一个解释。** 保存 goal/context，区分 API、实例、重写、缺数学事实、资源问题；障碍重复无新信息则缩小例子/换路线。来源：lean-proof-repair:21–37 与 diagnostics 表。
4. **检查层级与依赖新鲜度匹配。** 编辑期用可用 LSP 或 `lake env lean Scratch.lean`；修改 imported module 后先 `lake build Changed.Module`；集成后构建真实下游主模块。来源：lean-check:14–33、lean-proof-repair:15–19。
5. **有测得热点才做性能修复。** 区分等待、下载、导入与 elaboration；先用类型明确的 `have`、精简 tactic 输入、复用现成 lemma，再决定局部 profiling/资源上限。来源：profiling-and-repair:3–49。

这些操作应进入按需读取的一份短参考，由当前 implementation loop 链接。主技能继续围绕命题、连接、执行、核验与交付，不扩大为 Horizon 安装指南。

## 9. 文档和实现的差距与适用场景

本轮发现的差距主要是版本与证据层级，而不是一个已证实的数学错误：

- **历史 CLI 与当前 CLI 不同。** 旧 check/search/attempt 的例子不能照搬；新 managed check 与搜索 Python/MCP 是各自入口。
- **LSP 是可用时使用的工具。** skill 文字不能替代 adapter 的实际工具配置。
- **语义审阅是模型程序，结构/公理审计有确定性实现。** 两者均有价值，保证不同，不能统称自动数学 fidelity gate。
- **有工具和有测试，不等于本轮运行过。** 8 个搜索测试与一次真实库搜索已经执行；build/Comparator/数据库路径仅源码核查。`architecture.md` 自己也区分运行时测试和数学判断、完工时限保证。[architecture:164–173](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/docs/architecture.md#L164-L173)

对当前已完成证明及通用 ARIS 草案，增加一份具体 Lean 工作参考就能取得主要收益。Horizon 整体平台适用于长期并行的多个项目、不同 worker 机器、需要持久任务所有权与 Forge 发布的一致运行环境；只有出现这些真实需求才值得承担部署与迁移成本。

本次借鉴对象也有上游来源：Horizon 明确记录其若干 Lean 技能改编自 `cameronfreer/lean4-skills` 固定提交 `4400419ba345fd0dc07f278359b372505780ef71`，是经过编辑的部分指导，不是安装完整上游插件。[PROVENANCE.md](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/_sources/lean4-skills/PROVENANCE.md#L1-L42) 应记录参考来源；无需为了吸收几个操作原则增加上游 hook、调度框架或下载链。
