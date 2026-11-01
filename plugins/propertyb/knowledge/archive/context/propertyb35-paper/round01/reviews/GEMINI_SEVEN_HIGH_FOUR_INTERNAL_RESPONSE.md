**HERO — 24点七高点四内部边整支归约与八正四集修复（8门）静态对抗核查报告**

本次仅做静态数学与代码逻辑审阅，**未执行任何程序或 Lean**。

---

### 1. 顶层分流与新一／二三迹连接核查
* **共同预算与内部缺失图**（[TWENTYFOUR_SEVEN_HIGH_FOUR_INTERNAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_FOUR_INTERNAL.md)）：
  24点35边、$\delta\ge 7$、$|P|=7$ 迫 $P$ 全8度、$L$（17点）全7度；无全7度边迫每边交 $P$（无零 $P$ 迹）。点对覆盖迫每点 $p\in P$ 内部次数 $c_p\le 3$（否则余4边在 $L$ 容量 $\le 16<17$），故4条内部五边的缺失对构成无孤点7点4边简单图，度序列必为 $(2,1,1,1,1,1,1)$，重命名后 $\mathcal M=\{01,02,34,56\}$，$S=\{1,\dots,6\}$ 内部次数全为3且 $\mathcal M|_S=\{34,56\}$ 最大度为1。31条非内部边的 $P$ 盈余为 $(56-20)-31=5$。有四迹走既有双划分匹配支；无四迹则 $n_2+2n_3=5$，完整分为 $(n_2,n_3)\in\{(5,0),(3,1),(1,2)\}$。
* **纯五条二迹 $(5,0)$**（[TWENTYFOUR_PURE_FIVE_PAIR_TRACE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_PURE_FIVE_PAIR_TRACE.md)）：
  $p\in S$ 的 $L$ 覆盖容量 $20-s_p\ge 17\implies s_p\le 3$，且 $5\le\sum_{p\in S}s_p\le 10$。按 $S$ 中零度点数分 $0,\ge 2,1$ 三类解析选出 $u,v\in S$，满足 $uv\notin\mathcal M, m_G(u,v)=0, t=s_u+s_v\in\{2,3\}$，精确落入 $(8,3,18)$（8门）或 $(7,2,19)$（7门）。
* **一条三迹 $(3,1)$**（[TWENTYFOUR_ONE_TRIPLE_TRACE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_ONE_TRIPLE_TRACE.md)）：
  容量 $20-2\mathbf{1}_{p\in T}-d_J(p)\ge 17\implies A=T\cap S$（$|A|\in\{2,3\}$）中每点 $d_J(u)\le 1$，$|B|=|S\setminus A|\in\{4,3\}$。无论是 $\exists u\in A, d_J(u)=1$（在 $|B|\ge 3$ 中避开1个 $J$ 邻点和至多1个 $\mathcal M$ 邻点）还是 $A$ 在 $J$ 中全零度（3条无环边迫 $\exists v\in B, d_J(v)\ge 1$，在 $|A|\ge 2$ 中避开至多1个 $\mathcal M$ 邻点），均得 $u\in A,v\in B$ 使 $uv\notin\mathcal M, m_J(u,v)=0, 1\le d_J(u)+d_J(v)\le 3$。三迹 $T$ 恰含1蓝2红已 proper，非内部多迹数 $h=1+d_J(u)+d_J(v)\in\{2,3,4\}$ 给出 $(10-h, 4-h, 17+h)=(8,2,19),(7,1,20),(6,0,21)$。
* **两条三迹 $(1,2)$**（[PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/low_edge/k7_no_four_trace/two_triples/PROOF.md)）：
  容量 $20-2r_p-q_p\ge 17\implies r_p\le 1$，故 $A=T_1\cap S$ 与 $B=T_2\cap S$ 不交且 $|A|,|B|\ge 2$，给出 $\ge 4$ 个跨池对，减去 $\mathcal M|_S$ 至多2对及唯一二迹 $e$ 至多1对，必有 $u\in A,v\in B$ 使 $uv\notin\mathcal M, \{u,v\}\neq e$。两条三迹各含1蓝2红已 proper；按 $e$ 含0或1蓝点精确得 $(8,1,20)$ 或 $(7,0,21)$。
* **负四集缩三元子集**：三支中凡负约束总数为21者，将多余负四集替为任意三元子集，索引数不变、逐点总出现不增，且避开三元子集蕴含避开原四集，与7门/8门接口完全吻合。

---

### 2. 八正四集修复（8门）逐项核查
核查 [EIGHT_POSITIVE_FOUR_SET_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_POSITIVE_FOUR_SET_REPAIR.md) 及配套 [SMALL_POSITIVE_FAMILY_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/low_edge/k7_no_four_trace/SMALL_POSITIVE_FAMILY_REPAIR.md)、[OCC_THREE_REDUCTION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/OCC_THREE_REDUCTION.md)：
* **最大正出现 $\le 2$**：由占用耦合上界得 $3(7/16)^3+18(7/16)^4 = 29841/32768 < 1$。
* **最大正出现 $k\ge 4$**：$k\ge 6$ 与 $k=5$ 直接闭合；$k=4$ 四余集不交时 $3\cdot 16+18\cdot 4=120<256$；有交点 $y$ 恰覆盖2集时，删交集（$|U_0\cap V_0|=t\le 3$）后 $a=4-t\in\{1,2,3,4\}$，堵数 $\le a(a-1)+(a-1)=a^2-1<a^2$（含 $a=1$ 亦严密成立）。
* **最大正出现 $k=3$（固定 $x\in R$，$r+b\le 4$）**：
  * **余五族仍有三重点 $y$**：$a=4-t\ge 2$ 时堵数 $\le 2a-1+s(a-2)\le a^2-a+1<a^2$；唯一等号型 $a=1,t=3$ 迫 $x,y$ 各自正3、负三3、负四1（度7饱和，其余 $\le 17$ 个负四集均不含 $x,y$）。改染 $y$ 蓝、保留 $x$ 红，含 $y$ 的4个负集自动满足，余五正集变为3个三集与2个四集，调用五小正集引理（重合点分支 $5<27$，不交分支 $24\cdot 4=96<243$）在 $L\setminus\{x,y\}$ 上得 $R'$，拼回 $\{x\}\cup R'$ 完全严密。
  * **余五族最大出现 $\le 2$（五标签交多重图 $J$，$\Delta(J)\le 4, E=20-|U|\ge 4$）**：
    * $M_2\ge 7$：每个二匹配 $M$ 留单标签 $w_M$，私有点贡献权1、图边点贡献权 $1/2$，故 $C_3=\sum_M(4-\frac{1}{2}d_J(w_M))\ge 2M_2\ge 14$，严格大于四点红集堵界 $4r+(3-r)+b\le 7+2r\le 13$。
    * $M_2=0$：非孤立支撑仅星或三角。星形 $E=4$ 给 $C_4\ge 256-3^4=175>69$；三角形 $K=ij+ik+jk\in[5,12]$ 给 $16K\ge 80>69$。
    * $1\le M_2\le 6$：由 $\sum_v\binom{d_J(v)}{2}\le 3E$ 得 $M_2\ge E(E-7)/2$，排除 $E\ge 9$，锁定有限域 $\Delta(J)\le 4, 4\le E\le 8, 1\le M_2\le 6$。由于 $|U|\le 16$ 且任两点至多盖4个正标签（留一个正四集 $A_i$ 未盖），扩为四点横截数至多 $\binom{14}{2}-\binom{10}{2}=46$；三点扩展 $\le 13$，四点扩展 $\le 1$。五点红集统一堵界为 $46r+13(3-r)+13b+(18-b)=57+33r+12b\le 105+21r\le 168$。
    * 静态核查 [five_graph_catalogue.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/five_graph_catalogue.py) 与 [INDEPENDENT_COUNT_REPLAY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/INDEPENDENT_COUNT_REPLAY.py)：两套独立枚举器一致生成5307个有标签向量、$S_5$ 取商得86个轨道，四点子集直接枚举与32项容斥一致给出 $\min C_4=178>168$。

---

### 3. 四项总结回答
1. **实际读取的文件**：
   * [TWENTYFOUR_SEVEN_HIGH_FOUR_INTERNAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_FOUR_INTERNAL.md)
   * [TWENTYFOUR_PURE_FIVE_PAIR_TRACE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_PURE_FIVE_PAIR_TRACE.md)
   * [TWENTYFOUR_ONE_TRIPLE_TRACE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_ONE_TRIPLE_TRACE.md)
   * [two_triples/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/low_edge/k7_no_four_trace/two_triples/PROOF.md)
   * [k7_four_trace/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/low_edge/k7_four_trace/PROOF.md)
   * [EIGHT_POSITIVE_FOUR_SET_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_POSITIVE_FOUR_SET_REPAIR.md)
   * [SEVEN_POSITIVE_FOUR_SET_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_POSITIVE_FOUR_SET_REPAIR.md)
   * [SMALL_POSITIVE_FAMILY_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/low_edge/k7_no_four_trace/SMALL_POSITIVE_FAMILY_REPAIR.md)
   * [OCC_THREE_REDUCTION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/OCC_THREE_REDUCTION.md)
   * [five_graph_catalogue.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/five_graph_catalogue.py)、[INDEPENDENT_COUNT_REPLAY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/INDEPENDENT_COUNT_REPLAY.py)、[INDEPENDENT_COUNT_REPLAY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/INDEPENDENT_COUNT_REPLAY.json)（前80行）
2. **新一／二三迹连接是否正确**：**完全正确**。容量不等式、候选池构造、蓝对避开 $\mathcal M$ 与全蓝二迹、三迹恰含一蓝点自动 proper、负四集缩为三元子集的保度加强及原染色返回均严密闭合。
3. **8门计算承担什么依赖**：仅承担最大正出现恰为3、余五族最大出现 $\le 2$ 且 $\Delta(J)\le 4, 4\le E\le 8, 1\le M_2\le 6$ 这一个局部五标签多重图域（5307个有标签图 / 86个 $S_5$ 轨道）上四点横截数 $C_4\ge 178$ 的有限整数计数依赖；不依赖原超图 $H$ 枚举、负约束位置枚举或 $P$ 端40968图目录。
4. **是否发现实质缺口**：**未发现任何实质数学缺口或条件误用**（此局部整支闭合不代表整个24点或 $m(5)\ge 36$ 完成）。
