threadId: fded2cad-1a8d-4b2a-8313-00577078e29e

HERO

### 一、实际读取范围与执行声明

本次静态对抗审阅已完整读取以下文件，**未修改任何文件，未执行任何 Python 脚本、Shell 命令或 Lean 构建**；占用乘积引理（[RANDOM_TRANSVERSAL_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md)）作为上一轮已核验通过的明确导入直接调用：
1. [FIVE_SPARSE_POSITIVE_SMALL_NEGATIVE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SPARSE_POSITIVE_SMALL_NEGATIVE_REPAIR.md)（全文第 1–185 行，含五正四集主定理、四正四集推论、以及末节 $\le 3$ 个负二集的四项参数族推论）
2. [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_THREE_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_THREE_TRIPLES.md)（全文第 1–42 行，$r=3$ 三个三点高迹解析归约）
3. [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_FOUR_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_FOUR_TRIPLES.md)（全文第 1–38 行，$r=4$ 四个三点高迹解析归约）
4. [CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/three_internal/sparse_positive_independent_20261020/CHECK.py)（第 1–52 行）与 [CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/three_internal/sparse_positive_independent_20261020/CHECK.json)（第 1–50 行，静态核对标量有理数复算公式与输出）

---

### 二、[FIVE_SPARSE_POSITIVE_SMALL_NEGATIVE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SPARSE_POSITIVE_SMALL_NEGATIVE_REPAIR.md) 证明与算术核查

1. **负二集去重等价性与度约束单调性（逻辑核查）**
   - 若两个不同负索引具有完全相同的二元底集 $F=\{u,v\}$，合并为单一代表元后，避开条件 $F\not\subseteq R$ 在逻辑上完全等价；合并操作不改变任何正集，仅减少或保持负二集个数 $t_2$ 及各点的总带索引出现次数 $\le 7$。
   - **关键推论**：去重后所有负二集作为二元子集两两不同，因此**任意两个固定重复正点 $\{x,y\}$ 之间至多存在 $1$ 个负二集**。该性质在 $(2,2)$ 与 $(3,2)$ 两种 profile 中被合法调用，无多重边漏洞。

2. **正重复盈余 $\le 3$ 的 7 种 Profile 完备性（逻辑核查）**
   - 对 5 个正四集且 $|\bigcup_{i=1}^5 A_i|\ge 17$，总正关联数为 $5\times 4=20$，故正重复盈余
     $$\sum_{v\in \bigcup A_i}(a_v-1) = 20 - \Big|\bigcup_{i=1}^5 A_i\Big| \le 3.$$
   - 整数分拆 $\sum (a_v-1) \in \{0,1,2,3\}$ 的全部多重集情形恰为：
     - 盈余 $0$: $\emptyset$（全单点）；
     - 盈余 $1$: $(2)$（1 个二重点）；
     - 盈余 $2$: $(3)$（1 个三重点）或 $(2,2)$（2 个二重点）；
     - 盈余 $3$: $(4)$（1 个四重点）、$(2,2,2)$（3 个二重点）或 $(3,2)$（1 个三重点 + 1 个二重点）。
   - 共 **7 种 profile**，分类穷尽无遗漏。四正四集且并 $\ge 14$ 时盈余 $\le 16-14=2$，对应前 **4 种 profile**；三正四集且并 $\ge 11$ 时盈余 $\le 12-11=1$，对应前 **2 种 profile**。

3. **主定理（$\le 4 N_2, \le 1 N_3, \le 22 N_4, \text{occ}\le 7$）各 Profile 极值与弦斜率（证明+算术核查）**
   - 独立均匀选点下，单点占用率为 $q=1-(3/4)^1=1/4$，$p=1-(3/4)^2=7/16$，$r=1-(3/4)^3=37/64$，$s=1-(3/4)^4=175/256$；基线和 $B_0 = 4q^2+q^3+22q^4 = \frac{1}{4}+\frac{1}{64}+\frac{22}{256} = \frac{45}{128}$。
   - **前 5 种 Profile 标量核对**：
     - $\emptyset$: $\frac{45}{128} < 1$；
     - $(2)$: $4pq+pq^2+22pq^3 = \frac{7}{16}\cdot\frac{90}{64} = \frac{315}{512} < 1$；
     - $(3)$: $4rq+rq^2+22rq^3 = \frac{37}{64}\cdot\frac{90}{64} = \frac{1665}{2048} < 1$；
     - $(2,2)$: 两二重点至多成 1 个负二集（权重 $p^2$），其余 3 个负二集至多含其一（权重 $pq$），得 $p^2+3pq+p^2q+22p^2q^2 = \frac{784+1344+196+1078}{4096} = \frac{1701}{2048} < 1$；
     - $(4)$: 四重点 $x$ 的负出现 $\le 7-4=3$，故至多进入 3 个负二集（其余 1 个负二集 $\le q^2$），得 $3sq+q^2+sq^2+22sq^3 = \frac{8400+1024+700+3850}{16384} = \frac{6987}{8192} < 1$。
   - **$(2,2,2)$ 三个二重点的共享 15 负关联与凸弦斜率分配**：
     - 每个二重点负出现 $\le 7-2=5$，故三点在全部负集中的总关联数 $J_2+J_3+J_4 \le 15$，且逐类容量上限为 $J_2 \le 4\times 2=8$，$J_3 \le 1\times 3=3$。
     - 对含 $j$ 个二重点的负 $k$-集（注意全局仅有 3 个二重点，即使 $k=4$ 也有 $0\le j\le 3$！），由指数函数 $j\mapsto (p/q)^j$ 的凸性，在整数区间 $j\in [0, \min(k,3)]$ 上被连接两端点的割线控制：
       $$p^j q^{k-j} \le q^k + j A_k,\quad A_2 = \frac{p^2-q^2}{2} = \frac{33}{512} = \frac{1056}{16384},\quad A_3 = \frac{p^3-q^3}{3} = \frac{93}{4096} = \frac{372}{16384},\quad A_4 = \frac{p^3q-q^4}{3} = \frac{93}{16384}.$$
     - 因 $A_2 > A_3 > A_4 > 0$，将 15 个关联预算贪心填满前两档 $(J_2,J_3,J_4)=(8,3,4)$ 严格给出最坏上界：
       $$\frac{45}{128} + 8\cdot\frac{33}{512} + 3\cdot\frac{93}{4096} + 4\cdot\frac{93}{16384} = \frac{5760+8448+1116+372}{16384} = \frac{15696}{16384} = \frac{981}{1024} < 1.$$
   - **$(3,2)$ Profile 的共同负索引预算与精确最紧界 $8181/8192$**：
     - 设 $a_x=3, a_y=2$，增量 $\Delta_x = r-q = \frac{21}{64}$，$\Delta_y = p-q = \frac{3}{16}$。对任一负 $k$-集 $F$（$k\ge 2$），将 $(q+\mathbf{1}_{x\in F}\Delta_x)(q+\mathbf{1}_{y\in F}\Delta_y)q^{k-2}$ 完全展开：
       $$q^k + \mathbf{1}_{x\in F}\Delta_x q^{k-1} + \mathbf{1}_{y\in F}\Delta_y q^{k-1} + \mathbf{1}_{\{x,y\}\subseteq F}\Delta_x\Delta_y q^{k-2}.$$
     - 一阶项利用 $q^{k-1}\le q$（因 $k\ge 2$）及负出现上限 $b_x \le 7-3=4$、$b_y \le 7-2=5$，总和 $\le 4q\Delta_x + 5q\Delta_y$。
     - 二阶交叉项：同时含 $\{x,y\}$ 的负索引数至多为 $\min(b_x,b_y)=\min(4,5)=4$。由负二集去重，这 $\le 4$ 个共同负索引中至多 $1$ 个是 $N_2$（权 $q^0=1$），至多 $1$ 个是 $N_3$（权 $q^1=q$），其余至多 $2$ 个是 $N_4$（权 $q^2$），故交叉权和至多为 $1 + q + 2q^2 = 1 + \frac{1}{4} + \frac{1}{8} = \frac{11}{8}$。
     - 合并得精确分式：
       $$\frac{45}{128} + 4\cdot\frac{1}{4}\cdot\frac{21}{64} + 5\cdot\frac{1}{4}\cdot\frac{3}{16} + \frac{21}{64}\cdot\frac{3}{16}\cdot\frac{11}{8} = \frac{2880 + 2688 + 1920 + 693}{8192} = \frac{8181}{8192} < 1.$$
       余量为 $11/8192 > 0$，严格小于 $1$。

4. **四正推论与末节 $\le 3$ 负二集四项推论核查（证明+算术核查）**
   - **四正推论（$4 P_4$, 并 $\ge 14$, $\le 4 N_2, 0 N_3, \le 23 N_4$）**：4 种 profile 依次为 $\frac{87}{256}, \frac{609}{1024}, \frac{3219}{4096}, \frac{3255}{4096} < 1$，全部准确。
   - **末节推论第 1 项（$5 P_4$, 并 $\ge 17$, $\le 3 N_2, \le 3 N_3, \le 21 N_4$）**：
     - 基线 $B_0 = 3q^2+3q^3+21q^4 = \frac{81}{256}$；前 5 种 profile 依次为 $\frac{81}{256}, \frac{567}{1024}, \frac{2997}{4096}, \frac{3297}{4096}, \frac{14175}{16384} < 1$。
     - $(2,2,2)$ 时 $J_2\le 3\times 2=6, J_3\le 3\times 3=9$，因 $6+9=15$ 恰好耗尽 15 个负关联预算（$J_4=0$），上界为 $\frac{81}{256} + 6\cdot\frac{33}{512} + 9\cdot\frac{93}{4096} = \frac{1296+1584+837}{4096} = \frac{3717}{4096} < 1$。
     - $(3,2)$ 时 $\le 4$ 个共同负索引中至多 $1$ 个在 $N_2$（权 $1$）、其余至多 $3$ 个全部落在 $N_3$（权 $q$），故交叉权和至多为 $1+3q = \frac{7}{4}$，总界为
       $$\frac{81}{256} + \frac{21}{64} + \frac{15}{64} + \frac{21}{64}\cdot\frac{3}{16}\cdot\frac{7}{4} = \frac{1296 + 1344 + 960 + 441}{4096} = \frac{4041}{4096} < 1,$$
       余量 $55/4096 > 0$，严格小于 $1$。
   - **末节推论第 2、3、4 项**：
     - 第 2 项（$4 P_4$, 并 $\ge 14$, $3 N_2, 2 N_3, 22 N_4$）最大值为 $(2,2)$ 的 $\frac{1575}{2048} < 1$；
     - 第 3 项（$3 P_4$, 并 $\ge 11$, $3 N_2, 1 N_3, 23 N_4$）最大值为 $(2)$ 的 $\frac{525}{1024} < 1$；
     - 第 4 项（$2 P_4$, 并 $\ge 8$, $\le 3 N_2$, 任意尺寸 $\ge 3$ 负集）正重复盈余 $\le 8-8=0$，两正四集不交，产生 $4\times 4=16$ 个两点候选 $R=\{u,v\}$；因 $|R|=2$，尺寸 $\ge 3$ 的负集不可能包含于 $R$，而 $\le 3$ 个负二集至多堵死 $3 < 16$ 个候选。

---

### 三、两个实际 Caller 与独立复算文件核查

1. [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_THREE_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_THREE_TRIPLES.md)（$r=3$）与 [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_FOUR_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_FOUR_TRIPLES.md)（$r=4$）：
   - **前置分流边界**：在 $|P|=7$（全 8 度）、$|L|=17$（全 7 度）、3 条内部五边 $e_{\text{int},1..3}\subseteq P$ 下，3 对缺失点对至多覆盖 $6$ 个点，故公共交 $C = \bigcap_{i=1}^3 e_{\text{int},i}$ 必非空（$|C|\ge 1$）。若有任何高迹与 $C$ 相交，已由 [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md) 第三覆盖域闭合；故此处仅在**全部 $r$ 条高迹均避开 $C$** 时取任意 $q\in C$ 染蓝、$P\setminus\{q\}$ 染红，前提衔接严密。
   - **无负单点与无零迹边**：因假定非内部高迹恰为 $r$ 条三点 $P$-迹（$|e\cap P|=3 \implies |e\cap L|=2$），故不存在四点 $P$-迹（即无 $L$ 中负单点）；又 $P$ 击中全部 35 条边，无零 $P$-迹边。
   - **$q$ 的外部容量与正集并下界**：$q\in C$ 含于全部 3 条内部边且避开全部高迹，故恰有 $8-3=5$ 条非内部边，分为 $s=d_J(q)$ 条二点 $P$-迹边（在 $L$ 中截出 3 点，因含蓝点 $q$ 与红点 $P\setminus\{q\}$ 已双色）和 $m=5-s$ 条单点 $P$-迹边（在 $L$ 中截出 $m$ 个正四集）。由于 $H$ 覆盖全部点对，$\{q\}$ 与 $L$ 中全部 17 个点的点对只能由这 5 条非内部边提供，每条二点迹边提供 3 个 $L$-点，故 $m=5-s$ 个正四集的并集大小至少为 $17-3s$（自然迫使 $0\le s\le 3$）。
   - **参数匹配与返回原染色**：
     - 当 $r=3$ 时，$n_2=9-6=3, n_1=26$，对 $s\in\{0,1,2,3\}$ 分别得到 $m=5-s\in\{5,4,3,2\}$ 个正四集（并 $\ge 17,14,11,8$）、$3$ 个负二集、$3-s$ 个负三集、$21+s$ 个负四集，逐一精确对应末节推论第 1–4 项。
     - 当 $r=4$ 时，$n_2=9-8=1, n_1=27$，唯一二点迹对 $J$ 给出 $s\in\{0,1\}$，分别得到 $(5 P_4, \text{并}\ge 17, 4 N_2, 1 N_3, 22 N_4)$ 与 $(4 P_4, \text{并}\ge 14, 4 N_2, 0 N_3, 23 N_4)$，精确对应主定理与四正推论。
     - $L$ 中每点在原超图中恰为 7 度，正负集由不同原边在 $L$ 上的迹导出（$s$ 条过 $q$ 的二点迹边已双色被直接丢弃），故逐点带索引总出现 $\le 7$；在 $L$ 上将 $R$ 染红、$L\setminus R$ 染蓝后，内部边（含蓝 $q$ 及 $P\setminus\{q\}$ 中 4 红点）、过 $q$ 的单点迹边（蓝 $q$ + $R$ 中至少一红点）、其余非内部边（$P\setminus\{q\}$ 全红 + $L\setminus R$ 中至少一蓝点）全部双色。
2. [CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/three_internal/sparse_positive_independent_20261020/CHECK.py) 与 [CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/three_internal/sparse_positive_independent_20261020/CHECK.json) 的 `Fraction` 公式及全部有理数结果与纸面推导逐项完全一致。

---

### 四、审阅结论

在本次指定的静态审阅范围内，[FIVE_SPARSE_POSITIVE_SMALL_NEGATIVE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SPARSE_POSITIVE_SMALL_NEGATIVE_REPAIR.md) 及其两个解析调用文件 [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_THREE_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_THREE_TRIPLES.md)、[TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_FOUR_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_ANALYTIC_FOUR_TRIPLES.md) **未发现任何逻辑漏洞或算术错误**。该局部闭合结论成立（不代表其余 8-mixed 门或全局 $m(5)\ge 36$ 命题已闭合）。

