# 七维受控圈供体转移

## 命题

设 $M$ 为 $Q_7$ 的短边匹配，原孔集 $H$ 独立。短边连接 Hamming 距离为一的顶点，$K(Q_d)$ 表示同一顶点集上的完全图。沿外坐标切分得六维面 $A,B$，按全局两色 $\alpha,\beta$ 计，原孔型分别为 $(r,r+k)$、$(s+k,s)$，其中 $r,s\ge0$、$k\ge2$。取 $A$ 中 $k$ 个 $\beta$ 原孔为源集 $S$，令 $Y\subset B$ 为其外短镜像，$H'_A=(H\cap A)\setminus S$，$H'_B=(H\cap B)\cup Y$。

供体满足 $r\le5$，或 $A$ 存在一个五维坐标半面，其中 $H'_A$ 的两色孔数之差绝对值至多一。接收体 $B$ 存在一个内坐标切分 $Z,T$。对 $V\in\{Z,T\}$，令 $H_V=H'_B\cap V$、$Y_V=Y\cap V$、$q_V=|Y_V|$。要求 $q_V\ge1$，且
$$
 |H_V\cap\alpha|-|H_V\cap\beta|=2q_V.
$$
还要求每个五维带标记配置 $(H_V,Y_V)$ 有如下局部接口：对每个孔集恰为 $H_V$ 的 $K(V)$ 匹配，存在恰覆盖 $V\setminus Y_V$ 的简单圈，包含规定匹配，其余圈边均短。

则存在包含 $M$ 的全短 Hamilton 圈。给定上述孔几何与接口，结论对每个实现该孔集的短匹配及所有立方体自同构像成立。本稿为待独立审计的证明及有限应用。

## 使用的局部工具

供体平衡圈 $C_r$ 在 $0\le r\le5$ 时适用。近平衡 $C6^+$ 要求六维总孔平衡和一个五维半面的孔差绝对值至多一。两个接口均对任意完全图规定匹配成立，输出 $64$ 点圈，新增边均短。 [平衡圈及其依赖](R7_CYCLE_DONOR_THREE_BRIDGE_UNIVERSAL.md) · [审计](R7_CYCLE_DONOR_THREE_BRIDGE_UNIVERSAL_REVIEW.json) · [近平衡圈](<E:/新问题/research/seven_directions/R7_NEAR_BALANCED_BLOCKS.md>) · [审计](<E:/新问题/research/seven_directions/R7_NEAR_BALANCED_BLOCKS_REVIEW.json>)

| 工具 | 五维带标记适用域 | 证明及审计 |
|---|---|---|
| `Q5_A_ALL` | 两色孔数为 $(m,m+2)$，省略一个指定多数孔 | [差二归约](<E:/新问题/research/six_directions/Q5_HIGHER_HOLE_REDUCTION.md>) · [归约审计](<E:/新问题/research/six_directions/Q5_HIGHER_HOLE_REDUCTION_REVIEW.json>) · [A10 全部闭合](<E:/新问题/research/six_directions/Q5_A10_FULL_CLOSURE.md>) · [最终审计](<E:/新问题/research/six_directions/Q5_A10_FULL_REVIEW.json>) |
| `Q5_T44` | 四个同色孔，任意两个指定省略 | [证明](<E:/新问题/research/six_directions/T44_Q5_CLOSURE_DRAFT.md>) · [审计](<E:/新问题/research/six_directions/T44_Q5_CLOSURE_REVIEW.json>) |
| `Q5_T15_RANK_nn` | $(1,5)$ 孔型，精确对应秩表编号 `nn` 的带标记轨道 | [十五行证明](<E:/新问题/research/six_directions/Q5_T15_RANK_BATCH_PROOF.md>) · [审计](<E:/新问题/research/six_directions/Q5_T15_RANK_BATCH_REVIEW.json>) |
| `Q5_T15_CORE_nn` | $(1,5)$ 孔型，精确对应八孔终审 JSON `complete_marked_core_registry` 的 `nn` 行。轨道编号来自解析几何表。 | [解析几何](<E:/新问题/research/six_directions/t15_analytic_geometry.json>) · [24 个完整局部核心的终审](<E:/新问题/research/six_directions/EIGHT_HOLE_FULL_REVIEW.json>) · [审计范围](<E:/新问题/research/six_directions/EIGHT_HOLE_FULL_REVIEW.md>) |
| `Q5_T15_SPLIT_AXIS_i` | $(1,5)$ 孔型，平移唯一少数孔至 $0$ 后，坐标 $i$ 的位 $1$ 面含五个多数孔中的两个，两个省略标记分居两面 | [五维分面推论](<E:/新问题/research/six_directions/Q4_RICH_GLUING.md>) · [审计](<E:/新问题/research/six_directions/Q4_RICH_GLUING_REVIEW.json>) |

各项均保任意完全图规定匹配，所列省略点之外恰好全覆盖，其余圈边均短。两个 T15 表的行号各有自己的编号体系。带标记同构同时运输整个孔集与省略集。

## 证明

### 1. 具有规定内跨边的接收圈

设 $F$ 是 $K(B)$ 上任意孔集为 $H'_B$ 的匹配，至少有一条内跨边。令 $F_Z,F_T$ 为面内部分，$C_{\mathrm{in}}$ 为内跨匹配，$P_Z,P_T$ 为其端点集。两面各有偶数个孔，因为孔数之差为偶数。于是
$$
 |C_{\mathrm{in}}|=32-|H_Z|-2|F_Z|
$$
为正偶数。在 $P_Z$ 上任取完全配对 $D_Z$。$F_Z\cup D_Z$ 的孔恰为 $H_Z$，故可调用 $Z$ 接口得到避 $Y_Z$ 的圈。删去非空配对 $D_Z$ 得一组路径，端点恰为 $P_Z$，各路径的点集分割 $Z\setminus Y_Z$。接回每条内跨边，为每个端点接上一枚互异的 $P_T$ 叶点，压缩这些路径为 $P_T$ 上的带标签配对 $R_T$。$F_T\cup R_T$ 的孔恰为 $H_T$，故 $T$ 接口给出避 $Y_T$ 的圈。按标签展开 $R_T$，其各路径内部互不相交且均在 $Z\setminus Y_Z$，得到恰覆盖 $B\setminus Y$ 的简单圈。它恢复全部 $F$，新增边均来自两面接口的短边。

### 2. 供体配对与路径压缩

记 $M_A,M_B$ 为外切两侧的原面内匹配，$C_{\mathrm{out}}$ 为原外跨匹配，$X_A,X_B$ 为其端点集。每个 $y\in Y$ 与原孔源相邻，所以独立性保证 $y$ 被覆盖。它的唯一外方向短邻点是原孔源，故其原配偶边 $yq_y$ 属于 $M_B$。各 $q_y$ 互异、均为 $\beta$ 点，并避开 $X_B\cup Y$。令
$$
 N=M_B\setminus\{yq_y:y\in Y\},\qquad U_{\mathrm{eff}}=X_B\cup\{q_y:y\in Y\}.
$$

$A$ 中 $\alpha$ 非孔比 $\beta$ 非孔多 $k$，而 $M_A$ 每条短边覆盖两色各一点。因此 $X_A$ 中 $\alpha$ 端点比 $\beta$ 端点多 $k$，$|X_A|\ge k$ 且 $|X_A|\equiv k\pmod 2$。集合 $U=X_A\cup S$ 由互异点组成，大小为正偶数，且避开 $M_A$ 的端点。对 $U$ 的每个完全配对 $D$，$M_A\cup D$ 是完全图规定匹配，孔集为固定的 $H'_A$，两色各有 $r$ 个孔。按供体条件调用 $C_r$ 或 $C6^+$，得到包含该规定匹配的 $64$ 点圈，新增边均短。

从供体圈删去 $D$，得到端点恰为 $U$ 的路径森林。接回 $C_{\mathrm{out}}$ 并加入 $S$ 到 $Y$ 的短桥，使端点移到 $X_B\cup Y$，再接入每条 $yq_y$，使端点移到 $U_{\mathrm{eff}}$。由于各附加端点互异，路径仍两两点不交，即使一条路径两端都接到标记。其内部点恰为 $A\cup Y$。把每条路径压成带标签的边，得配对 $R_{\mathrm{eff}}$。$N$ 避开有效端口，$F_B=N\cup R_{\mathrm{eff}}$ 是 $K(B)$ 上的匹配，孔集恰为 $H'_B$。

上述端点迁移定义双射 $U\to U_{\mathrm{eff}}$。因此可事先指定 $U_{\mathrm{eff}}$ 上的配对 $D_{\mathrm{eff}}$，以其逆像为 $D$。两个配对 $D_{\mathrm{eff}}$ 与所得 $R_{\mathrm{eff}}$ 的带标签并连通，因为它由单个供体圈收缩删 $D$ 后的路径，再经双射运输而得。相同端点对仍按两条标签计。

### 3. 选配对以保证正内跨并展开

若 $N$ 有内跨边，则任取 $D_{\mathrm{eff}}$，该边都保留在 $F_B$ 中。否则，每个内面 $V$ 的点由 $H_V$、$N$ 的面内端点和 $U_{\mathrm{eff}}\cap V$ 分割。面内有两色各 $16$ 点，$N$ 的每条边覆盖两色各一点，故
$$
 |U_{\mathrm{eff}}\cap V\cap\beta|-|U_{\mathrm{eff}}\cap V\cap\alpha|=2q_V>0.
$$
两面各有正偶数个有效端口。选 $D_{\mathrm{eff}}$ 全在各自内面配对。若 $R_{\mathrm{eff}}$ 也全在各自内面，则两个非空端口块分别在两组配对下封闭，违背并图连通性。所以 $F_B$ 必有内跨边。

由 §1 取得 $B\setminus Y$ 上含 $F_B$ 的单圈。按标签展开全部 $R_{\mathrm{eff}}$，恢复 $A\cup Y$ 的每个点一次。路径内部互不相交且均在接收圈之外，因此仍是一个简单圈，点数为 $(64-k)+(64+k)=128$。它保留 $N$，展开恢复 $M_A$、全部原外跨边及各 $yq_y$。所有人工配对已删，全部压缩边均按标签展开。圈中新增边来自各局部圈的短边或 $k$ 条短桥。立方体自同构保持切分、孔计数、标记及短边。$\square$

## E14 的 35 个固定余表代表

以 $H=L\cup(127\mathbin{\mathrm{xor}}V)$ 读取固定代表。每次选有向外切、$k$ 枚源和内切，在两内面要求各有 $q>0$ 标记且原多数孔比原少数孔多 $q$。投影时按坐标升序保留其余五位，T15 以少数孔平移到 $0$，再用全部五坐标置换同时规范化多数孔及标记。E14 满足 $r+s+k=7$，因此这里 $r\le5$。

首轮 $k=3,4$ 使用差二避一、T44 及十五个 T15 秩表轨道，仅 $k=3$ 命中 ID 2。扩张轮只测 $k=3$，加入完整解析核心表及已审几何分面接口，得到下表 17 个见证。$j$ 为外切坐标，$b_A$ 为供体面的位，$\beta$ 用 Hamming 重量奇偶 $0,1$ 表示，$i$ 为内切坐标。局部工具按两内面的位 $0,1$ 排列。完整投影、镜像及文件哈希随机器表保存。 [固定输入](R7_MU3_FINAL_REMAINDER.json) · [探查脚本](R7_CONTROLLED_CYCLE_DONOR_PROBE.py) · [具体计划](R7_CONTROLLED_CYCLE_DONOR_PROBE.json)

| ID | $j$ | $b_A$ | $\beta$ | $i$ | $S$ | 内面工具 |
|---:|---:|---:|---:|---:|---|---|
| 2 | 1 | 1 | 0 | 3 | 63,83,119 | rank 12 / A |
| 3 | 1 | 1 | 0 | 3 | 63,83,119 | core 14 / A |
| 4 | 1 | 1 | 0 | 3 | 63,83,119 | core 23 / A |
| 5 | 5 | 0 | 1 | 0 | 1,2,7 | A / core 24 |
| 7 | 5 | 0 | 1 | 0 | 1,2,67 | A / split 0 |
| 8 | 1 | 1 | 0 | 2 | 27,95,123 | core 13 / A |
| 10 | 5 | 0 | 1 | 0 | 1,2,67 | A / core 14 |
| 17 | 0 | 1 | 0 | 3 | 45,83,119 | core 23 / A |
| 19 | 5 | 0 | 1 | 0 | 1,2,67 | A / split 0 |
| 20 | 0 | 1 | 0 | 2 | 27,45,123 | core 24 / A |
| 21 | 1 | 1 | 0 | 4 | 15,95,111 | core 13 / A |
| 22 | 0 | 1 | 0 | 2 | 27,53,123 | core 13 / A |
| 24 | 5 | 0 | 1 | 0 | 1,2,67 | A / core 14 |
| 25 | 5 | 0 | 1 | 0 | 1,2,67 | A / core 14 |
| 28 | 5 | 0 | 1 | 1 | 1,2,67 | A / core 14 |
| 29 | 0 | 1 | 0 | 4 | 15,45,63 | core 19 / A |
| 32 | 5 | 0 | 1 | 0 | 1,2,69 | A / core 23 |

未命中 ID 为 $1,6,9,12,13,14,15,16,18,23,197,200,202,203,204,205,206,209$。其中仅 ID 1 具有 $k=3$ 的孔数与标记分布，首个尚缺接口的 T15 配置规范形为少数孔 $0$、多数孔 $\{7,11,19,28,31\}$、省略对 $\{28,31\}$。所有 35 个代表均无 $k=4$ 的内切计数计划。本探查只枚举孔几何，未调用匹配、Hamilton 或秩求解。表中的 17 项是供独立审计的应用，其他 $k$、整域覆盖及余表登记超出本稿范围。
