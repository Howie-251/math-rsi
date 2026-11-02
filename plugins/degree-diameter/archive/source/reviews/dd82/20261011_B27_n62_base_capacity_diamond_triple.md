# B27 — heavy base, strict triangle capacity, diamond trace, and triple geometry

### Review Metadata and Execution Scope

- **CLI-selected model & reasoning effort**: `gemini-3.8-flash-high` / `high` (preserves CLI configuration metadata; distinct from backend attestation).
- **Execution disclosure**: **0 executions performed by the reviewer.** No shell commands, build commands, or scripts were executed during this review. All referenced build outputs and axiom logs pre-existed in the workspace.
- **Reading scope**:
  - **Read in full**:
    - [`proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_BASE_NEAR_EXTREMAL_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_BASE_NEAR_EXTREMAL_EXCLUSION.md) (all 283 lines).
    - [`proofs/dd82/n62/CONNECTED_REPEAT_STRICT_TRIANGLE_CAPACITY.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_STRICT_TRIANGLE_CAPACITY.md) (all 66 lines).
    - [`proofs/dd82/n62/CONNECTED_REPEAT_DIAMOND_TRACE_REFINEMENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_DIAMOND_TRACE_REFINEMENT.md) (all 101 lines).
    - [`formal/DegreeDiameter/N62TripleRepeat.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62TripleRepeat.lean) (all 275 lines).
    - [`formal/ReviewN62TripleRepeat.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62TripleRepeat.lean) (all 57 lines).
    - [`formal/N62_TRIPLE_REPEAT_HANDOFF.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/N62_TRIPLE_REPEAT_HANDOFF.md) (all 40 lines).
    - [`formal/logs/n62-triple-repeat-second.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-repeat-second.log) (all 34 lines).
    - [`formal/logs/n62-triple-repeat-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-repeat-type-axiom-audit.log) (all 101 lines).
  - **Consulted as provisional context**:
    - [`reviews/dd82/proof-checker-n62-base-seventeen-20261011/PROOF_AUDIT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/reviews/dd82/proof-checker-n62-base-seventeen-20261011/PROOF_AUDIT.md).
    - [`reviews/dd82/proof-checker-n62-heavy-original-20261011/STRICT_CAPACITY_DELTA_AUDIT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/reviews/dd82/proof-checker-n62-heavy-original-20261011/STRICT_CAPACITY_DELTA_AUDIT.md).
    - [`reviews/dd82/proof-checker-n62-heavy-original-20261011/DIAMOND_TRACE_DELTA_AUDIT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/reviews/dd82/proof-checker-n62-heavy-original-20261011/DIAMOND_TRACE_DELTA_AUDIT.md).
- **Prose boundary corrections preserved**:
  1. $\operatorname{codegree} \le 1$ in $G[D]$ applies specifically to nonmate *heavy* pairs in $D$.
  2. Generated triangles lie in $S \subseteq U$, while the heavy unit mates $L$ lie *outside* every unit repeat triangle.
  3. The port multigraph in `CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md` places edges between the two light mates of each heavy pair.
  4. The values $0, 3, 6, 11, 17$ are pointwise upper bounds on $m = |E(F)|$, not an exact spectrum of realizable values.
  5. Equality in the squared-degree bound implies regularity for every component of $F$; the $d=5$ contradiction arises from the isolated degree-2 vertex in the multiset $\{3, 3, 3, 3, 2\}$.
  6. Base separation in the distance lemma applies to distinct pair indices $i \ne j$.

---

### Part A: Review of `CONNECTED_REPEAT_HEAVY_BASE_NEAR_EXTREMAL_EXCLUSION.md`

#### 1. Three Short-Cycle Obstructions on Simple Signed Base $F$
- **Codegree $\le 2$ (Section 1.1)**: If base vertices $i, j$ have three distinct common neighbors $x, y, z$, the three length-2 paths $i-x-j$, $i-y-j$, $i-z-j$ take signs in $\{+1, -1\}$. By pigeonhole, two must share the same sign, so their union forms a 4-cycle of positive sign product $(+1)(+1) = +1$ or $(-1)(-1) = +1$. But every 4-cycle in $F$ must have sign product $-1$ to prevent lifting to an original $C_4$ in $G[D]$. Hence codegree in $F$ is at most 2.
- **Edge in $\le 1$ triangle (Section 1.2)**: If an edge $ij$ belonged to two triangles with third vertices $u, v$, each triangle has sign product $-1$. The 4-cycle $i-u-j-v-i$ has sign product $\frac{\sigma(iju)\sigma(ijv)}{\sigma(ij)^2} = \frac{(-1)(-1)}{1} = +1$, which is forbidden. Thus adjacent pairs have codegree at most 1, all triangles are edge-disjoint, $a = m - 3t$, and $a_i = r_i - 2t_i$. Since $r_i \le 4$, every base vertex belongs to at most 2 triangles.
- **Forbidden triangular prism (Section 1.3)**: If $F$ contains two vertex-disjoint triangles $A=\{a_1, a_2, a_3\}$ and $B=\{b_1, b_2, b_3\}$ connected by matching edges $a_i b_i$ ($i=1,2,3$), the three 4-cycles $a_1 a_2 b_2 b_1$, $a_2 a_3 b_3 b_2$, $a_3 a_1 b_1 b_3$ all have sign $-1$, so their product is $(-1)^3 = -1$. Multiplying the cycle signs cancels each matching edge twice and leaves $\sigma(A)\sigma(B) = (-1)(-1) = +1$, yielding the contradiction $-1 = +1$. This obstruction is valid for any subgraph (no inducedness required).

#### 2. Exact Local Degree Identity
- Defining $\varepsilon_i = 2d - 2 - \sum_{j \sim i} r_j$, the sum of 2-paths from $i$ decomposes over endpoints:
  - $r_i - a_i$ adjacent vertices have codegree 1; $a_i$ adjacent vertices have codegree 0.
  - $b_i$ nonadjacent vertices have codegree 1; $c_i$ nonadjacent vertices have codegree 0; the remaining $d - 1 - r_i - b_i - c_i$ nonadjacent vertices have codegree 2.
  $$\sum_{j \sim i} (r_j - 1) = (r_i - a_i) + b_i + 2(d - 1 - r_i - b_i - c_i) = 2d - 2 - r_i - a_i - b_i - 2c_i.$$
  Adding $r_i$ yields $\varepsilon_i = a_i + b_i + 2c_i$.
  Summing over all vertices gives $2d(d-1) - \sum_i r_i^2 = 2(a + b + 2c)$.

#### 3. Exclusion of Seventeen Edges at $d=9$
- If $d=9, m=17$, then $\sum r_i = 34$ with $r_i \le 4$. The only degree multisets are:
  - **Pattern A**: $\{4^7, 3^2\} \implies \sum r_i^2 = 130 \implies a + b + 2c = 7$.
  - **Pattern B**: $\{4^8, 2^1\} \implies \sum r_i^2 = 132 \implies a + b + 2c = 6$.
  With $a = 17 - 3t \ge 0$, both patterns force $t \in \{4, 5\}$.
- **Five triangles force the forbidden prism (Section 4)**:
  The triangle-intersection graph $I$ (vertices = triangles, edges = shared base vertices) is triangle-free, because three intersecting triangles sharing one vertex would require vertex degree $\ge 6 > 4$, while sharing three distinct vertices would form an extra base triangle sharing edges with all three (violating Section 1.2).
  For $t=5$, $v_\triangle = 15 - |E(I)| \le 9 \implies |E(I)| \ge 6$. The unique triangle-free graph on 5 vertices with $\ge 6$ edges is $K_{2,3}$. Its two nonadjacent degree-3 vertices correspond to disjoint triangles $A, B$, and the three bipartite neighbors supply the three disjoint matching edges $a_i b_i$. This is exactly the forbidden triangular prism. Thus $t=5$ is impossible, forcing $t=4$ and $a = 5$.
- **Pattern B contradiction (Section 5)**:
  For the unique degree-2 vertex $z$, $\varepsilon_z = 16 - (4+4) = 8$. But $a=5$ and $a+b+2c=6$ force $b=1, c=0$. Then $\varepsilon_z = a_z + b_z \le r_z + b = 2 + 1 = 3 < 8$, a contradiction.
- **Pattern A contradiction (Section 6)**:
  Let $u, v$ be the two degree-3 vertices, $k = \mathbf{1}_{u \sim v}$. Then $\varepsilon_z = 4+k$, and $a_z = 3 - 2t_z$ gives $b_z + 2c_z = 1 + k + 2t_z$. Since $a=5$ and $a+b+2c=7$, we have $b+2c=2$:
  - If $b=2, c=0$: $b_z = 1 + k + 2t_z$. If $k=1$, $b_u + b_v \ge 4$, but the two nonedges cannot be $\{u, v\}$ and can supply at most 2 incidences to $\{u, v\}$. Thus $k=0$. This forces $t_u = t_v = 0$. All 4 triangles must lie on the remaining 7 degree-4 vertices. But a triangle-free graph on 4 vertices has $|E(I)| \le 4$, so 4 triangles must cover at least $12 - 4 = 8 > 7$ vertices, contradiction.
  - If $b=0, c=1$: $2c_z = 1 + k + 2t_z$. Parity forces $k=1, t_z=0, c_z=1$. The unique codegree-0 nonedge must be incident to both $u$ and $v$, forcing it to be $\{u, v\}$, contradicting $k=1$ ($u \sim v$).
- **Conclusion**: Both patterns are excluded analytically without graph enumeration. Thus $|E(F)| \le 16$, and $|E(G[D])| \le 32$.
- **Incidences**: Heavy endpoints have $144 - 4m \ge 80$ edges into $V \setminus D$. Subtracting the 54 edges to their own generated triangles leaves $\ge 26$ original incidences going to $W$ or other generated triangles. The paper correctly qualifies that *all* 26 incidences go to $W$ only if $\operatorname{diam}(F) \le 2$.
- **Verdict for Item A: PASS (Provable as stated).**

---

### Part B: Review of `CONNECTED_REPEAT_STRICT_TRIANGLE_CAPACITY.md`

#### 1. Strict Capacity Bound
- Let $R = V \setminus (D \cup U \cup C_1)$, where $|U| = 3d + v_{\text{extra}}$ and $c_{\text{out}} = |C_1 \setminus U|$.
- Then $|R| = 62 - 5d - v_{\text{extra}} - c_{\text{out}}$.
- All $2d$ unit repeat incidences from $D$ terminate in $R$, so $\sum_{w \in R} \ell(w) = 2d$.
- Since $\ell(w) \le 3$, we have $2d \le 3|R|$.
- If equality $2d = 3|R|$ held, every $w \in R$ would have $\ell(w) = 3$. Then $Z = D \cup R$ would be a closed component of positive repeat support:
  - Every $u \in D$ has its heavy mate in $D$ and its unit mate in $R$.
  - Every $w \in R$ has all 3 repeat neighbors in $D$.
  $Z$ is nonempty ($d \ge 1$) and proper (omits the $3d$ vertices of generated triangles in $S \subseteq U$). This directly contradicts connectedness of repeat support. (Equivalently, it contradicts $3L_3 < 2d$ from `CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md`).
- Thus $2d < 3|R| = 3(62 - 5d - v_{\text{extra}} - c_{\text{out}}) \implies 17d + 3v_{\text{extra}} + 3c_{\text{out}} < 186$.

#### 2. Boundaries and Scope
- For $d=9$: $153 + 3(v_{\text{extra}} + c_{\text{out}}) < 186 \implies v_{\text{extra}} + c_{\text{out}} \le 10$.
- The previously analyzed boundary $v_{\text{extra}} = 11$ is impossible (vacuous antecedent).
- At $v_{\text{extra}} = 10$, $c_{\text{out}} = 0$. The cluster partition $3s + 4k = 10$ uniquely forces $s=2, k=1$, meaning exactly four nongenerated unit triangles (two isolated triangles and one diamond).
- **Verdict for Item B: PASS (Provable as stated).**

---

### Part C: Review of `CONNECTED_REPEAT_DIAMOND_TRACE_REFINEMENT.md`

#### 1. Pointwise Shared-Endpoint Penalty
- In a unit diamond with shared-edge endpoints $x, y$ and tips $z, w$, repeat rows satisfy $B_x = B_y = e_{\text{shared}} + e_z + e_w$. Since positive repeat pairs are original nonedges, $m(x) = m(y) = A_{zw} \le 1$.
- If either diamond triangle has type 1, the adjacent-tip lemma (`TRIANGLE_WITNESS_REFINEMENT.md`, Section 6) forces $A_{zw} = 0 \implies m(x) = m(y) = 0$.
- Shared endpoints have $\ell = 0$ (they lie in a unit triangle).
  - A center in $C_1$ has $m = 0$ and is already deducted in the $+4t_1$ penalty; $H \setminus C_1$ explicitly excludes centers to prevent double counting.
  - A vertex in $(H \cap U_1) \setminus C_1$ previously received a penalty of 1 (from $m \le 1$); since $m = 0$, it gains an additional 1.
  - A vertex in $H \setminus (U_1 \cup C_1)$ previously had $m \le 2$; since $m \le 1$, it gains an additional 1.
- In all cases, each vertex in $H \setminus C_1$ yields an additional $+1$ saving in $m(w)$, which translates to $+2|H \setminus C_1|$ in $\tau = 2\sum m(w)$:
  $$\tau + 4t_1 + 2|U_1 \setminus C_1| + 2|H \setminus C_1| \le 248 - 24d + 2L_3.$$

#### 2. The $d=9, v_{\text{extra}}=10$ Boundary Contradiction
- Strict capacity gives $c_{\text{out}} = 0$ and nongenerated clusters $2K_3 + \text{Diamond}$ (4 triangles on 10 vertices).
- If all 4 triangles are type 1:
  - The center graph $\Gamma$ has 4 vertices and no isolates ($c_{\text{out}} = 0$). Permitted components are $K_1, K_2, P_3, P_4$. Since $P_4$ requires two diamonds and only one exists, $\Gamma \cong 2K_2$.
  - All 4 centers lie in $U_1$, giving $|U_1 \setminus C_1| = 10 - 4 = 6$.
  - A shared diamond endpoint cannot be a center (it belongs to two type-1 triangles, which would give degree 2 in $\Gamma$, but $\Gamma \cong 2K_2$ is 1-regular). Thus $H \cap C_1 = \emptyset \implies |H \setminus C_1| = 2$.
  - With $L_3 \le 5$, the bound gives $\tau + 16 + 12 + 4 \le 248 - 216 + 10 = 42 \implies \tau \le 10$.
  - But total unit triangles $u = 9 + 4 = 13$ is odd, so $C_5 \equiv u \equiv 1 \pmod 2$.
  - Within $2498 \le C_5 \le 2501$, the odd values are $2499$ and $2501$, giving $\tau = 10C_5 - 24976 \in \{14, 34\}$. Both contradict $\tau \le 10$.
- Hence, at the boundary $d=9, v_{\text{extra}}=10$, at least one nongenerated triangle must have type 0.
- **Verdict for Item C: PASS (Provable as stated).**

---

### Part D: Formal Review of `N62TripleRepeat.lean`

#### 1. Implementation and Mathematical Coverage
- **Source**: [`formal/DegreeDiameter/N62TripleRepeat.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62TripleRepeat.lean) (275 lines).
- **Hypotheses**: Original graph $G$ with `degreeAtMostEight G`, `diameterAtMostTwo G`, `Fintype.card V = 62`, and an actual defect entry `defectMatrix G u v = 3`.
  - No supplied root certificate or row pattern assumed.
  - No global $B \le 2$ or full triple elimination assumed.
- **Formalized Steps (RECOVERED_REDUCTION Steps 1–2)**:
  1. `n62_triple_repeat_rows`: Saturated rows $B_u = 3e_v$ and $B_v = 3e_u$.
  2. `n62_triple_repeat_nonadj`: Endpoints are distinct and non-adjacent in $G$.
  3. `n62_triple_endpoint_zero_triangle`: Both endpoints are triangle-free in $G$.
  4. `n62_triple_common_card`: Common neighbor set $S = \operatorname{CN}(u, v)$ has $|S| = 4$.
  5. `n62_triple_common_nonadj`: $S$ is an independent set in $G$.
  6. `n62_triple_common_rows`: For each $x \in S$, $B_x = \mathbf{1}_{S \setminus \{x\}}$. Block $B[S] = J_4 - I_4$ and no repeat edges leave $S$.
  7. `n62_triple_common_pair_neighbors`: For distinct $x, y \in S$, $\operatorname{CN}(x, y) = \{u, v\}$.
  8. `n62_triple_outside_common_neighbors_unique`: Vertices outside $\{u, v\}$ have at most one neighbor in $S$.
  9. `n62_triple_pair_component`: Support component of $u$ is exactly $\{u, v\}$.
  10. `n62_triple_common_component`: Support component of each $x \in S$ is exactly $S$.
  11. `n62_triple_component_sizes`: Constructs actual support components of sizes 2 and 4.
  12. `mem_commonNeighborVertices`: Definitional membership API for common neighbors.

#### 2. Axiom and Build Audit
- **Axioms**: The audit log [`formal/logs/n62-triple-repeat-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-repeat-type-axiom-audit.log) verifies that all 12 public declarations depend solely on the standard Lean 4 axioms:
  `[propext, Classical.choice, Quot.sound]`.
  No `sorry`, no unproven axioms, and no `native_decide` are present.
- **Example Callers**: All 3 original-input callers in [`formal/ReviewN62TripleRepeat.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62TripleRepeat.lean) compile and pass with exit 0.
- **Build Status**: Verified via pre-existing log [`formal/logs/n62-triple-repeat-second.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-triple-repeat-second.log) (exit 0, 1798 jobs, 16s).
- **Verdict for Item D: PASS (Complete and verified).**

---

### Summary of Scoped Verdicts

| Item | Artifact | Scope | Verdict |
|---|---|---|---|
| **A** | `CONNECTED_REPEAT_HEAVY_BASE_NEAR_EXTREMAL_EXCLUSION.md` | Excludes $m=17$ for $d=9$, showing $m \le 16$ and $\|E_G(D)\| \le 32$ | **PASS** |
| **B** | `CONNECTED_REPEAT_STRICT_TRIANGLE_CAPACITY.md` | Proves $17d + 3v_{\text{extra}} + 3c_{\text{out}} < 186$; at $d=9$, $v_{\text{extra}} + c_{\text{out}} \le 10$ | **PASS** |
| **C** | `CONNECTED_REPEAT_DIAMOND_TRACE_REFINEMENT.md` | Adds $+2\|H \setminus C_1\|$ penalty; proves type-0 exists at $d=9, v_{\text{extra}}=10$ boundary | **PASS** |
| **D** | `formal/DegreeDiameter/N62TripleRepeat.lean` | Lean 4 formalization of RECOVERED_REDUCTION Steps 1–2 (size 2 & 4 components) | **PASS** |

*Global Scope Confirmation*: No claim of full order-62 nonexistence, exact $N(8,2)$ bound, or exclusion of any remaining value of $d \in \{1, 3, 5, 7, 9\}$ is made. Known 63–65 work remains stopped.


## Executor disposition

All four source scopes accepted; no source repair required. The review inspected pre-existing execution logs and ran no programs. Metadata is requested/CLI-selected model information, not independent backend attestation.

Two shorthand expressions in the review are not adopted literally: in Part B, D union R is a nonempty proper closed set, potentially a union of components, which is enough for the contradiction; in Part C the precise rows are B_x=e_y+e_z+e_w and B_y=e_x+e_z+e_w, not equal vectors. The source proofs use these correct statements. No additional type-zero existence outside the specified d9,v_extra10 boundary, d exclusion, whole62 exclusion, or exact N8 result is inferred.

