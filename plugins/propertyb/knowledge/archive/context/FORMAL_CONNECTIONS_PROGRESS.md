# 实际类型、概率与染色结论的连接

2026-10-06。**类型表、概率公式、实际 link 扣除及所有19–25点分支已接入 [Main](../formal/Aris4Math/Main.lean)，原目标 T 已完成形式证明。** 本文说明接口如何落实到实际超图；最终构建与命题范围见[完整核验记录](FORMAL_VERIFICATION_PROGRESS.md)。

## 类型表确实来自实际超图

`positionType vertices positions e` 是真实边包含的锁点所占的位置列表，采用从1开始的索引，去重并排序。它由实际顶点嵌入和位置嵌入生成。

`TableRealization` 要求表内类型不重复、每条真实边都有表内类型，而且每种类型的重数等于实际纤维基数。`RealizesProfile` 另要求顶点数、锁位置与数值数据的有效性一致。`SmallLockProfiles`、`DoubleTripleLockProfiles`、`TripleLockProfiles`、`K4Profiles` 和 `TraceProfiles` 分别从21–25点的真实结构证明这些条件，没有将剖面存在性当作超图的额外假设。

`TypeCounting` 证明：若类型 t 的对象数为 l_t，则不同有序对象对中 (t,u) 的数量恰为 l_t(l_u−[t=u])。同型排除自身、异型不扣，两个方向保持区分。真实纤维求和给出 `Numeric.boundA`、`boundB` 及无特殊 cap 时 `boundC` 的精确表达式。20点的948单交有序边对界由 `GlobalPairs` 另行证明。

## 概率与存在性连接

`ProfileProbability` 证明真实单边端点概率等于 `Numeric.edgeWeight`，真实不同有序边对的 critical 事件概率不大于 `Numeric.pairWeight`。证明处理锁定/自由中心、兼容条件、从0到1的位置转换和自由点容量；左右位置使用不放回的联合排列计数。

`ProfileApplication` 将真实概率公式接入 `TypeCounting` 的聚合结果，然后应用 `ConditionalUnion`：

- `propertyB_of_uncorrected_profile` 从实际实现的无扣除剖面及其严格总界推出原 `PropertyB`。
- `propertyB_of_corrected_profile` 要求每个修正中心的 `Numeric.deduction` 不超过该真实锁点的坏边对双向权重和。该条件由 `LinkCounting`、`LinkDeletion` 和 `LinkWeightCertificates` 在21、22、23点实际应用中证明，随后同样推出 `PropertyB`。

`ProfileDeletion` 按位置构造删除集合并证明子集关系及非贡献性，避免在同一位置重复扣除。扣除先进入 C 项，再取 min。`totalBound_eq_sum_of_eq` 将从1开始的数值列表求和转换为实际 `Fin v` 位置求和，顶点数一致性来自 `RealizesProfile`。

23点677三锁的末中心允许例外权重为0：两种例外类型各只有一条实际边，故至多产生一个无序坏边对；真实坏对数至少为2，其余坏对具有严格正权重下界。这一例外已进入 `v23_677_deduction_13`，不是由数值表猜测后省略的条件。

## 全部分支与最终装配

`TwentyOne` 实例化度5、6、7单锁；`TwentyTwo` 实例化共度1的66、67、77双锁；`TwentyThree` 实例化66双锁或677三锁。`LargeVertices` 使用实际四锁/六锁分类及精确类型重数，完成24、25点。各完整分支仅有约化给出的真实超图条件，没有未满足的类型、概率或扣除前提。

`NoLocks` 和 `GlobalPairs` 已分别给出19、20点完整结论。`Aris4Math.finite_goal` 装配全部七类，`SmallVertices.target_of_finite_goal` 消除有限目标中的顶点数与点对覆盖条件，得到任意有限顶点集上的原 T。

原四模块及八个关键声明的构建/导入审计保存在 [run08](../.aris/traces/proof-checker/2026-10-06_run08/) 的 `lean-root-connections-*` 文件。包含所有新连接的最终证据为 [run09 构建日志](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-build.log)和[独立导入审计](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.log)。最终主声明的公理依赖只有 `propext`、`Classical.choice`、`Quot.sound`。

全链条没有穷举所有超图、染色或排列。有限求值用于明确的局部类型与有理数系数，输入结构分类、真实事件计数和分类完备性由定理证明。
