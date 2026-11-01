### 1. Scope of Reading and Audit Execution

* **Files read:**
  * [`context/propertyb33/round01/large-math/REPORT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/REPORT.md)
  * [`context/propertyb33/round01/profile33/REPORT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/profile33/REPORT.md)
  * [`context/propertyb33/round01/profile33/compatibility.patch`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/profile33/compatibility.patch)
  * [`context/propertyb33/round01/twenty-complete/REPORT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/twenty-complete/REPORT.md)
  * [`context/propertyb33/round01/twenty-complete/import-audit.log`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/twenty-complete/import-audit.log)
  * [`context/propertyb33/round01/twenty-complete/assembly-build.log`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/twenty-complete/assembly-build.log)
  * [`proofs/propertyb33/TWENTY_ONE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY_ONE.md)
  * [`context/propertyb33/round01/twentyone-math/ORDINARY_SEVEN.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/twentyone-math/ORDINARY_SEVEN.json)
  * [`context/propertyb33/round01/twentyone-math/REMAINING_ROUTES.json`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/twentyone-math/REMAINING_ROUTES.json)
  * [`context/propertyb33/round01/large-math/V25_EIGHT_LOCK_ROUTE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/V25_EIGHT_LOCK_ROUTE.md)
  * [`context/propertyb33/round01/large-math/EIGHT_COVERAGE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/EIGHT_COVERAGE.md)
  * [`context/propertyb33/round01/large-math/eight-classification-lean.log`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/eight-classification-lean.log)
  * [`formal/Aris4Math/ThirtyThree/EightClassification.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/EightClassification.lean)
  * [`formal/Aris4Math/ThirtyThree/TwentyFiveStructure.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFiveStructure.lean)
* **Actions executed:** Strictly read-only tool calls (`view_file`, `grep_search`, `find_by_name`). No shell commands, build commands, or file edits were executed.

---

### 2. Explicit Correction: The 22-Point (7,7) Proposal

* **Retraction & Correction:** In the previous checkpoint, the suggestion that an ordinary-link lower bound on the $(7,7)$ profile at $v=22$ would *"provide the extra margin needed to close the (7,7) case"* was an unverified heuristic conjecture and **factually incorrect**.
* **Observed Evidence:** As established by the exact arithmetic in [`context/propertyb33/round01/large-math/REPORT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/REPORT.md#L52-L55):
  * For $v=22$, lock pair $(7,7)$ with $\lambda=1$, the counts are $q_{\mathrm{all}} \ge 3$ and $q_{LL} \ge 2$.
  * Weight $w_{LL} = 42/4199$ and $w_{LD} = 39/4199$, giving a per-center deduction lower bound of $123/4199$.
  * Applying this strengthened deduction still leaves:
    $$U \le \frac{4212}{4199} = \frac{324}{323} > 1$$
  * Because $324/323 > 1$, ordinary-link deduction on $(7,7)$ fails numerically and **does not close the 22-point $(7,7)$ case**.

---

### 3. Formal Status Audit: 20-Vertex Branch and Main Regression

#### A. 20-Vertex Branch Connection
* **Source-to-input chain:**
  * [`TwentyStructure.exists_two_locks_of_twenty`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyStructure.lean#L22): Unconditionally extracts an actual codegree-1 pair $(x, y)$ in one of 12 degree pairs from any pair-covering $H$ with $|E|=33$ on $\mathrm{Fin}\; 20$.
  * [`TwentyStandard.propertyB_of_standard_pair`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyStandard.lean#L49): Discharges the 11 standard degree pairs via real profile realization and P8 link deletion.
  * [`TwentyEight.propertyB_of_eight_eight`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyEight.lean#L58): Discharges $(8,8)$ using [`OrdinaryLink`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/OrdinaryLink.lean) and [`CustomDeletion`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/CustomDeletion.lean) with deduction $1239/24310$ per center, achieving $2421/2431 < 1$.
  * [`Twenty.twenty_propertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Twenty.lean#L11): Dispatches $H$ to the 12 cases with no leftover probability or profile assumptions.
* **Assembly state:**
  * [`Assembly.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/Assembly.lean#L28-L30) connects `twenty_propertyB` alongside `nineteen_propertyB`.
  * The actual reduction theorem proven is:
    $$\mathrm{Target33}.\{u\} \leftrightarrow \mathrm{RemainingGoal}$$
    where `RemainingGoal` is explicitly:
    $$\forall v : \mathbb{N}, \; 21 \le v \le 25 \implies \forall H : \mathrm{Simple5Hypergraph}(\mathrm{Fin}\; v), \; |H.\mathrm{edges}| = 33 \to H.\mathrm{PairCovering} \to \mathrm{PropertyB}\; H$$
* **Logs & Axiom check:**
  * [`twenty-complete/assembly-build.log`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/twenty-complete/assembly-build.log) and [`import-audit.log`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/twenty-complete/import-audit.log) confirm exit code 0.
  * Transitive axioms for `twenty_propertyB`, `TwentyEight.propertyB_of_eight_eight`, and `target_iff_remaining_goal` are strictly `[propext, Classical.choice, Quot.sound]`. No `sorry` or `sorryAx`.

#### B. Compatibility Patch and Old Main Regression
* [`profile33/compatibility.patch`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/profile33/compatibility.patch) introduces an optional default argument `(edgeCount : ℕ := 32)` across 6 core files (`Numeric.lean`, `TypeCounting.lean`, `ProfileProbability.lean`, `ProfileApplication.lean`, `ProfileDeletion.lean`, `LinkWeightCertificates.lean`).
* Old callers default to 32; new 33-edge callers supply 33.
* [`profile33/REPORT.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/profile33/REPORT.md#L58-L70) and build logs confirm the old 32-edge `Aris4Math.Main` rebuilds with exit code 0 and identical axioms.

---

### 4. Mathematical Attack: 21-Vertex Candidate Proof ([`TWENTY_ONE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY_ONE.md))

We audited the structural coverage and numerical verification in [`TWENTY_ONE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY_ONE.md) and [`twentyone-math/`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/twentyone-math/).

#### A. Case $\delta(H) = 5$
* For a degree-5 vertex $x$, surplus is $\sum_{y \ne x} (\lambda_{xy} - 1) = 4(5) - 20 = 0 \implies \lambda_{xy} = 1$ for all $y \ne x$.
* If another vertex $y$ has degree 5, 6, or 7, lock $(x, y)$ with $\lambda=1$. The profiles `5_5_lambda_1` ($4092/4199$), `5_6_lambda_1` ($8163/8398$), `5_7_lambda_1` ($4155/4199$) are all strictly $< 1$.
* If all remaining 20 vertices have degree $\ge 8$: total degree budget is $5 + 20 \times 8 = 165$, forcing all 20 other vertices to have degree exactly 8.
  * Pick $y \ne x$ ($d(y)=8$). Surplus is $4(8) - 20 = 12$, leaving at least $20 - 12 = 8$ codegree-1 partners.
  * Exclude $x$ and the 3 other vertices in the unique $xy$ edge: at most 4 vertices.
  * There remain $\ge 8 - 4 = 4$ candidates for $z$, yielding a triple $(x, y, z)$ with degrees $(5, 8, 8)$, pairwise codegrees $\lambda = (1, 1, 1)$, and triple codegree $t = 0$.
  * Bound: `5_8_8_pairwise_lambda_1_triple_0` at positions $(11, 12, 13)$ is $2369/2431 < 1$. Fully covered.

#### B. Case $\delta(H) = 6$, Multiple Degree-6 Vertices
* Pick any two degree-6 vertices $x, y$. Codegree $\lambda(x, y) \in \{1, 2, 3, 4, 5, 6\}$.
* Profiles `6_6_lambda_1` through `6_6_lambda_6` evaluate to $4077/4199$, $20671/20995$, $11508/12155$, $205429/230945$, $192332/230945$, $13797/17765$, all strictly $< 1$. Fully covered.

#### C. Case $\delta(H) = 6$, Unique Degree-6 Vertex $x$
* All other 20 vertices have degree $\ge 7$. Since $6 + 20 \times 8 = 166 > 165$, there must exist at least one degree-7 vertex.
* If any degree-7 vertex $y$ has $\lambda(x, y) \in \{1, 3, 4, 5, 6\}$, profiles `6_7_lambda_1` and `6_7_lambda_3`..`6_7_lambda_6` all evaluate to $< 1$.
* Remaining subcase: **Every degree-7 vertex has $\lambda(x, y) = 2$**.
  * If there are $\ge 2$ degree-7 vertices $y, z$:
    * If $\lambda(y, z) \ge 3$, covered by high-codegree `7_7_lambda_3`..`7_7_lambda_7` (all $< 1$).
    * If $\lambda(y, z) \in \{1, 2\}$, then $t \le \min(2, 2, \lambda(y, z))$. This yields five $(6,7,7)$ triple configurations: $(\lambda_{xy}, \lambda_{xz}, \lambda_{yz}) = (2, 2, 1)$ with $t \in \{0, 1\}$, and $(2, 2, 2)$ with $t \in \{0, 1, 2\}$. All five evaluated profiles (`6_7_7_...`) are strictly $< 1$.
  * If there is a unique degree-7 vertex $y$:
    * Then the remaining 19 vertices have degree exactly 8 ($6 + 7 + 19 \times 8 = 165$).
    * $y$ has $\ge 12$ codegree-1 partners outside $x$.
    * $x$ has total surplus $4(6) - 20 = 4$; $y$ consumes 1, leaving at most 3 non-$y$ bad partners.
    * The two $xy$ edges contain at most 6 other vertices.
    * Candidates for $z$ from $y$'s codegree-1 partners: $12 - (3 + 6) = 3 \ge 1$.
    * This guarantees a $(6, 7, 8)$ triple with $\lambda = (2, 1, 1)$ and $t = 0$. Profile `6_7_8_lambdas_2_1_1_triple_0` at $(12, 9, 10)$ gives $3292/3315 < 1$. Fully covered.

#### D. Case $\delta(H) \ge 7$ (Minimum Degree 7)
* Surplus $\sum (d(z) - 7) = 165 - 147 = 18$. The number of degree-7 vertices $r$ satisfies $165 \ge 7r + 8(21 - r) = 168 - r \implies r \ge 3$.
* Pick any three degree-7 vertices $x, y, z$.
  * If any pair has codegree $\ge 3$, covered by `7_7_lambda_3`..`7_7_lambda_7` ($< 1$).
  * Otherwise, all three pairs have codegree $\in \{1, 2\}$. Up to permutation, 4 codegree patterns:
    * $(1, 1, 1)$, $t \in \{0, 1\}$
    * $(2, 1, 1)$, $t \in \{0, 1\}$
    * $(2, 2, 1)$, $t \in \{0, 1\}$
    * $(2, 2, 2)$, $t \in \{0, 1, 2\}$
  * Seven of these 9 triple configurations pass directly with standard deletion:
    * $(1,1,1), t=0 \implies 2406/2431 < 1$
    * $(2,1,1), t=0 \implies 24047/24310 < 1$
    * $(2,2,1), t=0 \implies 8297/8580 < 1$, $t=1 \implies 35281/36465 < 1$
    * $(2,2,2), t=0 \implies 1413/1430 < 1$, $t=1 \implies 369/374 < 1$, $t=2 \implies 141/143 < 1$.
  * The two tight configurations are:
    1. $(1, 1, 1), t = 1$
    2. $(2, 1, 1), t = 1$
  * **Strengthened Ordinary Center Count:**
    * In both configurations, there is a vertex $z$ with $\lambda(z, x) = 1$ and $\lambda(z, y) = 1$, and a unique edge $D$ containing $\{x, y, z\}$.
    * The remaining 6 edges through $z$ avoid both $x$ and $y$, forming 6 distinct 4-element links on $V \setminus \{x, z\}$ (size 19).
    * Link vertex frequencies satisfy $\sum a_u = 24$, giving $\sum \binom{a_u}{2} \ge 24 - 19 = 5$. Since 4-sets intersect in $\le 3$ vertices outside $z$, the number of ordinary-ordinary bad pairs is at least $\lceil 5/3 \rceil = 2$.
    * Setting $z$ at center position 11 (with free positions $a_{11}=9, b_{11}=9, N=18$), the two-directional weight is $w_{LL} = \frac{126}{12155}$.
    * Deleting at least $2 w_{LL} = \frac{252}{12155}$ at position 11 gives:
      * $(1, 1, 1), t = 1$ at $(10, 11, 12) \implies 12043/12155 < 1$
      * $(2, 1, 1), t = 1$ at $(9, 13, 11) \implies 1847/1870 < 1$.
* **Status:** Mathematically complete and verified in [`TWENTY_ONE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY_ONE.md). Lean formalization for $v=21$ is pending.

---

### 5. Mathematical Attack: 25-Vertex 8-Lock Route ([`V25_EIGHT_LOCK_ROUTE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/V25_EIGHT_LOCK_ROUTE.md), [`EIGHT_COVERAGE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/EIGHT_COVERAGE.md))

#### A. Structural Selection ($10 \to 8$)
1. **Ten degree-6 vertices:** At $v=25, |E|=33$, pair-covering requires $d(x) \ge 6$. Total degree budget gives $165 \ge 6r + 7(25 - r) \implies r \ge 10$.
2. **Pairwise unit codegree:** For any degree-6 vertex $x$, $\sum_{y \ne x} \lambda(x, y) = 24$ across 24 vertices, forcing $\lambda(x, y) = 1$ for all $y \ne x$.
3. **Trace structure on 10-set $W$:**
   * If any multiTrace $B = e \cap W$ has $|B| \ge 4$, taking a 6-element subset containing $B$ reduces to K6-7, K6-8, or K6-9 (all have $U < 1$).
   * If all multiTraces have size $\le 3$, double counting pairs gives:
     $$2 \binom{10}{2} = 90 = \sum B + 3 |\{B \mid |B|=3\}| \le 60 + 3 |\{B \mid |B|=3\}| \implies |\{B \mid |B|=3\}| \ge 10$$
4. **Averaging to 8 vertices:**
   * Each triple block in $W$ is contained in $\binom{10-3}{8-3} = \binom{7}{5} = 21$ eight-element subsets of $W$.
   * Total occurrences across all $\binom{10}{8} = 45$ eight-subsets: $\ge 10 \times 21 = 210$.
   * Average per 8-subset: $210 / 45 = 14/3 > 4$.
   * Hence there exists an 8-subset $S \subset W$ containing $\ge 5$ triple blocks.
   * Every vertex of $S$ must lie in at least one triple block; otherwise its 7 other vertices would require 7 distinct 2-element blocks, forcing degree $\ge 7$, contradiction.
* **Lean status of $10 \to 8$:** Fully proven in [`TwentyFiveStructure.exists_six_large_or_eight_triples`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/TwentyFiveStructure.lean#L301-L329).

#### B. Classification of the 8-Point Triple Family to 14 Types
Let $T$ be a 3-uniform, linear, covering hypergraph on an 8-element set $X$ with $|T| \ge 5$.
* **Step A (Two Disjoint Triples):**
  * If every two triples in $T$ intersect, pick $A \in T$. The other $\ge 4$ triples each intersect $A$ in 1 point.
  * By pigeonhole, two triples $B, C$ intersect $A$ at the same vertex $x$. By linearity, $B \cap C = \{x\}$.
  * Since each vertex has triple degree $\le 3$, $x$ belongs to no other triple.
  * $A \cup B \cup C$ has size $1 + 2 + 2 + 2 = 7$.
  * Any other triple $D$ must intersect $A, B, C$ in 3 distinct vertices (none of which is $x$), forcing $D \subseteq A \cup B \cup C$.
  * Thus all triples lie in a 7-element set, contradicting that $T$ covers 8 vertices.
  * Therefore, **there must exist two disjoint triples $A, B \in T$**.
* **Step B (Connecting Triple $C$):**
  * Let $Z = X \setminus (A \cup B)$, so $|Z| = 8 - 6 = 2$.
  * Any other triple $D \in T \setminus \{A, B\}$ intersects $A$ in $\le 1$ vertex and $B$ in $\le 1$ vertex.
  * If $D$ does not intersect both $A$ and $B$, it must contain both vertices of $Z$.
  * By linearity, at most one triple can contain both vertices of $Z$.
  * Since $|T \setminus \{A, B\}| \ge 3$, at least two triples must intersect both $A$ and $B$.
  * Pick one such triple $C$: it intersects $A$ in 1 vertex, $B$ in 1 vertex, and its third vertex is in $Z$.
* **Standard Seed:**
  * Labeling $A = \{0, 1, 2\}$, $B = \{3, 4, 5\}$, $C = \{0, 3, 6\}$ maps $\{A, B, C\}$ to `seed8`.
* **255-Leaf Candidate Recursion:**
  * Only 16 triples on $\mathrm{Fin}\; 8$ are linear-compatible with `seed8`.
  * The recursion generates 255 leaves, with 236 valid covering leaves of size $\ge 5$, each isomorphic to one of the 14 representatives.
* **Lean Certification Status:**
  * In [`EightClassification.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/ThirtyThree/EightClassification.lean):
    * The recursion completeness (`extensions_complete`), candidate filtering (`compatible_triple_is_candidate`), and normalized classification (`classify_seed_eight`) are fully proved and checked in [`eight-classification-lean.log`](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb33/round01/large-math/eight-classification-lean.log).
    * `exists_disjoint_triples`, `exists_seed_blocks`, `label_seed_blocks`, and `classify_eight` are also written in the file.
  * **Remaining gap:** General coverage from an actual hypergraph $H$ on 25 vertices into the 14 probability profiles and final `PropertyB` is **not yet connected in Lean**. There is no `TwentyFive.lean` or top-level 25-vertex theorem.

---

### 6. Summary of Resolved vs. Pending Components

| Vertex Count $v$ | Mathematical Status | Lean Formalization Status |
| :--- | :--- | :--- |
| **$v \le 18$** | Solved (balanced permutations / union bound) | **Fully proved & connected** (`Reduction.lean`) |
| **$v = 19$** | Solved (global pairs cap 1003, sum $228354/230945 < 1$) | **Fully proved & connected** (`Nineteen.lean`) |
| **$v = 20$** | Solved (12 configurations + ordinary link (8,8)) | **Fully proved & connected** (`Twenty.lean`, `Assembly.lean`) |
| **$v = 21$** | Solved in [`TWENTY_ONE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb33/TWENTY_ONE.md) (all 9 triples + center deduction) | **Pending Lean formalization** |
| **$v = 22$** | (6,6) and (6,7) solved; (7,7) remains open ($324/323 > 1$) | Partial Lean: (6,6) and (6,7) proved in `TwentyTwo.lean`; (7,7) open |
| **$v = 23$** | Open (needs 6-degree existence or $\ge 7$ resolution) | Pending |
| **$v = 24$** | Open (needs $r \in \{3,4,5,6\}$ 6-degree coverage) | Pending |
| **$v = 25$** | Solved via 8-lock route + 14 types ($10 \to 8$, seed normalization) | Partial Lean: structure & normalized seed proved; top-level assembly open |
