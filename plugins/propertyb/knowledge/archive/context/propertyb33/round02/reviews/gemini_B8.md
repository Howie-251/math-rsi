### 24点分支阶段 B 代码与命题对齐对抗式审阅报告

---

### 一、顶层定理反译与最终谓词真实性

#### 1. 顶层入口反译
在 [`TwentyFourComplete.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFourComplete.lean) 中，导出的主定理为：
```lean
theorem twenty_four_propertyB (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) : PropertyB H
```
- **输入对象**：任意定义在有限基集 `Fin 24` 上的五元简单超图 $H$（每条边严格恰含5点，无重边）。
- **显式前提**：
  1. `cover : H.PairCovering`：$\forall x \ne y, \exists e \in H.edges, x \in e \wedge y \in e$（点对完全覆盖）。
  2. `edges33 : H.edges.card = 33`：超边数恰好为 33。
- **输出结论**：`PropertyB H`。
- **原始定义核对**：[`Aris4Math.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L31-L34) 中 `PropertyB H` 定义为：
  $$\exists c : V \to \text{Bool}, \forall e \in H.edges, 1 \le |\{x \in e : c(x) = \text{true}\}| \le 4$$
- **核查结论**：
  - 顶层定理**完全不含**任何局部剖面、锁点存在性、概率上界证书、非空坏槽或结构性附带前提；
  - 没有任何形式的空域旁路（vacuous truth）或公理逃逸；
  - 结论是原汁原味的二染色存在性，与原题规格 [`FORMAL_SPEC_PROPERTYB_33.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md) 中的 $F33(v=24)$ 严格对齐。

---

### 二、逐层架构与实际对象连接攻击

```
twenty_four_propertyB (Fin 24, cover, edges=33)
  ├── TwentyFourLowComplete (propertyB_or_matching_or_mixed)
  │     ├── TwentyFourSelection (2r+t≥27: r≥5 ∨ t≥19)
  │     └── TwentyFourQuadRedirect (selected_of_twenty_four)
  │           ├── TwentyFourFourLow (4 unit 6-locks, all pairs)
  │           ├── TwentyFourTripleLow (4 unit 6-locks, 1 triple)
  │           └── TwentyFourFullFive (full 5-lock edge, ≤1 bad pair)
  ├── TwentyFourFiveMatchingComplete (5 matching 6-locks)
  │     ├── TwentyFourMatchingHighCatalog (65536 Boolean vectors → 51 families → 18 orbits)
  │     └── TwentyFourFiveMatching (propertyB_of_large)
  └── TwentyFourMixed (2 low 6-locks, 3 high 7-locks)
        ├── TwentyFourUniqueBadPair (arms Ax, Bx, Ay, By)
        ├── ActualBadSlot (two real bad slots chosen BEFORE positions)
        ├── RefinedDeletion (dualPenalty = excess / 2 on all incident pairs)
        └── CustomDeletion (propertyB_of_custom_deletion)
```

#### 1. 全称分支覆盖完整性（无遗漏图结构）
- **度数预算**：由点对覆盖，$\forall x, d(x) \ge \lceil 23/4 \rceil = 6$。总度 $\sum d(x) = 5 \times 33 = 165$。
  [`TwentyFourSelection.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFourSelection.lean#L33-L58) 证明 `six_seven_budget`: $27 \le 2r + t$。若六度点数 $r \le 4$，则七度点数 $t \ge 27 - 8 = 19$。因此无条件二分：$r \ge 5$ 或 $t \ge 19$。
- **$r \ge 5$ 子分支覆盖**：
  - 由六度点共度超额 $\le 1$，度数6点诱导的非单位图最大度 $\le 1$（必为匹配）。
  - `four_unit_or_five_matching` 证明：任意5个六度点中，要么存在4个两两单位共度点，要么其非单位图恰为两条不相交匹配边（`FiveMatchingLocks`）。
  - 对具有4个单位六度锁点 $S$ 的情形，`TwentyFourQuadRedirect.lean` 证明：
    1. 若四锁迹全是 pair，进入 `TwentyFourFourLow`；
    2. 若含 1 个 triple，进入 `TwentyFourTripleLow`；
    3. 若含 4 点全迹 $S \subset E$：
       - 若外部还有其他六度点 $z \notin E$，因 $z$ 至多1个非单位邻居，在 $S$ 中可选出3个与 $z$ 单位共度的点，重构出含真实 triple 迹的新四锁（`TripleLocks`）；
       - 若外部无六度点，则所有六度点全在 $E$ 内，由 $|E|=5$ 迫使 $E$ 就是全体六度点，且 $S \subset E$ 保证内部至多一对共度2，进入 `FullFiveLocks`。
- **$t \ge 19$（包含 $t \ge 18$）子分支覆盖**：
  - 由 $r \ge 3$ 取两个相互单位共度的六度点 $x, y$；通过 `TwentyFourUniqueBadPair.lean` 构造各自唯一坏对的臂 $A_x, B_x$ 与 $A_y, B_y$（各至多3点）；
  - 在 $\ge 18$ 个七度点中排除坏邻居与臂交叉乘积，通过 `exists_unit_pair_avoiding_crosses` 严格选出3个两两单位共度且与 $x,y$ 单位共度的七度点 $z, u, v$，且保证 $x, y$ 的每个坏边对各有一条边避开 $\{z, u, v\}$，进入 `MixedLocks`。
- **结论**：**分支覆盖严密闭合，不存在未处理的中间图或悬空条件。**

---

#### 2. Matching 高迹 Boolean 覆盖、置换方向与代表绑定
在 [`TwentyFourMatchingHighCatalog.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFourMatchingHighCatalog.lean) 与 [`TwentyFourFiveMatchingComplete.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFourFiveMatchingComplete.lean) 中：
- **Boolean 映射的保真性**：
  五锁上大小 $\ge 3$ 的子集共有 16 个。因非单位对仅为 $\{0,1\}$ 和 $\{2,3\}$，任意 $\ge 3$ 点子集均包含至少一个单位对（`large_has_unit_pair` 由内核常算完成），故其在 $H$ 中的真实迹重数至多为 1（`large_count_le_one`）。因此用 `actualBits : Fin 16 → Bool` 表达真实高迹重数是完全严格等价的，没有截断误差。
- **全称覆盖无死角**：
  `covers_vector` 与 `covers` 对所有 $2^{16} = 65536$ 个 Boolean 分配向量进行内核检查，证明只要满足对偶点对预算（`FastAdmissible`，由真实的超边剖面求和不等式严格推出），必落在 51 个有标号族之中。
- **置换方向与代表绑定**：
  在 `representatives` 中，每个有标号族 $s \in \text{Fin } 51$ 关联一个置换 $\sigma$ 和代表索引 $k \in \text{Fin } 18$：
  $$\text{highValue}(\text{catalog } s)(T.\text{image } \sigma) = \text{counts } k\ T$$
  在 [`TwentyFourFiveMatchingComplete.lean` L117-L124](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFourFiveMatchingComplete.lean#L117-L124) 中，定义新锁点映射为 `newVertices = σ.toEmbedding.trans vertices`。
  根据 `count_relabel`：
  $$\text{count } H\ \text{newVertices } T = \text{count } H\ \text{vertices } (T.\text{image } \sigma) = \text{counts } k\ T$$
  且 $\sigma$ 保持了 matching 的共度定义：$\text{pairDegree}(\sigma i, \sigma j) = \text{pairDegree}(i, j)$。
- **结论**：**置换方向正确，真实超图 count 准确无误地代入了 18 个数值代表，没有发生标签颠倒或同构伪证。**

---

#### 3. 混合 32 型与两实际坏槽 $\to$ 自适应位置的顺序和回接
在 [`TwentyFourMixed.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFourMixed.lean) 中：
- **量词与选择次序核查**：
  1. 首先由 $H$ 和已选五锁确定局部的 32 族之一 $t : \text{Fin } 32$（`actual_classification`，L99）；
  2. 然后针对两个六度中心 $j \in \{0, 1\}$，由 $H$ 的实际点对覆盖和度数 6 确定各自存在的真实坏边对（`link_bad_pair_lower_bound` 保证坏边对非空），并在位置确定前确定其实际坏槽索引 $b_0, b_1 : \text{Fin } 8$（`actual_low_slot`，L100-L101）；
  3. 随后以 $(t, b_0, b_1)$ 为键，通过完全确定的选择函数取行索引 $r = \text{choice } t\ (b\ 0)\ (b\ 1)$，得到具体配置 $c = \text{configOf } r$（L102-L103）；
  4. 配置 $c$ 提供了固定的锁点排列位置 `positions c`。在此固定位置下，坏槽双向记账权重下界（`slotWeight`）和高中心/基线中心的对偶下界（`dualLoss`）联合构成了 `loss r`。
- **回接严密性**：
  - 位置选择是在固定坏边对槽之后执行的确定性查找；
  - 随机置换发生在位置固定之后（作为条件置换事件）；
  - `strict r` 由内核计算保证严格小于 1，直接驱动 `CustomDeletion.propertyB_of_custom_deletion`。
- **结论**：**不存在“先随机再选位置”的颠倒，也不依赖槽类型与位置之间的独立性假设，自适应查找表与超图事实完全闭合。**

---

#### 4. 重叠配额 Dual 各半双向罚项与无多扣（Over-deduction Attack）
在 [`RefinedDeletion.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/RefinedDeletion.lean) 中：
- **惩罚项定义**：
  ```lean
  def dualPenalty (P : ι → Finset (Finset V)) (a : ι → ℚ)
      (w : Finset V × Finset V → ℚ) (z : Finset V × Finset V) : ℚ :=
    max 0 (quotaWeight P a {z.1, z.2} - (w z + w (z.2, z.1))) / 2
  ```
- **代数展开核验**：
  对无序边对 $p = \{e, f\}$（$e \ne f$），其在两个有序方向上的记账权重和为 $w(e, f) + w(f, e)$。
  多重重叠配额在该无序对上要求的权重为 $\text{quotaWeight} = \sum_{i: p \subseteq P_i} a_i$。
  超出部分为 $\text{excess} = \max(0, \text{quotaWeight} - (w(e, f) + w(f, e)))$。
  在有序对 $(e, f)$ 上罚项定义为 $\text{excess} / 2$，在 $(f, e)$ 上同样为 $\text{excess} / 2$。
  两方向之和恰好为 $\text{excess}$，**无多扣（各半双向加和恰为单倍无序超额）**。
- **求和范围与下界方向**：
  在定理 `dual_bad_weight_lower`（L45-L72）中：
  $$\sum_i q_i a_i - \sum_{z \in (H.\text{incidentEdges } x).\text{offDiag}} \text{dualPenalty}(z) \le \sum_{z \in \text{directedBadPairs } H x} w(z)$$
  - 左侧将罚项求和扩大到了中心 $x$ 的**所有**关联边有序对（而不仅是坏对），因 $\text{dualPenalty} \ge 0$，这一步使减数更大，得到的下界更加保守安全；
  - 转化为剖面表格后，`penaltySum`（L172-L176）中的容量系数为 $t.count \times (u.count - [t=u])$，精确等于两迹实际超边构成的有序对总数。
- **结论**：**代数方向正确，对偶惩罚完全守恒，不存在多重扣除或正负号颠倒漏洞。**

---

### 三、证据链与构建状态区分

1. **直接编译与传递公理（已实证）**：
   - 查看 [`direct-compile.log`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round02/twentyfour-complete/direct-compile.log)：
     ```
     'Aris4Math.ThirtyThree.twenty_four_propertyB' depends on axioms: [propext, Classical.choice, Quot.sound]
     ```
   - 本地源码全链路核查确认：24点装配定理及其所有依赖子分支（LowComplete、Selection、QuadRedirect、FourLow、TripleLow、FullFive、FiveMatchingComplete、Mixed）**顶层均为零 `sorry`，零额外公理**。
2. **Lake 构建状态区分**：
   - 依据工程记录，全局 `lake build` 在目录合并时部分下游日志尚在在途状态；
   - 本次审阅严格基于**源码静态语义核查**与已落盘的标准直接编译日志，不将“在途构建”预先宣称为全局 CI 最终通过。
3. **顶层 Target 状态界定**：
   - 查看 [`Assembly.lean` L21-L24, L56-L61](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Assembly.lean#L21-L24)：
     `RemainingGoal` 当前已被严格压缩为仅剩 23 点：
     ```lean
     def RemainingGoal : Prop :=
       ∀ H : Simple5Hypergraph (Fin 23), H.edges.card = 33 → H.PairCovering → PropertyB H
     ```
   - `target_iff_remaining_goal` 证明了 `Target33 ↔ RemainingGoal`。
   - **绝不宣称 T33 或 Target33 已经全部完成。23 点仍是待闭合的实质前提。**

---

### 四、审阅结论

在当前设定的核心审查范围内：
- [`TwentyFourComplete.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFourComplete.lean) 及逐层调用的全部关联源码，**未发现逻辑漏洞、量词颠倒、代表错配、多重扣除或未闭合命题**；
- 24 点分支的数学架构与形式化实现严密对应，成功从原始简单超图条件推导出标准的 `PropertyB H`。
