### 1. Inspection and Execution Record

- **Files Read in Full**:
  1. [`proofs/dd82/n59/zero_heavy_global_capacity_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/zero_heavy_global_capacity_20261011.md)
  2. [`formal/DegreeDiameter/N59ZeroCore.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59ZeroCore.lean)
  3. [`formal/logs/n59-zero-core-heavy-build.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n59-zero-core-heavy-build.log)
  4. [`formal/logs/n59-zero-core-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n59-zero-core-type-axiom-audit.log)
- **Commands Executed**: **Zero**. No processes, bash commands, Lake builds, or solver runs were executed by the reviewer. Build logs, audit traces, and proof scripts were inspected strictly as static artifacts.
- **Model and Effort Metadata**: Gemini 3.8 Flash (High), reasoning effort `high`.
- **Baseline Alignment**: No work on known orders 63–65 was requested or performed. Analysis is restricted strictly to unresolved orders 58–62.

---

### 2. Paraphrase Clarification: Brown Union-Size 21 Case Enumeration

In Checkpoint B10, the figure of 72,520 cases per parallel class represents:
$$\binom{203}{2} = 20,503 \text{ distinct unordered pairs of extra edges},$$
which expand to **72,520 total known-deletion cases** after branching over the deleted-edge refinements in the (up to two) affected base triangles. Across the two parallel classes, the search exhaustively covers $2 \times 72,520 = 145,040$ cases. The fresh root audit confirming that the full $\ge 10$ deletion obstruction passes all 28 obligations on single-CPU reruns is noted as established.

---

### 3. $n=59$: Global Heavy-Repeat Capacity ($m \ge 20, T \ge 7$)

The proof package in [`zero_heavy_global_capacity_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/zero_heavy_global_capacity_20261011.md) is completely self-contained. It dispenses with the zero-heavy endpoint lemma, the zero-support transport theorem, the separate degree lower bound $d_N(z) \ge 2$, and all small-$T$ configuration classifications. It requires only:
1. $G$ is an original legal graph on 59 vertices ($\Delta \le 8, \operatorname{diam} \le 2$).
2. At every zero-triangle vertex $z \in Z$, its defect row has entries 2, 2, 1, 1, and the two endpoints of each equal-weight pair are adjacent in $G$.

#### (1) Independent Derivation and Adversarial Check of Core Steps

1. **Capacity Bound on Common Zero Neighbors**:
   - For an independent set $U \subseteq Z$, each vertex $u \in U$ has its two light endpoints adjacent in $G$ and its two heavy endpoints adjacent in $G$. Since $U$ is independent, it contains at most one endpoint of each pair. Thus the defect edges restricted to $U$ form a union of two matchings (properly 2-edge-colored). No odd cycle (and specifically no triangle) can exist in this defect graph.
   - For any distinct $r, s \in V$, the set $N_G(r) \cap N_G(s) \cap Z$ is independent (an edge would create a triangle at a zero vertex). If it contained $\ge 3$ vertices, every pair would have defect $B \ge 2 - 1 = 1 > 0$, forming a defect triangle in $U$. Contradiction.
   - Hence for all $r \ne s$:
     $$|N_G(r) \cap N_G(s) \cap Z| \le 2\tag{2}$$
   - Any heavy defect edge with an endpoint in $Z$ is a nonedge with 3 common neighbors. By (2), at most 2 are in $Z$, so **at least one common neighbor lies in $N$**.

2. **Exact Nonzero Root Identity and Slack**:
   - Fix $n \in N$ and set $U_n = N_G(n) \cap Z$ (which is independent in $G$).
   - For any pair $\{z, w\} \subseteq U_n$, $n$ is one common neighbor. No other common neighbor can lie in $N_G(n)$ (otherwise an edge between neighbors of $n$ would touch a zero vertex). Hence all other common neighbors lie in $V \setminus N_G[n]$.
   - Since $z, w$ are nonadjacent, $B_{zw}$ is precisely their common neighbor count outside $N_G[n]$.
   - Summing over all pairs $\{z, w\} \subseteq U_n$:
     $$\ell_n + 2h_n = \sum_{\{z, w\} \subseteq U_n} B_{zw} = \sum_{y \notin N_G[n]} \binom{q_y}{2}\tag{3}$$
     where $q_y = |N_G(y) \cap U_n| = |N_G(y) \cap N_G(n) \cap Z| \le 2$ by (2).
   - Pointwise comparison with nonedge row entries $B_{ny}$:
     - If $q_y \le 1$: $\binom{q_y}{2} = 0 \le B_{ny}$.
     - If $q_y = 2$: $\binom{q_y}{2} = 1$. The 2 vertices in $N_G(y) \cap U_n$ are common neighbors of $n$ and $y$, so $B_{ny} = c(n, y) - 1 \ge 2 - 1 = 1 = \binom{q_y}{2}$.
   - **Crucial Slack from Zero Heavy Repeats**:
     - Let $k_n = |\{y \in Z : B_{ny} = 2\}|$.
     - For each such $y$, $B_{ny} = 2$, whereas $\binom{q_y}{2} \le 1$ (since $q_y \le 2$).
     - Thus $B_{ny} - \binom{q_y}{2} \ge 2 - 1 = 1$. Each zero heavy repeat contributes at least 1 unit of strict slack.
   - Summing over $y \notin N_G[n]$ and using $\sum_{y \notin N_G[n]} B_{ny} = 6 - 2t(n)$:
     $$\ell_n + 2h_n + k_n \le \sum_{y \notin N_G[n]} \binom{q_y}{2} + k_n \le \sum_{y \notin N_G[n]} B_{ny} = 6 - 2t(n)$$
     $$\implies 2h_n + k_n \le 6 - 2t(n)\tag{4}$$

3. **Global Summation and Inequality Direction**:
   - Let $H_{ZZ}$ be the number of heavy defect edges within $Z$, and $K_{ZN}$ the number between $Z$ and $N$.
   - Sum of heavy degrees in $Z$: $2|Z| = 2H_{ZZ} + K_{ZN}$.
   - Every heavy edge in $Z$ has at least one common neighbor in $N$ and is thus counted in $h_n$ for each such neighbor. Hence:
     $$H_{ZZ} \le \sum_{n \in N} h_n\tag{6}$$
   - Also $K_{ZN} = \sum_{n \in N} k_n$ exactly.
   - Summing (4) over all $n \in N$:
     $$2|Z| = 2H_{ZZ} + K_{ZN} \le 2\sum_{n \in N} h_n + \sum_{n \in N} k_n \le \sum_{n \in N} (6 - 2t(n)) = 6m - 6T$$
   - Substituting $|Z| = 59 - m$:
     $$2(59 - m) \le 6m - 6T \iff 118 \le 8m - 6T \iff \mathbf{59 \le 4m - 3T}\tag{7}$$

4. **Corollaries**:
   - Triangle incidence gives $m \le 3T$, so $-3T \le -m$. Substituting into (7):
     $$59 \le 4m - m = 3m \implies m \ge \lceil 59/3 \rceil = \mathbf{20}$$
   - Similarly $4m \le 12T$. Substituting into (7):
     $$59 \le 12T - 3T = 9T \implies T \ge \lceil 59/9 \rceil = \mathbf{7}$$
   - **Exact Slack Identity**:
     $$2(4m - 3T - 59) = \sum_{n \in N} \ell_n + 2\left(\sum_{n \in N} h_n - H_{ZZ}\right) + \sum_{n \in N} R_n$$
     where each $R_n \ge 0$ pointwise.
   - For equality $(m = 20, T = 7)$, all slack terms vanish: no light zero defect edge has a common neighbor in $N$; every heavy zero defect edge has exactly 1 common neighbor in $N$ and 2 in $Z$; and no heavy defect edges exist within $N$.

---

### 4. Lean Formalization Review: `N59ZeroCore.lean`

- **Source File**: [`formal/DegreeDiameter/N59ZeroCore.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59ZeroCore.lean)
- **Compilation Status**: Verified in [`formal/logs/n59-zero-core-heavy-build.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n59-zero-core-heavy-build.log) (1792 jobs completed successfully, only benign unused-simp-argument linter warnings).
- **Axiomatic Audit**: Verified in [`formal/logs/n59-zero-core-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n59-zero-core-type-axiom-audit.log). Transitive axioms are strictly `[propext, Classical.choice, Quot.sound]`. Zero `sorry`, zero custom axioms.

#### Back-Translation of Formal Declarations

1. [`zeroTriangleVertex`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59ZeroCore.lean#L12-L13):
   ```lean
   def zeroTriangleVertex (G : SimpleGraph V) (z : V) : Prop :=
     ∀ u v, G.Adj z u → G.Adj z v → ¬ G.Adj u v
   ```
   - **Translation**: For any two neighbors $u, v$ of $z$, $u$ and $v$ are nonadjacent. This is the exact, standard graph-theoretic statement that $z$ is contained in no triangle.

2. [`commonZeroNeighbors`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59ZeroCore.lean#L16-L17):
   ```lean
   def commonZeroNeighbors (G : SimpleGraph V) (u v : V) : Finset V :=
     (G.neighborFinset u).filter (fun z => G.Adj z v ∧ zeroTriangleVertex G z)
   ```
   - **Translation**: The finite set $N_G(u) \cap N_G(v) \cap \{z : \text{zeroTriangleVertex}(G, z)\}$.

3. **Hypothesis Scope**:
   In [`common_zero_neighbors_card_le_two`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59ZeroCore.lean#L98-L100) and [`n59_zero_heavy_has_nonzero_common_neighbor`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59ZeroCore.lean#L159-L164), the premise is:
   ```lean
   (hm : ∀ z, zeroTriangleVertex G z → matchingRow G z)
   ```
   - **Audit**: The quantifier is strictly guarded by `zeroTriangleVertex G z`. It places no conditions on nonzero vertices. It does not assume any precomputed certificate, matrix embedding, or global graph structure.

4. **Compiled vs. Remaining Downstream Scope**:
   - **Compiled in Lean**:
     - `common_zero_neighbors_card_le_two`: $|N_G(r) \cap N_G(s) \cap Z| \le 2$ for all $r \ne s$.
     - `n59_zero_heavy_has_nonzero_common_neighbor`: For any zero vertex $u$ and $B_{uv} = 2$, there exists a common neighbor $w$ that belongs to at least one triangle (`¬ zeroTriangleVertex G w`).
   - **Pending in Lean**:
     - The finite summation step (Step 2 identity $\sum \binom{q_y}{2} = \ell_n + 2h_n$ and Step 3 global double-count $59 \le 4m - 3T$) remains in paper form and is not yet assembled in Lean.

---

### 5. Summary of Project Status (Orders 58–62)

| Component | Statement / Inequality | Mathematical Status | Lean Status |
| :--- | :--- | :--- | :--- |
| **Order 59 ($n=59$)** | Common zero neighbors $\le 2$ | **Proved** | **Compiled** ([`N59ZeroCore.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59ZeroCore.lean#L98)) |
| **Order 59 ($n=59$)** | Heavy zero defect edge has nonzero common neighbor | **Proved** | **Compiled** ([`N59ZeroCore.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N59ZeroCore.lean#L159)) |
| **Order 59 ($n=59$)** | Nonzero root slack: $2h_n + k_n \le 6 - 2t(n)$ | **Proved** (self-contained) | Pending formalization |
| **Order 59 ($n=59$)** | Global heavy capacity: $59 \le 4m - 3T$ | **Proved** (self-contained) | Pending formalization |
| **Order 59 ($n=59$)** | Exclusion of $T \le 6$ ($m \ge 20, T \ge 7$) | **Proved** (self-contained) | Pending formalization |
| **Order 58 (Brown57)** | Extensions of fixed Brown graph require $\ge 10$ deletions | **Proved** (28 obligations passed) | Paper / C++ checked |
| **Arbitrary $n=58$** | Arbitrary order-58 graph existence | **Open** | Open |
| **Exact Goal** | Determination of $N(8,2)$ | **Open** (Baseline $[57, 62]$) | Open |


Executor disposition: Accepted complete self-contained global heavy-capacity inequality59<=4m-3T,m>=20,T>=7 underzero-row2211+equalweightadjacency, exactslack/equalityscopes, andbacktranslationofcompiledN59ZeroCore. Reviewerexecutedzerocommands; actualbuild/axiomevidencebelongsexecutor. Freshdeltaauditpassed22paperobligations. Globalcapacityfinitecountcurrentlybeingformalized, notyetLean. LaterT7m20exclusionandcrossheavychargingpaperareoutsideB11. Known63–65workremainsstopped.
Requested/CLIselectedgemini-3.8-flash-high/high, nobackendattestation.
