### 有限范围实际 Caller 对抗数学审阅报告：I2 $(7,3,0)$ 库存

**审阅范围与执行声明：**
* **已完整核读文件（只读未修改）：**
  1. 主证明规范：[TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_THREE_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_THREE_TRIPLES.md)
  2. 不交 missing 证据与代码：[REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/REPORT.md)、[HIGH_JOBS.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/HIGH_JOBS.py)、[GENERATE.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/GENERATE.cpp)、[VERIFY.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/VERIFY.cpp)、[JOBS.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/JOBS.json)、[GENERATION.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/GENERATION.json)、[INDEPENDENT_CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/INDEPENDENT_CHECK.json)。
  3. 活跃 tag 进口定理声明核对：[FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)、[FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)、[FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md)、[SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)、[SIX_POSITIVE_SIX_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SIX_POSITIVE_SIX_TRIPLES_REPAIR.md)、[NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)、[THREE_LARGE_POSITIVE_TWO_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_LARGE_POSITIVE_TWO_NEGATIVE_PAIRS_REPAIR.md)、[FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md)、[FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md)。
* **执行情况：** 纯静态数学与代码逻辑审阅，**未编译或执行任何程序，未运行 Lean**。
* **审阅结论：** **未发现必须修正的数学问题（PASS）**。

---

### 1. 原始迹预算与共同点单蓝归约（第 1 节）

* **预算恒等式：** $|V|=24=7_P+17_L$，$P$ 度 8、$L$ 度 7，35 条五元边，无全七度边（$n_0=0$），恰有 $I=2$ 条内部边 $I_1,I_2 \subseteq P$，且 $n_3=3, n_4=0$。由 $n_1+n_2=35-2-3=30$ 及 $n_1+2n_2=56-10-9=37$ 唯一解得 $n_1=23, n_2=7$。
* **逐点度与 PL 覆盖：** 对任意 $v \in P$，$u_v = 8 - c_v - h_v - s_v \ge 0$；由 $v$ 与 $L$ 中 17 个点的点对覆盖得 $4u_v + 3s_v + 2h_v \ge 17$，代入 $u_v$ 即得 $s_v + 2h_v \le 15 - 4c_v$。
* **共同单蓝归约 $h_q + s_q \le 1$（$q \in C = I_1 \cap I_2$）：**
  * 只将 $q \in C$ 染蓝、$P \setminus \{q\}$ 染红时，$I_1,I_2$ 及含 $q$ 的二／三迹均已双色；未满足原边精确给出 $m_4 = 6 - h_q - s_q$ 个正四集、$N_2 = 3 - h_q \le 3$ 个负二集、$T = 7 - s_q$ 个负三集、$B = 23 - m_4$ 个负四集，无正三或负单，外点总出现次数 $\le d_H(y) = 7$。
  * 若存在 $q \in C$ 满足 $h_q + s_q \ge 2$，则 $m_4 \le 4, N_2 \le 3$，直接由已核的 [FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md) 完成原 35 边染色。因此反设未染时，同一 $H$ 的所有 $q \in C$ 同时满足 $h_q + s_q \le 1$。
* **Missing 二对完备性：** 两条互异内部五边在 7 点集 $P$ 中的补集为两个互异二元集，必为**交于一点（相邻 missing，$|C|=4$）**或**不相交（不交 missing，$|C|=3$）**，分类穷尽。

---

### 2. 相邻 Missing 型的独立重算（第 2 节，重点核查 $s_0=2$）

* **公共结构推导：** 设 missing 对为 $01, 02$，则 $C=\{3,4,5,6\}$，$c=(0,1,1,2,2,2,2)$。
  * 因 $c_0=0$，对每个 $q \in C$，点对 $0q$ 必由三迹或 $J$ 覆盖，故 $h_q+s_q \ge 1$；结合 (4) 得 $h_q+s_q = 1$，且 $q$ 的唯一三迹或唯一 $J$ 边必含 $0$。
  * 若某三迹不含 $0$，因 $|P \setminus (C \cup \{0\})| = |\{1,2\}| = 2 < 3$，该三迹必含某 $q \in C$，但这迫使 $q$ 的唯一三迹既含 $0$ 又不含 $0$，矛盾。故**三条高迹全部含 $0$（$h_0=3$）**。
  * 每个 $q \in C$ 有 $u_q = 8 - 2 - 1 = 5$（共 20 条单迹），故 $u_0 + u_1 + u_2 = 23 - 20 = 3$。结合 $u_0 = 8 - 0 - 3 - s_0 = 5 - s_0 \ge 0$ 得 $u_1 + u_2 = s_0 - 2 \ge 0$，即 $2 \le s_0 \le 5$；另有 $h_1 + h_2 = 9 - h_0 - H_C = 6 - H_C \ge 2$。
* **分支 1（$H_C > 0, s_0 \ge 3$）：** 取 $h_q=1, s_q=0$ 的 $q \in C$，令 $Q=\{0,q\}$ 蓝。两内部边（含 $q$ 不含 $0$）与三条高迹（均含 $0$ 且 $|Q|=2<3$）全双色；因 $s_q=0$ 无 $J$-正三（$m_3=0$），$N_2=0$，$m_4 = u_0+u_q = 10-s_0 \le 7$，$T = 7-s_0 \le 4$，$B = 13+s_0 \le 18$，满足 [SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)。
* **分支 2（$s_0 = 2$，独立重算）：**
  * 此时 $u_0 = 3$，$u_1 + u_2 = 0 \implies u_1 = u_2 = 0$。因 $h_1 + h_2 \ge 2$，取 $h_i \ge 1$ 的 $i \in \{1,2\}$。
  * **子情况 A（$h_i \ge 2$）：** $i$ 至多漏掉 1 条高迹。若漏掉某高迹 $T^*$，因 $0 \in T^*, i \notin T^*$ 且 $|\{1,2\}\setminus\{i\}|=1$，$T^*$ 必含某点 $q \in C$（若 $h_i=3$ 则任取 $q \in C$）。取 $Q=\{i,q\}$ 蓝：
    1. $I_1,I_2$ 均含 $q \in C$（蓝）及至少 3 个红点，已双色；
    2. 三条高迹均遇 $\{i,q\}$（蓝）且均含 $0 \notin \{i,q\}$（红），全部双色，故 $N_2 = 0, m_2 = 0$；
    3. $q \in C$ 的 $J$ 边若存在则唯一为 $0q$，绝不可能是 $iq$（$i \in \{1,2\}$），故无全蓝 $J$ 边，即 $m_3 = 0$；
    4. $m_4 = u_i + u_q = 0 + 5 = 5$ 个正四集，负集仅 $T \le 7$ 个负三与 $B = 18$ 个负四（$T+B \le 25 \le 35$），$D \le 7$，直接满足 [FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md)（及其总负 $\le 35$ 推论）。
  * **子情况 B（$h_i = 1$）：** $i$ 漏掉 2 条高迹 $T',T''$。同上，$T'$ 必含某点 $q \in C$，从而 $h_q = 1, s_q = 0$，且 $T'$ 为唯一含 $q$ 高迹（故 $q \notin T''$）。取 $Q=\{i,q\}$ 蓝：
    1. $I_1,I_2$ 含 $q$ 双色；含 $i$ 的高迹与 $T'$ 均含蓝点及红点 $0$ 而双色；唯独 $T''$ 避开 $\{i,q\}$，留下 **恰 1 个负二集（$N_2 = 1$）**（完全规避了旧版将 $\{1,2\}$ 染蓝时未考虑 $1,2$ 共处同一高迹导致剩 2 个负二的错误）；
    2. 由 (1)，$s_i = 8 - c_i - h_i - u_i = 8 - 1 - 1 - 0 = 6$，且 $s_q = 0$。故无全蓝 $J$ 边（$m_3 = 0$），6 条含 $i$ 的 $J$ 边已双色，仅剩 $T = 7 - 6 = 1$ 个负三集；
    3. $m_4 = u_i + u_q = 0 + 5 = 5$ 个正四集，$B = 18$ 个负四集；
    4. 从唯一负二集中任取一点固定为蓝（禁入红集），该负二整份满足删除，5 个正四集删 1 点后大小均 $\in \{3,4\}$，剩余负三集 $\le 1 \le 3$、负四集 $\le 18$，$D \le 7$，准确满足 [FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)。
* **分支 3（$H_C = 0$）：** 此时每个 $q \in C$ 有 $h_q=0, s_q=1$（$J$ 边为 $0q$），故 $s_0 \ge 4$，且三条高迹全为 $012$（$h_1=h_2=3$）。由 $u_1+u_2 = s_0-2 \le 3$ 取 $u_i \le 1$ 的 $i \in \{1,2\}$ 与任意 $q \in C$，令 $Q=\{i,q\}$ 蓝：两内部与三高迹全双色（$N_2=0$），$q$ 的唯一 $J$ 边为 $0q \ne iq$ 故 $m_3=0$，且 $s_i = 4-u_i, s_q=1$ 给出 $T = 7 - (5-u_i) = 2+u_i \le 3 \le 4$，$m_4 = 5+u_i \le 6 \le 7$，$B = 18-u_i \le 18$，满足 [SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)。

---

### 3. 不交 Missing 型：必要域、双生成、活跃 Tag 与运输（第 3–5 节及代码核对）

1. **高族多重集与真 48 群轨道（[HIGH_JOBS.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/HIGH_JOBS.py) 与 [VERIFY.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/VERIFY.cpp)）：**
   * 标准形固定 missing 对为 $01$（mask 3）与 $23$（mask 12），内部边为 mask 124, 115，$C=\{4,5,6\}$，$c=(1,1,1,1,2,2,2)$。
   * 35 个三元子集允许重复取 3 个得 $\binom{35+3-1}{3} = 7770$ 个高迹多重集；按 $C$ 上 $h_v \le 1$ 过滤得 1266 个。
   * 保持 $\{I_1,I_2\}$ 不变的 $S_7$ 子群恰由 $\{0,1\},\{2,3\}$ 的块置换（8 种）与 $\{4,5,6\}$ 的全置换（6 种）组成，阶为 $8 \times 6 = 48$，通过**同一顶点置换同时作用于三条高迹与 $J$**，将 1266 个高族无损分为 64 个轨道（轨道大小之和为 1266）。
2. **完整必要 $J$ 域与双生成逐键相等（[GENERATE.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/GENERATE.cpp) 与 [VERIFY.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/VERIFY.cpp)）：**
   * 必要条件 $\sum_{k=0}^{20} j_k = 7$、未覆盖 $P$-点对 $j_k \ge 1$、$u_v \ge 0$、$4u_v+3s_v+2h_v \ge 17$ 及 $v \in C$ 上 $h_v+s_v \le 1$ 全部是同一原超图 $H$ 的必要条件；每对重数 $\le 7$ 用 3 位编码入 63 位键无溢出。
   * `VERIFY.cpp` 采用按顶点前向星直接枚举的第二构造，逐键从 `NECESSARY.bin` 的 `expected` 集合中 `erase` 并断言唯一命中且最终为空，确认 64 个 job 共 **126,927 个必要键**逐键完全相等。
3. **全部 35 原迹重建与 11 个活跃 Tag 门假设逐一核对：**
   * `VERIFY.cpp`（第 59–61 行）对全部 126,927 条记录各自的 `r.blue`（$|Q| \in \{1,2,3,4\}$）重建全部 35 条原 $P$-迹（$4,442,445$ 个角色），断言两内部边双色（`free > 0`）、无全蓝高迹（`positive[1]==0 && positive[2]==0`）、无负单集（`negative[1]==0`），且全红高迹产生的负二集 `negative[2]` 全部保留。
   * 实际活跃的 11 个 tag（计数总和 $3208+36008+24664+8266+754+1+6275+22237+16190+7796+1528 = 126927$）与各自进口定理的假设逐一匹配无误：
     * **Tag 2 ($q=1, m_3=0, m_4 \le 4$) & Tag 3 ($q=0, m_3+m_4 \le 4$)：** Tag 2 先禁唯一负二的 1 点使正四集缩为 $\ge 3$ 元并消除负二，与 Tag 3 一并满足 [FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)（$s=3, D=7 \implies 4(D-1)=24 < 27=3s^2$）。
     * **Tag 4 ($q=0, m_3+m_4 \le 5, t \le 3$)：** 满足 [FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)。
     * **Tag 9 ($q=0, m_3=0, m_4 \le 7, t \le 4, b \le 35$)：** 满足 [SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)（含第 C 节 $b \le 35$ 扩展）。
     * **Tag 10 ($q=0, m_3=0, m_4 \le 6, t \le 6, b \le 35$)：** 满足 [SIX_POSITIVE_SIX_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SIX_POSITIVE_SIX_TRIPLES_REPAIR.md)。
     * **Tag 13 ($q=0, m_3=0, m_4=9, t \le 3$)：** $|L|=17 \le 18, D \le 7$（且实际 $b=23-9=14 \implies t+b \le 17 \le 20$），满足 [NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)。
     * **Tag 16 ($q \le 2, m_3+m_4 \le 2$)：** 从至多 2 个负二各禁 1 点，正三／四集删 $\le 2$ 点后仍非空，各取 1 点得 $\le 2$ 红，避开全部负集。
     * **Tag 17 ($q \le 3, m_3=0, m_4 \le 4$)：** 满足上一轮已审的 [FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md)。
     * **Tag 18 ($q \le 3, m_3=0, m_4 \le 3, t \le (4-q)16-1$)：** 满足 [THREE_LARGE_POSITIVE_TWO_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_LARGE_POSITIVE_TWO_NEGATIVE_PAIRS_REPAIR.md) 的参数化定理（$s=4, q \le 3$）。
     * **Tag 19 ($q=1, m_3+m_4 \le 5, m_3 \le 3, t \le 2$)：** 禁唯一负二的 1 点后，仅原 $m_3 \le 3$ 个正三集可能缩为正二集，正四集缩为三／四集，故剩余正二集数 $\le 3$、负三数 $\le 2$，满足 [FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md)。
     * **Tag 20 ($q=1, m_3+m_4 \le 5, t=0$)：** 禁唯一负二的 1 点后，至多 5 个正集大小均 $\ge 2$，无剩余负二／负三，满足 [FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md)。
4. **逆置换运输：** 任意不交 missing 的原 $H$ 若不满足第 1 节单蓝直接修复，则经真 48 群中的置换 $\pi$ 映射到某代表 `job.T` 及其必要域中的键 `r.J`；将记录自身的 `r.blue` 由 $\pi^{-1}$ 拉回原 $P$，外点集 $L$ 保持原索引不变，直接由对应门定理得到 $R \subseteq L$，完整恢复原 35 条边的双色性。

---

### 4. 认可的具体未发现问题范围与边界声明

* **具体未发现问题范围：** 确认 [TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_THREE_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_THREE_TRIPLES.md) 对 **24 点、35 条五元边、覆盖全部点对、$P_7$（八度）与 $L_{17}$（七度）、无全七度边、恰有 $I=2$ 条 $P$-内部边、$(n_2,n_3,n_4)=(7,3,0)$ 库存**（含相邻 missing 解析证明、不交 missing 1266 高族／64 轨道／126,927 必要 $J$ 键／11 个活跃 tag 接口及逆置换运输）的证明与代码逻辑静态核查无数学漏洞。
* **边界声明：** 本次审阅未执行任何程序或 Lean；仅覆盖上述 $I=2, (7,3,0)$ 库存，**未覆盖其余 $I=2$ 库存、整个 24 点分支或完整 $m(5) \ge 36$ 命题**。

