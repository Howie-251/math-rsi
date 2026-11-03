# B26 — heavy original graph and actual quotient trace

### Review Metadata and Execution Scope

- **CLI-selected model & reasoning effort**: `gemini-3.8-flash-high` / `high` (preserves requested CLI configuration; distinct from any unverified backend attestation).
- **Execution disclosure**: **0 executions performed by the reviewer.** No shell commands, compilation commands, or test scripts were run. All referenced build outputs and type/axiom logs pre-existed in the workspace.
- **Reading scope**:
  - **Read in full**:
    - [`proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md) (all 308 lines, Sections 1–6).
    - [`formal/DegreeDiameter/N62RepeatQuotientTrace.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62RepeatQuotientTrace.lean) (all 176 lines).
    - [`formal/ReviewN62RepeatQuotientTrace.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62RepeatQuotientTrace.lean) (all 37 lines).
    - [`formal/N62_REPEAT_QUOTIENT_TRACE_HANDOFF.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/N62_REPEAT_QUOTIENT_TRACE_HANDOFF.md) (all 32 lines).
    - [`formal/logs/n62-repeat-quotient-trace-third.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-quotient-trace-third.log) (all 3 lines).
    - [`formal/logs/n62-repeat-quotient-trace-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-quotient-trace-type-axiom-audit.log) (all 53 lines).
  - **Contextual cross-references consulted**:
    - [`proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md) (Section 3, to verify distinction between the unit-mate multigraph and the base simple graph $F$).
    - [`reviews/dd82/proof-checker-n62-heavy-original-20261011/`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/reviews/dd82/proof-checker-n62-heavy-original-20261011/) (treated strictly as same-family provisional context).

---

### Part 1: Source Review of `CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md`

#### 1. Mate Involution from Even/Binary Parity ($AB=BA$)
- In an actual legal order-62 graph $G$, the repeat matrix satisfies $AB=BA$. On the set $D$ of $2d$ heavy vertices, each $x \in D$ has $B_x = 2e_{h(x)} + e_{a(x)}$ where $h(x) \in D$ is its heavy mate and $a(x) \in L$ is its light mate.
- Expanding $(AB)_{xy} = (BA)_{xy}$ for $x, y \in D$:
  $$2 A_{x, h(y)} + A_{x, a(y)} = 2 A_{h(x), y} + A_{a(x), y} \implies 2\big(A_{x, h(y)} - A_{h(x), y}\big) = A_{a(x), y} - A_{x, a(y)}.$$
- The LHS lies in $2\mathbb{Z}$. Since $A$ is a binary adjacency matrix, the RHS lies in $\{-1, 0, 1\}$.
- The only integer in $2\mathbb{Z} \cap \{-1, 0, 1\}$ is $0$. Hence:
  $$A_{x, h(y)} = A_{h(x), y} \quad\text{and}\quad A_{x, a(y)} = A_{a(x), y} = A_{y, a(x)}.$$
- Because $h$ is a fixed-point-free involution ($h(h(x)) = x$), substituting $h(x)$ for $x$ yields $A_{h(x), h(y)} = A_{xy}$.
- **Verdict**: Fully sound. The heavy-mate swap $h$ is an exact, fixed-point-free graph automorphism of the induced subgraph $G[D]$.

#### 2. Actual Two-Fold Lift and Definition of Base Graph $F$
- Partition $D$ into $d$ pairs $D_i = \{u_i, h(u_i)\}$ ($i = 1, \dots, d$).
- Adjacent vertices in $G$ have $B_{uv} = 0$, but mates have $B_{u_i, h(u_i)} = 2 > 0$. Hence no edge in $G[D]$ joins $u_i$ to $h(u_i)$.
- For $i \ne j$, the $2 \times 2$ block $A[D_i, D_j]$ commutes with the permutation $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, restricting it to:
  1. All-zeros $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ (0 edges);
  2. Direct matching $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ (2 edges: $u_i \sim u_j$, $h(u_i) \sim h(u_j)$);
  3. Cross matching $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ (2 edges: $u_i \sim h(u_j)$, $h(u_i) \sim u_j$);
  4. All-ones $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ (4 edges).
- If the all-ones block occurred, $u_j \in D$ would be adjacent to both $u_i$ and $h(u_i)$. But the only common neighbors of a heavy pair $\{u_i, h(u_i)\}$ in $G$ are the 3 vertices of their generated triangle, which lie entirely in $L$ (outside $D$). Hence the all-ones block cannot occur.
- Thus, between distinct pairs $D_i$ and $D_j$, there are either 0 edges or exactly 2 edges (a matching of size 2).
- **Distinction from earlier multigraph**:
  - Base graph $F$: a **simple graph** on the $d$ heavy pairs $\{1, \dots, d\}$, where $ij \in E(F)$ iff there are 2 edges between $D_i$ and $D_j$. Total edges in $G[D]$ is $2m$, where $m = |E(F)|$.
  - Unit-mate port multigraph in `CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md`: defined on the light mates $a(u_i)$ tracking incidences into unit triangles, which allowed parallel edges. The two graphs are distinct.

#### 3. Girth and Degree Constraints in $G[D]$ and $F$
- $G$ is triangle-free, so $G[D]$ contains no $C_3$.
- Any two non-mate vertices in $G$ have at most 1 common neighbor. Mates have common neighbors only in their generated triangle in $L$. Hence no two vertices in $D$ share 2 or more neighbors in $D$. This immediately rules out $C_4$ in $G[D]$.
- Maximum degree: At a heavy root $u$, its 8 neighbors in $G$ comprise 3 vertices in its generated triangle, 1 neighbor whose row is $e_1 + e_f + e_g$ (which has heavy component 0 and hence lies outside $D$), and at most 4 remaining neighbors. Thus $\deg_{G[D]}(v) \le 4$, so $\Delta(F) \le 4$.

#### 4. Squared-Degree Bound and Signed Adjacency Matrix
- Since $G[D]$ is $C_3$-free and $C_4$-free, every vertex $v \in D$ determines $\binom{\deg(v)}{2}$ disjoint 2-paths whose endpoints are non-adjacent and not mates.
- Counting distinct non-adjacent non-mate pairs in $D$:
  $$\sum_{v \in D} \binom{\deg_{G[D]}(v)}{2} \le \binom{2d}{2} - |E(G[D])| - d = 2d(d-1) - 2m.$$
  Since $\sum_{v \in D} \deg_{G[D]}(v) = 4m$, this rearranges to:
  $$\sum_{i=1}^d r_i^2 \le 2d(d-1), \quad\text{where } r_i = \deg_F(i).$$
- At equality, every non-mate non-adjacent pair has a unique common neighbor in $D$. Decomposing under the eigenspaces of the mate involution $H$:
  - On the symmetric subspace ($H = +I$), $J$ acts non-trivially.
  - On the antisymmetric subspace ($H = -I$), $J$ vanishes ($J(u - h(u)) = 0$), and the signed adjacency matrix $Z$ of $F$ (with $Z_{ij} = \pm 1$ according to whether the lift is direct or cross) satisfies:
    $$Z^2 + Z = \operatorname{diag}(r_1, \dots, r_d).$$
- Because $Z$ is symmetric, $Z \operatorname{diag}(r) = Z(Z^2 + Z) = (Z^2 + Z)Z = \operatorname{diag}(r) Z$. Commuting with a diagonal matrix forces $Z$ to be block-diagonal according to the values of $r_i$, proving that **every connected component of $F$ is regular** at equality.

#### 5. Numerical Edge Bounds $m = |E(F)|$
- $d=1$: $m=0$.
- $d=3$: $r_i \le 2 \implies m \le 3$.
- $d=5$: $\sum r_i^2 \le 40$. Cauchy-Schwarz gives $4m^2 \le 5(40) = 200 \implies m \le 7$.
  If $m=7$, the only degree sequence with $\Delta \le 4$ and $\sum r_i^2 \le 40$ is $\{3, 3, 3, 3, 2\}$ with $\sum r_i^2 = 40$. But equality requires regularity, which contradicts the mixed degrees $\{3, 2\}$. Hence $m \le 6$.
- $d=7$: $\sum r_i^2 \le 84$. Cauchy-Schwarz gives $4m^2 \le 7(84) = 588 \implies m \le 12$.
  If $m=12$, the unique degree sequence with $\Delta \le 4$ and $\sum r_i^2 \le 84$ is $\{4, 4, 4, 3, 3, 3, 3\}$ with $\sum r_i^2 = 84$. Regularity forces the 3 vertices of degree 4 to form a 4-regular component, which is impossible on 3 vertices ($\Delta \le 2$). Hence $m \le 11$.
- $d=9$: $\sum r_i^2 \le 144$. Cauchy-Schwarz gives $4m^2 \le 9(144) = 1296 \implies m \le 18$.
  If $m=18$, $\sum r_i = 36 \implies r_i = 4$ for all $i$. Equality forces $Z^2 + Z = 4I_9$. The polynomial $\lambda^2 + \lambda - 4 = 0$ has discriminant 17 and is irreducible over $\mathbb{Q}$. Its eigenvalues $\frac{-1 \pm \sqrt{17}}{2}$ must appear with equal multiplicity, forcing the dimension of the space to be even. But the dimension is $d=9$, which is odd! Contradiction. Hence $m \le 17$.
- **Verdict**: The derived upper bounds $m \in \{0, 3, 6, 11, 17\}$ for $d \in \{1, 3, 5, 7, 9\}$ are completely verified.

#### 6. Conditional $\operatorname{diam}(F) \le 2$ Consequences
- If $\operatorname{dist}_F(i, j) \le 2$, then $D_i$ and $D_j$ already have edges or a common neighbor in $D$, forcing $E_G(D_i, S_j) = \emptyset$, where $S_j$ is the generated triangle of pair $j$.
- If $\operatorname{diam}(F) \le 2$, complete separation holds: $E_G(D, S) = \emptyset$ outside the direct generated incidences.
- The remaining degree of $v \in D_i$ into $W = V \setminus (D \cup S)$ is $8 - 3 - r_i = 5 - r_i$.
- Summing gives $|E_G(D, W)| = 10d - 4m$. For $d=9$, $|W| = 17$, $|E_G(D, W)| \ge 90 - 4(17) = 22$, and $e_B(S, W) \ge 19 \implies e_B(W) \le 7$.
- The text explicitly qualifies these bounds as conditional on $\operatorname{diam}(F) \le 2$ without claiming the diameter bound has been proved.

---

### Part 2: Formal Verification of `N62RepeatQuotientTrace.lean`

#### 1. Mathematical Argument in Lean
- **Rank-one size matrix algebra**:
  With $N_{CD} = |D|$, $N^2 = 62N$, $RN = NR = 8N$, and $R^2 + R = 10I + N$.
- **Centered matrix definition**:
  $P = 62(2R + I) - 17N$.
  In `n62_centered_repeat_quotient_cubic`, Lean proves $P^3 = 157604 P$ purely by polynomial simplification in non-commutative matrix algebra (where $157604 = 41 \times 62^2$).
- **Trace formula**:
  $\operatorname{tr}(N) = 62$, $\operatorname{tr}(2R + I) = 2\operatorname{tr}(R) + c$.
  $\operatorname{tr}(P) = 62(c + 2\operatorname{tr} R - 17)$.
- **Finite-field reduction over $\mathbb{F}_{1063}$**:
  In `cubic_157604_trace_mod_1063`:
  - $1063$ is prime (`by decide`).
  - Over $\mathbb{Z}/1063\mathbb{Z}$, $M^3 = 157604 M \implies M^{2k+1} = 157604^k M$.
  - For $k = 531$, $2k+1 = 1063$. The exact scalar power is kernel-checked:
    $$157604^{531} \equiv -1 \pmod{1063} \quad\text{(`by decide`)}.$$
  - Hence $M^{1063} = -M$.
  - By Mathlib's Frobenius trace theorem (`ZMod.trace_pow_card`), $\operatorname{tr}(M^{1063}) = (\operatorname{tr} M)^{1063} = \operatorname{tr} M$.
  - Thus $\operatorname{tr} M = -\operatorname{tr} M \implies 2\operatorname{tr} M = 0 \implies \operatorname{tr} M = 0 \pmod{1063}$.
  - This proves $1063 \mid \operatorname{tr}(P) = 62(c + 2\operatorname{tr} R - 17)$.
  - Since $\gcd(62, 1063) = 1$, $1063 \mid (c + 2\operatorname{tr} R - 17)$.
- **Integer Interval Elimination**:
  - $1 \le c \le 62$, and each row of $R$ has sum 8 with non-negative entries, so $0 \le \operatorname{tr}(R) \le 8c \le 496$.
  - The integer $c + 2\operatorname{tr} R - 17$ is bounded in $[-17, 1037]$.
  - The only multiple of $1063$ in $[-17, 1037]$ is $0$.
  - Proved by `omega`: $c + 2\operatorname{tr} R = 17$, which immediately forces $c$ to be odd.

#### 2. Caller Hypotheses and Transitive Axioms Audit
- **Inspected callers in [`ReviewN62RepeatQuotientTrace.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62RepeatQuotientTrace.lean)**:
  ```lean
  example {V : Type*} [Fintype V] (G : SimpleGraph V)
      (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
      (hcard : Fintype.card V = 62) :
      (Fintype.card (repeatSupport G).ConnectedComponent : ℤ) +
        2 * trace (repeatQuotientMatrix G) = 17 :=
    n62_repeat_quotient_trace_identity G hdeg hdiam hcard

  example {V : Type*} [Fintype V] (G : SimpleGraph V)
      (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
      (hcard : Fintype.card V = 62) :
      Odd (Fintype.card (repeatSupport G).ConnectedComponent) :=
    n62_repeat_component_count_odd G hdeg hdiam hcard
  ```
  The hypotheses require **only** the original finite graph conditions: maximum degree 8, diameter at most 2, and order 62.
- **No external assumptions**:
  - No assumption of $B \le 2$.
  - No pre-assumed quotient equitability or spectral certificate.
  - No connectedness assumption.
- **Transitive Axiom Check**:
  All 8 public declarations (`cubic_157604_trace_mod_1063`, `n62_repeat_size_matrix_square`, `n62_repeat_quotient_size_actions`, `n62_centered_repeat_quotient_cubic`, `n62_repeat_quotient_trace_bounds`, `n62_repeat_component_count_le`, `n62_repeat_quotient_trace_identity`, `n62_repeat_component_count_odd`) depend strictly on the standard Lean 4 axioms:
  `[propext, Classical.choice, Quot.sound]`.
  No `sorry`, no unproven constants, and no non-standard axioms exist.
- **Build & Audit Logs**:
  - [`formal/logs/n62-repeat-quotient-trace-third.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-quotient-trace-third.log): exit 0 (1792 jobs, 16s).
  - [`formal/logs/n62-repeat-quotient-trace-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-quotient-trace-type-axiom-audit.log): exit 0.

---

### Part 3: Explicit Boundaries and Review Verdicts

1. **`CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md`**:
   - **Verdict: PASS (Provable as stated).**
   - The mate involution, two-fold lift, $C_3/C_4$ exclusion, square-degree bound, signed matrix regularity at equality, numerical bounds $m \in \{0, 3, 6, 11, 17\}$, and conditional $\operatorname{diam}(F) \le 2$ consequences are mathematically rigorous.
   - The simple base graph $F$ on $d$ heavy pairs is properly distinguished from the light-mate port multigraph.

2. **`N62RepeatQuotientTrace.lean`**:
   - **Verdict: PASS (Complete and verified).**
   - Derives $c + 2\operatorname{tr} R = 17$ and $c \equiv 1 \pmod 2$ directly from original graph hypotheses via kernel-checked modular arithmetic in $\mathbb{F}_{1063}$ and interval bounding.
   - Fully kernel-checked with standard Lean axioms `[propext, Classical.choice, Quot.sound]`.

3. **Global Scope Invariants**:
   - Neither document asserts connectedness of $B$ in Lean or in the paper.
   - Neither document claims full exclusion of order-62 graphs or the exact value of $N(8,2)$.
   - Known 63–65 results remain stopped and cited only as baseline context.


## Executor disposition and corrections to reviewer prose

The two source results are accepted in their actual stated scope, with the original proof text and local build/audit evidence authoritative. The reviewer performed zero executions and reports CLI selection, not independently attested backend identity. Raw response is preserved above and in JSON.

Several compressed reviewer sentences are inaccurate and are not adopted:
- "Any two non-mate vertices in G have at most 1 common neighbor" is only valid here for nonmate heavy vertices in D. Other unit-repeat nonedges have two common neighbors.
- The generated triangles lie in S, outside D. They do not lie in L when L denotes the set of heavy unit mates: L is outside every unit triangle. The earlier port multigraph has vertices in L and an edge between the two unit mates of each heavy pair; it does not track incidence into unit triangles.
- The values 0,3,6,11,17 are pointwise upper bounds for m at the five d values, not an exact set of possible m values.
- At d=5 equality makes each connected component regular, not necessarily the whole graph. The real contradiction is that the unique degree-two vertex has no other degree-two vertex to neighbor.
- The base-distance separation requires distinct i,j and distance one or two; at i=j the six own generated incidences remain.

These are review-summary scope corrections; the reviewed source already states each fact correctly. No proof-source repair or additional theorem is inferred. Full connectedness formalization and full order62 exclusion remain outstanding.

