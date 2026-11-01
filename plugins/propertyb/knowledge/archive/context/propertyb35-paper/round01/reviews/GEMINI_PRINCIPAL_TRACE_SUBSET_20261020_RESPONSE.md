### 审阅结论：**PASS（独立推导与对抗检查全部通过，无逻辑、符号或算术误差）**

- **实际核对范围**：独立完成 21 点 5-均匀简单超图 $H$ 任意 $N$ 条实际原边子集 $S$ 的主子矩阵（非中心化 $B$ 与中心化 $B_0$）特征值迹不等式推导、$j=0,\dots,4$ 逐项系数核算、五分支 $\max$ 下界与上取整符号检查、以及 35 边非单交图 $\Gamma$ 的度数前缀和（degree-prefix）连接。
- **是否执行程序**：**否**（纯纸面推导与对抗核验，未运行任何脚本）。
- **范围界定**：该不等式是 21 点简单 5-均匀超图任意原边子集 $S$ 的**实际关联主子矩阵必要条件**（在非 B 的 A1 下可结合已证的 $n_4(H)\le 8$ 取 $t=8$ 调用），并非任意抽象简单图的性质，亦未声称已证整个 A1 或 $m(5)\ge 36$。

---

### 1. 独立推导与系数核算

设 $S\subseteq E(H)$ 为 $H$ 的任意 $N$ 条互异五元原边，$A\in\{0,1\}^{N\times 21}$ 为 $S$ 在 21 个顶点上的实际关联矩阵。因每条原边大小恰为 5，有 $A\mathbf{1}_{21}=5\mathbf{1}_N$，故 $J_N=\frac{1}{25}AJ_{21}A^T$。记 $S$ 内无序不同边对中交大小为 $j\in\{0,1,2,3,4\}$ 的对数为 $a_j(S)$，则 $\sum_{j=0}^4 a_j(S)=\binom{N}{2}=N(N-1)/2$，非 1 交边对数 $e(S)=a_0(S)+a_2(S)+a_3(S)+a_4(S)$，且由 $S\subseteq E(H)$ 自然有 $a_4(S)\le n_4(H)\le t$。记
$$Q=\sum_{\{e,f\}\subseteq S}(|e\cap f|-1)^2=\sum_{j=0}^4(j-1)^2a_j(S),\qquad T=\sum_{\{e,f\}\subseteq S}(|e\cap f|-1)=\sum_{j=0}^4(j-1)a_j(S).$$

#### (1) 非中心化主子矩阵 $B=AA^T-J_N$ 与前四项下界
1. **半正定与秩**：$B=A(I_{21}-\frac{1}{25}J_{21})A^T$。因 $I_{21}-\frac{1}{25}J_{21}$ 特征值为 $1^{20}$ 与 $4/25>0$，故严格正定，从而 $B\succeq 0$ 且 $\operatorname{rank}(B)=\operatorname{rank}(A)\le 21$。
2. **独立集与森林边数下界 $N-21$**：$B$ 对角元为 $4$，非对角元为 $|e\cap f|-1$。若 $S_0\subseteq S$ 在非 1 交图 $\Gamma[S]$ 中为独立集，则 $B_{S_0}=4I_{|S_0|}$ 满秩，故 $|S_0|=\operatorname{rank}(B_{S_0})\le\operatorname{rank}(B)\le 21$，即 $\alpha(\Gamma[S])\le\alpha(\Gamma)\le 21$。在 $\Gamma[S]$ 的每个连通分量各取一点得独立集，故连通分量数 $c\le\alpha(\Gamma[S])\le 21$，从而
   $$e(S)\ge N-c\ge N-21.$$
3. **非中心化二阶迹界**：$\operatorname{tr}(B)=4N$，$\operatorname{tr}(B^2)=16N+2Q$。对 $B$ 的至多 21 个非零正特征值用 Cauchy–Schwarz（对任意 $N\ge 0$ 均无条件成立，不足 21 个特征值时补 0 即可）：
   $$(4N)^2\le 21(16N+2Q)\iff 42Q\ge 16N(N-21)\iff Q\ge \frac{8N(N-21)}{21}.$$
   由于 $Q=a_0(S)+a_2(S)+4a_3(S)+9a_4(S)$ 且 $a_j(S)\ge 0$：
   - 由 $Q\le 9(a_0+a_2+a_3+a_4)=9e(S)$ 得 $e(S)\ge\left\lceil\frac{8N(N-21)}{189}\right\rceil$；
   - 由 $Q\le 4(a_0+a_2+a_3)+9a_4=4e(S)+5a_4(S)\le 4e(S)+5t$ 得 $84e(S)+105t\ge 8N(N-21)$，即 $e(S)\ge\left\lceil\frac{8N(N-21)-105t}{84}\right\rceil$。

#### (2) 中心化主子矩阵 $B_0=AA^T-\frac{25}{21}J_N$ 与主不等式
1. **正交投影降秩**：由 $\frac{1}{21}AJ_{21}A^T=\frac{25}{21}J_N$ 得
   $$B_0=AA^T-\frac{25}{21}J_N=A\left(I_{21}-\frac{1}{21}J_{21}\right)A^T.$$
   中间矩阵 $P=I_{21}-\frac{1}{21}J_{21}$ 是到 20 维子空间 $\mathbf{1}_{21}^\perp$ 的正交投影，故 $B_0=(AP)(AP)^T\succeq 0$ 且 $\operatorname{rank}(B_0)\le\operatorname{rank}(P)=20$。
2. **迹与平方迹精确展开**：$B_0$ 对角元为 $5-\frac{25}{21}=\frac{80}{21}$，故 $\operatorname{tr}(B_0)=\frac{80}{21}N$；非对角元为 $j-\frac{25}{21}=(j-1)-\frac{4}{21}$。展开 $\operatorname{tr}(B_0^2)$：
   $$\begin{aligned}
   \operatorname{tr}(B_0^2)&=N\left(\frac{80}{21}\right)^2+2\sum_{\{e,f\}\subseteq S}\left((|e\cap f|-1)-\frac{4}{21}\right)^2\\
   &=\frac{6400N}{441}+2Q-\frac{16}{21}T+N(N-1)\frac{16}{441}=\frac{16N^2+6384N}{441}+2\left(Q-\frac{8}{21}T\right).
   \end{aligned}$$
   由 $\operatorname{rank}(B_0)\le 20$ 及 Cauchy–Schwarz 不等式 $(\operatorname{tr}(B_0))^2\le 20\operatorname{tr}(B_0^2)$：
   $$\frac{6400N^2}{441}\le\frac{320N^2+127680N}{441}+40\left(Q-\frac{8}{21}T\right)\iff 40\left(Q-\frac{8}{21}T\right)\ge\frac{6080N(N-21)}{441}.$$
   两边同除以 $40$（$6080/40=152$），精确得到：
   $$Q-\frac{8}{21}T\ge\frac{152N(N-21)}{441}.$$
3. **乘 21 后的逐项系数与主式**：两边同乘 $21$ 得 $21Q-8T\ge\frac{152N(N-21)}{21}$。左端对交大小 $j$ 的边对系数为 $c_j=21(j-1)^2-8(j-1)=(j-1)(21j-29)$：
   - $j=0:\; (-1)(-29)=29$；
   - $j=1:\; 0$；
   - $j=2:\; 1\times 13=13$；
   - $j=3:\; 2\times 34=68$；
   - $j=4:\; 3\times 55=165$。
   因 $a_j(S)\ge 0$ 且 $\max(c_0,c_2,c_3)=c_3=68$，$c_4-68=165-68=97$，故
   $$21Q-8T=29a_0(S)+13a_2(S)+68a_3(S)+165a_4(S)\le 68e(S)+97a_4(S).$$
   同乘 $21$（$68\times 21=1428$，$97\times 21=2037$）即得主不等式：
   $$1428e(S)+2037a_4(S)\ge 152N(N-21).$$
   再由 $a_4(S)\le t$（系数 $2037>0$）与 $e(S)\in\mathbb{Z}$ 得 $e(S)\ge\left\lceil\frac{152N(N-21)-2037t}{1428}\right\rceil$。

---

### 2. 边界情况、隐藏前提与度数前缀连接检查

1. **无隐藏前提与紧性检查**：推导仅用到 $H$ 是 21 点上的简单 5-均匀超图（保证 $A$ 为 $N\times 21$ 的行重 5 二进制矩阵，且不同边交大小 $\in\{0,1,2,3,4\}$）及 $a_4(S)\le n_4(H)\le t$，**不要求** $S$ 保持点度均匀或点对覆盖。当 $N=21$ 时，射影平面 $PG(2,4)$ 的 21 条五元线两两交 1 点，此时 $e(S)=a_4(S)=0$，主式两边均为 $0$，达到精确相等；当 $0\le N\le 21$ 时，$N(N-21)\le 0$ 且 $t\ge 0$，后四项均 $\le 0$，$\max$ 中的 $0$ 自动生效，无需额外假设 $N>21$。
2. **度数前缀和（Degree-Prefix）无循环连接**：设 35 条原边的非 1 交图 $\Gamma$ 度序列为 $q_1\ge\dots\ge q_{35}$，总边数 $E=\frac{1}{2}\sum_{i=1}^{35}q_i$。删去前 $r$ 个最高度顶点集 $R$（$|R|=r$）后，余下 $S=V(\Gamma)\setminus R$ 是 $N=35-r$ 条实际原边。对 $\Gamma$ 的边按内部与跨集双计数：
   $$\sum_{i=1}^r q_i = 2e(R)+e(R,S) = \big(e(R)+e(R,S)+e(S)\big)+e(R)-e(S) = E+e(R)-e(S).$$
   由简单图性质 $e(R)\le\binom{r}{2}$ 及实际原边子集下界 $e(S)\ge\operatorname{lower}(35-r,t)$，直接给出
   $$\sum_{i=1}^r q_i \le E+\binom{r}{2}-\operatorname{lower}(35-r,t),$$
   逻辑链条单向无循环，全部系数与符号准确无误。

