### Mathematical and Research-Direction Review: $N(13,5) \ge 51418$

---

### 1. Mathematical and Evidentiary Validity of $N(13,5) \ge 51418$

The conclusion that the constructed graph witnesses $N(13,5) \ge 51418$ is **mathematically correct and fully justified**, conditioned on the inherited published diameter $D \le 5$ of the 51417-vertex base graph:

1. **Degree constraints and simplicity**:
   - The original raw adjacency list ([`source51417.adjlist.txt`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/verify_newroot.py#L16-L28)) has $n_0 = 51417$, $m_0 = 324451$, and maximum degree 13.
   - The literal edge file [`graph_d13_D5_n51418.edges`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/independent_newroot51418.json#L53) adds exactly 10 edges connecting new vertex $51417$ to $N(51417) = \{2813, 9214, 15101, 25662, 33884, 38121, 38574, 42842, 48533, 50577\}$.
   - The original degrees of these 10 vertices were $[11, 12, 11, 12, 12, 12, 12, 12, 11, 11]$, each strictly below 13. Their new degrees are $[12, 13, 12, 13, 13, 13, 13, 13, 12, 12] \le 13$. The new root degree is $10 \le 13$.
   - Maximum degree of $G_{51418}$ is strictly 13; the graph is simple, undirected, and has $m = 324461$ edges.

2. **Diameter induction (Single-Vertex Extension Induction)**:
   - **Old-old pairs**: Because every edge of the original graph is preserved ($E_{old} \subset E_{new}$), any path in $G_{old}$ remains a path in $G_{new}$. Hence, for all $u, v \in V_{old}$, $dist_{G_{new}}(u, v) \le dist_{G_{old}}(u, v) \le 5$.
   - **New-old pairs**: BFS from root $51417$ over the reconstructed graph confirms that every vertex $u \in V_{old}$ has $dist_{G_{new}}(51417, u) \le 5$, with exact distance histogram:
     - $d=0: 1$, $d=1: 10$, $d=2: 99$, $d=3: 1032$, $d=4: 9840$, $d=5: 40436$ (Sum $= 51418$).
   - Because all pairwise distances are $\le 5$ and eccentricity of $51417$ is 5, the graph diameter is exactly 5.

3. **Gaps and scope boundaries**:
   - There are **no logical, programmatic, or evidence gaps** in the single-vertex induction or independent root check [`verify_newroot.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/verify_newroot.py#L1-L71).
   - Inheriting the published base diameter from Francesc Comellas' table without re-running an all-pairs BFS on $51417$ vertices is standard practice in DD research and aligns with the user's explicit trade-off instructions.
   - Lean 4 instances remain 0; this result is a valid verified graph construction, not a formal Lean proof.

---

### 2. Prototype-Neighborhood Single-Fault Deletion and Guard Repair

1. **Distinction from full geometric / false-twin cloning**:
   - As documented in [`REPORT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/spare_star_transfer/REPORT.md#L9-L18), exact false-twin cloning was completely degree-blocked: every vertex in $G_{51417}$ had at least one degree-13 neighbor (minimum saturated count $= 1$, attained by 91 prototypes).
   - Dropping the saturated neighbor breaks the false-twin property: new vertex $z$ can no longer route to all vertices simply by following prototype $v$'s shortest paths. For prototype $51013$ ($deg=10$), deleting saturated pin $11352$ left 3614 vertices unreachable within radius 4.

2. **Validity and efficacy of the guard repair rule**:
   - The test searched for at most 2 free guards from the host anchor pool against the **actual complete radius-4 ball ($R_4$)** of the entire graph, rather than relying on geometric or core shortcuts.
   - A single guard ($50577$, degree 11) successfully eliminated all 3614 missing vertices in a single step ([`ord037_v51013_selected.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/items/ord037_v51013_selected.json#L1)).
   - While false-twin insertion and single-vertex extensions with auxiliary connections are established graph operations, this specific pruning heuristic—freezing prototypes by minimal saturated neighbors and performing bounded guard selection against whole-graph $R_4$—is sound, efficient (0.21s CPU), and provided a genuine escape from the degree bottleneck.

---

### 3. Limitation of Failed Cases and Soundness of Continuation Scope

1. **Correct bounding of negative findings**:
   - The 37 failed prototypes (ordinals 0–36) are accurately designated [`EXACT_NO_AT_MOST_TWO_GUARDS`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/RESULT.json#L51).
   - The record explicitly preserves `"larger_actual_guard_budget_open": true` and `"full_actual_guard_budget_excluded": false`. It does not overclaim non-existence of higher-guard repairs; it strictly logs that no repair exists within the tested $\le 2$ guard budget.
   - None of the 37 failed prototypes were reopened or entered into unbounded parameter tweaking.

2. **Soundness of continuing across the remaining 53 unattempted items**:
   - The candidate pool (91 prototypes) was frozen *prior* to testing ([`PREDICTION.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/PREDICTION.json#L1-L13)).
   - Visiting only the 53 unattempted items under a strict budget (20 CPU seconds, 16 accepts cap) is a well-disciplined finite continuation.
   - It avoids repeating failed configurations while leveraging the already-loaded host structure to extract any additional legal extensions.

---

### 4. Review Verdict and Criteria for Subsequent Inductive Steps

#### **Verdict: ACCEPT**
The graph $G_{51418}$ is an accepted, fully verified graph proving $N(13,5) \ge 51418$ under the inherited base diameter $D \le 5$.

#### **Acceptance Criteria for Future Same-Rule Steps ($G_k \to G_{k+1}$)**:
For any subsequent single-vertex extension under this rule to be accepted without paid reviewer re-engagement or re-running full-graph all-pairs BFS:
1. **Edge Monotonicity**: $E_{current} \subset E_{next}$. No previously existing edge may be deleted or redirected.
2. **Degree Validity**: For every chosen pin $p \in N(z_{new})$, $deg_{G_{current}}(p) < 13$, and $|N(z_{new})| \le 13$.
3. **Full Current $R_4$ Coverage**: The chosen pin set must achieve complete coverage of all vertices of $G_{current}$ within radius 4 in $G_{current}$ (missing count $= 0$), computed against the exact current adjacency.
4. **Independent Root BFS**: An independent verification script must parse the literal new edge list, confirm edge retention against the prior accepted graph, and execute a BFS from the newly added vertex to verify that its eccentricity is $\le 5$.
5. **Formalization Distinction**: The goal status remains `ACTIVE`, and Lean instances remain `0`. Inductive acceptance must not be reported as a Lean certificate.

