**HERO — Bounded Substantive Adversarial Review: 24-Vertex Six-High Two-Internal Pure-Pair Branch & Three New Repair Gates**

This review is based on a static mathematical and code-level inspection of the proofs and local enumeration scripts (**no code or Lean was executed**).

---

### 1. Files Actually Read
* **Caller & Existing Gate**:
  * [TWENTYFOUR_SIX_HIGH_TWO_INTERNAL_PURE_PAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SIX_HIGH_TWO_INTERNAL_PURE_PAIR.md)
  * [FIVE_POSITIVE_SIGNED_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_SIGNED_REPAIR.md)
* **Three New Repair Gates**:
  * [EIGHT_POSITIVE_18_ONE_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_POSITIVE_18_ONE_TRIPLE.md)
  * [SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md)
  * [EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md)
* **Local Domain Scripts & JSON Certificates**:
  * [THREE_EDGE_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/eighteen_one_triple/THREE_EDGE_CHECK.py) and [THREE_EDGE_CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/eighteen_one_triple/THREE_EDGE_CHECK.json)
  * [SMALL_GRAPH_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/eight_mixed_eighteen/SMALL_GRAPH_CHECK.py) and [SMALL_GRAPH_CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/eight_mixed_eighteen/SMALL_GRAPH_CHECK.json) (lines 1–80)

---

### 2. Verification of the Caller ([TWENTYFOUR_SIX_HIGH_TWO_INTERNAL_PURE_PAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SIX_HIGH_TWO_INTERNAL_PURE_PAIR.md))
* **Budget, Hitting Set, and Zero-$P$ Coverage**:
  With $|V|=24, |E|=35, \delta\ge 7$ and $|P|=6$, total degree $175 = 24\cdot 7 + 7$ forces one degree-9 vertex $h\in P$, five degree-8 vertices in $P$, and 18 degree-7 vertices in $L = V\setminus P$. Since $H$ has no all-degree-7 edge, $P$ hits every edge of $H$ (no zero-$P$-trace edge exists). The two distinct internal 5-edges are $P\setminus\{a\}$ and $P\setminus\{b\}$ ($a\neq b$), giving internal degrees $c_v=2$ on $C=P\setminus\{a,b\}$ ($|C|=4$) and $c_a=c_b=1$. The $P$-incidence surplus $\sum_{e\in H}(|e\cap P|-1)=49-35=14$ minus $8$ from the two internal edges leaves $6$ for non-internal edges; since non-internal $P$-traces have size $\le 2$, there are **6 pair-trace edges** (forming a 6-edge loopless multigraph $J$ on $P$ with degrees $s_v=d_J(v)$) and **27 singleton-trace edges** ($u_v = d_H(v)-c_v-s_v$ at each $v\in P$).
* **Single-Blue Reduction ($\exists p\in C, s_p\ge 2$, §2)**:
  Coloring $p$ Blue and $P\setminus\{p\}$ Red makes both internal edges proper (1 Blue, 4 Red), makes all $s_p$ pair traces through $p$ bichromatic, and leaves $6-s_p\le 4$ all-Red pair traces (negative triples), $u_p = d_H(p)-2-s_p \le 9-2-2 = 5$ positive 4-sets, and $27-u_p\le 27$ negative 4-sets, with indexed occurrence $\le 7\le 10$ on $L$. This matches Corollary A of [FIVE_POSITIVE_SIGNED_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_SIGNED_REPAIR.md) (whose padding from $m\le 5$ to 5 positives adds $\le 4$ to vertex occurrences, staying within $7+4=11\le 14$).
* **Matching + Attachments Reduction ($s_p\le 1$ on $C$, §§3–4)**:
  $J|_C$ is a matching of size $z\in\{0,1,2\}$, unmatched $C$-vertices contribute $k = k_a+k_b\le 4-2z$ attachments to $a,b$, and $ab$ has multiplicity $x = 6-z-k\ge 2+z$. Selecting Blue $\{p,q\}$ with $p\in C, q\in\{a,b\}, pq\notin E(J)$ makes both internal edges proper (1 or 2 Blue, 4 or 3 Red), creates 0 positive triples, leaves $t = z + k_{q'} - s_p$ negative triples, and yields
  $$m = u_p + u_q = (16+\eta) - 3 - s_p - (x + k_q) = 7 + \eta + t$$
  positive 4-sets and $27-m$ negative 4-sets ($\eta = \mathbf{1}_{h\in\{p,q\}}$).
  The explicit case split in §4 exhaustively covers all $(z, k_a, k_b)$ except $(z=0, \max(k_a,k_b)=4)$, achieving either $t=0, m\in\{7,8\}$ (dispatched to §3 of [FIVE_POSITIVE_SIGNED_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_SIGNED_REPAIR.md)) or $t=1, \eta=0, m=8, 27-m=19$ on $|L|=18$ (dispatched to [EIGHT_POSITIVE_18_ONE_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_POSITIVE_18_ONE_TRIPLE.md)).
* **Star Caller ($z=0, k_q=4, k_{q'}=0, x=2$, §5)**:
  Here $s_p=1$ ($p\in C$), $s_q=6, s_{q'}=2$. Picking $p\in C\setminus\{h\}$ and coloring $\{p,q\}$ Blue makes $pq$ the unique all-Blue pair trace (**1 positive 3-set**) and makes the other 5 pair traces bichromatic (**0 negative 3-sets**). Since $u_p = 8-2-1=5$ and $u_q = d_H(q)-7$:
  * If $q\neq h$ ($d_H(q)=8$, covering 3 of the 4 labeled placements): $u_q=1$, giving **6 positive 4-sets + 1 positive 3-set** and **21 negative 4-sets**, matching [SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md).
  * If $q=h$ ($d_H(q)=9$): $u_q=2$, giving **exact 7 positive 4-sets + 1 positive 3-set** and **20 negative 4-sets** on $|L|=18$, matching [EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md).

---

### 3. Verification of the Three New Repair Gates
1. **[EIGHT_POSITIVE_18_ONE_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_POSITIVE_18_ONE_TRIPLE.md) ($|L|\le 18$, exact 8 pos4, $\le 1$ neg3, $\le 19$ neg4, occ $\le 7$)**:
   * **$\max a_z\le 2$**: $(7/16)^3 + 19(7/16)^4 = 51107/65536 < 1$.
   * **$\max a_z = k\ge 4$**: Direct counting closes $k\ge 6, k=5$, and $k=4$ (disjoint $16+76=92<256$; overlapping at $y$ with $t=|U_0\cap V_0|\le 1$, $a=4-t\in\{3,4\}$, blocked $\le a(1-t)+3-t \in \{2,7\} < a^2$).
   * **$\max a_z = 3$ (fix $x$ Red, $0\le r\le 1, r+b\le 4$, $|U|\le 17$)**:
     * Second triple point $y$: $t=|U_0\cap V_0|\le 1$, blocked $\le a(1-t)+4-t \in \{3,8\} < a^2\in\{9,16\}$ (no equality case).
     * Remaining 5 sets have max occurrence $\le 2$: $|U|=20-E\le 17\implies E\ge 3$. For 5-point candidates $\{x\}\cup T_4$, a 2-point subset of $U$ misses at least one positive 4-set and has at most $\binom{15}{2}-\binom{11}{2}=50$ extensions; 3-point subsets have $\le 14$, 4-point subsets $\le 1$. Total blocked:
       $$50r + 14(1-r) + 14b + (19-b) = 33 + 36r + 13b \le 85 + 23r \le 108.$$
     * **$E=3$ boundary**: All $\binom{10+3-1}{3}=220$ 3-edge loopless multigraphs on 5 labels partition under $S_5$ into 7 orbits ($10+60+30+10+20+60+30=220$). Both direct 4-subset enumeration and 32-term inclusion-exclusion give $\min C_4 = 144 > 108$ (achieved on the triangle, where $4\cdot 4\cdot (\binom{9}{2}-3\binom{5}{2}+3\binom{2}{2})=16\cdot 9=144$).
     * **$E\ge 4$**: $|U|\le 16$, where $M_2\ge 7\implies C_3\ge 14>7$, $M_2=0\implies C_4\ge 80>44$, and $1\le M_2\le 6\implies E\le 8$ reuses the 86-orbit domain with $C_4\ge 178>108$.

2. **[SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md) ($\le 7$ pos of size $3/4$, $\le 1$ pos3, $\le 21$ neg4, 0 neg3, occ $\le 7$)**:
   * **$\max a_v\ge 3$**: Fixing $x$ leaves $\le 4$ sets of size $\ge 3$ and $b_x\le 4$ negative 4-sets containing $x$; all subcases close via $|R|\le 3$, $4<27$, $4<9$, or $21+3b_x\le 33<81$.
   * **$\max a_v\le 2$**: For $v\in T$ (the unique positive 3-set), $q_v \le 1 - \frac{2}{3}\cdot\frac{3}{4} = \frac{1}{2}$; for $v\notin T$, $q_v\le p = \frac{7}{16}$. By convexity of $w_j = (1/2)^j p^{4-j}$ on $j=|B\cap T|\in\{0,1,2,3\}$ and $\sum_B |B\cap T|\le 3\cdot(7-1)=18$,
     $$\sum_B \Pr(B\subseteq R) \le 21 w_0 + \frac{18}{3}(w_3-w_0) = 15\left(\frac{7}{16}\right)^4 + 6\left(\frac{1}{2}\right)^3\left(\frac{7}{16}\right) = \frac{36015 + 21504}{65536} = \frac{57519}{65536} < 1.$$

3. **[EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md) ($|L|\le 18$, exact 7 pos4 + 1 pos3 $T$, $\le 20$ neg4, 0 neg3, occ $\le 7$)**:
   * **$\max a_z\le 2$**: Chord bound gives $20 w_0 + 6(w_3-w_0) = 14 w_0 + 6 w_3 = 55118/65536 < 1$.
   * **$\max a_z\ge 4$**: Closes via $|R|\le 3$, $3<27$, $3<9$, or $4\cdot 3+17=29<81$.
   * **$\max a_z=3$ (fix $x$ Red, $b\le 4$, $|U|\le 17$)**:
     * Second triple point $y$ closes via $|R|\le 3$ or $4<9$.
     * Max occurrence $\le 2$ in remaining 5 sets: uniform 5-point candidate blocking bound is $14b + (20-b) = 20+13b \le 72$.
     * If $x\in T$ (five 4-sets remain): $E\ge 3$ reuses the 7-orbit ($C_4\ge 144>72$) and $E\ge 4$ ($\ge 80>72$ or $C_3\ge 14>4$) bounds.
     * If $x\notin T$ (one 3-set $A_0=T$ and four 4-sets $A_1..A_4$ remain): capacities $(3,4,4,4,4)$, $|U|=19-E\le 17\implies E\ge 2$.
       * $M_2\ge 3$: $C_3 = \sum_M (|A_{w_M}|-\frac{1}{2}d_J(w_M)) \ge \frac{3}{2}M_2 \ge \frac{9}{2}\implies C_3\ge 5 > b\le 4$.
       * $M_2=0$: Star gives $C_4 \ge \min(2\cdot 3\cdot 4\cdot 4, 3\cdot 4^3 - 3^3\cdot 4) = 84 > 72$. Triangle gives $\ge 3\cdot(3\cdot 4) = 36$ candidates, while each negative 4-set containing $x$ specifies either 2 isolated points + 1 triangle point (at most 4 partners in the third triangle set) or 2 triangle points + 1 isolated point (at most 4 choices in the other isolated set), giving the refined blocking bound $4b+(20-b)\le 32 < 36$.
       * $1\le M_2\le 2$: $M_2\ge E(E-7)/2\implies E\le 7$. In [SMALL_GRAPH_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/eight_mixed_eighteen/SMALL_GRAPH_CHECK.py), both enumerators produce the same 978 labeled vectors; the group action `PERMS` restricts to the 24 permutations of $S_4$ fixing label $0$ (correctly preserving the unique 3-set capacity), yielding 59 orbits. Direct enumeration and 32-term inclusion-exclusion agree and give $\min C_4 = 93 > 72$ (at $E=2, M_2=1$, where $A_0$ is isolated and $A_1..A_4$ form $2K_2$, giving $\binom{15}{2}-\binom{12}{2} + 2\cdot 3^3 = 39 + 54 = 93$).

---

### 4. Verdict & Unresolved Issues
* **Unresolved mathematical issues in the inspected scope**: **None.** All reductions, degree/source-index budgets, tagged-orbit actions, and obstruction counts are mathematically sound and complete for this local branch (which does not close non-pure-pair traces, all 24-vertex cases, or the full $m(5)\ge 36$ theorem).

