### 有限范围对抗数学审阅报告

**审阅范围与执行声明：**
* **已完整核读文件（只读未修改）：**
  1. [FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md)
  2. [THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md)
  3. [TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_THREE_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_THREE_TRIPLES.md)
  4. 辅助核查文件：[CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_negative_pairs/CHECK.py)、[CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_negative_pairs/CHECK.json)、[CHECK_R4.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_negative_pairs/CHECK_R4.py)、[CHECK_R4.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_negative_pairs/CHECK_R4.json)（前800行）及 [AUDIT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_negative_pairs/AUDIT.md)。
* **执行情况：** 纯静态数学审阅，**未执行任何程序、脚本或 Lean 构建**。
* **审阅结论：** **未发现数学漏洞（PASS）**。三份文稿的解析推导、边界尾型换色救援、负索引重数与原次数预算、同 $H$ 联合量词消去及原 35 边染色回收均严密闭合。

---

### 1. 四正三负二主门核查（[FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md)）

* **不任意 padding 与截取单调性（开篇及第 1–2 节）：**
  * 将每个大小 $\ge 4$ 的正集截取为 4 元子集只会减少正出现次数，保持每点总出现次数 $\le 7$，且后期对 $x \in A \cap B$ 或 $f \in U \cap V$ 使用的“至少 2 次正出现”在截后成立即在原正族中成立。
  * 正集数 $\le 2$ 时，直接从至多 3 个负二索引各选一点组成禁集 $F$（$|F| \le 3$），正四集删 $F$ 后仍非空，取 $\le 2$ 红点即避开全部负集，未用复制正集的非法 padding。
  * 三正不交（64 候选中至多堵 $24 + \frac{10}{3}q \le 34 < 64$）与四正不交（256 候选中由单一共同负容量 $2q+3t+4b \le 96$ 得至多堵 $128 + \frac{40}{3}q \le 168 < 256$）均按活跃索引一次性联合计费，无跨尺寸重复返还点容量。
* **四正交叠初态与重复负二索引（第 3 节）：**
  * 若无点命中 $\ge 3$ 个正集，取恰命中 $A,B$ 的 $x$，余两正四集 $U,V$ 避 $x$。$q_x \in \{0,1,2,3\}$ 严格定义为含 $x$ 的**负二索引数**，而 $F = \{f : \{x,f\} \text{ 为负二约束}\}$ 为不同禁邻点集，满足 $|F| \le q_x$。
  * 先令 $x$ 红、$F$ 蓝。若 $U' = U \setminus F$ 与 $V' = V \setminus F$ 相交，取交点与 $x$ 得二元红集，因避 $F$ 且大小为 2，不触发任何负集；若 $U' \cap V' = \varnothing$，因 $x \notin U' \cup V'$，$C = |U'||V'|$ 个三元候选 $\{x,u,v\}$ 两两互异。
  * 堵数上界：避 $x$ 的负二索引至多 $3 - q_x$ 个（各至多堵 1 份），含 $x$ 的负三索引由 $x$ 的总次数 $\le 7$（已占 $A,B$ 两次正出现和 $q_x$ 次负二索引出现）至多 $5 - q_x$ 个（各至多堵 1 份），合计至多 $8 - 2q_x$。$q_x=0$（$16>8$）与 $q_x=1$（$C \ge 9 > 6$）均严格通过。
* **攻击点 A：$q_x=2$ 的等号换色救援（第 4 节）：**
  * 此时堵数上界为 $8 - 2(2) = 4$，且 $|F| \le 2 \implies |U'| \ge 2, |V'| \ge 2 \implies C \ge 4$。
  * 若全堵，必有 $C = 4$，从而 $|U'|=|V'|=2$ 且 $|F|=2$，迫使 $F = \{f_1,f_2\} \subseteq U \cap V$（此情形下两个含 $x$ 的负二索引必为互异的 $\{x,f_1\},\{x,f_2\}$；若负二索引重复则 $|F| \le 1 \implies C \ge 9 > 4$，不入等号）。
  * 同时，含 $x$ 的负三至多 $5 - q_x = 3$ 个，不足以堵满 4 个候选，故第 3 个（避 $x$ 的）负二索引 $H$ 必存在且堵某候选 $\{x,u_0,v_0\}$（$u_0 \in U', v_0 \in V'$），从而 $H \subseteq U' \cup V'$，故 $H \cap F = \varnothing$。
  * **换色救援与原次数扣减：** 改令 $x$ 蓝、任取 $f \in F$ 红。$f$ 已击中 $U,V$；含 $x$ 的两个负二因 $x$ 蓝而安全，唯一剩余负二 $H$ 因 $H \cap F = \varnothing$ 而避开 $f$。对剩余两个三集 $A'=A\setminus\{x\}, B'=B\setminus\{x\}$：若 $f \in A'\cup B'$ 或 $A'\cap B'\ne\varnothing$，至多再取一点得 $\le 2$ 红（含 $f$ 避 $x$，故不可能是含 $x$ 负二或避 $f$ 的 $H$）；若 $A',B'$ 不交且均避 $f$，产生 $3 \times 3 = 9$ 个三红候选 $\{f,a,b\}$。其中 $H$ 至多堵 1 份；点 $f$ 在 $U,V$ 中有 2 次原正出现，且**原负二 $\{x,f\}$ 虽已因 $x$ 蓝而满足，仍在原系统中占用 $f$ 的至少 1 次负出现**，故含 $f$ 的负三索引至多 $7 - 2 - 1 = 4$ 个，总堵数至多 $1 + 4 = 5 < 9$。
* **攻击点 B：$q_x=3$ 的小候选换色救援（第 5 节）：**
  * 此时堵数上界为 $8 - 2(3) = 2$。若 $C \le 2$，由 $|U'|, |V'| \ge 1$ 知 $|U'| + |V'| \le 3$，即 $|U \cap F| + |V \cap F| \ge 5$。
  * 由 $|(U \cup V) \cap F| \le |F| \le 3$（无需假定三个含 $x$ 负二邻点互异；事实上若 $|F| \le 2$ 则 $|U \cap F| + |V \cap F| \le 4$，根本不会进入 $C \le 2$），容斥直接给出 $|U \cap V \cap F| \ge 5 - 3 = 2$。
  * 改令 $x$ 蓝、取 $f \in U \cap V \cap F$ 红。因 $q_x=3$，系统全部负二均含 $x$，故 $x$ 蓝使**所有负二全部安全**。同第 4 节，$A',B'$ 或以 $\le 2$ 红解决，或给出 9 个含 $f$ 三红候选；$f$ 已占 $U,V$ 两次正出现与 $\{x,f\}$ 至少一次原负二出现，含 $f$ 负三至多 4 个，$4 < 9$ 严格获救。

---

### 2. 无次数三正四负二短门核查（[THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md)）

* **正集数 $\le 2$（第 11–14 行）：** 0 或 1 个正集平凡；2 个正集有交点取 1 点，不交则取 $4 \times 4 = 16$ 个红对，至多 4 个负二各至多堵 1 对（$4 < 16$），避开了“先禁 4 个负二点导致正四集可能为空”的陷阱。
* **三正有交叠 $z \in A \cap B$（第 17–39 行）：**
  * 若 $z \in C$ 取单点 $\{z\}$；若 $z \notin C$，考察 $\{z,w\}$（$w \in C$）。二元候选仅能被负二阻塞。
  * 若全堵，因 $|C| \ge 4$ 且负二索引数 $\le 4$，必有 $|C| = 4$，且 4 个负二索引恰为互异的四边星 $\{z,w\}$（$w \in C$）。
  * 改令 $z$ 不入红集，则**全部 4 个负二因含 $z$ 而同时安全**。剩余正集 $A\setminus\{z\}, B\setminus\{z\}, C$ 大小分别至少 $3,3,4$：若任两者相交，取交点及至多另一点得 $\le 2$ 红（无可用负二、负三及以上大小 $\ge 3$，必安全）；若三者两两不交，产生至少 $3 \times 3 \times 4 = 36$ 个互异三红候选，仅受至多 35 个负三阻塞（$35 < 36$），负四及以上不阻塞三红。
* **三正两两不交（第 40–49 行）：** 截取为三个 4 集得 $4^3 = 64$ 个三红候选。每个负二跨两组时第三组有 4 种选法（至多堵 4 份），每个负三至多堵 1 份，总堵数至多 $4 \times 4 + 35 = 51 < 64$。

---

### 3. P7 I1 无四迹、$r \le 4$ 统一调用核查（[TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_THREE_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_THREE_TRIPLES.md)）

* **进口前提与原始迹预算（第 1 节）：**
  * $|V|=24 = 7_P + 17_L$，$P$ 度 8、$L$ 度 7，35 条五元边，无全七度边（故 $n_0 = 0$），唯一内部边 $C \subseteq P$（$|C|=5$），无四迹（$n_4=0$），三迹数 $n_3 = r$。
  * 由 $n_1 + n_2 + r = 34$ 与 $n_1 + 2n_2 + 3r = 56 - 5 = 51$ 准确解得 $n_2 = 17 - 2r$，$n_1 = 17 + r$，且 $\sum_{v \in P} h_v = 3r$，$\sum_{v \in P} s_v = 2n_2 = 34 - 4r$。
  * 对每点 $v \in P$，单迹数 $u_v = 8 - \mathbf{1}_{\{v \in C\}} - h_v - s_v \ge 0$。
* **完整原 35 边风险与外点度约束（第 2 节）：**
  * 固定 $q \in C$ 染蓝、$P \setminus \{q\}$（6 点）全染红。
  * 35 条原边无遗漏分类：① 内部边 $C$（1 条）含蓝 $q$ 与红 $C\setminus\{q\}$，已双色；② 含 $q$ 的二／三迹（$s_q + h_q$ 条）在 $P$ 上含蓝 $q$ 与至少一红点，已双色；③ $q$ 的单迹（$m = 7 - h_q - s_q$ 条）在 $P$ 上全蓝，给出 $m$ 个正四集；④ 不含 $q$ 的三迹（$r - h_q$ 条）、二迹（$n_2 - s_q$ 条）、单迹（$n_1 - m$ 条）在 $P$ 上全红，依次给出完整负二、负三、负四集；因 $n_4=0, n_0=0$，**无负单集或零迹遗漏**。
  * 每条未满足原边仅产生一个带原索引的正或负约束，故任一外点 $y \in L$ 的总正负出现次数 $\le d_H(y) = 7$。当 $R \subseteq L$ 染红、$L \setminus R$ 染蓝时，原 35 条边全部双色。
* **$r \le 3$ 的同 $H$ 联合量词消去（第 2–3 节）：**
  * 若存在 $q \in C$ 使 $h_q + s_q \ge 3$，则正四数 $m \le 4$、负二数 $r - h_q \le 3$，直接由四正三负二门得染。
  * 否则对**同一个 $H$**，所有 $q \in C$ **同时**满足 $h_q + s_q \le 2$。对 $C$ 求和得 $\sum_{q \in C} s_q \le 10 - H_C$，对 $D = P \setminus C$ 两点由 $u_d \ge 0$ 求和得 $\sum_{d \in D} s_d \le 16 - (3r - H_C)$。同一 $H$ 的 $H_C$ 相加消去，得 $\sum_{v \in P} s_v \le 26 - 3r < 34 - 4r$（$0 \le r \le 3$），矛盾。
* **$r = 4$ 的分流与频率矛盾（第 4 节）：**
  * $r=4 \implies n_2 = 9, n_1 = 21, \sum_{v \in P} h_v = 12, \sum_{v \in P} s_v = 18$。
  * 若存在 $q \in C$ 满足 $h_q \ge 3$、或 $(h_q=2, s_q \ge 1)$、或 $(h_q=1, s_q \ge 2)$，均有 $m = 7 - h_q - s_q \le 4$ 且负二数 $4 - h_q \le 3$，由四正三负二门闭合；若存在 $q \in C$ 满足 $(h_q=0, s_q \ge 4)$，则正四数 $m \le 3$、负二数 $4$、负三数 $9 - s_q \le 5 \le 35$，由无次数三正四负二门闭合。
  * 否则对**同一个 $H$**，所有 $q \in C$ **同时**满足 $h_q \in \{0,1,2\}$ 且 $(h_q=0 \Rightarrow s_q \le 3)$、$(h_q=1 \Rightarrow s_q \le 1)$、$(h_q=2 \Rightarrow s_q = 0)$。
  * 因 $D$ 中两点在 4 条三迹中各至多出现 4 次，有 $H_C = 12 - \sum_{d \in D} h_d \ge 4$。
  * 记 $C$ 中 $h_q = i$ 的点数为 $x_i$（$x_0+x_1+x_2=5, H_C = x_1+2x_2$），则：
    $$\sum_{q \in C} s_q \le 3x_0 + x_1 = 3(5 - x_1 - x_2) + x_1 = 15 - 2H_C + x_2,$$
    $$\sum_{d \in D} s_d \le 16 - (12 - H_C) = 4 + H_C.$$
    两式相加得 $\sum_{v \in P} s_v \le 19 - H_C + x_2$。又由 $H_C \ge 4$ 知 $H_C - x_2 = x_1 + x_2 \ge \lceil H_C/2 \rceil \ge 2$，故 $\sum_{v \in P} s_v \le 17 < 18$，与实际总度 18 矛盾。

---

### 4. 认可的精确 Scope 边界

1. **通用修复门：** 认可 [FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md)（$\le 4$ 正各 $\ge 4$、$N_2 \le 3$、$N_1=0$、其余负 $\ge 3$ 任意、$D \le 7$、底集不限）与 [THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md)（$\le 3$ 正各 $\ge 4$、$N_2 \le 4$、$N_3 \le 35$、$N_1=0$、其余负 $\ge 4$ 任意、无 $D$ 及底集限制）的完整定理。
2. **24 点子支闭合范围：** 认可 [TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_THREE_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_THREE_TRIPLES.md) 对 **24 点、35 条五元边、$\delta=7$（7 个八度点 $P$、17 个七度点 $L$）、无全七度边、恰 1 条 $P$-内部边、$n_4=0$ 且 $r = n_3 \le 4$**（含新增整库存 $(n_2,n_3,n_4)=(11,3,0)$ 与 $(9,4,0)$，以及统一的 $r \in \{0,1,2\}$）的完整纸面证明。
3. **不越界声明：** 本审阅仅确认上述两个通用门及 P7 I1 无四迹 $r \le 4$ 子支闭合，不涉及 $r \ge 5$ 或含四迹的其余 P7 分支，亦不声称整个 24 点或 $m(5) \ge 36$ 全题已证明。

