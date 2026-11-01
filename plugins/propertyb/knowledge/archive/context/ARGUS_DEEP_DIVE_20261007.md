# Argus 数学 agent 与 Lean 实现深读

2026-10-07。结论：**保留现有 ARIS Lean 工程和草案，吸收 Argus 对失败层次、不同证明路线和失败经验的处理；不迁移其运行平台，也不以其 checker 的 `success` 替换指定目标的传递公理审计。** 本次从源码推导出的检查范围问题已用真实 Lean 4.24.0 确认；它不影响 aris4math 已交付的证明。

本次浅克隆 `https://github.com/lbx154/Argus.git` 至 `ref/software/Argus/`，实际 HEAD 为 `9cfe9129fd90511c3a1865844ec7dfda1b5d1008`，提交日期 2026-09-30，标题 `Merge pull request #182 from lbx154/dev`；与昨日 `ARGUS_ASSESSMENT.md` 的版本相同。以下源码链接全部固定到该提交。未修改 Argus 源码，未启动 agent、daemon、网页服务、Jacobian 或外部模型；未更改全局配置。为直接导入 checker，只向本次证据目录局部安装了 `portalocker==4.4.0`，没有安装 Argus 平台。

草案对照基线是本次开始时的 `lean-formalize/SKILL.md` 及当时两份 references（641 行版本）。主代理在整合本次和并行调研结论；本报告不是整合后草案的新一轮质量验收。

## 实际工作方式：模型写证明，工具记录和检查

Argus 的 math vertical 将任务分为 `scope → solve → review`，证明、反例、计算、读文献、Lean 都是按问题选择的手段，并不强迫每题走同一数学路线。`targeted` 要处理指定命题；`exploratory` 允许探索性结果。Engineer 做数学和写文件，Reviewer 对照原问题审阅；`REQUIRE_INDEPENDENT_REVIEW=True` 表示独立角色，并不证明模型跨家族。[阶段源码](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/stages.py#L1-L49)

所读数学技能和 Lean 入口里，没有专门生成本题证明的算法、Lean tactic 搜索树、Pantograph/LeanDojo 接口或自动从错误推导新引理的实现。实际流程是通用模型根据数学技能写 `.lean`，调用文件级 checker，再根据返回继续工作。这个结论限于已读的 math vertical 和 Lean 工具，不是对仓库所有未来或外部插件的断言。[执行技能的 Lean 入口](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/skills/engineer/math-research-execution.md#L54-L114)

`run_lean_check` 的实际步骤是：

1. 找 Lean/Lake 和版本；用 Lake 时记录工作区内的 `lake env lean --version`，而非误记系统默认 Lean。
2. 在当前源文件上做轻量词法扫描，识别 `sorry`、`admit`、`axiom`、`constant`，跳过注释、普通/原始字符串及转义标识符。
3. 运行 `lean file` 或 `lake env lean file`；保留命令、cwd、退出码、stdout/stderr。
4. 检查编译器的 sorry 警告；成功后再用 `lean --run lean_axiom_audit.lean file` 重新 elaboration，并依据审计退出码/标记更新结果。

它返回 `success / proof_hole / syntax_error / type_error / timeout / unavailable`。编译返回 0 而审计未成功，不会被算作成功；超时回收进程组。[执行与结果归类](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/tools/lean_check.py#L69-L311)、[词法扫描](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/tools/lean_check.py#L315-L410)

较上层的 `lean_evidence` 进一步区分缺工具链、缺库、审计无法运行，避免把 `unknown module prefix Mathlib` 当作数学错误。台账将失败编译记为 `inconclusive`，不会从 Lean 没有证明出来推出命题为假。这是有实现支持的行为，不只是技能口号。[环境归因](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/lean_evidence.py#L397-L435)、[失败不是反驳](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/math_state.py#L401-L407)

## 核心实测：环境公理审计不等于目标的传递公理审计

`lean_axiom_audit.lean` 重读源文件，处理 import 和所有命令，然后仅遍历 `env.constants.map₂` 中新加入环境的声明，检查 `info.isAxiom`。它没有接收“目标定理名”，没有追踪该定理的证明依赖，也没有调用 `collectAxioms` 或 `#print axioms`。[完整 36 行审计器](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/tools/lean_axiom_audit.lean#L1-L36)

在隔离目录，用项目现有 Lean 4.24.0 直接运行未经修改的 `run_lean_check` 和上述审计器，得到：

|输入|Argus checker 返回|编译/审计退出码|实际含义|
|---|---|---|---|
|`theorem clean_target : True := by trivial`|`success`|0 / 0|正常对照；目标无公理依赖|
|仅 `def Target : Prop := False`|`success`|0 / 0|只定义命题，没有证明它；checker 不验收指定主定理|
|本文件 `axiom unproved : False`，随后引用|`proof_hole`|未运行 / 未运行|源扫描直接拦截|
|本文件 `theorem unfinished : False := by sorry`|`proof_hole`|未运行 / 未运行|源扫描直接拦截|
|import 已编译依赖，其中有 `axiom dependency_axiom : False`；当前定理引用它证明 `False`|`success`|0 / 0|当前文件的 `#print axioms imported_bad` 显示 `[dependency_axiom]`|
|import 已编译依赖，其中定理用 `sorry` 证明 `False`；当前定理引用它|`success`|0 / 0|当前文件的 `#print axioms imported_unfinished` 显示 `[sorryAx]`|

证据为 [探测脚本](argus-deep-dive-20261007/probe.py)、[完整命令与返回](argus-deep-dive-20261007/probe-results.json)、[隔离 Lean 源码](argus-deep-dive-20261007/sources/ImportedSorry.lean)。依赖 `.olean` 由同一脚本现场生成，日志同时记录该步骤。

在本项目根目录复现：`python3 -m pip install --target context/argus-deep-dive-20261007/deps portalocker==4.4.0`（已有时省略），然后执行 `PYTHONDONTWRITEBYTECODE=1 python3 context/argus-deep-dive-20261007/probe.py`。脚本使用本项目已有工具链和固定 checkout；只在其证据目录写测试文件与输出。不是通用安装指南。

**边界必须说清：这是对 checker 的真实检查，不是对整个 Argus 项目完成流程的攻击复现。** 更上层的源发现若同时纳入依赖源码，可发现那些文件的缺口；Reviewer 也应该拒绝错误命题。这里证明的是：单次 `success` 和这份 environment audit 本身，不承担“目标存在且无未批准传递公理”的保证。Lean 内核没有接受无条件的 `False`，其公理输出如实暴露了依赖。不能把该现象称为 Lean 漏洞，也不能声称已经复现整个平台错误交付。

本地草案已经要求检查实际 proof declaration、原始目标、独立导入和 `#print axioms`；应保留。Argus 的全文件局部 axiom 禁止比目标依赖审计在某些方向更严格，却在 imported 依赖方向更弱：即使无关实验声明了公理，也会拒绝文件，而 imported 公理未必被该审计发现。不能用“更严格”一个词概括两者。

第一次探测只指定 Lean 二进制绝对路径，未向子进程 PATH 加其目录；审计器的 `Lean.findSysroot` 需要调用 `lean`，因此返回 `unavailable`。该真实环境失败保存在 [首次记录](argus-deep-dive-20261007/probe-missing-path.json)。补齐**仅本探测进程**的 PATH 后得到上表；没有修改审计源码或放宽规则。这不是 Lean 4.24 不兼容。

## 命题保真、证据与目标闭合：强处和真实范围

Argus 正确区分“Lean 证明这个类型”与“这个类型就是用户的数学命题”。但所谓 substantive fidelity document 的程序检查，实质是文档存在、正文至少 40 字符、提及被扫描到的某个声明，以及未在检查后改写；不检查其数学解释正确性。代码明确承认这点。[阈值与声明正则](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/lean_evidence.py#L136-L158)、[检查实现](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/lean_evidence.py#L707-L772)、[语义仍由审阅负责](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/math_state.py#L390-L399)

proof ledger 的优点在于状态严格区分：模型意见不能升级为 kernel；有未关闭外部假设时为 conditional；route 所有 obligations 完成，不会自动升级目标，因为“这些 obligations 推出目标”还未证明；被反例否定的 route 不会连带否定 goal。这个区别落实在代码和回归测试中。[状态计算](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/proof_ledger/assessment.py#L316-L426)、[route 不改变目标状态](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/proof_ledger/assessment.py#L226-L273)、[对应回归测试](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/tests/proof_ledger/test_proof_obligations.py#L138-L189)

不过 `closed_kernel` 是证据记录的派生状态，取决于 producer 做了什么检查。`assess_claim` 不运行 Lean，也不验证 formal_statement 中存在目标证明。因此台账自身再严谨，也不能补上上节 checker 没有承担的义务。[实际升级条件](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/proof_ledger/assessment.py#L374-L416)

目标完成还有另一层：在 targeted 的 `review` 阶段，`stages.py` 要求 proof graph 的 goal 与保存的 goal 一致，且 `gap()` 为零。它能挡住“旁支引理完成，根目标仍标 open”的错误；相关测试有明确案例。其 proof graph 是模型维护的节点/依赖和 `reviewer_confirmed`，不是从 Lean 证明项导出的图。根节点标 proved 时 `gap()` 停止下探，因此这是流程一致性检查，不是依赖内核。[目标闭合门](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/stages.py#L113-L176)、[图算法](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/proof_graph.py#L199-L251)、[旁支不能完成目标的测试](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/tests/skills/test_math_targeted_goal_closure.py#L80-L139)

本地草案已经把这个要求落到 Lean 的实际 caller、任意原始输入和顶层 `Target` 证明，比另加 JSON “proved” 标记更适合当前工程。没有必要引入第二份 `MATH_STATE.json` 或 `PROOF_GRAPH.json`。

## 异步编译与结果解释

Argus 的 `submit` 将当前主源文件和 fidelity note 拷贝到 run 目录，后台检查该副本，`reclaim` 再确认原文件仍一致才发布记录；未完成时返回独立运行中状态，worker 丢失时不伪造数学 verdict。同步 `verify` 会在执行前后检查源与说明未改动。这解决的是后台运行与同时编辑的真实冲突。[异步入口及限制](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/lean_async.py#L301-L409)、[运行中/丢失处理](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/lean_async.py#L536-L580)、[同步绑定](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/lean_evidence.py#L1075-L1098)

这不是整个多模块 Lean 项目的快照。源码只复制两个文件；若项目自带 Lake 工作区导致副本解析到不同 workspace，`submit` 明确拒绝并要求用同步 `verify`。因此不能把它描述为已经解决任意 mathlib 多文件工程的并行快照问题。本次只静态阅读该路径，没有启动后台 worker。

对本地草案的实际借鉴是：编译较久且有人并行改相关文件时，要明确检查的是哪份输入；编辑变更后重新编译受影响模块，再验实际主入口。利用已有任务所有权、git revision/diff 和日志即可。不要为此复制 Argus 的完整异步服务、永久 hash/certificate 系统。

## 反例工作流与 Jacobian：能提供工具结果，不自动判真

数学技能建议在昂贵证明前尝试便宜的反例，构造必须满足全部原假设；这是数学选择，不是每题必须完成的阶段。Jacobian adapter 的工作是 `find/browse → inspect → run`：查操作、读 typed contract、保留 operation id、原始 payload、返回值和错误；它通过 stdio 调用独立可执行程序，并不在 Argus 内实现所有数学操作。[执行技能](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/skills/engineer/math-research-execution.md#L6-L16)、[实际 MCP 适配](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/tools/jacobian.py#L153-L213)、[run 请求](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/tools/jacobian.py#L333-L361)

Reviewer 要比较操作的 postcondition 与实际命题，成功退出不代表结果本身见证了反例；timeout、传输失败、不完整结果、UNKNOWN 都没有数学结论。[Reviewer 约束](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/skills/reviewer/math-research-review.md#L123-L135)

Counterexample Lab 本身是现有 CSV/文件的只读展示。`outputs/results.csv` 有该 ID 的行即显示 `verified`，有 `rejected.csv` 行即显示 rejected；并不自行复算反例或给 Reviewer acceptance。文档明确承认这是输入文件的投影。[说明](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/docs/counterexample-lab-jacobian.md#L45-L66)、[状态生成](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/webapi/counterexample_dashboard.py#L118-L150)

ledger 虽允许 computational tier 反驳，但本提交没有写入这个 tier 的 producer，Jacobian 的 stdout 也不会自动变成该 evidence。普通模型 `judgement: refutes` 不获得机械反驳地位。[允许 tier 与已有 producer](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/proof_ledger/assessment.py#L96-L119)

本地不需要安装 Jacobian 才能采用这套含义：候选反例记录“对象、原假设逐项成立、结论失败、精确复算/证明”；未找到只报告搜索范围。已有草案基本覆盖这些要点。不要搬运页面的进度百分比或 `verified` 标签。

## 最值得补充的研究循环和经验复用

|可吸收点|Argus 的具体做法|本地草案的新增价值和落点|
|---|---|---|
|区分失败层次|`proof` 修证明步骤；`plan` 重做子目标/依赖；`strategy` 停止该数学机制|在 `SKILL.md` implementation loop 第 4 步与 review 的 objections 中加一句归因；现有“API vs 数学”区分还没有细分数学失败层次|
|保存死路线的数学原因|retire-route 需要原因，后续任务会看到；不能只有 retired 标签|在已有 continuation note 增加一行“已放弃路线及阻碍/重新尝试条件”，不另建状态库；下次避免重新证明同样无效的充分条件|
|并行不同机制，不重复相同瓶颈|替代路线应会因不同原因失败；给探索者目标与已知失败，不预塞完整分解|现有草案适合“稳定 lemma 接口分工”；补充“未知路线探索”的不同委派方式，不改变已定路线的模块所有权要求|
|根据实际缺口衡量下一步|问某 lemma 成立后还缺什么；扩大同种有限实验不自动缩短全称证明缺口|强化既有“highest unclosed connection”：说明下一步会消除哪个剩余前提；数值范围扩大仅在连接已证明覆盖义务时计入证明进展|
|共享有用的已有知识|任务上下文给当前 claim、定义、直接义务、来源证据和死路线原因|在现有任务 packet 带入直接相关的已查结果、失败和最后有效错误；避免每个 agent 重查同一来源，不复制 depth-1 的硬截断|

原文依据：[失败层次](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/skills/reviewer/math-research-review.md#L27-L52)、[并行路线](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/skills/engineer/math-research-execution.md#L188-L230)、[上下文中已有查证结果](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/context_projection.py#L390-L407)、[适应来自具体方法失败](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/skills/scientist/math-research-adaptation.md#L6-L12)

建议可以控制在以下三段英文增补内，由维护草案的主代理结合另一项目的调研合并。本报告未直接编辑草案。

```text
When a mathematical attempt fails, distinguish a gap in the proof from a
wrong decomposition and from an obstruction to the strategy itself. Repair
at that level. Record why a route was abandoned in the existing continuation
note, including what new fact or mechanism would justify reopening it.

When the proof route is still unknown, parallelize genuinely different
attacks that face different obstructions. Give each worker the original goal,
relevant definitions, known results, and failed routes; let it derive its own
decomposition. Once a route is chosen, return to stable lemma interfaces and
non-overlapping module ownership.

For each substantial next step, identify the remaining premise or connection
it would close. A larger bounded experiment counts toward completion only
when a proved reduction and coverage argument connect that computation to
the target. Otherwise retain it as exploration and use what it teaches to
choose the next mathematical move.
```

不要照搬 Argus reviewer 中“扩展有限范围完全不缩小 gap”的绝对句式。若已证明全称目标约化到一个有限域，完成其中尚缺范围可能正是最后证明义务；本项目解析局部分类与精确算术就是必须保留的区分。也不要按“每轮 gap 节点数下降”评分：一个关键一般引理可能暂时拆出更多有意义的小义务。

已经吸收、不需要再加的内容：原始目标作为基线；独立回译；量词/对象/隐藏前提；conditional lemma 与实际输入分开；route 完成不等于原目标；真实编译与日志；错误不等于反例；绑定实际读过版本；只重审受影响内容；最终目标的传递公理与可重现交付。它们都已在本地 `SKILL.md` 和两个 references 中成为执行要求。

暂不采用：24/7 Manager/Planner/Engineer 调度、第二份 proof ledger、所有 `.lean` 文件一概门禁、硬编码文档长度、固定深度上下文、哈希证书体系、网页进度百分比、通用数学 sidecar 安装。当前 task scope 下，这些都没有替代更昂贵工作的实际收益。

## 文档与实现不一致之处

数学文档 §4.2 称 content check 唯一决定性回答是 `refutes`，并将它与 `REFUTING_TIERS` 混写；实际代码允许独立 reader 的 literature `supports` 得到 `CitationStatus.CONFIRMED`，而 literature 既不证明 claim，也不在 claim 的 REFUTING_TIERS 中。被错误引用的来源与原数学命题为假本来就是不同结论。应以该提交的代码为准，不能借文档推导自动反驳能力。[文档](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/docs/research-mathematics.md#L240-L257)、[citation 实现](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/proof_ledger/assessment.py#L561-L582)、[claim 的 tier](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/proof_ledger/assessment.py#L96-L119)

文档称已在数论问题跑通三阶段，这是仓库作者的报告。本次没有复现自主研究或评价其证明难度。仓库附带的 `erdos_straus_even_local.lean` 是正整数参数下的有理恒等式，不能称其证明了整个 Erdős–Straus 猜想；测试名也把它称为局部有界范围的 fixture。[实际 fixture](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/tests/fixtures/lean/erdos_straus_even_local.lean#L1-L10)

## 实测与阅读覆盖

- **真实 Lean 检查：** 上述六例，Lean 4.24.0，原 checker + 原 auditor；证据已链接。没有重新运行 aris4math 的已完成主证明。
- **局部上游测试：** `tests/tools/test_lean_check.py` 与 `tests/proof_ledger/test_proof_ledger_kernel.py`，最终 **81 passed、1 skipped、1 deselected**。Windows 路径测试在 macOS 跳过；一个 symlink 测试依赖根 conftest fixture，因本次主动隔离平台 fixtures 而明确不选。完整命令、退出码和输出在 [unit-tests.json](argus-deep-dive-20261007/unit-tests.json)。这些多为 fake compiler/台账单元测试，不是 81 个真实 Lean 定理。
- **测试前置尝试：** 首次仅用 `--confcutdir=tests/tools` 运行 checker 文件，缺 `require_symlink_support` fixture 而有一项 setup error；不是 Argus 逻辑测试失败。[初次命令和输出](argus-deep-dive-20261007/unit-tests-initial.txt) 单独保存。最终用 `--noconftest` 并明确 deselect 该项，避免触发仓库全局平台状态 fixtures。未声称全量 CI 通过。
- **完整读过：** `docs/research-mathematics.md`、`docs/counterexample-lab-jacobian.md`、`argus/tools/lean_check.py`、36 行 Lean auditor、math 的 manager/planner/engineer/reviewer/scientist adaptation/distillation 六份 skills、`proof_graph.py`；本地旧评估、AGENTS.md、lean-formalize 主技能和两份 reference。
- **针对相关函数细读：** `lean_evidence.py` 的声明提取、fidelity 检查、schema、环境归因、同步 verify 和 CLI；`lean_async.py` 的 submit、worker、reclaim 及 workspace 限制；`math_state.py` 的 compiler evidence 入账、编译失败语义和 certificate 引用；`assessment.py` 的 tiers、claim、citation、route 计算；`models.py` 的状态绑定设计；`context_projection.py` 的目标解析、定义选择和 citation 复用；Jacobian adapter 的发现/运行/typed result；counterexample dashboard 的状态派生。
- **测试源码有针对性阅读：** checker 的 fake compiler、环境/超时/sorry/axiom/词法案例；proof ledger 的 kernel/citation/route 案例；proof_obligations 的 route 不升级目标案例；targeted_goal_closure 的根目标/旁支案例；async 和 evidence 测试的相关案例入口；Jacobian mock 和需真实 sidecar 的集成测试。除上述两份已执行文件外，其他测试仅阅读。
- **未做：** 全仓源码逐行审计、全量测试、平台部署、外部模型自主求解、Jacobian 数学能力测试、长期并发或高难度定理成功率评估。相关文档承诺不能转写为本次实测结果。

本次直接价值是把可操作的研究循环经验与检查器保证范围分清。ARIS 草案应补充少量“失败后怎样换路线”的执行语言，继续以实际导出定理、原始命题对齐和传递公理作为 Lean 完成交付的依据。
