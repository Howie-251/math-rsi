# 19 点无锁分支：实际超图到 Property B

2026-10-06；入口为 `formal/Aris4Math/NoLocks.lean`。

已完成并经 Lean 4.24.0 内核检查的结论：

```lean
Aris4Math.NoLocks.nineteen_propertyB
  (H : Simple5Hypergraph (Fin 19))
  (hE : H.edges.card ≤ 32) : PropertyB H
```

这是真正的完整 **19 点分支**，没有点对覆盖、线性、度数、事件概率或类型剖面作为额外假设。它尚不是涵盖所有顶点数的 `Aris4Math.Target`。

## 实际事件如何接上算术

取空的锁定顶点列表 `Empty ↪ Fin v`，样本为全部排列。位置 `k : Fin v` 使用从 0 开始的下标。

- `endpoint_ratio`：任意真实五元边的最大值/最小值位于 `k` 的概率分别为
  `5 * choose(k,4) / (v * choose(v−1,4))` 和
  `5 * choose(v−1−k,4) / (v * choose(v−1,4))`。
  这由 `CriticalCounting.free_endpoint_ratio` 的实际排列计数推得。
- `critical_ratio_le`：任意两条不同的真实五元边，形成 `Greedy.CriticalPair` 的概率至多
  `choose(k,4) * choose(v−1−k,4) / (v * choose(v−1,4) * choose(v−5,4))`。
  单交时使用 `free_critical_ratio` 的等式；非单交时先证明实际事件概率为 0。
- `endpoint_sum_le` 与 `critical_sum_le`：实际边集至多有 32 项；不同有序边对至多 `32*31 = 992` 项。用非负权重推出实际事件和的上界。边对顺序没有丢失，也未额外乘交点选择数。
- `nineteen_sum_eq_numeric`：上述实际上界逐位置取 `min(A,min(B,C))` 后，其 19 项和恰等于 `Numeric.totalBound Numeric.v19`。这个封闭等式由 `decide +kernel` 核验，随后使用既有 `Numeric.v19_lt_one`；精确数值为 `222656/230945 < 1`。
- `ConditionalUnion.propertyB_of_position_bounds` 连接真实临界事件覆盖、实际贪心染色失败事件和概率严格小于 1，产生符合原 `PropertyB` 定义的染色。

封闭计算只处理 19 个明确的有理数公式；证明没有枚举超图、染色或排列，也没有以有限搜索未命中替代普遍结论。

## 核验与边界

全部 14 个定理通过检查。最终定理及所有本模块定理的导入后 `#print axioms` 仅显示标准基础依赖 `propext`、`Classical.choice`、`Quot.sound`；无 `sorry`、新增公理或 `native_decide`。

真实构建及导入审计记录：

- `.aris/traces/proof-checker/2026-10-06_run07/lean-nolocks-request.json`
- 同目录 `lean-nolocks-build.log`、`lean-nolocks-build-meta.json`
- 同目录 `lean-nolocks-axioms.lean`、`lean-nolocks-axioms.log`、`lean-nolocks-audit-meta.json`

本模块复用已冻结的 `CriticalCounting`、`ConditionalUnion` 与 `Numeric`。本次未修改 Numeric、Structure、Traces，未改变主证明总体状态。剩余 20–25 点分支及其最终顶层拼接仍需分别完成。
