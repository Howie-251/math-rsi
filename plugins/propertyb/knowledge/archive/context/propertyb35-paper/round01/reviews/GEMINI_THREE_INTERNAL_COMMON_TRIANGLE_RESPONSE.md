**HERO — Substantive Adversarial Review: `FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md` and New Sections 3–4 of `TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md`**

This review is a static mathematical audit of the requested files and sections (**no code or Lean was executed**).

---

### 1. Files and Ranges Actually Inspected
* [FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md) (full file, lines 1–54)
* [TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md) (theorem statement/scope lines 1–13, common structure lines 82–105, new Third & Fourth Coverage Domains and conclusion lines 132–229)
* [SEVEN_POSITIVE_FOUR_SET_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_POSITIVE_FOUR_SET_REPAIR.md) (lines 69–90, the $\le 22$ negative 4-set strengthening invoked in the Fourth Coverage Domain)

---

### 2. Adversarial Audit of Each New Argument

#### (1) [FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md) ($\le 4$ positives of size $\ge 2$, $\le 3$ neg3, arbitrary neg4, total indexed occ $\le 7$)
* **Overlapping positives ($a_x\ge 2$) or $\le 3$ disjoint positives**: Fixing $x$ leaves $\le 2$ positives (closing via $|R|\le 2$ or $\ge 2^2=4 > 3$ 3-point candidates); 3 disjoint positives give $\ge 2^3=8 > 3$ 3-point candidates.
* **Four disjoint positives $A_1..A_4$ with $\max s_i \ge 3$**:
  Under independent uniform selection from each $A_i$, each active negative 3-set has probability $\le 2^{-3}=1/8$ (total $\le 3/8$). Each active negative 4-set $B$ uses one point per $A_i$, so 4-variable AM-GM and $b_v\le 7-1=6$ give:
  $$\sum_B \Pr(B\subseteq R) \le \frac{1}{4}\sum_{i=1}^4\sum_{v\in A_i} 6 s_i^{-4} = \frac{3}{2}\sum_{i=1}^4 s_i^{-3} \le \frac{3}{2}\left(\frac{3}{8}+\frac{1}{27}\right) = \frac{89}{144},$$
  and $\frac{3}{8} + \frac{89}{144} = \frac{143}{144} < 1$.
* **Four disjoint 2-sets ($s_1=s_2=s_3=s_4=2$, 16 candidates on 8 vertices)**:
  Each active negative 3-set ($t\le 3$) blocks 2 candidates and uses 3 incidences on $\bigcup A_i$; each active negative 4-set ($b$) blocks 1 candidate and uses 4 incidences. Since each of the 8 vertices has negative degree $\le 7-1=6$, $3t+4b\le 48$, so total blocked candidates satisfy
  $$2t + \left\lfloor\frac{48-3t}{4}\right\rfloor = 12, 13, 14, 15 < 16 \quad (t=0,1,2,3).$$

#### (2) Third Coverage Domain ([TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md#L132-L175): $2\le r\le 4$ higher traces, at least one meets $C$)
* **Unique higher-trace incidence at $q\in C$**: Since $w_q = \sum_{E\ni q, E\not\subseteq P}(|E\cap P|-1)\le 3$ and any higher trace contributes $k-1\ge 2$, $q\in C$ belongs to **at most one** higher trace. Picking $q\in C$ in a higher trace gives $w_q=(k-1)+s\in\{2,3\}$ ($s\le 1$), $m=4-s\le 4$ positive 4-sets, $n_2-s$ negative 3-sets, and $r-1$ missed higher traces (whose exterior sets in $L$ are avoided by fixing a Blue set $Z\subset L$ of size $|Z|\le r-1$).
* **$r=2$**: $|Z|\le 1$ leaves $\le 4$ positive 3/4-sets, $\le 5\le 8$ neg3, $\le 32$ neg4 (closed by Lemma A).
* **$r=3$**: $|Z|\le 2$ leaves $\le 4$ positives of size $\ge 2$ and $n_2-s\le 3$ neg3 (closed by `FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md`).
* **$r=4$**: Here $(n_3,n_4,n_2)\in\{(4,0,1),(3,1,0)\}$, so $n_2\le 1$ and $|Z|\le 3$. If all shrunk positives have size $\ge 2$, `FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md` applies. If some $A_0$ shrinks to a singleton $\{x\}=A_0\setminus Z$, then $|Z|=3$ and $Z\subset A_0$. Because the 5 non-internal edges at $q$ cover all 17 points of $L$ with total $L$-size $20-w_q\le 18$, their total repeat surplus on $L$ is $3-w_q\le 1$. Hence any other positive 4-set $A$ at $q$ meets $A_0$ (and thus $Z$) in at most 1 vertex, leaving $|A\setminus Z|\ge 3$. Fixing $x\in R$ leaves $\le 3$ positive 3/4-sets avoiding $x$, which close via $|R|\le 2$, $\ge 3 > 1$ 3-point candidates, or $3^3=27 > 4t_x+(1-t_x)+(6-t_x)=7+2t_x\le 9$ 4-point candidates.

#### (3) Fourth Coverage Domain ([TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md#L176-L223): Missing graph $F$ is a triangle on $D$, $2\le r\le 4$, all higher traces avoid $C$)
* **Structure**: $|C|=4$ ($c_q=3$) and $|D|=3$ ($c_u=1$). Every higher trace avoiding $C$ must equal $D$ (so $n_4=0, n_3=r, n_2=9-2r\in\{5,3,1\}, n_1=23+r$).
* **Cross-selection lemma on $J$ ($C\times D$)**:
  * $|E(J)|=3$ ($r=3$): If every independent cross-pair had $s_q+s_u=0$, any positive-degree vertex would be adjacent to the entire opposite part, forcing all 12 cross-edges to be present, contradiction. Thus $\exists (q,u)\in C\times D$ with $qu\notin E(J)$ and $S=s_q+s_u\ge 1$.
  * $|E(J)|=5$ ($r=2$): If every independent cross-pair had $s_q+s_u\le 1$, picking $v$ with $s_v\ge 2$ forces $v$ to be adjacent to all of the opposite part, and forces all other vertices in $v$'s part to have degree $0$ (otherwise $\ge 6$ or $\ge 8$ cross-edges would be needed), which in turn prevents any opposite vertex from having degree $\ge 2$, capping $|E(J)|$ at $3$ (if $v\in C$) or $4$ (if $v\in D$), contradiction. Thus $\exists (q,u)$ with $qu\notin E(J)$ and $S\ge 2$.
  * $|E(J)|=1$ ($r=4$): Picking one endpoint of the unique edge and a non-adjacent vertex in the opposite part gives $qu\notin E(J)$ and $S=1$.
* **Exact signed counts & gate dispatch**:
  Coloring $q\in C, u\in D$ Blue makes all 3 internal edges and all $r$ higher traces $D$ proper, creates 0 positive 3-sets ($qu\notin E(J)$), leaves $t = n_2 - S$ negative 3-sets,
  $$m = (8-3-s_q) + (8-1-r-s_u) = 12 - r - S = 3 + r + t$$
  positive 4-sets, and $b = n_1 - m = (23+r)-(3+r+t) = 20 - t$ negative 4-sets on $|L|=17$:
  * $r=2$ ($0\le t\le 3$): $t=3\implies (m,t,b)=(8,3,17)$ (17-point 8-gate); $t\le 2\implies m\le 7, t\le 2, b\le 20\le 22$ (7-gate with the verified $\le 22$ neg4 strengthening: $2(7/16)^3+22(7/16)^4 = 63798/65536 < 1$ and $2\cdot 16+22\cdot 4=120<256$).
  * $r=3$ ($0\le t\le 2$): $t=2\implies (8,2,18)$ (17-point 8-gate); $t\le 1\implies m\le 7, t\le 1, b\le 20\le 22$ (7-gate).
  * $r=4$ ($t=0$): $(m,t,b)=(7,0,20)$ (7-gate).

---

### 3. Verdict & Remaining Scope
* **Concrete errors or gaps found**: **None.** All index/degree budgets, repeat-surplus deductions, cross-pair selections, and gate dispatches are mathematically complete and valid.
* **Exact remaining open scope in $P_7$/3-Internal**: At least two non-internal higher traces ($2\le r\le 4$), all disjoint from $C$, when the 3-edge missing graph $F$ is not a triangle (and the broader $m(5)\ge 36$ theorem remains open).

