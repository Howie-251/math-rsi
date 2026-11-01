### 1. 对“任意初态可修”的严格反驳（极大 $R_0$ 阻塞机制）

设 $\chi=(G\cup R_0, B_0)$ 为 $H-G$ 的合法二染色（$G$ 全红，外点分为原红 $R_0$ 与原蓝 $B_0$）。
**观测：** 对任意 $x\in B_0$，存在 $f\in\mathcal{E}\setminus\{G\}$ 使 $B_f=f\cap B_0=\{x\}$（负 1-集），**当且仅当**在初态 $\chi$ 中单独将 $x$ 由蓝翻红会使 $f$ 变为全红边。

- **反例初态构造：** 取 $H-G$ 的任意合法染色后，贪心将 $B_0$ 中所有“单独翻红不产生新全红边”的点并入 $R_0$，直至 $R_0$ **极大**。此时所得 $(G\cup R_0^{\max}, B_0^{\min})$ 仍是 $H-G$ 的合法染色，但对**每一个** $x\in B_0^{\min}$，必存在某边 $f_x\in\mathcal{E}\setminus\{G\}$ 满足 $B_{f_x}=\{x\}$。若这些 $f_x$ 均不交 $g$（例如来自 zero-$G$ 边），则对每个 $x\in B_0^{\min}$ 都有单点负约束 $\{x\}\not\subseteq R$，迫使 $R=\emptyset$，无法命中任何正集 $A\in\mathcal{A}_g$。故**绝不能假设任意初态可修**。

---

### 2. 极值初态选择：最小 $R_0$ 自由剪枝引理

记 zero-$G$ 边集为 $\mathcal{E}_0=\{f\in\mathcal{E}:f\cap G=\emptyset\}$（$m_0=|\mathcal{E}_0|\ge M+4-D_G$，其中 $D_G=\sum_{u\in G}d_H(u)$）。

**引理 1（$R_0$ 单调收缩与私有边性质）：**
在 $H-G$ 的任意合法染色 $(G\cup R_0,B_0)$ 中，任取仍命中全部 $\mathcal{E}_0$ 的子集 $R'_0\subseteq R_0$，令 $B'_0=(V\setminus G)\setminus R'_0\supseteq B_0$，则 $(G\cup R'_0,B'_0)$ **仍是 $H-G$ 的合法染色**，且所有负集 $B'_f=f\cap B'_0\supseteq B_f$ 单调扩大。
*证明：* 对 $f\notin\mathcal{E}_0\cup\{G\}$，因 $f\cap G\neq\emptyset$ 且 $G$ 全红，$f$ 已有红点；而 $f\cap B'_0\supseteq f\cap B_0\neq\emptyset$ 保持有蓝点。对 $f\in\mathcal{E}_0$，由 $R'_0$ 命中 $\mathcal{E}_0$ 及 $B'_0\supseteq B_0$ 知仍异色。$\blacksquare$

**极值规范化：** 取 $R_0$ 为 $\mathcal{E}_0$ 的**极小（或最小基数）横截集**，则：
1. 每个 $r\in R_0$ 必有私有边 $f_r\in\mathcal{E}_0$ 满足 $f_r\cap R_0=\{r\}$（从而 $|B_{f_r}|=4$），故 $|R_0|\le m_0$；
2. 对任意 $f\in\mathcal{E}\setminus\{G\}$，由 $|f|=5$ 有基本恒等式：
   $$4-|B_f| = (|f\cap G|-1) + |f\cap R_0|. \tag{1}$$

---

### 3. 两个核心精确守恒律（正集条数与小负集亏损的全局耦合）

固定七度点 $g\in G_7\subseteq G$（$d_H(g)=7$）。记负约束边集 $\mathcal{F}_g^-=\{f\in\mathcal{E}:g\notin f\}$（共 $M-7$ 条），$n_k(g)=|\{f\in\mathcal{F}_g^-:|B_f|=k\}|$（$k=1,2,3,4$）。将含 $g$ 的 $6$ 条非 $G$ 边分为正四集对应边 $\mathcal{E}_g^+$（$|\mathcal{A}_g|$ 条，满足 $|f\cap G|=1, |f\cap R_0|=0, |B_f|=4$）与其余边 $\mathcal{E}_g^0$（$6-|\mathcal{A}_g|$ 条，每条满足 $|f\cap G|\ge 1$ 且 $|B_f|\ge 1$）。

**定理 1（正集条数—外红点精确守恒律）：**
对每条 $f\in\mathcal{E}_g^0$，由式 (1) 有 $|f\cap R_0|+(|f\cap G|-1)+(|B_f|-1)=3$。对 $f\in\mathcal{E}_g^0$ 求和并利用 $\sum_{f\in\mathcal{E}_g^0}|f\cap R_0|=\sum_{r\in R_0}\lambda(g,r)$，得精确恒等式：
$$3|\mathcal{A}_g| + \sum_{r\in R_0}\lambda(g,r) + \sum_{f\in\mathcal{E}_g^0}(|f\cap G|-1) + \sum_{f\in\mathcal{E}_g^0}(|B_f|-1) = 18. \tag{2}$$
*直接推论：* 因 $\lambda(g,r)\ge 1$ 且后两项非负，恒有 $3|\mathcal{A}_g|+|R_0|\le 18 \implies |\mathcal{A}_g|\le 6-\lceil |R_0|/3\rceil$。**只要 $|R_0|\ge 4$，对所有 $g\in G_7$ 必有 $|\mathcal{A}_g|\le 4$**；仅当 $|R_0|\le 3$ 时才可能出现 $|\mathcal{A}_g|=5$。

**定理 2（小负集亏损精确恒等式）：**
在 $\mathcal{F}_g^-$ 上对式 (1) 求和，利用 $\sum_{f\not\ni g}|f\cap R_0|=\sum_{r\in R_0}(d_H(r)-\lambda(g,r))$ 及 $\sum_{f\not\ni g}|f\cap G|=D_G-7-\sum_{u\in G\setminus\{g\}}\lambda(g,u)$，得小负集加权亏损精确式：
$$3n_1(g)+2n_2(g)+n_3(g) = \sum_{r\in R_0}\bigl(d_H(r)-\lambda(g,r)\bigr) - (M+4-D_G) - \sum_{u\in G\setminus\{g\}}\bigl(\lambda(g,u)-1\bigr). \tag{3}$$
将式 (2) 与式 (3) 相加消去 $\sum_{r\in R_0}\lambda(g,r)$，还得全局耦合式：
$$\bigl(3n_1(g)+2n_2(g)+n_3(g)\bigr) - \sum_{f\in\mathcal{E}_g^0}(|B_f|-1) = 3|\mathcal{A}_g| + \sum_{r\in R_0}d_H(r) - (M+22-D_G). \tag{4}$$

---

### 4. 对 $n=24$（$D_G\le M+1, |G_7|\ge 4$）的降难效应与剩余义务

1. **低 $|R_0|$ 区间自动消除小负集：**
   - 当 $|R_0|=1$（$R_0=\{r\}$）时：由式 (1)，所有 $f\in\mathcal{E}_0$ 满足 $|B_f|=4$，所有 $|f\cap G|=1$ 的边满足 $|B_f|\in\{3,4\}$；仅当 $|f\cap G|\ge 2$ 时才可能有 $|B_f|\le 2$。且式 (3) 直接给出 $3n_1(g)+2n_2(g)+n_3(g)\le (d_H(r)-1)-3\le 4$，故 $n_1(g)\le 1$（至多 1 个负单点集，令其 $\pi_i(x)=0$ 即可消去）。
   - 对 $|G_7|\ge 4$ 平均：任一满足 $|f\cap G|=s\ge 2$ 的边 $f$ 已经命中 $G$ 中 $s$ 个点，故至多在 $5-s$ 个 $g\in G_7$ 的 $\mathcal{F}_g^-$ 中充当负集。
2. **高 $|R_0|$ 区间的正集压缩：**
   当 $|R_0|\ge 4$ 时，定理 1 强制 $|\mathcal{A}_g|\le 4$（若 $|R_0|\ge 7$ 则 $|\mathcal{A}_g|\le 3$）。
3. **当前预算的准确剩余未证义务：**
   式 (2)–(4) 表明小负集亏损由 $\sum_{r\in R_0}(d_H(r)-\lambda(g,r))$ 驱动。对 $|R_0|\in\{2,3\}$（此时 $|\mathcal{A}_g|$ 仍可达 $4$ 或 $5$），将全部负 1-集顶点 $U_1(g)=\{x: \{x\}\in\mathcal{B}_g\}$ 置 $q_x=0$（从正四集中删去 $U_1(g)$）后，需结合 $\sum_{x\in B_0}(a_x-1)_+\le 29-n$ 证明：存在 $g\in G_7$ 使删点后的正集大小仍 $\ge 3$（或退化为 2-集后可继续传递），且剩余负 2-集在点对精确容斥下总概率严格 $<1$。此步尚未闭合。
