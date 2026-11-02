### 1. Reduction, Normalization, and Potential Hidden Obstructions

#### Mathematical Reduction Verification
The mathematical derivation in [FALSE_TWINS58_EIGHT_SIX_FIBERS.md](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/FALSE_TWINS58_EIGHT_SIX_FIBERS.md) was reviewed in detail alongside [CYCLIC7_EIGHT_ORBITS58_SEED.md](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/CYCLIC7_EIGHT_ORBITS58_SEED.md):

1. **Regularity and false-twin fiber decomposition:**
   - Any 58-vertex graph with max degree $\le 8$ and diameter $\le 2$ must be 8-regular: a vertex of degree $\le 7$ has radius-2 ball size $\le 1 + 7\times 8 = 57 < 58$.
   - The defect matrix $B = A^2 + A - 7I - J_{58}$ is entrywise non-negative with row sums $7\mathbf{1}$.
   - For false twins $u, v$, $B_{uv} = 8 - 1 = 7$, completely exhausting the row budget at $u$ and $v$. This rigorously forces:
     - Their common neighborhood $S = N(u) = N(v)$ ($|S|=8$) is an independent set ($B_{us} = 0$).
     - The remaining 48 vertices $R = V \setminus (\{u,v\} \cup S)$ partition into eight 6-vertex fibers $G_i = N(s_i) \cap R$.
     - Each fiber $G_i$ is independent ($B_{s_i x} = 0$).
     - Between any two distinct fibers $G_i, G_j$, edges form a perfect matching ($B_{s_j x} = 0 \implies |G_j \cap N(x)| = 1$).
   - *Verdict:* The 8-fiber matching structure is an exact two-way equivalence for any 58-vertex graph with false twins.

2. **Order-7 automorphism with $f=9$ fixed vertices:**
   - From Section 1 of [CYCLIC7_EIGHT_ORBITS58_SEED.md](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/CYCLIC7_EIGHT_ORBITS58_SEED.md), $f \equiv 58 \pmod 7 \implies f \in \{2, 9\}$.
   - When $f=9$, the fixed subgraph is uniquely $H = K_{1,8}$ with center $h$ and eight leaves.
   - All 8 neighbors of $h$ in $G$ are the 8 fixed leaves. To reach $h$ within distance 2, every nonfixed vertex must attach to at least one fixed leaf.
   - There are 7 nonfixed 7-orbits and 8 fixed leaves. By the Pigeonhole Principle, the allocation of leaves to orbits is uniquely $2 + 1 + 1 + 1 + 1 + 1 + 1$.
   - The two leaves sharing a 7-orbit $T = \{s_0, \dots, s_6\}$ are false twins $u, v$ with $S = \{h\} \cup T$.
   - The other six leaves form the fixed fiber $G_\infty$ with parent $h$, each connected to one 7-orbit.
   - *Verdict:* Any 58-vertex target with an order-7 automorphism fixing 9 vertices mathematically forces this false-twin model.

3. **Normalization and domain coverage:**
   - In [FALSE_TWINS58_EIGHT_SIX_FIBERS.md](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/FALSE_TWINS58_EIGHT_SIX_FIBERS.md#L139-L145), labeling $x_{t, a} \in G_t$ by its matching neighbor $\ell_a \in G_\infty$ simultaneously normalizes all matchings $Q_{\infty, t} = I$. Because $\ell_a$ is fixed by $g$, $g(x_{t, a}) = x_{t+1, a}$ is an exact coordinate transport, not an extra assumption.
   - Matching invariance under $g$ forces $Q_{t, t+d} = P_d$ and $Q_{t+d, t} = P_{-d} = P_d^T$.
   - The hub condition $K_\infty = I + A + A^T + B + B^T + C + C^T = J_6 + F$ requires $(K_\infty)_{aa} - 1 = 2(A_{aa} + B_{aa} + C_{aa}) \in \{0, 1\}$. Being an even integer, it must be 0, forcing $A, B, C$ to be derangements and $F$ to be a fixed-point-free involution.
   - All 15 fixed-point-free involutions in $S_6$ are conjugate under $S_6$. Simultaneously conjugating $(A, B, C)$ by $\sigma \in S_6$ preserves the identity interfaces $Q_{\infty, t} = I$. Thus, fixing $F = (01)(23)(45)$ is a lossless canonical choice.
   - *Verdict:* The normalization loses zero isomorphism classes.

4. **Hidden already-excluded structures:**
   - *Vertex-transitive / Cayley exclusions:* Inapplicable. The model has multiple distinct orbit sizes ($1, 6, 7, 42$) and false twins; it is neither Cayley nor vertex-transitive.
   - *Induced HS50 exclusions:* Inapplicable. $G$ contains a star $K_{1,8}$, whereas $\Delta(\text{HS50}) = 7$; $G$ cannot contain an induced HS50.
   - *Order-7 automorphism exclusions:* Inapplicable. Prior work excluded order-7 automorphisms for orders 59, 60, and 61 ([AUTOMORPHISM_PRIME_60_61_OBSTRUCTION.md](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/AUTOMORPHISM_PRIME_60_61_OBSTRUCTION.md)); order 58 was explicitly left open.

---

### 2. Full 10,080 Coverage Test Evaluation

1. **Worthwhileness as a bounded decision:**
   - **Cost:** Negligible. In [false_twins58_f9_domain_prepare.py](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/construction/false_twins58_f9_domain_prepare.py), generating and storing all 10,080 triples took 0.34 wall seconds. Checking the three $6 \times 6$ matrix equations $K_1, K_2, K_3 \ge J_6$ for all 10,080 triples involves $\approx 1.5 \times 10^6$ lookups and additions, completing in $< 0.1$ CPU seconds.
   - **Decisiveness:** Total. If any triple passes, an explicit 58-vertex target is found. If all 10,080 fail, the entire $f=9$ $C_7$ branch of order 58 is rigorously and permanently closed.
   - **Conclusion:** It is highly worthwhile to run to completion.

2. **Exact complete-graph checks necessary:**
   - **Triple filter:**
     $$\begin{aligned}
     K_1 &= I + A + BA^T + CB^T + (C^T)^2 + B^TC + A^TB \ge J_6 \\
     K_2 &= I + B + A^2 + CA^T + C^TB^T + B^TC^T + A^TC \ge J_6 \\
     K_3 &= I + C + AB + BA + C^TA^T + (B^T)^2 + A^TC^T \ge J_6
     \end{aligned}$$
     *(Short-circuit upon any entry equal to 0).*
   - **Complete-graph certification protocol (if any triple passes):**
     Although the mathematical derivation proves $K_\infty \ge J$ and $K_d \ge J$ are sufficient for all $\binom{58}{2}$ pairs to have distance $\le 2$, independent verification requires:
     1. Constructing the explicit 58-vertex graph (232 edges).
     2. Verifying 8-regularity for all 58 vertices.
     3. Running an independent full-source BFS on the expanded graph to confirm diameter $\le 2$ (0 bad pairs).
     4. Verifying that the permutation $g = (h)(u)(v)\prod_{a=0}^5 (\ell_a)\,(s_0\dots s_6)\prod_{a=0}^5 (x_{0,a}\dots x_{6,a})$ preserves the edge set.

---

### 3. Concrete Mathematical Mechanisms if the $f=9$ $C_7$ Branch Fails

If all 10,080 triples fail, the failure is specific to the $f=9$ cyclic representation. To avoid continuing minor variants of near-HS searches or frozen quotients, the following two fully specified, executable mechanisms break away from the failed branches:

#### Mechanism A: Order 58 Bi-Circulant under $C_{29}$ (2-orbit model)
- **Mathematical origin:**
  By the prime-divisor theorem established in [AUTOMORPHISM_PRIME_60_61_OBSTRUCTION.md](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/AUTOMORPHISM_PRIME_60_61_OBSTRUCTION.md#L90-L98), any prime $p > 8$ dividing $|\text{Aut}(G)|$ has no fixed vertices, so $p \mid 58 \implies p = 29$.
  Thus, any target with a prime symmetry $p > 8$ must have an automorphism of order 29 with exactly two orbits $V_0, V_1$ of size 29. (Cayley graphs are excluded, but asymmetric bi-circulants are not Cayley and not vertex-transitive).
- **Explicit graph specifications:**
  - Vertices: $V_0 = \{ (0, t) : t \in \mathbb{Z}_{29} \}$, $V_1 = \{ (1, t) : t \in \mathbb{Z}_{29} \}$. Total 58 vertices.
  - Degree budget: Internal degree $2k$, bipartite degree $s = 8 - 2k$.
    - *Proved obstruction:* $k=2 \implies s=4$ cannot reach all 29 vertices in $V_0$ (max reach $\le 1 + 4 + 10 + 12 = 27 < 29$).
    - *Proved obstruction:* $k=3 \implies s=2$ cannot reach all 29 vertices in $V_0$ (max reach $\le 1 + 6 + 15 + 2 = 24 < 29$).
    - *Feasible parameters:* $k=1$ (internal 29-cycle in each orbit) and $s=6$ (bipartite degree 6).
  - Edge sets:
    - In $V_0$: differences $\pm d_0$; normalized to $d_0 = 1$.
    - In $V_1$: differences $\pm d_1$, where $d_1 \in \{2, 3, \dots, 14\}$.
    - Bipartite: 6 differences $C = \{0, c_1, c_2, c_3, c_4, c_5\} \subset \mathbb{Z}_{29}$.
- **Explicit obligations:**
  1. Internal coverage: Difference set $\Delta(C) = \{c_i - c_j : i \ne j\}$ must cover $\mathbb{Z}_{29} \setminus \{\pm 1, \pm 2\}$.
  2. Cross coverage: $C \cup (C + 1) \cup (C - 1) \cup (C + d_1) \cup (C - d_1) = \mathbb{Z}_{29}$.
- **Feasibility status:**
  *Proved:* $k \in \{2, 3\}$ are impossible; $k=1, s=6$ is the unique viable parameter set.
  *Search scope:* Exactly $13 \times \binom{28}{5} = 1,277,640$ candidates. A bounded, closed algebraic check.

#### Mechanism B: Order 58 False Twins under Elementary Abelian $C_2^3$ Fiber Action
- **Mathematical origin:**
  The derivation of the 8-fiber matching model in [FALSE_TWINS58_EIGHT_SIX_FIBERS.md](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/FALSE_TWINS58_EIGHT_SIX_FIBERS.md) does not depend on $C_7$. The failure of $f=9$ eliminates only the $C_7$ cyclic coupling. Replacing $C_7$ with $(V_8 \cong C_2^3)$ treats all 8 fibers symmetrically.
- **Explicit graph specifications:**
  - Vertices: Twins $u, v$; common neighbors $s_g$ for $g \in \mathbb{Z}_2^3$; fibers $G_g = \{x_{g, a} : a \in \{0, \dots, 5\}\}$ for $g \in \mathbb{Z}_2^3$. Total 58 vertices.
  - Edges: Matching between $G_g$ and $G_{g+w}$ is a permutation matrix $P_w$ depending only on $w \in \mathbb{Z}_2^3 \setminus \{0\}$.
    Since $w = -w$, undirectedness forces $P_w = P_w^T$ (symmetric permutations, i.e., involutions in $S_6$).
- **Explicit obligations:**
  - Select 7 involutions $P_w \in S_6$ for $w \in \mathbb{Z}_2^3 \setminus \{0\}$.
  - For each non-zero $w$, the 6 other non-zero elements partition into 3 pairs $\{u, w+u\}$ summing to $w$.
  - Coverage condition:
    $$K_w = P_w + \sum_{\{u, w+u\}} (P_u P_{w+u} + P_{w+u} P_u) \ge J_6 \quad \text{for all } w \in \mathbb{Z}_2^3 \setminus \{0\}.$$
- **Feasibility status:**
  *Proved:* Complete 58-vertex graph satisfies diameter $\le 2$ if and only if all $K_w \ge J_6$.
  *Suggestion:* Existence of 7 involutions in $S_6$ satisfying these coupled conditions remains to be tested.

---

### Files Inspected and Execution Record
- **Files read:**
  1. [`proofs/dd82/construction/FALSE_TWINS58_EIGHT_SIX_FIBERS.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/FALSE_TWINS58_EIGHT_SIX_FIBERS.md)
  2. [`computations/dd82/construction/false_twins58_f9_domain_prepare.py`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/construction/false_twins58_f9_domain_prepare.py)
  3. [`computations/dd82/construction/false_twins58_f9_domain_run/result.json`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/computations/dd82/construction/false_twins58_f9_domain_run/result.json)
  4. [`proofs/dd82/construction/CYCLIC7_EIGHT_ORBITS58_SEED.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/CYCLIC7_EIGHT_ORBITS58_SEED.md)
  5. [`context/dd82/WORK_SUMMARY_V2_20261013.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/context/dd82/WORK_SUMMARY_V2_20261013.md)
  6. [`proofs/dd82/construction/AUTOMORPHISM_PRIME_60_61_OBSTRUCTION.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/AUTOMORPHISM_PRIME_60_61_OBSTRUCTION.md)
- **Computations executed:** None (read-only review as instructed).

---

### Memory update
- **To revisit after actual 10,080 evaluation results:**
  - *If 10,080 test returns 0 valid triples:* Confirm and register the universal mathematical exclusion of the entire $f=9$ $C_7$ branch for order 58. Do not re-run or perturb $f=9$. The open order-58 branches will then be narrowed to:
    1. The $f=2$ $C_7$ branch (2 fixed vertices, 8 cyclic orbits of size 7).
    2. The $C_{29}$ bi-circulant model ($k=1, s=6$, $1.28 \times 10^6$ parameter space).
    3. The general false-twin 8-fiber matching model under non-cyclic fiber symmetries (e.g., $C_2^3$).
  - *If 10,080 test returns $\ge 1$ valid triple:* Immediately execute the complete graph verification (full-source BFS, 8-regularity check, edge permutation invariance), extract the canonical adjacency matrix, and establish $N(8, 2) \ge 58$.

