### Files Read & Execution Status

- **Files Read**:
  1. [context/propertyb-general/round02/baseline-comparison/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round02/baseline-comparison/REPORT.md) (full text, lines 1–262)
  2. [context/propertyb-general/round02/baseline-comparison/SOURCES_FINAL.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb-general/round02/baseline-comparison/SOURCES_FINAL.md) (full text, lines 1–113)
  3. [ref/source_packages/grill_linzmayer_2403_05674/PropB.tex](file:///Users/rfy_naiveai/Desktop/aris4math/ref/source_packages/grill_linzmayer_2403_05674/PropB.tex) (full text, lines 1–538, specifically checking eqs. (3)–(8), the two $\gamma$ bounds on lines 234–238, and Theorems 1–2)
  4. [proofs/propertyb-general/BASELINE_COMPARISON.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md) (full text, lines 1–350)
- **Computation Executed**: **None** (purely static mathematical verification; read-only).

---

### Audit Verdicts (Obligations 1–4)

#### 1. $L_{\rm GR}(k) \le 2^k < B_{\rm RS}(k) + 1$ for all $k \ge 32$
- **Verdict: SOUND (No mathematical or quantifier issues).**
- **Verification**:
  - **Quantifiers & Endpoint Rounding**: Matching [PropB.tex eqs. (3)–(5)](file:///Users/rfy_naiveai/Desktop/aris4math/ref/source_packages/grill_linzmayer_2403_05674/PropB.tex#L85-L97), a vertex-minimal counterexample $H$ on $v$ vertices with $m$ edges satisfies $v \ge 2k-1$ (since $v \le 2k-2$ is 2-colorable by splitting into $\lfloor v/2 \rfloor, \lceil v/2 \rceil \le k-1$), covers all vertex pairs (so $m \ge S_k(v) = \lceil \frac{v}{k}\lceil \frac{v-1}{k-1}\rceil \rceil$), and has expected monochromatic edges $m / R_k(v) \ge 1$ under a random balanced coloring (so $m \ge \lceil R_k(v) \rceil$, without an invalid $+1$ at integer values of $R_k(v)$). Thus $m(k) \ge L_{\rm GR}(k) = \min_{v \in \mathbb{Z},\, v \ge 2k-1} \max\{S_k(v), \lceil R_k(v) \rceil\}$.
  - **Selected $v$**: Choosing $q = 2^{\lfloor k/2 \rfloor}$ and $v = (k-1)q \ge 2k-1$ ([BASELINE_COMPARISON.md §3](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md#L88-L115)) gives $\lceil (v-1)/(k-1) \rceil = \lceil q - 1/(k-1) \rceil = q$, hence $S_k(v) = \lceil (k-1)q^2/k \rceil \le q^2 \le 2^k$. For $k \ge 32$, $q \ge 2^{k/2-1} > 8k \implies v > 8k(k-1) > 4k^2$, so the monochromatic edge probability in a balanced coloring satisfies $P = 1/R_k(v) \ge 2^{1-k}(1 - 2k/v)^k \ge 2^{1-k}(1 - 2k^2/v) > 2^{-k}$. Thus $R_k(v) < 2^k$, and since $2^k \in \mathbb{Z}$, $\lceil R_k(v) \rceil \le 2^k$. Combined with $B_{\rm RS}(k) \ge 2^k$, $L_{\rm GR}(k) \le 2^k < B_{\rm RS}(k) + 1$ holds for all $k \ge 32$.

---

#### 2. Necessary-Data Relaxation for Grill's Eq. (8) Exceeds $1$ for All $k \ge 256$ and Every $M > B_{\rm RS}(k)$
- **Verdict: SOUND (All indexing, bounds, and error margins hold across both $\kappa \le 3k$ and $\kappa \ge 3k$).**
- **Verification**:
  - **Grill Eq. (8) & $+3$ Indexing / Normalization ([BASELINE_COMPARISON.md §7](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md#L254-L278))**:
    In [PropB.tex eq. (8)](file:///Users/rfy_naiveai/Desktop/aris4math/ref/source_packages/grill_linzmayer_2403_05674/PropB.tex#L190-L209), the $h=0$ summand is $0$. Restricting $h \in \{1, \dots, v\}$ to $h \in \{k-1, \dots, v-k+2\}$ and setting $j = h - k + 1$ maps $h$ bijectively to $j \in \{0, \dots, N\}$ with $N = (v - k + 2) - (k - 1) = v - 2k + 3$. With $r = k-1$ and $s = N/v \in (0,1)$, the smallest factors in the numerator falling factorials $(h-1)_r = (j+r-1)_r$ and $(v-h)_r = (N-j+r-1)_r$ are $j$ and $N-j$ respectively, while $(v-1)_r, (v-k)_r \le v^r$. Using $s^r \ge s^{2r}$ on the two endpoint terms yields $\frac{s^{2r}}{v} f(j/N)$ per term. Since $f(x)$ is unimodal and symmetric on $[0,1]$ with peak $L = f(1/2) = \min\{\kappa k, \gamma/d^2\}$, $\operatorname{TV}(f) \le 2L$, so $\sum_{j=0}^N f(j/N) \ge NC - 2L$, giving the exact algebraic lower bound (B14):
    $$D_k(v, M, \gamma) \ge s^{2k-1} C - \frac{2s^{2k-2}}{v} L.$$
  - **Integer Choices $T = \lfloor M/k^{16} \rfloor, D = M - T$ & Test Admissibility ([BASELINE_COMPARISON.md §6](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md#L180-L253))**:
    For $k \ge 256$ and $M > B_{\rm RS}(k) \ge 2^k$, $t = \sqrt{M} \ge 2^{k/2} > 300 k^{10}$ (since $2^{128} = 2^{48}\cdot 2^{80} > 300\cdot 256^{10}$ and $\frac{\log 2}{2} - \frac{10}{x} > 0$). Thus $1 \le T \le M/k^{16}$ and $D < M$. Splitting $(k-1)D = \sum_{i=1}^{v-1} c_i$ and $kT = \sum_{i=1}^{v-1} b_i$ nearly equally among $n = v-1 = \lfloor (k-2)t \rfloor - 1$ non-center vertices gives $t \le c_i \le 2t$, $0 \le b_i \le t/2$, $d_0 = D \in [M/2, M-1]$, $d_i = c_i + b_i \in [t, 5t/2]$. All scalar/row-capacity tests (1)–(4) and the balanced coloring failure $MP > 1$ (B12) are satisfied. For the two cited $\gamma$ bounds in [PropB.tex lines 234–238](file:///Users/rfy_naiveai/Desktop/aris4math/ref/source_packages/grill_linzmayer_2403_05674/PropB.tex#L234-L238), both $\Gamma_1 = M(M-1) - R(R-1)$ and $\Gamma_2 = \sum_i [d_i(d_i-1) - r_i(r_i-1)]$ satisfy $\Gamma = \min(\Gamma_1, \Gamma_2) \ge \Lambda = D(D-1) - R(R-1)$, with $\gamma_0 - \Lambda \le 2MT + 4M$ and $\Lambda \ge M^2/2$.
  - **Case $2 \le \kappa \le 3k$ & FKG Gap ([BASELINE_COMPARISON.md §8](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md#L279-L323))**:
    By the identity $C_k(M, \Lambda) = \min_{p \in [0,1]} \{\kappa(1-p)^k + q J_k(p)\}$ ($q = \Lambda/d^2 \ge \kappa^2/2$), either $q \ge \kappa k$ ($p_*=0, C=\kappa \ge 2$) or $0 < p_* = (\kappa k/q)^{1/r} - 1 \le k^{1/(k-1)} - 1 \le \frac{2\log k}{k} < \frac{1}{2}$, giving $z = (1-p_*)^k \ge e^{-2kp_*} \ge k^{-4}$. The FKG gap $h_\kappa(z) = \kappa z - 1 + (1-z)^\kappa \ge z^2 \ge k^{-8}$ (for $\kappa \ge 2$) together with $F_0(M, p_*) \ge 1$ (from $M > B_{\rm RS}(k)$) and $\frac{\gamma_0 - \Lambda}{d^2} J_k(p_*) \le 2\kappa^2 k^{-16} + \frac{4\kappa^2}{M} \le 18 k^{-14} + \frac{36k^2}{M}$ yields $C \ge 1 + k^{-8} - 18k^{-14} - \frac{36k^2}{M}$. Subtracting the discretization loss $\frac{(2k-1)(2k-3)C + 2L}{v} \le \frac{30k^3}{v} \le \frac{60k^2}{t}$ and using $t > 300k^{10}$ gives:
    $$D_k(v, M, \Lambda) > 1 + k^{-8} - 18k^{-14} - \frac{96k^2}{t} > 1 + \left(1 - \frac{1}{3} - \frac{96}{300}\right) k^{-8} > 1.$$
  - **Case $\kappa \ge 3k$ ([BASELINE_COMPARISON.md §9](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md#L324-L340))**:
    Here $q = \Lambda/d^2 \ge \kappa^2/2 \ge \frac{3}{2}\kappa k > \kappa k$, so $p_* = 0$, $C = \kappa$, and $L = \kappa k$. Directly from (B14), $D_k(v, M, \Lambda) \ge \kappa[1 - (4k^2+2k)/v] \ge \kappa/2 > 1$. This covers every integer $M > B_{\rm RS}(k)$ without assuming downward closure of accepted budgets.

---

#### 3. Coverage of Applicable Published General Bounds in the Cited Primary Sources
- **Verdict: COMPLETE AND ACCURATELY SCOPED (No missing applicable published theorem or fabricated finite endpoint).**
- **Verification**:
  - In [BASELINE_COMPARISON.md §4](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md#L116-L140), the substitution $x = (1-p)/2$ establishes the exact identity $C_k(M, \gamma) = \min_{p \in [0,1]} \{\kappa(1-p)^k + (\gamma/d^2) J_k(p)\}$, and $1 - (1-z)^\kappa \le \kappa z$ (for $\kappa \ge 1$) together with $J_k(p) \le p$ and $C_k(M, \gamma_0) \le \gamma_0 \beta_k$ proves that for $k \ge 32$:
    $$B_{\rm pair}(k) \le B_{\rm cont}(k) \le B_{\rm RS}(k) \quad \text{and} \quad B_{\rm lin}(k) \le B_{\rm RS}(k).$$
    Combined with $L_{\rm GR}(k) \le 2^k < B_{\rm RS}(k) + 1$ (and Herzog–Schönheim $\frac{k}{k+2}2^k < 2^k$), the reference envelope $L_{\rm ref}(k)$ in (B2) equals $B_{\rm RS}(k) + 1$ for all $k \ge 32$.
  - Asymptotic statements in RS (2000) and CK (2015) ($\liminf \ge 1/\sqrt{2}$) are derived by optimizing the finite criterion $B_{\rm lin}(k)$ and do not provide an explicit finite $k_0(\varepsilon)$ or a closed-form finite bound stronger than $B_{\rm lin}(k) \le B_{\rm RS}(k)$.
  - In [PropB.tex](file:///Users/rfy_naiveai/Desktop/aris4math/ref/source_packages/grill_linzmayer_2403_05674/PropB.tex#L368-L471), Theorem 1 applies only to $k \in \{5,\dots,9\}$, Theorem 2 applies only to fixed $v = 2k+1$ ($\mathbf{m}(k, 2k+1)$), and general-$k$ multi-lock is explicitly described in §5 as a future hope rather than an established formula.

---

#### 4. Assessment of Full Composition Across the Four Proof Documents
- **Verdict: SOUND AND READY FOR ACCEPTANCE (No blocking mathematical gaps).**
- **Synthesis**:
  1. Combining [CORE_THEOREM.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CORE_THEOREM.md), [UNIFORM_INTEGER_GAIN.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md), and [CLIQUE_REFINEMENT.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/CLIQUE_REFINEMENT.md) yields an unconditional theorem for all finite simple $k$-uniform hypergraphs on $k \ge 17$:
     $$m(k) \ge B_{\rm RS}(k) + 1 + \left\lfloor \frac{\sqrt{B_{\rm RS}(k)}}{8(1 + \log k)} \right\rfloor,$$
     where the integer gain $\left\lfloor \frac{\sqrt{B_{\rm RS}(k)}}{8(1 + \log k)} \right\rfloor \ge 10 \ge 1$ is strictly positive for all $k \ge 17$.
  2. Combining this with [BASELINE_COMPARISON.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md) establishes that for $k \ge 32$, the bound strictly improves upon the entire published reference envelope $L_{\rm ref}(k) = B_{\rm RS}(k) + 1$ by $\left\lfloor \frac{\sqrt{B_{\rm RS}(k)}}{8(1 + \log k)} \right\rfloor$, and for $k \ge 256$, it also strictly exceeds the maximum fixed-$M$ budget accepted by the explicitly specified zero-lock discrete necessary-data test scheme of Grill–Linzmayer eq. (8) with the two cited degree/max-codegree $\gamma$ bounds.
  3. Both mathematical deductions and scope/attribution statements in [BASELINE_COMPARISON.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb-general/BASELINE_COMPARISON.md) are accurate; no edits or corrections are required.

