# 20 点分支及 948 有序边对界

2026-10-06；源码 `formal/Aris4Math/GlobalPairs.lean`。

完整分支结论：

```lean
Aris4Math.TwentyVertices.twenty_propertyB
  (H : Simple5Hypergraph (Fin 20))
  (hE : H.edges.card ≤ 32) : PropertyB H
```

结论不另假设点对覆盖、线性、度数、已知概率上界或已知边对计数。计数证明对任意 20 元有限顶点类型成立；最终染色定理使用 `Fin 20`。

## 948 的实际组合证明

`GlobalPairs.singletonPairs H` 是实际不同**有序**边对中交集基数恰为 1 的集合。其他不同有序边对组成互补集合 `otherPairs`。以下均为有限集上的解析双计数。

先设边数恰为 32。令 `P` 遍历 190 个无序顶点对，`λ(P)` 为包含它的实际边数。

1. 每条五元边包含十个顶点对，因此 `sum_pair_degrees` 给出 `Σ λ = 320`。
2. 自然数恒等不等式 `2λ ≤ λ(λ−1)+2` 对零度点对也成立，因此 `Σ λ(λ−1) ≥ 260`，不需要点对覆盖。
3. `pair_intersection_double_count` 按另一个顺序计算同一组“无序顶点对、包含它的有序不同边对”关联，得到
   `Σ_P λ(P)(λ(P)−1) = Σ_(e,f) choose(|e∩f|,2)`。
4. 简单性和五元性保证不同边的交集至多四点，所以每对至多贡献 6；单点相交对贡献 0。于是 `260 ≤ 6*|otherPairs|`，整数量词给出 `|otherPairs| ≥ 44`。
5. 总计 `32*31 = 992` 个不同有序边对，因此 `|singletonPairs| ≤ 992−44 = 948`。

边数至多 31 时，总不同有序边对已至多 `31*30 = 930 ≤ 948`。故 `singletonPairs_le_948` 对边数至多 32 全部成立。

## 接入原目标

`TwentyVertices.critical_sum_le` 先使用 `CriticalCounting.critical_ratio_zero_of_intersection` 将非单交对的实际临界事件概率置零，再使用 `NoLocks.critical_ratio_le` 和 948 界。

两类单边界沿用 `NoLocks.endpoint_sum_le`。`twenty_sum_eq_numeric` 将实际逐位置 `min(A,min(B,C))` 的二十项有理数和与 `Numeric.totalBound Numeric.v20` 等同；后者为 `20874/20995 < 1`。`ConditionalUnion.propertyB_of_position_bounds` 最终产生满足原 `PropertyB` 定义的染色。

本模块只对二十项封闭有理数公式使用 `decide +kernel`，没有枚举超图、排列或染色。

## 核验及交接

13 个定理已经真实编译；导入 olean 后逐项 `#print axioms`，仅使用标准 `propext`、`Classical.choice`、`Quot.sound`。无 `sorry`、新增公理或 `native_decide`。

证据目录：`.aris/traces/proof-checker/2026-10-06_run07/`，前缀 `lean-globalpairs-`。包括构建命令、构建输出和退出码，以及导入后完整公理审计。

NoLocks、Numeric、LinkCounting 的源码本次未修改。19、20 点分支均已直接得到 Property B；21–25 点及最终顶层连接尚待完成，本文不把局部分支完成表述为全局目标完成。
