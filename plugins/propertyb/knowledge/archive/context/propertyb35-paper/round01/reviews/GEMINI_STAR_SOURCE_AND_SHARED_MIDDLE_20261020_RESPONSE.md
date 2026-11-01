### 跨家族静态数学审阅：两项 A1 实际输入规范

**读取文件与执行说明**：已读取 [TWENTYONE_A1_BALANCED_STAR_FOREST.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md)、[GLOBAL_TWO_FLIP_SHARED_MIDDLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md) 及各自配套脚本 [GENERATE.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/GENERATE.py)、[VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/VERIFY.py)、[SATURATION.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_middle_wedge_capacity_20261020/SATURATION.py)、[CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_middle_wedge_capacity_20261020/CHECK.py)。**未运行任何程序**（纯静态数学与代码接口核验）。两份规范在各自声明的局部范围内均未发现逻辑漏洞或算术错误。

---

### 1. [TWENTYONE_A1_BALANCED_STAR_FOREST.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md)（§1–3 及 §6–7）

* **审阅结论**：**通过（非 B 的 A1 超图必满足 $n_4(H) \le 11$）**。
* **具体核验要点**：
  1. **真实 $x$ 星的 6 块 4 边多重图与重数 $\le 2$（§1）**：在 A1 角色中，$d(x)=6$，删去 $x$ 得到 $V\setminus\{x\}$（20点）上的 6 个互异四元 link $L_0,\dots,L_5$。恰有 4 名八度点 $B$ 与 $x$ 共度为 2，其余 16 点（$p$、5 名 $U$、10 名 $V_9$）与 $x$ 共度为 1。将每个 $b\in B$ 出现的两个 link 标号连一条无环边，即得 6 个标号块顶点上的 4 边多重图；每个块度 $\le 4$ 自动成立，不足 4 处由 16 个私有单位点唯一补齐。若两块间重数 $\ge 3$，则对应两条过 $x$ 原边共享 $x$ 及至少 3 个 $B$ 点，交集达 4 且含 $x$，直接由已证 `TWENTYONE_HIGH_FOUR_CORE_LOW`（含 $x/p$ 的四交核可染）排除。从 $\binom{6}{2}=15$ 对中可重复选 4 条边共 $\binom{18}{4}=3060$ 种，剔除 4 重（15种）与 3 重（$15\times 14=210$种）恰余 $2835$ 种有标签多重图，在全群 $S_6$ 块重标号下精确分为 18 个轨道（轨道大小之和为 2835）。
  2. **事件 $C$ 的普适下界 $164896$ 与回代量词（§2–3, §7）**：在 $V\setminus\{x\}$ 的均匀 $(10,10)$ 平衡二染色空间 $\Omega$（$D=\binom{20}{10}=184756$）上，事件 $C$ 定义为“至少一种颜色不出现单色 $L_i$”。若 $\chi\in C\cap\mathrm{proper}(\bar{H})$，将 $x$ 染为无单色 link 的那种颜色，则 6 条过 $x$ 边与 29 条 $\bar{H}$ 边同时双色，得到原 $H$ 的合法二染色。$\Omega\setminus C$ 为“至少一红 link 且至少一蓝 link”，[GENERATE.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/GENERATE.py#L22-L35) 的双非空容斥符号 $(-1)^{|I|-1}(-1)^{|J|-1}=(-1)^{|I|+|J|}$ 与 [VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/VERIFY.py#L36-L47) 的 De Morgan 形式 $2|\text{无红link}|-|\text{无红且无蓝link}|$ 完全等价。因为 $|C|$ 仅依赖 $(L_0,\dots,L_5)$ 的集合族同构型，对给定实际 $H$ 无需重标号原图即可在**同一 $\Omega$** 上享有普适下界 $|C|\ge 164896$（唯一最坏轨道 `01,01,02,02`）。结合上一轮已证的 §4–5（$r(\Gamma_4(\bar{H}))\ge 4\implies$ Hunter 扣除 $\ge 9306\implies |C\cap\mathrm{proper}(\bar{H})|\ge 164896-174174+9306=28>0$），非 B 必有 $r(\Gamma_4(\bar{H}))\le 3$，从而 $n_4(\bar{H})\le \binom{3+1}{2}=6$。
  3. **跨 $x$ 星四交对 $\le 5$ 的两个进口参数（§6）**：
     - 两条过 $x$ 边若有四交则核含 $x$，由进口①（`TWENTYONE_HIGH_FOUR_CORE_LOW`）排除；
     - 过 $x$ 边 $E=\{x\}\cup L_i$ 与 $\bar{H}$ 边 $F$ 四交当且仅当 $L_i\subset F$。因 $\lambda(x,p)=1$，恰有一条过 $x$ 边的 link 含 $p$，该边若有四交邻居则核 $L_p$ 含 $p$，亦由进口①排除；
     - 其余 5 条过 $x$ 边的 $L_i$ 全由 8/9 度点组成，且由强点对门知核内共度 $\le 4$。由进口②（`TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE`），非 B 时 $L_i$ 至多含于 2 条原边（含 $E$ 自身），故每条至多贡献 1 条跨星四交对。合计 $n_4(H)\le n_4(\bar{H})+5\le 6+5=11$。

---

### 2. [GLOBAL_TWO_FLIP_SHARED_MIDDLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md)（§1–5）

* **审阅结论**：**通过（非 B 的 A1 超图必满足 $522n_3+1175n_4-313\tau \ge 21538$）**。
* **具体核验要点**：
  1. **同一 middle 分组恒等式与因子 2（§1）**：固定中边 $F$ 及 $g<h\in F$，单交边集合 $\mathcal{T}(F,g)$ 与 $\mathcal{T}(F,h)$ 互斥且不含 $F$，任取 $G\in\mathcal{T}(F,g), J\in\mathcal{T}(F,h)$ 唯一对应无序外边对 $\{G,J\}$ 及中边标记 $F$，故无序路径总数 $P=\sum_{j=0}^4 C_j = \sum_F \sum_{g<h\in F} t(F,g)t(F,h)$ 无多余倍数；而二翻转期望 $\mathbb{E}Z$ 对每个无序外边对计正反两个有序方向，故 $\mathbb{E}Z = 2\sum_j C_j r_j$。同时 $\sum_F s(F)=2n_1$ 精确成立。
  2. **$f(s)$ 整数平衡上界（§2）**：5 个非负整数和为 $s=5a+r$ 时，$\sum_{g<h}t_g t_h = \frac{1}{2}(s^2-\sum t_i^2)$ 在平方和最小时取最大值 $f(s)$。$s=34=5\times 6+4$ 时 $f(34)=(1156-36-4\times 49)/2=462=\frac{66}{5}\cdot 34+\frac{66}{5}$；$s\le 33$ 时由 Cauchy 不等式 $f(s)\le \frac{2}{5}s^2\le \frac{66}{5}s$。对 35 边求和即得共享容量界 $P\le \frac{132}{5}n_1+\frac{66}{5}N_{34}$。
  3. **A1 例外边数 $N_{34}\le 9$（§3）**：因 $\sum_{j\neq 1} e_j(F)=34-s(F)$，故 $s(F)=34\iff e_0=e_2=e_3=e_4=0\iff \sum_{v\in F}(d_v-1)=34\iff \sum_{v\in F}d_v=39$。避开 $x,p$ 的边度值和 $\ge 40$。设唯一 $xp$ 边含 $v_0\in\{0,1,2,3\}$ 个 9 度点（$V$），其度和为 $37+v_0$（仅 $v_0=2$ 时达 39）；5 条仅含 $x$ 边度和为 $38+v$（需 $v=1$），由 $\lambda(x,V)=1$ 得 $S:=10-v_0\le k+4(5-k)\implies k\le\lfloor(20-S)/3\rfloor$；6 条仅含 $p$ 边度和为 $39+v$（需 $v=0$），由 $p$ 覆盖 $V$ 得 $S\le 4(6-l)\implies l\le 6-\lceil S/4\rceil$。代入 $v_0=0,1,2,3$ 得上限依次为 $3+3+0=6,\ 3+3+0=6,\ 4+4+1=9,\ 4+4+0=8$，故 $N_{34}\le 9$，$P\le (132n_1+594)/5$。
  4. **$j=3$ 满容量 $c(G,J)=16$ 的唯一四锁排除与 $C_3\le 15n_3$（§4）**：当 $|G\cap J|=3$ 时，$A=G\setminus J, B=J\setminus G$ 各含 2 点，中边必截 $A,B$ 各一点。若达上限 $16$，则 $A\cup B$ 四点全为 9 度，除 $G,J$ 外的 16 条关联边全为跨对 $\{a,b\}\in A\times B$ 的中边；结合强点对门 $\lambda_{ab}\le 4$，4 个跨对精确迹全为 4，迫使 $A\cup B$ 上的四锁精确库存唯一为 $\mu_0=17,\mu_A=\mu_B=1,\mu_{\{a,b\}}=4$。该唯一库存经固定位置 $(8,9,20,21)$ 证书给出失败界 $250309/437580<1$，故非 B 必有 $C_3\le 15n_3$。
  5. **底价 $\alpha=120$ 与最终系数（§5）**：取 $\alpha=120$，因 $r_0-120=-84<0,\ r_1-120=0$，直接消去 $C_0,C_1$ 独立上界需求，得 $R\le 120P+210C_2+672C_3+1596C_4$。代入 $C_2\le 24n_2,\ C_3\le 15n_3,\ C_4\le 4n_4$（四交外边对差集为单点对，共度 $\le 4$）及 $P$ 界，得 $R/2+3432n_1 \le 5016n_1+2520n_2+5040n_3+3192n_4+7128 = L_{15}$。代入点对覆盖恒等式 $n_1=368-2\tau+3n_3+8n_4,\ n_2=140+\tau-3n_3-6n_4$，得 $L_{15}=2205816+12528n_3+28200n_4-7512\tau$。由非 B 必要条件 $L_{15}\ge 2722720$，移项除以 24（$516904/24=21537.66\dots$）并由整性取上整，精确导出 $522n_3+1175n_4-313\tau\ge 21538$。

* **范围边界**：以上两项结论均为 A1 剩余分支上的必要结构约束与局部子类闭合，不代表整个 A1 或 $m(5)\ge 36$ 已整体证毕。

