# 22 点完整分支

2026-10-06；源码 `formal/Aris4Math/TwentyTwo.lean`。

```lean
Aris4Math.TwentyTwo.twenty_two_propertyB
  (H : Simple5Hypergraph (Fin 22))
  (cover : H.PairCovering)
  (edges32 : H.edges.card = 32) : PropertyB H
```

这是归约后 22 点情形的完整染色定理：结论已经是原 `PropertyB`，没有类型表、概率公式、link 计数或数值严格界作为尚待证明的假设。点对覆盖和 32 条边来自总体最小反例归约。

证明按 `LowDegree.exists_two_locks_of_twenty_two` 已证的实际度数组合分三类：

- **6,6**：`realizes_v22_66` 提供实际四类型表，使用无扣除的 `ProfileApplication.propertyB_of_uncorrected_profile` 与 `8193/8398 < 1`。
- **6,7**：`realizes_v22_67` 提供实际表，位置 12 的实际锁点度数为 7；`v22_67_deduction_12` 提供真实不同坏边对的扣除下界。最终总界为 `4092/4199 < 1`。
- **7,7**：实际两个锁点度数均为 7，位置 11、12 分别使用对应的已证 link 扣除下界。最终总界为 `8175/8398 < 1`。

后两类通过 `propertyB_of_corrected_profile` 把实际删除的零贡献边对权重先从 C 扣除，再取 `min(A,min(B,C−D))`。本分支没有把非最小项的下降直接算作总界下降。

全部四个定理真实编译通过；重编译 8.507 秒、导入审计 3.728 秒，退出码均为 0。导入后完整公理审计仅显示标准 `propext`、`Classical.choice`、`Quot.sound`；无 `sorry`、新增公理、`native_decide` 或超图枚举。

证据保存在 `.aris/traces/proof-checker/2026-10-06_run07/`，前缀 `lean-twentytwo-`。该分支供最终 Target 组合使用，未在本模块中宣告所有顶点数已完成。
