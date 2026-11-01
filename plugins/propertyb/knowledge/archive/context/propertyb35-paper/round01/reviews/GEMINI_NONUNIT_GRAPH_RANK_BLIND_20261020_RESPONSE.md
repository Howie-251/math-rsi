### 1. 通用秩引理 $r(\Gamma) \ge m - n + 2$ 的严格证明

**证明：**
设 $A \in \{0,1\}^{m \times n}$ 为 $m$ 个互异 $k$-元子集的特征向量矩阵，每行和为 $k$，即 $A\mathbf{1}_n = k\mathbf{1}_m$。考虑对称矩阵
$$M := AA^T - J_m = AA^T - \mathbf{1}_m\mathbf{1}_m^T.$$
1. **半正定性与核空间等价（利用 $n < k^2$）**：
   对任意 $x \in \mathbb{R}^m$，由 $\mathbf{1}_n^T(A^T x) = k(\mathbf{1}_m^T x)$ 及 $\mathbb{R}^n$ 上的 Cauchy–Schwarz 不等式，有
   $$k^2(\mathbf{1}_m^T x)^2 \le \|\mathbf{1}_n\|_2^2 \|A^T x\|_2^2 = n \|A^T x\|_2^2.$$
   因此
   $$x^T M x = \|A^T x\|_2^2 - (\mathbf{1}_m^T x)^2 \ge \left(1 - \frac{n}{k^2}\right)\|A^T x\|_2^2.$$
   因 $n < k^2$，故 $1 - n/k^2 > 0$。这证明 $M \succeq 0$，且
   $$Mx = 0 \iff x^T M x = 0 \iff A^T x = 0, \quad \text{即 } \ker(M) = \ker(A^T).$$
2. **连通分量分块直和**：
   设 $\Gamma$ 的连通分量为 $C_1, \dots, C_c$，大小为 $s_i = |C_i|$。若 $e, f$ 属于不同分量，则 $ef \notin E(\Gamma)$，故 $|e \cap f| = 1 \implies M_{ef} = 0$。因此 $M = \mathrm{diag}(M_1, \dots, M_c)$ 为分块对角阵，从而 $\ker(M) = \bigoplus_{i=1}^c \ker(M_i)$。对每个分量 $C_i$，限制在 $C_i$ 上的子矩阵 $A_{C_i}$ 满足 $\ker(M_i) = \ker(A_{C_i}^T)$，故
   $$r_i := \mathrm{rank}(M_i) = \mathrm{rank}(A_{C_i}), \qquad \sum_{i=1}^c r_i = \mathrm{rank}(M) = \mathrm{rank}(A) \le n.$$
3. **小分量秩下界与 $m > n$ 排除退化情形**：
   由于 $A$ 的行是互异的权 $k$（$k \ge 2$）$\{0,1\}$-向量：
   - 任意1行非零（$s_i=1 \implies r_i=1$）；
   - 任意2行不共线（$s_i=2 \implies r_i=2$）；
   - 任意3行线性无关：若 $\mathbf{1}_{f_3} = \alpha \mathbf{1}_{f_1} + \beta \mathbf{1}_{f_2}$，取 $u \in f_1 \setminus f_2$ 与 $v \in f_2 \setminus f_1$ 及非共线性迫使 $\alpha = \beta = 1$，两边求和得 $k = 2k$ 矛盾。故 $s_i \ge 3 \implies r_i \ge 3$。
   综上，对每个分量恒有 $r_i - 1 \ge \min(s_i - 1, 2)$，求和得
   $$n - c \ge \sum_{i=1}^c (r_i - 1) \ge \sum_{i=1}^c \min(s_i - 1, 2).$$
   若右端和 $\le 1$，则所有 $s_i \in \{1, 2\}$，此时每个分量均有 $r_i = s_i$，导致 $m = \sum s_i = \sum r_i \le n$，与 $m > n$ 矛盾。因此右端和 $\ge 2$，即 $c \le n - 2$，从而
   $$r(\Gamma) = m - c \ge m - n + 2. \quad \square$$

---

### 2. 实际接口、扩森林、数值与量词核验

* **参数调用**：$n=20, k=5, m=29$ 满足 $k \ge 2, n=20 < 25=k^2, m=29 > 20=n$，引理直接给出 $r(\Gamma) \ge 29 - 20 + 2 = 11$。
* **平衡染色计数**：在 $\Omega = \binom{[20]}{10}$（$|\Omega| = \binom{20}{10} = 184756$）中，单边全红/全蓝坏事件 $|B_e| = 2\binom{15}{5} = 6006$，29边总计 $29 \times 6006 = 174174$。对 $|e \cap f| = j$：
  - $j=0$：同色 $2\binom{10}{0}=2$ 加异色 $2\binom{10}{5}=504$，共 $506$；
  - $j \in \{1,2,3,4\}$：必同色，$|B_e \cap B_f| = 2\binom{10+j}{j}$，依次为 $22, 132, 572, 2002$。全部精确无误。
* **拟阵扩森林与 Hunter 扣除**：四交子图 $\Gamma_4 \subseteq \Gamma$（因 $4 \neq 1$）。在图拟阵 $M(\Gamma)$ 中，若 $r(\Gamma_4) \ge 4$，任取4条四交森林边 $F_4$，由拟阵扩张性质必可在 $\Gamma$ 中扩充为11边森林 $F_\Gamma$（新增 $11-4=7$ 条 $\Gamma$-边，其 $j \in \{0,2,3,4\}$，权重 $\ge \min(506,132,572,2002)=132$），再在 $K_{29}$ 中补 $28-11=17$ 条边（权重 $\ge 22$）成生成树 $T$。由 Hunter 生成树并界：
  $$\left|\bigcup_{i=1}^{29} B_{e_i}\right| \le 174174 - (4 \times 2002 + 7 \times 132 + 17 \times 22) = 174174 - 9306 = 164868.$$
* **量词与同一染色交集**：只要好事件 $C \subseteq \Omega$ 定义在**同一20点集 $(10,10)$ 平衡染色样本空间 $\Omega$** 上且 $|C| \ge 164896$，则使 $\bar{H}$ 无单色边且属于 $C$ 的染色数为
  $$\left|C \setminus \bigcup_{i=1}^{29} B_{e_i}\right| \ge |C| - \left|\bigcup_{i=1}^{29} B_{e_i}\right| \ge 164896 - 164868 = 28 > 0,$$
  量词方向完全正确（需确保调用处 $C$ 与 $\bar{H}$ 共享同一顶点集标号且未对 $C$ 额外作不等价重标号）。

