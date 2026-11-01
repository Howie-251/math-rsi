### 有限范围对抗数学审阅报告：四正五负二两负三门与三正五负二门

**审阅范围与执行声明：**
* **已完整核读文件（只读未修改）：**
  1. [FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md)
  2. [THREE_LARGE_POSITIVE_FIVE_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_LARGE_POSITIVE_FIVE_NEGATIVE_PAIRS_REPAIR.md)
  3. 进口定理接口核对：[FOUR_MIXED_POSITIVE_FOUR_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_MIXED_POSITIVE_FOUR_TRIPLES_REPAIR.md)（第 1–45 行）及上一轮已核的 [FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)。
* **执行情况：** 纯静态数学审阅，**未执行任何程序或 Lean**。
* **审阅结论：** **未发现数学反例、漏分情况或接口缺陷（PASS）**。

---

### 1. 进口门核查：三正四集、五负二、十一负三（[THREE_LARGE_POSITIVE_FIVE_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_LARGE_POSITIVE_FIVE_NEGATIVE_PAIRS_REPAIR.md)）

* **定理范围：** 任意有限底集 $L$，至多 3 个 $\ge 4$ 元正集，至多 5 个负二、至多 11 个负三、任意有限个 $\ge 4$ 元负集，无负单集，无逐点次数 $D$ 限制，输出 $|R| \le 3$。
* **逐分支核对：**
  1. **正集数 $\le 2$：** 0 或 1 正集平凡；2 正集相交取 1 点，不交则截取为四元集给 $4 \times 4 = 16$ 个二红候选，仅受至多 5 个负二阻塞（$5 < 16$）。
  2. **三正两两不交：** 截取后 $4^3 = 64$ 个三红候选，每个负二至多堵 4 份、每个负三至多堵 1 份，总堵数 $\le 5 \times 4 + 11 = 31 < 64$。
  3. **三正有交叠 $x$：** 若 $x$ 命中三正，单点完成；否则 $x$ 命中两正，余一正四集 $W$ 避 $x$。若 $W \setminus F \ne \varnothing$（$F$ 为含 $x$ 负二邻点集），取 $w \in W \setminus F$ 得 $\{x,w\}$ 完成。若 $W \subseteq F$，因 $|W|=4$，至少 4 个负二索引含 $x$，故避 $x$ 的负二索引 $H$ **至多 1 个**。将 $x$ 禁蓝，若 $H$ 存在再禁其一点 $f$，则全部负二均满足；原含 $x$ 的两正删 $\{x,f\}$ 后各 $\ge 2$ 元，$W$ 因不含 $x$ 删 $\{f\}$ 后 $\ge 3$ 元。若余三正有交点则 $\le 2$ 红完成；若两两不交则至少 $2 \times 2 \times 3 = 12$ 个三红候选，超过至多 11 个负三（$11 < 12$）。

---

### 2. 主门核查：四正四集、五负二、两负三、D7（[FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md)）

* **定理范围与预备：** 任意有限底集 $L$，至多 4 个 $\ge 4$ 元正集，至多 5 个负二（$q \le 5$）、至多 2 个负三（$t \le 2$）、任意有限个 $\ge 4$ 元负集，无负单，每点总出现次数 $D \le 7$，输出 $|R| \le 4$。正集数 $\le 3$ 直接由上述三正门（$t \le 2 \le 11$）覆盖；以下恰有 4 个正四集。
* **第 1 节（四正两两不交）：**
  * 16 个正点给出 256 个四红候选，活跃负二、负三、负四索引数 $q \le 5, t \le 2, b$ 共享同一批点的负容量 $2q + 3t + 4b \le 16 \times 6 = 96$。
  * 堵数上界为 $16q + 4t + b \le 16q + 4t + \frac{96 - 2q - 3t}{4} = 24 + \frac{31}{2}q + \frac{13}{4}t \le 24 + 77.5 + 6.5 = 108 < 256$。
* **第 2 节（存在正出现次数 $\ge 3$ 的点 $x$）：**
  * 若 $x$ 命中全部 4 个正集，取 $\{x\}$ 完成；否则 $x$ 恰命中 3 个正集，余唯一正四集 $W$ 避 $x$。
  * 若 $W \setminus F \ne \varnothing$，两红完成；否则 $W \subseteq F \implies$ 至少 4 个负二索引含 $x$，避 $x$ 的负二 $H$ 至多 1 个。
  * 令 $x$ 蓝：若无 $H$，四正删 $x$ 后均 $\ge 3$ 元，无剩余负二，由 [FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md) 完成；若有 $H$，再禁 $f \in H$ 蓝，因 $x \notin W$，$|W \setminus \{x,f\}| \ge 3$，仅原含 $x$ 的 **3 个**正集可能同时含 $x,f$ 而缩为二元集，故剩余 4 个正集大小在 $2..4$ 且**正二集数 $\le 3$**，无剩余负一／二，负三 $t \le 2 \le 4$，$D \le 7$，准确满足 [FOUR_MIXED_POSITIVE_FOUR_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_MIXED_POSITIVE_FOUR_TRIPLES_REPAIR.md)。
* **第 3 节（最大正出现次数为 2，初试与 $r \in \{0,1,4,5\}$）：**
  * 取恰含于 $A,B$ 的 $x$，余 $U,V$ 避 $x$。设过 $x$ 的负二索引数为 $r \in \{0..5\}$，不同邻点集为 $F$（$|F| \le r$）。
  * 初试令 $x$ 红、$F$ 蓝：若 $U\setminus F$ 与 $V\setminus F$ 相交则两红完成；否则记 $a=|U\setminus F|, b=|V\setminus F|$，当 $a,b>0$ 时 $ab$ 个三红候选 $\{x,u,v\}$ 仅被避 $x$ 的 $\le 5-r$ 个负二与含 $x$ 的 $\le \min(2, 5-r)$ 个负三阻塞，总堵数 $\le (5-r) + \min(2, 5-r)$。
  * $r=0 \implies 16 > 7$；$r=1 \implies a,b \ge 3, ab \ge 9 > 6$；$r=5 \implies$ 令 $x$ 蓝消去全部负二，正均 $\ge 3$，调四正最小三元门；$r=4 \implies$ 令 $x$ 蓝并禁唯一可能剩余负二的一点 $f$，仅同时含 $x,f$ 的正集可缩为二元（至多 $A,B$ 两个，$\le 3$），调四混合门。
* **第 4 节（难点 1：$r = 2$ 的最小 $K$-次数分流）：**
  * 初试堵界为 $3 + 2 = 5$，由 $a,b \ge 4-2 = 2$ 及失败 $ab \le 5$ 迫使 $a=b=2$，故 $|F|=2$ 且 $F = \{f,g\} \subseteq U \cap V$。
  * **关键度推论：** 因全局最大正出现次数为 2，且 $f,g$ 已在 $U,V$ 中各出现 2 次，故 **$f,g \notin A \cup B$**！
  * 令 $x$ 蓝，含 $x$ 的两份负二 $\{x,f\},\{x,g\}$ 满足，剩余避 $x$ 的负二多重集 $K$ 满足 $|K| \le 3$。不妨设 $v = d_K(f) \le d_K(g)$，记 $A'=A\setminus\{x\}, B'=B\setminus\{x\}$（各 3 元，且均避 $f,g$）：
    1. **$v=0$：** 取 $f$ 红，若 $A'\cap B'\ne\varnothing$ 得安全两红；否则 9 个三红对 $|K| \le 3$ 与 $t \le 2$（$9 > 5$）。
    2. **$v=1, fg \in K$：** 取 $f$ 红、$g$ 蓝。因 $g \notin A\cup B$，$A',B'$ 仍为 3 元；$fg$ 满足，余 $|K\setminus\{fg\}| \le 2$，故 $9 > 2 + 2 = 4$。
    3. **$v=1, fg \notin K$：** $f$ 在 $K$ 中唯一边为 $fw$（$w \ne g$），且 $d_K(g) \ge v = 1$ 知 $K$ 中至少有一条含 $g$ 的边。取 $f$ 红、$w$ 蓝，在 $A''=A'\setminus\{w\}, B''=B'\setminus\{w\}$（各 $\ge 2$ 元）中选点；因 $g \notin \{f\}\cup A\cup B$，**任何候选均自动不含 $g$**，故 $fw$（因 $w$ 蓝）与至少一条含 $g$ 的 $K$ 边（因 $g$ 不选）均安全，剩余可堵候选的 $K$ 边至多 $3 - 2 = 1$ 条。不交时至少 $2 \times 2 = 4$ 个三红候选对 $1 + 2 = 3$ 份堵（$4 > 3$）；相交时两红含 $f$ 且避 $w$，不含任何负二。
    4. **$v=2$：** 由 $2 \le d_K(f) \le d_K(g)$ 及 $|K| \le 3$ 知必有 $fg \in K$，且 $f$ 在 $K$ 中至多另有一邻点 $w$。取 $f$ 红、$g$ 与 $w$ 蓝。$A'',B''$ 仅可能损 $w$ 故各 $\ge 2$ 元；含 $f$ 的两条 $K$ 边因 $g,w$ 蓝而安全，若 $K$ 有第 3 条不含 $f$ 的边，因 $d_K(g) \ge 2$ 该边必含 $g$，亦因 $g$ 蓝而安全。故负二全消，$4 > 2$（仅剩 $t \le 2$ 个负三）。
    5. **$v=3$：** $K$ 的 3 条边全为平行 $fg$，取 $f$ 红、$g$ 蓝，负二全消，$9 > 2$。
* **第 5 节（难点 2：$r = 3$ 的一般共点分支 $U \cap V \cap F \ne \varnothing$）：**
  * 初试堵界为 $(5-3)+\min(2,2) = 4$，且 $a,b \ge 1$。若 $ab \le 4$，由 $|U\cap V\cap F| \ge (4-a)+(4-b)-|F| \ge 5-(a+b)$，除 $|F|=3$ 且 $(a,b) \in \{(1,4),(4,1)\}$ 外，必有 $a+b \le 4 \implies |U\cap V\cap F| \ge 1$。
  * 取 $f \in U\cap V\cap F$（同样有 $f \notin A\cup B$），令 $x$ 蓝，余 $|K| \le 2$：
    * $d_K(f)=0$：取 $f$ 红，$9 > 2 + 2 = 4$；
    * $d_K(f)=1$（边 $fw$）：取 $f$ 红、$w$ 蓝，$A'',B''$ 各 $\ge 2$ 元，余 $K$ 至多 1 条，$4 > 1 + 2 = 3$；
    * $d_K(f)=2$：直接令 $x,f$ 均蓝，全部 5 个负二均因含 $x$ 或 $f$ 而满足；因 $f \notin A\cup B$ 且 $x \notin U\cup V$，四正集 $A\setminus\{x\}, B\setminus\{x\}, U\setminus\{f\}, V\setminus\{f\}$ **大小全部恰为 3**，由 [FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md) 完成。
* **第 6 节（难点 3：$r = 3$ 的唯一非共点紧支 $(a,b)=(1,4)$）：**
  * 对称性下设 $(a,b)=(1,4), |F|=3$，则 $F \subseteq U, U\setminus F = \{u\}, V \cap F = \varnothing$。
  * 初试有 4 个互异三红候选 $\{x,u,v\}$（$v \in V=\{v_1,v_2,v_3,v_4\}$）。要被至多 2 个避 $x$ 负二与至多 2 个含 $x$ 负三全部堵满，4 个阻断索引必须全部存在且互异地一对一阻塞，故避 $x$ 的两个负二必为 $\{u,v_1\},\{u,v_2\}$，两个负三必为 $\{x,u,v_3\},\{x,u,v_4\}$（无其他负二／负三）。
  * **换色救援：** 令 $x,v_1,v_2$ 蓝，$u$ 红。
    1. 含 $x$ 的 3 个负二与 2 个负三因 $x$ 蓝满足，$\{u,v_1\},\{u,v_2\}$ 因 $v_1,v_2$ 蓝满足，故**全部负二与全部负三均已消去**；
    2. $u$ 已击中 $U$；$V'' = V\setminus\{v_1,v_2\} = \{v_3,v_4\}$ 为 2 元集；
    3. 因全局最大正出现次数为 2，且 $v_1,v_2 \in V$ 已各占 1 次正出现，$v_1,v_2$ 在 $A,B$ 中**合计至多出现 2 次**！故 $A'=A\setminus\{x\}$（3 元）与 $B'=B\setminus\{x\}$（3 元）再删去 $\{v_1,v_2\}$ 后，大小至少为 $(1,3)$ 或 $(2,2)$，均非空；
    4. 若 $u \in A\cup B$ 或余三正有交点，则连同 $u$ 至多取 3 红即完成（无活跃负二／负三，负四不堵三红）；
    5. 若余三正两两不交且均避 $u$，各取一点加 $u$ 得至少 $\min(1\cdot 3\cdot 2, 2\cdot 2\cdot 2) = 6$ 个四红候选 $\{u,a,b,v\}$。能堵它的负四必含 $u$；而 $u$ 在原系统中已占 1 次正出现（$U$）、2 次负二出现（$uv_1, uv_2$）、2 次负三出现（$xuv_3, xuv_4$），由 $D \le 7$ 知**含 $u$ 的原负四索引至多 $7 - 1 - 2 - 2 = 2$ 个**（原负二／负三虽已满足仍占原次数），$6 > 2$ 严格获救。

---

### 3. 认可的具体范围与边界声明

* **认可范围：** 静态核查确认 [THREE_LARGE_POSITIVE_FIVE_NEGATIVE_PAIRS_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/THREE_LARGE_POSITIVE_FIVE_NEGATIVE_PAIRS_REPAIR.md)（$\le 3$ 正各 $\ge 4$、$N_2 \le 5$、$N_3 \le 11$、$N_1=0$、其余负 $\ge 4$ 任意、无 $D$ 限制）与 [FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md)（$\le 4$ 正各 $\ge 4$、$N_2 \le 5$、$N_3 \le 2$、$N_1=0$、其余负 $\ge 4$ 任意、$D \le 7$、底集不限）的完整纸面证明严密成立。
* **边界声明：** 本次审阅未执行任何程序或 Lean；仅确认上述两个通用修复门本身成立，不提前计入具体 I1 实际 caller 的完整闭合，亦不代表整个 24 点或 $m(5) \ge 36$ 已证明。

