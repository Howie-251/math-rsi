### 审阅结论：**PASS（§3.4–3.5 逻辑与算术完全严密，未发现漏洞或反例）**

- **实际审阅范围**：完整精读并逐项对抗核验 [a1_incidence_rank_subset_20261020/DERIVATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_incidence_rank_subset_20261020/DERIVATION.md#L177-L236) 的 **§3.4–3.5**（结合 §1 的实际关联 Gram 矩阵定义）。
- **是否执行程序**：**否**（纯纸面数学对抗审阅，未运行任何脚本）。
- **结论边界**：本节结论是基于 21 点 35 条互异五元边实际关联矩阵 $B=AA^T-J_{35}$ 的必要条件（当 $35<E<88$，乃至 $35<E<98$ 时，非单交图 $\Gamma$ 中度 $\le 1$ 的原边节点数 $t_0=z+l\le 19$，即度 $\ge 2$ 的节点数 $\ge 16$），并非抽象简单图性质，亦未声称已证整个 A1 或 $m(5)\ge 36$。

---

### 针对关键对抗点的逐项核验

#### 1. 低度节点成对（leaf-leaf）的逆矩阵是否影响 Core 非对角元？
- **核验结果：完全不影响（贡献恒为零）**。
- **证明**：$L_0=\{v\in V(\Gamma): d_\Gamma(v)\le 1\}$ 按在**全图 $\Gamma$** 中的度与邻接分为三类互不交集合：
  1. $z$ 个全图孤立点（$d_\Gamma(u)=0$）：对应 $D=B[L_0]$ 的一阶主块 $[4]$，且在耦合矩阵 $B[L_0,C]$ 中整行全零；
  2. $p$ 条一度—一度边（$2p$ 个节点，$0\le p\le\lfloor l/2\rfloor$）：若 $u,w\in L_0$ 互连，因它们在**全图 $\Gamma$** 中的度均为 $1$，故 $u,w$ 与 core $C=V(\Gamma)\setminus L_0$ 之间**没有任何边**。虽然 $D$ 中对应的二阶块 $\begin{pmatrix}4&\zeta\\\zeta&4\end{pmatrix}$（$\zeta\in\{-1,1,2,3\}$，$\det=16-\zeta^2\ge 7>0$）求逆后非对角，但 $B[\{u,w\},C]=0$，故该二阶块对 Schur 补修正项 $B[C,L_0]D^{-1}B[L_0,C]$ 的贡献为 $0\cdot D[\{u,w\}]^{-1}\cdot 0 = 0$；
  3. $l-2p$ 个悬挂叶节点 $u\in L_{\text{pendant}}$（$d_\Gamma(u)=1$ 且唯一邻居 $c(u)\in C$）：在 $D$ 中互不相邻，对应一阶对角块 $[4]$（逆为 $1/4$），且在 $B[L_0,C]$ 的第 $u$ 行仅有唯一的非零元 $B_{u,c(u)}=\zeta_u\in\{-1,1,2,3\}$。
- 因此，对任意 $i,j\in C$，Schur 补 $S=B[C]-B[C,L_0]D^{-1}B[L_0,C]$ 精确满足：
  $$S_{ij}=\begin{cases} B_{ij}, & i\neq j, \\ 4-\frac{1}{4}\sum_{u\in L(i)}\zeta_u^2, & i=j, \end{cases}$$
  其中 $L(i)=\{u\in L_0: u\sim i\}\subseteq L_{\text{pendant}}$。Schur 消元**只减少 $B[C]$ 的对角元，保持全部非对角元不变**。

#### 2. 秩可加性与 $E>35\implies t_0\le 20$（式 8）
- 因 $B\succeq 0$ 且 $D\succ 0$ 满秩（$\operatorname{rank}(D)=t_0=z+l$），Guttman 秩可加性给出 $S\succeq 0$ 且 $\operatorname{rank}(B)=t_0+\operatorname{rank}(S)\le 21$。
- 触及 $L_0$ 的 $\Gamma$-边数恰为 $p+(l-2p)=l-p\le l\le 35$，故 core 内部边数 $E_{\text{core}}=E-l+p$。当 $E>35$（特别地 $E\in[72,80]$）时，$E_{\text{core}}\ge E-35\ge 1$，故 $B[C]$（从而 $S$）必存在非零非对角元，迫使 $\operatorname{rank}(S)\ge 1$，即 $t_0\le 20$。

#### 3. $t_0=20$ 时 Rank-1 支持集、带符号非对角元与 $\{1,4,9\}$ 平方和排除
- **Rank-1 实分解与带符号项**：当 $t_0=20$ 且 $E>35$ 时，$|C|=15$ 且 $\operatorname{rank}(S)=1$。因 $S\succeq 0$ 为实对称半正定矩阵，必存在非零实向量 $v\in\mathbb{R}^{15}$（允许坐标带正负号以匹配 $B_{ij}=-1$）使得 $S=vv^T$，即 $S_{ij}=v_iv_j$。对不同节点 $i\neq j\in C$，$B_{ij}=S_{ij}=v_iv_j\neq 0\iff v_i\neq 0\text{ 且 }v_j\neq 0$。故非零坐标集 $A_{\text{act}}=\{i\in C:v_i\neq 0\}$（设 $|A_{\text{act}}|=a$，$2\le a\le 15$）在 $\Gamma[C]$ 中诱导完全图 $K_a$，而 $C\setminus A_{\text{act}}$ 的 $15-a$ 个节点在 $\Gamma[C]$ 中两两不相邻，从而 $E-l+p=\binom{a}{2}$。
- **非活跃点（$i\in C\setminus A_{\text{act}}$）必接至少 4 叶**：此时 $S_{ii}=v_i^2=0\implies\sum_{u\in L(i)}\zeta_u^2=16$，其中 $\zeta_u^2\in\{1,4,9\}$。若 $|L(i)|\le 3$：
  - 不含 $9$ 时，至多三项和 $\le 4+4+4=12<16$；
  - 含恰一个 $9$ 时，余下一或两项来自 $\{1,4\}$，只可能取 $9+\{0,1,4,2,5,8\}=\{9,10,13,11,14,17\}$，均不等于 $16$；
  - 含至少两个 $9$ 时，和 $\ge 18>16$。
  故 $|L(i)|\ge 4$ 严密成立。
- **活跃点（$i\in A_{\text{act}}$）至多一点无叶**：无论 $v_i,v_j$ 正负号如何，对任意不同 $i,j\in A_{\text{act}}$，均有 $|B_{ij}|=|S_{ij}|=|v_iv_j|=\sqrt{S_{ii}S_{jj}}$。因原五元边互异，交大小 $\in\{0,1,2,3,4\}$，必有 $|B_{ij}|\le 3$。若有两个活跃点满足 $S_{ii}>3, S_{jj}>3$，则 $|B_{ij}|=\sqrt{S_{ii}S_{jj}}>3$，矛盾。故 $A_{\text{act}}$ 中至多一个点满足 $S_{ii}>3$，其余 $a-1$ 个点必有 $S_{jj}\le 3\implies \frac{1}{4}\sum_{u\in L(j)}\zeta_u^2=4-S_{jj}\ge 1\implies |L(j)|\ge 1$。

#### 4. 同一叶能否重复计数及 $E\ge 88$ / $E\ge 98$ 下界
- **叶集合互不交**：每个 $u\in L_{\text{pendant}}$ 在全图 $\Gamma$ 中度为 $1$，故其唯一邻居 $c(u)\in C$ 唯一确定，即各 $\{L(i)\}_{i\in C}$ **两两不交**，同一叶绝不可能被两个 core 节点重复计数。
- **$E\ge 88$ 与 $E\ge 98$ 核算**：由于 $2p$ 个 leaf-leaf 节点不连向 $C$，实际仅有 $l-2p$ 个悬挂叶可供分配，故
  $$l\ge l-p\ge l-2p=\sum_{i\in C}|L(i)|\ge 4(15-a)+(a-1)=59-3a=:D.$$
  由 $l\le t_0=20$ 得 $59-3a\le 20\implies a\ge 13$（即 $a\in\{13,14,15\}$）：
  1. **主界 $88$**：由 $p\le\lfloor l/2\rfloor$ 知 $l-p\ge\lceil l/2\rceil$。当 $a=13$ 时 $l\ge 20\implies E=\binom{13}{2}+l-p\ge 78+10=88$；$a=14,15$ 时仅 $\binom{a}{2}$ 已达 $91,105$。
  2. **加强界 $98$**：直接用 $l-p=(l-2p)+p\ge D+p\ge D=59-3a$，得 $E=\binom{a}{2}+l-p\ge\binom{a}{2}+59-3a$，在 $a=13,14,15$ 时依次为 $78+20=98$、$91+17=108$、$105+14=119$。
  故在 $E\in[72,80]$ 下排除 $t_0=20$（断定 $t_0\le 19$）完全严密。

