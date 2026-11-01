# 实际超图结构：Lean 已证明的部分

`formal/Aris4Math/Structure.lean` 已从原始 `Simple5Hypergraph V` 的有限边集出发，
证明度数/共度双计数、顶点数上界，以及 24、25 点分支所需的锁点存在性。
没有把度数恒等式作为额外前提，也没有穷举候选超图或局部块族。

正式定义和定理位于 `Aris4Math.Simple5Hypergraph` 命名空间。

## 已连接到实际超图的结论

| 定理 | 结论 |
|---|---|
| `sum_degrees` | Σ_x degree(x) = 5·|E| |
| `sum_codegrees_erase` | Σ_{y≠x} codegree(x,y) = 4·degree(x) |
| `one_le_codegree` | 点对覆盖给出不同点的实际共度至少 1 |
| `pairCovering_degree_bound` | 点对覆盖 ⇒ |V|−1 ≤ 4·degree(x) |
| `card_le_twenty_five` | 点对覆盖且 |E|≤32 ⇒ |V|≤25 |
| `sum_degrees_eq_160` | |E|=32 ⇒ 实际总度数 160 |
| `sixVertices_budget` | 最小度≥6 且 |E|=32 ⇒ 7|V|≤160+六度点数 |
| `sixVertices_card_ge_eight` | 24 点、32 边、点对覆盖 ⇒ 至少 8 个六度点 |
| `sixVertices_card_ge_fifteen` | 25 点、32 边、点对覆盖 ⇒ 至少 15 个六度点 |
| `codegree_eq_one_of_twenty_five` | 25 点六度点与每个不同点的共度恰为 1 |
| `sum_codegree_excess` | 点对覆盖时，共度减一的总和为 4·degree(x)−(|V|−1) |
| `badPartners_card_le_one_of_twenty_four` | 24 点六度点至多有一个共度≥2的伙伴 |
| `exists_pairwise_avoiding_subset` | 对称关系中每点至多一个不同伙伴，2k个点可选k个两两不相关点 |
| `exists_four_six_degree_codegree_one` | **24 点分支可选 4 个六度点，任意不同两点共度恰为 1** |
| `exists_seven_six_degree_codegree_one` | **25 点分支可选 7 个六度点，任意不同两点共度恰为 1** |

另有 `codegree_comm` 和 `badPartners_card_le_excess` 两个通用辅助定理，共 17 个定理。

`degree` 与 `codegree` 的定义是对 H.edges 过滤后取有限集基数。
`PairCovering H` 是对任意不同顶点 x、y，存在 H 的一条边同时包含它们。
后续最小反例约化可导入本模块，使用这些定义和 `card_le_twenty_five`。
本模块不导入 Reduction，避免依赖环。

## 解析证明路线

双计数交换实际有限求和的次序；每条五元边给总度数贡献 5，
每条经过 x 的边给 x 的其他共度贡献 4。
点对覆盖给每个不同点至少一份共度，由此得到最小度与总顶点数约束。

24/25 点的六度点数来自逐点不等式
`7 ≤ degree(x) + indicator(degree(x)=6)`。
其最小度 6 已由点对覆盖和顶点数推导，未加入原命题。
25 点六度点的 24 份共度和，恰好分给 24 个各需至少一份的点，所以每份只能为 1。

24 点六度点的共度超额总和为 1，因此至多一个坏伙伴。
四点选择使用关于 k 的一般归纳：选一个点，删掉它及至多一个坏伙伴，
在余下集合继续选 k−1 个点。这是有限集上的一般构造性论证，
没有枚举四点子集、独立集、图或超图。

25 点从至少 15 个六度点中选取 7 个，利用已证明的六度点刚性即可。
K4/K6 分类、截面块族及七点避坏型属于接下来的结构连接，本模块没有把这些当成已证明。

## 核验与复现

```sh
export ELAN_HOME="$PWD/.tools/elan"
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build Aris4Math.Structure
```

已真实编译成功，Lean 日志报告本模块构建耗时 5.7 秒。
随后从生成的 olean 导入，对全部 17 个定理执行 `#print axioms`：
公理依赖不超出 `propext`、`Classical.choice`、`Quot.sound`，没有 `sorryAx` 或新公理。

证据在 `.aris/traces/proof-checker/2026-10-06_run05/lean-structure-build.log`、
`lean-structure-build.meta.json`、`lean-structure-axioms.lean` 和 `lean-structure-axioms.log`。

原始 `Aris4Math.Target` 仍待所有概率、类型分类和选择分支连接完成。
本模块给出的是已接到真实超图定义的结构部分，不单独声称完成主定理。
