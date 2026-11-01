### 0. 前轮 4.1 节上界纠错

前轮恒等式 (2)–(4) 本身准确，但 4.1 节在 $n=24,\delta\ge 7,|R_0|=1$ 时写“$d_H(r)-4\le 4$”误用了 $G$ 内部点的度界 $d\le 8$。实际上外点 $r\in R_0$ 可吸收全局盈余（$M=35$ 时 $E=7 \implies d_H(r)\le 14$；$M=34$ 时 $d_H(r)\le 9$），故式 (3) 在 $|R_0|=1$ 时仅给出 $3n_1+2n_2+n_3\le d_H(r)-4\le 10$（或 $5$）。本轮不再使用该错误常数。

---

### 1. 23 点 $(4\text{six}+1\text{seven}+18\text{eight})$ 核心结构与精确度分解

设 $K=\{u_1,u_2,u_3,u_4\}$（按 $C_4$ 顺序 $u_1u_2u_3u_4$），$G=K\cup\{z\}$，$W=V\setminus G$（$|W|=18$）。
由每个 $u_i$ 的星自由部分划分 $V\setminus K$，且 $\{z\}=G\setminus K$，知对每个 $i\in\mathbb{Z}_4$：
$$W = T_{i-1,i} \sqcup T_{i,i+1} \sqcup Q_{i,1} \sqcup Q_{i,2} \sqcup Q_{i,3} \quad (3+3+4+4+4=18), \tag{1}$$
且对任意 $w\in W$ 及 $u_i\in K$，恒有 **$\lambda(u_i,w)=1$**。
对任一外点 $w\in W$，记 $\tau_T(w)=|\{i\in\mathbb{Z}_4:w\in T_{i,i+1}\}|$。因相邻三元集不交（$T_{i-1,i}\cap T_{i,i+1}=\emptyset$），必有 $\tau_T(w)\in\{0,1,2\}$。
- $w$ 出现在 $\tau_T(w)$ 条环对边 $E_{i,i+1}$ 中（每条覆盖 $K$ 中 $2$ 点），故出现在 $4-2\tau_T(w)$ 条单点迹边 $S_{i,j}=\{u_i\}\cup Q_{i,j}$ 中；
- 因此 $w$ 在 $18$ 条空迹边 $\mathcal{E}_0=\{f\in\mathcal{E}:f\cap K=\emptyset\}$ 中的度数精确为：
  $$d_{\mathcal{E}_0}(w) = d_H(w) - \bigl(\tau_T(w) + 4 - 2\tau_T(w)\bigr) = d_H(w) - 4 + \tau_T(w). \tag{2}$$
将 $\mathcal{E}_0$ 分为含 $z$ 的边 $\mathcal{E}_z$（$d_H(z)-1\in\{6,7\}$ 条）与真 zero-$G$ 边 $\mathcal{E}_{00}$（$19-d_H(z)\in\{11,12\}$ 条）。

---

### 2. 精确横截空间 $\Omega_i$ 与 $|B_f|=4$ 负集的自动免疫引理

设 $H-G$ 有合法染色 $\chi=(G\cup R_0,B_0)$，$G$ 全红，$W=R_0\sqcup B_0$。固定 $u_i\in K$，记正四集族 $\mathcal{A}_{u_i}=\{Q_{i,j}:Q_{i,j}\subseteq B_0\}$，条数 $a_i=|\mathcal{A}_{u_i}|\in\{0,1,2,3\}$（若某 $a_i=0$，单翻 $u_i\to\text{Blue}$ 即得 $H$ 的合法染色；以下设 $a_i\ge 1$）。

**引理 1（单 six 翻转的精确横截消减与负集过滤）：**
将 $u_i$ 由红翻蓝，并在乘积空间 $\Omega_i=\prod_{Q\in\mathcal{A}_{u_i}}Q$（共 $4^{a_i}$ 个横截集，每个 $R\in\Omega_i$ 恰从各 $Q\in\mathcal{A}_{u_i}$ 取 $1$ 点，故 $|R|=a_i\le 3$）中等概率取 $R$ 由蓝翻红，则：
1. **环边自动免疫：** $E_{i-1,i}$ 与 $E_{i,i+1}$ 各含蓝点 $u_i$ 与红点 $u_{i-1}$（或 $u_{i+1}$），在 $K$ 内部已异色，不产生正约束或负约束。
2. **负 4-集与跨区负集完全失效：** 记 $U_i^+=\bigsqcup_{Q\in\mathcal{A}_{u_i}}Q\subseteq B_0$。任一避开 $u_i$ 的边 $f\in\mathcal{F}_{u_i}^-$（共 $29$ 条），其负集 $B_f=f\cap B_0$ 能阻塞某个 $R\in\Omega_i$（即 $\exists R\in\Omega_i, B_f\subseteq R$）**当且仅当**同时满足：
   - **(i)** $|B_f|\le a_i\le 3$（**所有满足 $|B_f|=4$ 的边阻塞数为 $0$**）；
   - **(ii)** $B_f\subseteq U_i^+$（凡含 $T_{i-1,i}\cap B_0$、$T_{i,i+1}\cap B_0$ 或 $Q_{i,j}\setminus U_i^+$ 中蓝点的边，阻塞数皆为 $0$）；
   - **(iii)** 对每个 $Q\in\mathcal{A}_{u_i}$ 有 $|B_f\cap Q|\le 1$。
   当 (i)–(iii) 成立且 $|B_f|=s\in\{1,2,3\}$ 时，$B_f$ 在 $\Omega_i$ 中阻塞的比例恰为 **$4^{-s}\in\{\frac{1}{4},\frac{1}{16},\frac{1}{64}\}$**。

*证明：* 因 $Q_{i,1},Q_{i,2},Q_{i,3}$ 两两不交，任一 $R\in\Omega_i$ 满足 $|R|=a_i\le 3, R\subseteq U_i^+$ 且 $|R\cap Q|=1$（$\forall Q\in\mathcal{A}_{u_i}$），故 $B_f\subseteq R$ 必满足 (i)–(iii)，且固定 $s$ 个不同 $Q$ 中的点后剩余自由度为 $4^{a_i-s}$。$\blacksquare$

---

### 3. 双守恒律与条件子分支 $|R_0|\le 2$ 的完整闭合证明

记 $\tau_{i,i+1}=|T_{i,i+1}\cap R_0|\in\{0,1,2\}$（因 $|T_{i,i+1}\cap B_0|\ge 1$），并记 $\tau_T(R_0)=\sum_{r\in R_0}\tau_T(r)=\tau_{12}+\tau_{23}+\tau_{34}+\tau_{41}\le\min(2|R_0|,8)$。

**引理 2（$Q$-亏损与 $\mathcal{E}_0$-亏损精确守恒律）：**
对任意合法初态 $(G\cup R_0,B_0)$，所有边 $f\neq G$ 满足 $1\le |B_f|\le 4$，且：
1. **12 条单点迹边 $S_{i,j}$ 的总亏损：** 由式 (1) 对 $i=1,2,3,4$ 求和，得：
   $$\sum_{i=1}^4\sum_{j=1}^3 (4-|B_{S_{i,j}}|) = \sum_{i=1}^4\sum_{j=1}^3 |Q_{i,j}\cap R_0| = 4|R_0| - 2\tau_T(R_0). \tag{3}$$
2. **18 条空迹边 $\mathcal{E}_0$ 的总亏损：** 对 $f\in\mathcal{E}_z$ 有 $4-|B_f|=|f\cap R_0|$；对 $f\in\mathcal{E}_{00}$ 有 $4-|B_f|=|f\cap R_0|-1\ge 0$。结合式 (2) 求和得：
   $$\sum_{f\in\mathcal{E}_0}(4-|B_f|) = \sum_{r\in R_0}(d_H(r)-4) + \tau_T(R_0) - (19-d_H(z)) \le 4|R_0| + \tau_T(R_0) - 11. \tag{4}$$
   （注：$d_H(z)=7$ 时全 $W$ 皆 $8$ 度，上式精确等于 $4|R_0|+\tau_T(R_0)-12$；$d_H(z)=8$ 时 $\le 4|R_0|+\tau_T(R_0)-11$。）

**定理 3（$|R_0|\le 2$ 分支完全闭合）：**
若 $H-G$ 存在满足 $|R_0|\le 2$ 的合法染色（特别地，当 $\tau(\mathcal{E}_{00})\le 2$ 时由前轮极小 $R_0$ 剪枝必可取到），则 $H$ 必可通过翻转某 $u_i\in K$ 及至多 $3$ 个外蓝点完成二染色。

*证明：* 由式 (4) 左端 $\ge 0$ 及 $\tau_T(R_0)\le 2|R_0|$，有 $6|R_0|-11\ge 0\implies |R_0|\ge 2$（$|R_0|=1$ 不可能合法染 $\mathcal{E}_{00}$）。
当 $|R_0|=2$ 时，$\tau_T(R_0)\le 4$，由式 (4) 知 $\tau_T(R_0)\in\{3,4\}$ 且 $\sum_{f\in\mathcal{E}_0}(4-|B_f|)\le \tau_T(R_0)-3\le 1$：
- **情形 A（$\tau_T(R_0)=4$）：** 代入式 (3) 得 $\sum_{i,j}(4-|B_{S_{i,j}}|)=8-8=0$，故全部 $12$ 条 $S_{i,j}$ 均满足 $|B_{S_{i,j}}|=4$（从而 $a_1=3$，且其余 $9$ 条 $S_{k,j}$ 在 $\Omega_1$ 中阻塞数为 $0$）。又因 $\sum_{f\in\mathcal{E}_0}(4-|B_f|)\le 1$，$18$ 条空迹边中至多 $1$ 条满足 $|B_f|=3$，其余 $\ge 17$ 条满足 $|B_f|=4$（阻塞数为 $0$）。故在 $\mathcal{F}_{u_1}^-$ 的 $29$ 条边中，仅 $E_{23},E_{34}$ 与至多 $1$ 条 $|B_f|=3$ 的空迹边能阻塞 $\Omega_1$，总阻塞比例 $\le \frac{1}{4}+\frac{1}{4}+\frac{1}{64}=\frac{33}{64}<1$，$\Omega_1$ 必有解。
- **情形 B（$\tau_T(R_0)=3$）：** 代入式 (4) 得 $\sum_{f\in\mathcal{E}_0}(4-|B_f|)\le 0$，故 **全部 $18$ 条空迹边皆满足 $|B_f|=4$（在任意 $\Omega_i$ 中阻塞数全为 $0$）**。代入式 (3) 得 $\sum_{i,j}(4-|B_{S_{i,j}}|)=8-6=2$（且因 $|R_0|=2$，每条 $S_{i,j}$ 有 $|B_{S_{i,j}}|\ge 2$）。取 $a_i=3$ 的 $u_i\in K$，其余 $9$ 条 $S_{k,j}$ 中至多 $2$ 条满足 $|B_f|\in\{2,3\}$，连同 $E_{i+1,i+2},E_{i+2,i+3}$，在 $\Omega_i$ 中总阻塞比例 $\le \frac{1}{4}+\frac{1}{4}+\frac{1}{16}+\frac{1}{16}=\frac{5}{8}<1$，必有解。$\blacksquare$

---

### 4. 多 six 同时改色机制与 $|R_0|\ge 3$ 的精确剩余障碍

1. **对角双 six 同时翻蓝（$\{u_1,u_3\}\to\text{Blue}$）：**
   此时 $G$ 为 $2$ 蓝 $3$ 红，且 **$C_4$ 的全部 $4$ 条环边 $E_{12},E_{23},E_{34},E_{41}$ 在 $K$ 上皆为 $1$ 蓝 $1$ 红**，使全部 $4$ 个三元集 $T_{i,i+1}$ 从负约束中彻底消失；正四集为 $\mathcal{A}_{u_1}\cup\mathcal{A}_{u_3}$。
2. **三 six 同时翻蓝（$K\setminus\{u_i\}\to\text{Blue}$，配合 $R'\subseteq R_0\to\text{Blue}$）：**
   $G$ 含 $3$ 蓝 $2$ 红（$u_i,z$ 留红）。此时仅需从 $R_0$ 中选少量红点翻蓝以消除 $\mathcal{E}_{00}$ 中的全红负约束，其对偶亏损由 $|B_0|=18-|R_0|$ 控制。
3. **$|R_0|\ge 3$ 的精确障碍：**
   当 $|R_0|\ge 3$ 时，式 (3) 与式 (4) 呈反向消长：$\tau_T(R_0)$ 大则 $S_{k,j}$ 几乎全为 $|B_f|=4$，但 $\mathcal{E}_0$ 中 $|B_f|\le 3$ 增多；$\tau_T(R_0)$ 小则反之。要闭合 $|R_0|\ge 3$，必须用引理 1(ii) 的跨区条件 $B_f\subseteq U_i^+$：因为每条含 $B_0\setminus U_i^+$（含 $T_{i-1,i}\cap B_0, T_{i,i+1}\cap B_0$ 及 $3-a_i$ 个非正四集中的蓝点，总数 $\ge 5-a_i$ 个蓝点）的空迹边在 $\Omega_i$ 中阻塞数严格为 $0$，需对 $i=1,2,3,4$ 平均证明落在 $U_i^+$ 内部的空迹边亏损不足以耗尽 $\Omega_i$。此步尚未在全称下证毕。
