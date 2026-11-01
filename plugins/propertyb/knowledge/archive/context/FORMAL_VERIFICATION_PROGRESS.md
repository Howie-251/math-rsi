# 原命题的完整 Lean 核验记录

2026-10-06。**[Main.lean](../formal/Aris4Math/Main.lean) 已证明正式规格中的原目标 T，默认构建及独立导入审计均成功。** 原先列出的约化、概率表示、实际类型表、link 扣除和分支装配义务均已闭合。Grok 与全新 Gemini 会话 r10 的最终装配审阅均已有效返回，在各自读取范围内未发现具体问题；它们阅读现有构建日志，没有亲自执行构建。展示文档验收和交付状态见[项目交接](../NEXT_SESSION.md)。

## 实际证明了什么

规范源为 [FORMAL_SPEC.md](../FORMAL_SPEC.md) 的 D1、D2、T。Lean 中 `Simple5Hypergraph V` 的边集为 `Finset (Finset V)`，每条边的基数等于5；`PropertyB H` 要求存在一个布尔染色，使每条边中取值为 `true` 的顶点数介于1与4之间。

主声明为 `Aris4Math.propertyB_of_at_most_thirty_two : Target`。同文件提供展开后的声明：

```lean
theorem two_colorable_of_at_most_thirty_two
    (V : Type u) [Fintype V] (H : Simple5Hypergraph V)
    (edges : H.edges.card ≤ 32) :
    ∃ c : V → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4
```

`V` 是任意宇宙层级上的有限顶点类型；`Fintype` 给出有限性，不限定顶点数或预先枚举某类超图。边集无重复，孤立顶点允许。结论不要求两色人数均衡。顶层前提只有五元简单超图及边数至多32，没有点对覆盖、结构剖面、概率上界或所需引理成立等附加假设。

另一个顶层定理 `non_propertyB_edges_ge_thirty_three` 直接证明 `¬ PropertyB H → 33 ≤ H.edges.card`。按规格 D3 定义，这给出 **m(5)≥33**；项目没有将极值函数另定义为 Lean 对象，也没有声称证明等号或构造33边反例。

## 全部情形如何覆盖

`Reduction` 证明合并不共边顶点、合法染色拉回、最小顶点反例及点对覆盖；`Structure` 给出顶点数上界；`SmallVertices` 证明至多18点全部可染，并完成 `Target ↔ FiniteGoal`。这里的 `FiniteGoal` 是19–25点、恰32边、点对覆盖的全部五元超图。补边和重标号也在约化中证明，整个约化不依赖文献基准 m(5)≥32。

`Aris4Math.finite_goal` 逐一调用下列实际超图定理，随后 `SmallVertices.target_of_finite_goal` 将结论返回任意有限顶点类型：

| 顶点数 | 完整分支入口 | 关键内容 |
|---|---|---|
|19|`NoLocks.nineteen_propertyB`|无锁条件下实际端点与单交事件计数、逐位置最小值及严格总界|
|20|`TwentyVertices.twenty_propertyB`（`GlobalPairs.lean`）|解析双计数给出至多948个单交有序边对，再接实际概率界|
|21|`TwentyOne.twenty_one_propertyB`|选出度5、6或7的锁点；度7情形证明实际 link 扣除|
|22|`TwentyTwo.twenty_two_propertyB`|共度1的度数组合66、67、77全部覆盖；后两种实际扣除闭合|
|23|`TwentyThree.twenty_three_propertyB`|66双锁或677三锁全部覆盖；三锁末中心的零权重例外界已证|
|24|`LargeVertices.twenty_four_propertyB`|四锁解析分类、真实类型重数及严格概率界|
|25|`LargeVertices.twenty_five_propertyB`|七点选六锁、解析标签分类、完整迹恢复及严格概率界|

19、20点定理本身允许边数至多32，不需要点对覆盖。21–25点分支使用恰32边和点对覆盖，正是最小反例约化提供的条件；它们没有未满足的剖面或概率前提。

## 从实际对象到数值界的连接

| 数学义务 | 完成模块及证明内容 |
|---|---|
|真实算法与失败覆盖|`Greedy`：递归染色无全红边，失败产生单交的有序 critical pair；成功排列给出原 `PropertyB`|
|条件排列计数|`Counting`、`JointCounting`、`EndpointCounting`、`CriticalCounting`：锁点像、自由双射、端点与临界事件的精确计数；左右占位采用不放回联合计数，不假设独立|
|实际选点与分类|`Structure`、`LowDegree`、`SevenPoint`、`Avoidance`、`Traces`、`BlockClassification`、`K6Classification`、`K6Traces`：证明结构情形覆盖及所需标签选择|
|实际类型重数|`TypeCounting`、`TraceRecovery`、`SmallLockProfiles`、`DoubleTripleLockProfiles`、`TripleLockProfiles`、`K4Profiles`、`TraceProfiles`：每条真实边对应类型，表中重数等于实际纤维基数；同型有序边对正确排除自身|
|概率公式的数值表示|`ProfileProbability`：真实端点事件比率等于 `Numeric.edgeWeight`，实际有序边对事件比率不超过 `Numeric.pairWeight`；锁定/自由中心及位置索引一致|
|实际 link 扣除|`LinkCounting`、`LinkDeletion`、`LinkWeightCertificates`、`ProfileDeletion`：真实无序坏边对数、两个方向、非贡献性及权重下界；每位置不重复扣除；23点例外至多一对|
|严格上界到染色存在性|`Numeric`、`ConditionalUnion`、`ProfileApplication`：有理数严格界、在 C 项内先扣除再取 min、失败样本少于总样本；所有应用条件由真实超图定理消除|

`Numeric` 保留的两个失败剖面用于诊断，不是主证明的成功分支。解析分类和选点定理证明实际输入一定进入适用情形。更详细的接口说明见 [连接记录](FORMAL_CONNECTIONS_PROGRESS.md)；先前分模块证明与构建历史保留在同目录其他 `FORMAL_*_PROGRESS.md` 及 proof-checker 各 run 目录中。

## 实际构建与独立导入证据

最终记录目录为 [2026-10-06_run09](../.aris/traces/proof-checker/2026-10-06_run09/)：

- [默认构建日志](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-build.log)及[元数据](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-build-meta.json)：`lake build`，默认目标 `Aris4Math.Main`，退出码0。日志中的1005个任务包含依赖缓存重放，不表示全部依赖重新编译。
- [独立导入审计源码](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.lean)、[输出](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.log)及[元数据](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit-meta.json)：另行导入 `Main`，打印对象定义、展开后的顶层类型并检查传递公理，退出码0。

四个装配声明 `finite_goal`、`propertyB_of_at_most_thirty_two`、`two_colorable_of_at_most_thirty_two`、`non_propertyB_edges_ge_thirty_three` 的传递公理依赖均仅为：

```text
[propext, Classical.choice, Quot.sound]
```

主证明没有 `sorryAx` 或项目自加公理，也未使用 `native_decide`。精确数值部分以证明项和内核计算核验，没有把外部 Python 输出作为公理导入。

从项目根目录复现：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build
lake env lean ../.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.lean
```

Lean 固定为4.24.0，Mathlib 为 v4.24.0，锁定提交 `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`。旧文档中“默认只构建根模块”的描述已被 `lakefile.toml` 的 `defaultTargets = ["Aris4Math.Main"]` 覆盖。

## 证明依据与适用边界

这不是对所有输入超图、染色或排列做穷举。结构覆盖和排列计数由一般引理证明；有限分情况用于已证明完备的局部结构类型，有限内核求值用于明确的类型表与有理数常数。SAT 搜索、随机样例和模型意见均不是顶层定理的前提。

形式核验依赖 Lean 的标准逻辑基础、内核与所使用的 Lean/Mathlib 工具链；本记录不声称已验证编译器自身或从源码重建全部 Mathlib。完整形式证明、外部模型审阅和人类专家评审是不同证据，本项目尚不声称完成人类专家评审。

## 最终命题对齐与模型审阅

fresh Codex 独立导入 `Main` 并检查原题语义，见[语义审阅](reviews/research/fresh_codex_semantic_r8.md)；同家族意见保留 `provisional` 标记。

[Grok 最终装配审阅原始记录](reviews/research/grok_lean_main_r8.json)实际返回 `grok-4.7-build`、`xhigh`、`end_turn`。它核对任意有限顶点类型、原 `PropertyB`、≤32边、最终约化及22/23点的实际度数/共度/类型输入，未发现具体问题。它明确只阅读源码及给定日志，没有声称亲自运行构建。

Gemini 全新会话 r10 的[原始响应](reviews/research/gemini_lean_main_fresh_r10.json)返回 `gemini-3.8-flash-high`、`high`、`SUCCESS`；模型和 effort 为 CLI 选择记录。其[审阅报告](reviews/research/gemini_lean_main_fresh_r10.md)核对原 Target 与展开结论、最小反例约化、七个分支入口、22/23点实际选点与类型、link 零权重例外、无放回联合条件计数、贪心染色还原及已有构建公理日志，在所读范围内未发现具体问题。报告明确没有执行命令行构建，不能把它计作一次独立重建。

此前的[最终补充 r8](reviews/research/gemini_lean_main_r8.json)、[retry1](reviews/research/gemini_lean_main_r8_retry1.json)和 r9 均返回 API 位置限制 `FAILED_PRECONDITION`，仍是无有效意见的失败记录。r10 使用全新会话，不表明旧会话恢复，也不确定此前报错的根因。此前其他成功审阅仍保持原检查范围。详情与 reviewer 措辞纠正见[审阅汇总](reviews/research/REVIEW_NOTES.md)。模型意见是针对性查错证据，主定理成立的形式依据仍是上述已完成的 Lean 证明。
