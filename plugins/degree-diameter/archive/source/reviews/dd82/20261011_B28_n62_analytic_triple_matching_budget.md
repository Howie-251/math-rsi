# B28 — analytic triple exclusion, actual matching, and component budget

### Review Metadata and Execution Scope

- **CLI-selected model & reasoning effort**: `gemini-3.8-flash-high` / `high` (preserves CLI configuration metadata; distinct from backend attestation).
- **Execution disclosure**: **0 executions performed by the reviewer.** No shell commands, compiler invocations, or test scripts were run. All referenced compilation and type/axiom audit records pre-existed in the workspace.
- **Reading scope**:
  - **Read in full**:
    - [`proofs/dd82/n62/TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md) (all 213 lines).
    - [`proofs/dd82/n62/RECOVERED_REDUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/RECOVERED_REDUCTION.md), Steps 1–3 (lines 42–134).
    - [`formal/DegreeDiameter/N62TripleMatching.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62TripleMatching.lean) (all 280 lines).
    - [`formal/ReviewN62TripleMatching.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62TripleMatching.lean) (all 90 lines).
    - [`formal/N62_TRIPLE_MATCHING_HANDOFF.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/N62_TRIPLE_MATCHING_HANDOFF.md) (all 38 lines).
    - [`formal/logs/n62-triple-matching-second.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-matching-second.log) (all 34 lines).
    - [`formal/logs/n62-triple-matching-type-axiom-audit-final.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-matching-type-axiom-audit-final.log) (all 145 lines).
    - [`formal/DegreeDiameter/N62RepeatComponentBudget.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62RepeatComponentBudget.lean) (all 55 lines).
    - [`formal/ReviewN62RepeatComponentBudget.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62RepeatComponentBudget.lean) (all 31 lines).
    - [`formal/N62_REPEAT_COMPONENT_BUDGET_HANDOFF.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/N62_REPEAT_COMPONENT_BUDGET_HANDOFF.md) (all 35 lines).
    - [`formal/logs/n62-repeat-component-budget-first.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-component-budget-first.log) (all 3 lines).
    - [`formal/logs/n62-repeat-component-budget-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-component-budget-type-axiom-audit.log) (all 21 lines).
  - **Consulted as provisional context**:
    - [`reviews/dd82/proof-checker-n62-triple-analytic-20261011/PROOF_AUDIT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/reviews/dd82/proof-checker-n62-triple-analytic-20261011/PROOF_AUDIT.md) (same-family provisional review).
- **Prose boundary clarifications preserved**:
  1. $D \cup R$ in `CONNECTED_REPEAT_STRICT_TRIANGLE_CAPACITY.md` is a proper $B$-closed set (which may be a union of multiple components, not necessarily a single connected component).
  2. The exact repeat rows of a unit diamond are $B_x = e_y + e_z + e_w$ and $B_y = e_x + e_z + e_w$ (distinct vectors with $x$ and $y$ swapped).

---

### Part A: Review of `TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md`

#### 1. Context and Elimination of Matrix Enumeration
- In `RECOVERED_REDUCTION.md`, Steps 1–3 establish that a hypothetical triple entry $B_{uv} = 3$ decomposes $V(G)$ into five $B$-closed cells $\{u, v\}$, $S$, $E$, $U$, $V$ of sizes $2, 4, 8, 24, 24$.
- The repeat block on $E = E^+ \sqcup E^-$ is $B_E = \begin{pmatrix} 0 & N \\ N & 0 \end{pmatrix}$ where $N$ is symmetric, zero-diagonal, with row sum 3. The opposite-pair weights $(a, b, c)$ must sum to 3:
  - $(3, 0, 0)$ is eliminated directly in Step 3 because type $(0, 2)$ has $Q$ row concentrated with weight 3 at $(3, 1)$, but $(3, 1)$ is its forced $L$-neighbor (contradicting $LQ = 0$).
  - $(2, 1, 0)$ is eliminated directly in Step 3 because type $(0, 3)$ has $Q$-targets $(2, 1)$ and $(1, 2)$, which are both its forced $L$-neighbors.
  - Thus only $N = J_4 - I_4$ survived, which historically required a 24-vertex matrix enumeration (Step 4) and a parity contradiction (Step 5).
- The new paper provides an **entirely analytic replacement** for Steps 4–5.

#### 2. Twin Edges and the Three Actual 8-Point Components
- In $N = J_4 - I_4$, each of the 12 ordered pairs $(p, q)$ ($p \ne q \in \{0, 1, 2, 3\}$) has exactly $|V_{pq}| = 1 + N_{pq} = 2$ vertices in $V$.
- Let $z, \bar{z}$ be the two copies of type $(p, q)$.
  - They both have original neighbors $e_p^+ \in E^+$ and $e_q^- \in E^-$.
  - Therefore, $Q_{z\bar{z}} = |N_G(z) \cap N_G(\bar{z})| + A_{z\bar{z}} - 1 \ge 2 + 0 - 1 = 1$.
  - From $AB=BA$, the marginal equations on $V$ are:
    $$\sum_{z': \operatorname{first}(z')=a} Q_{zz'} = 1 - \delta_{aq}, \qquad \sum_{z': \operatorname{second}(z')=b} Q_{zz'} = 1 - \delta_{bp}.$$
  - For $z \in V_{pq}$, the first-label $p$ marginal is $1 - \delta_{pq} = 1 - 0 = 1$. Since $Q_{z\bar{z}} \ge 1$ and $\bar{z}$ has first label $p$, this forces:
    $$Q_{z\bar{z}} = 1.$$
  - This twin edge completely saturates the first-label $p$ marginal and the second-label $q$ marginal.
  - The remaining 2 repeat neighbors of $z$ must use the complementary labels $\{r, s\} = \{0, 1, 2, 3\} \setminus \{p, q\}$. Since types with equal labels $(r, r)$ do not exist, the remaining two repeat neighbors of $z$ must have types $(r, s)$ and $(s, r)$, exactly one each.
- This immediately partitions the 24 vertices of $V$ into three subsets of 8 vertices:
  $$W_1 = \{01, 10, 23, 32\} \times \{0, 1\}, \quad W_2 = \{02, 20, 13, 31\} \times \{0, 1\}, \quad W_3 = \{03, 30, 12, 21\} \times \{0, 1\}.$$
- **No $Q$-edges leave $W_i$**: from type $pq$, repeat neighbors lie in $\{pq, qp, rs, sr\} \subseteq W_i$.
- **Connectedness of each $W_i$**:
  - The twin edges $Q_{z\bar{z}} = 1$ connect the two copies of every type.
  - The edges between types form a connected $K_{2, 2}$ between $\{pq, qp\}$ and $\{rs, sr\}$.
  - Hence each $W_i$ is a connected subgraph in the positive repeat support.
- Since $V$ is $B$-closed, $W_1, W_2, W_3$ are **three whole connected components of the actual repeat matrix** in $G$.

#### 3. Original Internal Degrees and Trace Contradiction
- In $V$, original neighbors of $(p, q)$ lie in $(r, s)$ and $(s, r)$, which are also in $W_i$. Every vertex in $V$ has original degree 2 into $V$, so its internal degree in $W_i$ is exactly 2.
- Thus $R_{W_i W_i} = 2$ for each $i \in \{1, 2, 3\}$, giving:
  $$\operatorname{tr}(R) \ge R_{W_1 W_1} + R_{W_2 W_2} + R_{W_3 W_3} = 2 + 2 + 2 = 6.$$
- The graph has at least five identified whole components: $\{u, v\}$ (size 2), $S$ (size 4), $W_1$ (size 8), $W_2$ (size 8), $W_3$ (size 8).
  Their total size is $2 + 4 + 8 + 8 + 8 = 30$.
- The remaining $62 - 30 = 32$ vertices ($E \cup U$) are nonempty, so they must contain at least one additional whole component.
  Therefore, the total number of actual repeat components satisfies:
  $$c \ge 5 + 1 = 6.$$
- Applying the quotient trace identity $c + 2\operatorname{tr}R = 17$:
  $$17 = c + 2\operatorname{tr}R \ge 6 + 2(6) = 18,$$
  which is an immediate arithmetic contradiction ($17 \ge 18$).

#### 4. Non-Circularity and Scope Audit
- **No premise $B \le 2$ or $B$-connectedness**: The trace theorem `n62_repeat_quotient_trace_identity` from `formal/DegreeDiameter/N62RepeatQuotientTrace.lean` requires only `degreeAtMostEight G`, `diameterAtMostTwo G`, and `Fintype.card V = 62`. It holds unconditionally for any legal 62-vertex graph.
- **Scope**: This argument eliminates actual triple repeat entries ($B_{xy} \le 2$ for all distinct $x, y$). It does not claim nonexistence of order-62 graphs.
- **Verdict for Item A: PASS (Provable as stated; clean analytic replacement).**

---

### Part B: Formal Review of `N62TripleMatching.lean`

#### 1. Mathematical Structure and Implementation
- **Source**: [`formal/DegreeDiameter/N62TripleMatching.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62TripleMatching.lean) (280 lines), importing `N62TripleRepeat`.
- **Definition**: Exclusive original-neighbor side is defined constructively:
  `tripleExclusiveNeighbors G u v = G.neighborFinset u \ commonNeighborVertices G u v`.
- **Key Results Proved**:
  - `n62_triple_exclusive_card`: $|E^+| = |E^-| = 4$.
  - `triple_exclusive_disjoint` & `triple_exclusive_common_disjoint`: $E^+$, $E^-$, and $S$ are mutually disjoint.
  - `n62_triple_exclusive_independent` & `n62_triple_exclusive_common_nonadj`: $E^+$ and $E^-$ are independent sets in $G$ and have no original edges into $S$.
  - `n62_triple_exclusive_opposite_common_card`: For $x \in E^+$, $|\operatorname{CN}(x, v)| = 1$.
  - `n62_triple_cross_neighbors_eq`: $\operatorname{CN}(x, v)$ is precisely $N_G(x) \cap E^-$.
  - `n62_triple_cross_degree_one` & `n62_triple_exclusive_unique_neighbor`: Cross degree from $E^+$ into $E^-$ is exactly 1, defining a unique neighbor in $E^-$.
  - `tripleExclusiveMate`: The choice function selecting the unique cross-side neighbor.
  - `tripleMatchingEquiv`: The constructed equivalence (bijection) between subtypes $\{x // x \in E^+\}$ and $\{y // y \in E^-\}$.
  - `tripleMatchingEquiv_adj_iff`: $G.\text{Adj } x \, y \iff \text{tripleMatchingEquiv } x = y$.
  - `n62_triple_exclusive_exterior_card`: Subtracting $\{u\}$ and the matching mate leaves exactly 6 neighbors for $x \in E^+$, all lying outside $\{u, v\} \cup S \cup E^+ \cup E^-$.

#### 2. Axioms and Build Audit
- **Audited declarations**: 19 declarations (17 public theorems + 2 constructions).
- **Axioms**: The audit log [`formal/logs/n62-triple-matching-type-axiom-audit-final.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-matching-type-axiom-audit-final.log) confirms all 19 declarations depend strictly on the standard Lean 4 axioms:
  `[propext, Classical.choice, Quot.sound]`.
  No `sorry`, no unproven axioms, no `native_decide`.
- **Callers**: All 4 actual-input example callers in [`formal/ReviewN62TripleMatching.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62TripleMatching.lean) compile and pass.
- **Build Status**: Verified via pre-existing log [`formal/logs/n62-triple-matching-second.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-matching-second.log) (exit 0, 1799 jobs, 41s).
- **Verdict for Item B: PASS (Complete and verified).**

---

### Part C: Formal Review of `N62RepeatComponentBudget.lean`

#### 1. Mathematical Structure and Implementation
- **Source**: [`formal/DegreeDiameter/N62RepeatComponentBudget.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62RepeatComponentBudget.lean) (55 lines), importing only `N62RepeatQuotientTrace`.
- **Public Theorems**:
  1. `n62_repeat_component_weight_sum`:
     $$\sum_{C} (1 + 2 R_{CC}) = 17.$$
  2. `n62_repeat_component_subset_budget`: For any finite subset $S$ of actual components:
     $$|S| + 2 \sum_{C \in S} R_{CC} \le 17.$$
  3. `n62_no_six_components_three_internal_two`: Proves `False` given original graph assumptions, $c \ge 6$, and a 3-element subset $S$ with $R_{CC} \ge 2$ for all $C \in S$.
- **Caller Hypotheses**: The component conditions ($c \ge 6$ and existence of $S$ with $|S|=3, R_{CC} \ge 2$) are **explicit hypotheses** of theorem 3, formalizing the exact numerical tail of `TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md`. It does not claim formal construction of those components from $B_{uv}=3$ in this module.

#### 2. Axioms and Build Audit
- **Axioms**: The audit log [`formal/logs/n62-repeat-component-budget-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-component-budget-type-axiom-audit.log) confirms all 3 theorems depend strictly on:
  `[propext, Classical.choice, Quot.sound]`.
  No `sorry`, no extra axioms.
- **Callers**: Both example callers in [`formal/ReviewN62RepeatComponentBudget.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62RepeatComponentBudget.lean) compile and pass.
- **Build Status**: Verified via pre-existing log [`formal/logs/n62-repeat-component-budget-first.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-component-budget-first.log) (exit 0, 1793 jobs, 12s).
- **Verdict for Item C: PASS (Complete and verified).**

---

### Summary of Scoped Verdicts

| Item | Artifact | Scope | Verdict |
|---|---|---|---|
| **A** | `TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md` | Purely analytic exclusion of $B_{uv}=3$ via three 8-point components and quotient trace | **PASS** |
| **B** | `formal/DegreeDiameter/N62TripleMatching.lean` | Formal construction of exclusive sides $E^+, E^-$ and their perfect matching | **PASS** |
| **C** | `formal/DegreeDiameter/N62RepeatComponentBudget.lean` | Formal component budget $\sum (1+2R_{CC})=17$ and the $c \ge 6, |S|=3, R_{CC} \ge 2$ obstruction | **PASS** |

*Global Scope Confirmation*: No claim of full order-62 nonexistence, exact $N(8,2)$ bound, or Lean connectedness of $B$ is made. Known 63–65 work remains stopped.


## Executor disposition

All three actual source scopes accepted. The new paper replaces the triple-repeat proof's external matrix enumeration and final row-support parity table; it retains the recovered original-graph reductions in Steps1--3 and the independent raw-input trace identity. This is a paper-level dependency replacement, not a claim that the entire triple exclusion has been formalized.

One mathematical notation error in the review is explicitly rejected: the N300 contradiction uses entrywise disjointness L_zz' Q_zz'=0, NOT the matrix-product assertion LQ=0. The recovered source states the correct entrywise relation, and the fresh local audit independently checked both direct cases with that relation. Matrix commutation LQ=QL is a different fact and is unnecessary in the new N111 argument. No proof-source repair is needed.

The reviewer ran no programs; actual build and caller audit records are independent local evidence. Requested/CLI-selected model metadata is not backend attestation. ComponentBudget's six-component and three-diagonal hypotheses remain explicit and unconstructed in that module. No whole62 exclusion or exact N8 value follows.

