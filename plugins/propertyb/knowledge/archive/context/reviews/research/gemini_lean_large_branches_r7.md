### 1. 审阅范围与核心结论

本次对抗性审阅针对最新接入的 $v=24$ 与 $v=25$ 形式化闭合分支：
- 入口声明：[`LargeVertices.twenty_four_propertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/LargeVertices.lean#L11-L16) 及 [`twenty_five_propertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/LargeVertices.lean#L21-L26)
- 桥接与规格文件：[`ProfileApplication.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ProfileApplication.lean)、[`ProfileProbability.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ProfileProbability.lean)、[`TypeCounting.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/TypeCounting.lean)、[`TraceProfiles.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/TraceProfiles.lean)、[`K4Profiles.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K4Profiles.lean) 以及规范入口 [FORMAL_SPEC.md](file:///Users/rfy_naiveai/Desktop/aris4math/FORMAL_SPEC.md)。

**审阅结论：Scoped No Mismatch Found**。  
在审阅范围内，**未发现语义保真度偏差、未声明隐藏假设或桥接反例**。两分支的输入完全对齐目标规格 F 的有限规约边界；中间层类型聚合、概率支配、对角线剔除与容量约束均已闭合；最终结论严格产出原始 [FORMAL_SPEC.md](file:///Users/rfy_naiveai/Desktop/aris4math/FORMAL_SPEC.md) 的 Property B 谓词。

---

### 2. 关键语义与潜在漏洞逐项核验

#### 2.1 任意 5-uniform $H$、点对覆盖与 32 边输入合法性
- **观察事实**：
  - [`twenty_four_propertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/LargeVertices.lean#L11-L12) 接收 `(H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering) (edges32 : H.edges.card = 32)`。
  - [`twenty_five_propertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/LargeVertices.lean#L21-L22) 接收 `(H : Simple5Hypergraph (Fin 25)) (cover : H.PairCovering) (edges32 : H.edges.card = 32)`。
- **数学对齐**：
  - `H.PairCovering` 定义为 $\forall x \ne y, \exists e \in H.edges, x \in e \wedge y \in e$，即 $\lambda_{uv} \ge 1$。
  - 顶点集固定为 `Fin 24` / `Fin 25`，边数恰为 32。这与 [FORMAL_SPEC.md](file:///Users/rfy_naiveai/Desktop/aris4math/FORMAL_SPEC.md) 核心规约 **F** 完全一致。
  - 声明中不存在任何预选 profile、局部正则性、线性超图、颜色均衡或特定选点假定。选点与分类定理（如 $v=24$ 的 4 个度 6 且共度 1 的顶点集；$v=25$ 的 6 个度 6 且避免两三元交的顶点集）完全由 `cover` 与 `edges32` 在超图内部构造性析出。

#### 2.2 实际边类型计数、覆盖与 1-based 位置映射
- **观察事实**：
  - $v=24$：[`positions24`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/K4Profiles.lean#L118-L125) 映射 $i \in \text{Fin } 4$ 至 $i + 10$（0-based 为 $\{10, 11, 12, 13\}$）。转换为 1-based 索引 $(positions24(i)).val + 1 = i + 11 \in \{11, 12, 13, 14\}$，与 [`Numeric.v24_K4_1..3`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L321) 的 `positions = [11, 12, 13, 14]` 严格吻合。
  - $v=25$：[`positions25`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/TraceProfiles.lean#L218-L225) 映射 $i \in \text{Fin } 6$ 至 $i + 9$（0-based 为 $\{9, \dots, 14\}$）。转换为 1-based 索引为 $\{10, 11, 12, 13, 14, 15\}$，与 [`Numeric.v25_K6_1..9`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L354) 的 `positions = [10, 11, 12, 13, 14, 15]` 严格吻合。
  - 覆盖完备性：[`TableRealization`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/TypeCounting.lean#L41-L46) 要求 `covers : ∀ e ∈ E, classify e ∈ p.types.map Numeric.EdgeType.locks`。[`actual_entries_cover`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/TraceProfiles.lean#L305) 证明了超图的任意实际边必映射到 Profile 中的某个有效行，杜绝了遗漏边掩盖概率的可能。

#### 2.3 虚拟类型 Count 0 与权重计算的独立性
- **观察事实**：
  - 在 [`ProfileApplication.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ProfileApplication.lean#L19-L20) 中，单边和边对分别传入 `⟨positionType vertices positions e, 0⟩`。
  - [`endpoint_ratio_numeric`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ProfileProbability.lean#L179-L185) 与 [`critical_ratio_le_numeric`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ProfileProbability.lean#L400-L408) 证明了单事件概率仅由几何锁集 `t.locks`（长度及位置元素）、未锁位置数及空槽数决定。
  - `Numeric.edgeWeight` 与 `Numeric.pairWeight` 函数体完全不读取 `t.count` 或 `u.count`，虚拟计数值 0 对概率权重的计算无任何副作用。

#### 2.4 有序边对对角线剔除（Off-Diagonal & $t = u$ 扣除）
- **观察事实**：
  - 贪心失败的关键点要求 $A \ne B$（交集恰为 $\{x\}$ 且 $|A|=|B|=5$）。
  - 在实际边对求和中，求和范围明确限制在 `H.edges.offDiag`（即 $A \ne B$ 的有序对）。
  - 在聚合定理 [`pair_fiber_card`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/TypeCounting.lean#L56-L58) 及 [`pair_sum_by_type`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/TypeCounting.lean#L99-L104) 中：
    - 当类型相同 $t = u$ 时，有序对数精确为 $m_t (m_t - 1)$，严格剔除了 $(e, e)$ 对角项；
    - 当类型不同 $t \ne u$ 时，由于两 fiber 不相交，有序对数精确为 $m_t \cdot m_u$。
  - 这与 `Numeric.pairCount` 中 `t.count * (u.count - if t.locks = u.locks then 1 else 0)` 精确一致。

#### 2.5 真实条件概率与 Numeric 权重
- **观察事实**：
  - 在条件排列空间 `Locked vertices positions`（等度量均匀分布）下，[`ProfileProbability.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ProfileProbability.lean) 分情形完成闭式对齐：
    1. **锁定交点**：交点 $x = \text{vertices } j$。当且仅当位置 $k = \text{positions } j$ 且其他锁满足偏序时非零，未锁点分别独立落入左侧 $a$ 槽与右侧 $b$ 槽，概率为 $\frac{\binom{a}{r} \binom{b}{q}}{\binom{N}{r} \binom{N-r}{q}}$，与 `Numeric.pairWeight` 分支严格一致；
    2. **自由交点**：交点 $x$ 自由。当且仅当位置 $k$ 未被锁定时非零，$x$ 占位概率 $1/N$，剩余自由点落槽概率为 $\frac{\binom{a}{r-1} \binom{b}{q-1}}{\binom{N-1}{r-1} \binom{N-r}{q-1}}$，与 `Numeric.pairWeight` 分支严格一致；
    3. **非单点相交或偏序冲突**：实际临界事件为空集，概率为 0，而 `Numeric.pairWeight` 非负，自然满足 $\le$ 支配。

#### 2.6 容量兼容性与逐位求 Min（Min-before-total）
- **观察事实**：
  - **容量保证**：自由交点由 [`free_union_bound`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ProfileProbability.lean#L247-L250) 保证 $r + q - 1 \le N$；锁定交点由 [`locked_union_bound`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ProfileProbability.lean#L274-L276) 保证 $r + q \le N$。
  - **Min 顺序**：在 [`failure_ratio_le_position_bounds`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ConditionalUnion.lean#L77-L86) 中，上界形式为 $\sum_{k \in \text{Fin } v} \min(A_k, \min(B_k, C_k))$。
  - 取小操作是在**每个扫描位置 $k$ 单独完成**后，再沿 $k=1,\dots,v$ 求和；不存在“先对 $C_k$ 全局求和再与全局 $A, B$ 取小”的松弛失误。
  - $v=24, 25$ 分支中 `correctionCenters = []` 且 `emptyPairCap = none`，无需引入额外的 link 扣除有效性假设。

#### 2.7 最终 Property B 输出保真度
- **观察事实**：
  - [`propertyB_of_failure_ratio_lt_one`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ConditionalUnion.lean#L96-L99) 证明：若失败概率 $< 1$，则必存在未导致失败的排列 $\sigma$。
  - [`Greedy.propertyB_of_successful_permutation`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L242-L245) 严格构造出染色 $c : V \to \text{Bool}$，使得每条边满足 $1 \le |\{x \in e : c(x) = \text{true}\}| \le 4$。
  - 最终导出的结论即为标准 [`Aris4Math.PropertyB H`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L31-L34)，不存在降级或假借。

---

### 3. 公理与依赖闭合检查

- **依赖公理**：查看 [`twenty_four_propertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/LargeVertices.lean#L31) 与 [`twenty_five_propertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/LargeVertices.lean#L30) 的公理足迹：
  - 仅依赖 Lean 核心公理集合：`propext`、`Classical.choice`、`Quot.sound`。
  - 无 `sorryAx`，无自定义 `axiom`，无 `native_decide` 信任开销。
- **已证明范围声明**：
  - 本次审阅确认 $v=24$ 与 $v=25$ 两条单顶点数有限目标分支已在 Lean 中无缝贯通并达成完全闭合；
  - 顶层全称目标 $T$（以及 $v=21, 22, 23$）尚未在此处组合，符合已知交接状态。

