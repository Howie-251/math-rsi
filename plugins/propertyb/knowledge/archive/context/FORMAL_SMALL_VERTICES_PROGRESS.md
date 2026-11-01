# R4 与完整有限等价约化的 Lean 核验

2026-10-06。`SmallVertices.lean` 已编译通过并冻结。
**任意至多18点、至多32边的简单五元超图可染已证明；原目标 T 与规范 F 的等价已证明。**
F 本身仍待19–25点的结构、概率及数值分支完整接入，故没有宣称 T 已无条件证明。

源文件：[formal/Aris4Math/SmallVertices.lean](../formal/Aris4Math/SmallVertices.lean)。
成功日志：[lean-small-vertices-build.log](../.aris/traces/proof-checker/2026-10-06_run06/lean-small-vertices-build.log)。

## 解析计数与全称结论

先固定有限顶点集上的红位置集合 `red`，将它沿任意排列的逆像拉回为红点集。
对固定五元边 `e`，`monochromaticPermutations_card` 调用
`Counting.card_image_subset` 的一般纤维计数，得到全红排列数为

\[
\binom{|red|}{5}\,5!\,(v-5)!;
\]

全蓝排列数只需把 `|red|` 换成 `v-|red|`。
`propertyB_of_partition_count_bound` 对每条边的两个事件取并，再对全部边取并，
由有限集 union bound 证明：若

\[
|E|\left(\binom{|red|}{5}+\binom{v-|red|}{5}\right)5!(v-5)! < v!,
\]

则某个排列不产生任何单色边。证明从这个排列构造布尔染色，并证明每边红点数
至少1、至多4，最终结论使用主模块原 `PropertyB` 定义。

该条件是正文概率界乘以正的样本空间大小 `v!` 后的精确整数形式；
不涉及浮点近似或未经论证的概率公式。
均衡红位置集合的存在性由 `Finset.exists_subset_card_eq` 给出，大小为 `v/2`。
`balanced_count_strict` 仅对十个整数 `v=9,…,18` 验证32倍上界严格小于 `v!`。
所有超图均由同一个解析计数与union bound定理覆盖，没有枚举超图、染色或排列。

## 已完成的接口

| 定理 | 结论 |
|---|---|
| `propertyB_nine_to_eighteen` | 对任意9–18点五元超图，边数≤32即有Property B |
| `propertyB_of_vertices_le_eighteen` | 结合已证明的≤8点分支，覆盖全部≤18点对象；不要求点对覆盖 |
| `exists_nineteen_to_twenty_five_counterexample` | 任意有限原反例产生19–25点、恰32边且覆盖全部点对的反例 |
| `target_of_finite_goal` | 只以规范F的七类全称命题为输入，推出原 `Target.{u}`；不再有small-cases输入 |
| `target_iff_finite_goal` | 原 `Target.{u}` 与 `FiniteGoal` 双向等价；正向用 `ULift` 处理任意宇宙层级，反向用已闭合约化 |

`FiniteGoal` 只是与 `FORMAL_SPEC.md` F 完全相同的命题定义，仍未单独证明。
两者等价不意味着任一者已经成立。尚存工作集中在19–25点有限对象的结构覆盖、
贪心条件概率、link删除与NUM数值的连接，不再是一般有限对象到该范围的约化。

## 编译证据

从 `formal/` 运行：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build Aris4Math.SmallVertices
```

最终新模块编译4.7秒。八项定理均做了 `#print axioms`：
`balanced_count_strict` 仅依赖 `propext`；其余仅依赖
`propext`、`Classical.choice`、`Quot.sound`。
源码无 `sorry`、`admit`、新公理或 `native_decide`。
十个标量不等式用 `interval_cases` 与内核可检查的 `decide`，
没有把外部计算结果导入为公理。
版本继续固定为 Lean 4.24.0/Mathlib v4.24.0。
