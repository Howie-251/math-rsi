### 数学 Checkpoint B 对抗式审阅报告

**审阅范围**：
- 核心规格与地图：[`FORMAL_SPEC_PROPERTYB_33.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md)、[`COMPLETE_CANDIDATE_MAP.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/COMPLETE_CANDIDATE_MAP.md)
- 核心论证稿件：
  1. [`TWENTY_THREE_LOW_WITH_SEVEN_BAD.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/TWENTY_THREE_LOW_WITH_SEVEN_BAD.md)（23点 $r=1$、存在七度非单位邻居）
  2. [`TWENTY_THREE_ONE_SIX_ALL_SEVENS_UNIT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/r123-child/TWENTY_THREE_ONE_SIX_ALL_SEVENS_UNIT.md)（23点 $r=1$、六度点与全部七度点单位共度）
  3. [`TWENTY_THREE_MANY_SEVENS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/TWENTY_THREE_MANY_SEVENS.md)（23点 $r=0$、$t \ge 19$）
  4. [`REFINED_DELETION_CERTIFICATES.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/REFINED_DELETION_CERTIFICATES.md)（坏边对有限配额与对偶证书）
- 依据代码与审计记录：
  - [`CustomDeletion.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/CustomDeletion.lean)、[`ConditionalUnion.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ConditionalUnion.lean)、[`LinkDeletion.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/LinkDeletion.lean)
  - [`one_low_bad_high_v23.py`](file:///Users/rfy_naiveai/Desktop/aris4math/computations/propertyb33/round01/one_low_bad_high_v23.py)、[`one_low_five_high.py`](file:///Users/rfy_naiveai/Desktop/aris4math/computations/propertyb33/round01/r123-child/one_low_five_high.py)、[`mixed_matching_five.py`](file:///Users/rfy_naiveai/Desktop/aris4math/computations/propertyb33/round01/r123-child/mixed_matching_five.py)、[`avoided_lock_quotas.py`](file:///Users/rfy_naiveai/Desktop/aris4math/computations/propertyb33/round01/avoided_lock_quotas.py)、[`multilock.py`](file:///Users/rfy_naiveai/Desktop/aris4math/computations/multilock.py)
  - [`LOW_HIGH_COLORED_SELECTION.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/candidate-audit/LOW_HIGH_COLORED_SELECTION.md)、[`ONE_LOW_ALL_UNIT_SELECTION.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/candidate-audit/ONE_LOW_ALL_UNIT_SELECTION.md)、[`REPORT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/candidate-audit/REPORT.md)
  - 相关证书数据：[`ONE_LOW_BAD_HIGH_V23.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/ONE_LOW_BAD_HIGH_V23.json)、[`ONE_LOW_BAD_HIGH_REFINEMENT_V23.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/ONE_LOW_BAD_HIGH_REFINEMENT_V23.json)、[`MIXED_MATCHING_FIVE.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/r123-child/MIXED_MATCHING_FIVE.json)、[`SIX_SEVEN_MATCHING_V23.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/SIX_SEVEN_MATCHING_V23.json)、[`SIX_SEVEN_MATCHING_REFINEMENT_V23.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/SIX_SEVEN_MATCHING_REFINEMENT_V23.json)

**未检查部分**：
- 23点 $r=2, 3$ 分支（`TWENTY_THREE_TWO_SIXES.md`、`TWENTY_THREE_THREE_SIXES.md`）；
- 23点 $r \ge 4$ 分支及全部24点分支；
- 独立重新运行浮点LP求解器（仅核验保存的精确有理证书算术与理论不等式方向）。

---

### 一、对抗式攻击核验结论

#### 1. 十点有色选择（`TWENTY_THREE_LOW_WITH_SEVEN_BAD.md`）
- **核查内容**：10点简单图 $J$（$\delta(J) \ge 3$，色类大小 $\le 4$）中是否存在三角形或两端异色的诱导 $P_3$；以及实际 $H$ 是否提供该假设。
- **数学验证**：
  1. **池大小与度数**：$H$ 为23点点对覆盖，$r=1$ 给出 $t \ge 17$。六度点 $x$ 剩余超额 $3-l$，七度点 $y$ 剩余超额 $7-l$。与 $x,y$ 均单位共度的七度点集 $U$ 满足 $|U| \ge (t-1)-(3-l)-(7-l) = t+2l-11$。当 $l=2, t \ge 17$ 时 $|U| \ge 10$；当 $l=3, t \ge 15$ 时 $|U| \ge 12 \ge 10$。任意七度点非单位邻居至多6，故10点子集上的单位共度图 $J$ 满足 $\delta(J) \ge 9-6=3$。每个点由包含 $y$ 的唯一超边着色，色类大小至多 $5-1=4$。前提完全由 $H$ 满足。
  2. **引理极小反例推导**：假设无三角形且所有诱导 $P_3$ 两端同色。无三角形蕴含每个顶点的所有邻居互不相邻，因而两两构成以该点为中心的诱导 $P_3$，故同色。沿路径推导，每个连通分支至多使用2种颜色（即使含奇环，两步同色约束会使颜色折叠为单色），分支大小至多 $4+4=8$。另一方面，在无三角形且 $\delta \ge 3$ 的简单图中，任意边 $uv$ 满足 $N(u) \cap N(v) = \emptyset$，故分支顶点数 $\ge |N(u) \cup N(v)| \ge 3+3=6$。10个点无法容纳两个 $\ge 6$ 的分支，故整图连通（10点），与分支至多8点矛盾。
  3. **真实迹禁止条件**：在诱导 $P_3$（两端 $b, c$，中点 $d$）情形，$b, c$ 异色意味着包含 $y, b$ 的唯一边与包含 $y, c$ 的唯一边不重合，因此任何实际边不能同时包含 $\{y, b, c\}$（掩码14）。在 [`ONE_LOW_BAD_HIGH_V23.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/ONE_LOW_BAD_HIGH_V23.json) 中原始未严格通过的代表仅有 group 27, 31, 35，它们全部位于 $l=2, \lambda(b,c)=2$ 且均含掩码14或15，被真实选点条件严格排除。三角形分支（$\lambda(b,c)=1$）全部代表本身均已严格通过，未添加多余排除。
- **结论**：**成立，无缺口。**

#### 2. 四份 defect-1 分组（`TWENTY_THREE_ONE_SIX_ALL_SEVENS_UNIT.md`）
- **核查内容**：最大度 $\le 6$ 的图是否可4分组使各部诱导最大度 $\le 1$；是否能选出5个七度锁。
- **数学验证**：
  1. 考虑 $L$ 的全部4分组划分，取使部内边数 $\sum_{i=1}^4 e(G[V_i])$ 最小的划分。若某点 $v \in V_i$ 在所在部内度数 $d_{V_i}(v) \ge 2$，因总度 $d(v) \le 6$，其他3部中 $v$ 的邻居总数 $\le 4$。由抽屉原理必有某部 $V_j$（$j \ne i$）满足 $d_{V_j}(v) \le 1$。将 $v$ 移至 $V_j$ 会使目标函数至少减少 $2 - 1 = 1$，与极小性矛盾。故每部诱导最大度 $\le 1$（各部均为匹配）。
  2. 由 $t \ge 17$，最大部大小 $\ge \lceil 17/4 \rceil = 5$。取其中5点，其诱导非单位共度图为0、1或2条边的匹配。结合 $x$（与所有七度点单位共度），构成6锁（5高1低），非单位对仅为高点间的至多两条二共度边。
- **结论**：**成立，无缺口。**

#### 3. $\lambda=3$ 排除（七度点间三共度排除）
- **核查内容**：$r=1$ 和 $r=0$ 中 $\lambda=3$ 的排除是否依赖循环假设或未通过行。
- **数学验证**：
  1. **$r=1$ 分支**：设七度点 $y, z$ 满足 $\lambda(y, z)=3$。由于二者消耗各自超额的2个单位，各至多另有4个非单位邻居。$L \setminus \{y, z\}$ 中至少 $t - 2 - 8 = t - 10 \ge 17 - 10 = 7$ 个点与 $y, z$ 均单位共度。任选其中两点 $u, v$，其相互共度 $\lambda(u, v) \in \{1, 2, 3\}$（$\ge 4$ 已由双锁引理排除）。五锁 $(x, y, z, u, v)$ 中 $x$ 与其余四点均单位共度，非单位对仅为 $yz$（共度3）与 $uv$（共度1、2或3）。在 [`MIXED_MATCHING_FIVE.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/r123-child/MIXED_MATCHING_FIVE.json) 中，包含3的75个代表**全部严格小于1**（最坏8365/8398）。该文件未通过的行全部位于 $(1,1), (1,2), (2,2)$，不参与 $\lambda=3$ 排除。
  2. **$r=0$ 分支**：设七度点 $a, b$ 满足 $\lambda(a, b)=3$。共同单位邻居池至少 $t - 10 \ge 19 - 10 = 9$ 点。9点子集在非单位图中的最大度 $\le 6$，其补图最小度 $\ge 9 - 1 - 6 = 2 > 0$，必存在单位共度对 $u, v$（$\lambda(u, v)=1$）。四锁 $(a, b, u, v)$ 仅一对共度3、其余5对共度1，在 [`SEVEN_PAIR3_FOUR_V23.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/SEVEN_PAIR3_FOUR_V23.json) 中完整5个同构型全部严格通过。
- **结论**：**成立，无缺口。**

#### 4. 三团 Moment 不等式与全局矛盾（`TWENTY_THREE_MANY_SEVENS.md`）
- **核查内容**：$W_e \le 6(I_e - C_e)$ 在每条边上是否恒成立；全局求和是否矛盾；选出的大迹六锁是否准确。
- **数学验证**：
  1. **单边不等式逐分支核验**：设边 $e$ 在三团中的交集大小为 $p = (a, b, c)$，非负整数，$\sum p_i \le 5$，且反设 $\sum \min(p_i, 2) \le 3$。
     - 仅占1团 $(r, 0, 0)$（$r \le 5$）：$C_e = 0, I_e = r, W_e = \binom{r}{2}$。$\binom{r}{2} \le 6r$ 对所有 $r \le 5$ 成立（$10 \le 30$）。
     - 占2团 $(r, s, 0)$（$r, s \ge 1$）：因 $\min(r, 2) + \min(s, 2) \le 3$，必有至少一团大小为1，设为 $(r, 1, 0)$（$1 \le r \le 4$）。此时 $I_e = r+1, C_e = r \implies I_e - C_e = 1$。$W_e = \binom{r}{2}$。当 $r=4$ 时，$\binom{4}{2} = 6 \le 6 \times 1 = 6$（精确临界饱和）；对 $r \le 3$ 严格小于6。
     - 占3团 $(a, b, c)$（$a, b, c \ge 1$）：因 $\min(a, 2) + \min(b, 2) + \min(c, 2) \ge 3$，等号迫使 $(a, b, c) = (1, 1, 1)$。此时 $W_e = 0, I_e = 3, C_e = 3 \implies I_e - C_e = 0$。$0 \le 6 \times 0$ 成立。
     - 覆盖完全：所有满足条件的非负整数组合均严格满足 $W_e \le 6(I_e - C_e)$。
  2. **全局求和代数验证**：
     - $I = \sum_{v \in L} d(v) = 7t$（每个七度点出现7次）。
     - $W = 2 \sum_{i=1}^3 \binom{s_i}{2} = \sum s_i^2 - t = t^2 - 2C - t$（团内点对共度恒为2）。
     - $C = s_1 s_2 + s_1 s_3 + s_2 s_3$（跨团点对共度恒为1，由点对覆盖及无外部坏边给出）。
     - $W - 6(I - C) = t^2 - 43t + 4C$。
     - 对全部四种可能团规模 $(5,7,7), (6,6,7), (6,7,7), (7,7,7)$，代入计算结果分别为 **20, 24, 72, 126**，全部严格大于0。与 $\sum W_e \le 6(I - C)$ 矛盾！
  3. **六锁大迹存在性**：故必存在边 $e$ 满足 $\sum \min(|e \cap L_i|, 2) \ge 4$。从 $e$ 在各团中至多各取2点，至少取到4点；再从各团不足2点者补足到各恰2点（因每团大小 $\ge 5$ 必可补足）。所得6个锁点内部共度2图恰为3条不交匹配边，且 $e$ 在这6个锁点上的迹大小 $\ge 4$。
  4. **局部域排除对应**：在787个有标号类型（54代表）中，含 $\ge 4$ 点块的代表恰有22个；其中21个由总/纯配额通过，唯一的 group 4 由 exact dual 闭合（23849/24310 < 1）。未通过的 group 20 和 30 仅含有大小为3的块，确被本节大迹选择排除。
- **结论**：**成立，无缺口。**

#### 5. 大迹分类与重复迹对应性
- **核查内容**：大迹（大小 $\ge 3$）是否可能重复；二元迹是否正确保留重数；空迹与单点迹恢复是否准确。
- **数学验证**：
  1. **大迹不可重复性**：若大小 $\ge 3$ 的迹 $B$ 在不同超边中重复出现两次，则 $B$ 中**任意两点**的共度均 $\ge 2$，从而 $B$ 在共度2图中诱导一个完全图 $K_{|B|}$（包含三角形）。然而：
     - 在 $r=1$ 有坏邻居分支中，共度2图是两条不交边；
     - 在 $r=1$ 全单位分支中，共度2图是至多两条边的匹配；
     - 在 $r=0$ 分支中，共度2图是 $P_3$、$P_3+K_2$、或匹配；
     - 它们全部是**无三角形图**（triangle-free）。因此大小 $\ge 3$ 的迹在所有这些分支中**数学上绝对不可能出现 $\ge 2$ 次**，重数至多为1。
  2. **二元与单元/空迹恢复**：首个未覆盖 pair 递归允许二元迹出现多次（由 pair 余量决定）；单元迹由度数守恒 $n_i = d_i - \sum_{B \ni i, |B| \ge 2} n_B$ 唯一定出；空迹由总边数 $n_\emptyset = 33 - \sum_{B \ne \emptyset} n_B$ 唯一定出。凡出现负重数者均无法由实际超图实现，剔除合法。
- **结论**：**成立，无缺口。**

#### 6. 真实坏槽、避开锁子族配额、非负对偶罚项与量词次序（`REFINED_DELETION_CERTIFICATES.md`）
- **核查内容**：式 $(D)$ 是否成立；配额 $q_R$ 是否来自真实超图；量词次序是否合法（选位置后再随机）。
- **数学验证**：
  1. **不等式 $(D)$ 的代数严密性**：
     设槽 $s$ 的实际坏对数为 $b_s \in [0, c_s]$，双向概率权重为 $w_s \ge 0$。配额为 $\sum_s a_{Rs} b_s \ge q_R$。对任意 $\alpha_R \ge 0$：
     $$\sum_s \beta_s b_s \ge \sum_R \alpha_R q_R, \quad \text{其中 } \beta_s = \sum_R \alpha_R a_{Rs}$$
     逐槽分析 $(\beta_s - w_s) b_s$：
     - 若 $\beta_s - w_s \le 0$，因 $b_s \ge 0$，$(\beta_s - w_s) b_s \le 0 \le c_s \max(0, \beta_s - w_s)$；
     - 若 $\beta_s - w_s > 0$，因 $b_s \le c_s$，$(\beta_s - w_s) b_s \le c_s (\beta_s - w_s) = c_s \max(0, \beta_s - w_s)$。
     两情形均满足 $(\beta_s - w_s) b_s \le c_s \max(0, \beta_s - w_s)$。求和即证：
     $$D = \sum_s w_s b_s \ge \sum_R \alpha_R q_R - \sum_s c_s \max(0, \beta_s - w_s)$$
     完全初等，不依赖 LP 最优性、对偶定理或浮点精度。
  2. **配额 $q_R$ 的底集与交集界**：
     对中心 $x$ 关联且避开 $R$ 的边族 $F_R$，删去 $x$ 后的四元 link 底集大小为 $v_0 = v - 1 - |R|$（$x \notin R$）。因 $H$ 为简单超图，互异四元 link 的交集大小至多为3。点重数 $a_y$ 满足：
     $$4|F_R| - v_0 \le 4|F_R| - |\bigcup L(e)| = \sum (a_y - 1) \le \sum \binom{a_y}{2} = \sum_{e \ne e'} |L(e) \cap L(e')| \le 3 b_R$$
     故坏对数 $b_R \ge \lceil (4|F_R| - v_0)/3 \rceil$。槽指示 $a_{R, \{t, u\}} = 1 \iff (t \cup u) \cap R = \emptyset$，准确覆盖了 $F_R$ 内的所有坏对。
  3. **量词与位置次序**：
     在 [`CustomDeletion.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/CustomDeletion.lean) 中，量词结构为：
     $$\forall H, \quad (\exists \text{vertices}, \text{positions}, p, \text{loss}), \quad \text{RealizesProfile} \implies \text{strict} < 1 \implies \text{PropertyB } H$$
     **位置分配是在超图与锁点固定后、根据局部剖面确定性选择的，随机置换在选定位置后才进行条件采样。**
     因此不存在“随机之后再选择位置”的量词颠倒风险；无需引入排列混合或 Jensen 平均。
  4. **共享锁零权重保持**：
     若两边在中心 $x$ 之外还共享另一个锁点，则在中心 $x$ 处的双向记账权重 $w_s = 0$（代码在 $t \cap u \ne \text{pivot}$ 时严格返回 0）。该槽容量仍被保留在容量罚项中，对偶公式不会凭空赋予正权重。
- **结论**：**成立，无缺口。**

---

### 二、最小实质缺口与修法（形式化交接边界）

所审查的四份核心候选在**纯数学推导与数值证书**层面未发现逻辑漏洞、算术错误或全称覆盖缺口。当前存在的“缺口”严格属于**尚未完成的形式化工程连接（Paper Candidate $\to$ Lean Proof）**：

| 序号 | 形式化连接缺口 | 影响范围 | 最小修法 / 推荐路线 |
|---|---|---|---|
| 1 | **十点彩色选点引理**未 Lean 化 | $r=1$ 有坏邻居分支 | 在 `ThirtyThree` 新建图论辅助模块，形式化“$\delta \ge 3$、色类 $\le 4$、10点简单图无三角必含两端异色诱导 $P_3$”的有限极小性证明；输出三点及掩码14排除见证。 |
| 2 | **四份 defect-1 分组引理**未 Lean 化 | $r=1$ 全单位分支 | 形式化有限图划分的势能下降法（同部边数最少划分），证明 $\Delta \le 6$ 蕴含部内最大度 $\le 1$；应用抽屉原理取大小 $\ge 5$ 的部。 |
| 3 | **三团 Moment 不等式求和**未 Lean 化 | $r=0$ 分支 | 形式化有限边求和不等式 $\sum W_e \le 6(I - C)$ 与全局整数度数代数矛盾（20, 24, 72, 126 > 0），导出 $\exists e, \sum \min(\|e \cap L_i\|, 2) \ge 4$。 |
| 4 | **有限子族配额与式 $(D)$** 未接回 Lean | 依赖 exact dual 的5个剖面 | 形式化 link 交集 $\le 3$ 引理及有理对偶逐槽不等式 $(D)$，证明其下界满足 [`CustomDeletion.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/CustomDeletion.lean) 的 `center_lower` 假定。 |
| 5 | **有限局部域覆盖见证** | 全部23点分支 | 形式化时可直接将生成的有标号多重迹列表作为有限归纳基底，或为每个同构代表提供置换拉回见证，避免在 Lean 内证明复杂的多项同构分类定理。 |

---

### 三、总结评估

本次 Checkpoint B 对抗式审阅确认：
1. **数学全称覆盖完全闭合**：23点 $r=1$（两分支互补穷尽）与 $r=0$（七度点 $t \ge 19$）的数学分支结构完备，无任何悬空假设。
2. **所有关键机制成立**：十点着色引理、四分组引理、$\lambda=3$ 排除、三团矩不等式及非负对偶惩罚公式 $(D)$ 均在数学上经受住了对抗性检验，定义与量词次序正确。
3. **状态定性**：这三个分支目前是**数学完备、算术精确、证据链闭合的纸面候选（Paper Candidates with Exact Certificates）**，可安全推进到形式化装配阶段，不构成已完成的 Lean 定理。
