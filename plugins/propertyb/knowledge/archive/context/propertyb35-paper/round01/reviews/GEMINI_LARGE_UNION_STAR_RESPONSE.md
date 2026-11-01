**HERO — 静态数学对抗核查报告：六正大并门、六高一内部唯一高迹、七混合正一负三门及七高三内部第五覆盖域**

本次核查仅针对指定文件及新增段落做静态数学审阅，**未执行任何程序或 Lean**。

---

### 1. 实际读取的文件与范围
* [SIX_POSITIVE_LARGE_UNION_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SIX_POSITIVE_LARGE_UNION_REPAIR.md)（全文，1–70行）
* [ONE_HIGH_TRACE_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/six_high_one_internal_high/ONE_HIGH_TRACE_PROOF.md)（全文，1–42行）及所引 [FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md)（1–60行）
* [SEVEN_MIXED_POSITIVE_ONE_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_MIXED_POSITIVE_ONE_TRIPLE.md)（全文，1–56行）
* [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md)（定理声明 1–25行，第五覆盖域与返回原染色 215–293行）

---

### 2. 逐项数学与算术核查

#### (1) [SIX_POSITIVE_LARGE_UNION_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SIX_POSITIVE_LARGE_UNION_REPAIR.md)（$\le 6$ 正4集、正并 $\ge 14$、$\le 8$ 负3、$\le 20$ 负4、总出现 $\le 7$）
* **最大正出现 $\le 2$（算术与弦界）**：
  正总关联 $\le 24$ 且正并 $\ge 14$ 迫双重点（$a_v=2$）数 $\le 24-14=10$，每名双重点负出现 $\le 5$，故负族中双重点总关联 $J_3+J_4\le 50$，且8个负三集中 $J_3\le 24$。由 $\alpha_3=(p^3-q^3)/3 = 93/4096 > \alpha_4=(p^4-q^4)/4 = 2145/262144 > 0$（$p=7/16, q=1/4$），坏概率和在 $J_3=24, J_4=26$ 处取上界：
  $$8q^3+20q^4+24\alpha_3+26\alpha_4 = 8p^3+\frac{13}{2}p^4+\frac{27}{2}q^4 = \frac{87808+31213+6912}{131072} = \frac{125933}{131072} < 1.$$
  （正并 $\ge 16$ 时预算 $40=24+16$ 给出 $8p^3+4p^4+16q^4 = 14401/16384 < 1$ 亦精确成立。）
* **高出现次数与交换后“禁 $w$ 的4对3收尾”**：
  * $k\ge 3$ 且余 $\le 2$ 正集（$16>4$）或 $k=3$ 余3不交正集（$64 > 8\cdot 4+4=36$）直接闭合。
  * 余3正集交于 $y$（命中2集、余 $A$）：若四份 $\{x,y,a\}$（$a\in A$）全为负三集，则 $x$ 度7饱和（正3+负三4），$y$ 已有正 $\ge 2$ 及这4个负三集，故在剩余 $\le 4$ 个负三集和 $\le 20$ 个负4集中，含 $y$ 的索引数满足 $r+b\le 7-2-4=1$。
  * 改令 $x$ 蓝、保持 $y$ 红：4个指定负三集因含蓝 $x$ 被避开，剩余 $\le 4$ 个待击中正集（避开 $x,y$，若恰4个则为三3一4）。余 $\le 3$ 个正集（$9>1$ 或 $27 > 4r+(4-r)+b\le 7$）及余4个不交正集（$3^3\cdot 4=108 > 16r+4(4-r)+4b+(20-b)\le 48$）均闭合。
  * 余4个正集有交点 $z$（恰命中2集，余 $U,V$ 大小 $\ge 3$ 避开 $y,z$）：$U\cap V=\emptyset$ 时 $9>7$；若 $w\in U\cap V$ 且 $\{y,z,w\}$ 是负三集，则由 $r+b\le 1$ 知 $r=1, b=0$，即 $\{y,z,w\}$ 是**唯一**含 $y$ 的剩余负集。再令 $w$ 蓝、保留 $y,z$ 红：$U\setminus\{w\}, V\setminus\{w\}$ 各大小 $\ge 2$；若仍有交点 $c$，则 $\{y,z,c\}$ 避开 $w$ 且含 $y$，不可能为负三集；若不交，给出 $\ge 2\times 2=4$ 份四点候选 $\{y,z,u',v'\}$（均含 $y$ 且避开 $w$）。此时含 $y$ 的唯一负三集 $\{y,z,w\}$ 已因 $w$ 蓝被避开，其余 $\le 3$ 个负三集均不含 $y$（故至多等于 $\{z,u',v'\}$，各堵 $\le 1$ 份），且 $b=0$ 知无含 $y$ 的负4集（不含 $y$ 的4集不能包含于含 $y$ 的四点集），总堵数 $\le 3 < 4$，收尾严密。

#### (2) [ONE_HIGH_TRACE_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/six_high_one_internal_high/ONE_HIGH_TRACE_PROOF.md)（24点 $|P|=6$、1内部边 $C$、1非内部高迹 $T$）
* **预算与选点**：$|P|=6$（一9五8）、$|L|=18$（全7度），非内部多迹盈余 $14-4=10$，故 $|T|=3\implies (n_2,n_1)=(8,25)$，$|T|=4\implies (n_2,n_1)=(7,26)$，恒有 $n_1+n_2=33$。由 $|C|=5$ 知 $|C\cap T|\ge |T|-1\ge 2$，必含8度点 $q$。染 $q$ 蓝、$P\setminus\{q\}$ 红，内部边 $C$ 与高迹 $T$ 均 proper，给出 $m=6-s$ 个正4集、$n_2-s$ 个负3集、$n_1-m$ 个负4集。
* **$s\ge 1$**：$m=6-s\le 5$，负3集 $n_2-s\le 7\le 10$，负约束总数 $(n_2-s)+(n_1-(6-s)) = n_1+n_2-6 = 33-6 = 27 \le 35$，调用 [FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md) 的总负35推论成立。
* **$s=0$（真实 $q$-star 正并下界）**：$q$ 的8条边为内部 $C$（0个 $L$ 点）、高迹边（$5-|T|\in\{2,1\}$ 个 $L$ 点）及6条单迹边（6个正4集）。由 $q$ 与全部18名 $L$ 点的点对覆盖，6个正4集的并集至少含 $18-(5-|T|)\in\{16,17\}\ge 14$ 点，负族为 $(8,19)$ 或 $(7,20)$，完全满足 `SIX_POSITIVE_LARGE_UNION_REPAIR.md`。

#### (3) [SEVEN_MIXED_POSITIVE_ONE_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_MIXED_POSITIVE_ONE_TRIPLE.md)（$\le 7$ 正3/4集且 $\le 1$ 正3集、$\le 1$ 负3、$\le 20$ 负4、总出现 $\le 7$）
* **最大正出现 $\le 2$**：无正3集时 $20(7/16)^4+(7/16)^3 = 53508/65536 < 1$；有唯一正3集 $Q$ 时，20个负4集由弦界与 $\sum_B|B\cap Q|\le 18$ 得 $\le 14(7/16)^4+6(1/2)^3(7/16) = 55118/65536$，唯一负3集坏概率 $\le (1/2)^3 = 1/8 = 8192/65536$，总和 $\le 63310/65536 < 1$。
* **高出现次数 $k\ge 3$**：余 $\le 2$（$9>1$）、余3（$|R|\le 2, 3>1$ 或 $27>8$）、余4不交（$3\cdot 4^3=192 > 16+80=96$）、余4有3重点 $y$（$3>1$）均闭合；余4有2重点 $y$ 剩 $U,V$（大小 $\ge 3,4$）按 $|U\cap V|\ge 2$（$2>1$）、$|U\cap V|=0$（$12 > \max(4+3, 1+4)=7$）、$|U\cap V|=1$（若 $\{x,y,z\}$ 是唯一负3集，删 $z$ 得 $\ge 2\times 3=6 > 7-3-1=3$ 份四点候选）完整闭合。

#### (4) [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md#L225-L293) 第五覆盖域（missing星、恰两高迹避 $C$）
* **强制边与跨对计数**：missing星中心 $a$（$c_a=0$）、三叶 $b,c,d$（$c=2$）、$|C|=3$（$c_q=3$）。两高迹 $\subseteq D=\{a,b,c,d\}$（大小 $\alpha,\beta\in\{3,4\}$），$n_2=11-\alpha-\beta\in\{5,4,3\}, n_1=19+\alpha+\beta$。因内部边不含 $a$ 且高迹不含 $C$，点对覆盖强制 $J$ 含3条不同索引边 $aq$（$q\in C$）。两高迹在 $D$ 中交集 $\ge 2$，必含星叶 $u\in I\subseteq\{b,c,d\}$；余 $\le 2$ 条边不能连满 $u$ 与三名 $C$ 点，故 $\exists q\in C, qu\notin E(J)$ 且 $S=d_J(q)+d_J(u)\ge 1$。染 $q,u$ 蓝得 $m=9-S=\alpha+\beta-2+t, t=n_2-S, B=21-t$：
  * $\alpha+\beta\in\{7,8\}$（含4迹）：全部落入8门（含总负21推论）或7门（22负4加强）。
  * $\alpha=\beta=3$ 且可选 $S\ge 2$：$t\le 3, m=4+t\le 7, B\le 21$，落入 `SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md`。
* **无法选 $S\ge 2$ 的刚性分类**：迫 $\forall u\in I, d_J(u)=0$ 且 $\forall q\in C, d_J(q)=1$，故 $J$ 的余下2条无环边必位于 $D\setminus I$：
  * 两迹均不含 $a$：$I=\{b,c,d\}, |D\setminus I|=1$，无环多重图不可能放2边，排除。
  * 两迹同为 $abc$：$I=\{b,c\}, J=aC+2ad$。染 $q,a$ 蓝得5正4+1正3、0负3、20负4，由 `SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md` 闭合。
  * 两迹为 $abc, abd$：$I=\{b\}$，余2边在 $\{a,c,d\}$ 上且含 $a$ 的条数为 $x\in\{0,1,2\}$。染 $q,a$ 蓝得 $(7-x)$ 正4 + 1正3、$(2-x)$ 负3、$(18+x)$ 负4：$x=2$ 由 `SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md` 闭合，$x=1$（6正4+1正3、1负3、19负4）由新增 `SEVEN_MIXED_POSITIVE_ONE_TRIPLE.md` 闭合，$x=0$（$J=aC+2cd$）诚实保留为未闭合 **C2型**。
  * 两迹为 $abc, bcd$：$I=\{b,c\}, J=aC+2ad$，诚实保留为未闭合 **B型**（染 $q,a$ 蓝时 $bcd$ 全红，其外部2集是必须保留的**负二集**，不能丢弃或直接调零负三混合门）。

---

### 3. 核查结论
在本次列明的静态审阅范围内，**所有证明逻辑、有理数算术、逐点索引度预算及未闭合边界（B型负二集与C2型）均完全严密，未见任何数学缺口**（局部结论不代表整个24点三内部边或 $m(5)\ge 36$ 完成）。

