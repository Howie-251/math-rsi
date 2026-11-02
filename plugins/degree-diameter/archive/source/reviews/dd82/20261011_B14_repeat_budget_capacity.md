### 1. Inspection and Execution Record

- **Files Read in Full**:
  1. [`proofs/dd82/n59/seven_triangle_nonzero_repeat_budget_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/seven_triangle_nonzero_repeat_budget_20261011.md)
  2. Predecessor dependencies examined: [`proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md), [`proofs/dd82/n59/zero_heavy_global_capacity_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/zero_heavy_global_capacity_20261011.md), [`proofs/dd82/n59/nonzero_support_transport_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/nonzero_support_transport_20261011.md), [`proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md).
  3. [`formal/DegreeDiameter/N59Capacity.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean)
  4. [`formal/ReviewN59Capacity.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN59Capacity.lean)
  5. [`formal/logs/n59-capacity-global-second.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n59-capacity-global-second.log)
  6. [`formal/logs/n59-capacity-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n59-capacity-type-axiom-audit.log)
- **Commands Executed**: **Zero**. No subprocesses, shell commands, Lake builds, or solver runs were executed by the reviewer. Build logs, test executions, and proof scripts were inspected strictly as static artifacts.
- **Model and Effort Metadata**: Gemini 3.8 Flash (High), reasoning effort `high`.
- **Baseline Alignment**: No work on known orders 63–65 was requested or performed. Analysis is restricted strictly to unresolved orders 58–62.

---

### 2. $n=59$: Nonzero Repeat Budget at Seven Triangles ($T=7, m=21$)

The paper [`seven_triangle_nonzero_repeat_budget_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/seven_triangle_nonzero_repeat_budget_20261011.md) analyzes the surviving branch of $T=7, m=21$, where nonedges inside $N$ have total repeat weight $W = \sum_{\{u, v\} \subseteq N, u \not\sim v} B_{uv} > 0$.

#### (1) Derivation of the Exact Slack Identity $8 = 2W + l_1 - 2h_3 + R_{NZ}$
1. **Global Slack Decomposition**:
   From [`zero_heavy_global_capacity_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/zero_heavy_global_capacity_20261011.md), total slack is $2(4m - 3T - 59) = 2(4(21) - 3(7) - 59) = 8$.
   - $\sum_{n \in N} \ell_n = l_1 + 2l_2$, where $l_i$ counts light defect edges in $Z$ having $i$ common neighbors in $N$.
   - $2D = 2(\sum h_n - H_{ZZ}) = 2h_2 + 4h_3$, where $h_i$ counts heavy defect edges in $Z$ having $i$ common neighbors in $N$.
   - $\sum_{n \in N} R_n = R_{NN} + R_{NZ}$, where $R_{NN} = 2\sum_{\{u, v\} \subseteq N, u \not\sim v} (B_{uv} - \binom{q_{uv}}{2})$.
   - This gives:
     $$8 = l_1 + 2l_2 + 2h_2 + 4h_3 + R_{NN} + R_{NZ}\tag{1}$$
2. **Pair Counting & Exact Cancellation**:
   - Let $P$ count unordered nonedges in $N$ with $q_{uv} = 2$ zero common neighbors. Each such pair has a unique pair of zero common neighbors.
   - Pairs in $Z$ with common neighbors in $N$: light pairs with 2 common neighbors contribute $\binom{2}{2} = 1$ ($l_2$ times); heavy pairs with 2 common neighbors contribute $\binom{2}{2} = 1$ ($h_2$ times); heavy pairs with 3 common neighbors contribute $\binom{3}{2} = 3$ ($h_3$ times).
   - Thus $P = l_2 + h_2 + 3h_3$ (equation 2).
   - From the definition of $R_{NN}$: $W = P + \frac{1}{2} R_{NN} \implies R_{NN} = 2W - 2P = 2W - 2l_2 - 2h_2 - 6h_3$ (equation 3).
   - Substituting into (1):
     $$8 = l_1 + 2l_2 + 2h_2 + 4h_3 + [2W - 2l_2 - 2h_2 - 6h_3] + R_{NZ}$$
     $$8 = 2W + l_1 - 2h_3 + R_{NZ}\tag{4}$$
   - The terms $2l_2$ and $2h_2$ cancel completely and rigorously.

#### (2) Bounds $1 \le W \le 6$ and $2W + K \le 12$
- Since $h_3 \le 2$ (from $4h_3 \le 8$ in (1)) and $K \le R_{NZ}$:
  $$2W + K \le 2W + R_{NZ} + l_1 = 8 + 2h_3 \le 8 + 2(2) = 12\tag{5}$$
- In particular $2W \le 12 \implies W \le 6$.
- $W = 0$ was excluded in [`heavy_cross_repeat_slack_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md), giving $1 \le W \le 6$.

#### (3) Adversarial Verification of $W = 5$: Doubled-Edge Triangle Exclusion
1. **Parameter Constraints at $W = 5$**:
   - (4) gives $8 = 10 + l_1 - 2h_3 + R_{NZ} \implies 2h_3 = 2 + l_1 + R_{NZ} \ge 2 \implies h_3 \ge 1$.
   - But $W \ge 3h_3 \implies 5 \ge 3h_3 \implies h_3 \le 1$.
   - Thus $h_3 = 1$ uniquely, forcing $l_1 = R_{NZ} = K = 0$.
   - Unique heavy pair counted by $h_3$ forms a repeat triangle in $N$, consuming 3 units of $W$. Exactly 2 units remain.
2. **Fourth-Trace Filter**:
   - $s = 506 + 2F + 2K = 506 + 2F$, where $F = \sum_{\{u, v\} \subseteq N, u \not\sim v} B_{uv}(B_{uv} - 1)$.
   - $8C_4 = 776 + 2F \implies 2F \equiv 0 \pmod 8 \implies F \equiv 0 \pmod 4$.
   - Distributing the 2 remaining units:
     - Two distinct edges of the triangle doubled: $B = 2, 2, 1 \implies F = 2(1) + 2(1) = 4 \equiv 0 \pmod 4$.
     - Two distinct unit edges outside the triangle: $F = 0 \equiv 0 \pmod 4$.
     - All other distributions give $F = 2$ or $F = 6$, failing the fourth trace.
3. **Exclusion of the Doubled Triangle ($B_{uv} = B_{uw} = 2, B_{vw} = 1$)**:
   - **Accounting for Isolated Zero Repeats**: The paper does **not** assume zero repeats are paired.
     - Root $u$ uses all 4 nonedge units on $v, w$, so $u$ has no zero repeats.
     - Roots $v, w$ each use 3 units in $N$, leaving exactly one unit zero repeat, $x_v$ and $x_w$. Being singletons, they are necessarily **isolated** in zero support.
     - Support transport at $x_v$: $\sum_{y \sim x_v} B_{vy} = B_{vx_v} = 1$.
     - Because $R_{NZ} = 0$, $x_v$ has no nonzero common neighbor with $v$. This forbids $x_v$ from being adjacent to triangle partners of $v$.
     - However, $x_v$ **can be adjacent to nonedge repeat endpoints**! The positive nonedge repeats of $v$ are $u$ (weight 2) and $w$ (weight 1).
     - Since total weight is 1, $x_v$ cannot be adjacent to $u$ (weight 2). Thus $x_v \sim w$ and $x_v \not\sim u$. Similarly $x_w \sim v$ and $x_w \not\sim u$.
   - **$AB = BA$ Expansion at $(u, v)$**:
     - $(AB)_{uv} = \sum_y A_{uy} B_{yv}$. Neighbors of $u$ in positive support of $B_v$: triangle partners of $v$ (count $q_{uv}$). (Vertices $w, x_v$ are nonadjacent to $u$). Thus $(AB)_{uv} = q_{uv}$.
     - $(BA)_{uv} = \sum_y B_{uy} A_{yv}$. Positive support of $B_u$ is triangle partners of $u$ (adjacent to $v$ count $p_{uv}$), plus $v, w$. Thus $(BA)_{uv} = p_{uv}$.
     - Hence $p_{uv} = q_{uv}$. Since triangles are disjoint, $p_{uv} + q_{uv} \le 1 \implies p_{uv} = q_{uv} = 0$.
   - **Fifth-Trace Calculation**:
     - At $u$: $Q_2(u) = 1$, row squares $= 10 \implies e_u = 1 - 10 + 5 = -4$.
     - At $v$: nonzero support edge is triangle edge (weight 1) plus $x_v w$ (weights $1 \times 1 = 1$). Thus $Q_2(v) = 1 + 1 = 2$. Row squares $= 1^2 + 1^2 + 2^2 + 1^2 + 1^2 = 8 \implies e_v = 2 - 8 + 5 = -1$. Similarly $e_w = -1$.
     - Remaining 18 roots: $e_n = 2$.
     - Total $\sum_{n \in N} e_n = -4 - 1 - 1 + 18(2) = 30$.
     - Congruence: $\sum e_n + T = 30 + 7 = 37 \equiv 2 \pmod 5 \ne 4$.
     - Contradiction! The doubled-edge triangle is completely eliminated.
   - For $W = 5$, the repeat graph on $N$ consists strictly of **one unit triangle and two disjoint unit edges**.

#### (4) Adversarial Verification of $W = 6$: Forced Isolated Light Supports
- $W = 6$ forces $h_3 = 2, l_1 = R_{NZ} = K = R_{NN} = 0, P = 6$.
- Defect graph on $N$ consists of two unit triangles sharing at most one vertex.
- **Subcase 4.1 (Disjoint Triangles)**:
  - Remainder sum $\sum e_n = 36 + q$, where $q$ counts active roots (having isolated light zero repeats).
  - Fifth trace gives $36 + q + 7 \equiv 4 \pmod 5 \implies q \equiv 1 \pmod 5$.
  - For repeat edge $vw$, $(AB)_{vw} = (BA)_{vw}$ forces $j_{vw} = j_{wv}$, so active count per triangle cannot be 1.
  - Across two triangles, $q \in \{0, 2, 3, 4, 5, 6\}$. Only $q = 6$ satisfies $q \equiv 1 \pmod 5$.
  - Thus **all 6 vertices are active**, and $j_{vw} = 1$ on all repeat edges.
- **Subcase 4.2 (Triangles Sharing One Vertex $u$)**:
  - Center $u$ has repeat degree 4 and no zero repeats. Outer vertices have repeat degree 2.
  - Matching edges between outer pairs: count $c_0 \in \{0, 1, 2\}$.
  - Active outer roots: count $q$. Remainder sum gives $c_0 + q \equiv 1 \pmod 5$.
  - $(AB)_{au} = (BA)_{au}$ forces $j_{au} = c_a$.
  - Commutation on outer repeat edge gives $2\epsilon_a - c_a = 2\epsilon_b - c_b$, which forces $c_a = c_b$ and $\epsilon_a = \epsilon_b$.
  - Thus $c_0 \ne 1$. If $c_0 = 0$, $q \in \{0, 2, 4\} \not\equiv 1 \pmod 5$.
  - Hence **$c_0 = 2$ and $q = 4$ uniquely**.
  - All four outer roots are active, with exactly two matching edges between opposite pairs.

---

### 3. Lean Formalization Review: `N59Capacity.lean`

- **Source Files**: [`formal/DegreeDiameter/N59Capacity.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean), [`formal/ReviewN59Capacity.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN59Capacity.lean)
- **Verified Log**: [`formal/logs/n59-capacity-global-second.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n59-capacity-global-second.log) (1793 jobs built cleanly).
- **Axiomatic Audit**: [`formal/logs/n59-capacity-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n59-capacity-type-axiom-audit.log).
  - Main theorem: [`n59_nonzero_triangle_vertices_at_least_twenty`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L380-L402)
  - Transitive axioms: strictly `[propext, Classical.choice, Quot.sound]`.
  - Zero `sorry`, zero extra axioms, zero supplied certificate matrices.

#### Back-Translation of Declarations
1. [`nonedgeVertices`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L10-L11):
   `fun {V} [Fintype V] G n => {y | y ≠ n ∧ ¬G.Adj n y}` — vertices outside closed neighborhood $N_G[n]$.
2. [`nonedgeDefectBudget`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L14-L15):
   `∑ y ∈ nonedgeVertices G n, defectMatrix G n y` — sum of defect entries outside $N_G[n]$.
3. [`heavyZeroRepeats`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L18-L19):
   `{y | zeroTriangleVertex G y ∧ defectMatrix G n y = 2}` — zero-triangle vertices with defect 2 from $n$.
4. [`orderedHeavyZeroPairs`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L139-L141):
   `{p ∈ (zeroNeighbors G n).offDiag | defectMatrix G p.1 p.2 = 2}` — ordered pairs of adjacent zero neighbors with defect 2.
5. [`globalHeavyZeroPairs`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L288-L291):
   `{p ∈ zeroTriangleVertices G ×ˢ zeroTriangleVertices G | defectMatrix G p.1 p.2 = 2}` — all ordered heavy pairs with both endpoints zero.
6. [`n59_nonzero_local_heavy_capacity`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L263-L268):
   ```lean
   theorem n59_nonzero_local_heavy_capacity (G : SimpleGraph V)
       (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
       (hcard : Fintype.card V = 59)
       (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z)
       {n : V} (hn : ¬ zeroTriangleVertex G n) :
       ((orderedHeavyZeroPairs G n).card : ℤ) + ((heavyZeroRepeats G n).card : ℤ) ≤ 4
   ```
7. [`n59_nonzero_triangle_vertices_at_least_twenty`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L380-L384):
   ```lean
   theorem n59_nonzero_triangle_vertices_at_least_twenty (G : SimpleGraph V)
       (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
       (hcard : Fintype.card V = 59)
       (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z) :
       20 ≤ (nonzeroTriangleVertices G).card
   ```

#### Distinction: Compiled Lean Theorem vs. Paper Inequalities
- **Compiled in Lean**:
  - The theorem `n59_nonzero_triangle_vertices_at_least_twenty` proves $20 \le m$ directly from:
    $$\sum_{n \in N} (|(\text{orderedHeavyZeroPairs } n)| + |(\text{heavyZeroRepeats } n)|) \le 4m$$
    combined with the degree identity $2|Z| \le 4m \implies 2(59 - m) \le 4m \implies 118 \le 6m \implies m \ge 20$.
  - It uses only the uniform nonedge budget bound $\le 4$ on nonzero vertices.
- **Paper Theorem (Pending Lean Compilation)**:
  - The refined inequality $59 \le 4m - 3T$ and the deduction $T \ge 7$ track the individual triangle counts $2t(n)$ across $N$, yielding $6m - 6T$ instead of $4m$.
  - This tighter relation and its $T \ge 7$ corollary remain currently in verified paper status, distinct from the compiled $m \ge 20$ lemma.

---

### 4. Summary Table of Project Status (Orders 58–62)

| Problem Domain | Proposition / Subcase | Status | Scope & Boundary |
| :--- | :--- | :--- | :--- |
| **Order 59 ($n=59$)** | Nonzero repeat budget identity $8 = 2W + l_1 - 2h_3 + R_{NZ}$ | **Proved** | Exact algebraic slack relation |
| **Order 59 ($n=59$)** | Bound $1 \le W \le 6$ and $2W + K \le 12$ | **Proved** | General for $T=7, m=21$ |
| **Order 59 ($n=59$)** | $W = 5$ doubled-edge triangle exclusion | **Proved** | Eliminated via trace congruence; leaves unit edges |
| **Order 59 ($n=59$)** | $W = 6$ forced isolated light zero supports | **Proved** | Isolated light repeats accounted for without pairing assumption |
| **Order 59 ($n=59$)** | $m \ge 20$ lower bound | **Fully Verified in Lean** | [`N59Capacity.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59Capacity.lean#L380) (standard axioms only) |
| **Order 59 ($n=59$)** | Global capacity $59 \le 4m - 3T$ & $T \ge 7$ | **Proved** (paper) | Formal Lean assembly pending |
| **Order 59 ($n=59$)** | $T=7, m=21$ surviving branches ($1 \le W \le 4$ or restricted $W=5,6$) | **Open** | Constrained necessary forms, not yet excluded |
| **Order 62 ($n=62$)** | Template `S_TOUCH` exclusion | **Proved** | Excluded via saturated rows 0, 1, 2 |
| **Order 58 (Brown57)** | Extensions of Brown57 | **Proved** | Requires $\ge 10$ deletions |
| **Exact Goal** | Determination of $N(8,2)$ | **Open** | Certified baseline interval remains $[57, 62]$ |

