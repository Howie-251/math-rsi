# Global private-pair moment diagnostic

The proposed counting condition is correct. Root's subsequent pointwise repair bound gives the stronger presentation as a direct sufficient theorem, now written in `proofs/propertyb35/GLOBAL_PRIVATE_PAIR_REPAIR.md`. No assumption that the input is edge-critical, or that a prescribed deleted hypergraph is properly colored, is needed.

## 1. Exact counting and scope

For a uniform random red \(a\)-set in an \(n\)-vertex, \(M\)-edge, \(k\)-uniform simple hypergraph, \(k\ge2\), put

\[
 p=\frac{\binom{n-k}{a-k}+\binom{n-k}{a}}{\binom na},\qquad
 q=\frac{\binom{n-2k+1}{a-k}+\binom{n-2k+1}{a-k+1}}{\binom na}.
\]

Invalid binomial coefficients are zero. With \(n_1\) counting unordered edge pairs meeting in one vertex, the expected number of ordered private-pair events is exactly \(2n_1q\), including both orientations and both monochromatic colors. On a unique-bad-edge coloring, flipping each vertex of the bad edge either repairs the whole original input or exposes one of these events. Distinct vertices require distinct events. Consequently

\[
 Mp+2n_1q/k<2\quad\Longrightarrow\quad H\text{ has Property B}.
\]

This proves an actual coloring criterion; it does not prove that every input under the project target satisfies the inequality.

For \(k=5,M=35,a=\lfloor n/2\rfloor\), a non-B input must have the following exact counts:

| \(n\) | \(p\) | \(q\) | real lower bound for \(n_1\) | integer lower bound |
|---:|---:|---:|---:|---:|
|21,22|\(2/57\)|\(11/2261\)|\(1190/3\)|397|
|23,24|\(6/161\)|\(495/104006\)|\(36176/99\)|366|
|25|\(9/230\)|\(143/30590\)|\(96425/286\)|338|

For a pair-covering five-uniform input, \(W=\sum_v\binom{d_v}2\), \(T=\sum_{u<v}\binom{\lambda_{uv}}2\), and \(\tau=\sum_{u<v}\binom{\lambda_{uv}-1}2\) satisfy

\[
 n_1=W-2T+3n_3+8n_4,\qquad T=350-\binom n2+\tau.
\]

For A1, \(W=648\), so non-B implies

\[
 3n_3+8n_4-2\tau\ge29.
\]

In particular, this excludes every A1 input satisfying \(3n_3+8n_4-2\tau\le28\). The two individual bounds \(n_3\ge10\) or \(n_4\ge4\) are valid only when the other high-intersection count is zero. The mixed cases remain essential.

## 2. Complete intersection-distribution PSD relaxation

One tiny relaxation was considered, only for the A1 parameters. Its five variables are the real counts \(n_0,\ldots,n_4\). It imposes

\[
 n_j\ge0,\quad \sum_jn_j=595,\quad\sum_jj n_j=648,
 \quad n_2+3n_3+6n_4\ge140,\quad n_1\ge397,
\]

together with all six Johnson-scheme projection PSD inequalities on the 5-subsets of a 21-set. This has no variables for an original hypergraph or negative-edge layout. It retains the A1 degree sequence only through its moment \(W=648\); individual degree positions, the special six-degree star, and simultaneous point-pair realizability are relaxed.

For reproducibility, the PSD kernels were checked directly, with no reliance on a recalled eigenvalue convention. Write \(B_\ell(E,F)=\binom{|E\cap F|}{\ell}\). For \(0\le\ell\le5\), define six-entry rational kernels recursively by

\[
 K_\ell(s)=\frac{\binom s\ell-
 \sum_{j<\ell}\binom{5-j}{\ell-j}\binom{n-\ell-j}{5-\ell}K_j(s)}
 {\binom{n-2\ell}{5-\ell}}.
\]

For each \(n=21,\ldots,25\), `CHECK.py` verifies directly that the symmetric matrix \(K_\ell(|E\cap F|)\), indexed by all 5-subsets, is idempotent. It does so at the six possible entries, rather than forming a large matrix. If \(|E\cap F|=s\), the number of 5-subsets \(Z\) with \(|Z\cap E|=u\), \(|Z\cap F|=v\) is

\[
 C_s(u,v)=\sum_h\binom sh\binom{5-s}{u-h}
                 \binom{5-s}{v-h}\binom{n-10+s}{5-u-v+h}.
\]

The exact identity checked is

\[
 \sum_{u,v=0}^5 C_s(u,v)K_\ell(u)K_\ell(v)=K_\ell(s)
 \quad(s=0,\ldots,5).
\]

A symmetric idempotent matrix is positive semidefinite. Thus the six inequalities actually used in the relaxation are rigorously necessary:

\[
 35K_\ell(5)+2\sum_{s=0}^4n_sK_\ell(s)\ge0.
\]

This exact finite entry check also avoids treating a floating-point PSD assertion as a mathematical premise.

## 3. The relaxation is feasible

A HiGHS prototype found feasibility; the saved conclusion is instead established by exact rational substitution. The **integer abstract intersection distribution**

\[
 (n_0,n_1,n_2,n_3,n_4)=(78,397,110,9,1)
\]

has \(W=648\), \(T=143\), \(\tau=3\), and

\[
 3n_3+8n_4-2\tau=29.
\]

Its six PSD quadratic forms are, in levels zero through five,

\[
 \frac{175}{2907},\quad\frac1{306},\quad\frac{21}{340},\quad
 \frac{35852}{14535},\quad\frac{305479}{39780},\quad\frac{54651}{2210},
\]

all positive. This explicitly shows why neither the degree moments nor these complete edge-intersection PSD inequalities contradict the new necessary condition. It also illustrates a surviving mixed case with \(n_3<10\) and \(n_4<4\).

For an additional exact check, the relaxation has maximum

\[
 n_1=\frac{1664}{3},
\]

attained by \((17,1664/3,0,0,70/3)\). Indeed,

\[
 W-\frac23T=n_1+\frac43n_2+n_3\ge n_1,
 \qquad T\ge140,
\]

so \(n_1\le648-280/3=1664/3\). The displayed optimizer meets every PSD inequality, as verified with Fractions. No numerical optimality assertion is needed.

Neither displayed distribution is claimed to be realizable by a family of 35 actual edges, much less by an A1 pair-covering hypergraph. No hypergraph was generated or searched.

## 4. Useful remaining mathematical interface

The new general repair criterion closes the subfamily having sufficiently few intersection-one edge pairs. For A1, any remaining counterexample has the genuine high-intersection budget \(3n_3+8n_4\ge29+2\tau\). For example, at \(\tau=0\), \(n_4=0,1,2,3\) respectively force \(n_3\ge10,7,5,2\).

To turn this into a full A1 proof, a new argument must use actual high-intersection edges or simultaneous point-codegree/degree structure. More inequalities depending only on the same five edge-intersection counts would need to exclude the exact feasible distributions above. This diagnostic does not supply that missing argument, and no new local scan was launched.

## 5. Reproduction and actual reading/calculation scope

Run from the project root:

```sh
.tools/math-python/bin/python context/propertyb35-paper/round01/middle/global_private_pair_moments_20261020/CHECK.py
```

The standard-library Fraction replay checks all five threshold rows, 180 exact projector-idempotence entry identities across \(n=21,\ldots,25\), the A1 integer feasible witness, and the rational optimum witness. Actual result: PASS, about 0.0093 CPU seconds on this run. Exact values are in `CHECK.json`.

This was a mathematical counting/finite scalar task. No new literature, original-H enumeration, Lean build, MCP call, or wiki/navigation edit was performed. The new canonical theorem and this report are subject to the parent agent's review; no cross-family acceptance is asserted here.
