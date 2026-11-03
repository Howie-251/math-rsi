# Gemini B21 — corrected moments and three-component exclusions

### Metadata & Environment

- **Model**: Gemini 3.8 Flash (High), reasoning effort `high`.
- **Execution & modification status**: Zero shell or script execution performed; zero files created or modified. All audits are based strictly on static source reading and independent mathematical verification.
- **File audit inventory**:
  - **Fully read sources**:
    - [`D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md) (all 314 lines)
    - [`D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md) (all 194 lines)
    - [`THREE_COMPONENT_6_24_32_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_6_24_32_EXCLUSION.md) (all 167 lines)
    - [`THREE_COMPONENT_8_24_30_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_8_24_30_EXCLUSION.md) (all 223 lines)
    - [`THREE_COMPONENT_12_20_30_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_12_20_30_EXCLUSION.md) (all 233 lines)
    - [`three_component_quotients.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/three_component_quotients.py) (all 69 lines)
    - [`three_component_quotients.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/three_component_quotients.json) (all 121 lines)
  - **Partially read predecessor references**:
    - [`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md) (lines 90–240: Sections 2, 3, 4, 5, 6)
    - [`TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md) (lines 1–110: Sections 1–4)
    - [`D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md) (lines 1–60: Sections 1–2)

---

### TASK A: Audit of Size 12-by-16 and 12-by-20 D1 Partner Exclusions

#### 1. Exact Moment Substitution Table for `D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`

Using the exact source moment formulas ([lines 57–64](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L57-L64)):
$$S_x = 48 - 12s, \quad F_x = 72 - 12s^2, \quad S_y = 80 - 16t, \quad F_y = 144 - 16t^2, \quad C = 48(3 - s - t)$$
derived from $(A^2+A)\mathbf{1}_L = 10\mathbf{1}_L + |L|\mathbf{1}$ and $B\mathbf{1}_L = 3\mathbf{1}_L$, the values across all seven $(s,t)$ pairs are:

| $(s,t)$ | $s+t$ | $S_x$ | $F_x$ | $S_y$ | $F_y$ | $C$ | Source Section & Contradiction Mechanism |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$(0,0)$** | $0$ | $48$ | $72$ | $80$ | $144$ | $144$ | §2: $C=144 \notin \{0, 48\}$ |
| **$(0,1)$** | $1$ | $48$ | $72$ | $64$ | $128$ | $96$ | §2: $C=96 \notin \{0, 48\}$ |
| **$(0,2)$** | $2$ | $48$ | $72$ | $48$ | $80$ | $48$ | §3: Type $M$ violates $4x+3y \le 16$; type $P$ exhausts $S_y=48$ but gives $F_y=48 < 80$ |
| **$(1,1)$** | $2$ | $36$ | $60$ | $64$ | $128$ | $48$ | §3: Type $P$ leaves residual $F_x=60 > 36$; type $M$ forces $r_{XX}=4$, violating diagonal quotient $20 \le 16$ |
| **$(1,2)$** | $3$ | $36$ | $60$ | $48$ | $80$ | $0$ | §5: Pure distribution $(3,0):8, (2,0):6, (0,4):4, (0,2):16$ gives $(Ad_K)(z)+d_K(z) \ge 20 > 16$ |
| **$(2,0)$** | $2$ | $24$ | $24$ | $80$ | $144$ | $48$ | §3: Type $M$ violates $3x+3y \le 12$; type $P$ exhausts $S_x=24$ but gives $F_x=0 < 24$ |
| **$(2,1)$** | $3$ | $24$ | $24$ | $64$ | $128$ | $0$ | §4: Pure $x$-support $|U| \ge 12$ and pure $y$-support $|V|=24$ force $|U|+|V| \ge 36 > 34$ |

#### 2. Divisor Table and Coexistence of Mixed Types $P$ and $M$

- **Divisor audit**: For $1 \le x, y \le 3$, even component sizes and equitability divisibilities $12 \mid x N_{xy}$ and $16 \mid y N_{xy}$ ([line 50](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L50)) force $N_{xy}$ to be a multiple of $\operatorname{lcm}(2, \frac{12}{\gcd(12,x)}, \frac{16}{\gcd(16,y)})$. The divisor table in [lines 108–110](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L108-L110) is verified exact:
  - Divisor 48: $(1,1), (1,3), (2,1), (2,3)$ (exceeds 34 exterior vertices).
  - Divisor 16: $(3,1), (3,3)$ ($N \ge 16 \implies F_x \ge 16 \times 3 \times 2 = 96 > 72$).
  - Divisor 24: $(2,2)$ ($N_{22}=24 \implies S_x \ge 48$; if $s>0$, $48 > S_x$; if $s=0$, exhausts $S_x$ and leaves $F_x = 48 < 72$).
  - This leaves only $P=(1,2)$ with $N_{12}=24$ and $M=(3,2)$ with $N_{32}=8$ ([lines 125–129](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L125-L129)). (A size $N_{32} \ge 16$ would give $F_x \ge 96 > 72$).
- **Coexistence exclusion including $s=0$** ([lines 134–137](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L134-L137)):
  If $P$ and $M$ coexist, their combined contributions are $\sum x = 24(1) + 8(3) = 48$ and $\sum x(x-1) = 24(0) + 8(6) = 48$.
  - If $s > 0$: $S_x = 48 - 12s \le 36 < 48$, exceeding the total available sum.
  - If $s = 0$: $S_x = 48$. $P$ and $M$ completely exhaust $S_x$, forcing $x_v=0$ on all remaining exterior vertices. The total exterior factorial moment is then frozen at $48$. But for $s=0$, $F_x = 72 - 12(0)^2 = 72 \ne 48$.
  Thus $P$ and $M$ cannot coexist for any $s \ge 0$, and each contributes $48$ to $C$, proving $C \in \{0, 48\}$.

#### 3. The $(1,1)$ Branch with Type $M$ ($N_{32}=8$)

- **Residual moments & forcing of $X$** ([lines 163–174](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L163-L174)):
  $M$ exhausts $C=48$, so all other exterior vertices have $y_v=0$.
  Residuals on $x>0$: $\sum x = 36 - 24 = 12$, $\sum x(x-1) = 60 - 48 = 12$.
  Divisibility gives $4 \mid N_{30}$ and $6 \mid N_{40}$. A nonempty type $(3,0)$ or $(4,0)$ would contribute $\ge 24$ or $\ge 72$ to $\sum x(x-1)$, which exceeds 12. Thus $N_{30} = N_{40} = 0$.
  The system $N_{10} + 2N_{20} = 12$ and $2N_{20} = 12$ uniquely forces $N_{20}=6$ and $N_{10}=0$. Denote this 6-vertex set of type $(2,0)$ by $X$.
- **$X$ is a whole $B$-component** ([lines 175–178](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L175-L178)):
  Any repeat component $L \subseteq X$ has constant $x_L=2$. Balance with $H$ gives $12 r_{HL} = |L| \cdot 2 \implies |L| = 6 r_{HL}$. Hence $6 \mid |L|$. Since $|X|=6$, $X$ itself is an individual repeat component. (Likewise $8 \mid |L'|$ for $L' \subseteq M$, so $M$ is a single 8-vertex component).
- **H-neighbor identity and $r_{XX}=4$** ([lines 180–197](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L180-L197)):
  Identity $(Ad_H)(v) + d_H(v) = 12$:
  - For $v \in M$ ($d_H(v)=3$): $v$ has 3 neighbors in $H$ (where $d_H=1$), 2 in $K$ (where $d_H=3$), $d_M(v)$ in $M$ ($d_H=3$), and $d_X(v)$ in $X$ ($d_H=2$).
    $$(3 \cdot 1 + 2 \cdot 3 + 3 d_M(v) + 2 d_X(v)) + 3 = 12 \implies 3 d_M(v) + 2 d_X(v) = 0.$$
    Since degrees are nonnegative, $d_M(v) = 0$ and $d_X(v) = 0$. This establishes that there are **no edges between $M$ and $X$**.
  - For $v \in X$ ($d_H(v)=2$): $v$ has 2 neighbors in $H$ ($d_H=1$), 0 in $K$, 0 in $M$, and $d_X(v)$ in $X$ ($d_H=2$).
    $$(2 \cdot 1 + 2 d_X(v)) + 2 = 12 \implies 2 d_X(v) = 8 \implies d_X(v) = 4.$$
    Thus $r_{XX} = 4$.
- **Quotient diagonal contradiction**:
  The diagonal entry of $R^2+R = 10I + \mathbf{1}n^T$ for component $X$ requires $(R^2+R)_{XX} = 10 + |X| = 16$. But $(R^2+R)_{XX} \ge r_{XX}^2 + r_{XX} = 4^2 + 4 = 20$. The resulting inequality $20 \le 16$ is a concrete contradiction.

#### 4. Audit of the Two $C=0$ Pure Cases

- **$(s,t)=(2,1)$** ([lines 198–226](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L198-L226)):
  Moments: $S_x=24, F_x=24, S_y=64, F_y=128$.
  $x-1 \le x(x-1)/2$ implies $|U| \ge S_x - F_x/2 = 24 - 12 = 12$.
  Divisibilities $N_{01}=16a, N_{02}=8b, N_{03}=16c, N_{04}=4d$ give $a+b+3c+d=4$ and $b+6c+3d=8$. This uniquely forces $c=0$, $d=2$, $b=2$, $a=0$, so $N_{04}=8, N_{02}=16$, yielding $|V|=24$.
  Disjoint support gives total exterior vertices $\ge |U|+|V| \ge 12 + 24 = 36 > 34$.
- **$(s,t)=(1,2)$ and final $16 \ge 20$** ([lines 227–278](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md#L227-L278)):
  Moments $S_x=36, F_x=60, S_y=48, F_y=80$. Divisibilities uniquely force pure types $(3,0):8, (2,0):6, (0,4):4, (0,2):16$ (total 34, so no $(0,0)$ vertices).
  For $z \in T_{04}$, $d_H(z)=0$ and $z$ has 4 neighbors in $K$ (where $d_H=3$). Identity $(Ad_H)(z)+d_H(z)=12$ forces $4 \cdot 3 + 3|N(z)\cap T_{30}| + 2|N(z)\cap T_{20}| = 12$, so $z$ has no neighbors in $T_{30} \cup T_{20}$.
  Hence all 8 neighbors of $z$ lie in $K \cup T_{04} \cup T_{02}$, where $d_K \ge 2$.
  Identity $(Ad_K)(z)+d_K(z) = |K| = 16$ yields:
  $$16 = (Ad_K)(z) + d_K(z) \ge 8 \cdot 2 + 4 = 20.$$
  Contradiction $16 \ge 20$.

#### 5. Inspection of `D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md`

- **Definitions and the $(H,K)$ quotient entry** ([lines 52–60, 131–146](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md#L52-L60)):
  The variables are defined as:
  $$p = r_{HE} \quad (\text{outgoing } H \to E), \qquad q = r_{KE} \quad (\text{outgoing } K \to E),$$
  $$x = r_{EH} \quad (\text{incoming } E \to H), \qquad y = r_{EK} \quad (\text{incoming } E \to K).$$
  The off-diagonal entry of $R^2+R$ at $(H,K)$ is $\sum_{C} r_{HC} r_{CK} + r_{HK}$.
  For an exterior component $E \notin \{H,K\}$, the cross-term is $r_{HE} r_{EK} = p \cdot y$, **not** $p \cdot q$.
  The source correctly writes:
  $$r_{HH}r_{HK} + r_{HK}r_{KK} + \sum_{E \ne H,K} py + r_{HK} = |K| \implies 0 + 10 + \sum py + 5 = 20 \implies \sum py = 5.$$
  Balance gives $12py = exy = 20qx \implies 3py = 5qx \implies 5 \mid py$. But pointwise bounds force $xy = 0 \implies py = 0$, giving $0 = 5$.
  **Audit finding**: The source text correctly distinguishes $q$ from $y$ and accurately computes $p \cdot y$.

---

### TASK B: Audit of the Three Actual-Graph Quotient Exclusions

#### 1. Code Review of `three_component_quotients.py` and `.json`

- **Enumeration logic**:
  - Searches all integer matrices $R$ of size $3 \times 3$ with nonnegative integer entries, row sum 8, and trace 7 ($a+e+i=7$ derived from $k + 2\sum r_{ii} = 17$ with $k=3$).
  - Search ranges: $a, e \in [0, 7]$ with $i = 7-a-e \ge 0$. Rows satisfy $b \in [0, 8-a]$, $d \in [0, 8-e]$, $g \in [0, 8-i]$. Total tested matrices: exactly 9,108.
  - Hard filters applied:
    1. $R^2 + R - 10I = \mathbf{1} n^T$ (identical rows in $R^2+R-10I$).
    2. Component sizes $n_v \ge 4$ and $n_v \equiv 0 \pmod 2$.
    3. Balance: $n_u r_{uv} = n_v r_{vu}$ for all $u,v$.
  - Canonicalization: minimizes tuple $(n_{\pi}, R_{\pi})$ over all 6 simultaneous permutations $\pi \in S_3$.
- **Outputs**:
  Exactly 3 canonical matrices survive:
  1. Sizes $[6, 24, 32]$: $R = \begin{pmatrix} 0 & 8 & 0 \\ 2 & 2 & 4 \\ 0 & 3 & 5 \end{pmatrix}$
  2. Sizes $[8, 24, 30]$: $R = \begin{pmatrix} 2 & 6 & 0 \\ 2 & 1 & 5 \\ 0 & 4 & 4 \end{pmatrix}$
  3. Sizes $[12, 20, 30]$: $R = \begin{pmatrix} 3 & 0 & 5 \\ 0 & 2 & 6 \\ 2 & 4 & 2 \end{pmatrix}$
- **Audit verdict**: The code correctly and exhaustively identifies all 3-component integer equitable quotients under the established graph identities and $B \le 2$ ($n_i \ge 4$).

#### 2. Paper 1: `THREE_COMPONENT_6_24_32_EXCLUSION.md`

- **Decisive contradiction**: $G[K]$ is 2-regular. The cross-component neighbor identity forces 3 consecutive $K$-vertices along any cycle to partition the independent 6-vertex component $H$ into their three 2-element parent pairs. A parent pair of repeat weight 0 in $H$ has a unique common neighbor $v_0 \in K$. This uniqueness forces the walk in $G[K]$ to close at length 3, creating an original triangle in $K$. Triangle pairing then forces $K$ to have size 6, contradicting $|K|=24$.
- **Load-bearing step audit**:
  - *Partition of $H$* ([lines 83–98](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_6_24_32_EXCLUSION.md#L83-L98)): For $v \in K$ and its two $K$-neighbors $v_-, v_+$, $c_G(h,v) + A_{hv} = 1 + B_{hv} = 1$ since $h \in H, v \in K$ belong to distinct repeat components. Since $N_G(h) \subseteq K$, common neighbors of $h$ and $v$ can only be $v_-$ or $v_+$. Thus $\mathbf{1}_{h \in P(v_-)} + \mathbf{1}_{h \in P(v_+)} = 1 - \mathbf{1}_{h \in P(v)}$, which proves $P(v), P(v_-), P(v_+)$ form a disjoint partition of $H$.
  - *Unique parent pair* ([lines 101–116](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_6_24_32_EXCLUSION.md#L101-L116)): In $H$, row sum of $B$ is 3 on 5 other vertices, so at least two other vertices have $B_{h_1 h_2} = 0$. Since $G[H]$ is independent, $c_G(h_1, h_2) = 1 + B_{h_1 h_2} = 1$. The unique common neighbor $v_0$ lies in $K$ and is the unique vertex with parent pair $\{h_1, h_2\}$.
  - *Length-3 cycle* ([lines 119–137](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_6_24_32_EXCLUSION.md#L119-L137)): Consecutive partitions give $P(v_3) = H \setminus (P(v_1) \cup P(v_2)) = P(v_0) \implies v_3 = v_0$. Thus $v_0 v_1 v_2$ is an original triangle in $K$.
  - *Triangle pairing* ([lines 140–144](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_6_24_32_EXCLUSION.md#L140-L144)): By [`TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md), every triangle belongs to a closed 6-vertex component of $B$. Thus $|K|=6 \ne 24$.
- **Audit verdict**: Airtight; provable as stated.

#### 3. Paper 2: `THREE_COMPONENT_8_24_30_EXCLUSION.md`

- **Decisive contradiction**: $B[C]$ is simple by D0/D1 quotient bounds. $G[C]$ cannot be $C_8$ (would force $c_G(c,c') \ge 6 > 4$), so $G[C] = 2 C_4$. Commutation $B[C]X = XB[K]$ on a zero-repeat parent pair $F(v) = \{a_i, b_j\}$ forces repeat weight 2 covering $o(a_i)$ and repeat weight 2 covering $o(b_j)$. Their intersection $U \cap V$ consists only of the matching partner $p(v)$, which has repeat weight 0 with $v$. Weighted inclusion-exclusion gives row sum $\ge 2 + 2 - 0 = 4 > 3$.
- **Load-bearing step audit**:
  - *No double repeat in $C$ without needing $|H| \ge 14$* ([lines 53–60](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_8_24_30_EXCLUSION.md#L53-L60)): No size 6 component $\implies$ $G$ is triangle-free. No size 4 component $\implies$ no D0 double edges. For a D1 heavy component in $C$, Section 4 of [`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md#L195-L200) requires $r_{CC} \ge 4$ (if $J=C$), $r_{KC} \ge 3$ (if $J=K$), or $r_{CL} \ge 4$ (if $J=L$). Here $r_{CC}=2 < 4$, $r_{KC}=2 < 3$, and $r_{CL}=0 < 4$. All are directly violated by the quotient matrix entries! **Confirmed: The 8-case proof does not need the $|H| \ge 14$ theorem.**
  - *$C_8$ exclusion* ([lines 93–104](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_8_24_30_EXCLUSION.md#L93-L104)): Disjoint closed neighborhoods in $C_8$ require distance 3 or 4. Distance 3 forces $F(p(v))$ to be adjacent in $C_8$, creating an original triangle with $p(v)$ (impossible). Distance 4 makes all parent pairs antipodal, giving $c_G(c, c') \ge 6 > 1 + B_{cc'} \le 4$. Thus $G[C] = 2 C_4$.
  - *Opposite cross-repeat entries* ([lines 138–151](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_8_24_30_EXCLUSION.md#L138-L151)): Two 1s at $j, j+2$ in row $i$ would force $\{a_i, a_{i+2}, b_j, b_{j+2}\}$ to induce a closed unit $K_4$ in $B$, disconnecting $C$. Thus $M_{i, j+2} = 1 - M_{ij}$ and $M_{i+2, j} = 1 - M_{ij}$.
  - *Zero cross-repeat contradiction* ([lines 170–207](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_8_24_30_EXCLUSION.md#L170-L207)): Picking $M_{ij}=0$, $(B[C]X)_{o(a_i), v} = 1 + M_{i+2, j} = 2 = \sum_{w \in U} B_{vw}$ and $(B[C]X)_{o(b_j), v} = M_{i, j+2} + 1 = 2 = \sum_{w \in V} B_{vw}$. Since $U \cap V = \{p(v)\}$ and $B_{v, p(v)} = 0$, $\sum_{w \in K} B_{vw} \ge 2 + 2 - 0 = 4 > 3$.
- **Audit verdict**: Airtight; provable as stated.

#### 4. Paper 3: `THREE_COMPONENT_12_20_30_EXCLUSION.md`

- **Decisive contradiction**: $P = A[C,C]$ is a connected cubic triangle-free graph on 12 vertices. The auxiliary weighted graph $W = XX^T - 5I$ is proved connected via an invariant-subspace trace inequality. Consequently, the incidence kernel $\ker X^T$ has dimension at most 1, with eigenvalue at most 1 on that direction. Thus all 11 nonprincipal eigenvalues of $P$ lie in $[-3, 1]$. The trace polynomial $p(t) = (t-1)(t+3)^2 = t^3 + 5t^2 + 3t - 9$ yields $\operatorname{tr} p(P) = 72 = p(3)$, which forces all nonprincipal eigenvalues to lie in $\{1, -3\}$. Then $\operatorname{tr} P = 0 \implies 3 + (11-b)(1) - 3b = 0 \implies 4b = 14 \implies b = 7/2 \notin \mathbb{Z}$.
- **Load-bearing step audit**:
  - *Connectedness of $P$* ([lines 66–88](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_12_20_30_EXCLUSION.md#L66-L88)): Triangle-free cubic components must have even order $\ge 4$. $K_4$ has triangles; 6-vertex triangle-free cubic is $K_{3,3}$, which has 3 common neighbors, violating $|N(u) \cap N(v)| \le 2$. Thus components have order $\ge 8$, so the 12-vertex graph $P$ is connected.
  - *Connectedness of $W$* ([lines 115–153](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_12_20_30_EXCLUSION.md#L115-L153)): If $W$ has $q > 1$ components, the quotient matrix $S$ of $B_C$ on $U = \ker(W-5I)$ has $\operatorname{tr} S \le 2q$. On $U \cap \mathbf{1}^\perp$, $B_C = P^2 + P + 3I \implies \mu \ge 11/4$. Thus $\operatorname{tr} S \ge 3 + \frac{11}{4}(q-1) = 2q + \frac{3q+1}{4} > 2q$, a direct contradiction.
  - *Kernel bound & eigenvalue control* ([lines 154–193](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_12_20_30_EXCLUSION.md#L154-L193)): $PX + XZ + X = J \implies Z(X^T v) = -(\lambda+1)X^T v$. For $X^T v \ne 0$, eigenvalues of 2-regular $Z$ lie in $[-2, 2] \implies \lambda \in [-3, 1]$. For $X^T v = 0$, $v \in \ker X^T$, which is at most 1-dimensional (spanned by sign vector $f$ of bipartite $F$). Commutation forces $Pf = \lambda f$ with $\lambda \in \{-3, -1, 1, 3\}$. Connectedness of $P$ excludes $\lambda = 3$ on a nonconstant vector, so $\lambda \le 1$.
  - *Trace polynomial* ([lines 194–224](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_12_20_30_EXCLUSION.md#L194-L224)): For $p(t)=(t-1)(t+3)^2$, $\operatorname{tr} p(P) = 5(36) - 9(12) = 72 = p(3)$. Nonpositivity on $[-3, 1]$ forces all nonprincipal $\lambda_i \in \{1, -3\}$, yielding $b = 7/2 \notin \mathbb{Z}$.
  - *Dependency note on $|H| \ge 14$*: The paper cites $|H| \ge 14$ to exclude D1 double repeats in $C$ ([lines 70–72](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/THREE_COMPONENT_12_20_30_EXCLUSION.md#L70-L72)). Note that even without this theorem, Section 4 of [`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md#L195-L200) requires $r_{EC} \ge 3$ for partner $E$, whereas the quotient has $r_{EC} = 2 < 3$. As currently written, however, the source formally depends on the $|H| \ge 14$ result established by [`D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md).
- **Audit verdict**: Airtight; provable as stated.

---

### Separate Audit Verdicts

1. **Source Arithmetic & Divisor Case Coverage** ([`D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md) and [`D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n62/D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md)):
   **VERDICT: PASS.** All 7 moment tuples, the divisor table, the $s=0$ and $s>0$ coexistence exclusions, the whole-component derivation of $X$ and $r_{XX}=4$, both $C=0$ branches, and the distinction between $q$ and $y$ are verified correct.
2. **Three-Component Quotient Enumeration** ([`three_component_quotients.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/three_component_quotients.py) / [`.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/n62/three_component_quotients.json)):
   **VERDICT: PASS (as exhaustive integer quotient diagnostic).** The search domain completely covers all trace-7, row-sum-8 integer quotients with $n_i \ge 4$ even. Exactly 3 canonical forms exist.
3. **Paper `THREE_COMPONENT_6_24_32_EXCLUSION.md`**:
   **VERDICT: PASS.** Independent of D1 minimum size bounds; load-bearing steps are mathematically sound.
4. **Paper `THREE_COMPONENT_8_24_30_EXCLUSION.md`**:
   **VERDICT: PASS.** Completely self-contained using direct D1 quotient incidence bounds; does not rely on $|H| \ge 14$.
5. **Paper `THREE_COMPONENT_12_20_30_EXCLUSION.md`**:
   **VERDICT: PASS.** Spectral trace argument and invariant subspace bound are mathematically complete. Its formal dependency on the $|H| \ge 14$ chain is validated by the verified pass of `D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`.

### Combined Mathematical Scope

Combining the exhaustive enumeration diagnostic with the three verified exclusion papers proves that **an actual legal order-62 graph cannot have exactly 3 repeat-support components of sizes $\ge 4$**.
- This batch does **not** rule out a connected repeat matrix ($k=1$) or component counts $k \ge 5$.
- D0 and D1 components may coexist in configurations with other component counts; one D1 double edge does not imply all double edges are D1.
- No overall order-62 nonexistence or exact degree-diameter $N(8,2)$ bound is claimed.


## Executor disposition

B21 is a genuinely new Antigravity conversation, thread c38adf11-80d2-416a-a023-3c41c0c71073, rather than a continuation falsely claiming fresh context. Requested/CLI-selected gemini-3.8-flash-high/high is preserved without independent backend attestation. Zero reviewer executions.

The corrected seven-row moment table matches the actual formulas and the reviewed source. The response now checks the s=0 coexistence deficit, the eight-point mixed type, individual component divisibility, actual H-neighbor equations and both pure cases. It correctly distinguishes py from pq. This closes the substantive B20 paper-review transcription problem; B20's raw errors remain preserved rather than silently replaced.

One compressed sentence in the (1,1) M discussion is still too strong: exhausting the mixed moment makes every remaining vertex pure (xy=0), not necessarily y=0. The subsequent residual calculation correctly concerns the positive-x part, where y=0; the source retains positive-y pure types. This wording error does not supply a missing proof step and is corrected here. No source was changed.

All three actual quotient exclusion sources and the original minsize4 enumeration are accepted within the listed read scopes. B21 did not read the newly widened minsize2 checker, THREE_COMPONENT_EXCLUSION integration, large5/7/9 classifications, or CONNECTED_REPEAT_REDUCTION. Its code review is static; execution/count corroboration belongs to local exact checkers. The actual graph proofs and general D1 size chain remain paper-level, not Lean formalizations.

The newer minsize2 classification has an independent local exact receipt; integration directly derives B_C simplicity in the12-case from D1 quotient incidences and excludes local B=3 via absence of size2 components. Those deltas still need their own cross-family read. No whole62 exclusion or exact N8 result follows.

