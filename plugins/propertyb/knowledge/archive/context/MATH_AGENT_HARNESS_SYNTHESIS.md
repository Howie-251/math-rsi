# Argus 与 Archon-Horizon：本项目吸收了什么

2026-10-07。**两者都有可用价值。这次补充的重点是实际 Lean 工作方法：查库、试用、诊断、改表示、选择下一条证明路线。** 之前主要吸收了命题对齐与证明闭合；本轮把执行层的做法写进了本地 `lean-formalize` 草案，并用项目固定环境做了小规模验证。

详细源码核查分别见 [Argus 深读](ARGUS_DEEP_DIVE_20261007.md) 和 [Horizon 深读](HORIZON_DEEP_DIVE_20261007.md)。两份报告区分源码阅读、实际执行和未运行的平台能力；均提供固定提交链接。

## 本次看的版本和材料

| 项目 | 实际提交 | 核查重点 |
|---|---|---|
| Argus | `9cfe9129fd90511c3a1865844ec7dfda1b5d1008` | 数学六类角色技能、Lean checker/auditor、proof ledger、route/goal区分、异步编译、citation和counterexample工具及相关测试 |
| Archon-Horizon | `0df5571f81aae29130c8ec621c9fe7419ca28d6a` | 12个Lean技能、相关review/representation参考、搜索实现、managed build、milestone公理审计及Comparator调用链 |

源码保存在 `ref/software/Argus/` 和 `ref/software/Archon-Horizon/`。当前固定版本与此前评估相同；这次增加的是阅读深度与小规模实测。Horizon 网页缓存存在旧版 CLI，实际源码是 0.2 alpha，不能直接照旧网页运行 `horizon search/check/attempt`。

## 以前已吸收的内容

这些已在上一版技能里形成执行要求：

- 原数学命题独立固定，Lean 定义先反译再对照。
- 从原输入构造引理所需的条件，最后证明这些引理确实推出原目标。
- 检查导出证明的实际类型及传递公理，不根据文件数或编译输出的“成功”判断完成。
- 构建、语义对齐、跨模型意见与独立复现分别报告。
- 模型审阅检查具体义务；多个角色或多个同家族代理不自动提供跨家族独立性。

本轮没有为了匹配另一平台的术语再增加一套审阅流程。

## 这次新增的具体用法

已新增 [Lean 工作循环参考](../aris-skill-drafts/lean-formalize/references/lean-working-loop.md)，并从 [主技能的 implementation loop](../aris-skill-drafts/lean-formalize/SKILL.md) 连接进入。

| 何时用 | 吸收的操作 | 会改变什么 |
|---|---|---|
| 不确定 Mathlib 是否已有结果 | 先查固定库的名称、类型形状、相邻声明和已有调用，再检查完整签名 | 减少猜引理名、重写已有证明和使用错误版本API |
| 找到疑似匹配引理 | 用真实参数和假设写最小 caller，实际编译 | 提早暴露隐式参数、coercion、实例和额外条件 |
| 要更换数学对象的表示 | 先试构造一个对象及一个代表性下游定理，比较是否一条桥接就够 | 避免大规模重构后才发现新表示更难用 |
| Lean 报错 | 先处理第一条因果错误，区分名字、类型应用、实例、重写、数学缺口、资源 | 选择有解释的修复，不重复随机更换 tactic |
| 数学路线卡住 | 区分证明步骤失效、分解错误、方法本身受阻；保存准确阻碍 | 换正确层次的方案，避免把路线失败误作原命题被否定 |
| 多代理探索 | 探索阶段选择失败机制不同的路线；实现阶段按稳定引理接口分工 | 并行增加信息，而非复制同一个瓶颈 |
| 编译慢或并发构建 | 分清排队、下载、导入、elaboration；局部测量并检查真实消费者 | 避免盲目增加全局心跳或将等待误判成数学失败 |

这些操作主要参考 Horizon 的
[搜索](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-search/SKILL.md)、
[证明修复](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/lean/lean-proof-repair/SKILL.md)、
[表示实验](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/review/definition-quality/references/representation-experiments.md)，以及 Argus 的
[数学执行](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/skills/engineer/math-research-execution.md)与
[评审归因](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/verticals/math/skills/reviewer/math-research-review.md)。

## 实际做过的检查

### Horizon 搜索到 Lean 调用

直接调用 Horizon 的 Python 搜索模块，未安装平台：

1. 在本项目固定 Mathlib 的 `Data/Finset/Card.lean` 抽取135项，名称搜索找到 `Finset.card_union_le`，签名模式搜索找到 Disjoint 相关声明。
2. 运行8个上游搜索测试，全部通过。
3. 用项目 Lean 4.24.0 编译实际调用：从 `s.card ≤ 12` 与 `t.card ≤ 20` 推出 `(s ∪ t).card ≤ 32`。搜索返回的库引理接到了真实参数与结论。
4. 同时形式验证一个反例：两个相同单元素集合的并集大小不等于两者大小之和，说明不带不交条件的等式路线不成立。
5. 两个演示声明的传递公理均只有 `propext`、`Classical.choice`、`Quot.sound`。

[搜索原始结果](horizon-deep-dive-20261007/search-smoke.json)、[搜索测试](horizon-deep-dive-20261007/search-tests.txt)、[可读Lean例子](harness-reading-20261007/LeanWorkingLoop.lean)、[最终编译输出](harness-reading-20261007/lean-working-loop.log)。

Horizon 的签名搜索实际是启发式源码抽取及正则匹配，不是 Lean 类型合一；这正是后续真实调用检查的用途。本次没有运行BM25文本检索或启动MCP服务，也没有重新构建 Property B 主证明。

### Argus checker 的精确范围

直接运行未修改的 Argus checker/auditor，测试正常证明、仅定义命题、本地 axiom/sorry、导入 axiom/sorry 共六种情况。结果显示：本地缺口可被拦截，但仅定义 `Target : Prop` 或经导入依赖使用 axiom/sorry 的文件，单次 checker 仍可能返回 `success`。同一个文件中的 Lean `#print axioms` 则准确列出了实际依赖。[复现记录](argus-deep-dive-20261007/probe-results.json)、[原始审计器](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/tools/lean_axiom_audit.lean)。

因此我们保留现有的“指定导出证明＋目标对齐＋传递公理”检查。这里检查的是一个工具组件，未复现 Argus 整个完成流程错误验收；它不是 Lean 内核漏洞。

另外运行了81个 checker/ledger 局部单元测试，通过；1项平台相关跳过、1项隔离 fixture 相关未选。这些多为模拟编译器与台账测试，不是81个真实数学证明。完整范围在 Argus 深读报告。

## 整个平台什么时候值得用

**当前可以直接用的部分：**上述 Lean 工作循环、Horizon 本地名称/签名索引、已有 Lean/Lake、ARIS 的持久知识与 Grok/Gemini 审阅。已把方法落入技能，不必先部署平台。

**Horizon 整体平台适合：**多个相互依赖的 Lean 项目、多人或多机器长期工作、共享构建资源、需要固定公共契约并集中审阅。其 managed build 与 milestone audit 有真实实现；Comparator 比较独立 challenge/solution 的调用链也在，但本轮未运行它。两份 Lean 接口一致仍不能自动证明最初接口忠于纸面数学。[核验实现](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/worker/milestone_verify.py)。

**Argus 整体平台适合：**需要长期自主推进多个研究路线、持久角色分工和统一证据台账的项目。当前项目已有 ARIS、已完成数学工程和审阅记录，新增第二套台账不会直接改善证明。

本轮没有部署两套平台、替换现有MCP或改变已完成数学定理。Horizon 对一些 Lean 技能也明确记录了其上游来源
[cameronfreer/lean4-skills](https://github.com/frenzymath/Archon-Horizon/blob/0df5571f81aae29130c8ec621c9fe7419ca28d6a/src/archon_horizon/pipeline/skills/_sources/lean4-skills/PROVENANCE.md)；
当前只吸收与我们实际任务相符的用法。

## 技能修订的验证状态

先前的两轮跨模型审阅对应641行版本。新增工作循环已单独经过 Grok 和 Antigravity/Gemini 定向增量复审，两者均有效返回，未发现剩余执行性问题，认为可以纳入本地技能草案。原请求、输入快照和实际返回保存在[增量评审目录](skill-evaluation/lean-formalize/harness-addition-review/)；不将旧审阅自动扩大为新内容的审阅。

当前技能入口318行、三份参考共516行，总计834行，结构校验通过。[技能评审汇总](skill-evaluation/lean-formalize/REVIEW_SUMMARY.md)记录各轮实际范围。新内容尚未安装到全局或提交ARIS上游；本轮也未测试通用解题成功率或加速比。
