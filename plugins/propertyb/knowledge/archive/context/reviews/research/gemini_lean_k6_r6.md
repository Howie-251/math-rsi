### 1. 审阅范围与核心结论

本次针对以下文件进行只读审阅：
- [BlockClassification.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean)
- [K6Classification.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean)
- [K6Traces.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean)
- [Traces.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Traces.lean) / [Avoidance.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Avoidance.lean) / [SevenPoint.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/SevenPoint.lean) / [Structure.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Structure.lean)
- [proofs/STRUCTURE_24_25.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_24_25.md)

**审阅结论：未发现数学漏洞、漏分类别、二元块恢复失真、标号方向/顺序错位或循环/假设增强。**
所审阅模块的数学范围与命题保真度成立：
1. **全部分类完备**：六点上任意大小 $\le 5$、两两交至多 $1$ 的块族的大块族（大小 $\ge 3$）严格落入给出的 9 个代表之一；
2. **二元块精确恢复**：基于单共度（UnitCodegrees）与点对覆盖，未被大块覆盖的点对唯一且全部恢复为二元块；
3. **同构映射为真双射**：通过关联上纤维的莫比乌斯反演构造出真实点集双射（`Equiv`），标号方向与锁定顶点定义完全一致；
4. **顶层定理无未证假设**：[`exists_full_labeled_six_good_locks`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L174-L185) 仅依赖标准假设（$V$ 为有限集、5-uniform 超图 $H$、点对覆盖、32 条边、25 个顶点），无任何未证的剖面假定或分类公理；
5. **七点避坏引理严格排除 $k=2,3$**：整数双计数矛盾 $4t = 14$ 仅依赖“删点后剩余三元块个数恒为 2”，对两三元块“相交 1 点”或“不交”不作区分，因此合法且必然同时排除 $k=2$ 与 $k=3$。

---

### 2. 数学范围与命题保真度逐项核验

#### 2.1 六点块族（大小 $\le 5$，交至多 1）的完备分类
在 [BlockClassification.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean) 与 [K6Classification.lean](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean) 中，对于 $|W| = 6$ 的基集，设大块族为 $L = \{B \in \text{blocks} : 3 \le |B|\}$：

1. **存在 5 元块 $B$**（[`five_block_unique_large`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L35-L42)）：
   若存在 $C \ne B$ 且 $|C| \ge 3$，由容斥原理 $|B \cup C| + |B \cap C| = |B| + |C|$，有 $|B| + |C| \le |W| + 1 = 7$（[`two_block_sizes`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L24-L33)）。但 $|B| + |C| \ge 5 + 3 = 8 > 7$，导出矛盾。因此 5 元块唯一，且无其他大块。由于 6 点上的任意 5 元子集在点置换下同构，归入代表 $k=8$（即 `{0, 1, 2, 3, 5}`）。
2. **存在 4 元块 $B$，无 5 元块**（[`large_beside_four`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L126-L150), [`four_block_at_most_one_other`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L152-L166)）：
   若存在另一大块 $C \ne B$，则 $|C| \le 7 - 4 = 3$，故 $|C| = 3$。此外 $|C \setminus B| \ge 3 - 1 = 2$。因 $|W \setminus B| = 2$ 且 $C \setminus B \subseteq W \setminus B$，必有 $C \setminus B = W \setminus B$，从而 $W \setminus B \subseteq C$ 且 $|B \cap C| = 1$。若存在两个这样的大块 $C, D$，则 $W \setminus B \subseteq C \cap D \implies |C \cap D| \ge 2$，违反线性条件。故至多存在一个其他大块：
   - 无其他大块：仅一个 4 元块，归入代表 $k=6$（即 `{0, 1, 2, 5}`）；
   - 有一个其他大块：一个 4 元块和一个 3 元块交于 1 点，归入代表 $k=7$（即 `{0, 3, 4, 5}` 与 `{1, 2, 3}`，交点为 3）。
3. **最大块大小至多为 3（纯三元块族）**：
   - 顶点度数上界：任一点 $x$ 若属于 $m$ 个三元块，这些块在去掉 $x$ 后为 $W \setminus \{x\}$（5 个点）中的两两不交二元集。故 $m \le \lfloor 5 / 2 \rfloor = 2$（[`triple_degree_le_two`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L58-L90)）。
   - 三元块总数上界：$3t = \sum_{x \in W} \deg(x) \le 2 \times 6 = 12 \implies t \le 4$（[`triple_count_le_four`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L109-L122)）。
   - 不交三元块排他性（[`disjoint_triples_only`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L185-L208)）：若存在两块 $B, C$ 不交，则 $B \cup C = W$。任意第三块 $D$ 满足 $D \subseteq B \cup C \implies |D| \le |D \cap B| + |D \cap C| \le 1 + 1 = 2$，与 $|D| = 3$ 矛盾。故两不交三元块存在时，不可能有第三个三元块。
   - 由此，当 $t \ge 3$ 时，任意两块必交于 1 点（[`triple_intersection_eq_one`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L210-L224)）。
   - 分类分支（[`classify_triples`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L207-L233)）：
     - $t = 0$：空集，对应 $k=0$；
     - $t = 1$：单三元块，对应 $k=1$；
     - $t = 2$：交点数只可能为 0 或 1。交点为 1 归入 $k=2$；交点为 0 归入 $k=3$（[`label_two_triples`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L183-L204)）；
     - $t = 3$：3 块两两交于 1 点，顶点度数 $\le 2$ 迫使交点各不相同（无三重交点），且各有一私有点，同构唯一，归入 $k=4$（[`label_three_triples`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L158-L168)）；
     - $t = 4$：4 块两两交于 1 点，总度数 12，故每点度数恰为 2。这对应 $K_4$ 的边-点对偶，同构唯一，归入 $k=5$（[`label_four_triples`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L170-L180)）。

该分支树无遗漏，所有可能组合均被严格穷尽。

#### 2.2 二元块恢复与 Pair Completion
定义与定理见 [K6Classification.lean:32-72](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L32-L72) 及 [K6Traces.lean:109-136](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L109-L136)。
- `pairCompletion (large)` 将大块族与所有“未被任何大块包含的无序点对”取并。
- [`recover_pairs`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L42-L72) 证明：若 `blocks` 满足（1）块大小 $\ge 2$；（2）两两交至多 1；（3）覆盖所有点对，则 `blocks = pairCompletion (largeBlocks blocks)`。
  - 若 $P \in \text{blocks}$ 且 $|P| = 2$：若 $P \subseteq B$ 且 $|B| \ge 3$，则 $|P \cap B| = 2 > 1$，违反线性条件。故 $P$ 绝不可能被任何大块包含，必然属于 `filter (fun P => ∀ B ∈ large, ¬ P ⊆ B)`。
  - 反之，若点对 $P$ 未被任何大块包含：由点对覆盖，存在 $B \in \text{blocks}$ 覆盖 $P$。若 $|B| \ge 3$，与未被大块包含矛盾，故 $|B| \le 2$。又 $P \subseteq B \implies |B| = 2$ 且 $P = B \in \text{blocks}$。
- 超图映射 [`labeled_traces_recovered`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L109-L136)：在 $H$ 的 6 个锁定点 $W$ 上，由单共度条件，点对覆盖条件由超图边的存在性直接提供（`H.existsUnique_multiTrace_pair`）。因此，实际超图的全部多点截面 `H.multiTraces W` 经标号后恰好等于 `fullRepresentative k`。

#### 2.3 标号等价性与方向保真度
- **对偶关联同构**（[BlockClassification.lean:226-363](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L226-L363)）：
  定理 [`exists_equiv_of_incidence_data`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L282-L316) 证明：当超图中每个顶点的块度数（signature）至多为 2 时，所有基数 $\ge 3$ 的上纤维均为 $\emptyset$。因此，各精确纤维（Exact Fibers）的基数完全由顶点总数（空集纤维和）、单块大小（单元素上纤维）以及两两块交大小（双元素上纤维）经向下莫比乌斯反演决定。
  两组具有相同块大小和两两交大小的块系统，其精确纤维基数处处相等。通过 [`Equiv.ofFiberEquiv`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L275) 拼接各纤维上的局部双射，得到真实的基集双射 $e : \alpha \simeq \beta$。
- **标号方向与语义**（[K6Traces.lean:80-90](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L80-L90)）：
  - 映射定义：`labelBlock W label B := (onGround W B).map label.toEmbedding`，其中 `label : ↥W ≃ Fin 6`。
  - 成员性质：`i ∈ labelBlock W label B ↔ (label.symm i).val ∈ B`（[`mem_labelBlock`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L83-L86)）。
  - 对应关系：标号 $i \in \{0,\dots,5\}$ 所对应的超图顶点即为 `(label.symm i).val`。若代表块包含 $i$，则其实际超图截面包含该锁定顶点。方向与纸面证明中“顶点 $x \in W$ 赋予标号 $f(x)$，标号 $i$ 对应顶点 $f^{-1}(i)$”完全一致，无反向或错位。

#### 2.4 [`exists_full_labeled_six_good_locks`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L174-L185) 的假设闭合性
检查该定理的定义签名与前提：
```lean
theorem exists_full_labeled_six_good_locks [Fintype V] (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (vertices25 : Fintype.card V = 25) :
    ∃ W : Finset V, W.card = 6 ∧ (∀ x ∈ W, H.degree x = 6) ∧ H.UnitCodegrees W ∧
      ∃ k : Fin 9, k ≠ 2 ∧ k ≠ 3 ∧ ∃ label : ↥W ≃ Fin 6,
        (H.multiTraces W).image (labelBlock W label) = fullRepresentative k
```
- 依赖链：
  1. [`Structure.exists_seven_six_degree_codegree_one`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Structure.lean#L289-L303)：利用 $v=25$ 时总度数 $160 \implies$ 六度点数 $r \ge 15$，且每个六度点与其余 24 点共度均为 1（由 $\sum_{y \ne x} \lambda_{xy} = 24$ 且 $\lambda \ge 1$ 推出等号）。由此选出 7 个相互共度为 1 的六度点。
  2. [`Avoidance.exists_deletion_not_two_triple_shape`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Avoidance.lean#L72-L93)：在这 7 个点中，必存在一个点的删点截面不满足 `TwoTripleShape`。
  3. [`Traces.exists_six_good_locks`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Traces.lean#L430-L446)：将此删点限制在超图上，得到 6 个六度点，相互共度为 1，且多点截面非 `TwoTripleShape`。
  4. [`classify_good_six`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L317-L324)：在 6 点上应用纯解析分类，直接得出 $k \ne 2 \land k \ne 3$ 以及同构标号映射。
  5. [`labeled_traces_recovered`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L109-L136)：由共度 1 与覆盖性将大块同构提升到全代表 `fullRepresentative k`。
- 全链条中无任何 `sorry`，亦无对 $H$ 添加额外关于交型、正则性或未锁定点结构的主观强假设。

---

### 3. 具体代表的有限检查 vs 任意输入族的解析分类

审阅中明确区分了两类不同的证明性质：
1. **具体代表的有限检查（Exact Finite Checks on Displayed Representatives）**：
   在 [K6Classification.lean:163-166](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L163-L166) 及 [175-178](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L175-L178) 中出现的 `by decide`：
   ```lean
   have small : ∀ x, (signature C x).card ≤ 2 := by decide
   have singles : ∀ i, (C i).card = 3 := by decide
   have pairs : ∀ i j, i ≠ j → (C i ∩ C j).card = 1 := by decide
   have labels : Finset.univ.image C = representative 4 := by decide
   ```
   这些有限检查**仅作用于显式写出的具体参考常数**（如 $C = ![\{0,3,4\}, \{1,2,3\}, \{1,4,5\}]$）。它们的作用是让 Lean 内核验证“该给定的参考数组确实满足块大小为 3、两两交大小为 1、顶点度数 $\le 2$”。这完全属于静态常数项求值，不涉及任何输入族的枚举。
2. **所有输入块族的解析分类（Analytic Classification of All Input Families）**：
   对任意抽象超图诱导的块族 `blocks`，证明从不遍历或枚举 6 点上的 $2^{\binom{6}{2}} = 32768$ 个图或 352 个有标号分解。相反，证明纯粹基于：
   - 容斥不等式（两块大小之和 $\le 7$）；
   - 关联双计数（点度数 $\le 2 \implies 3t \le 12 \implies t \le 4$）；
   - 几何排他性（两不交三元块覆盖全部 6 点，迫使其余块大小 $\le 2$）；
   - 关联上纤维的反演定理（当顶点度数 $\le 2$ 时，两两交大小完全决定同构型）。

由此，输入族的分类是**纯解析推导**，而 `decide` 仅用于为同构定理的目标端提供经过验证的基准参考点。

---

### 4. 七点避坏引理与排除两个双三元块型（$k=2,3$）的独立推导

#### 4.1 双计数矛盾推导
设 $W$ 为 7 个两两共度为 1 的顶点构成的集合。
超图截面中大小 $\ge 2$ 的块构成的族记为 $\mathcal{D}_W$。
1. **大块（大小 $\ge 4$）的排除**（[Avoidance.lean:21-43](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Avoidance.lean#L21-L43)）：
   若 $\mathcal{D}_W$ 中存在块 $B$ 使得 $|B| \ge 4$，因为 $|B| \le 5 < 7 = |W|$，必存在顶点 $u \in W \setminus B$。
   当删去顶点 $u$ 时，$B$ 不含 $u$，故在 $W \setminus \{u\}$ 的截面中原样保留，从而 $W \setminus \{u\}$ 包含一个大小 $\ge 4$ 的块。
   若假定每个删点截面都不含大小 $\ge 4$ 的块，则 $\mathcal{D}_W$ 中从一开始就不能有大小 $\ge 4$ 的块。因此 $\mathcal{D}_W$ 中的块只能为二元块或三元块。
2. **删点与三元块数**（[Avoidance.lean:46-68](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Avoidance.lean#L46-L68)）：
   由于不存在 4 元或 5 元块，删去 $u$ 时不可能有更大的块降级为新的三元块。
   因此，删去 $u$ 后保留的三元块，**恰好是原三元块族中不包含 $u$ 的那些块**。
3. **整数矛盾**（[SevenPoint.lean:29-54](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/SevenPoint.lean#L29-L54)）：
   设 $\mathcal{D}_W$ 中三元块总数为 $t$，点 $u$ 所属的三元块数为 $r_u$。删去 $u$ 后剩余的三元块数为 $t - r_u$。
   若假设对所有 7 个顶点 $u \in W$，删去 $u$ 后的截面**都恰好包含 2 个三元块**：
   $$
   t - r_u = 2 \qquad (\forall u \in W).
   $$
   对全部 7 个点求和：
   $$
   \sum_{u \in W} (t - r_u) = 7 \times 2 = 14.
   $$
   另一方面，由于每个三元块恰含 3 个顶点，$\sum_{u \in W} r_u = 3t$。因此：
   $$
   \sum_{u \in W} (t - r_u) = 7t - \sum_{u \in W} r_u = 7t - 3t = 4t.
   $$
   两式联立得出：
   $$
   4t = 14 \implies t = \frac{7}{2} \notin \mathbb{Z},
   $$
   产生整数矛盾。因此，不可能对所有 7 个删点都留下恰好 2 个三元块。

#### 4.2 为什么能够合法且同时排除 $k=2$ 与 $k=3$
对比纸面原表与形式化定义：
- 在纸面 9 型列表（[proofs/STRUCTURE_24_25.md:164-173](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_24_25.md#L164-L173)）中：
  - K6-3（0-based 索引 $k=2$）：2 个三元块，交于 1 点（例如 $145, 234$），数值上界为 $8297/8398 < 1$；
  - K6-4（0-based 索引 $k=3$）：2 个三元块，两两不交（例如 $156, 234$），数值上界为 $8405/8398 > 1$。
- 纸面原注记仅强调“避开 K6-4”，是因为 K6-4 的原始上界大于 1，必须排除；而 K6-3 的上界小于 1，原本被视为可接受型。
- 然而，在形式化定义中：
  ```lean
  def TwoTripleShape (blocks : Finset (Finset α)) : Prop :=
    (∀ B ∈ blocks, B.card ≤ 3) ∧ (blocks.filter (fun B => B.card = 3)).card = 2
  ```
  `TwoTripleShape` 的定义**只约束“无 4 元以上块且三元块数恰为 2”**，完全不限制这两个三元块是“相交 1 点”还是“不交”。
- 关键在于：上述双计数等式 $\sum (t - r_u) = 4t = 14$ 的推导，**完全不需要知道这两个三元块是否相交**。只要某个删点截面的大块形态是“恰好两个三元块（其余为二元块）”，无论它是 $k=2$ 还是 $k=3$，它都满足 `TwoTripleShape`。
- 如果 7 个删点截面全部落在 $\{k=2, k=3\}$ 之内，则它们每一个都满足 `TwoTripleShape`，立即导出 $4t = 14$ 的矛盾。
- 因此，7 个删点中**至少存在一个删点既不是 $k=2$ 也不是 $k=3$**。
- 这在数学上是完全合法的强结论（Stronger Elimination）：
  因为主定理只需要存在**至少一个**可染或满足概率界 $< 1$ 的锁定截面。既然 7 点中必然存在一个属于 $\{0, 1, 4, 5, 6, 7, 8\}$ 的截面，那么下游的概率检查只需要覆盖这 7 个型即可；无需把 $k=2$ 纳入必须适配的分支，也更无需顾虑 $k=3$。

---

### 5. 审查确认清单（Checklist）

| 审查项 | 结论 | 证据位置与事实支持 |
|---|---|---|
| **是否存在遗漏块族** | 否 | [BlockClassification.lean:35-224](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L35-L224)，按最大块大小（5, 4, $\le 3$）与三角形数（0..4）完全闭合 |
| **二元块恢复是否有效** | 是 | [K6Classification.lean:42-72](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L42-L72) [`recover_pairs`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Classification.lean#L42)，单共度保证二元截面互不包含且覆盖全部未涉点对 |
| **标号方向/顺序是否错位** | 否 | [K6Traces.lean:80-86](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L80-L86) [`mem_labelBlock`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L83)，$i \in labelBlock \leftrightarrow (label.symm\ i).val \in B$，点与标号双射一一对齐 |
| **是否存在循环论证或假设增强** | 否 | [`exists_full_labeled_six_good_locks`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K6Traces.lean#L174) 纯粹由 $H$ 的 25 点、32 边、点对覆盖推导，无任何外部公理或剖面假定 |
| **静态有限检查 vs 任意族分类** | 已严格区分 | `decide` 仅用于验证参考常数 $C$ 的基数；任意输入族通过莫比乌斯反演同构定理 [`exists_equiv_of_incidence_data`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/BlockClassification.lean#L282) 进行解析判定 |
| **同时排除 $k=2,3$ 是否成立** | 是 | $4t = 14$ 整数矛盾对两三元块的相交状态无感，必然同时避开 $k=2$ 与 $k=3$，下游仅需处理 7 个型 |

