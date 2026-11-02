# Gemini B19 — component sizes and actual D0/parity sources

### 1. Inspection and Execution Record

- **Files Read in Full**:
  1. [`proofs/dd82/n62/D1_COMPONENT_MINIMUM_SIZES.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_COMPONENT_MINIMUM_SIZES.md)
  2. [`proofs/dd82/n62/D1_TWELVE_COMPONENT_EXTERIOR_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_COMPONENT_EXTERIOR_EXCLUSION.md)
  3. [`proofs/dd82/n62/D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md)
  4. [`computations/dd82/n62/component_exterior_separators_check.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_exterior_separators_check.json)
  5. [`proofs/dd82/n62/D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md)
  6. [`formal/DegreeDiameter/N62D0Components.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62D0Components.lean)
  7. [`formal/ReviewN62D0Components.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62D0Components.lean)
  8. [`formal/logs/n62-d0-components-final-build.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-d0-components-final-build.log)
  9. [`formal/logs/n62-d0-components-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-d0-components-type-axiom-audit.log)
  10. [`formal/DegreeDiameter/N62DoubleParity.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62DoubleParity.lean)
  11. [`formal/ReviewN62DoubleParity.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62DoubleParity.lean)
  12. [`formal/logs/n62-double-parity-full-third.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-double-parity-full-third.log)
  13. [`formal/logs/n62-double-parity-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-double-parity-type-axiom-audit.log)
  14. [`formal/N62_D0_COMPONENTS_HANDOFF.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/N62_D0_COMPONENTS_HANDOFF.md)
- **Commands Executed**: **Zero**. No compiler commands, shell executions, Lake builds, or Python scripts were run by the reviewer. All evidence was inspected as read-only static files.
- **Model and Effort Metadata**: Requested `gemini-3.8-flash-high` / reasoning effort `high`.
- **Baseline Alignment**: Known orders 63–65 work remains stopped. The classical upper bound of 62 is a cited mathematical baseline; the master theorem compiled in Lean remains `original_graph_card_le_63`.

---

### 2. Adversarial Review of `D1_COMPONENT_MINIMUM_SIZES.md`

#### A. Mathematical Verification
1. **Common-Neighbor Budget Equation**:
   - Double counting common neighbors of pairs inside component $C_i$ gives:
     $$\sum_j n_j \binom{r_{ji}}{2} = \binom{n_i}{2} + \frac{3n_i}{2} - \frac{n_i r_{ii}}{2} = \frac{n_i(n_i + 2 - r_{ii})}{2}.$$
   - By balance $n_j r_{ji} = n_i r_{ij}$, this simplifies to equation (3):
     $$\sum_j r_{ij}(r_{ji} - 1) = n_i + 2 - r_{ii}.$$
   - Every off-diagonal term $r_{ij}(r_{ji} - 1) \ge 0$ since $r_{ij} > 0 \implies r_{ji} \ge 1$.
   - The diagonal term is $r_{ii}(r_{ii} - 1)$.
   - Hence $n_i \ge r_{ii}^2 - 2$. If $H = K$, then $r_{HH} \ge 4$ implies $h \ge 14$.
   - If $H \ne K$, then $a(b - 1) \le h + 2 - r_{HH}$ and $b(a - 1) \le k + 2 - r_{KK}$.
2. **Lower Bound $h \ge 8$ and Exclusion of $h = 8, 10$**:
   - Distinct endpoints $0, w, a, r, p, q \in H$ with $B_{ar} = B_{pq} = 0$ force $h \ge 8$.
   - If $h = 8$: $a(b - 1) \le 10$ with $a \ge 4, b \ge 3$ forces $b = 3, a \in \{4, 5\}$, but $k = 8a/3 \notin \mathbb{Z}$. Excluded.
   - If $h = 10$: $a(b - 1) \le 12$ leaves $(k, a, b) \in \{(10, 4, 4), (20, 6, 3)\}$, both forcing $r_{HH} = 0$.
     - $(10, 4, 4)$: Common neighbors of the 100 cross-pairs total 60, but each of the 42 exterior vertices contributes at most 1, giving $60 \le 42$. Contradiction.
     - $(20, 6, 3)$: Degrees force $e(Y, K) = 40(t - 1)$, but common neighbors to each $y \in Y$ force $12 \le e(Y, K) \le 36$, which has no multiple of 40. Contradiction.
   - Thus $h \ge 12$.
3. **Lower Bound $k \ge 12$**:
   - If $k \le 10$, $h(a^2 - k) \le k(a + 2)$. For $a \ge 4, k \le 10$, $a^2 - k \ge a + 2$, forcing $h \le k \le 10$, contradicting $h \ge 12$. Thus $k \ge 12$.
4. **Analysis of $k = 12$**:
   - $b(a - 1) \le 14$ forces $h = k = 12, a = b = 4$, with $\alpha, \beta \in \{0, 1\}$.
   - Cross-moment $\sum x_v y_v = 96 - 48(\alpha + \beta)$ rules out $\alpha = \beta = 0$ (gives $72 \ge 96$) and $\alpha = \beta = 1$ (gives disjoint supports, but each has size $\ge 30 > 38/2$).
   - Thus $\{\alpha, \beta\} = \{0, 1\}$.
5. **Surviving $h = 12$ Triples**:
   - Leaves exactly five candidate triples $(k, a, b)$:
     $$(12, 4, 4), \quad (16, 4, 3), \quad (20, 5, 3), \quad (24, 6, 3), \quad (28, 7, 3).$$

**Verdict**: Rigorous and fully verified.

---

### 3. Adversarial Review of `D1_TWELVE_COMPONENT_EXTERIOR_EXCLUSION.md`

#### A. Mathematical Verification
1. **Exterior Moments and Coordinates**:
   - For $(h, k, a, b) = (12, 12, 4, 4)$ with internal degrees $\alpha = 0, \beta = 1$:
     Exterior vertex count is $N = 38$. Moments:
     $$\sum 1 = 38, \quad \sum x_v = 48, \quad \sum y_v = 36, \quad \sum x_v(x_v - 1) = 24, \quad \sum y_v(y_v - 1) = 12, \quad \sum x_v y_v = 48.$$
   - Pointwise bounds $x_v + 4y_v \le 12$ and $4x_v + 2y_v \le 12$ restrict $x_v, y_v \in \{0, 1, 2\}$.
2. **Component Equitability and Lower Bound on Type Counts**:
   - Every component of $B$ has even size $\ge 4$ ($n_i = 2$ would force an off-diagonal entry 3, excluded by $B \le 2$).
   - Because $(x_v, y_v)$ are equitable neighbor counts, they are constant on each component of $B$.
   - Thus each exterior type count $n_{ij}$ satisfies:
     $$n_{ij} \in \{0\} \cup \{4, 6, 8, \dots\}.$$
3. **The Six Vertices with $y_v = 2$**:
   - Factorial moment $\sum y_v(y_v - 1) = 12 \implies 2(n_{02} + n_{12} + n_{22}) = 12 \implies n_{02} + n_{12} + n_{22} = 6$.
   - Since each $n_{ij}$ is 0 or $\ge 4$, exactly one of them is 6, and the other two are 0.
4. **Exhaustion of All Three Subcases**:
   - **Subcase $n_{22} = 6$**: Moment equations force $n_{21} + n_{00} = 2$. Impossible because each is 0 or $\ge 4$.
   - **Subcase $n_{12} = 6$**: Nonnegativity forces $n_{21} = 12$, which leaves $n_{00} = 2$. Impossible ($2 < 4$).
   - **Subcase $n_{02} = 6$**: Requires $n_{21} \le 12$ and $n_{21} \ge 24$. Impossible.

**Verdict**: The configuration $(12, 12, 4, 4)$ is unconditionally excluded. Consequently, any generated-triangle component $K$ has:
$$\boxed{|K| \ge 14}.$$

---

### 4. Adversarial Review of Exterior Refinements and Partner Exclusions

#### A. Moment Refinement (`D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md`)
- Replaces floating LP bounds with **21 exact integer separating vectors** $z \in \mathbb{Z}^6$.
- For each case, $z \cdot \phi(x, y) \ge 0$ holds at all 334 admissible integer points in the domain, but $z \cdot M < 0$.
- Verified by [`component_exterior_separators_check.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_exterior_separators_check.json): 21 integer separators check out across all 33 cases, leaving 12 candidate tuples.

#### B. Two Large Partner Exclusions (`D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md`)
1. **Case $(h, k, a, b, s, t) = (12, 20, 5, 3, 1, 2)$**:
   - Moments force type distribution $(2, 0): 6, (3, 0): 4, (0, 3): 20$.
   - Identity $(A d_K)(v) + d_K(v) = |K| = 20$.
   - For $v \in X$, $d_K(v) = 0$, giving $5x_v + 3|N(v) \cap Y| = 20$.
   - With $x_v \in \{2, 3\}$, $20 - 5x_v \in \{10, 5\}$, neither divisible by 3. **Excluded**.
2. **Case $(h, k, a, b, s, t) = (12, 24, 6, 3, 0, 2)$**:
   - Moments force type distribution $(2, 3): 12, (0, 3): 4, (0, 4): 6, (0, 0): 4$.
   - Identity $(A d_H)(v) + d_H(v) = |H| = 12$.
   - For $v$ of type $(0, 3)$, $d_H(v) = 0$, giving $3 \times 3 + 2|N(v) \cap X| = 12 \implies 2|N(v) \cap X| = 3$.
   - Contradiction by parity. **Excluded**.

#### C. Remaining Scope for $h = 12$
Combining the $(12, 12)$ exclusion, the 21 integer separators, and these 2 partner exclusions, only **8 tuples** survive for $h = 12$:
- $(k, a, b) = (16, 4, 3)$ with $(s, t) \in \{(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 0), (2, 1)\}$.
- $(k, a, b, s, t) = (20, 5, 3, 0, 2)$.

Cases with $h \ge 14$ and $H = K \ge 14$ remain open.

---

### 5. Independent Back-Translation of Lean Formalizations

#### A. `formal/DegreeDiameter/N62D0Components.lean`
- **Structures and Definitions**:
  - `D0ParentTemplate`: Strictly graph-theoretic parent conditions for D0 (root $r$, independent neighborhood, parents $i, j, k$ for $w$, parents $b, d$ for $a$).
  - `D0EdgeBoutTemplate`: Extends `D0ParentTemplate` with $w \sim a$, root-neighbor $b$ outside the parents, and two common neighbors of $w, b$.
  - `ClosedDoubleFour G r w b a`: Specifies four saturated rows ($B_r = 2e_w + e_a$, $B_w = 2e_r + e_b$, $B_a = 2e_b + e_r$, $B_b = 2e_a + e_w$).
- **Theorems Verified**:
  - `n62_d0_match_closed_component`: From `D0ParentTemplate` and $w \not\sim a$, derives `ClosedDoubleFour` and all 6 nonedges among $\{r, w, b, a\}$ in $G$.
  - `n62_d0_bout_closed_component`: From `D0EdgeBoutTemplate`, derives `ClosedDoubleFour` and exactly edges $rb$ and $wa$ in $G$.
  - `bout_common_neighbors_of_unit_repeat`: Connects $B_{wb} = 1$ to the `D0EdgeBoutTemplate` witness.
  - `closedDoubleFour_no_external_repeat`: Confirms no repeat edges leave the 4 vertices.
- **Axioms and Build**:
  - Audit log [`n62-d0-components-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-d0-components-type-axiom-audit.log): strictly `[propext, Classical.choice, Quot.sound]`.
  - Build log [`n62-d0-components-final-build.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-d0-components-final-build.log): clean build in 13s (1798 jobs).

#### B. `formal/DegreeDiameter/N62DoubleParity.lean`
- **Four-Cycle Flag Involution and Odd Double-Edge Parity**:
  - Defines `fourCycleFlags G` as pairs $(P, Q)$ where $P$ is an unordered nonedge and $Q \in \binom{CN(P)}{2}$.
  - `n62_four_cycle_flags_even`: Swapping $(P, Q) \leftrightarrow (Q, P)$ is a fixed-point-free involution, proving $|fourCycleFlags|$ is even.
  - `n62_four_cycle_flag_incidence`:
    $$|fourCycleFlags| = |unitNonedgePairs| + 3 |doubleNonedgePairs|.$$
  - `n62_double_repeat_incidence`:
    $$2 |unitNonedgePairs| + 4 |doubleNonedgePairs| + 6 |cliqueFinset 3| = 186.$$
  - `n62_double_repeat_pairs_eq_nonedge_pairs`: Proves all double repeats are nonedges.
  - Main Theorem `n62_double_repeat_pair_count_odd`:
    ```lean
    theorem n62_double_repeat_pair_count_odd (G : SimpleGraph V)
        (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
        (hcard : Fintype.card V = 62) (hbound : ∀ x y, defectMatrix G x y ≤ 2) :
        Odd (doubleRepeatPairs G).card
    ```
- **Axioms and Build**:
  - Audit log [`n62-double-parity-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-double-parity-type-axiom-audit.log): strictly `[propext, Classical.choice, Quot.sound]`.
  - Build log [`n62-double-parity-full-third.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-double-parity-full-third.log): clean build in 9.8s (1802 jobs).

---

### 6. Summary Status Table (Order-62 Candidates and Formal Proofs)

| Component / Result | Mathematical Status | Formal Status | Scope & Boundary |
| :--- | :--- | :--- | :--- |
| **Simple Defect ($B \le 1$)** | Excluded | **Compiled in Lean** ([`N62SimpleExclusion.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62SimpleExclusion.lean#L209)) | Excludes `S_TOUCH` & `S_DISJOINT` |
| **`D2_MATCH` Template** | Excluded | **Compiled in Lean** ([`N62D2.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62D2.lean#L648)) | Excluded |
| **`D0_EDGE_BIN` Template** | Excluded | **Compiled in Lean** ([`N62D0Bin.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62D0Bin.lean#L285)) | Excluded |
| **`D0` Component Isolation** | Closed $B_4$ components | **Compiled in Lean** ([`N62D0Components.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62D0Components.lean#L462)) | Saturated rows, zero exterior defect |
| **Global Double-Edge Parity** | Total double edges odd | **Compiled in Lean** ([`N62DoubleParity.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62DoubleParity.lean#L464)) | Conditional on $B \le 2$ |
| **D1 Component Bounds** | $h \ge 12, k \ge 14$ | **Proved** (paper) | Excludes $(12, 12, 4, 4)$ |
| **D1 $h = 12$ Remaining List** | 8 candidate tuples | **Proved** (paper) | 21 integer separators checked, 2 cases excluded |
| **`D1_MATCH` Status** | Active research | **Open** | $h \ge 12, k \ge 14$ or $H = K \ge 14$ remain |
| **Overall Master Lean Bound** | Order $\le 63$ | **Compiled in Lean** (`Moore64.lean`) | Certified 63; classical 62 is cited baseline |


## Executor disposition

B19 correctly read the repaired first-case equation 20=5x+3d_Y and accepted it. The separate fresh blind receipt also passed all three local partner exclusions; the prior critical coefficient error and its repair remain recorded. The minimum-size and twelve-by-twelve papers passed independent PASS24/PASS12; finite inequalities passed PASS10 with the exact checker rerun.

B19's full-read list includes the finite-check output but does not list the checker source or discovery JSON, so it is not recorded as an independent full code audit. Its 334 evaluations are case-specific domain checks, not one domain on which every separator is valid. The statement that pointwise bounds alone force x,y≤2 in the twelve-by-twelve proof is compressed incorrectly: the source additionally uses moments and minimum nonempty type sizes to exclude coordinate3. The reviewed source supplies that step. “Unconditionally excluded” is read within the actual graph and imported triple-repeat-exclusion hypotheses, not as a new Lean upper bound.

D0 and double-parity actual Lean sources are accepted within their caller scopes, standard axioms, with zero reviewer executions. Dependency job totals are not CPU parallelism (executor≤3threads). N62DoubleRoot/N62D1Outlet were completed after this batch's source list and still require their own source review. The newer twenty-zero-two paper and size-sixteen paper were not part of B19. No global order62 or exact N(8,2) claim follows. Model metadata is CLI selected, not independently attested.

