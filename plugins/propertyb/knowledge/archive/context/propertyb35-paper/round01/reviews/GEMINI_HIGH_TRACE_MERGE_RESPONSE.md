**HERO — Substantive Adversarial Review: New Small-Positive Gates, Full $P_6$/2-Internal Branch, and $P_7$/3-Internal Unique High Trace**

This review is a static mathematical audit of the new proofs (**no code or Lean was executed**).

---

### 1. Files Actually Read
* [FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md)
* [FIVE_POSITIVE_SIGNED_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_SIGNED_REPAIR.md)
* [TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md)
* [SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md) (specifically Section A warmup, lines 1–74)
* [UNIQUE_HIGH_FORBIDDEN_POINT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/three_internal/UNIQUE_HIGH_FORBIDDEN_POINT.md)

---

### 2. Adversarial Audit of the Four New Components

#### (1) [FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md) ($\le 5$ positives of size $\ge 2$, negative 4-sets only with no count bound, total indexed occ $\le 7$)
* **Repeated positive point ($a_x\ge 2$)**: If $a_x\ge 3$, $\le 2$ positives remain, giving $|R|\le 3$ (cannot contain a 4-set). If $\max a_v = 2$, fixing $x$ leaves $\le 3$ positives avoiding $x$; if $\le 2$ remain or two intersect, $|R|\le 3$; if 3 pairwise disjoint sets of size $\ge 2$ remain, they yield $\ge 2^3=8$ distinct 4-point candidates containing $x$, while at most $7-2=5 < 8$ indexed negative 4-sets contain $x$.
* **Pairwise disjoint positives ($a_v\le 1$)**: Choosing one uniform random point independently from each $A_i$ ($i\le 5$) gives $\Pr(B\subseteq R)=0$ unless $B$ takes one vertex from each of four distinct $A_i$'s, in which case independent selection between distinct $A_i$'s gives the exact equality $\Pr(B\subseteq R)=\prod_{x\in B} q_x$ ($q_x=1/|A_i|$). By 4-variable AM-GM and $b_x\le 7-1=6$ for $x\in A_i$:
  $$\sum_B \Pr(B\subseteq R) \le \frac{1}{4}\sum_{i=1}^m\sum_{x\in A_i} b_x |A_i|^{-4} \le \frac{6}{4}\sum_{i=1}^m |A_i|^{-3} \le \frac{6}{4}\cdot 5\cdot 2^{-3} = \frac{15}{16} < 1.$$
  Controlling the sum via vertex negative degree $b_x\le 6$ legitimately eliminates any need for a global bound on the number of negative 4-sets.
* **Forbidden-point reduction (§3)**: Fixing at most two exterior points $F$ Blue to hit $\le 2$ negative pairs/singletons shrinks each positive 4-set to size $\ge 2$ and discards every negative constraint meeting $F$ (already proper), without increasing any remaining vertex's indexed occurrence.

#### (2) [FIVE_POSITIVE_SIGNED_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_POSITIVE_SIGNED_REPAIR.md) (Lemma B & Corollary B strengthened to $\le 2$ negative triples)
* All three modified counts in Lemma B ($D\le 14$, 5 positives of size 3/4, $\le 2$ neg3, $\le 28$ neg4) are strict:
  * Pairwise disjoint positives: $3^5 = 243$ 5-point candidates vs $2\cdot 16 + 28\cdot 4 = 144 < 243$ blocked.
  * $a_x\ge 3$ with 2 disjoint remaining positives: $\ge 3^2 = 9 > 2$ 3-point candidates.
  * $\max a_v = 2$ (fix $x$): if two of the 3 remaining positives intersect at $y$, the last positive has size $\ge 3 > 2$ (giving $\ge 3$ 3-point candidates vs $\le 2$ neg3); if the 3 remaining positives are pairwise disjoint, $\ge 3^3 = 27$ 4-point candidates vs $2\cdot 4 + (14-2) = 20 < 27$ blocked.
* Padding in Corollary B ($m\le 5$ positives, original occ $\le 10 \to$ padded occ $\le 14$) carries over unchanged.

#### (3) [TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md) & Section A of [SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)
* **Section A of `SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md` ($\le 6$ pos4, $\le 4$ neg3, $\le 22$ neg4, occ $\le 7$)**:
  * $\max a_z\le 2$: Number of double points is $r\le 24/2=12$, so total double-point negative incidences satisfy $J_3+J_4\le 5r\le 60$ and $J_3\le 12$. Since $\alpha_3 = 93/4096 > \alpha_4 = 2145/262144 > 0$, the chord bound is maximized at $J_3=12, J_4=48$, giving $4p^3+12p^4+10q^4 = 53324/65536 < 1$.
  * $\max a_z\ge 4$ closes via $16>4$; $\max a_z=3$ closes via $64>20$, except when 3 remaining positives share $y$ in 2 sets and all 4 candidates $\{x,y,a\}$ ($a\in A$) are negative 3-sets. Then $x$ is degree-7 saturated ($3+4=7$) and $y$ has $b\le 7-2-4=1$ negative 4-set; flipping $x$ Blue and keeping $y$ Red eliminates all 4 negative 3-sets and leaves at most four 3/4-sets avoiding $x,y$, closing via $1<27$, $1<9$, or $4b+(22-b)\le 25 < 3^3\cdot 4=108$.
* **Full $P_6$/2-Internal Branch (`TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md`)**:
  * $5|H|\ge 174\implies |H|=35$, $P$ has degrees $(9,8,8,8,8,8)$ and hits every edge, and non-internal traces satisfy $n_2+2n_3+3n_4=6, N_1=33-n_2-n_3-n_4$, yielding the exact 7 inventories.
  * $(6,0,0;27)$ calls the already reviewed pure-pair theorem.
  * In all 6 higher-trace inventories ($\S\S 4\text{--}8$), picking a single Blue $q\in C$ makes both internal edges proper, creates 0 all-Blue non-internal traces, and leaves $m = d_H(q)-2-k-s$ positive 4-sets, $n_2-s$ negative 3-sets, $N_1-m$ negative 4-sets, and missed higher traces as negative pairs/singletons:
    * $(4,1,0;28)$ & $(3,0,1;29)$: If an 8-degree $q\in C\cap T$ exists (automatic for $|T|=4$ since $|T\cap C|\ge 2$), $m=5-s\le 5$, neg3 $\le 4$, neg4 $\le 27$ (Cor A). Otherwise $|T|=3, h\in C, T=\{h,a,b\}$; picking $q=h$ gives $m=6-s, 4-s$ neg3, $22+s$ neg4, handled by Cor A for $s\ge 1$ and by Section A of `SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md` for $s=0$ $(6,4,22)$.
    * $(0,0,2;31)$: Pick 8-degree $q\in C\cap T_1$; either $k=2$ ($m=4$, Cor A) or $k=1$ ($m=5$, 1 negative singleton forbidden $\to$ Cor B).
    * $(1,1,1;30)$: Pick 8-degree $q\in C\cap T_1$; either $k=2$ ($m=4-s$, Cor A) or $k=1$ ($m=5-s$, $\le 1$ neg3, $\le 26$ neg4, 1 negative pair forbidden $\to$ Cor B).
    * $(2,2,0;29)$: If an 8-degree $q\in C\cap(T_1\cup T_2)$ exists, $k=2$ uses Cor A and $k=1$ ($m=5-s, 2-s\le 2$ neg3, $\le 26$ neg4, 1 negative pair forbidden) uses the strengthened 2-triple Cor B; if neither contains an 8-degree $C$-point, $h\in C$ and $T_1=T_2=\{h,a,b\}$, so $q=h$ gives $k=2, m=5-s\le 5$ (Cor A).
    * $(0,3,0;30)$: If an 8-degree $q\in C$ hits $k\in\{1,2,3\}$ triples, $m=6-k\le 5$, 0 neg3, and $3-k\le 2$ negative pairs are avoided by forbidding $|F|\le 2$ points, reducing to `FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md`; otherwise $T_1=T_2=T_3=\{h,a,b\}$ with $h\in C$, and $q=h$ gives $k=3, m=4$ (Cor A).

#### (4) [UNIQUE_HIGH_FORBIDDEN_POINT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/three_internal/UNIQUE_HIGH_FORBIDDEN_POINT.md) ($P_7$/3-Internal, Unique High Trace Avoiding Common $C$)
* **Actual-$H$ reduction (§3)**: 3 internal edges on 7 vertices leave $C=\bigcap e_{\text{int}}\neq\emptyset$ ($c_q=3$). With a unique higher trace $T$ of size $r\in\{3,4\}$ disjoint from $C$, excess $9$ gives $n_2=10-r\in\{7,6\}, n_1=21+r\in\{24,25\}$. Coloring $q\in C$ Blue ($s\le 3$) and fixing one Blue vertex $z\in W = e_T\cap L$ ($|W|=5-r$) makes internal edges and $T$ proper, discards all other negatives containing $z$, and leaves $m=5-s$ positive 3/4-sets in $L\setminus\{z\}$ (16 points), $\le 7-s$ neg3, and $\le 20+s$ neg4.
* **$s\ge 1$ (Lemma A′)**: $m\le 4$ positives of size 3/4, $\le 6\le 8$ neg3, $\le 23\le 32$ neg4; closes via $9>8$, $27>8$, or $81 > 8\cdot 4+32=64$.
* **$s=0$ (Lemma C)**: By pair-covering at $q$, the 5 positive 4-sets cover all 17 points of $L$, so $a=\#\{i:z\in A_i\}\in\{1,2,3,4\}$ and the repeat surplus on the 16 points of $L\setminus\{z\}$ is $D = (20-a)-16 = 4-a \in \{0,1,2,3\}$.
  * $\max \text{occ}_{A'}\ge 3$ closes via $9>7$.
  * For $\max \text{occ}_{A'}\le 2$ ($D$-edge multigraph $J$ on 5 labels):
    * Any edge covering all edges of $J$ (fixing $x$ Red, $t_x+b_x\le 5$) leaves 3 disjoint sets of size $\ge 3$, giving $\ge 27 > 4t_x+(7-t_x)+b_x\le 22$.
    * $D=0$: $3^4\cdot 4 = 324 > 7\cdot 16 + 20\cdot 4 = 192$.
    * $D=2$ matching ($a=2$): At least one matching edge covers a 3-set; fixing its point $x$ Red leaves at most one 3-set among $\{U,V,W\}$, so $(U\setminus\{y\})\times(V\setminus\{y\})\times W$ has size $\ge \min(2\cdot 3\cdot 4, 3^3) = 24 > 22$.
    * $D=3$ with no 2-vertex edge cover ($a=1$, one 3-set and four 4-sets): $J$ must be $P_3\sqcup K_2$ or $ab^2\sqcup cd\sqcup\text{isolated}$. Fixing the independent edge point $w$ Red ($t_w\le 5$) gives either $|L_1|+|L_2|-1 \ge 3+4-1 = 6$ ($P_3$ type) or $2\cdot 3 = 6$ (parallel type) 3-point candidates containing $w$, strictly exceeding $t_w\le 5$ (and negative 4-sets block 0).

---

### 3. Verdict & Scope
* **Concrete errors or gaps found**: **None.** Every inequality, degree/source-index budget, and forbidden-point reduction is sound.
* **Valid scope**: Closes the full 24-vertex, no-all-7-edge, $|P|=6$, 2-internal-edge branch (`TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md`) and the 24-vertex, $|P|=7$, 3-internal-edge, unique-higher-trace branch (`UNIQUE_HIGH_FORBIDDEN_POINT.md`), together with the supporting repair lemmas. Other 24-vertex branches and the full $m(5)\ge 36$ theorem remain open.

