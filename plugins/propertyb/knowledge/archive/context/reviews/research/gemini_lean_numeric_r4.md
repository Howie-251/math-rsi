### 1. Verdict

**No discrepancy found** inside the 23 supplied profiles.

The numerical evaluator in [`formal/Aris4Math/Numeric.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean) implements the paper's formulas from [`proofs/PROBABILITY_LEMMAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md), [`proofs/STRUCTURE_19_23.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_19_23.md), and [`PROOF_PACKAGE.md`](file:///Users/rfy_naiveai/Desktop/aris4math/PROOF_PACKAGE.md) for all 23 profiles (21 successful branches certifying total bound $< 1$, and 2 retained diagnostic branches certifying total bound $> 1$).

No separating input exists within the 23 supplied profiles.

---

### 2. Formula-by-Formula Mathematical Correspondence

#### A. Actual Positions vs. Vertex Labels
- **Paper specification**: In [PROBABILITY_LEMMAS.md (lines 26–45)](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L26-L45), locked vertices $s_i$ have positions $t_i \in [v]$. The set of locked positions in edge $e$ is $\{t_i : s_i \in e\}$, and position comparisons are $t_i < k$ or $t_i > k$.
- **Lean implementation**: [`EdgeType.locks`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L21-L24) directly stores the 1-based permutation positions $t_i$, not abstract labels $1 \dots s$. In [`edgeWeight`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L45-L58) and [`pairWeight`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L60-L77), conditions `t.locks.all (· < k)` and `u.locks.all (k < ·)` compare positions directly to $k$. When $k \in p.\mathrm{positions}$, $k \in t.\mathrm{locks}$ checks that the locked center is in the edge, and `(t.locks.filter (· != k)).all fits` checks that all other locked positions in the edge precede (or follow) $k$. This matches the paper without label-indirection error.

#### B. Truncated Natural Subtraction
- `freeCount` ([Numeric.lean:36](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L36)): $v - |\mathrm{positions}|$. In all 23 profiles, $|\mathrm{positions}| \le 6 \le v$, so no underflow occurs.
- `leftCount` ([Numeric.lean:38-40](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L38-L40)): $k - 1 - |\{t \in \mathrm{positions} : t < k\}|$. Because locked positions are in $[1, v]$, every locked position $< k$ belongs to $\{1, \dots, k-1\}$. Thus the filtered length is always $\le k - 1$, and natural subtraction does not underflow.
- `rightCount` ([Numeric.lean:41-43](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L41-L43)): $v - k - |\{t \in \mathrm{positions} : k < t\}|$. Because all locked positions are in $[1, v]$, every locked position $> k$ belongs to $\{k+1, \dots, v\}$, avoiding underflow.
- `edgeWeight` and `pairWeight` ([Numeric.lean:47, 56, 62, 70, 74](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L47)): In the free center case, $1 \le r$ and $r + q - 1 \le N$ guard $r - 1$, $q - 1$, $N - 1$, and $N - r$. In the locked center case, $r + q \le N$ guards $N - r$. The denominators are strictly positive natural numbers, avoiding division by zero.
- `pairCount` ([Numeric.lean:80](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L80)): When $t.\mathrm{locks} = u.\mathrm{locks}$, $u.\mathrm{count} \ge 1$ is guaranteed by `validProfile` (`0 < t.count`), so $u.\mathrm{count} - 1$ never underflows.
- `positionBound` ([Numeric.lean:116](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L116)): `boundC p k - deduction p k` is evaluated in `Rat`, which is field subtraction, not truncated natural subtraction.

#### C. Pair Compatibility
- **Paper P3a / P4a** ([PROBABILITY_LEMMAS.md:128-174](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L128-L174)):
  - Free center $k$: requires $T \subseteq I_k^-$, $U \subseteq I_k^+$, $T \cap U = \varnothing$, $r_T, r_U \ge 1$, and $r_T + r_U - 1 \le N$.
  - Locked center $k$: requires $T \cap U = \{k\}$, $T \setminus \{k\} \subseteq I_k^-$, $U \setminus \{k\} \subseteq I_k^+$, and $r_T + r_U \le N$.
- **Lean implementation** ([Numeric.lean:66-77](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L66-L77)):
  - For $k \in p.\mathrm{positions}$: checked by `t.locks.filter (· ∈ u.locks) = [k]`, `(t.locks.filter (· != k)).all (· < k)`, `(u.locks.filter (· != k)).all (k < ·)`, and `r + q ≤ N`.
  - For $k \notin p.\mathrm{positions}$: checked by `1 ≤ r ∧ 1 ≤ q`, `t.locks.all (· ∉ u.locks)`, `t.locks.all (· < k)`, `u.locks.all (k < ·)`, and `r + q - 1 ≤ N`.
  - Incompatible pairs branch to `else 0`, implementing P3b/P4b without spurious fractions.

#### D. Same-Type Ordered-Pair Counts ($M_{TU}$)
- **Paper formula** ([PROBABILITY_LEMMAS.md:36](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L36)): $M_{TU} = \ell_T(\ell_U - \mathbf{1}_{T=U})$.
- **Lean implementation** ([Numeric.lean:79-82, 89-91](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L79-L82)):
  `pairCount` sets $m = t.\mathrm{count} \cdot (u.\mathrm{count} - \mathbf{1}_{t.\mathrm{locks} = u.\mathrm{locks}})$. Because types in each profile have distinct lock lists (verified by `validProfile`), $t.\mathrm{locks} = u.\mathrm{locks} \iff t = u$. `boundC` iterates over all ordered pairs $(t, u) \in \mathrm{types} \times \mathrm{types}$.

#### E. $q$ Rounding and Integer Ceiling
- **Paper formula P8 / S2** ([PROBABILITY_LEMMAS.md:269](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L269)): $q(u) \ge \lceil \frac{4d(u) - (v - 1)}{3} \rceil$.
- **Lean implementation** ([Numeric.lean:105-106](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L105-L106)):
  `linkQLower p k := (4 * linkDegree p k - (p.v - 1) + 2) / 3`.
  For non-negative integer $X = 4d - (v-1)$, Lean integer division $\lfloor (X + 2) / 3 \rfloor$ equals $\lceil X / 3 \rceil$. In all five profiles with correction centers (`v21_d7`, `v22_67`, `v22_77`, `v23_66`, `v23_677`), $4d \ge v - 1$ holds strictly, avoiding natural underflow before `+ 2`. The values ($q=3, 3, 3, 1, 2$) match theorems `*_link_*`.

#### F. Unordered Slot Capacity and Two Directions
- **Paper formulation P6b / S23T** ([PROBABILITY_LEMMAS.md:223](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L223), [STRUCTURE_19_23.md:175-189](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_19_23.md#L175-L189)):
  Unordered bad pairs $\{e, f\}$ around center $k$ must be weighted by $w_k(T(e), T(f)) + w_k(T(f), T(e))$. The capacity of $\{T, U\}$ is $\binom{\ell_T}{2}$ if $T = U$, and $\ell_T \ell_U$ if $T \ne U$.
- **Lean implementation** ([Numeric.lean:94-99](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L94-L99)):
  `linkSlots` filters types containing $k$, iterates over $(t, i)$ and $u \in ts.\mathrm{drop}(i)$, assigning capacity `if t.locks = u.locks then binom t.count 2 else t.count * u.count`, and replicating `pairWeight p t u k + pairWeight p u t k`. Every unordered pair of edges containing $k$ appears exactly once.

#### G. Zero Slots and Sorting
- **Paper constraint P6b / P9c** ([PROBABILITY_LEMMAS.md:227-230, 332](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L227-L230)): Zero-weight bad pairs (such as $\{xz, yz\}$ at center $z=13$ in $v=23$) must not be credited with positive deductions.
- **Lean implementation** ([Numeric.lean:109-112](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L109-L112)):
  `deduction` sorts `linkSlots` in non-decreasing order (`insertionSort (· ≤ ·)`) and takes the first $q$ elements. Any zero-weight slot sorts to the front and contributes $0$ to the deduction. At $z=13$ in `v23_677`, the cheapest 2 slots are $0$ and $3/323$, giving deduction $3/323$ ([Numeric.lean:312](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L312)), exactly matching the paper.

#### H. Changing $C$ Before Min
- **Paper formula P7a / P7b** ([PROBABILITY_LEMMAS.md:238, 242-250](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L238)): $C'_k = C_k - d_k$, then evaluate $\min\{A_k, B_k, C'_k\}$.
- **Lean implementation** ([Numeric.lean:115-117](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L115-L117)):
  `positionBound p k := min (boundA p k) (min (boundB p k) (boundC p k - deduction p k))`.
  Deduction is subtracted from $C_k$ before taking the minimum with $A_k$ and $B_k$.

#### I. 948 Cap Only in $v=20$
- **Paper derivation** ([STRUCTURE_19_23.md:32-52](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_19_23.md#L32-L52)): $v=20$ uses the global pair-covering surplus $\lceil 130 / 6 \rceil = 22$ to cap ordered single-intersection pairs at $992 - 44 = 948$.
- **Lean implementation** ([Numeric.lean:81, 151-153](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L81)):
  Only `v20` sets `emptyPairCap := some 948`. All other 22 profiles set `emptyPairCap := none` (generated by [generate_numeric_certificate.py:38](file:///Users/rfy_naiveai/Desktop/aris4math/formal/generate_numeric_certificate.py#L38)). In `validProfile` ([Numeric.lean:132-133](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L132-L133)), non-empty cap is restricted to $v=20$ with empty lock types.

#### J. Static Profile Correspondence
- All 23 profiles in [`Numeric.lean:140-444`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Numeric.lean#L140-L444) match the case parameters in `results/reproduced_bounds.json` and the corresponding sections of [`STRUCTURE_19_23.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_19_23.md) and [`STRUCTURE_24_25.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_24_25.md):
  - $v=19$: 1 profile (`v19`), bound $222656/230945 < 1$.
  - $v=20$: 1 profile (`v20`), bound $20874/20995 < 1$.
  - $v=21$: 3 profiles (`v21_d5`, `v21_d6`, `v21_d7`), bounds $483/494$, $4179/4199$, $8337/8398 < 1$.
  - $v=22$: 3 profiles (`v22_66`, `v22_67`, `v22_77`), bounds $8193/8398$, $4092/4199$, $8175/8398 < 1$.
  - $v=23$: 3 profiles:
    - 2 successful: `v23_66` ($117203/117572 < 1$), `v23_677` ($645/646 < 1$).
    - 1 diagnostic: `v23_67` ($122609/117572 > 1$).
  - $v=24$: 3 profiles (`v24_K4_1`, `v24_K4_2`, `v24_K4_3`), all $< 1$.
  - $v=25$: 9 profiles:
    - 8 successful: `v25_K6_1`, `2`, `3`, `5`, `6`, `7`, `8`, `9`, all $< 1$.
    - 1 diagnostic: `v25_K6_4` ($8405/8398 > 1$).

---

### 3. Exact Semantic Bridges Not Established by Numeric.lean

Kernel verification of `Aris4Math.Numeric` proves arithmetic statements about static data records. It does **not** prove the top-level specification `Aris4Math.Target`. The unproved mathematical bridges are:

1. **Hypergraph Realizability of Profiles**:
   `Numeric.lean` takes the `Profile` records as given constants. It does not prove that for an arbitrary 32-edge pair-covering hypergraph $H$, there exists an assignment of locked vertices $S$ and positions $t_i$ yielding these exact type counts $\ell_T$.
2. **$v=20$ Pair Cap Justification**:
   The number $948$ in `v20` is an external input. The double-counting derivation $\sum \binom{\lambda_{xy}}{2} \ge 130 \implies \text{pairs} \ge 22 \implies M_{\varnothing\varnothing} \le 948$ is not verified in Lean.
3. **Classification Completeness and Avoidance**:
   - For $v=22, 23$: Exhaustiveness of the degree/codegree branches ($(6,6)$, $(6,7)$, $(7,7)$ for $v=22$; $(6,6)$ vs. $(6,7,7)$ for $v=23$) is not formalized.
   - For $v=24, 25$: The linear-space clique decomposition classifications ($K_4$ into 3 types, $K_6$ into 9 types) and the 7-vertex integer contradiction lemma avoiding $K_6$-4 are not connected to `Numeric.lean` in Lean.
4. **Permutation Counting and Probability Semantics (P1–P5)**:
   `Numeric.lean` defines rational formulas using `binom`. It does not formalize the probability space $\Omega$ of conditional permutations, does not prove that greedy coloring failure is contained in $\bigcup Q_k$, and does not prove that the closed-form fractions upper-bound $\Pr(Q_k)$.
5. **Link Slot Deduction Injection (P6, P8)**:
   The algorithm sorts `linkSlots` and takes the $q$ lowest-weight slots. It is not proved in Lean that the true set of intersecting link pairs injects into this slot list, nor that this relaxed minimum is a valid lower bound on the removable probability mass.
6. **Global Minimum Counterexample Reduction**:
   The reduction from arbitrary $H$ with $|E| \le 32$ to pair-covering hypergraphs with $v \in \{19, \dots, 25\}$, as well as the 2-colorability of cases $v \le 18$, is not formalized.
7. **Connection to `Aris4Math.Target`**:
   The main target `m(5) >= 33` remains unproved in Lean until these structural, probabilistic, and reduction bridges are formally verified and linked to `all_successful_values`.

