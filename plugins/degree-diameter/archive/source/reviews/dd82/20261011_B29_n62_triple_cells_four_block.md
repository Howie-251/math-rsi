# B29 — actual triple cells and four-label classification

### Review Metadata and Execution Scope

- **CLI-selected model & reasoning effort**: `gemini-3.8-flash-high` / `high` (preserves CLI configuration metadata; distinct from backend attestation).
- **Execution disclosure**: **0 executions performed by the reviewer.** No shell commands, compilation jobs, or test scripts were run. All referenced build outputs and axiom logs pre-existed in the workspace.
- **Reading scope**:
  - **Read in full**:
    - [`formal/DegreeDiameter/N62TripleCells.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62TripleCells.lean) (all 372 lines).
    - [`formal/ReviewN62TripleCells.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62TripleCells.lean) (all 101 lines).
    - [`formal/N62_TRIPLE_CELLS_HANDOFF.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/N62_TRIPLE_CELLS_HANDOFF.md) (all 34 lines).
    - [`formal/logs/n62-triple-cells-second.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-cells-second.log) (all 40 lines).
    - [`formal/logs/n62-triple-cells-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-cells-type-axiom-audit.log) (all 176 lines).
    - [`formal/DegreeDiameter/N62TripleFourBlock.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62TripleFourBlock.lean) (all 141 lines).
    - [`formal/ReviewN62TripleFourBlock.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62TripleFourBlock.lean) (all 25 lines).
    - [`formal/N62_TRIPLE_FOUR_BLOCK_HANDOFF.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/N62_TRIPLE_FOUR_BLOCK_HANDOFF.md) (all 75 lines).
    - [`formal/logs/n62-triple-four-block-build-third.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-four-block-build-third.log) (all 3 lines).
    - [`formal/logs/n62-triple-four-block-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-four-block-type-axiom-audit.log) (all 34 lines).
  - **Unfinished files not reviewed**: [`N62TripleActualBlock.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62TripleActualBlock.lean) and [`N62TripleCellDegrees.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62TripleCellDegrees.lean) were explicitly omitted per caller instructions.
- **Correction recognized**: In case $(3,0,0)$, the obstruction is the entrywise contradiction $L_{zz'} Q_{zz'} = 0$ (an original edge in a triangle has defect at most 1, contradicting $Q_{zz'} = 3$), not matrix product $LQ=0$.

---

### Part 1: Audit of `N62TripleCells.lean`

#### 1. Mathematical Structure and Grounding
- **Input Hypotheses**: Takes raw `G : SimpleGraph V`, `degreeAtMostEight G`, `diameterAtMostTwo G`, `Fintype.card V = 62`, and the actual hypothesis `defectMatrix G u v = 3`. No partition, cell, equitable quotient, or row certificates are assumed.
- **Exclusive Repeat Crossing and Closure**:
  - `n62_triple_exclusive_repeat_sum`: Proves $\sum_{y \in E^-} B_{xy} = 3$ for every $x \in E^+$. The derivation evaluates $(AB)_{vx} = (BA)_{vx} = 3$ using the saturated row $B_v = 3e_u$ and $A_{ux} = 1$. It then removes $S = \operatorname{CN}(u, v)$ from $N_G(v)$ because $x \notin S$ and the repeat block $B[S]$ is closed, leaving exactly the sum over $E^-$.
  - `n62_triple_exclusive_repeat_zero_outside`: With row sum 3 and nonnegativity, all repeat entries from $x \in E^+$ outside $E^-$ vanish.
  - `n62_triple_exclusive_repeat_crosses`: Any positive repeat entry from $E^+$ crosses into $E^-$.
  - `n62_triple_exclusive_union_card` & `n62_triple_exclusive_union_repeat_closed`: The 8-element set $E = E^+ \cup E^-$ is constructed and proved repeat-closed.
- **Outer 24-Set $U$ Construction and Disjoint Fibers**:
  - `tripleOuterFiber G u v s = G.neighborFinset s \ {u, v}`: Has cardinality 6 for each $s \in S$ (`n62_triple_outer_fiber_card`).
  - `n62_triple_outer_fibers_disjoint`: Proves the four fibers are pairwise disjoint using `n62_triple_outside_common_neighbors_unique`.
  - `tripleOuterVertices G u v`: Defined as the finite union $\bigcup_{s \in S} \operatorname{fiber}(s)$, with cardinality exactly $4 \times 6 = 24$ (`n62_triple_outer_card`).
  - `n62_triple_outer_outside`: Proves $U$ is disjoint from $\{u, v\}$, $S$, $E^+$, and $E^-$.
- **Repeat Closure of $U$ via Component Equitability**:
  - `tripleCommonDegree G u v z`: Counts original neighbors in $S$. It equals 4 on $\{u, v\}$ and 1 on $U$. In fact, `n62_triple_outer_iff_common_degree_one` establishes that $z \in U \iff \operatorname{deg}_S(z) = 1$.
  - `n62_triple_common_degree_repeat_eq`: Proves that if $B_{xy} > 0$, then $\operatorname{deg}_S(x) = \operatorname{deg}_S(y)$. The proof invokes `n62_repeat_components_equitable` on the actual connected component $S$.
  - `n62_triple_outer_repeat_closed`: Directly follows from equitability: if $x \in U$, its degree into $S$ is 1, so any repeat neighbor $y$ also has degree 1 into $S$, placing $y \in U$.
- **Inner 14-Set and Remaining 24-Set $V$**:
  - `tripleInnerVertices G u v = {u, v} ∪ (N_G(u) ∪ N_G(v))`: Has cardinality $2 + 12 = 14$ (`n62_triple_inner_card`), decomposes into $\{u, v\} \cup S \cup E^+ \cup E^-$, and is repeat-closed (`n62_triple_inner_repeat_closed`).
  - `tripleRemainingVertices G u v`: Defined as $V(G) \setminus (\text{Inner} \cup \text{Outer})$. Has cardinality $62 - 14 - 24 = 24$ (`n62_triple_remaining_card`).
  - `n62_triple_remaining_repeat_closed`: Proved repeat-closed via the symmetry of $B$ and the established closures of Inner and Outer sets.

#### 2. Axioms and Verification
- **Axiom Check**: The 23 public declarations depend strictly on `[propext, Classical.choice, Quot.sound]`. No `sorry`, no extra axioms.
- **Example Callers**: All 4 actual-input callers in `ReviewN62TripleCells.lean` compile cleanly.
- **Pre-existing Build Evidence**: `formal/logs/n62-triple-cells-second.log` (exit 0, 1800 jobs, 27s; contains only two standard linter suggestions on `simpa`). `formal/logs/n62-triple-cells-type-axiom-audit.log` (exit 0).
- **Scoped Scope**: The module does not assert the full 5-cell original-neighbor quotient matrix, the 4-block classification, or full triple elimination.

---

### Part 2: Audit of `N62TripleFourBlock.lean`

#### 1. Mathematical Structure and Grounding
- **Input Hypotheses**: Generic matrix $N : \operatorname{Matrix}(\operatorname{Fin } 4)(\operatorname{Fin } 4)\,\mathbb{Z}$ with explicit hypotheses:
  `hsym` ($N = N^T$), `hdiag` ($N_{ii} = 0$), `hnonneg` ($N_{ij} \ge 0$), and `hrow` ($\sum_j N_{ij} = 3$).
- **Opposite-Entry Equality**:
  - `n62_four_block_opposite_entries`: Proves $N_{01} = N_{23}$, $N_{02} = N_{13}$, $N_{03} = N_{12}$, and $N_{01} + N_{02} + N_{03} = 3$. Proved via integer linear arithmetic on the four row-sum equations.
- **Ten Integer Weight Partitions**:
  - `n62_four_block_weight_cases`: Classifies $(N_{01}, N_{02}, N_{03})$ into the 10 nonnegative integer partitions of 3.
- **Classification via Actual Label Permutations**:
  - `tripleFourPattern N a b c` defines the six upper off-diagonal entries:
    $$N_{01}=a, N_{02}=b, N_{03}=c, N_{12}=c, N_{13}=b, N_{23}=a.$$
  - `n62_four_block_classification`: Proves the existence of $\sigma \in \operatorname{Perm}(\operatorname{Fin } 4)$ fixing label 0 ($\sigma(0) = 0$) such that the relabeled matrix $(i, j) \mapsto N_{\sigma(i), \sigma(j)}$ satisfies `tripleFourPattern` for $(3,0,0)$, $(2,1,0)$, or $(1,1,1)$.
  - **Permutations are Label Permutations**: The witnesses are explicit elements of $\operatorname{Perm}(\operatorname{Fin } 4)$ generated by transpositions of labels $\{1, 2, 3\}$ (e.g., $\operatorname{id}$, $(1\,2)$, $(1\,3)$, $(2\,3)$, $(1\,2)(1\,3)$, $(1\,3)(1\,2)$). They act by conjugating the matrix entries $N_{\sigma(i), \sigma(j)}$, which corresponds to actual vertex relabeling, not an ungrounded reordering of numbers.
- **Isolation of Matrix Premises**: The matrix premises are supplied explicitly to this module and are **not** constructed from an original graph $G$ here. The bridge to an actual graph $G$ remains separate ongoing work.

#### 2. Axioms and Verification
- **Axiom Check**: All 3 exported theorems depend strictly on standard Lean 4 axioms `[propext, Classical.choice, Quot.sound]`.
- **Example Caller**: The caller in `ReviewN62TripleFourBlock.lean` compiles with exit 0.
- **Pre-existing Build Evidence**: `formal/logs/n62-triple-four-block-build-third.log` (exit 0, 1042 jobs, 9.6s). `formal/logs/n62-triple-four-block-type-axiom-audit.log` (exit 0).

---

### Summary of Scoped Verdicts

| Item | Artifact | Scope | Verdict |
|---|---|---|---|
| **1** | `formal/DegreeDiameter/N62TripleCells.lean` | Formal construction of cells $E$ (size 8), $U$ (size 24), Inner (size 14), Remaining $V$ (size 24) and their repeat-closures via $S$-component equitability | **PASS** |
| **2** | `formal/DegreeDiameter/N62TripleFourBlock.lean` | Algebraic classification of symmetric $4 \times 4$ zero-diagonal row-sum-3 nonnegative integer matrices into patterns 300, 210, 111 under label permutations fixing 0 | **PASS** |

*Global Scope Confirmation*: No claim of full order-62 nonexistence, exact $N(8,2)$ bound, or complete 5-cell original-neighbor quotient is made. The graph-to-matrix bridge remains separate. Known 63–65 work remains stopped.


## Executor disposition

Both completed module scopes accepted. Actual local builds and caller audits remain the execution evidence; the reviewer executed no commands. The generic FourBlock premises are not yet discharged by an actual-graph construction in this module. Cells does not yet export all original-neighbor five-cell counts. No full triple elimination or order62 theorem is claimed.

The review opening gloss about an original edge in a triangle is not used: the retained N300 contradiction is the exact entrywise relation L_zz'Q_zz'=0 from the recovered reduction. The new source scopes under review do not depend on that gloss. Requested and CLI-selected model metadata is not backend attestation.
