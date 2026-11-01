### 1. Files Inspected and Actions Run

* **Files read:**
  * [`context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md)
  * [`formal/Aris4Math/ThirtyThree/Target.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Target.lean)
  * [`formal/Aris4Math/ThirtyThree/Reduction.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Reduction.lean)
  * [`formal/Aris4Math/ThirtyThree/GlobalPairs.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/GlobalPairs.lean)
  * [`formal/Aris4Math/ThirtyThree/Nineteen.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Nineteen.lean)
  * [`formal/Aris4Math/ThirtyThree/Assembly.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Assembly.lean)
  * [`context/propertyb33/round01/reduction/REPORT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/reduction/REPORT.md)
  * [`context/propertyb33/round01/nineteen/REPORT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/nineteen/REPORT.md)
  * [`proofs/propertyb33/TWENTY.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY.md)
  * [`computations/propertyb33/round01/twenty_bounds.py`](file:///Users/rfy_naiveai/Desktop/aris4math/computations/propertyb33/round01/twenty_bounds.py)
  * [`context/propertyb33/round01/small-math/TWENTY_BOUNDS.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/small-math/TWENTY_BOUNDS.json)
  * [`proofs/PROBABILITY_LEMMAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md)
  * Related implementations inspected for context: [`TwentyStructure.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyStructure.lean), [`OrdinaryLink.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/OrdinaryLink.lean), [`TwentyEight.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyEight.lean), [`TwentyStandard.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyStandard.lean), [`Twenty.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Twenty.lean), [`TwentyTwoStructure.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyTwoStructure.lean), [`TwentyTwo.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyTwo.lean).
* **Actions executed:** Strictly read-only tool calls (`view_file`, `grep_search`, `find_by_name`). No shell commands, Lake builds, or file modifications were executed.

---

### 2. Follow-up A: Comparison Against Prose Specification

Comparing the independent mathematical back-translation of [`Aris4Math.Target33`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Target.lean#L16-L18) against Section 1 of [`FORMAL_SPEC_PROPERTYB_33.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md):

* **Universe and Domain:** Lean defines `Target33.{u}` as quantifying over an arbitrary finite type $V : \mathrm{Type}\; u$ (`[Fintype V]`). The specification specifies: *"V 是任意有限集合"*. Exact match.
* **Hypergraph Objects:** Lean defines `Simple5Hypergraph V` as $E \in \mathrm{Finset}(\mathrm{Finset}\; V)$ with $\forall e \in E, |e|=5$. The specification specifies: *"E ⊆ \binom{V}{5} 是不同五元子集构成的边集"*. Both rule out multi-edges and non-uniform edges. Exact match.
* **Premise Bound:** Both specify $|E| \le 33$. Exact match.
* **Property B:** Lean defines $\exists c : V \to \mathrm{Bool}, \forall e \in E, 1 \le |\{x \in e \mid c(x) = \mathrm{true}\}| \le 4$. The specification specifies: *"存在 c:V→{0,1}，使每条 e∈E 同时包含两种颜色，即 1≤Σ_{x∈e}c(x)≤4"*. Exact match.
* **Structural Premises:** Neither Lean's `Target33` nor Section 1 of the spec assumes vertex bounds, degree regularity, pair-covering, or color balance.
* **Conclusion:** There is **zero semantic or formal mismatch** between the Lean definition `Target33` and the mathematical target specification.

---

### 3. Audit of Formal Reduction, 19-Vertex Branch, and Assembly

#### A. Reduction to $19 \le v \le 25$ ([`Reduction.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Reduction.lean))
* **Minimal counterexample:** Any minimum-vertex counterexample $H$ must cover every vertex pair, because an uncovered pair $\{x, y\}$ can be merged without shrinking any edge, yielding a smaller counterexample.
* **Upper bound $v \le 25$:** In [`card_le_twenty_five`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Reduction.lean#L22-L34), pair-covering enforces $v - 1 \le 4d(x)$ for all $x \in V$. If $v \ge 26$, then $v - 1 \ge 25$, forcing every integer degree $d(x) \ge \lceil 25/4 \rceil = 7$. Then $\sum_{x \in V} d(x) \ge 7v \ge 7 \times 26 = 182$. But $5|E| \le 5 \times 33 = 165 < 182$, a direct contradiction. (The implementation correctly uses the integer ceiling rather than the weaker continuous relaxation $v(v-1) \le 660$, which would fail at $v=26$).
* **Lower bound $v \ge 19$:** For $v \le 8$, two color classes of size $\le 4$ admit no monochromatic 5-edge. For $9 \le v \le 18$, balanced permutations give $33 \times p_v < 1$, proven by kernel scalar evaluation in [`balanced_count_strict`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Reduction.lean#L37-L41).
* **33-edge extension:** For $v \ge 8$, $\binom{v}{5} \ge \binom{8}{5} = 56 \ge 33$. A counterexample with $< 33$ edges can be padded with arbitrary 5-sets to exactly 33 edges preserving non-colorability and pair-covering.
* **Equivalence:** [`target_iff_finite_goal`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Reduction.lean#L183-L192) proves $\mathrm{Target33} \leftrightarrow \mathrm{FiniteGoal}$, where `FiniteGoal` is explicitly an unproved hypothesis over $v \in \{19, \dots, 25\}$.

#### B. Complete 19-Vertex Branch ([`GlobalPairs.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/GlobalPairs.lean), [`Nineteen.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Nineteen.lean))
* **Incidence lower bound:** Double counting vertex pairs in edges gives:
  $$20 |E| \le \sum_{p \in E_{\mathrm{offDiag}}} \binom{|p.1 \cap p.2|}{2} + 2 \binom{v}{2}$$
  At $v=19, |E|=33$, $20 \times 33 = 660$ and $2 \binom{19}{2} = 342$, forcing the sum of $\binom{|p.1 \cap p.2|}{2}$ to be at least $660 - 342 = 318$.
* **Singleton pair cap 1003:** Since $|p.1 \cap p.2| \le 4$, non-singleton intersecting pairs have $\binom{|p.1 \cap p.2|}{2} \le \binom{4}{2} = 6$. Singleton pairs contribute 0. Thus at least $\lceil 318 / 6 \rceil = 53$ ordered pairs have intersection $\ge 2$. Total ordered pairs is $33 \times 32 = 1056$. Hence ordered singleton pairs are capped at $1056 - 53 = 1003$.
* **Exact rational bound:** Without locks, evaluating the 19 positions with edge multiplier 33 and singleton pair multiplier 1003 in [`nineteen_sum_value`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Nineteen.lean#L55-L60) yields:
  $$\sum_{k \in \mathrm{Fin}\; 19} \min(A_k, B_k, C_k) = \frac{228354}{230945} < 1 \quad \left(\text{margin } \frac{2591}{230945}\right)$$
* **Status:** Discharges the 19-vertex case unconditionally via [`nineteen_propertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Nineteen.lean#L68-L78).

#### C. Assembly State ([`Assembly.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Assembly.lean))
* In the current repository state, [`Assembly.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Assembly.lean#L17-L20) defines `RemainingGoal` over $21 \le v \le 25$.
* However, per project rules and user instructions, **source interfaces for $v=20$ remain subject to full audit and are not to be called formally complete at the project level.**

---

### 4. Mathematical Audit of the 20-Vertex Attack ([`TWENTY.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY.md))

We audited the mathematical derivations in [`TWENTY.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY.md), Python verification [`twenty_bounds.py`](file:///Users/rfy_naiveai/Desktop/aris4math/computations/propertyb33/round01/twenty_bounds.py), and numerical dump [`TWENTY_BOUNDS.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/small-math/TWENTY_BOUNDS.json).

#### Step 1: Coverage of the Twelve Degree Configurations
* Let $x$ be a vertex of minimum degree $d = d(x)$.
  * Pair-covering: $4d \ge 19 \implies d \ge 5$.
  * Budget: $20d \le 165 \implies d \le 8$. Thus $d \in \{5, 6, 7, 8\}$.
* The surplus of codegrees with $x$ is:
  $$\sum_{y \ne x} (\lambda_{xy} - 1) = 4d - 19$$
  Since $\lambda_{xy} \ge 1$, at most $4d - 19$ vertices have $\lambda_{xy} \ge 2$.
  The set of codegree-1 partners $W = \{y \ne x \mid \lambda_{xy} = 1\}$ satisfies:
  $$|W| \ge 19 - (4d - 19) = 38 - 4d =: s > 0$$
* The total degree surplus across all vertices is $\sum_{z \in V} (d(z) - d) = 165 - 20d$.
  Since $W \subseteq V$ and $d(z) \ge d$, the surplus restricted to $W$ satisfies $\sum_{y \in W} (d(y) - d) \le 165 - 20d$.
  By the discrete averaging principle on $W$:
  $$\min_{y \in W} d(y) \le d + \left\lfloor \frac{165 - 20d}{|W|} \right\rfloor \le d + \left\lfloor \frac{165 - 20d}{38 - 4d} \right\rfloor$$
* Evaluating for each minimum degree $d$:
  * $d=5$: $s = 18$, $\lfloor (165 - 100)/18 \rfloor = \lfloor 65/18 \rfloor = 3 \implies d(y) \in \{5, 6, 7, 8\}$ (4 pairs).
  * $d=6$: $s = 14$, $\lfloor (165 - 120)/14 \rfloor = \lfloor 45/14 \rfloor = 3 \implies d(y) \in \{6, 7, 8, 9\}$ (4 pairs).
  * $d=7$: $s = 10$, $\lfloor (165 - 140)/10 \rfloor = \lfloor 25/10 \rfloor = 2 \implies d(y) \in \{7, 8, 9\}$ (3 pairs).
  * $d=8$: $s = 6$, $\lfloor (165 - 160)/6 \rfloor = \lfloor 5/6 \rfloor = 0 \implies d(y) = 8$ (1 pair).
* Total configurations: $4 + 4 + 3 + 1 = 12$.
* **Audit finding:** Coverage is unconditional and mathematically airtight.

#### Step 2: Actual Profile Counts
For any pair $x, y$ with codegree $\lambda_{xy} = 1$ in an $H$ with $|E|=33$:
* Double-lock edge containing both $x, y$: $\ell_{xy} = \ell_3 = 1$.
* Edges containing only $x$: $\ell_x = \ell_1 = d(x) - 1$.
* Edges containing only $y$: $\ell_y = \ell_2 = d(y) - 1$.
* Edges disjoint from $\{x, y\}$: $\ell_\emptyset = \ell_0 = 33 - 1 - (d(x)-1) - (d(y)-1) = 34 - d(x) - d(y)$.
* For all 12 pairs, $\ell_0 \ge 34 - 8 - 8 = 18 \ge 0$. Profile counts are exact.

#### Step 3: Ordinary-Link Overlap Bound in $(8,8)$
* Let $V_0 = V \setminus \{x, y\}$, so $|V_0| = 18$.
* The $d(x) - 1 = 7$ ordinary edges through $x$ yield 7 distinct 4-element subsets $L_1, \dots, L_7 \subset V_0$.
* For each $z \in V_0$, let $a_z = |\{i \mid z \in L_i\}|$, so $\sum_{z \in V_0} a_z = 7 \times 4 = 28$.
* For every integer $a \ge 0$, $\binom{a}{2} \ge a - 1$ holds identically (since $(a-1)(a-2) \ge 0$ for all $a \in \mathbb{Z}$). Thus:
  $$\sum_{z \in V_0} \binom{a_z}{2} \ge \sum_{z \in V_0} (a_z - 1) = 28 - 18 = 10$$
* Combinatorially, $\sum_{z \in V_0} \binom{a_z}{2} = \sum_{1 \le i < j \le 7} |L_i \cap L_j \cap V_0|$.
* For any pair of distinct 4-sets in $V_0$, $|L_i \cap L_j \cap V_0| \le 3$. Hence:
  $$10 \le \sum_{1 \le i < j \le 7} |L_i \cap L_j \cap V_0| \le 3 \times |\text{ordinary bad pairs}|$$
  implying $|\text{ordinary bad pairs}| \ge \lceil 10/3 \rceil = 4$.
* Meanwhile, by P8 on all 8 incident links on 19 points:
  $$q(x) \ge \left\lceil \frac{4 \times 8 - 19}{3} \right\rceil = \left\lceil \frac{13}{3} \right\rceil = 5$$
* **Audit finding:** The lower bound of 4 ordinary-ordinary bad link pairs and 5 total bad link pairs is mathematically exact.

#### Step 4: Weighted Deletion per Position in $(8,8)$
* Lock positions: $t_1 = 10, t_2 = 11$, with $N = 18, a_{10} = 9, b_{10} = 9$.
* By P4b, for center $s_1$ at position 10:
  * For an ordinary-ordinary unordered pair (type $\{1\}$ with $\{1\}$):
    $$w_{LL} = 2 \times \frac{\binom{9}{4}\binom{9}{4}}{\binom{18}{4}\binom{14}{4}} = 2 \times \frac{63}{12155} = \frac{126}{12155}$$
  * For an ordinary-doublelock unordered pair (type $\{1\}$ with $\{1, 2\}$):
    Forward weight is $\frac{\binom{9}{4}\binom{9}{3}}{\binom{18}{4}\binom{14}{3}} = \frac{21}{2210}$. Backward weight is 0 (as $2 \notin I_{10}^-$).
    $$w_{LD} = \frac{21}{2210} + 0 = \frac{21}{2210}$$
* Difference: $w_{LL} - w_{LD} = \frac{126}{12155} - \frac{21}{2210} = \frac{21}{24310} > 0$.
* Deletion lower bound at position 10:
  $$\text{Loss}_{10} \ge 5 w_{LD} + 4 (w_{LL} - w_{LD}) = 5\left(\frac{21}{2210}\right) + 4\left(\frac{21}{24310}\right) = \frac{1239}{24310}$$
* By left-right permutation symmetry, the exact same bound $\text{Loss}_{11} \ge \frac{1239}{24310}$ holds at position 11 for center $y$.
* **No double deletion / interference:** Deletions are applied to the respective position failure bounds $C_{10}$ and $C_{11}$. Since $\lambda_{xy} = 1$, no edge pair is incident to both $x$ and $y$ simultaneously (which would require codegree $\ge 2$). Within each position, the unordered weight sums the forward and backward directions once.

#### Step 5: Strict Totals Check
* All 12 totals in [`TWENTY.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY.md#L88-L101) match [`TWENTY_BOUNDS.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/small-math/TWENTY_BOUNDS.json) exactly:
  * (5,5): $2157 / 2431 < 1$
  * (5,6): $21863 / 24310 < 1$
  * (5,7): $11204 / 12155 < 1$
  * (5,8): $11487 / 12155 < 1$
  * (6,6): $11078 / 12155 < 1$
  * (6,7): $22701 / 24310 < 1$
  * (6,8): $23267 / 24310 < 1$
  * (6,9): $25147 / 25740 < 1$ (positions 11, 12)
  * (7,7): $11623 / 12155 < 1$
  * (7,8): $11906 / 12155 < 1$
  * (7,9): $19813 / 19890 < 1$ (positions 11, 12; tightest, margin $77/19890 \approx 0.00387$)
  * (8,8): $2421 / 2431 < 1$ (positions 10, 11; enhanced deletion, margin $10/2431 \approx 0.00411$)
* **Counterexample search:** No counterexample or mathematical gap was found. The derivation in [`TWENTY.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY.md) is correct as stated.

---

### 5. Smallest Key Argument and Remaining Proof Scope

* **Smallest key argument for 20 vertices:** The combination of:
  1. The pigeonhole surplus bound $\min_{y \in W} d(y) \le d + \lfloor(165 - 20d)/(38 - 4d)\rfloor$ which caps partner degrees and bounds the configuration space to 12 pairs.
  2. The identity $\binom{a}{2} \ge a - 1$ for all $a \in \mathbb{Z}$ applied to incidence on $V \setminus \{x, y\}$, yielding $\ge 4$ ordinary bad pairs in $(8,8)$ without assuming pair-coverage on $V \setminus \{x, y\}$.
* **Remaining proof scope for T33:**
  $$\text{Vertices } v \in \{21, 22, 23, 24, 25\}$$
  * $v=19$: formally proved and integrated in Lean.
  * $v=20$: mathematically established in [`TWENTY.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY.md); Lean formalization files are present on disk, but in accordance with instructions, not called closed at the project level.
  * $v \in \{21, \dots, 25\}$: still require complete branch resolution to prove `Target33`.

---

### 6. Mathematically Justified Next Steps (21 and 22 Vertices)

* **Analysis of 22 vertices with minimum degree 7:**
  * At $v=22$, pair-covering gives $d(x) \ge 6$. If there is a degree-6 vertex, [`TwentyTwo.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyTwo.lean) already verifies (6,6) at $4155/4199 < 1$ and (6,7) at $441/442 < 1$.
  * If there are no degree-6 vertices, every degree is $\ge 7$. Total surplus $\sum (d(z) - 7) = 165 - 22 \times 7 = 11$.
  * Hence at least $22 - 11 = 11$ vertices have degree exactly 7.
  * For any such degree-7 vertex $x$, surplus is $4 \times 7 - 21 = 7$, so at most 7 bad partners exist. Among the other $\ge 10$ degree-7 vertices, at least $10 - 7 = 3$ have $\lambda_{xy} = 1$. This guarantees the existence of a $(7,7)$ pair with $\lambda_{xy} = 1$ (proved in [`TwentyTwoStructure.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyTwoStructure.lean#L80)).
  * *Concrete next improvement (Conjecture):* The baseline $(7,7)$ profile with standard deletion at $v=22$ is tight or slightly exceeds 1. However, the ordinary-link lower bound developed for $(8,8)$ at 20 vertices directly ports here: on $V \setminus \{x, y\}$ of size 20, the $d(x)-1 = 6$ ordinary edges have incidence $6 \times 4 = 24$, giving $\sum \binom{a_z}{2} \ge 24 - 20 = 4$, which forces at least $\lceil 4/3 \rceil = 2$ ordinary-ordinary bad pairs at higher weight $w_{LL}$, providing the extra margin needed to close the $(7,7)$ case.

* **Analysis of 21 vertices:**
  * Minimum degree is $\ge \lceil 20/4 \rceil = 5$. Total degree 165, average $165/21 \approx 7.857$.
  * *Concrete next improvement (Conjecture):* If a degree-5 or degree-6 vertex exists, partner surplus on $W$ caps the partner degree similarly to $v=20$. If minimum degree is 7, total degree is $21 \times 7 = 147 \le 165$, so a triple-lock configuration or enhanced ordinary-link deletion on (7,7) pairs will provide sufficient negative drift.
