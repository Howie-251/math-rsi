# A uniform conditional-permutation framework for Property B: certified bounds for 8- and 9-uniform hypergraphs

## Results and status

**Theorem A (exact-rational computer-assisted proof candidate).** Every simple 8-uniform hypergraph with at most 265 edges has Property B. Hence **\(m(8)\ge266\)**.

**Theorem B (exact-rational computer-assisted proof candidate).** Every simple 9-uniform hypergraph with at most 541 edges has Property B. Hence **\(m(9)\ge542\)**.

The mathematical selection lemmas and exact finite profile ranges are proved below. All the finite rational comparisons are certified by the accompanying standalone standard-library Python script `propertyB_m8_certificate_v2.py` and `propertyB_m9_certificate_v2.py`. The script has been run for both cases. These results have **not** been independently peer-reviewed or Lean-verified.

The previously published comparison is Grill–Linzmayer (2024, arXiv:2403.05674v3), Theorem 1: \(m(8)\ge263\), \(m(9)\ge538\).

## 1. Reduction

Assume a non-Property-B \(k\)-uniform hypergraph with at most \(M\) edges exists; choose one with the smallest number \(v\) of vertices. Identifying any pair of vertices not in a common edge would produce a smaller counterexample without increasing the number of edges; hence its codegrees satisfy \(\lambda_{xy}\ge1\). Consequently,

\[
(k-1)d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1,\qquad
\sum_xd(x)=km\le kM.
\]

Thus \(v\lceil (v-1)/(k-1)\rceil\le kM\). Balanced random coloring excludes any \(v\) for which

\[
M\frac{\binom{\lfloor v/2\rfloor}{k}+\binom{\lceil v/2\rceil}{k}}{\binom vk}<1.
\]

For \((k,M)=(8,265)\), this gives \(47\le v\le120\). For \((k,M)=(9,541)\), it gives \(57\le v\le194\). For \(v<2k-1\), two color classes with at most \(k-1\) vertices directly suffice. Add distinct edges to reach exactly \(m=M\); this preserves pair coverage and a counterexample, and is possible since \(\binom vk\ge M\) in both candidate intervals.

## 2. Generic conditioned greedy bound

Take a uniformly random permutation conditioned on fixed distinct vertices \(s_i\) occupying fixed distinct positions \(t_i\), and greedily recolor each vertex blue if it is the final vertex of a presently all-red edge; otherwise leave it red. The final coloring has no red monochromatic edge. If there is a blue monochromatic edge \(B\), its first vertex \(x\) is the last vertex of another edge \(A\), and \(A\cap B=\{x\}\). Thus failure is covered by ordered **critical pairs**.

Write \(T\subseteq [s]\) for the exact set of locked vertices in an edge, \(\ell_T\) for the count of its type and \(r_T=k-|T|\), \(N=v-s\). At a position \(h\), write \(a_h,b_h\) for the numbers of free positions before and after \(h\). The allowed preceding/succeeding lock masks are \(I_h^-,I_h^+\). For a genuinely single-intersection ordered pair of types \(T,U\), its critical probability is

\[
w_h(T,U)=
\begin{cases}
\displaystyle\frac{\binom{a_h}{r_T-1}\binom{b_h}{r_U-1}}{N\binom{N-1}{r_T-1}\binom{N-r_T}{r_U-1}},&h\text{ free, }T\subseteq I_h^-,\ U\subseteq I_h^+,\ r_T+r_U-1\le N,\\[3mm]
\displaystyle\frac{\binom{a_h}{r_T}\binom{b_h}{r_U}}{\binom N{r_T}\binom{N-r_T}{r_U}},&h=t_j,\ T\cap U=\{j\},\ T\setminus\{j\}\subseteq I_h^-,\ U\setminus\{j\}\subseteq I_h^+,\ r_T+r_U\le N,\\[3mm]
0,&\text{otherwise.}
\end{cases}
\]

A locked center cannot have its incident locked vertices in the wrong order. For a free center, both incident edge types must respect the earlier/later locked vertices. Binomial coefficients are zero when their lower argument exceeds the upper argument.

Let \(A_h\) and \(B_h\) be the sums of exact one-edge endpoint probabilities of ending/starting at \(h\), respectively, and let

\[
C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf 1_{T=U})w_h(T,U).
\]

The latter bounds true critical-pair probability because it replaces the number of genuinely single-intersection pairs by the number of all distinct ordered pairs in each type cell.

For a locked center \(s_j\), link counting yields at least

\[
q_j=\left\lceil\frac{(k-1)d(s_j)-(v-1)}{k-2}\right\rceil
\]

distinct unordered incident-edge pairs that share another vertex. None can be critical. For each unordered type cell \(\{T,U\}\) of edges incident to \(s_j\), there are at most \(\binom{\ell_T}{2}\) available unordered pairs when \(T=U\), or \(\ell_T\ell_U\) when \(T\ne U\); each has nonnegative removable accounting weight \(w_{t_j}(T,U)+w_{t_j}(U,T)\). Sum the \(q_j\) cheapest available such weights, counting cells with multiplicity: call this \(D_{t_j}\). Then every possible placement of at least \(q_j\) actual bad pairs has total removable weight at least \(D_{t_j}\). At free positions set \(D_h=0\).

Therefore the conditional failure probability is at most

\[
\boxed{U(v,t,\ell)=\sum_{h=1}^v\min\{A_h,B_h,C_h-D_h\}}.
\]

If this is below 1, the hypergraph is 2-colorable.

For no locks, the global pair surplus yields at least

\[
Q_v=\max\left\{0,\left\lceil\frac{M\binom k2-\binom v2}{\binom{k-1}2}\right\rceil\right\}
\]

unordered multi-intersection pairs. So in the no-lock stage, replace the total number of ordered critical-pair candidates \(M(M-1)\) by \(M(M-1)-2Q_v\).

## 3. The single- and double-lock selection lemmas

A minimal-degree vertex \(x\) has degree

\[
\lceil(v-1)/(k-1)\rceil\le d(x)\le\lfloor kM/v\rfloor.
\]

For one lock, put \(x\) at position \(\lfloor v/2\rfloor\), with \(\ell_\varnothing=M-d(x)\), \(\ell_x=d(x)\).

For two locks, let \(x\) be a minimum-degree vertex of degree \(d\). Its codegree surplus is \(e=(k-1)d-(v-1)\). Hence at least

\[
s=(v-1)-e=2(v-1)-(k-1)d
\]

other vertices \(y\) satisfy \(\lambda_{xy}=1\). In all two-lock ranges below, \(s>0\). Let \(B\ge d\) be the smallest integer for which

\[
vd+s(B+1-d)>kM.
\]

If every such \(y\) had degree at least \(B+1\), the sum of degrees would exceed \(kM\), a contradiction. Thus there is \(y\) of degree \(d\le d(y)\le B\), with \(\lambda_{xy}=1\). Lock \(x,y\) at positions \((\lfloor v/2\rfloor,\lfloor v/2\rfloor+1)\). Their exact edge-type profile is

\[
\ell_{xy}=1,\quad \ell_x=d-1,\quad \ell_y=d(y)-1,\quad
\ell_\varnothing=M-d-d(y)+1.
\]

The certificate loops through every \(d\) in the minimum-degree range and every \(d(y)\in[d,B]\); there is no assumption that some particular degree combination must exist.

## 4. Unified three-lock Caro–Wei lemma

**Lemma.** Let \(H\) be a pair-covering \(k\)-uniform hypergraph with \(m=M\) edges. Put \(d_0=\lceil(v-1)/(k-1)\rceil\) and choose \(D\ge d_0\). Assume

\[
Z=(D+1)v-kM>0,
\qquad
2(k-1)Z>\bigl((k-1)(D+1)-v+2\bigr)^2.
\tag{CW}
\]

Then there exist three vertices \(x,y,z\), each of degree at most \(D\), with all three pairwise codegrees equal to 1.

*Proof.* Let \(L=\{x:d(x)\le D\}\), \(r=|L|\). Since vertices outside \(L\) have degree at least \(D+1\), and total degree is \(kM\), \(Z>0\) implies \(r>0\). Make an auxiliary graph \(G\) on \(L\), joining vertices of codegree greater than 1. Each vertex of \(L\) has at most \((k-1)d(x)-(v-1)\) neighbors in \(G\). Summing, with \(\sum_{x\in L}d(x)\le kM-(D+1)(v-r)\),

\[
2e(G)\le Ar+B,
\quad A=(k-1)(D+1)-(v-1),\quad B=(k-1)(kM-(D+1)v)=-(k-1)Z.
\]

By Caro–Wei followed by Cauchy–Schwarz, \(\alpha(G)\ge r^2/(r+2e(G))\ge r^2/((A+1)r+B)\). We have

\[
r^2-2((A+1)r+B)=(r-(A+1))^2+2(k-1)Z-(A+1)^2>0
\]

by (CW), hence \(\alpha(G)>2\). Any three vertices of an independent set have pairwise codegree 1. \(\square\)

For three pairwise codegree-1 vertices with degrees \(d_1\le d_2\le d_3\le D\), their exact types are of one of two forms:

* **One triple edge:** \(\ell_{xyz}=1\), \(\ell_x=d_1-1,\ell_y=d_2-1,\ell_z=d_3-1\), \(\ell_\varnothing=M-(d_1+d_2+d_3)+2\).
* **Three separate pair edges:** \(\ell_{xy}=\ell_{xz}=\ell_{yz}=1\), \(\ell_x=d_1-2,\ell_y=d_2-2,\ell_z=d_3-2\), \(\ell_\varnothing=M-(d_1+d_2+d_3)+3\).

Lock the three points at \((\lfloor v/2\rfloor-1,\lfloor v/2\rfloor,\lfloor v/2\rfloor+1)\). Checking all \(d_0\le d_1\le d_2\le d_3\le D\) in both forms suffices.

## 5. Instantiations of the three-lock lemma

* **\(k=8,M=265,v=108,\ldots,120,D=20\):** Here \(kM=2120\), \(Z=21v-2120\), \(A+1=149-v\). The (CW) gap is

\[
14(21v-2120)-(149-v)^2\ge391>0,
\]

where the minimum occurs at \(v=108\). Thus three suitable locks exist throughout the range. The certificate checks 700 three-lock profiles.

* **\(k=9,M=541,v=183,\ldots,194,D=28\):** Here \(kM=4869\), \(Z=29v-4869\), \(A+1=234-v\). The (CW) gap is

\[
16(29v-4869)-(234-v)^2\ge4407>0,
\]

where the minimum occurs at \(v=183\). Thus three suitable locks exist throughout the range. The certificate checks 936 three-lock profiles.

The Caro–Wei use is crucial: a simple bound based only on the maximum degree of \(G\) would not force a triple in every part of these ranges.

## 6. All finite verification branches and results

The implementation evaluates all fractions exactly (`fractions.Fraction`), with no floating-point comparison in the proof test.

| Result | Vertex range | Method | Number of exact profiles | Worst U in branch |
|---|---:|---|---:|---|
| \(m(8)\ge266\) | 47–84 | no locks | 38 | 1979153923656815602/1985567608105406325 |
|  | 85–94 | 1 lock | 111 | 143069864934103397/143211910248511236 |
|  | 95–107 | 2 locks | 441 | 491423928434682146/492001961412997035 |
|  | 108–120 | 3 locks | 700 | 21583550469172616239/21708585360805549635 |
| **Total** | | | **1290** | all <1 |
| \(m(9)\ge542\) | 57–139 | no locks | 83 | 4863399653443677633091/4864892534121183467475 |
|  | 140–154 | 1 lock | 225 | 2189630134274718894978663/2191584453807237426487550 |
|  | 155–182 | 2 locks | 1324 | 382302187427945065441709/382387455366150843293685 |
|  | 183–194 | 3 locks | 936 | 471963185043213974227303/476249827247335799582925 |
| **Total** | | | **2568** | all <1 |

All these numerators are strictly smaller than their denominators.

Thus if a non-Property-B hypergraph with at most 265 eight-edges or at most 541 nine-edges existed, the reduction and selection lemmas would put it in one of the checked profiles, which yields failure probability <1 and hence a successful two-coloring, a contradiction.

**Conclusion:** \(\boxed{m(8)\ge266,\quad m(9)\ge542}\) conditional only on the explicitly stated mathematical lemmas (proved above) and the finite, reproducible exact arithmetic checks.

## Reproduction

```bash
python3 propertyB_m8_certificate_v2.py
python3 propertyB_m9_certificate_v2.py
```

No third-party Python dependencies. The script checks the balanced-coloring and upper-v reductions, all one- and two-lock degree ranges, all Caro–Wei selection inequalities (including every feasible cardinality of the low-degree set), and every rational profile.

**Verification status:** a reproducible computer-assisted proof candidate, not a statement of Lean verification or independent peer review.
