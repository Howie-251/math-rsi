# Independent two-flip path check

The proposed two-flip theorem and all supplied 21/22-point coefficients are correct. The complete new theorem is written in `proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md` (185 lines). This report records the independent checks and the exact remaining moment-level obstruction.

## 1. The original-edge risk classification is complete

Start with a unique monochromatic edge \(G\) of color \(c\). Suppose \(g\in G\) has exactly one private original edge \(F_g\), and let \(h\in F_g\setminus\{g\}\). Initially \(g,h\) have opposite colors. After simultaneously flipping them:

- \(G\) and \(F_g\) are both proper, including at \(k=2\).
- An edge containing both flipped vertices remains bichromatic; an edge containing neither does not change.
- A new edge of the color opposite to \(c\) would be another \(g\)-private edge avoiding \(h\), contrary to uniqueness of \(F_g\).
- Every remaining new bad edge \(J\) has \(h\) as its unique vertex initially opposite to \(c\), and avoids \(g\).

Such \(J\) automatically satisfies \(F_g\cap J=\{h\}\). Different \(h\) supply different ordered paths, since their singleton intersections with \(F_g\) differ. Paths arising at different \(g\) have different middle edges. Thus no multiplicity is lost in

\[
 Z\ge(k-1)(2k-S)_+
\]

on a failed unique-bad-edge coloring. With \(I_2\) the algorithm's failure indicator, the claimed pointwise bound is valid:

\[
 I_2\le X/2+(S+Z/(k-1))/(4k).
\]

The corresponding expected sufficient criterion is exactly

\[
 \mathbb EX+[\mathbb ES+\mathbb EZ/(k-1)]/(2k)<2.
\]

It gives an actual proper coloring of the full original input; it has no criticality or deleted-hypergraph hypothesis.

## 2. Path expectation, orientation and middle capacity

A structural path with outer intersection size \(j\) prescribes \(2k-1-j\) vertices of color \(c\), \(k-1\) of its opposite color, and \(3k-2-j\) vertices altogether. Its two-color event probability is therefore

\[
 r_j=\frac{\binom{n-3k+2+j}{a-2k+1+j}
              +\binom{n-3k+2+j}{a-k+1}}{\binom na}.
\]

For each unordered outer pair there are two orientations, each with the same middle-edge count and probability \(r_j\). Thus the factor two in \(\mathbb EZ=2\sum_j C_jr_j\) is correct.

Each valid middle edge meets each outer difference in one vertex. Summing \(d_v-1\) over either outer difference counts that middle edge exactly once, excludes the corresponding outer edge, and can only overcount other edges. Hence

\[
 c(G,J)\le\min\{M-2,\sum_{G\setminus J}(d_v-1),
                         \sum_{J\setminus G}(d_v-1)\}
 \le\min\{M-2,(k-j)(\Delta-1)\}.
\]

This is a safe upper bound on the unconditional expected failure certificate; it does not assert independence between different repair trials.

## 3. Exact supplied arithmetic

For \(n=21,22,k=5,M=35,\Delta\le9\), use \(D=352716\). The checked vectors are

\[
 Dr=(36,120,330,792,1716),\quad c=(33,32,24,16,8),
\]

and the sufficient condition is

\[
 L=594n_0+5352n_1+3960n_2+6336n_3+6864n_4<2722720.
\]

The 22-point balanced denominator doubles both the ordinary numerator and denominator, leaving these probabilities unchanged.

For A1, the moment substitution is exactly

\[
 L=2575614+9918n_3+24138n_4-6150\tau.
\]

Thus non-B requires \(9918n_3+24138n_4-6150\tau\ge147106\), equivalently \(\ge147108\) because this expression is a multiple of six. With \(n_4=\tau=0\), this now forces \(n_3\ge15\); with \(n_3=\tau=0\), it forces \(n_4\ge7\). Mixed cases must still be retained.

The previous feasible integer moment distribution \((78,397,110,9,1)\) gives \(L=2670564\), so it is excluded by the new criterion, exactly as proposed.

## 4. Tiny intersection-distribution relaxation still feasible

Only the five edge-intersection counts were varied. The constraints were nonnegativity, \(\sum n_j=595\), the stated \(W\), the pair-covering lower bound on \(T\), the old one-flip necessary bound, the new two-flip necessary bound, and all six Johnson projection PSD inequalities already exactly checked by the preceding task. No original hypergraph or negative layout was generated.

A HiGHS prototype was feasible in both requested parameter cases. The following **integer abstract distributions**, verified by exact substitution, prove feasibility without relying on numerical solver status:

| Diagnostic parameters | \((n_0,n_1,n_2,n_3,n_4)\) | \(W\) | \(T\) | gap in the new necessary inequality before clearing denominators |
|---|---|---:|---:|---:|
|21, \(\Delta\le9\)|\((72,413,95,15,0)\)|648|140|\(32/6783\)|
|23, \(\Delta\le8\)|\((105,403,85,0,2)\)|581|97|\(53195/1352078\)|

All six PSD forms are nonnegative for each; their exact values are saved in `CHECK.json`. The first distribution has \(L=2724384\), just above the necessary threshold. Neither distribution is claimed to be simultaneously realizable by actual edges and the prescribed vertex degrees.

For reference, the exact 23-point sufficient inequality is

\[
 5445n_0+39600n_1+27027n_2+42042n_3+45045n_4<18811520.
\]

This uses \(r=(165,495,1287,3003,6435)/1352078\) and \(c=(33,28,21,14,7)\). It also excludes the \(W=581,T=97\) distribution \((111,387,97,0,0)\), which survived the one-flip bounds. The table above records a surviving mixed distribution.

## 5. Reproduction and exact acceptance scope

Run

```sh
.tools/math-python/bin/python context/propertyb35-paper/round01/middle/global_private_pair_moments_20261020/two_flip_path_20261020/CHECK.py
```

Actual result: PASS; 259 local originally proper edge-color types for \(k=2,\ldots,6\), private multiplicities 1–4 at each vertex in those dimensions, the exact probability/coefficient identities, the old witness exclusion, and the two new feasible distributions. Actual CPU was approximately 0.0121 seconds. The local check supports the classification; the canonical proof is general and does not infer arbitrary \(k\) from this finite sample.

The PSD arithmetic reuses only the exact six-entry kernels from the previous `../CHECK.py`; it does not rerun an H search or enlarge any local inventory. No Lean, MCP, wiki or navigation changes were made. The parent agent still owns full mathematical acceptance and any cross-family review. The two-flip criterion strengthens the available actual sufficient conditions, but this task does not close A1 or the 23-point original branch.
