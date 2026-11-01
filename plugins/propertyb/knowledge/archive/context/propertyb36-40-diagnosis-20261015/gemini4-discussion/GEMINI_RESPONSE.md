### 已证结论一：原命题成立（存在满足条件的 9 点集 $S$）

**证明：**
设 $H=(V,E)$ 为 $25$ 个顶点、$35$ 条边的简单 $5$-一致超图，且对任意不同顶点 $x,y\in V$ 有 $\lambda(x,y)\ge 1$。定义超额共度 $w(x,y):=\lambda(x,y)-1\in \mathbb{Z}_{\ge 0}$。

1. **度数与超额预算：**
   对每个 $x\in V$，由双计数得 $\sum_{y\neq x}\lambda(x,y)=4d(x)$。因 $|V\setminus\{x\}|=24$ 且 $w(x,y)\ge 0$，顶点 $x$ 的总超额共度为
   $$s(x):=\sum_{y\neq x}w(x,y)=4d(x)-24=4(d(x)-6)\ge 0,$$
   故所有顶点满足 $d(x)\ge 6$。记 $V_d=\{x\in V:d(x)=d\}$，$n_d=|V_d|$，$n_{\ge 8}=\sum_{d\ge 8}n_d$。由 $\sum_{x\in V}d(x)=5|E|=175=7|V|$ 得
   $$0=\sum_{x\in V}(d(x)-7)=-n_6+\sum_{d\ge 8}(d-7)n_d\ge -n_6+n_{\ge 8},$$
   故 $n_{\ge 8}\le n_6$，从而 $n_7=25-n_6-n_{\ge 8}\ge 25-2n_6$。
   对任意 $x\in V_6$ 有 $s(x)=0$，即对一切 $y\neq x$ 均有 $\lambda(x,y)=1$；对任意 $x\in V_7$ 有 $s(x)=4$。若 $n_6\ge 9$，任取 $V_6$ 中 $9$ 点即得全共度为 $1$ 的子集。以下设 $n_6\le 8$。

2. **最大独立集与第一层划分：**
   在 $V_7$ 上定义支撑简单图 $G=(V_7,E_G)$，其中 $xy\in E_G \iff w(x,y)\ge 1$。取 $G$ 的一个**最大独立集** $I\subseteq V_7$，记 $a=|I|=\alpha(G)$。若 $n_6+a\ge 9$，取 $V_6$ 及 $I$ 中 $9-n_6$ 个点即可，其两两共度全为 $1$。以下设 $a\le 8-n_6$。

   对 $x\in V_7\setminus I$，记 $w(x,I)=\sum_{u\in I}w(x,u)$。因 $I$ 为极大独立集，必有 $w(x,I)\ge 1$。令
   $$R_1=\{x\in V_7\setminus I: w(x,I)=1\},\qquad R_{\ge 2}=\{x\in V_7\setminus I: w(x,I)\ge 2\}.$$
   则 $|R_1|+|R_{\ge 2}|=n_7-a$，且由 $I$ 与 $V_7\setminus I$ 之间的权和上界得
   $$|R_1|+2|R_{\ge 2}|\le \sum_{x\in V_7\setminus I}w(x,I)\le \sum_{u\in I}s(u)=4a.$$
   消去 $|R_{\ge 2}|$ 得
   $$|R_1|=2(|R_1|+|R_{\ge 2}|)-(|R_1|+2|R_{\ge 2}|)\ge 2(n_7-a)-4a=2n_7-6a\ge 50-4n_6-6a.$$

3. **团性质与贪心选点证明：**
   对每个 $u\in I$，令 $C_u=\{x\in R_1: w(x,u)=1\}$，则 $R_1=\bigsqcup_{u\in I}C_u$。
   - **断言：每个 $C_u$ 在 $G$ 中都是团。**
     若存在不同顶点 $x,y\in C_u$ 使 $xy\notin E_G$，因 $x,y$ 在 $I\setminus\{u\}$ 中均无邻点，集合 $(I\setminus\{u\})\cup\{x,y\}$ 将成为 $G$ 中大小为 $a+1$ 的独立集，与 $a=\alpha(G)$ 最大性矛盾。
   - 于是对任意 $x\in C_u$，其在 $C_u\setminus\{x\}$ 中的每个点 $y$ 都满足 $w(x,y)\ge 1$，故
     $$4=s(x)\ge w(x,u)+\sum_{y\in C_u\setminus\{x\}}w(x,y)+\sum_{z\in R_1\setminus C_u}w(x,z)\ge 1+(|C_u|-1)+|N_G(x)\cap (R_1\setminus C_u)|,$$
     即 $|C_u|+|N_G(x)\cap (R_1\setminus C_u)|\le 4$。

   现在 $R_1$ 中贪心构造 $B$：只要未删空，任取剩余点 $x\in C_u$ 选入 $B$，并从候选池中删去 $C_u\cup (N_G(x)\cap (R_1\setminus C_u))$。每步至多删去 $4$ 个点，故可选出 $B\subseteq R_1$ 满足：每个 $C_u$ 至多含 $B$ 中一点、$B$ 在 $G$ 中独立，且
   $$|B|\ge \left\lceil\frac{|R_1|}{4}\right\rceil \ge \left\lceil\frac{50-4n_6-6a}{4}\right\rceil = \left\lceil\frac{25-3a}{2}\right\rceil - n_6.$$
   令 $U=V_6\cup I\cup B$，则 $U\subseteq V_6\cup V_7$，且因 $a\le 8$，
   $$|U|=n_6+a+|B|\ge a+\left\lceil\frac{25-3a}{2}\right\rceil = \left\lceil\frac{25-a}{2}\right\rceil \ge \left\lceil\frac{25-8}{2}\right\rceil = 9.$$
   在 $U$ 中，$V_6$ 与所有点共度为 $1$，$I$ 与 $B$ 内部共度均为 $1$，而 $x\in B\cap C_u$ 仅与唯一的 $u\in I$ 满足 $\lambda(u,x)=2$，其余跨边共度全为 $1$。故共度为 $2$ 的点对构成匹配。任取 $S\subseteq U$ 且 $|S|=9$ 即证。$\blacksquare$

---

### 已证结论二：不能加强为“9 点两两共度全为 1”（显式超图反例）

**反例构造（无需任何未证猜测）：**
取顶点集 $V=\mathbb{F}_5^2$（$|V|=25$）：
- 令 $E_0$ 为有限仿射平面 $\mathrm{AG}(2,5)$ 的全部 $30$ 条仿射直线（每条含 $5$ 点，任意两点恰共一条直线）；
- 令 $E_1=\{f_i : i\in \mathbb{F}_5\}$，其中 $f_i=\{(x,x^2+i): x\in \mathbb{F}_5\}$ 为 $5$ 条互不相交的平移抛物线。

因二次曲线与任意仿射直线在 $\mathbb{F}_5^2$ 中至多交于 $2$ 点，故 $E_0\cap E_1=\emptyset$。因此 $H=(V,E_0\cup E_1)$ 是 $25$ 点、$35$ 边的简单 $5$-一致超图，每个顶点度数为 $6+1=7$，且：
$$\lambda(u,v)=\begin{cases}2, & \text{若 }u,v\text{ 属于同一条 }f_i,\\ 1, & \text{若 }u,v\text{ 属于不同 }f_i.\end{cases}$$
由抽屉原理，任何两两共度全为 $1$ 的子集 $S\subseteq V$ 在每个 $f_i$ 中至多取 $1$ 点，故 $|S|\le 5<9$。因此结论无法加强为两两共度全为 $1$。

