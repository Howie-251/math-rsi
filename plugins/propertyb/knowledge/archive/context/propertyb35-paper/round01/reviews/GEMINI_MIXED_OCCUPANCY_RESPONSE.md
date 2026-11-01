threadId: fded2cad-1a8d-4b2a-8313-00577078e29e

**HERO — 静态数学对抗审阅报告：`SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md` 及 `RANDOM_TRANSVERSAL_REPAIR.md` 占用乘积引理**

本次审阅仅针对指定的两个文件进行静态数学推导与精确有理算术复核，**未修改任何文件，未执行任何程序或 Lean**。

---

### 1. 实际读取范围与执行状态
* **实际全文读取**：
  * [SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md)（1–131行，含主定理、实际调用及文末无负三集扩展推论）
  * [RANDOM_TRANSVERSAL_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md)（1–159行，重点核查第19–43行自含占用乘积耦合证明）
* **程序执行状态**：未执行任何 Python 脚本或 Lean 构建；所有分式与不等式均通过精确手工通分独立复算。

---

### 2. 核心数学机制与精确常数对抗核查

#### (1) 独立正选点的自含占用乘积上界（[RANDOM_TRANSVERSAL_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md#L19-L43)）
* **单点重抽耦合的严密性**：各正集独立抽取 $X_i\sim \pi_i$，令 $R=\{X_1,\dots,X_m\}$，$q_x=\Pr(x\in R)$。对 $0<q_x<1$，条件事件 $\{x\notin R\}=\bigcap_{i=1}^m\{X_i\neq x\}$ 下各次抽取仍独立且服从 $\tilde{\pi}_i(\cdot)=\pi_i(\cdot\mid X_i\neq x)$。耦合构造将 $X_i=x$ 的分量独立重抽为 $\tilde{X}_i\sim\tilde{\pi}_i$、其余保留 $\tilde{X}_i=X_i$，逐样本点满足 $R\setminus\{x\}\subseteq \tilde{R}\setminus\{x\}$。故对只依赖 $R\setminus\{x\}$ 的递增事件 $E=\{F\setminus\{x\}\subseteq R\}$，有 $\Pr(E\mid x\notin R)\ge \Pr(E)$，结合全概率公式得 $\Pr(x\in R, E)=\Pr(E)-(1-q_x)\Pr(E\mid x\notin R)\le q_x\Pr(E)$。对 $|F|$ 归纳即得 $\Pr(F\subseteq R)\le \prod_{x\in F}q_x$。该证明完全自含，不依赖正集不相交或原超图边独立。

#### (2) 低出现次数（$\max a_v\le 2$）按正关联收费与精确分数（[SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md#L9-L55) 及 [L100-L116](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md#L100-L116)）
* **AM-GM 的 $1/4$ 因子与逐点度支配**：每个负四集 $B$ 有4个不同顶点，由占用乘积界与四元 AM-GM 得 $\Pr(B\subseteq R)\le \prod_{v\in B}p_v \le \frac{1}{4}\sum_{v\in B}p_v^4$。按负四集索引求和（即使不同索引对应同一集合，每个索引对所属4点的 $b_v$ 各贡献1），并由 $a_v+b_v\le 7$ 得：
  $$\sum_{B\text{ 负四集}}\Pr(B\subseteq R) \le \frac{1}{4}\sum_{v\in L} b_v p_v^4 \le \frac{1}{4}\sum_{v\in L}(7-a_v)p_v^4.$$
  无正出现的点 $a_v=0\implies p_v=0$，对右端贡献为 $0$，从而彻底免除了对 $|L|$ 或全局负四集数量的上界要求。
* **五种正关联类型的 $\alpha,\beta$ 收费核对**：
  设 $\alpha=\frac{5}{2}(\frac{5}{9})^4=\frac{3125}{13122}$，$\beta=\frac{5}{2}(\frac{7}{16})^4=\frac{12005}{131072}$：
  1. 两正3集（$p_v=5/9, 7-a_v=5$）：点代价 $5(5/9)^4 = 2\alpha$（等号）；
  2. 两正4集（$p_v=7/16, 7-a_v=5$）：点代价 $5(7/16)^4 = 2\beta$（等号）；
  3. 一正3、一正4（$p_v=1-\frac{2}{3}\cdot\frac{3}{4}=\frac{1}{2}, 7-a_v=5$）：点代价 $\frac{5}{16}$；因 $\frac{5}{16}-\beta = \frac{28955}{131072}$，且 $28955\times 13122 = 379947510 < 409600000 = 3125\times 131072$，故 $\frac{5}{16} < \alpha+\beta$ 严格成立；
  4. 单一正3集（$p_v=1/3, 7-a_v=6$）：$\frac{6}{81}=\frac{972}{13122} < \frac{3125}{13122}=\alpha$；
  5. 单一正4集（$p_v=1/4, 7-a_v=6$）：$\frac{6}{256}=\frac{3072}{131072} < \frac{12005}{131072}=\beta$。
* **线性极值与两个九位分母常数复算**：
  因 $3\alpha = \frac{3125}{4374} > 4\beta = \frac{12005}{32768} > 0$，设正3集、正4集数为 $r,s$（$r+s\le 7$），则总点代价 $\sum_v(7-a_v)p_v^4 \le 3r\alpha+4s\beta \le 28\beta + r(3\alpha-4\beta)$：
  * **主定理（$r\le 2$，含 $\le 1$ 个负3集）**：保留 AM-GM 的 $1/4$ 因子，且任意点 $p_v\le 5/9$ 使唯一负3集坏概率 $\le (5/9)^3=\frac{125}{729}$。公分母为 $\operatorname{lcm}(8748, 131072) = 3^7\cdot 2^{17} = 286654464$：
    $$\frac{6\alpha+20\beta}{4} + \left(\frac{5}{9}\right)^3 = \frac{3125+1500}{8748} + \frac{60025}{131072} = \frac{4625\times 32768 + 60025\times 2187}{286654464} = \frac{151552000 + 131274675}{286654464} = \frac{282826675}{286654464} < 1.$$
  * **文末扩展（$r\le 4$，无负3集）**：
    $$\frac{12\alpha+12\beta}{4} = 3(\alpha+\beta) = \frac{3125}{4374} + \frac{36015}{131072} = \frac{3125\times 65536 + 36015\times 2187}{286654464} = \frac{204800000 + 78764805}{286654464} = \frac{283564805}{286654464} < 1.$$
  两项精确有理常数完全无误。

#### (3) 高出现次数（$a_x=k\ge 3$）全分流与局部容量界核查
固定 $x$ 红，余 $m\le 7-k\le 4$ 个未击中正集（均避开 $x$，大小3或4）：
* **$m\le 3$**：$m\le 2$（$|R|\le 2$ 或 $9>1$）、$m=3$ 相交（$|R|\le 2$ 或 $3>1$）、$m=3$ 不交（$27 > 4+(7-k)\le 8$）均直接闭合。
* **$m=4$（$k=3$）且余族相交（§3）**：
  * 交点 $y$ 命中 $\ge 3$ 集时 $|R|\le 2$ 或 $3>1$；
  * $y$ 恰命中2集，余 $U,V$（避开 $x,y$，大小 $\ge 3$）：$|U\cap V|\ge 2$ 给 $\ge 2>1$ 份三点候选 $\{x,y,w\}$；$U\cap V=\emptyset$ 给 $\ge 9$ 份四点候选 $\{x,y,u,v\}$，对至多 $\max(4+3, 1+4)=7<9$ 份受堵；
  * $U\cap V=\{w\}$：若 $\{x,y,w\}$ 被唯一负3集堵住，则负3集必等于 $\{x,y,w\}$（从而耗去 $x$ 的1次负出现，使含 $x$ 的负4集至多 $7-3-1=3$ 个）。此时令 $w$ 蓝（禁 $w$）、保持 $x,y$ 红，唯一负3集因含蓝 $w$ 被避开，$U\setminus\{w\},V\setminus\{w\}$ 不交且各大小 $\ge 2$，给出 $\ge 4$ 份四点候选 $\{x,y,u',v'\}$，仅含 $x$ 的 $\le 3$ 个负4集各能堵1份（$3<4$）。（无负3集扩展中 $|U\cap V|\ge 1$ 直接取 $\{x,y,w\}$ 得 $|R|=3$ 即避开全部负4集。）
* **$m=4$（$k=3$）且余四集 $A_1..A_4$ 两两不交（§4 与第126–129行）**：
  设 $U=\bigsqcup_{i=1}^4 A_i$（$|U|\le 16$），五点候选 $\{x,u_1,u_2,u_3,u_4\}$ 在主定理中有 $\ge 3\cdot 3\cdot 4\cdot 4=144$ 份，在扩展中有 $\ge 3^4=81$ 份：
  * 唯一负3集（主定理）至多堵 $4^2=16$ 份；
  * 含 $x$ 的负4集至多 $7-3=4$ 个，每个固定3个组中的点、剩1组至多4选，共堵 $\le 4\cdot 4=16$ 份；
  * **不含 $x$ 的负4集局部容量计数**：不含 $x$ 的负4集 $B$ 只有当 $B=\{u_1,u_2,u_3,u_4\}\subseteq U$（每组各一点）时才堵1份候选。由于每个 $v\in U$ 在 $A_1..A_4$ 中已有1次正出现，其带索引负4集出现次数 $b_v\le 7-1=6$。按索引对活跃 $B\subseteq U$ 双重计数：
    $$4\cdot\#\{\text{活跃 }B\subseteq U\} = \sum_{\text{活跃 }B\subseteq U}|B\cap U| \le \sum_{v\in U}b_v \le 6|U| \le 96 \implies \#\{\text{活跃 }B\subseteq U\}\le \frac{6|U|}{4}\le 24.$$
    即使存在重复负四集索引，每个重复索引均计入其4个顶点的 $b_v\le 6$ 额度内，故 $24$ 对带索引重集同样严格有效。
  * 总堵数在主定理中 $\le 16+16+24 = 56 < 144$，在扩展中 $\le 16+24 = 40 < 81$，均无需全局负四集数量上界。

---

### 3. 核查结论
在所审阅的静态范围内，**未发现任何数学逻辑漏洞、索引重数漏洞或算术错误**；定理与扩展推论在不设全局 $|L|$ 及全局负四集数量上界的条件下完全成立（此局部通用门结论不等于完整 $m(5)\ge 36$ 证明）。

