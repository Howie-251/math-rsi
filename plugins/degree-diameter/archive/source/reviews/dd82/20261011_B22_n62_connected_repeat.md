# B22 Antigravity review: connected actual repeat support

Requested and CLI-selected model: `gemini-3.8-flash-high`, effort `high`. This records CLI metadata, not independent backend attestation. Review used the already authorized Google MCP path. Reviewer executed no code; local executions and independent checker receipts are separate evidence.

### Metadata & Environment

- **Model**: Gemini 3.8 Flash (High), reasoning effort `high`.
- **Execution & modification status**: Zero shell commands executed, zero files created or modified. All review verdicts are based strictly on static source reading and independent mathematical verification.
- **Reading scope disclosure**:
  - **Fully read sources**:
    - [`CONNECTED_REPEAT_REDUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_REDUCTION.md) (all 194 lines)
    - [`FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md) (all 180 lines)
    - [`THREE_COMPONENT_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_EXCLUSION.md) (all 206 lines)
    - [`component_quotient_search.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotient_search.py) (all 140 lines)
    - [`component_quotients_5.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotients_5.json) (all 83 lines)
    - [`component_quotients_7.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotients_7.json) (all 106 lines)
    - [`component_quotients_9.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotients_9.json) (all 30 lines)
    - [`check_three_component_quotients.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/check_three_component_quotients.py) (all 130 lines)
    - [`three_component_quotients_check.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/three_component_quotients_check.json) (all 100 lines)
    - [`check_large_component_quotients.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/check_large_component_quotients.py) (all 272 lines)
    - [`large_component_quotients_check.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/large_component_quotients_check.json) (all 201 lines)
  - **Partially read / inspected predecessor sources**:
    - [`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md) (Sections 2–5)
    - [`D1_MATCH_HARD_BRANCH_REDUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_MATCH_HARD_BRANCH_REDUCTION.md) (Sections 1–2)
    - [`D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md) (Sections 1–2)
    - [`TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md) (Sections 1–4)

---

### Audit of the Five Key Obligations

#### 1. Integration of Widened $c=3$ Domain ($n_i \ge 2$) and Replacement of $|H| \ge 14$

- **Domain widening to $n_i \ge 2$**:
  In [`check_three_component_quotients.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/check_three_component_quotients.py#L58-L59), the size constraint is relaxed from $n_i \ge 4$ to any positive even integer $n_i \ge 2$. Across all 9,108 trace-7 matrices formed from 45 nonnegative integer triples summing to 8, exactly 18 labelled matrices survive in the same 3 canonical orbits: $(6,24,32)$, $(8,24,30)$, and $(12,20,30)$.
- **Local impossibility of $B=3$**:
  A triple repeat $B_{uv}=3$ exhausts the row sum 3 of both endpoints, forcing $\{u,v\}$ to be an isolated repeat component of size 2. Because no surviving quotient has $n_i=2$, triple repeats cannot occur in any actual graph realization of these quotients. Hence $B \le 2$ holds locally without invoking global triple-repeat exclusion.
- **Direct D1 quotient incidence replaces $|H| \ge 14$ in the 12-case**:
  In [`THREE_COMPONENT_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_EXCLUSION.md#L146-L149), if the 12-point component $C$ contains a D1 heavy pair, its partner $K$ must satisfy $r_{CC} \ge 4$ (if $K=C$), $r_{CD} \ge 4$ (if $K=D$), or $r_{CE} \ge 4 \land r_{EC} \ge 3$ (if $K=E$). In the candidate quotient:
  $$r_{CC} = 3 < 4, \quad r_{CD} = 0 < 4, \quad r_{EC} = 2 < 3.$$
  All three choices are directly contradicted by the quotient entries. Thus $B_C$ is simple without using the $|H| \ge 14$ lower-bound chain.
- **Dependencies retained**: Triangle pairing (ruling out triangles since $n_i \ne 6$), D0 component closure in size 4 (ruling out D0 since $n_i \ne 4$), and the spectral trace-polynomial contradiction on the connected cubic graph $P$.

#### 2. Bound $c \le 9$ (Odd) in `CONNECTED_REPEAT_REDUCTION.md`

- **Global dependencies used**:
  Unlike the isolated $c=3$ exclusion, bounding the total component count $c$ uses global triple-repeat elimination ($B \le 2$), odd-double parity giving $d_1 \ge 1$ (existence of at least one D1 pair), and the size lower bounds $|H|, |K| \ge 14$ from [`D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md).
- **Branch analysis**:
  From $c + 2\operatorname{tr}(R) = 17$, $c$ is odd.
  - *If $H = K$*: The heavy component has internal degree $r_{HH} \ge 4$. Thus $\operatorname{tr}(R) \ge 4$, giving $c = 17 - 2\operatorname{tr}(R) \le 17 - 8 = 9$.
  - *If $H \ne K$*: Both components have size $\ge 14$, consuming $\ge 28$ vertices. Under $B \le 2$, the remaining $c-2$ components have even size $\ge 4$. The vertex packing bound is:
    $$28 + 4(c - 2) \le 62 \implies 4(c - 2) \le 34 \implies c - 2 \le 8.5 \implies c \le 10.$$
    Because $c$ is odd, $c \le 10$ implies $c \le 9$.
  - With $c \in \{1, 3, 5, 7, 9\}$ and $c=3$ excluded, $c \in \{1, 5, 7, 9\}$.

#### 3. Large Quotient Generator Coverage & Semantics ($c=5, 7, 9$)

- **Generator design ([`component_quotient_search.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotient_search.py#L28-L52))**:
  - Partitions of 62 into $k$ even parts $\ge 4$: 221 (for $k=5$), 201 (for $k=7$), 94 (for $k=9$).
  - Off-diagonal entries are parametrized via $g_{ij} = \gcd(n_i, n_j)$: $r_{ij} = (n_j/g_{ij})t_{ij}$ and $r_{ji} = (n_i/g_{ij})t_{ij}$, enforcing exact edge balance.
  - The diagonal entry $r_{ii} = 8 - \sum_{j \ne i} r_{ij}$ is constrained by $r_{ii} \le \text{trace}$, $r_{ii} < n_i$ (simple graph), and the diagonal quadratic identity:
    $$r_{ii}^2 + r_{ii} + \sum_{j \ne i} r_{ij} r_{ji} = n_i + 10.$$
  - Backtracking checks compatibility between assigned row $i$ and previously assigned row $j$:
    $$\sum_{z=1}^k r_{iz} r_{zj} + r_{ij} = n_j \quad \text{and} \quad \sum_{z=1}^k r_{jz} r_{zi} + r_{ji} = n_i.$$
    Both ordered off-diagonal identities are tested.
- **Completeness and execution confirmation**:
  In [`component_quotients_5.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotients_5.json), [`.7.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotients_7.json), and [`.9.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotients_9.json), all partitions finished (`size_partitions_completed == size_partitions_total`, wall time $< 1.5$s total, no timeout).
  The independent checker [`check_large_component_quotients.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/check_large_component_quotients.py) generated rows via weak compositions (stars and bars), checked forward filtering, verified all 3,358 row domains, and reproduced:
  - $c=5$: 2 labelled solutions $\to$ 1 canonical quotient ($n = (4,8,10,20,20)$);
  - $c=7$: 6 labelled solutions $\to$ 1 canonical quotient ($n = (4,4,4,10,10,10,20)$);
  - $c=9$: 0 solutions.

#### 4. The Uniform Lemma & Exclusion of Surviving 5- and 7-Quotients

- **Uniform lemma proof ([`FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md#L78-L121))**:
  Let $C$ be a 4-vertex component of $B$ with internal original edge $uv \in E(G)$.
  1. *Triangle-free*: If any vertex in $C$ were in an original triangle, triangle pairing would place it in a closed 6-vertex component, forcing $|C|=6 \ne 4$. Hence $C$ is triangle-free.
  2. *Edge repeat is zero*: Triangle-freeness forces $c_G(u,v)=0$, so $c_G(u,v)+A_{uv}=1+B_{uv} \implies 0+1=1+B_{uv} \implies B_{uv}=0$.
  3. *Double repeat in $C$*: The repeat row sum at $u$ on the remaining two vertices $x, y \in C$ is $B_{ux}+B_{uy}=3$. Under $B \le 2$, one entry is 2 and one is 1. Thus $C$ contains a double repeat.
  4. *Double repeat is D0*: A D1 heavy component contains at least 6 distinct vertices: heavy endpoints $0, w$, light mate $a$, and endpoints $r, p, q$ from [`D1_MATCH_HARD_BRANCH_REDUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_MATCH_HARD_BRANCH_REDUCTION.md#L41-L68). Since $|C|=4 < 6$, the double repeat cannot be D1. It is therefore D0.
  5. *Companion prism of size 6*: By [`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md#L99-L133) Section 2, every D0 component has a companion 6-vertex independent unit prism.
- **Application**:
  - The $c=5$ quotient has $n=(4,8,10,20,20)$ with internal degrees $(1,2,0,2,1)$. Component 1 has size 4 and degree 1, forcing a 6-vertex component. No component has size 6. Contradiction.
  - The $c=7$ quotient has $n=(4,4,4,10,10,10,20)$ with internal degrees $(1,1,1,0,0,0,2)$. Components 1, 2, 3 have size 4 and degree 1, forcing a 6-vertex component. No component has size 6. Contradiction.
  Both quotients are excluded. Combined with $c=9$ having 0 quotients, $c \in \{5, 7, 9\}$ is impossible. Hence $c=1$.

#### 5. Consequences of $c=1$ (Connected Repeat Support)

In [`CONNECTED_REPEAT_REDUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_REDUCTION.md#L152-L185):
1. **$G$ is triangle-free ($T=0$)**: Original triangles require 6-vertex components; here $|C|=62 \ne 6$.
2. **No D0 double repeats ($d_0=0$)**: D0 doubles require 4-vertex components; here $|C|=62 \ne 4$.
3. **All doubles are D1 ($d_1=d$)**: Since all doubles are D0 or D1, all $d$ doubles are D1.
4. **Range of $d$**:
   Global port bound $15d + 9T + 2d_1 \le 186$ with $T=0$ and $d_1=d$ gives:
   $$17d \le 186 \implies d \le 10.$$
   Odd-double parity forces $d$ to be odd, so:
   $$d \in \{1, 3, 5, 7, 9\}.$$
5. **Exact unit repeat count**:
   Total row sum is $62 \times 3 = 186$, so the total sum of unordered repeat pairs is 93. Double pairs consume $2d$, leaving:
   $$\text{unit repeat pairs} = 93 - 2d.$$
6. **Exact $C_4$ count**:
   Because $G$ is triangle-free, adjacent vertices have 0 common neighbors ($c_G = 0$), nonadjacent unit pairs have $c_G = 2$ ($\binom{2}{2} = 1$ common 4-cycle path), nonadjacent double pairs have $c_G = 3$ ($\binom{3}{2} = 3$ common 4-cycle paths), and non-repeat nonedges have $c_G = 1$ ($\binom{1}{2} = 0$).
   Each 4-cycle contains 2 pairs of opposite vertices. Thus:
   $$\text{Number of } C_4 = \frac{1 \cdot (93 - 2d) + 3 \cdot d}{2} = \frac{93 + d}{2}.$$
   For $d \in \{1, 3, 5, 7, 9\}$, $(93+d)/2 \in \{47, 48, 49, 50, 51\}$, which are integers because $93+d$ is even.

---

### Separate Audit Verdicts

1. **Widened Domain & $c=3$ Integration ([`THREE_COMPONENT_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_EXCLUSION.md))**:
   **VERDICT: PASS.** Allowing $n_i \ge 2$ preserves the 3 canonical quotients. Absence of size 2 establishes local $B \le 2$. Direct D1 quotient bounds rigorously replace the $|H| \ge 14$ dependency in the 12-case.
2. **Large Quotient Encoding & Search Coverage ([`component_quotient_search.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/component_quotient_search.py), [`check_large_component_quotients.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/check_large_component_quotients.py))**:
   **VERDICT: PASS (as exhaustive integer quotient diagnostic).** Parameterization via gcd, off-diagonal dual identities, and diagonal quadratic constraints are mathematically complete. Independent stars-and-bars reproduction completed all partitions without truncation.
3. **Uniform Lemma & 5/7 Exclusions ([`FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md))**:
   **VERDICT: PASS.** Triangle-free 4-vertex component with an edge forces a double repeat; 4 vertices cannot fit the 6 distinct vertices of D1, forcing D0_EDGE_BOUT and its companion 6-vertex prism. This rules out the $c=5$ and $c=7$ survivors.
4. **Full Connectedness Integration & Corollaries ([`CONNECTED_REPEAT_REDUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_REDUCTION.md))**:
   **VERDICT: PASS.** The chain successfully proves that any surviving order-62 graph has **connected repeat support ($c=1$)**. The corollaries $T=0$, $d_0=0$, all doubles D1, $d \in \{1, 3, 5, 7, 9\}$, and $C_4 \in \{47, 48, 49, 50, 51\}$ follow rigorously.

### Mathematical Boundary & Non-Claims

- **Retained dependencies**: The global reduction to $c=1$ genuinely retains the triple-repeat elimination and the $|H|, |K| \ge 14$ minsize chain (used to obtain $c \le 9$).
- **Unit triangles**: Not all unit repeat triangles in $B$ are asserted to be generated by D1 pairs.
- **External computation**: The finite quotient classifications ($c=3, 5, 7, 9$) are verified external integer computations, not Lean formal proofs.
- **Order-62 status**: This establishes connectedness of positive repeat support as a structural necessity for any hypothetical order-62 graph; it does **not** assert nonexistence at order 62 or resolve the exact $N(8,2)$ problem.


## Executor disposition

Accepted the four scoped paper/code-review verdicts. Connectedness relies on the retained global triple-repeat elimination, D1 existence and both-component minimum-size chain; finite quotient classifications are external exact computations, not Lean certificates. The c=3-only reduction uses its widened positive-even size domain and direct quotient incidence, avoiding those two global imports where stated. No full order-62 exclusion and no exact N(8,2) determination is claimed. In the local four-point lemma the presence of an original edge selects D0_EDGE_BOUT before invoking its companion six-component result; do not generalize that companion statement to arbitrary unexamined D0 variants.

