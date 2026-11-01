### 1. 审阅范围与执行记录

* **程序执行情况**：本次为只读静态数学与代码审计（**未运行任何 C++/Python 程序，未运行 Lean，未读取历史审阅记录，未访问 `aris4math_v2`**）。所有解析推导、矩阵迹不等式、取整边界、表格分配算术与 C++/Python 代码逻辑均已由人工逐行静态核对。
* **完整全文阅读的文件**：
  1. 主稿：[TWENTYONE_UNIQUE_SIX_ONE_SEVEN.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_UNIQUE_SIX_ONE_SEVEN.md)（全文 1–295 行，含主定理及 §1–§11）
  2. 本支新增递推与核验源码/数据（位于 `context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/`）：
     * [SIMPLE_CHAIN_DP.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_DP.cpp)（全文 1–44 行）
     * [SIMPLE_CHAIN_FREQUENCY_VERIFY.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_FREQUENCY_VERIFY.cpp)（全文 1–35 行）
     * [SCALAR_T_ONLY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SCALAR_T_ONLY.py)（全文 1–22 行）及 [SCALAR_T_ONLY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SCALAR_T_ONLY.json)（全文 1–487 行）
     * [SIMPLE_CHAIN_RUN.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_RUN.py)（全文 1–50 行）
     * [SIMPLE_CHAIN_VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_VERIFY.py)（全文 1–49 行）及 [SIMPLE_CHAIN_VERIFY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_VERIFY.json)（全文 1–126 行）
  3. 全部 §11 数学进口证明文件（均全文读取）：
     * [SIX_UNIT8_POOL_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md)（全文 1–95 行）
     * [TWENTYONE_HIGH_FOUR_CORE_LOW.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_HIGH_FOUR_CORE_LOW.md)（全文 1–204 行）
     * [TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md)（全文 1–73 行）
     * [TWENTYONE_A1_STRONG_FOREST_RANK.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_STRONG_FOREST_RANK.md)（全文 1–143 行）
     * [TWENTYONE_A1_BALANCED_STAR_FOREST.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md)（全文 1–238 行）
     * [GLOBAL_PRIVATE_PAIR_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_PRIVATE_PAIR_REPAIR.md)（全文 1–158 行）
     * [GLOBAL_TWO_FLIP_PATH_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md)（全文 1–288 行）
     * [THREE_INTERSECTION_MIDDLE_NEAR_SATURATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_INTERSECTION_MIDDLE_NEAR_SATURATION.md)（全文 1–102 行）
     * [GLOBAL_TWO_FLIP_SHARED_MIDDLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md)（全文 1–196 行）
     * [TWENTYONE_LOW_NONUNIT_DEGREE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_LOW_NONUNIT_DEGREE_REPAIR.md)（全文 1–70 行）
     * [DERIVATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_incidence_rank_subset_20261020/DERIVATION.md)（全文 1–268 行）
     * [TWENTYONE_A1_QUAD_TAU_COUPLING.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_QUAD_TAU_COUPLING.md)（全文 1–58 行）
     * [PROBABILITY_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md)（全文 1–370 行）
* **部分阅读 / 未重跑的底层大证书文件**：
  * [SIMPLE_CHAIN_RESULT.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_RESULT.json)（读取前 800 行，含全部 19 条 `(e, n4_cap)` 最优度序列记录及状态统计）。
  * 各局部修复引理底层的固定排列证书 JSON 与生成脚本（如 `unique6_no7/replay.py`、`high_edge_intersection_repair_20261020/VERIFY.json`、`high_four_core_mixed_q3_20261020/VERIFY.json`、`a1_middle_near_saturation_20261020/VERIFY.json`）未重跑或逐行展开大 JSON，仅在各进口文档与 `SIX_UNIT8_POOL_PROOF.md` 中核对了其调用假设与接口一致性。

---

### 2. 逐节覆盖与核查简表（MAIN-THEOREM 及 MAIN-1..11）

| 章节标识 | 核心命题/接口 | 核查状态 | 审计要点与结论 |
|---|---|---|---|
| **MAIN-THEOREM** | 21点、35互异五边、点对覆盖、$\delta=6$、唯一6度点 $x$ 且唯一7度点 $p \implies$ Property B | **PASS** | 反证法结构闭环：§1 强迫唯一 A1 角色 $\to$ §2–§3 强迫 $\lambda\le 4$ 及 $\bar{H}$ 四交秩 $\le 2, n_4\le 8$ $\to$ §4–§6 筛出 25 个交谱 profile $\to$ §7–§9 用 $q_i\ge 2$ 与主子矩阵前缀 DP 排除 24 项 $\to$ §10 用 $\bar{H}$ 四交三角形迫 $\tau\ge 3$ 排除最后 1 项。 |
| **MAIN-1 (§1)** | 从原假设强迫唯一 A1 角色：$d=(6,7,8^9,9^{10})$，$\lambda(x,B)=2$，其余与 $x$ 共度 1 | **PASS** | 六单位八度池引理不依赖“无7度点”或自由点度数；总度下界 $b\ge 9$ 与 $x$ 行盈余 4 结合池引理 $b-4\le 5$ 迫 $b=9$、十点恰9度、$\lambda(x,p)=1$ 且恰四名8度点共度2。 |
| **MAIN-2 (§2)** | 强点对及含 $x/p$ 四交核、8/9度四核三重覆盖修复进口 | **PASS** | 全部前提与 §1 A1 角色精确匹配；非 B 时全局 $\lambda(u,v)\le 4$（7/8 对 $\le 3$），四交核避 $x,p$，且任意 $\{8,9\}$ 四元核至多属于 2 条原边。 |
| **MAIN-3 (§3)** | 删星 $\bar{H}$ 平衡计数、$r(\bar{\Gamma})\ge 19$、中心化 Gram 给 $r_4(\bar{H})\le 2$ 及 $n_4(H)\le 8$ | **PASS** | 权重 $506,22,132,572,2002$、孤立边 $\le 3$、仿射二进制秩界 $r(\bar{\Gamma})\ge 19$、中心化迹 $a_0+a_3+3a_4\ge 28$ 及嵌套 Kruskal 界 $9438>9278$ 全部精确无误，无循环依赖。 |
| **MAIN-4 (§4)** | 原 $H$ 单翻 $n_1\ge 397$ 与两翻路径判据 $L<2722720$ | **PASS** | 单翻与两翻均直接作用于原 $H$ 的 10/11 平衡染色，无临界性假设；外边对方向因子 2 仅出现一次，系数 $(36,120,330,792,1716)$ 与阈值 $2722720$ 准确。 |
| **MAIN-5 (§5)** | 五容量上界 (4)、凸度目标 $f(s)$ 在 threshold 图最大化及递推 $T(35,n_1,0)$ | **PASS** | $C_0..C_4$ 每一项上界（含 $C_1\le 26n_1+339$ 与 $C_3\le 13n_3$）均对同一原 $H$ 成立；按字典序最大度序列的边交换证明邻域嵌套，严格导出 $T(n,m,r)$，无需 N34 线性界。 |
| **MAIN-6 (§6)** | 完整原矩域 21615 个整数 profile 覆盖及第一筛 25 项 | **PASS** | 由 $\lambda\in\{1..4\}$ 逐对有 $\binom{\lambda-1}{2}\le \lambda-1$，故 $0\le \tau\le 140$；反演公式 (6) 唯一且 $n_2\ge 0, t\le 8 \implies n_1\le 524<546$，21615 域无遗漏覆盖所有非 B 实际 $H$。 |
| **MAIN-7 (§7)** | $\Gamma$ 中存在 $q_F\le 1$ 直接给原 $H$ 染色（迫 $2\le q_i\le 34$） | **PASS** | 固定 $F$ 一红四蓝、外 16 点均匀 9 红 7 蓝；三支 union bound（$434/455, 1007/1040, 448/455$）均 $<1$，无独立性假设，完全替代旧 low19/13 Schur 分类。 |
| **MAIN-8 (§8)** | 原关联矩阵主子矩阵迹与删1/删2边度损耗给前缀式 (8)–(11) | **PASS** | $\ell_t(N)$ 四项下界、单删 $q_1\le R, q_{13}\le R-1$（偶整数取整 $52169/441\to 120$、$52988/441\to 122$）及双删 $q_1+q_2\le E-49+2t$ 均由原 $H$ 子集导出。 |
| **MAIN-9 (§9)** | 固定最大度 DP 与频率 DP 覆盖放松域，25 项筛剩唯一式 (13) | **PASS** | 两种 C++ 实现均精确覆盖满足 (7)–(11) 的全部非增整数序列；代码中 $q_2\le 29$ 在 $E\le 80,t\le 8$ 下由 $2q_2\le q_1+q_2\le 47 \implies q_2\le 23$ 自动蕴含，无 T33/T34 依赖。 |
| **MAIN-10 (§10)** | 最后 profile $(33,523,0,31,8;\tau=1)$ 的四交—$\tau$ 耦合矛盾 | **PASS** | $n_4=8$ 与跨星 $\le 5$、$r_4(\bar{H})\le 2$ 迫 $\bar{H}$ 四交图为 3 边秩 2 简单图，必含 $K_3$；三边交 $\ge 3$ 点贡献 3 个 $\lambda\ge 3$ 点对，迫 $\tau\ge 3 > 1$，矛盾。 |
| **MAIN-11 (§11)** | 进口条件地图、证据与复算入口说明 | **PASS** | 每个进口的适用条件、原 $H$ 染色连接与本支调用范围准确对应，未将局部结果夸大为全 36 完成。 |

---

### 3. 关键攻击点与反例尝试的逐项核查

1. **原假设强迫 A1 角色是否完整（是否存在隐藏自由点度数假设或遗漏情况）？**
   * **核查**：在 [SIX_UNIT8_POOL_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md) 中，局部迹库存仅锁 $x$（6度）和 5 或 6 名与 $x$ 共度 1 的 8 度点，概率上界 $A_k,B_k,C_k-\ell_k$ 的无放回注入公式与中心 link 配额只读取锁点度数 $[6,8,\dots,8]$ 与总边数 35，完全不读取未选自由点的度数。
   * **反例尝试**：若 $p$（7度点）与 $x$ 共度 $\ge 2$，能否避开 6 名单位 8 度点？
     若 $\lambda(x,p)\ge 2$，由于 $x$ 的总行盈余 $\sum_{v\ne x}(\lambda(x,v)-1)=4$，$p$ 至少消耗 1 份盈余，故 $b\ge 9$ 名 8 度点中至多 3 名与 $x$ 共度 $\ge 2$，必有至少 $9-3=6$ 名单位 8 度点，触发池引理染色。同理，若 $b\ge 10$，则至少 $10-4=6$ 名单位 8 度点。因此 $b=9$、余 10 点恰为 9 度、$\lambda(x,p)=1$ 且恰 4 名 8 度点满足 $\lambda(x,b)=2$ 被唯一强迫。
2. **删星森林给 $n_4\le 8$ 且保留 $\bar{H}$ 四交秩 $\le 2$ 是否循环？**
   * **核查**：§3 的证明仅依赖 §1 的 A1 角色和 §2 的两个四核修复引理（四交核避 $x,p$ 及 $\{8,9\}$ 四核重数 $\le 2$）。
   * 在 $\bar{H}=H-x$（20 点 29 边，度谱 $6^5,7^5,8^{10}$）上：
     * 孤立于 $\bar{\Gamma}$ 的原边必满足 $\sum_{v\in e}\bar{d}(v)=33$，仅有 $S=(2,3,0)$ 和 $T=(3,1,1)$ 两型，由点集容斥知至多 3 条孤立边（$I\le 3$）。
     * 由 $\operatorname{rank}(B)=\operatorname{rank}(A)\le 20$ 及每分量 $s_i$ 条等重二进制行的仿射维数界 $d_i\ge 1+\lceil\log_2 s_i\rceil$，消去 $r\le 17$（维数直接越界）与 $r=18$（零空间维数 $\le 1 < 9$），得 $r_{0234}\ge 19$。
     * 由 20 点中心化 Gram 矩阵 $B_0 = A(I_{20}-J_{20}/20)A^T$（秩 $\le 19$）的 Cauchy 不等式得 $608\bar{Q}\ge 66238 \implies \bar{Q}\ge 109$，结合 $\bar{Q}-54=2a_0+2a_3+6a_4$ 及偶整数性得 $a_0+a_3+3a_4\ge 28$。
     * 若 $r_4(\bar{H})=3$，则 $a_4\le \binom{4}{2}=6 \implies a_0+a_3+a_4\ge 16 \implies h_0\ge 6$，Kruskal 嵌套森林权给出 $F\ge 616+110(19)+374(6)+66(3)+1430(3)=9438>9278$，染色成功。
   * 因此 $r_4(\bar{H})\le 2$（从而 $a_4\le 3$）及 $n_4(H)\le a_4+5\le 8$ 在进入 §6 和 §8 之前已完全独立证毕，**不存在任何循环论证**。
3. **原 $H$ 单翻/两翻事件的方向因子与共有 middle 的五容量：**
   * **核查**：在 `GLOBAL_TWO_FLIP_PATH_REPAIR.md` 中，无序外边对 $\{G,J\}$ 的 middle 数 $c(G,J)$ 关于 $G,J$ 对称；有序路径 $(G,F,J)$ 选择 $\{G,J\}$ 的两个方向之一（产生唯一因子 2），固定方向后 $g\in G\cap F$ 与 $h\in F\cap J$ 唯一确定，因此 $\mathbb{E}[Z]=2\sum_{j=0}^4 C_j r_j$ 中**没有多余或缺失的方向因子**。
   * **核查 $C_3\le 13n_3$ 的隐藏点度条件**：`THREE_INTERSECTION_MIDDLE_NEAR_SATURATION.md` 假设外边对差集 $A\cup B$ 的四点度属于 $\{7,8,9\}$（至多一个 7）。若某三交外边对的 $A\cup B$ 含有唯一 6 度点 $x$，是否会漏网？不会：该文 §2 证明了当 $c(G,J)\ge 14$ 时，$A\times B$ 四条跨边对重数 $\le 4$ 迫每行每列跨边和 $\ge 14-8=6$，加上自身外边后 $A\cup B$ 每点原度自动 $\ge 7$，故 6 度点 $x$ 不可能出现在 $c(G,J)\ge 14$ 的差集中。
4. **Threshold 凸度最大化的压缩证明：**
   * **核查**：$f(s)=\frac{1}{2}(s^2-(5-b)a^2-b(a+1)^2)$ 的差分为 $f(s+1)-f(s)=s-\lfloor s/5\rfloor$，单调非减。在固定点数 $n$ 与边数 $m$ 的简单图中，取使 $\sum f(d_v)$ 最大且排序度序列字典序最大的图，若 $d_u\le d_v$ 而 $u$ 有不邻于 $v$ 的邻居 $w\ne v$，将边 $uw$ 移为 $vw$ 使目标不减且排序度序列字典序严格增大，矛盾。故邻域满足嵌套性 $N(u)\setminus\{v\}\subseteq N(v)\setminus\{u\}$，每次必存在孤立点或全邻点，严格给出动态规划 $T(n,m,r)$。该压缩仅用于求无约束简单图上界 $P\le T(35,n_1,0)$，未将压缩图性质混入 §8 的关联矩阵前缀。
5. **全部 21615 矩域如何覆盖任意实际 $H$：**
   * **核查**：点对覆盖保证 $\lambda(u,v)\ge 1$，§2 保证非 B 时 $\lambda(u,v)\le 4$。对任意整数 $\lambda\in\{1,2,3,4\}$ 恒有 $\binom{\lambda-1}{2}\le \lambda-1$，求和即得 $0\le \tau\le \sum(\lambda-1)=140$。由 $n_2=140+\tau-3m-6t\ge 0$ 及 $t\le 8$ 自动有 $n_1=508-\tau-n_2+2t\le 524<546$。因此遍历 $\tau\in[0,140], t\in[0,8], m\in[0,\lfloor(140+\tau-6t)/3\rfloor]$ 且保留 $n_j\ge 0, n_1\ge 397$ 的 21615 个整数元组完整覆盖所有非 B 实际 $H$。
6. **$q_\Gamma\le 1$ 直接给原染色且无独立性假设：**
   * **核查**：在 `TWENTYONE_LOW_NONUNIT_DEGREE_REPAIR.md` 中，对 $\Gamma$-度 $\le 1$ 的原边 $F$，固定 $F$ 内一红四蓝、外 16 点均匀 9 红 7 蓝：
     * $q_F=0$：选最小 singleton 组 $a\le \lfloor 34/5\rfloor=6$ 为红点，union bound 为 $(34\times 35+91\times 6)/1820=434/455<1$；
     * $q_F=1$ 且 $|F\cap G|=0$：$a\le \lfloor 33/5\rfloor=6$，加上 $G$ 单色概率 $7/208$，union bound 为 $243/260+7/208=1007/1040<1$；
     * $q_F=1$ 且 $|F\cap G|\in\{2,3,4\}$：选 $v\in F\cap G$ 为 $F$ 中唯一红点，则 $G$ 必含 $v$（红）与 $F\setminus\{v\}$ 中至少一蓝点而**确定性双色**；过 $v$ 的 singleton 边数恰为 $d(v)-2\le 7$，union bound 为 $(33\times 35+91\times 7)/1820=448/455<1$。
   * 全部使用有限样本空间上的线性期望/并集界，完全不假设边事件独立。
7. **主子矩阵与原点度删1/删2产生全部前缀的取整：**
   * **核查**：对任意 $N$ 条原边子集 $S$，$\ell_t(N)$ 的四项均对上取整。
   * 删 1 条边（$N=34$）：$2e_S+4a_{4S}\ge Q-T\ge \frac{67184-273T}{441}$。一般 $F$ 有 $D_F\ge 37\implies T\le 55$，右端为 $52169/441=118.297\dots$，左端为偶整数故 $\ge 120\implies e_S+2a_{4S}\ge 60\implies q_1\le E-60+2t=R$；23 条避 $x,p$ 的原边有 $D_F\ge 40\implies T\le 52$，右端为 $52988/441=120.154\dots$，左端为偶整数故 $\ge 122\implies e_S+2a_{4S}\ge 61\implies q_{13}\le R-1$。
   * 删 2 条边（$N=33$）：放松顶点重数 $R_v\in\{0,1,2\}$ 到最低五度 $6,7,8,8,8$ 各取 2，得 $W-W_S\ge 59\implies T\le 61$，从而 $e_S+2a_{4S}\ge \frac{14513}{294}=49.3639\dots \implies e_S+2a_{4S}\ge 50\implies q_1+q_2\le E+1-(50-2t)=E-49+2t$。
8. **固定最大度 DP 与独立频率 DP 真正覆盖放松域，且 25 项恰剩式 (13)：**
   * **核查代码与数学等价性**：
     * 在 [SIMPLE_CHAIN_DP.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_DP.cpp#L9-L26) 和 [SIMPLE_CHAIN_FREQUENCY_VERIFY.cpp](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/SIMPLE_CHAIN_FREQUENCY_VERIFY.cpp#L10-L30) 中，`lower(N)` 在分子为负时由 `max({0, ...})` 截断为 $\ge 0$，分子为正时 `(num + den - 1)/den` 精确实现 $\lceil\text{num}/\text{den}\rceil$。
     * 代码中 $i\ge 2$ 时的 `q <= 29` 是否会误删合法序列？不会：25 个候选满足 $E\in[72,80], t\in[4,8]$，故 $q_1+q_2\le E-49+2t\le 47$（实际 19 组输入中最大为 $78-49+16=45$），由 $q_2\le q_1$ 必有 $q_2\le 23 < 29$。同理，在 $q_i\ge 2$ 下 $z=l=0$，`z<=3` 与 `M+l+z<=50` 恒真。
     * 复算表 §9 中关键行：最大被排项 $(33,522,2,30,8;\tau=0)$ 有 $B=12803$，分配 $C=(0,12333,48,390,32)$，得 $U=3432(522)+60(12333)+165(48)+396(390)+858(32)=2721300<2722720$；唯一幸存项 $(33,523,0,31,8;\tau=1)$ 有 $B=12827$，分配 $C=(0,12392,0,403,32)$，得 $U=2725500\ge 2722720$。
9. **同 $H$ 的 $n_4=8\implies \bar{H}$ 四交三角形 $\implies \tau\ge 3$ 是否成立：**
   * **核查**：同一非 B 原 $H$ 若有 $n_4(H)=8$，由 §3 跨星四交对 $\le 5$ 及星内四交对 $=0$，必有 $\bar{H}$ 内四交边对数 $a_4\ge 3$；又由 §3 知 $\bar{H}$ 四交图森林秩 $q\le 2$，故 $a_4=3, q=2$。3 条边且森林秩 $\le 2$ 的简单图必为一个三角形 $K_3$ 加孤立点。设该 $K_3$ 对应原边 $E_1,E_2,E_3\in \bar{H}\subset H$，则在 5 元集 $E_1$ 内 $|E_1\cap E_2|=|E_1\cap E_3|=4 \implies |E_1\cap E_2\cap E_3|\ge 4+4-5=3$。任取其中 3 点 $u,v,w$，三对 $\{u,v\},\{u,w\},\{v,w\}$ 均同时属于 $E_1,E_2,E_3$，故原共度均 $\ge 3$，每对向 $\tau(H)$ 贡献至少 $\binom{3-1}{2}=1$，从而 $\tau(H)\ge 3$，与 (13) 中 $\tau=1$ 矛盾。

---

### 4. 错误、推导与最小修正

* **结论**：经逐节、逐公式、逐代码分支的对抗性核查，[TWENTYONE_UNIQUE_SIX_ONE_SEVEN.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_UNIQUE_SIX_ONE_SEVEN.md) 主链及本支新增代码实现**未发现任何数学错误、逻辑跳跃、循环依赖、取整方向错误或边界遗漏**，无需修改主稿或代码。

---

### 5. 最终判定

* **本支审阅判定**：**PASS（静态全文数学与代码审计通过）**。
  * 在明确标注“本次未重新执行底层局部排列证书及未在会话内运行 C++/Python 脚本”的前提下，主稿 [TWENTYONE_UNIQUE_SIX_ONE_SEVEN.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_UNIQUE_SIX_ONE_SEVEN.md) 给出了**21点、35条互异五元边、点对覆盖、最小度6、唯一六度点且恰一个七度点（A1整支入口）**具有 Property B 的完整、严密、无循环的自然语言与有限算术证明。
* **全局范围区分**：
  * 本结论仅闭合 **21点唯一六度且恰一七度（reduced A1）** 这一完整分支；
  * 21–25 点的其余开放分支及整个 $m(5)\ge 36$ 目标**仍未完成证明**，已验收无条件全局下界仍为 34。

