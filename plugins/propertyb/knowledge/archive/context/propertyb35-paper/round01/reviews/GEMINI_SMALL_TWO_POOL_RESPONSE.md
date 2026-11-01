**HERO — 静态数学对抗审阅报告：受限五小正两负三集门、24点六高一内部新增库存及21点六度中心六名unit-8邻点定理**

本次审阅仅针对指定文件做静态数学与代码逻辑核查，**未执行任何程序或 Lean**。

---

### 1. 实际读取与未读／未执行范围声明
* **实际读取的文件**：
  * [FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md)（全文，1–103行）及所引 [FIVE_SMALL_POSITIVE_ONE_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_ONE_TRIPLE.md)（全文，1–89行）
  * [TWENTYFOUR_SIX_HIGH_ONE_INTERNAL_PARTIAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SIX_HIGH_ONE_INTERNAL_PARTIAL.md)（全文，重点核对 §2 禁两七度点共度桥、§8 新增库存 $(2,4,0)/(2,1,2)$ 及 §10–11 返回染色与剩余范围）
  * [SIX_UNIT8_POOL_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md)（全文，1–95行）、[UNIQUE6_NO7_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_no7/UNIQUE6_NO7_PROOF.md)（全文，1–95行）
  * [six_unit8_star_join.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/six_unit8_star_join.py)、[SIX_UNIT8_STAR_JOIN.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_STAR_JOIN.json)、[independent_pool_replay.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/independent_pool_replay.py)、[INDEPENDENT_POOL_REPLAY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/INDEPENDENT_POOL_REPLAY.json)
* **未读／未重跑而作为既有依赖的项**：未重跑 `unique6_no7/replay.py` 及旧 `THREE/FOUR/FIVE/SIX_DOMAIN.json`、`_DP.json`、`_JOINT.json` 概率证书，将其已验证的 26 个五邻点残轨道与 3 个六邻点全共度二严格证书作为既有依赖。

---

### 2. 逐项数学对抗核查

#### (1) [FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md)（$\le 5$ 正2..4集且**至多3个正二集**、$\le 2$ 负3、任意负4、总出现 $\le 7$）
* **$\le 4$ 正集或 5 个两两不交正集（§1）**：$\le 4$ 正集直接调四小正三负三门。恰 5 个不交正集时，至少 2 个大小 $\ge 3$；独立均匀选点下，由 4 变量 AM-GM 与正点负出现 $\le 6$ 得负4集坏概率和 $\le \frac{3}{2}\sum_{i=1}^5|A_i|^{-3} \le \frac{3}{2}(\frac{3}{8}+\frac{2}{27}) = \frac{97}{144}$，加上 2 个负3集至多 $2\cdot\frac{1}{8}=\frac{36}{144}$，总和 $\le \frac{133}{144} < 1$。
* **三重点与不属于正二集的重复点（§2）**：$a_x\ge 3$ 直接闭合（$4>2$）。在 $\max a_v=2$ 下，若重复点 $x$ 不属于任何正二集（即所属两正集大小均 $\ge 3$）：
  * 若有负3集含 $x$，令 $x$ 蓝（禁 $x$），则两正集删 $x$ 后大小仍 $\ge 2$，且含 $x$ 的负3集被消去，余 $\le 1$ 个负3集，归约为 `FIVE_SMALL_POSITIVE_ONE_TRIPLE.md`（其包含全二元 $Q_5$ 立方体度约束 $14=\sum_{i=1}^5 e_i \ge 3\cdot 4+2\cdot 2=16$ 矛盾证明）。
  * 若两负3集均不含 $x$，固定 $x$ 红，余 $\le 3$ 正集：相交或 $\le 2$ 集时 $|R|\le 3$ 且含 $x$（故不等于任何负3集）；两两不交时 $\ge 2^3=8$ 份四点候选对至多 $2+5=7$ 份受堵。
  * 由此严密推得：**所有重复点均属于某个正二集，且任意两个大小 $\ge 3$ 的大正集互不相交**。
* **便宜构造与二集交形归约（§§3–5）**：
  固定二重点 $x$ 红，若余三集不交（最大大小 $a\ge 2$），候选 $S=\prod s_i\ge 4a > 2a+3 \ge 7+(a-2)r$；若余三集交于 $y$ 且第三集大小 $\ge 3$，则 $\ge 3>2$ 份三点候选。因此当正二集 $\le 2$ 个或两正二集相交时，余族至多含一个二集且两大集不交，必落入上述两构造。唯一剩余情况为 **3 个两两不交正二集 $P_1,P_2,P_3$ 与 2 个不交大正集 $A,B$**。
* **三二集与两大集端点关联的两型穷尽与收尾（§§5–6）**：
  设 $a_i=|A\cap P_i|, b_i=|B\cap P_i|$（$a_i+b_i\le 2$），$\alpha=\sum a_i>0, \beta=\sum b_i>0$。对 $a_i>0$ 固定 $x\in A\cap P_i$ 红，若 $\beta-b_i=0$ 则余族不交；若 $\beta-b_i\ge 2$ 则两余二集中击中 $B$ 的点对数为 $4-(2-b_j)(2-b_k)\ge 3>2$。故仅当 ($\forall a_i>0\implies \beta-b_i=1$) 且 ($\forall b_i>0\implies \alpha-a_i=1$) 时未完成，結合 $a_i+b_i\le 2$ 唯一解出两型：
  1. **第一型（$\alpha=\beta=1$，$x\in A\cap P_1, y\in B\cap P_2, P_1=\{x,p\}, P_3=\{z_0,z_1\}$）**：若 $\{x,y,z_0\},\{x,y,z_1\}$ 均被堵，则两负3集恰为此二者。改令 $x$ 蓝、固定 $p,y$ 红，从 $A\setminus\{x\}$（大小 $\ge 2$，且与 $\{p,y,z_0,z_1\}$ 不交）和 $P_3$ 各取一点，得 $\ge 2\times 2=4$ 份四点候选 $\{p,y,a',z_j\}$。两负3集因含蓝 $x$ 被避开；$y$ 已有正2+负三2=4次出现，故含 $y$ 的负4集至多 $7-4=3$ 个（不含 $y$ 的负4集不堵），**4候选对 $\le 3$ 堵**成功。
  2. **第二型（$\alpha=\beta=2$，$P_1=\{a_1,b_1\}, P_2=\{a_2,b_2\}, P_3=\{z_0,z_1\}$）**：四份三点候选 $\{a_1,b_2,z_j\},\{b_1,a_2,z_j\}$（$j=0,1$）均击中五正集，4候选对 $\le 2$ 负3集成功。

#### (2) [TWENTYFOUR_SIX_HIGH_ONE_INTERNAL_PARTIAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SIX_HIGH_ONE_INTERNAL_PARTIAL.md)（§2 共度桥与 §8 两新增库存）
* **§2 禁两七度外点的共度桥**：当 $|F|=|\{f,g\}|=2$ 且有 $r$ 个正4集 $\{q\}\cup A_i$ 缩为正2集时，这 $r$ 条不同原边均含 $\{q,f,g\}$，故 $\lambda_H(f,q)\ge r, \lambda_H(f,g)\ge r$。由24点点对覆盖与 $d_H(f)=7$：
  $$2(r-1) \le (\lambda_H(f,q)-1) + (\lambda_H(f,g)-1) \le \sum_{v\neq f}(\lambda_H(f,v)-1) = 4\cdot 7 - 23 = 5 \implies r\le 3.$$
  故条件 (2)（$m_q\le 5$、未命中高迹 $\le 2$、$n_2-s_q\le 2$）严密满足 `FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md` 的“至多3个正二集”前提。
* **§8 库存 $(2,4,0)$ 与 $(2,1,2)$**：
  * $(2,4,0)$（$n_1=28$）：4条三迹在 $C$（$|C|=5$）内总关联 $\sum_{q\in C}h_q \ge 4\cdot 2 = 8$。若有8度点 $q\in C$ 满足 $h_q\ge 2$，则 $m_q=7-h_q-s_q\le 5, 4-h_q\le 2, 2-s_q\le 2$，满足条件 (2) 闭合；若所有8度 $C$ 点均 $h_q\le 1$，则唯一9度点必在 $C$ 且 $h_q=4$，染该9度点 $q$ 蓝使全部4条高迹 proper，$m_q=9-1-4-s_q=4-s_q\le 4$，总负集数 $(2-s_q)+(28-m_q)=26\le 35$，由 `FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md` 直接闭合。
  * $(2,1,2)$（$n_1=29, k=3$）：$\sum_{q\in C}h_q \ge 2 + 2\cdot 3 = 8$。由于9度点至多贡献 $k=3$，其余四名8度 $C$ 点不可能全 $\le 1$（否则和 $\le 7<8$），故必存在8度点 $q\in C$ 满足 $h_q\ge 2$，此时 $m_q\le 5$、未命中高迹 $3-h_q\le 1$、负3集 $2-s_q\le 2$，由条件 (2) 闭合。

#### (3) [SIX_UNIT8_POOL_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md)（21点六度中心 + 六名unit-8邻点即染）
* **对“唯一六度／无七度”前提的剥离核查**：
  对照 [UNIQUE6_NO7_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_no7/UNIQUE6_NO7_PROOF.md)，旧证明仅在第1节用“唯一六度、无七度”导出单位八度池大小 $N\ge 7$。一旦固定6度中心 $x$ 与所选单位8度子集 $Y$（$|Y|\in\{3,4,5,6\}$），其精确迹恢复（仅用35总边数、5元简单性及锁点度 $6,8,\dots,8$）与排列失败界 $A_k,B_k,C_k-D_k$（仅用 $v=21, s=|Y|+1$、锁点迹库存及由锁点20邻点覆盖导出的 link 配额）均完全不读取未选自由点的度数。因此任意6名单位8度邻点 $U$ 的每个五元子集若无严格染色证书，必落入旧26个五邻点残轨道。
* **$\Pi=3+3$ 的解析排除**：
  旧26残轨道允许的五点中心划分仅为 $3+2, 2+2+1, 2+1+1+1, 1+1+1+1+1$，故6点划分 $\Pi$ 若含 $\ge 3$ 点块则必为 $3+3$（两块 $B,D$ 各3点）。静态核查 `INDEPENDENT_POOL_REPLAY.json` 确认26残中 $3+2$ 仅出现在轨道12，其全部点对共度为2，且唯一非零 $\ge 3$ 邻点包含数即三点块本身（数值1，恰来自过 $x$ 的中心边）。于是在不含 $x$ 的非中心边中，任意3名 $U$ 点的包含数全为0。任取 $u\in B$，其非中心度为 $8-1=7$，但其与 $B\setminus\{u\}$ 两点的非中心共度各为 $2-1=1$、与 $D$ 三点的非中心共度各为 $2$，非中心共度和为 $2\cdot 1+3\cdot 2=8 > 7$，迫某条非中心边含 $u$ 及另外至少两名 $U$ 点，矛盾。故 $\Pi$ 每块大小 $\le 2$。
* **共度一图 $G=K_{1,5}$ 与六份五视图共享包含数空连接**：
  每个五点诱导子图为空或 $K_{1,4}$ 迫6点图 $G$ 为空（直接由旧六邻点全共度二、块 $\le 2$ 的3轨道严格证书 $\le 977/1001<1$ 闭合）或完整星 $K_{1,5}$。当 $G=K_{1,5}$（中心1，叶2..6）时，静态核查 [six_unit8_star_join.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/six_unit8_star_join.py) 与 [independent_pool_replay.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/independent_pool_replay.py)：两套独立实现（分别从 `FIVE_DOMAIN.json` 标签过滤与从26残轨道代表做全部 $S_5$ 重标号）对6个五元视图（前5个含星中心1各有153项，最后1个全叶 $\{2,3,4,5,6\}$ 有545项）按共享子集包含数 $I_A$ 逐步连接，前缀连接数为 `153 -> 999 -> 898 -> 207 -> 15 -> 0`，无任何相容六元组。

---

### 3. 核查总结
在本次审阅的局部范围内，**未发现任何数学逻辑缺口、计数偏差或隐含前提越界**。24点六高一内部仍余 $(6,2,0),(4,3,0),(5,1,1),(3,2,1)$ 四个库存未全闭，21点其余分支及完整 $m(5)\ge 36$ 命题仍保持开放。

