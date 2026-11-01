### 全文对抗审阅报告：21点、35条五元边、点对覆盖、最小度 $\delta(H)\ge 8$ 分支完整闭合候选

- **审阅对象**：[TWENTYONE_MINIMUM_EIGHT.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_MINIMUM_EIGHT.md)（178行，冻结主稿）及其输入清单 [INPUTS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/audit-twentyone-minimum-eight-20261020/INPUTS.md)（U01–U13）
- **目标定理**：设 $H=(V,E)$ 是 $21$ 个顶点、$35$ 条互异五元边的简单超图，覆盖所有 $\binom{21}{2}=210$ 个顶点对，且最小点度 $\delta(H)\ge 8$（**无任何额外共度假设**），则 $H$ 具有 Property B。
- **执行环境声明**：**纯静态数学核对与源码/证书逐行审阅（未执行任何程序或 Shell 命令，CPU 执行 0 秒）**；未运行 Lean，未读取 `v2` 或其他模型审阅记录。
- **审阅结论**：**通过（`SOUND_MODULO_DECLARED_IMPORTS`）**。在显式声明的底层通用引理进口下，主稿及全部下游模块逻辑严密、无循环论证、无量词漂移、无域遗漏，完整闭合了 $21$ 点 $\delta(H)\ge 8$ 整支（不扩大到 $\delta(H)=7$ 或完整 $m(5)\ge 36$）。

---

### 一、 实际阅读范围（全文核对 vs 接口核对）

#### 1. 全文精读与静态核对文件（U01–U13 全覆盖）
- **清单与主稿**：
  - [INPUTS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/audit-twentyone-minimum-eight-20261020/INPUTS.md)（全文 1–50 行）
  - **U01**：[TWENTYONE_MINIMUM_EIGHT.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_MINIMUM_EIGHT.md)（全文 1–178 行，§1–§8）
  - **U02**：[TWENTYONE_MINIMUM_EIGHT_SMALL_CODEGREES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_MINIMUM_EIGHT_SMALL_CODEGREES.md)（全文 1–150 行，§1–§8）
- **前置已审并在本轮复核实际调用接口的模块**：
  - **U03**：[CLEAN_EXTERIOR_STAR_FROM_TRACE_BUDGET.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/CLEAN_EXTERIOR_STAR_FROM_TRACE_BUDGET.md)（前轮全文审阅通过，本轮复核 $c=8$ 调用）
  - **U04 & U10**：[min_degree_eight_singleton_star_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_eight_singleton_star_20261020/PROOF.md)、[SCOPE_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_eight_singleton_star_20261020/SCOPE_CHECK.py)、[CONDITIONAL_SCALAR_REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_REPORT.md)、[CONDITIONAL_SCALAR_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_CHECK.py)（全文核对）
  - **U08**：[ONE_EXCEPTIONAL_POINTPAIR_CAPACITIES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/ONE_EXCEPTIONAL_POINTPAIR_CAPACITIES.md)（前轮全文审阅通过，本轮复核四谱调用）
  - **U12**：[CAPACITY_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/CAPACITY_LEMMAS.md) 及 [generic_c3_fourteen_gate_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md)（第一轮全文审阅通过，本轮核对局部调用前提）
- **本轮新增完整精读模块（U05, U06, U07, U09, U11, U13）**：
  - **U05**：[delta8_strong_pair_transfer_20261020/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_strong_pair_transfer_20261020/REPORT.md)（全文 1–168 行）及 [VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_strong_pair_transfer_20261020/VERIFY.py)（全文 1–55 行）
  - **U06**：[delta8_c3_capacity_transfer_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_c3_capacity_transfer_20261020/PROOF.md)（全文 1–79 行）及 [INDEPENDENT_VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_c3_capacity_transfer_20261020/INDEPENDENT_VERIFY.py)（全文 1–66 行）
  - **U07**：[delta8_high_center_q4_20261020/audit/AUDIT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_high_center_q4_20261020/audit/AUDIT.md)（全文 1–76 行）、[CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_high_center_q4_20261020/CHECK.py)（全文 1–56 行）及 [audit/VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_high_center_q4_20261020/audit/VERIFY.py)（全文 1–149 行）
  - **U09**：[c3_unique_high_pair_five_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/PROOF.md)（全文 1–189 行）、[PILOT.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/PILOT.py)（全文 1–66 行）、[VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/VERIFY.py)（全文 1–50 行）及 [VERIFY_RESULT.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/VERIFY_RESULT.json)（1–800 行抽样逐行手算核对）
  - **U11**：[delta8_one_exception_scalar_20261020/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_one_exception_scalar_20261020/REPORT.md)（全文 1–70 行）、[CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_one_exception_scalar_20261020/CHECK.py)（全文 1–99 行）、[audit/CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_one_exception_scalar_20261020/audit/CHECK.py)（全文 1–111 行）及 [audit/CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_one_exception_scalar_20261020/audit/CHECK.json)（全文 1–248 行）

#### 2. 接口核对（Declared Imports，不重复宣称底层重审）
- 底层通用排列概率引理与单边/双边翻转密度不等式：[PROBABILITY_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md)（条件排列引理 $\mathcal{U}=\sum_{k=1}^{21}\min(A_k,B_k,C_k)<1$、单标签一红/树阈值公式、以及 $\delta(\Gamma)\ge 4$ 下单翻转给出 $n_1\ge 397$、双翻转给出 $2L=6864n_1+\sum_{j=0}^4 w_j C_j\ge 5445440$）。
- 通用注入下降阶乘实现：`computations/independent_structure_bounds.py` 中的 `independent_rows` 与 `context/propertyb34/round01/high-math/subset_position_dp.py` 中的 `SubsetEngine`（已在第一轮全文审阅）。

---

### 二、 核心攻击点逐项独立核查

#### 1. 完整 15 个度谱枚举与强共度对唯一性二分（U01 §1–2, U02 §1, U05）
- **15 个全局度谱的完备性**：
  设 $b$ 为 $8$ 度点数，$e=\sum_{v\in V}\max(d(v)-9,0)$ 为高于 $9$ 度的总盈余。由总度数 $\sum_{v\in V}d(v)=35\times 5=175$ 得：
  $$175 = 8b + 9(21-b) + e = 189 - b + e \implies b = 14 + e, \qquad g := |\{v:d(v)\ge 9\}| = 21 - b = 7 - e.$$
  若 $e\ge 7$，则 $b\ge 21$，即全部 $21$ 个点均为 $8$ 度，从而 $e=0$，矛盾。故 $0\le e\le 6$，且 $e$ 的正整数分拆项数（即度数 $\ge 10$ 的点数）至多为 $7-e$。逐一枚举 $e=0,\dots,6$ 下长度 $\le 7-e$ 的正整数分拆，个数依次为 $1+1+2+3+4+3+1=15$（其中 $e=4$ 时仅剔除长度 $4>3$ 的 `(1,1,1,1)`；$e=5$ 保留长度 $\le 2$ 的 `(5),(4,1),(3,2)`；$e=6$ 保留长度 $1$ 的 `(6)` 即 `8^20,15`）。15 个度谱完整无遗漏。
- **100 个强共度元组与四谱唯一高点对二分**：
  在 15 个度谱中，实际可同时出现的有序度对 $(d_u,d_v)$（$d_u\le d_v$，若 $d_u=d_v$ 要求重数 $\ge 2$）共 20 种，搭配 $5\le c\le \min(d_u,d_v)$ 共产生 **100 个元组 $(d_u,d_v,c)$**（见 [delta8_strong_pair_transfer_20261020/VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_strong_pair_transfer_20261020/VERIFY.py#L11-L21)）。
  对固定双锁布局 `(10,21)` 与 `(21,10)`（零配额），100 个元组中有 **96 个严格 $\mathcal{U}<1$**（最大值 $9935/10296<1$），涵盖了**所有 $c\ge 6$ 的情形**以及**所有 $\min(d_u,d_v)\le 9$ 的点对**。唯一未通过双锁的 4 个元组全部满足 $c=5$：
  1. `(10,12,5)` $\longrightarrow$ 仅出现在 Source 8（`8^18,9,10,12`，$W=18\binom{8}{2}+\binom{9}{2}+\binom{10}{2}+\binom{12}{2}=504+36+45+66=651$）；
  2. `(11,11,5)` $\longrightarrow$ 仅出现在 Source 9（`8^18,9,11,11`，$W=504+36+2\binom{11}{2}=650$）；
  3. `(10,13,5)` $\longrightarrow$ 仅出现在 Source 11（`8^19,10,13`，$W=19\binom{8}{2}+45+78=532+123=655$）；
  4. `(11,12,5)` $\longrightarrow$ 仅出现在 Source 12（`8^19,11,12`，$W=532+55+66=653$）。
  （注：主稿 [TWENTYONE_MINIMUM_EIGHT.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_MINIMUM_EIGHT.md#L123-L128) 中四谱的 $W=651,650,655,653$ 与手算及代码完全一致。）
  更重要的是，在这四个度谱中，度数 $\ge 10$ 的顶点**恰好只有两个**（即 $\{u,v\}$ 在原图 $H$ 中是**唯一**具有该度数的点对），其余 209 个点对均满足 $\min(d_a,d_b)\le 9$，因而其 $c\ge 5$ 已全部被 96 个严格双锁证书排除，且 $\{u,v\}$ 本身的 $c\ge 6$ 也已被排除。因此，**完全不需要使用 [REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_strong_pair_transfer_20261020/REPORT.md#L121-L148) §4 中含 24 个未过尾项的三锁附加探索**，任何非 B 的原超图 $H$ 必然严格落入以下二分支之一：
  - **分支一（全小共度）**：所有 210 个点对满足 $\lambda(a,b)\le 4$；
  - **分支二（四谱唯一高点对 $\lambda=5$）**：度谱属于 Sources 8, 9, 11, 12 之一，唯一高点对 $\{u,v\}$ 满足 $\lambda(u,v)=5$，其余 209 个点对满足 $\lambda(a,b)\le 4$。

---

#### 2. 无 $e$ 限制的 $\delta(\Gamma)\ge 4$ 与分支一（全 $\lambda\le 4$）闭合（U02, U03, U04, U06, U07, U10）
- **$\delta(\Gamma)\ge 4$ 不依赖全局 $e\le 4$ 或 $\lambda\le 4$**：
  如前轮已核，[min_degree_eight_singleton_star_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_eight_singleton_star_20261020/PROOF.md) 仅利用 $F$ 内 5 个点满足 $d(v)\ge 8$（从而 $S_1\ge 40-S_2-S_3-S_4$）将 $q_\Gamma(F)\le 3$ 的 119 个高迹轨道压至 25 个 `C_A2=0` 轨道；其中 23 个由 5 锁直接闭合，最后 2 个尾项 `(4,7,13)` 与 `(4,7,14)` 满足 $S_1\ge 22 > 7\times 3=21$，由 [CLEAN_EXTERIOR_STAR_FROM_TRACE_BUDGET.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/CLEAN_EXTERIOR_STAR_FROM_TRACE_BUDGET.md) 从所有 15 个度谱皆有的至少 $14$ 个 $8$ 度点中选出与 3 条例外外边不交的干净外点 $z$（$d(z)=8$），其 70 个 6 锁库存全部严格 $<1$（最大 $6569/6860<1$）。因此 **$\delta(\Gamma)\ge 4$ 对全 15 谱无条件成立**。
- **分支一的 $C_3\le 13n_3$（U06）**：
  在全 $\lambda\le 4$ 下，15 个全局度谱中任取 4 点子集 $K=(G\setminus J)\cup(J\setminus G)$ 共产生 **38 种四点度多重集**（见 [delta8_c3_capacity_transfer_20261020/INDEPENDENT_VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_c3_capacity_transfer_20261020/INDEPENDENT_VERIFY.py#L15-L26)）。其中 33 种满足局部条件 $\max_{w\in K}d(w)\le 13$ 且 $\sum_{w\in K}(d(w)-9)_+\le 4$，直接由第一轮已审的局部定理 [generic_c3_fourteen_gate_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md) 排除 $c(G,J)\ge 14$；新增的 5 种四点度多重集 `(8,8,8,14)`, `(8,8,8,15)`, `(8,8,9,14)`, `(8,8,10,13)`, `(8,8,11,12)` 产生 412 个带标号库存 / 62 个保侧群轨道，在旧三固定布局 `(8,9,20,21)`, `(9,10,20,21)`, `(9,20,10,21)`（零配额）下全部严格（最大 $\mathcal{U}=1427/1716<1$）。
- **分支一的标量矩扫描与 Source 13/14 握手矛盾（U07, U10）**：
  在 $\delta(\Gamma)\ge 4$、全 $\lambda\le 4$、$C_3\le 13n_3$ 下，[CONDITIONAL_SCALAR_REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_REPORT.md) 扫描全部 15 谱的 $1,166,584$ 个必要矩键：13 个度谱全严格 $2L<5445440$，仅剩：
  - Source 13（`8^19,9,14`）：唯一幸存键 $E=70$；
  - Source 14（`8^20,15`）：14 个幸存键，均满足 $E\in [70,73]$。
  而 [delta8_high_center_q4_20261020/audit/AUDIT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_high_center_q4_20261020/audit/AUDIT.md) 与 [audit/VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_high_center_q4_20261020/audit/VERIFY.py) 证明：若边 $F$ 的点度多重集为 `(14,8,8,8,8)`, `(14,9,8,8,8)` 或 `(15,8,8,8,8)` 且 $F$ 内 10 个点对共度 $\le 4$，则 $q_\Gamma(F)=4$ 蕴含 $H$ 可二染色（$23751\times 3$ 个带标号四迹经独立重算的 70 组一红/树阈值筛后分别剩 $0,6,6$ 个尾项，全部 12 个尾项在固定五锁 `(4,3,12,2,1)` 零配额下满足 $\mathcal{U}=11203/12012<1$）。
  - 在 Source 13 中，过 $14$ 度点的全部 14 条原边度型必为 `(14,8,8,8,8)` 或 `(14,9,8,8,8)`，故这 14 条边均满足 $q_\Gamma(F)\ge 5$，其余 21 条边满足 $q_\Gamma(F)\ge 4$，握手得 $2E=\sum_{F}q_\Gamma(F)\ge 14\times 5+21\times 4=154\implies E\ge 77>70$，与唯一幸存键 $E=70$ 矛盾！
  - 在 Source 14 中，过 $15$ 度点的全部 15 条原边度型必为 `(15,8,8,8,8)`，故 $2E\ge 15\times 5+20\times 4=155\implies E\ge 78>73$，与所有幸存键 $E\le 73$ 矛盾！
  分支一完整闭合。

---

#### 3. 分支二的新单例外 $C_3\le 13n_3$ 门：选定 $K$ 无遗漏、$t\ge c$ 方向与 425 库存（U09）
在分支二中，$H$ 属于四谱 Sources 8, 9, 11, 12 之一，唯一高点对 $\{u,v\}$ 满足 $\lambda(u,v)=5$，其余所有点对满足 $\lambda\le 4$。任取三交原边对 $G,J$（$|G\cap J|=3$），令 $A=G\setminus J, B=J\setminus G, K=A\cup B$（$|A|=|B|=2$）：

1. **当 $\{u,v\}\not\subseteq K$ 时的局部调用合法性（无误用全局定理）**：
   - 因为 $\{u,v\}$ 是全图唯一的 $\lambda=5$ 点对，当 $\{u,v\}\not\subseteq K$ 时，$K$ 内部全部 $\binom{4}{2}=6$ 个点对均满足 $\lambda\le 4$。
   - 同时，在 Sources 8 (`8^18,9,10,12`), 9 (`8^18,9,11,11`), 11 (`8^19,10,13`), 12 (`8^19,11,12`) 中，全图仅有 $u,v$ 两个点的度数 $>9$，且 $\max(d(u),d(v))\le 13$。既然 $\{u,v\}\not\subseteq K$，$K$ 至多包含 $u,v$ 中的一个点，因此 $K$ 必然满足**局部条件**：
     $$\max_{w\in K} d(w) \le 13, \qquad \sum_{w\in K}\max(d(w)-9,0) \le 13-9 = 4.$$
   - 旧 [generic_c3_fourteen_gate_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md) 本身就是关于选定四点集 $K$ 的**局部定理**（仅依赖 $K$ 内六点对 $\lambda\le 4$ 及 $K$ 的四点度多重集属于 $\max\le 13, \sum(d-9)_+\le 4$ 的 37 类之一，不依赖 $K$ 外点度或全局 $e\le 4$）。因此当 $\{u,v\}\not\subseteq K$ 时直接调用该局部门是完全合法的，没有任何越界。

2. **当 $\{u,v\}\subseteq K$ 时的 6 种四点度组合与 14 个标记族**：
   - 在四谱中去掉 $\{u,v\}$ 后，剩余 19 个点在 Sources 8, 9 中为 `8^18,9`（从中任取两点度数为 `(9,8)` 或 `(8,8)`），在 Sources 11, 12 中为 `8^19`（任取两点度数为 `(8,8)`）。故 $(d(u),d(v);d(w),d(z))$ 精确只有 [c3_unique_high_pair_five_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/PROOF.md#L15-L18) 式 (1) 列出的 6 种组合：
     `{(10,12;9,8), (10,12;8,8), (11,11;9,8), (11,11;8,8), (10,13;8,8), (11,12;8,8)}`。
   - 按 $\{u,v\}$ 在同侧（`same`，置于 `bits 0,1`，另一侧两点按度数排序，共 6 族）或跨侧（`cross`，置于 `bits 0,2`，另一对点在 `(9,8)` 时保留 `(9,8)` 和 `(8,9)` 两种侧向安排，共 $2+1+2+1+1+1=8$ 族），共 **14 个标记族**，完整覆盖所有情况。

3. **$t\ge c(G,J)$ 方向、同侧为空与全四/三迹紧预算**：
   - 任何满足 $F\cap G=\{g\}, F\cap J=\{j\}$ ($g\neq j$) 的有效中间边 $F$ 必满足 $F\cap (G\cap J)=\emptyset$ 且 $|F\cap A|=|F\cap B|=1$，故 $F\cap K\in\mathcal{C}=\{5,6,9,10\}$。反之，迹在 $\mathcal{C}$ 中的边仍可能交 $G\cap J$，证明只单向使用必要条件 $t=\sum_{p\in\mathcal{C}}\mu_p\ge c(G,J)\ge 14$。
   - 由精确恒等式 $\sum_{p\in\mathcal{C}} I_p = t + 2P + 4q$（其中 $P=\sum_{|T|=3}\mu_T, q=\mu_{15}$）：同侧时 $\sum_{p\in\mathcal{C}}I_p\le 16$，跨侧时一个 cross 对为 $5$、其余三个 $\le 4$，故 $\sum_{p\in\mathcal{C}}I_p\le 17$。结合 $t\ge 14$ 得 $2P+4q\le 3\implies q=0, P\le 1$。
   - 同侧时 $d(u)+d(v)\ge 2\lambda(u,v)+t\ge 10+14=24 > 23\ge d(u)+d(v)$，故 6 个同侧族解析为空（代码仍完整枚举验证为 0）；跨侧且 $t=17$ 时四个 cross 对精确重数为 $(5,4,4,4)$，加上 $\mu_3\ge 1,\mu_{12}\ge 1$ 迫使 $w,z$ 两点度数均 $\ge 4+4+1=9$，与至少一点为 $8$ 度矛盾，故 $t=17$ 在单点度恢复 $\mu_{\{i\}}\ge 0$ 时自然排尽。
   - 两种独立生成法（[PILOT.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/PILOT.py) 高迹→exactpair 与 [VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/VERIFY.py) inclusive→Möbius 反演）逐键一致给出 **425 个完整库存**，在三固定布局 `(8,9,20,21)`, `(9,10,20,21)`, `(9,20,10,21)`（零配额）下经 35 原边索引独立重放全部严格 $\mathcal{U}<1$（最大值 $25963/29172<1$）。我已对 [VERIFY_RESULT.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/VERIFY_RESULT.json#L26-L404) 首项（度 `(10,8,12,9)`，位置 `(8,9,20,21)`）抽样手算核对：$k=5$ 时 $A_5=12/\binom{17}{5}=3/1547$，$k=6$ 时 $A_6=12\binom{5}{4}/\binom{17}{5}=15/1547$，$k=20$（锁点 bit 2）时 $A_{20}=\mu_4+\mu_5+\mu_6+\mu_7=2+5+4+0=11$，分母与分子完全准确。

---

#### 4. 分支二的单例外标量闭合：$\tau\le 142$、$C_4$ 修正、共享 $P$ 与 $2L$ 阈值（U08, U11）
- **单例外容量上界（U08）**：
  - 由点对覆盖，$\sum_{p}(\lambda(p)-1)=35\binom{5}{2}-\binom{21}{2}=140$。对 $\lambda\in\{1,2,3,4\}$ 有 $\binom{\lambda-1}{2}\le \lambda-1$，仅唯一高点对 $\lambda(u,v)=5$ 有 $\binom{4}{2}=6=(5-1)+2$，故 $\tau=\sum_p\binom{\lambda(p)-1}{2}\le 142$。
  - 逐点行下界：因 $\binom{\lambda-1}{2}\ge \lambda-2$ 对 $\lambda=1,\dots,5$ 皆成立，故 $\tau\ge \tau_v\ge 4\Delta-40$ 保持不变（不除 2）。
  - $C_4$ 上界：四交无序外边对 $\{G,J\}$ 仅当其对称差 $G\triangle J=\{u,v\}$ 时才有 $c(G,J)\le \lambda(u,v)=5$（其余 $\le 4$）。每个此类无序对 $\{G,J\}$ 恰有一边含 $u$ 避 $v$、另一边含 $v$ 避 $u$，且由 $J=(G\setminus\{u\})\cup\{v\}$ 唯一互定，故无序对个数至多为 $\min(d(u)-5,d(v)-5)=\min(d(u),d(v))-5$（无方向因子 2）。在 Sources 8, 11 中加 $5$，在 Sources 9, 12 中加 $6$。
- **315,870 个双参数矩键全严格（U11）**：
  结合已闭合的 $\delta(\Gamma)\ge 4$ 与单例外 $C_3\le 13n_3$，[delta8_one_exception_scalar_20261020/CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_one_exception_scalar_20261020/CHECK.py)（按 $(n_1,t,m)$ 奇偶生成）与 [audit/CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/delta8_one_exception_scalar_20261020/audit/CHECK.py)（按 $(\tau,t,m)$ 独立生成）对四谱全部 **315,870** 个可行矩键逐键核对相等，全部满足 $2L < 5445440$（即 $L < 2722720$）。
  我对最紧见证（Source 12：`8^19,11,12`，$W=653$，$(n_0,n_1,n_2,n_3,n_4)=(31,525,0,28,11),\tau=10$）作了独立手算复核：
  - $P\le B(525)=35 f(30)=12600$；
  - 容量上界 $(C_0,C_1,C_2,C_3,C_4)\le (1023, 14175, 0, 364, 50)$（其中 $525\le 19\binom{8}{2}=532$，故 $K_d(525)=525\times 8=4200, 35\times 525-4200=14175$）；
  - 按权重 $(1716,792,330,120,36)$ 贪心分配 $P=12600$ 得 $(\hat{C}_0,\dots,\hat{C}_4)=(0,12186,0,364,50)$；
  - $2L = 6864\times 525 + 120\times 12186 + 792\times 364 + 1716\times 50 = 3603600 + 1462320 + 288288 + 85800 = 5440008 < 5445440$，严格余量 $2(2722720-L)=5432\implies 2722720-L=2716>0$。

---

#### 5. 同一原超图 $H$ 的量词一致性
全篇证明固定**同一个反证假设下的原超图 $H$**（不具有 Property B）：
- 由 $H$ 不可二染色，局部固定位置证书推出 $H$ 满足强共度二分（全 $\lambda\le 4$ 或四谱唯一高对 $\lambda(u,v)=5$）、$\delta(\Gamma(H))\ge 4$、以及每个三交对 $c(G,J)\le 13\implies C_3(H)\le 13n_3(H)$；
- 同时，单翻转与双翻转全局概率不等式表明，若 $H$ 不可二染色，则 $H$ 的真实矩向量必须满足 $n_1\ge 397$ 且 $2L(H)\ge 5445440$；
- 在 13 个小共度谱与 4 个单例外谱中，所有必要矩键均满足 $2L<5445440$，直接矛盾；在剩下的 Sources 13, 14（全 $\lambda\le 4$）中，幸存矩键要求 $E(\Gamma(H))\le 73$，而局部 $q_4$ 门迫使高点星中每条边 $q_\Gamma(F)\ge 5$、其余边 $q_\Gamma(F)\ge 4$，握手得 $E(\Gamma(H))\ge 77$，在同一 $\Gamma(H)$ 中直接矛盾。
不存在将标量幸存键当作真实超图、或在不同子引理间偷换原图 $H$ 的量词谬误。

---

### 三、 最终判定

- **具体数学错误或反例**：**无（0 项）**。
- **判定状态**：**`SOUND_MODULO_DECLARED_IMPORTS`**。
- **准确覆盖范围**：仅认可 **21 点、35 条互异五元边、点对覆盖、最小点度 $\delta(H)\ge 8$ 的超图具有 Property B**（[TWENTYONE_MINIMUM_EIGHT.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_MINIMUM_EIGHT.md)）；不扩大到 21 点 $\delta(H)=7$ 分支或完整 $m(5)\ge 36$。
