# 原始模型回应

threadId: a0384e32-0db0-41a2-ad60-fa0d06c0222b

### 21点、35边、唯一六度点且无七度点分支（`UNIQUE6_NO7`）的独立静态对抗审阅

**审阅范围与结论：** 本次对 [UNIQUE6_NO7_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_no7/UNIQUE6_NO7_PROOF.md)、[POOL_SELECTION_LEMMA.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_no7/POOL_SELECTION_LEMMA.md)、[replay.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_no7/replay.py)、[REPLAY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_no7/REPLAY.json) 及 [SIX_DOMAIN.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_no7/SIX_DOMAIN.json)、[SIX_DP.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/unique6_no7/SIX_DP.json)、[UNIT_PAIRS.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-high/UNIT_PAIRS.json) 进行只读静态对抗核查（未重新执行代码，基于既有独立重放记录与项目条件排列／真实坏对配额及弱对偶引理接口）。**在所述条件接口下，从实际超图 $H$ 的全单位八度池 $N\ge 7$、三至五邻点共同域、五点残型向全池的结构提升引理，到六邻点 270 标签／3 轨道严格闭合的完整推导链条严密无缺口。** 本结论仅覆盖 $v=21, M=35$、点对覆盖、唯一 6 度点且其余点度数 $\ge 8$ 的分支，不声称含 7 度点、多 6 度点或全局 $m(5)\ge 36$ 已完成。

---

### 核心环节对抗核查

1. **全单位八度邻点池 $U$ 的大小下界 $N=|U|\ge 7$：**
   设唯一 6 度点为 $x$，其余 20 个外点度数 $\ge 8$。由点对覆盖，$\sum_{v\ne x}(\lambda(x,v)-1)=4\times 6-20=4$，故至多 4 个外点满足 $\lambda(x,v)\ge 2$；同时外点总度数为 $175-6=169$，满足 $\sum_{v\ne x}(d(v)-8)=169-160=9$，故至多 9 个外点度数 $\ge 9$。因此，全体满足 $\lambda(x,u)=1$ 且 $d(u)=8$ 的外点池 $U$ 必满足 $N=|U|\ge 20-4-9=7$。此处 $U$ 取为**全池**，不依赖任何额外选点假设。

2. **前置 `(6,8,8)` 门与三／四／五邻点共同域的无损衔接：**
   - 对任意 $y\ne z\in U$，三锁 $\{x,y,z\}$ 的非负精确迹由 $c=\lambda(y,z)\in\{1,\dots,8\}$ 与 $\tau=I_{xyz}\in\{0,1\}$ 唯一确定（满足 $\mu_y=\mu_z=7-c+\tau\ge 0$ 及 $c-\tau\ge 0$，共 $7+8=15$ 型）。`UNIT_PAIRS.json` 的严格证书排除了所有 $c\ge 4$ 以及 $(c,\tau)=(3,0)$，仅余 $c\in\{1,2\}$（$\tau\in\{0,1\}$）和 $(c,\tau)=(3,1)$。
   - 对 $U$ 的任意 $s\in\{3,4,5\}$ 元子集 $Y$，若 $H$ 不可染，则 $Y$ 的每个 $(s-1)$ 元子集视图必落在上一层的非严格残域中，且所有视图共享**同一个**实际中心边划分 $\Pi|_Y$（块大小 $\le 4$、块数 $\le 6$）与全部低阶包含数 $I_A$。当 $s=5$ 时，简单五元性强制五高包含数 $I_Y\in\{0,1\}$ 且六点包含数 $I_{\{x\}\cup Y}=0$。`replay.py` 以全包含数 Möbius 反演独立重建 `THREE`（116 标签/40 轨道→19 残）、`FOUR`（3133 标签/232 轨道→45 残）、`FIVE`（15940 标签/245 轨道→26 残），与发现域完全一致。

3. **五点视图向全池 $U$（$N\ge 7$）提升的量词与图论证明（`POOL_SELECTION_LEMMA.md`）：**
   `replay.py`（第 79–82 行）直接核实全部 26 个五邻点残轨道均满足两条共同性质：(a) $\Pi|_Y$ 的块大小分拆仅属于 $\{3+2,\ 2+2+1,\ 2+1+1+1,\ 1+1+1+1+1\}$（特别排除了 `4+1` 与 `3+1+1`）；(b) 高对共度均 $\in\{1,2\}$，且共度 1 的高对在 $Y$ 上构成的诱导子图 $G[Y]$ 仅为空图或四叶星 $K_{1,4}$。
   - **全池 $\Pi$ 块大小 $\le 2$ 的核查：** 因 $x$-边为 5 元，全池 $\Pi$ 每块原本 $\le 4$。若存在 4 点块 $B$，由 $N\ge 7$ 任取一点 $u\in U\setminus B$ 即得禁止的 `4+1` 五点视图；若存在 3 点块 $B$，则 $|U\setminus B|=N-3\ge 4$，任取两点 $u,v\in U\setminus B$ 与 $B$ 组成五点视图，因 `3+1+1` 被禁止、仅 `3+2` 允许，$u,v$ 必须同块。由 $u,v$ 的任意性，$U\setminus B$ 的全部 $\ge 4$ 个点必须落入同一块 $B'$，但这会给出 $|B'|=4$（取 $B'$ 加 $B$ 中一点即得 `4+1`）或 $|B'|>4$（超中心边容量），均矛盾。故全池 $\Pi$ 的每块至多 2 点。
   - **全池共度 1 图 $G$ 为空或完整星 $K_{1,N-1}$ 的核查：** 若 $G$ 非空，取一边扩充为五点集 $Y_0=\{a,b,c,d,e\}$，则 $G[Y_0]\cong K_{1,4}$（设中心为 $a$）。对任意池中其余点 $z\in U\setminus Y_0$，五点集 $\{a,b,c,d,z\}$ 中 $a$ 已有 3 条星边，故其诱导 $K_{1,4}$ 的中心必仍为 $a$，从而 $az\in E(G)$ 且 $bz,cz,dz\notin E(G)$；再看 $\{a,b,c,e,z\}$ 得 $ez\notin E(G)$。对任意两个池中其余点 $z,w\in U\setminus Y_0$（$N\ge 7$ 时可取），在 $\{a,b,c,z,w\}$ 中 $a$ 已与 $b,c,z,w$ 相连（度 4），故必有 $zw\notin E(G)$。因此 $G$ 在全池 $U$ 上是以 $a$ 为中心的完整星。
   - **选 6 点结论：** 从 $U$ 中删去至多 1 点（星中心 $a$），余下至少 $N-1\ge 6$ 个点两两共度均为 2，且 $\Pi$ 限制在其上仅有大小 $\le 2$ 的块。

4. **六邻点共同域（270 标签／3 轨道）与六高简单性边界：**
   对选出的 6 个八度单位邻点 $Y=\{y_1,\dots,y_6\}$，其全部 6 个五元子集视图必须落在 26 残型中满足“高对共度全为 2 且 $\Pi$ 块大小 $\le 2$”的 13 个残轨道内。在 `replay.py` 的 `extend(domains['FIVE'], 6, keep, maxblock=2)` 中：
   - 因五点划分块数 $\le 5<6$，第 6 点作为新单点块或并入原单点块（保持 `maxblock=2`）遍历了 $Y$ 上所有块大小 $\le 2$ 且块数 $\le 6$ 的划分；
   - **六高与七点包含数为 0：** 因 $H$ 为 5 元超图，任何边不可能包含 6 个或 7 个顶点，故 $I_Y=0$（`n>=6: upper=0`）与 $I_{\{x\}\cup Y}=0$（`centerfull=0`）是五元性的精确恒等结果，无需额外简单性假设；
   - 7 点全包含数 Möbius 反演保留全部非负库存，精确得到 270 个有标签库存（3 个 $S_6$ 轨道），其代表在固定位置下的排列上界分别为 $127/132$、$557/572$、$977/1001<1$，经 $S_6$ 逆置换运输直接给出原超图 $H$ 的合法二染色。

---

### 附：前次 $a=5$ 组外星建议中交集表述的精确修正

在前次关于 25 点 $a=5$ 六锁 $S=G\cup\{x\}$（$x\notin G$）的建议中，应严格区分**锁迹交集**与**整边交集**：跨组共度 $\lambda(x,g)=1$（$\forall g\in G$）仅证明过外点 $x$ 的任意两条不同边 $e_1,e_2$ 在 $G$ 上的迹不交，从而它们在六锁集合 $S$ 上的**锁迹交集**必为 $e_1\cap e_2\cap S=\{x\}$（故在枢轴 $x$ 处不存在因共享第二锁点而产生权为 0 的跨锁槽）；但 $e_1$ 与 $e_2$ 在整图 $V$ 中的**完整交集** $e_1\cap e_2$ 仍可在 $x$ 所属外组内共享第二个自由点 $y\in V\setminus S$（因同组共度为 2）。两条 $x$-边是否构成真实坏 link 对（即在 $V\setminus\{x\}$ 中有公共点）由避锁配额决定：当 $\Pi_x$ 含三元块 $T^*$（$|T^*|=3$）时，避开 $R=T^*$ 的 $f=6$ 条 $x$-边在 $24-3=21$ 个外点上的关联超额确实保证 $q_{T^*}(x)=\lceil(24-21)/3\rceil=1$ 个真实坏 link 对，但该配额目前仅作为可保留的候选机制，尚未宣称已产生新的严格排除结果。
