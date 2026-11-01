# 有限反例约化的 Lean 进度

2026-10-06。`Reduction.lean` 已编译通过，源码冻结供语义审阅。
**本轮证明了原对象的重标、合并、最小反例点对覆盖、少点数分支及补边步骤；
没有将尚未完成的有限分支冒充主定理 T 的无条件证明。**

源文件：[formal/Aris4Math/Reduction.lean](../formal/Aris4Math/Reduction.lean)。
成功日志：[lean-reduction-build.log](../.aris/traces/proof-checker/2026-10-06_run05/lean-reduction-build.log)。

## 已闭合的数学步骤

1. **一般映射接口。** `pushforward` 将每条边取像，再去除重复的像边。
   假定的只是映射在每条边上单射；由此证明每条像边仍有五点、不同边数不增加。
   `red_count_image` 证明拉回布尔染色时每条边的红点数完全相同，
   `propertyB_pullback` 据此证明像超图可染则原超图可染。
2. **任意有限顶点类型到 `Fin v`。** `relabel` 沿任意类型等价重标，
   `relabel_edge_count` 保持边数，`propertyB_relabel_iff` 给出 Property B 双向等价。
   `toFin` 用 `Fintype.equivFin` 取 `v=Fintype.card V`，保留孤立点。
   `target_of_fin_cases` 将全部 `Fin v` 情形接回原 `Target.{u}`；
   其结论没有增加顶点数、点对覆盖或颜色平衡假设。
3. **不共边顶点的合并。** `mergeVertex x y` 将 `y` 映到 `x`，其余顶点保持身份，
   值域为删除 `y` 后的 subtype。不共边条件被用于证明该映射在每条边上单射，
   不是直接假定合并结果五元。顶点数严格下降、去重后边数不增、染色可拉回。
   `smaller_counterexample_of_uncovered_pair` 因而构造更小的不可染简单五元超图。
4. **真实的最小反例。** `exists_minimal_counterexample` 对所有边数至多32的
   `Fin v` 反例应用 `Nat.find`，证明其余更小顶点数的同范围对象全部可染。
   `minimal_counterexample_pair_covering` 将上述合并构造与最小性矛盾，推出点对覆盖。
   `exists_pair_covering_counterexample` 从任意有限原反例得到该结论，
   没有先把点对覆盖加进原假设，也不使用文献基准 B0。
5. **原点集补至32边。** `exists_extension_32` 对 `v≥8` 使用所有五元子集作为有限候选集，
   由 `choose v 5 ≥ choose 8 5 = 56 ≥32` 及中间基数子集存在定理构造扩张。
   `exists_pair_covering_extension_32` 证明加边保持不可染和点对覆盖。
6. **`v≤8`。** `propertyB_of_vertices_le_eight` 把位置小于4的点染红、其余染蓝。
   通过两个到四元素集的单射，证明两类各至多4点；每条五元边因此有1至4个红点。
   这是一般有限集计数证明，不是超图抽样。
7. **接入 `v≤25`。** 引入 `Structure.lean` 中从真实度数/共度双计数证明的
   `H.card_le_twenty_five`，将以上步骤接成 `exists_finite_counterexample`。

目前已无条件证明的反例约化为：

\[
\text{任意有限简单五元 }H,\ |E(H)|\le32,\ \neg PB(H)
\Longrightarrow
\exists v\in\{9,\ldots,25\},\ \exists K\text{ on }\mathrm{Fin}\,v,
\quad |E(K)|=32,\quad\neg PB(K),\quad K\text{覆盖所有点对}.
\]

这里的9点下端是当前已经形式化的范围。纸面规格中的19点下端仍需9–18点的
均衡染色概率论证；没有悄悄把规格改成9–25点。

## 最终装配接口及其未消除输入

`target_of_nineteen_to_twenty_five` 的结论是原 `Aris4Math.Target.{u}`，
但它**仍是两个明确输入的蕴含定理**：

- 所有9–18点、边数至多32的五元超图可染。
- 所有19–25点、恰32边且点对覆盖的五元超图可染。

这些正是尚待其他证明模块接入的具体数学义务。该接口不是无条件 T，
没有用隐藏的 certificate、额外公理或 `sorry` 把输入当成已成立。
9–18点分支需完成一般计数及对应严格不等式；19–25点分支还需结构覆盖、
条件排列权重、删除修正和 NUM 数值的完整语义拼接。

## 编译与信任记录

从 `formal/` 运行：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build Aris4Math.Reduction
```

最终新模块编译4.4秒；19项关键定理的 `#print axioms` 均仅为
`propext`、`Classical.choice`、`Quot.sound`。
源码不含 `sorry`、`admit`、新增公理或 `native_decide`。
`choose 8 5 = 56` 用内核可检查的 `decide`，不是原生编译结果公理。
继续沿用固定 Lean 4.24.0/Mathlib v4.24.0。

单个合并计数接口使用 `DecidableEq` 以便表示删除顶点的有限类型；最终
`target_of_fin_cases` 和 `target_of_nineteen_to_twenty_five` 的目标仍是任意
`Fintype V` 上的原 `Target`，没有将可判定相等性加入其数学假设。
