### 审阅结论：**PASS（静态数学审阅通过，无逻辑或算术漏洞）**

- **实际阅读范围**：完整精读目标文件 [TWENTYONE_A1_STRONG_FOREST_RANK.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_STRONG_FOREST_RANK.md)（§1–6 全文，共 143 行），并回读进口源 [TWENTYONE_A1_BALANCED_STAR_FOREST.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md)（§1–6 主证陈述）核对接口条件。
- **是否执行程序**：**否**（纯静态数学与逻辑对抗审阅，未运行任何脚本或外部程序）。
- **结论边界核实**：证明严密确立了“具备 A1 实际角色且不可二染色的 21 点 35 边对覆盖超图 $H$ 必满足 $n_4(H)\le 8$”，明确未宣称整支 A1 闭合或 $m(5)\ge 36$ 已证，且主证明完全独立于 $r(\Gamma)\ge 20$ 的补充材料及未证的 $r(\Gamma)\ge 21$。

---

### 逐项对抗核验与认可理由

#### 1. 删星度谱与从 $\bar{H}$ 到原超图 $H$ 的染色接口（§1 & §5）
- **删星度谱与二阶矩**：删去唯一六度点 $x$ 及其 6 条原边后，余下 $20$ 点上保留 $29$ 条互异五元边（原 $35$ 边互异且余边不含 $x$，故删星后不可能重合）。各点删星度 $\bar{d}(v)=d(v)-\lambda(x,v)$：
  - $p$（1 点，$7-1=6$）与 $B$（4 点，$8-2=6$）共 $5$ 名 6 度点；
  - $U$（5 点，$8-1=7$）共 $5$ 名 7 度点；
  - $V_9$（10 点，$9-1=8$）共 $10$ 名 8 度点。
  度谱恰为 $6^5,7^5,8^{10}$，总度 $5\times 6+5\times 7+10\times 8=145=29\times 5$，$\bar{W}=\sum_v \binom{\bar{d}(v)}{2}=5\times 15+5\times 21+10\times 28=460$，完全准确。
- **同一样本空间与原 $H$ 延伸**：进口 [TWENTYONE_A1_BALANCED_STAR_FOREST.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md#L21-L153) 在余 20 点的全体 $D=\binom{20}{10}=184756$ 个均匀 $10/10$ 染色样本上，对全部 2835 个有效星标签（18 个 $S_6$ 轨道）给出 $|C|\ge 164896$，29 条 $\bar{H}$ 边单色坏事件计数和为 $29\times 6006=174174$，交大小 $j=0,1,2,3,4$ 的同时单色计数依次为 $506,22,132,572,2002$。当最大生成树权 $F>9278$ 时，$D\Pr(C\cap\text{proper}(\bar{H}))\ge |C|-174174+F>0$，故同一概率空间中存在既使 $\bar{H}$ 全部 29 边非单色、又至少有一种颜色不含单色 $x$-link $L_i$ 的 20 点染色；将 $x$ 赋该颜色即可使 6 条 $x\cup L_i$ 与 29 条 $\bar{H}$ 边同时正常二染色。跨星四交边对 $\le 5$（含 $p$ 的唯一 $x$-边为 $0$，其余 5 条各 $\le 1$）及星内四交为 $0$、非 B 时 $\bar{H}$ 四交森林秩 $q\le 3$ 均与进口定理完全一致。

#### 2. 非单交图 $\Gamma$ 孤立点 $\le 3$ 的两型几何（§2）
- **度方程唯一解**：若 $e\in V(\Gamma)$ 在 $\Gamma$ 中孤立，则它与其余 28 条边交大小均恰为 $1$，故 $\sum_{v\in e}\bar{d}(v)=5+28\times 1=33$。设 $e$ 含 $6,7,8$ 度点各 $a,b,c$ 个，由 $a+b+c=5$ 与 $6a+7b+8c=33$ 消去 $c$ 得 $2a+b=7$。因 $a+b\le 5$，故 $a=(2a+b)-(a+b)\ge 2$，结合 $2a\le 7$ 仅有两个非负整数解：$S=(2,3,0)$ 与 $T=(3,1,1)$。
- **同类上界与异类互斥**：任意两条不同孤立边在 $\Gamma$ 中不相邻，故**两两交恰为 1 点**。$S$ 型边在 5 个 7 度点 $V_7$ 上截出三元集，若存在 3 条 $S$ 型边，其 $V_7$-三元集两两交 $\le 1$，容斥给出并集大小 $\ge 3\times 3-3\times 1=6>5=|V_7|$，矛盾；同理 $T$ 型在 $V_6$ 上至多 2 条。
- **排除两 $S$ 两 $T$ 共存**：设 $T_1,T_2$ 为两条 $T$ 型孤立边。它们在 5 元集 $V_6$ 上的两个三元集交集大小至少为 $3+3-5=1$；由 $|T_1\cap T_2|=1$ 知两三元集在 $V_6$ 中恰交于唯一公共点 $w$，并集覆满 $V_6$，且各自在 $V_7$ 中的单点 $u_1,u_2$ 必互异。对任一 $S$ 型孤立边，其 $V_6$-二元集不能含 $w$（否则另一点落入 $(T_1\cup T_2)\cap V_6\setminus\{w\}$，导致 $S$ 与某 $T_i$ 交 $\ge 2$），也不能同属单个 $T_i\cap V_6\setminus\{w\}$，故必从 $T_1\cap V_6\setminus\{w\}$ 与 $T_2\cap V_6\setminus\{w\}$ 各取 1 点。此时 $S$ 与 $T_1,T_2$ 已在 $V_6$ 中各交 1 点，由 $|S\cap T_i|=1$ 知 $S\cap V_7$ 必须避开 $\{u_1,u_2\}$，从而唯一被迫取 $V_7\setminus\{u_1,u_2\}$（大小恰为 $5-2=3$）。若有两条 $S$ 型边，它们共此三元集，交集 $\ge 3>1$，矛盾。故 $I\le 3$ 严密成立。

#### 3. 仿射二进制坐标单射秩界与分块零空间（§3）
- **正定 Pullback 与分块对角**：$A\in\{0,1\}^{29\times 20}$ 每行和为 $5$，故 $J_{29}=\frac{1}{25}AJ_{20}A^T$，从而 $B=AA^T-J_{29}=A(I_{20}-\frac{1}{25}J_{20})A^T$。因 $20<25$，中间矩阵 $Q=I_{20}-\frac{1}{25}J_{20}$ 严格正定（特征值 $1^{19}$ 与 $1/5$），故对任意行子矩阵 $A_C$ 均有 $\ker(B_C)=\ker(A_C Q A_C^T)=\ker(A_C^T)$，即 $\operatorname{rank}(B_C)=\operatorname{rank}(A_C)$，且 $\operatorname{rank}(B)=\operatorname{rank}(A)\le 20$。又 $B_{ef}=|e\cap f|-1$，非对角元非零当且仅当 $ef\in E(\Gamma)$，故 $B$ 按 $\Gamma$ 的连通分量分块对角，各分量块秩之和等于 $\operatorname{rank}(B)\le 20$。
- **仿射维数与坐标投影单射**：设某分量含 $s$ 条互异行 $v_1,\dots,v_s\in\{0,1\}^{20}$，线性成包 $W=\operatorname{span}(v_1,\dots,v_s)$ 维数为 $d$。线性泛函 $\ell(x)=\mathbf{1}_{20}^T x$ 在 $v_i$ 上恒取非零常数 $5$，故差空间 $U=\operatorname{span}(v_i-v_1)\subseteq\ker(\ell|_W)$ 维数至多 $d-1$（实为恰 $d-1$）。由标准线性代数，存在 $d-1$ 个坐标泛函限制在 $U$ 上构成一组基，即坐标投影 $\pi:\mathbb{R}^{20}\to\mathbb{R}^{d-1}$ 在 $U$ 上单射，从而在仿射包 $\operatorname{aff}(v_1,\dots,v_s)=v_1+U$ 上单射。因 $v_i$ 互异且为 $0/1$ 向量，其投影 $\pi(v_i)\in\{0,1\}^{d-1}$ 两两不同，故 $s\le 2^{d-1}$，即 $d\ge 1+\lceil\log_2 s\rceil$。
- **$r(\Gamma)\le 18$ 的排除**：设 $r=r(\Gamma)$，$c=29-r$，非平凡分量数 $h=c-I\ge 26-r$，记 $\ell_i=\lceil\log_2 s_i\rceil$，$L=\sum_{s_i\ge 2}\ell_i\ge h$。由 $\sum_{i=1}^c d_i\ge c+L$ 及 $\operatorname{rank}(B)\le 20$ 得 $L\le 20-c=r-9$。
  - 若 $r\le 17$，则 $26-r\ge 9>8\ge r-9$，与 $26-r\le h\le L\le r-9$ 矛盾；
  - 若 $r=18$，则 $h\ge 8, L\le 9$，故 $\sum_{s_i\ge 2}(\ell_i-1)=L-h\le 1$。这意味着所有非平凡分量满足 $\ell_i=1$（$s_i=2$，块秩 $\ge 2$，块零空间维数 $2-2=0$），至多一个分量满足 $\ell_i=2$（$s_i\in\{3,4\}$，块秩 $\ge 3$，块零空间维数 $\le 4-3=1$），其余孤立点 $s_i=1$ 块秩为 $1$、零空间为 $0$。于是 $\operatorname{nullity}(B)\le 1$，但 $B$ 为 $29$ 阶方阵且 $\operatorname{rank}(B)\le 20$，必有 $\operatorname{nullity}(B)=29-\operatorname{rank}(B)\ge 9$，矛盾。故 $r(\Gamma)\ge 19$ 无需任何分量表或四维超立方体枚举即告成立。

#### 4. 中心化 Gram 矩阵 $B_0$ 的二阶迹预算与整性（§4）
- **投影与半正定秩**：由 $A\mathbf{1}_{20}=5\mathbf{1}_{29}$ 知 $B_0=AA^T-\frac{5}{4}J_{29}=A(I_{20}-\frac{1}{20}J_{20})A^T$。因 $P=I_{20}-\frac{1}{20}J_{20}$ 是到 $\mathbf{1}_{20}^\perp$ 的正交投影，故 $B_0=(AP)(AP)^T\succeq 0$ 且 $\operatorname{rank}(B_0)\le\operatorname{rank}(P)=19$。
- **迹与平方迹展开**：$B_0$ 对角元为 $5-\frac{5}{4}=\frac{15}{4}$，故 $\operatorname{tr}(B_0)=\frac{435}{4}$。利用 $\sum_{j=0}^4 a_j=\binom{29}{2}=406$ 与 $\sum_{j=0}^4(j-1)a_j=460-406=54$，记 $Q=\sum_{j=0}^4(j-1)^2 a_j$，有
  $$\operatorname{tr}(B_0^2)=29\left(\frac{15}{4}\right)^2+2\sum_{j=0}^4\left((j-1)-\frac{1}{4}\right)^2 a_j=\frac{6525}{16}+2Q-54+\frac{406}{8}=\frac{6473}{16}+2Q.$$
- **Cauchy 不等式与整性进位**：对 $B_0$ 的至多 19 个非零特征值用 Cauchy–Schwarz 得 $(\frac{435}{4})^2\le 19(\frac{6473}{16}+2Q)$，同乘 16 化为 $189225\le 122987+608Q$，即 $608Q\ge 66238\implies Q\ge 108+\frac{574}{608}$。因 $Q\in\mathbb{Z}$，故 $Q\ge 109$。再由恒等式 $Q-54=\sum_{j=0}^4(j-1)(j-2)a_j=2a_0+2a_3+6a_4\ge 55$，两边除以 2 并利用左端整性 $a_0+a_3+3a_4\in\mathbb{Z}$，严密推出 $a_0+a_3+3a_4\ge 28$。

#### 5. 嵌套 Kruskal 同树兼容性与 $n_4(H)\le 8$ 闭合（§5）
- **重图秩界**：若 $q=3$，简单四交图边数 $a_4\le\binom{3+1}{2}=6$，代入上式得 $a_0+a_3+a_4\ge 28-2a_4\ge 16>\binom{5+1}{2}=15$，故 $\{0,3,4\}$-交图（heavy 图）森林秩必满足 $h_0\ge 6$。
- **同树兼容与算术收尾**：权值按交型严格单调递减：$w(4)=2002>w(3)=572>w(0)=506>w(2)=132>w(1)=22$，对应的阈值子图构成严格嵌套链 $G_4\subseteq G_{34}\subseteq G_{034}\subseteq G_{0234}=\Gamma\subseteq K_{29}$。Kruskal 贪心算法按权降序在同一棵生成树 $T$ 中依次选出 $q$ 条 4-交边、$r_{34}-q$ 条 3-交边、$h_0-r_{34}$ 条 0-交边、$r_{0234}-h_0$ 条 2-交边及 $28-r_{0234}$ 条 1-交边，Abel 分部求和精确给出同一棵树权
  $$F=616+110r_{0234}+374h_0+66r_{34}+1430q.$$
  由于各项系数均正，代入 $r_{0234}\ge 19$、$h_0\ge 6$、$r_{34}\ge q=3$ 得 $F\ge 616+2090+2244+198+4290=9438>9278$（余量 $160>0$），与非 B 矛盾。从而 $q\le 2$，$a_4\le\binom{3}{2}=3$，结合跨星 $\le 5$ 及星内 $0$ 得 $n_4(H)\le 3+5=8$。全篇推导严密完备。

