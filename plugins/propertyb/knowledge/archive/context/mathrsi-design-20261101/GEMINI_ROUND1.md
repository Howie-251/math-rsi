# `mathrsi-base` + `mathrsi-propertyB` 架构审阅与设计建议（致 ARIS 作者）

> **实际核查文件清单（只读审阅，未执行程序或修改文件）：**
> 1. 设计底稿与证据札记：[BRIEF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-design-20261101/BRIEF.md)、[EVIDENCE_NOTES.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-design-20261101/EVIDENCE_NOTES.md)
> 2. 项目方法与失败图谱：[PROPERTY_B_RESEARCH_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md)、[PROPERTY_B_FAILURE_ATLAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md)
> 3. 小参数完整证明沉淀：[PROPERTY_B_M6_GE67.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_M6_GE67.md)、[PROPERTY_B_M8_M9_INCREMENT_20261029.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_M8_M9_INCREMENT_20261029.md)
> 4. 形式化与外部框架吸收：[ARIS_LEAN_WORKFLOW.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/ARIS_LEAN_WORKFLOW.md)、[MATH_AGENT_HARNESS_SYNTHESIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/MATH_AGENT_HARNESS_SYNTHESIS.md)

Root 提出的“三层切分 + 内外循环解耦 + 轻量 Markdown/JSON 接口”总体方向扎实，尤其将完成标准锚定在**“原始输入到原始结论的真实调用链（actual caller）”**上，切中了数学 Agent 最常见的“条件引理编译通过但原题悬空”痛点。但若要让该架构真正阻断局部组合搜索黑洞，Root 初稿在**瓶颈语义接口、停滞熔断判据、局部退回全局机制**三处仍显过宽。以下按底稿六个核心问题给出批判性审阅与可执行设计方案。

---

### 一、 三层职责边界、易错切分与最小信息交换实例（答问题 1）

#### 1. 职责归属
* **`mathrsi-base`（通用数学工作流内核）**：负责原命题与量词固定、未闭义务有向图（`RemainingGoal`）维护、证据等级划分（纸面推导 / 独立精确复算 / 跨家族对抗审阅 / 按需 Lean 内核核验）、失败层次归因（引理被反例证伪 vs. 松弛界不足 vs. 表示/编译资源瓶颈）、`原对象 → 局部数据 → 原结论` 桥接完整性检查，以及重计算/重构建的并发资源调度（[ARIS_LEAN_WORKFLOW.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/ARIS_LEAN_WORKFLOW.md#L7-L20)、[MATH_AGENT_HARNESS_SYNTHESIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/MATH_AGENT_HARNESS_SYNTHESIS.md#L30-L41)）。
* **`mathrsi-propertyB`（领域插件）**：封装最小顶点反例与点对覆盖归约、整数度数与共度超额预算 $\epsilon_x = (k-1)d(x)-(v-1)$、选锁定理（如 $m(8)/m(9)$ 嵌套最低度单位池）、迹恢复、排列概率引擎 $U=\sum_k \min\{A_k,B_k,C_k-D_k\}$、相交图组件配额与有限 LP 对偶乘子，以及独立下降阶乘复算器（[PROPERTY_B_RESEARCH_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md#L23-L31)、[PROPERTY_B_M8_M9_INCREMENT_20261029.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_M8_M9_INCREMENT_20261029.md#L24-L59)）。
* **单题工作区（Task Workspace）**：存放冻结的本题参数（如 $k=6, M=66, v\in[27,44]$）、任务级策略与信任基础（如是否要求 Lean、是否禁用整图枚举、指定 Grok+Gemini 审阅）、各分支已扫域/余域台账、有理数证书与失败见证。

#### 2. 三个最容易切错的边界（对 Root 初稿的挑战）
1. **不能把“项目偏好”当成 `base` 铁律**：禁止整图穷举、特定双模型审阅、只允许三个标准公理而不允许 `native_decide`，均属**单题工作区策略**或**验证器配置**（[ARIS_LEAN_WORKFLOW.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/ARIS_LEAN_WORKFLOW.md#L58-L63)）。若固化进 `base`，碰到拉姆齐数小参数或编码理论有限域穷举任务就会自缚手脚。
2. **不能因为“base 不懂领域数学”就让插件只报标量总分**：Root 认为 `base` 无法理解所有数学语义，但若插件只向 `base` 返回 `U = 4212/4199 > 1`，`base` 就无法拦截“在非活跃项上空转优化”的低效行为。**正确切法是：`base` 定义通用的“活跃瓶颈与松弛量（Active Bottleneck & Slack）结构契约”，由插件负责填值。**
3. **跨参数复用不等于跨领域通用**：链接组件配额、非负有理数对偶删除在 $k=5\dots 12$ 通用，但仍属超图插件资产；而**“用浮点 LP 找候选乘子、用精确有理数不等式做验收证书”**（[PROPERTY_B_RESEARCH_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md#L81-L90)）才是应沉淀进 `base` 的通用神经符号验证范式。

#### 3. 最小可执行信息交换示例（JSON 契约）
以 T33 中 $v=20$、双锁 $(7,9)$ 的真实无效扣除教训（[PROPERTY_B_FAILURE_ATLAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L53-L66)）为例：

```json
{
  "obligation_id": "T33_v20_lock7_9",
  "caller_bridge": "SimpleHypergraph5(M<=33) -> MinVertexCounterexample(v=20) -> UnitLockPair(7,9) -> PropertyB",
  "action_proposal": {
    "fixed_assumptions": ["v=20", "M=33", "unit_co_degree_locks=(7,9)"],
    "input_domain": "all_labeled_positions (380 pairs)",
    "already_scanned": "380/380 exact rational evaluation",
    "target_bottleneck": "reduce sum_k min(A_k, B_k, C_k - D_k) below 1",
    "stop_condition": "1 round; abort if active min-term is unchanged"
  },
  "action_result": {
    "coverage": "EXHAUSTIVE_ON_DECLARED_DOMAIN",
    "bottleneck_audit": {
      "position_12": {"min_AB": "28/153", "C_raw": "45/221", "D_deducted": "10/221", "active_term": "B_k", "effective_drop": "0"}
    },
    "verdict": "NO_BOTTLENECK_SHIFT",
    "base_routing": "FREEZE_POSITION_SEARCH -> ESCALATE_TO_SUBFAMILY_QUOTA_OR_STRUCTURE"
  }
}
```

---

### 二、 核心固定与 RSI 演进如何兼容？（答问题 2）

**插件在单题运行期内不改 `base`，不仅不妨碍 RSI，反而是防止“自我奖励作弊（Reward Hacking）”的必要前提。** 若允许解题代理在攻关受阻时直接修改 `base` 的验收门槛或完成定义，系统极易把 `Target` 偷偷退化为 `Certificate H → Target`，或把“16 个 pilot 通过”记为“1993 个完整布局通过”（[PROPERTY_B_RESEARCH_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md#L120-L122)、[L150-L152](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md#L150-L152)）。

兼顾可解释性与核心演进的正确机制是**“双时间尺度分层 RSI”**：
1. **任务内（内层循环）：插件层面的数学资产演进**。在冻结 `base` 验收规则的前提下，插件可自由新增领域引理、修复门（如将附录独立引理增补进 `REPAIR_GATE_CATALOG`，见 [PROPERTY_B_RESEARCH_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md#L192-L194)）或新选锁公式，只要每个新组件通过 `base` 的实际 caller 桥接和独立复算即可立即在本题生效。
2. **任务间（外层循环）：受控的 `base` 补丁晋升**。当执行过程暴露出通用流程缺陷——例如 T34 发现稀疏大 `Nat` 模式匹配导致 8GB 内存与栈溢出，而分离数据/覆盖/调用并改用关联查询可在 87.75 秒内通过（[PROPERTY_B_FAILURE_ATLAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L184-L192)）；或发现向已完成代理 `send_message` 只排队不唤醒（[PROPERTY_B_RESEARCH_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md#L207-L210)）——插件只能向独立目录提交 `BASE_PATCH_PROPOSAL`。
3. **合入准则**：复用 ARIS 现有的 [`meta-optimize`](file:///Users/rfy_naiveai/.gemini/config/skills/meta-optimize/SKILL.md) 与 [`meta-apply`](file:///Users/rfy_naiveai/.gemini/config/skills/meta-apply/SKILL.md) 机制，补丁必须在**冻结历史失败切片上重放验证**（确认能拦截旧陷阱且不破坏已闭义务），并通过**跨领域退化检查**（确认未把 Property B 特有启发式写死在 `base` 中），在下一任务启动前版本化合入。

---

### 三、 阻断局部搜索黑洞：区分有效计算与停滞，以及如何从局部退回全局（答问题 3）

从项目证据看，局部搜索吞噬算力主要有三大病灶：① **已穷尽域盲目重采样**（T33 双锁已完整扫完 462/506 个位置，同模型下换随机种子零增量，见 [PROPERTY_B_FAILURE_ATLAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L31-L38)）；② **非瓶颈项无效微调**（扣除 $D_k$ 未跨过 $C_k - \min(A_k,B_k)$ 的松弛量）；③ **局部松弛丢失全局守恒后靠扩表硬扛**（如 $m(6)\ge 67$ 的 35 点分支四锁扩表失败，见 [PROPERTY_B_M6_GE67.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_M6_GE67.md#L32-L38)）。

#### 1. 挑战 Root 的“连续两轮无有用事实则换路线”
如果“有用事实”定义含糊，Agent 会把“上界从 $4224/4199$ 降到 $4212/4199$”（[PROPERTY_B_FAILURE_ATLAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L43)）或“86 个代表只剩 7 个未过”（[L205](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L205)）包装成“有进展”，从而在死胡同里无限续命。必须将其收紧为硬性判据：
* **必要计算 vs. 无效计算**：计算仅在三种情况下合法——① 针对单代表做表示/caller 探针（Probe）；② 输入域已被证明完整覆盖某个未闭分支，且只对**失败父型**继续分流（如 $m(8)/m(9)$ 仅对 72/73 个失败双锁父型扩三锁，严格父型立即停算，见 [PROPERTY_B_M8_M9_INCREMENT_20261029.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_M8_M9_INCREMENT_20261029.md#L51)）；③ 优化项确系当前活跃最小项且具备跨过阈值 `< 1` 的理论容量。凡未接通真实 caller 的批量建表、已扫完固定域的换种子重跑，一律判定为无效计算。
* **必要的长期攻关 vs. 必须换路线的停滞**：
  * **允许长期推进**：数学归约已闭环、单个非平凡真实 caller 已编译通过，剩余工作只是已知有限目录的分块核验（如 T34 将 925 项与 3618 项重证书拆块编译，见 [PROPERTY_B_FAILURE_ATLAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L189-L192)）；或者每一轮都引入了**能严格排除上一轮失败见证的新全局不变量**（如 A1 从分量大小 $\rho(s)$ 升级到主子式 Gram 秩分离器，见 [L234-L249](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L234-L249)）。
  * **触发停滞熔断**：若同一局部模型下，① 极值代入手检（如代入均匀分数解 $z_A=32/\binom{v}{5}$ 或不交并图，见 [PROPERTY_B_FAILURE_ATLAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L139-L145)、[L236](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L236)）表明松弛上下界恒等，或 ② 增补同类局部配额后活跃瓶颈仍未跨过阈值且无新结构余量，则立即熔断局部扩表。

#### 2. 局部停滞时如何系统地“退回全局”？
当局部搜索触发熔断时，`base` 强制要求插件按以下三步回退，禁止直接把 $s$ 锁扩成 $(s+1)$ 锁大表：
1. **找回被局部松弛丢掉的“同一原超图 $H$ 跨视图守恒律”**：局部失败往往是因为允许对手在每个位置或每个局部视图中独立取最坏情况。退回全局即恢复**量词顺序**（先固定同一个实际坏对再选锁序，如 T33 的 24 点四锁从 $8535/8398>1$ 降为 $8301/8398<1$，见 [PROPERTY_B_FAILURE_ATLAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md#L91-L98)）或**跨视图列守恒**（如 c13 共享 17 个外点的总收费 $192 < 17\times 12 = 204$，直接保证存在低收费视图，见 [PROPERTY_B_RESEARCH_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md#L224-L227)）。
2. **用上游选点定理排除坏局部型，而非硬算坏型概率**：当少数局部残型接近或超过 1 时，退回原图总度预算 $kM$ 与共度超额，证明“原图必存在避开该坏型的锁点选择”。典型证例是 $m(6)\ge 67$ 的 35 点末支：放弃四锁扩表，退回全图度数预算迫使低度共度 2 伙伴与共同单位邻点中心，将分支直接压成 $(12,10,10)$ 与两次 $51>46$ 矛盾（[PROPERTY_B_M6_GE67.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_M6_GE67.md#L32-L38)）；以及 $m(8)$ 在 $v=120$ 利用 $7\times 17 = v-1$ 的整数端点刚性直接取四单位锁（[PROPERTY_B_M8_M9_INCREMENT_20261029.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_M8_M9_INCREMENT_20261029.md#L60-L63)）。
3. **用解析交换或代数秩替代纯组合计数**：如 36 边候选中 $\le 18$ 点放弃双锁残型微调，改用唯一单色边与平衡交换的五个交大小系数直接导出矛盾（[PROPERTY_B_RESEARCH_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md#L3)）。

---

### 四、 区分“数学对象的组合性”与“证明策略搜索的组合爆炸”（答问题 4）

对用户“数学问题很大程度是组合问题”的判断，需做严格的两层切分，避免无依据泛化：
1. **对象层（领域数学）并非都是有限组合**：Property B 的小参数下界确实属于有限超图极值组合，需要处理局部迹、度数分拆与排列位置；但即便在本项目内，一般 $k\ge 12$ 的统一增长定理（结合精确积分与单调性解析估计）以及 Gram 矩阵半正定秩界，靠的也是连续分析与代数不变量，而非有限情况枚举。因此 `mathrsi-base` 绝不能假设所有数学对象都能离散化为有限表。
2. **元层（证明策略与归约树搜索）普遍存在组合爆炸**：所有数学领域的共同点在于，**定义展开、引理串联、案例划分（Case Split）与辅助不变量选择**在元层构成一棵组合爆炸的决策树。
3. **核心方法论启示**：低效的数学 Agent 往往**用“对象层的暴力分案枚举”去弥补“元层策略树缺少强不变量”的缺陷**——在错误的松弛模型下切出成千上万个带标签子情况。高效架构的本质，是在元层用**早期的实际 caller 试编与全局守恒律**剪掉无效策略分支，在对象层用**自同构商集、容量剪枝与仅扩失败父型**把必须计算的有限域压到最小，最后才启动确定性算术核验。

---

### 五、 基于现有 ARIS 组件的最小验证方案（答问题 5）

遵循 HERO 原则与 [MATH_AGENT_HARNESS_SYNTHESIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/MATH_AGENT_HARNESS_SYNTHESIS.md#L73-L80)，**不要新建独立运行时、状态数据库或通用事件总线**，直接用现有 ARIS 技能与目录拼装验证：
1. **零平台映射**：
   * `mathrsi-base` 直接由 [`proof-orchestrator`](file:///Users/rfy_naiveai/.gemini/config/skills/proof-orchestrator/SKILL.md)（管理运行目录、义务表与停止条件）、[`proof-writer`](file:///Users/rfy_naiveai/.gemini/config/skills/proof-writer/SKILL.md)（推导与局部到全局桥接）、[`proof-checker`](file:///Users/rfy_naiveai/.gemini/config/skills/proof-checker/SKILL.md)（A/B/C 三阶段独立审计）与按需调用的 [`lean-formalize`](file:///Users/rfy_naiveai/.gemini/config/skills/lean-formalize/SKILL.md)（最小 caller 试编、分块核验、`#print axioms` 审计）组成。
   * `mathrsi-propertyB` 直接落地为 `research-wiki/` 下的结构引理目录、失败地图及各参数目录下的独立复算脚本（如 `independent/check.py`）。
   * 外层 RSI 演进直接复用 [`meta-optimize`](file:///Users/rfy_naiveai/.gemini/config/skills/meta-optimize/SKILL.md) 与 [`meta-apply`](file:///Users/rfy_naiveai/.gemini/config/skills/meta-apply/SKILL.md)。
2. **最小验证设计（不虚报加速比，只测真实闭合与止损）**：
   * **历史陷阱反事实回放（止损测试）**：选取项目已有的 3 个典型高成本切片——① T33 $v=20$ $(7,9)$ 非活跃项扣除、② $m(6)\ge 67$ 的 35 点四锁扩表、③ T34 的 21 点稀疏大 `Nat` 编译卡死。验证加入“活跃瓶颈 JSON 契约 + 局部退回全局清单 + 表示探针”后，工作流能否在 **1 轮探针内**自动阻断无效扩表并路由到正确层级。
   * **真实子目标端到端闭合验收**：在一个待闭数学分支或跨领域小命题上实测，严禁以“步骤完成率、生成表格行数、模型赞同票数”衡量进度；唯一验收指标是 **① `RemainingGoal` 是否被连接原始输入的完整证据链实质消减（纸面 `sound-modulo-imports` 或 Lean 标准三公理通过），以及 ② 被废弃分支消耗的真实 CPU 秒与 Token 占比是否下降。**

