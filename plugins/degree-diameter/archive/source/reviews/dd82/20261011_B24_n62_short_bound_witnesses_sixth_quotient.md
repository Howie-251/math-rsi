# B24: shorter component bound, witnesses, sixth traces and actual quotient Lean

Requested/CLI-selected model `gemini-3.8-flash-high` / `high`, not independent backend attestation. Proxy and temperature prose is not a new environment measurement. Reviewer executed no code; existing local executions remain separate evidence.

### Review Metadata & Scope Disclosure

- **Requested / Selected Model**: Gemini 3.8 Flash (High), reasoning effort `high`.
- **CLI / Backend Metadata**: Antigravity CLI executing against Gemini backend via proxy (`US-Dedicated-P1-1`), default temperature, effort `high`.
- **Execution & Modification Disclosure**: Zero shell commands, background tasks, or build tools executed during this review. Zero workspace files created or modified. Build logs and Lean outputs inspected are pre-existing local execution records.
- **Reading Scope Disclosure**:
  - **Fully read sources**:
    - [`proofs/dd82/n62/SHORT_COMPONENT_COUNT_BOUND.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/SHORT_COMPONENT_COUNT_BOUND.md) (all 109 lines)
    - Updated Section 1 of [`proofs/dd82/n62/CONNECTED_REPEAT_REDUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_REDUCTION.md) (lines 15–60)
    - [`proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md) (all 308 lines)
    - [`proofs/dd82/n62/CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md) (all 291 lines)
    - [`formal/DegreeDiameter/N62RepeatQuotient.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62RepeatQuotient.lean) (all 192 lines)
    - [`formal/ReviewN62RepeatQuotient.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/ReviewN62RepeatQuotient.lean) (all 50 lines)
    - [`formal/N62_REPEAT_QUOTIENT_HANDOFF.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/N62_REPEAT_QUOTIENT_HANDOFF.md) (all 30 lines)
    - [`formal/logs/n62-repeat-quotient-second.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-quotient-second.log) (all 3 lines)
    - [`formal/logs/n62-repeat-quotient-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-quotient-type-axiom-audit.log) (all 76 lines)
  - **Partially read / inspected predecessor references**:
    - [`D1_COMPONENT_MINIMUM_SIZES.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_COMPONENT_MINIMUM_SIZES.md) (Sections 1–5)
    - [`D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md) (Section 3)
    - [`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md) (Sections 3–5)
    - [`D1_MATCH_HARD_BRANCH_REDUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_MATCH_HARD_BRANCH_REDUCTION.md) (Sections 1–2)

---

### (A) Shorter Component Count Bound (`SHORT_COMPONENT_COUNT_BOUND.md`)

#### 1. Mathematical Derivations & Logic Audit
- **Retained Imports**:
  - Global triple-repeat elimination $\implies B \le 2 \implies$ each component size $n_i \ge 4$ even.
  - Actual equitability, trace identity $c + 2\operatorname{tr}(R) = 17 \implies c$ is odd.
  - Existence of at least one D1 pair from [`D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md) Section 3.
  - Earlier lower bounds $|H| \ge 12, |K| \ge 12$ from [`D1_COMPONENT_MINIMUM_SIZES.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_COMPONENT_MINIMUM_SIZES.md) Sections 1–5.
  - **Removed dependencies**: The entire subsequent chain establishing $|H|, |K| \ge 14$ (`D1_TWELVE_COMPONENT_EXTERIOR_EXCLUSION.md`, `D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md`, `D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md`, `D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md`, and `D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`) is **completely bypassed**.
- **Common-Neighbor Budget Identity**:
  $$(R^2+R)_{ii} = \sum_j r_{ij} r_{ji} + r_{ii} = 10 + n_i \implies \sum_j r_{ij}(r_{ji} - 1) = n_i + 2 - r_{ii}. \tag{1}$$
  All summands are nonnegative because balance gives $r_{ij} > 0 \implies r_{ji} \ge 1$, and diagonal $r_{ii}(r_{ii}-1) \ge 0$.
- **Bounding $c$**:
  - If $H = K$: $r_{HH} \ge 4 \implies \operatorname{tr}(R) \ge 4 \implies c = 17 - 2\operatorname{tr}(R) \le 9$.
  - If $H \ne K$: Packing $h, k \ge 12$ and other $c-2$ components of size $\ge 4$ gives $24 + 4(c-2) \le 62 \implies c \le 11$.
- **Exclusion of $c=11$**:
  The other 9 components use $\ge 36$ vertices $\implies h+k \le 26$. Even sizes $\ge 12$ leave only $(12,12), (12,14), (14,12)$.
  - $(12,14)$: Balance $12a = 14b \implies (a,b)=(7,6)$. The $K$-summand in (1) is $a(b-1) = 7(5) = 35 > 14 = h+2$, contradiction.
  - $(14,12)$: Balance $14a = 12b \implies (a,b)=(6,7)$. The $K$-summand is $a(b-1) = 6(6) = 36 > 16 = h+2$, contradiction.
  - $(12,12)$: $12a = 12b \implies a = b \ge 4$. Budget (1) on $H$ gives $a(a-1) \le 14 \implies a = b = 4$.
    Remaining 9 components sum to $62 - 24 = 38$, so they must be eight 4s and one 6. Every remaining component $L$ has $|L| \le 6$.
    Balance gives $r_{LH} = (12/|L|)x_L \ge 2x_L$. For $x_L > 0$, $x_L(r_{LH}-1) \ge x_L$.
    Summing outward degree from $H$ (row sum 8, $r_{HK}=4$, $r_{HH}=\alpha$):
    $$\sum_L x_L = 4 - \alpha \implies \sum_L x_L(r_{LH}-1) \ge 4 - \alpha. \tag{2}$$
    Exact budget (1) gives:
    $$\sum_L x_L(r_{LH}-1) = (14 - \alpha) - 4(4-1) - \alpha(\alpha-1) = 2 - \alpha^2. \tag{3}$$
    Combining (2) and (3) forces $4 - \alpha \le 2 - \alpha^2 \implies \alpha^2 - \alpha + 2 \le 0$, which is impossible for any integer $\alpha \ge 0$ (discriminant $-7 < 0$).
  Thus $c \ne 11$, forcing $c \le 9$ (odd).
- **Verdict**: **PASS (Provable as stated).** Replaces the $|H|,|K| \ge 14$ dependency cleanly with genuine imports explicit.

---

### (B) Nongenerated Triangle Witness Refinement (`CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md`)

#### 1. Mathematical Derivations & Constraints Audit
- **Heavy-Root Neighborhood $B[N(u)]$ & Nonheavy Witnesses** ([lines 66–100](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md#L66-L100)):
  For $u \in D$, $X = N_G(u)$ is independent. Common original neighbors inside $X$ are only $w$ (parents $1,2,3$) and $a$ (parents $1,4$). Thus $B[X]$ is the generated triangle $\{1,2,3\}$, edge $14$, and 4 isolated vertices. Any positive pair in $X$ meets $\{1,2,3\}$.
  Because any nongenerated unit triangle $T$ is disjoint from $\{1,2,3\}$, $|N_G(u) \cap T| \le 1$.
  Consequently, **no pair in $T$ can have a common original neighbor in $D$**. All witnesses of type 0 (6 witnesses) and type 1 (4 witnesses) lie strictly outside $D$.
- **Center Properties & Exact Zero Block** ([lines 101–148](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md#L101-L148)):
  - For type 1 triangle $T$, center $u$ has row $B_u = e_a + e_b + e_c$. Since $a,b,c \notin D$ and $a,b,c$ are independent, $\ell(u) = 0$ and $m(u) = 0$.
  - Commutation gives $(BA)_{au} = \sum_v B_{av} A_{vu} = (AB)_{au} = 0$, so repeat neighbors of $a,b,c$ are original nonneighbors of $u$. Because $T \subset N_G(u)$, $B[a, T] = B[b, T] = B[c, T] = 0$. Since $u \sim T$, $B[u, T] = 0$. Thus $\mathbf{B[\{u,a,b,c\}, T] = 0}$.
  - At $x \in T$, repeat row is $y,z,p_x$. If $p_x$ neighbored both $y$ and $z$, $p_x \in N(y)\cap N(z) = \{u,b\}$, contradicting $B[p_x, x] = 1$ and $B[\{u,b\}, T] = 0$. Thus $m(v) \le 1$ for all $v \in U_1$.
- **Strengthened Packing & Mixed Trace** ([lines 149–171](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md#L149-L171)):
  - Packing: Light mates of $D$ lie outside $D \cup U \cup C_1$. Capacity 3 gives:
    $$2d \le 3(62 - 5d - v_{\text{extra}} - c_{\text{out}}) \implies \mathbf{17d + 3v_{\text{extra}} + 3c_{\text{out}} \le 186}.$$
  - Mixed trace: Centers $C_1$ improve $m(w) \le 2$ by $-2$; $U_1 \setminus C_1$ improves by $-1$:
    $$\mathbf{\tau + 4t_1 + 2|U_1 \setminus C_1| \le 248 - 24d + 2L_3}.$$
- **Center Graph $\Gamma$ & Classification** ([lines 173–222](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md#L173-L222)):
  - Symmetry: $c(T) \in T' \iff c(T') \in T$ because $T' = \{u, a, b\}$ has center $y \in T$.
  - Degree $\le 2$ (at most 2 triangles contain a center, forming a diamond).
  - Any 5-vertex path forces 3 triangles in one cluster (impossible, diamond has 2). Triangles in $\Gamma$ are impossible (overlapping triangles cannot be adjacent in $\Gamma$).
  - Allowed components: $\mathbf{K_1, K_2, P_3, P_4, C_4}$. In $P_3$, the middle triangle is an isolated unit triangle ($s$).
- **$d=9$ Restrictions** ([lines 223–253](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md#L223-L253)):
  - $v_{\text{extra}} = 11 \implies s=1, k=2, c_{\text{out}}=0$. If all 5 triangles were type 1, $\Gamma$ would be $P_3 + K_2$. The middle of $P_3$ is the isolated triangle ($s=1$), the ends form one diamond ($k=1$), but $K_2$ would force the two overlapping triangles of the second diamond to be adjacent in $\Gamma$ (which requires disjoint triangles). Contradiction. Hence **at $d=9, v_{\text{extra}}=11$, not all triangles can be type 1 (at least one is type 0)**.
  - If a type 1 triangle exists at $d=9$: $\tau + 4 \le 44 \implies \tau \le 40 \implies 10c_5 - 24976 \le 40 \implies \mathbf{c_5 \le 2501}$.
- **Diamond Matching & Tips** ([lines 254–299](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md#L254-L299)):
  - Perfect matching between $N(x)\setminus N(y)$ and $N(y)\setminus N(x)$.
  - Tips $z,w$ have rows $B_z = e_x+e_y+e_p, B_w = e_x+e_y+e_q$ where ports $p,q$ may coincide ($p=q$).
  - Tip adjacency $z \sim w$ forces $m(z) \ge 2, m(w) \ge 2$, ruling out type 1 ($m \le 1$). Thus **$z \sim w \implies$ both diamond triangles have type 0**. Coincident ports $p=q$ are handled correctly.
- **Verdict**: **PASS (Provable as stated).** Provides an exact necessary structural catalog without asserting existence of any component.

---

### (C) Sixth Cycles & Determinant (`CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md`)

#### 1. Mathematical Derivations & Identities Audit
- **Nonbacktracking 6-Walks & $\operatorname{tr}(A^6)$** ([lines 83–124](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md#L83-L124)):
  - $F_6 = A^6 - (5r-4)A^4 + 3(r-1)(2r-1)A^2 - r(r-1)^2 I$.
  - In a triangle-free graph, nonbacktracking 6-walks are simple 6-cycles ($12c_6$) and 4-cycles with an initial/final spike ($8(r-2)c_4$).
  - For $n=62, r=8, c_4=(93+d)/2$:
    $$\operatorname{tr}(A^6) = 62\cdot8(5\cdot64 - 48 + 2) + 48(7)c_4 + 12c_6 = \mathbf{151528 + 168d + 12c_6}.$$
- **Cubic Repeat Trace, Parity & Cycle Relations** ([lines 125–193](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md#L125-L193)):
  - In D1, repeat triangles have weights $1,1,1 \implies \operatorname{tr}(B^3) = 6u$.
  - Cube $B^3 = (Q-J)^3$ expansion yields:
    $$\operatorname{tr}(B^3) = \operatorname{tr}(A^6) + 30c_5 - 72d - 373984 = 12c_6 + 30c_5 + 96d - 222456.$$
    Dividing by 6 gives:
    $$\mathbf{u = 2c_6 + 5c_5 + 16d - 37076} \implies \mathbf{u \equiv c_5 \pmod 2}.$$
    Substituting $\tau = 10c_5 + 8d - 25048$ yields $\mathbf{4c_6 + \tau + 24d - 49104 = 2u}$.
  - Mixed trace: $\mathbf{\operatorname{tr}(A^2B^2) = 1860 + 28d + 6u - \tau}$.
- **Integer-Square Determinant $\det(29I+4B) = 41S^2$** ([lines 194–220](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md#L194-L220)):
  - $M = 2A+I \implies M^2 = 4(A^2+A)+I = 4B + 29I + 4J \implies 29I+4B = M^2 - 4J$.
  - $M\mathbf{1} = 17\mathbf{1} \implies M^{-2}\mathbf{1} = \frac{1}{289}\mathbf{1}$.
  - $\det(M^2 - 4\mathbf{1}\mathbf{1}^T) = (\det M)^2 (1 - 4\frac{62}{289}) = (\det M)^2 \frac{41}{289} = 41 S^2$ where $S = \det(2A+I)/17$ is an odd nonzero integer.
- **Weighted Tree Congruences & Characteristic Polynomial** ([lines 221–271](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md#L221-L271)):
  - $S^2 = \prod_{i=1}^{61} (29 + 4\mu_i)$. Modulo 41, $29 \equiv -12$, so $S^2 \equiv 4^{61}(-1)q(3) \equiv -4(62)\kappa(B) \equiv 39\kappa(B) \pmod{41}$.
    Since $39 \equiv 11^2 \pmod{41}$ and $11^{-1} \equiv 15 \pmod{41}$, $\mathbf{\kappa(B) \equiv (15S)^2 \pmod{41}}$.
  - Modulo 17: $\det(29I+4B) \equiv 4^{62}\det(3I+B) \equiv -\det(3I+B) \equiv 7S^2 \implies \mathbf{\det(3I+B) \equiv 10S^2 \pmod{17}}$.
  - Spectral polynomial: $\mathbf{q(t^2+t-7) = -p(t)p(-1-t)}$.
  - Correctly notes that no value of $d$ is currently excluded by these identities.
- **Verdict**: **PASS (Provable as stated).** All traces, algebraic expansions, and modular arithmetic reductions are verified exact.

---

### (D) Lean 4 Formalization (`N62RepeatQuotient.lean` & Verification Suite)

#### 1. Inspection of Definitions, Identities & Proof Chain
- **Constructed Objects**:
  - `repeatComponentSize G C`: Actual cardinality of `repeatComponentVertices G C`.
  - `repeatMembershipMatrix G`: Matrix $S : V \times \text{Component} \to \mathbb{Z}$ with $S_{xC} = \mathbf{1}_C(x)$.
  - `repeatSizeMatrix G`: Matrix with column $C$ having constant entry $n_C$.
  - `repeatQuotientMatrix G`: Matrix $R_{DC} = \operatorname{repeatComponentDegree}(G, D, C)$.
- **Formalized Proof Chain**:
  - `n62_adjacency_repeat_membership`: $AS = SR$.
  - `n62_defect_repeat_membership`: $BS = 3S$.
  - `ones_repeat_membership`: $JS = S \cdot \operatorname{repeatSizeMatrix}(G)$.
  - `n62_repeat_quotient_quadratic`: Directly proves $R^2 + R = 10\cdot I + \operatorname{repeatSizeMatrix}(G)$ by evaluating $(A^2+A-7I-J)S = BS = 3S$ at a representative $x \in D.\text{supp}$.
  - `n62_repeat_quotient_row_sum`: Proves $\sum_C R_{DC} = 8$ using $AS=SR$ and 8-regularity of $A$.
  - `n62_repeat_quotient_balance`: Proves $n_D R_{DC} = n_C R_{CD}$ via symmetric double summation $\sum_x \sum_y \mathbf{1}_D(x) A_{xy} \mathbf{1}_C(y)$.
  - `n62_repeat_component_sizes_sum`: Proves $\sum_C n_C = 62$.

#### 2. Premise, Axiom & Log Audits
- **Caller Premise Audit**:
  The module takes **only**:
  ```lean
  (G : SimpleGraph V) (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G) (hcard : Fintype.card V = 62)
  ```
  It requires **NO** $B \le 2$, **NO** D1/D0 classification, **NO** assumed quotient matrix, and **NO** pre-assigned equitable partition.
- **Axiom Audit Verification**:
  From [`formal/logs/n62-repeat-quotient-type-axiom-audit.log`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/logs/n62-repeat-quotient-type-axiom-audit.log#L65-L75):
  All 11 public theorems depend strictly on standard Lean core axioms:
  $$\text{axioms: } [\texttt{propext}, \texttt{Classical.choice}, \texttt{Quot.sound}].$$
  Zero `sorry`, zero `native_decide`, zero custom axioms.
- **Formal Boundary**:
  Evenness of component sizes, the trace identity $\operatorname{tr}(R) = (17-c)/2$, $c \le 9$, connectedness, and finite quotient searches are **not** formalized in this module; only the exact algebraic identities connecting $G$ to $R$ are certified.
- **Verdict**: **PASS (Airtight Lean formalization).**

---

### Summary Table of Scoped Verdicts

| Source File / Component | Subject Scope | Audit Verdict | Key Load-Bearing Result / Formal Boundary |
| :--- | :--- | :---: | :--- |
| [`SHORT_COMPONENT_COUNT_BOUND.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/SHORT_COMPONENT_COUNT_BOUND.md) | Component count $c \le 9$ | **PASS** | Uses only $|H|,|K| \ge 12$; budget (1) excludes unequal $(12,14)$ and forces $a=b=4$; outward budget $4-\alpha \le 2-\alpha^2$ excludes $c=11$. Removes all subsequent $\ge 14$ exclusions. |
| [`CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md) | Witness isolation & packing | **PASS** | Nongenerated witnesses lie outside $D$; center $\ell=m=0$; packing $17d+3v_{\text{extra}}+3c_{\text{out}} \le 186$; $\Gamma$ components $\{K_1, K_2, P_3, P_4, C_4\}$; $d=9 \implies$ not all type 1; tip adjacency $\implies$ both type 0. |
| [`CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md) | Length-6 cycles & determinants | **PASS** | $\operatorname{tr}(A^6) = 151528 + 168d + 12c_6$; $u = 2c_6 + 5c_5 + 16d - 37076 \equiv c_5 \pmod 2$; $\det(29I+4B) = 41S^2$; $\kappa(B) \equiv (15S)^2 \pmod{41}$; no $d$ excluded. |
| [`N62RepeatQuotient.lean`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/formal/DegreeDiameter/N62RepeatQuotient.lean) | Formal Lean 4 quotient identities | **PASS** | Full algebraic quotient identity $R^2+R=10I+\mathbf{1}n^T$, row sum 8, balance proved from raw order-62 hypotheses; standard Lean axioms only. |

### Global Mathematical Scope
- The removal of the $\ge 14$ chain makes the connected reduction dependency profile substantially leaner.
- No source in this batch claims that all unit repeat triangles are generated, that $\tau = 0$, that any specific $d$ is eliminated, or that order 62 is excluded. The exact degree-diameter $N(8,2)$ problem remains open.


## Executor disposition and scope correction

Accepted the four scoped derivations. The summary table compresses the type-one boundary too far: the statement that not all nongenerated triangles are type one requires BOTH d=9 and v_extra=11, as correctly retained in the detailed review and actual source. It does not follow from d=9 alone. The earlier count c5<=2501 there requires a type-one triangle; the later separate heavy-port note is outside B24 and proves it without that extra hypothesis. Formal quotient source acceptance covers its exact algebraic identities only. The later ComponentBounds source was not in this batch. No full order62 exclusion or exact N claim.

