threadId: 8e21bc5e-56e9-40d6-83d0-82896e24229b

### 1. Inspection and Execution Record

- **Files Read in Full**:
  1. [`proofs/dd82/n59/seven_triangles_twenty_core_exclusion_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/seven_triangles_twenty_core_exclusion_20261011.md)
  2. [`proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md)
  3. Predecessor dependencies examined: [`proofs/dd82/n59/zero_heavy_global_capacity_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/zero_heavy_global_capacity_20261011.md), [`proofs/dd82/n59/nonzero_support_transport_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/nonzero_support_transport_20261011.md), [`proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md).
- **Commands Executed**: **Zero**. No subprocesses, shell commands, Lake builds, or solver runs were executed by the reviewer. Build logs, test executions, and proof scripts were inspected strictly as static artifacts.
- **Model and Effort Metadata**: Gemini 3.8 Flash (High), reasoning effort `high`.
- **Baseline Alignment**: No work on known orders 63–65 was requested or performed. Analysis is restricted strictly to unresolved orders 58–62.

---

### 2. Independent Mathematical Review: Exclusion of $T=7, m=20$

The paper [`seven_triangles_twenty_core_exclusion_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/seven_triangles_twenty_core_exclusion_20261011.md) completely eliminates the equality case $T = 7, m = 20$ of the global heavy capacity theorem $59 \le 4m - 3T$.

#### Adversarial Derivation Check
1. **Vanishing Nonedge Defect in $N$ ($B_{ny} = 0$)**:
   - At equality $4m - 3T - 59 = 0$, every pointwise slack term in the exact capacity identity vanishes:
     $$B_{ny} = \binom{q}{2} + \mathbf{1}_{\{y \in Z, B_{ny} = 2\}}$$
     where $q = |N_G(n) \cap N_G(y) \cap Z| \le 2$.
   - For nonadjacent $n, y \in N$, the indicator vanishes, so $B_{ny} = \binom{q}{2} \in \{0, 1\}$.
   - If $B_{ny} = 1$, then $q = 2$, yielding two zero common neighbors $z, w \in Z$. The pair $\{z, w\}$ is independent in $G$ and shares common neighbors $n, y \in N$, so $B_{zw} \ge 2 - 1 = 1$.
     - If $B_{zw} = 1$, $n \in N$ is a nonzero common neighbor of a light zero defect edge, violating the equality fact $\sum \ell_n = 0$.
     - If $B_{zw} = 2$, $n, y \in N$ are two nonzero common neighbors of a heavy zero defect edge, violating the equality fact $D = \sum h_n - H_{ZZ} = 0$.
   - Thus $B_{ny} = 0$ for all nonedges $\{n, y\} \subseteq N$.

2. **Triangle Support and Transport**:
   - $3T = 21$ incidences on $m = 20$ vertices forces exactly one vertex $v_0 \in N$ with $t(v_0) = 2$ and 19 vertices with $t(v) = 1$. The triangles sharing $v_0$ share only $v_0$; all other triangles are disjoint.
   - For any $v \in N$ with $t(v) = 1$, its nonzero positive defect support consists solely of its two adjacent triangle partners $a, b$, each with weight 1.
   - Transport identity $(BA)_{xv} = B_{vx}$ at zero vertex $x$ shows that if $v$ has nonedge repeats $\{x, y\} \subset Z$ of weight 2, then $x \sim y$ in $G$.

3. **Exclusion of Heavy Cross Repeats ($B_{nz} \ne 2$)**:
   - Suppose $u \in N, z \in Z$ with $B_{uz} = 2$. By the equality fact, $q = 2$, so $u, z$ have two zero common neighbors $x, y$ and one nonzero common neighbor $v \in N$.
   - $v, x$ have common neighbors $u \in N$ and $z \in Z$, and are nonadjacent (otherwise $u, v, x$ would be a triangle at $x \in Z$). Thus $B_{vx} \ge 1$.
     - If $B_{vx} = 1$, the equality fact forces $v, x$ to have no nonzero common neighbor, contradicting common neighbor $u \in N$.
     - Hence $B_{vx} = 2$, and similarly $B_{vy} = 2$.
   - Nonedge budget at $v \in N$ is $6 - 2t(v) \le 4$. The entries $B_{vx} = B_{vy} = 2$ consume all 4 units, forcing $t(v) = 1$.
   - Transport forces $x \sim y$. But $x$ and $y$ are both adjacent to $u \in N$, creating a triangle $u, x, y$ containing zero vertices. Contradiction.
   - Hence **no heavy defect edge exists between $N$ and $Z$**.

4. **Fourth-Trace Contradiction**:
   - Every nonzero root has only unit positive entries (triangle edges have weight 1, nonedges in $N$ have weight 0, and nonedges to $Z$ have weight $\le 1$). Row sum is 6, so row square sum $s_n = 6$.
   - Zero roots have N15 rows, with square sum $s_z = 10$.
   - Total $s = \operatorname{tr}(B^2) = 20(6) + 39(10) = 510$.
   - Four-cycle count:
     $$8C_4 = 6n + s - 12T = 6(59) + 510 - 12(7) = 354 + 510 - 84 = 780$$
     $$780 / 8 = 97.5 \notin \mathbb{Z}\qquad (780 \equiv 4 \pmod 8)$$
   - Integer contradiction excludes the entire $T=7, m=20$ case.

- **Immediate Consequence**: Any graph under zero-row N15 with $T = 7$ must have **$m = 21$**, meaning its seven triangles are **pairwise vertex-disjoint**.

---

### 3. General Injective Heavy $ZN$ Charging ($K \le R_{NZ}$)

The paper [`heavy_cross_repeat_slack_20261011.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md) establishes the universal inequality:
$$K \le R_{NZ} \le 2(4m - 3T - 59)$$
where $K$ is the number of heavy defect edges between $N$ and $Z$, and $R_{NZ} = \sum_{n \in N} \sum_{z \in Z \setminus N[n]} r(n, z)$ with $r(n, z) = B_{nz} - \binom{q(n,z)}{2} - \mathbf{1}_{\{B_{nz}=2\}}$.

#### Adversarial Verification of Charging Map
1. **Charging Construction**:
   - For each heavy cross edge $\{n, z\}$ ($n \in N, z \in Z, B_{nz} = 2$):
     - *Case $q(n, z) \le 1$*: $\binom{q}{2} = 0 \implies r(n, z) = 2 - 0 - 1 = 1$. Charge $\{n, z\}$ to the heavy pair $(n, z)$ itself.
     - *Case $q(n, z) = 2$*: Common neighbors are two zeros $x, y$ and one nonzero $v \in N$. Both $vx$ and $vy$ are nonedges with common neighbors $n \in N, z \in Z$, so $B_{vx}, B_{vy} \in \{1, 2\}$.
       - If both were 2, budget forces $t(v) = 1$ and nonedge repeats $\{x, y\}$, so transport forces $x \sim y$, creating triangle $nxy$ at $x \in Z$. Contradiction.
       - Thus at least one, say $B_{vx}$, equals 1. Common neighbors of $v, x$ are exactly $n, z$, so $q(v, x) = 1$. Thus $\binom{q(v,x)}{2} = 0$, giving $r(v, x) = 1 - 0 - 0 = 1$. Charge $\{n, z\}$ to the light pair $(v, x)$.
2. **Injectivity & Disjointness**:
   - Heavy charges have $B = 2$; light charges have $B = 1$. They are disjoint.
   - For light charges, the pair $(v, x)$ has common neighbors $n \in N$ and $z \in Z$. Its unique nonzero common neighbor is $n$, and its unique zero common neighbor is $z$.
   - Thus $(v, x)$ **uniquely determines** the source edge $\{n, z\}$. No two heavy edges can charge to the same light pair.
   - Injectivity is mathematically sound, proving $K \le R_{NZ}$.

---

### 4. $T=7, m=21$: Exclusion of the Repeat-Free Core Branch ($B_{NN} = 0$)

#### (1) The $b$-Correction for Isolated Light Zero Repeats
In a prior provisional draft, all 1111 zero-repeat rows were assumed to have their 4 zero endpoints fully paired. In the final paper, the general case is properly parameterized:
- Nonzero roots have 22 rows ($a$ roots) or 1111 rows ($21 - a$ roots).
- For a 1111 root $n$, let $p_n \in \{0, 1, 2\}$ be the number of paired edges in its zero support.
- There are $4 - 2p_n$ isolated zero repeats, giving $2b = \sum (4 - 2p_n)$ isolated light repeats in total.
- **Verification of Slack Contribution**:
  - For each isolated light repeat $x \in Z$ of root $n$, transport forces $x$ to have neighbors in the nonzero support of row $n$ totaling weight $B_{nx} = 1$. The nonzero support is a single triangle edge, so $x$ has exactly one nonzero common neighbor $w \in N$ with $n$.
  - Thus $n$ and $x$ have common neighbor $w \in N$. Since $B_{nx} = 1$, they have only 2 common neighbors in total.
  - Hence $q(n, x) \le 1 \implies \binom{q(n, x)}{2} = 0 \implies r(n, x) = 1 - 0 - 0 = 1$.
- **Verification of Disjointness from Heavy Charges**:
  - Heavy charges landing on light terms $(v, x)$ arise from a heavy repeat $n, z$ of type 22. In row $n$, zero repeats are isolated from nonzero support, so $z$ has no edge to triangle partners of $n$. Thus common neighbor $v$ is not a triangle partner of $n$.
  - Under $B_{NN} = 0$, positive nonzero support of row $v$ consists only of its own triangle partners. Since $n$ is not a triangle partner of $v$, $n$ is not in the positive support of row $v$.
  - The common neighbors of $v, x$ are $n, z$. Neither is in the positive nonzero support of row $v$.
  - Transport at row $v$ forces $x$ to be paired with another zero repeat; it cannot be isolated.
  - Hence the $2a$ heavy charges and $2b$ isolated light terms are **strictly disjoint**.
  - Total slack inequality:
    $$2a + 2b \le R_{NZ} \le 8 \implies a + b \le 4$$

#### (2) Trace Congruences and Contradiction
1. **Fourth Trace**: $s = 506 + 4a \implies 8C_4 = 776 + 4a$. Since $776 \equiv 0 \pmod 8$, $a$ must be **even** ($a \in \{0, 2, 4\}$).
2. **Fifth Trace**:
   - $e_n = 0$ for type 22 roots; $e_n = 4 - p_n = 2 + (2 - p_n)$ for type 1111 roots.
   - $\sum_{n \in N} e_n = 2(21 - a) + b = 42 - 2a + b$.
   - Global congruence $\sum e_n + T \equiv 4 \pmod 5$ with $T = 7 \equiv 2 \pmod 5$:
     $$42 - 2a + b + 2 \equiv 4 \pmod 5 \implies b \equiv 2a \pmod 5$$
   - Evaluating even $a \le 4$ under $a + b \le 4$:
     - $a = 4 \implies b \equiv 3 \pmod 5$, but $b \le 0 \implies$ no solution.
     - $a = 2 \implies b \equiv 4 \pmod 5$, but $0 \le b \le 2 \implies$ no solution.
     - $a = 0 \implies b \equiv 0 \pmod 5 \implies b = 0$.
3. **Incidence Contradiction at $a = 0, b = 0$**:
   - $a = 0$ means all 21 nonzero roots have type 1111, giving $21 \times 4 = 84$ light defect incidences between $N$ and $Z$.
   - By N15 at the 38 zero vertices, each zero vertex has degree 2 in light defect edges.
   - Total light defect incidences at $Z$ is at most $38 \times 2 = 76$.
   - Contradiction: $84 \le 76$.
   - Thus the repeat-free nonzero core branch ($B_{uv} = 0$ for all nonedges in $N$) is **excluded**.

- **Exact Branch Scope**: This excludes only the branch where nonedges in $N$ have $B = 0$. The branch where some nonedges in $N$ have positive defect remains **open** (subject to the total slack bound of 8).

---

### 5. Summary Table of Project Status (Orders 58–62)

| Problem Domain | Proposition / Subcase | Status | Scope & Boundary |
| :--- | :--- | :--- | :--- |
| **Order 59 ($n=59$)** | Exclusion of $T=7, m=20$ | **Proved** | Eliminates equality case of $59 \le 4m - 3T$ |
| **Order 59 ($n=59$)** | $T=7 \implies m=21$ (7 disjoint triangles) | **Proved** | Follows from $T=7, m=20$ exclusion |
| **Order 59 ($n=59$)** | General charging $K \le R_{NZ} \le 2(4m - 3T - 59)$ | **Proved** | Injective charging map verified |
| **Order 59 ($n=59$)** | $T=7, m=21$ repeat-free branch ($B_{NN} = 0$) | **Proved** | Excluded via $b$-correction and trace congruence |
| **Order 59 ($n=59$)** | $T=7, m=21$ with positive $B_{NN}$ nonedges | **Open** | Constrained by slack $\le 8$, not yet excluded |
| **Order 59 ($n=59$)** | Higher triangle counts ($T \ge 8$) | **Open** | Open |
| **Order 58 (Brown57)** | Extensions of fixed Brown graph require $\ge 10$ deletions | **Proved** | All 28 obligations verified |
| **Arbitrary $n=58$** | Arbitrary order-58 graph existence | **Open** | Baseline interval remains $[57, 62]$ |

