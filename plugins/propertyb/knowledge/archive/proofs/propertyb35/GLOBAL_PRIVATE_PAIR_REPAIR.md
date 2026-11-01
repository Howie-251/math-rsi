# Global private-pair repair

**Status: PROVABLE AS STATED.** The theorem below gives a sufficient condition for Property B and a corresponding necessary condition for a counterexample. It does not assert that every five-uniform hypergraph with at most 35 edges meets the sufficient condition.

## 1. Objects and probabilities

Let \(H\) be a finite simple \(k\)-uniform hypergraph on \(n\) vertices, where \(k\ge2\), \(n\ge k\), and \(M=|H|\). Fix an integer \(0\le a\le n\), and choose the red vertex set uniformly among the \(a\)-subsets. All remaining vertices are blue.

Write \(n_1\) for the number of **unordered pairs of distinct edges** whose intersection has size exactly one. Put

\[
 p=\frac{\binom{n-k}{a-k}+\binom{n-k}{a}}{\binom na}
   =\frac{\binom ak+\binom{n-a}k}{\binom nk},
 \qquad
 q=\frac{\binom{n-2k+1}{a-k}+\binom{n-2k+1}{a-k+1}}{\binom na}.
\]

A binomial coefficient is zero unless its upper and lower arguments are integers satisfying \(0\le v\le u\). In particular, when \(n<2k-1\), the displayed numerator for \(q\) is zero, and there are no edge pairs intersecting in exactly one vertex.

For a coloring, let \(X\) be its number of monochromatic edges. Define \(S\) as the number of **ordered pairs** \((E,F)\) of distinct edges such that:

1. \(E\cap F=\{g\}\) for one vertex \(g\);
2. \(E\) is monochromatic;
3. every vertex of \(F\setminus\{g\}\) has the color opposite to \(E\).

Both possible colors of \(E\) are included in this definition. Consequently,

\[
 \mathbb E X=Mp,\qquad \mathbb E S=2n_1q.
\]

For the second identity, each unordered intersecting pair contributes its two orientations. For any fixed orientation, the two color patterns specify colors on \(2k-1\) vertices. If \(E\) is red, they require \(k\) red and \(k-1\) blue vertices, leaving \(a-k\) red vertices outside the union. If \(E\) is blue, they require \(k-1\) red vertices, leaving \(a-k+1\) red vertices outside. This gives precisely \(q\).

## 2. Repair theorem

**Theorem.** Under these hypotheses, if

\[
 \boxed{\quad Mp+\frac{2n_1q}{k}<2,\quad}
\]

then \(H\) has Property B.

**Proof.** Apply this procedure to the sampled coloring.

If \(X=0\), keep the coloring. If \(X=1\), let \(G\) be the unique monochromatic edge. Look for a vertex \(g\in G\) for which there is no edge \(F\ne G\) containing \(g\), with all of \(F\setminus\{g\}\) colored opposite to \(G\). If such a vertex exists, flip its color. If \(X\ge2\), or if no such vertex exists when \(X=1\), declare failure.

The flip in the second case produces a proper coloring. The edge \(G\) becomes proper because \(k\ge2\). Any newly monochromatic edge must contain the flipped vertex \(g\), and all its other vertices must originally have the color opposite to \(G\). Such an edge cannot contain another vertex of \(G\), since those vertices retain the original color. Therefore it would be an excluded edge \(F\) with \(G\cap F=\{g\}\).

If the procedure fails with \(X=1\), every \(g\in G\) has such an edge \(F\). The resulting ordered pairs \((G,F)\) are distinct for different \(g\), because each \(F\) meets \(G\) in exactly one vertex. Thus \(S\ge k\).

Let \(I_{\rm fail}\) be the indicator of failure. Pointwise,

\[
 I_{\rm fail}\le \frac X2+\frac{S}{2k}.
\]

For \(X=0\) the left side is zero. For \(X=1\), a failure has \(S\ge k\). For \(X\ge2\), the term \(X/2\) is already at least one. Taking expectations gives

\[
 \Pr(\mathrm{failure})\le\frac{Mp}{2}+\frac{n_1q}{k}<1.
\]

Some sampled coloring therefore succeeds, and the procedure supplies a proper coloring of the original \(H\). No edge-criticality or initial proper coloring of a deleted hypergraph is assumed. ∎

## 3. Equivalent necessary condition

For a non-Property-B hypergraph, the procedure must fail on every input coloring. Thus

\[
 2n_1q\ge k(2-Mp).
\]

When \(q>0\), this implies

\[
 n_1\ge \max\!\left\{0,
 \left\lceil\frac{k(2-Mp)}{2q}\right\rceil\right\}.
\]

There is also a direct unique-bad-edge derivation. Non-Property-B gives \(X\ge1\) on every coloring, hence

\[
 \mathbb E X\ge\Pr(X=1)+2\Pr(X\ge2)=2-\Pr(X=1),
 \qquad \Pr(X=1)\ge2-Mp.
\]

Every coloring with exactly one monochromatic edge has at least \(k\) of the ordered private pairs counted by \(S\), by the flip argument above. Therefore \(\mathbb E S\ge k\Pr(X=1)\), giving the same inequality. This argument also requires no critical normalization.

## 4. Five-uniform, 35-edge, balanced specialization

Take \(k=5\), \(M=35\), and \(a=\lfloor n/2\rfloor\). Exact values are:

| \(n\) | \(a\) | \(p\) | \(q\) | \(2-35p\) | \(5(2-35p)/(2q)\) | Necessary \(n_1\) for non-B |
|---:|---:|---:|---:|---:|---:|---:|
| 21 | 10 | \(2/57\) | \(11/2261\) | \(44/57\) | \(1190/3\) | \(\ge397\) |
| 22 | 11 | \(2/57\) | \(11/2261\) | \(44/57\) | \(1190/3\) | \(\ge397\) |
| 23 | 11 | \(6/161\) | \(495/104006\) | \(112/161\) | \(36176/99\) | \(\ge366\) |
| 24 | 12 | \(6/161\) | \(495/104006\) | \(112/161\) | \(36176/99\) | \(\ge366\) |
| 25 | 12 | \(9/230\) | \(143/30590\) | \(29/46\) | \(96425/286\) | \(\ge338\) |

In particular, the theorem proves Property B directly when \(n_1\le396\) for \(n=21,22\), when \(n_1\le365\) for \(n=23,24\), or when \(n_1\le337\) for \(n=25\).

For 21 points, the alternative unsimplified probabilities \(p=34/969\) and \(q=1716/352716\) are equal to the entries in the table.

## 5. Pair-covering intersection moments

Suppose now that every pair of distinct vertices is covered by an edge. For \(0\le j\le4\), let \(n_j\) be the number of unordered pairs of distinct edges whose intersection has size exactly \(j\). Simplicity excludes intersection size five. Let \(d_v\) and \(\lambda_{uv}\) be the vertex degrees and point-pair codegrees, and put

\[
 W=\sum_v\binom{d_v}{2},\qquad
 T=\sum_{\{u,v\}}\binom{\lambda_{uv}}2.
\]

Double counting yields

\[
 W=\sum_{j=0}^4j n_j,\qquad
 T=\sum_{j=0}^4\binom j2n_j,
 \qquad n_1=W-2T+3n_3+8n_4.
\]

Since \(\lambda_{uv}\ge1\),

\[
 T=350-\binom n2+\tau,\qquad
 \tau=\sum_{\{u,v\}}\binom{\lambda_{uv}-1}{2}\ge0.
\]

Here the identity \(\binom\lambda2=(\lambda-1)+\binom{\lambda-1}2\) is used only for covered point pairs. Consequently a 35-edge non-B input must satisfy

\[
 3n_3+8n_4-2\tau\ge
 \begin{cases}
 677-W,&n=21,\\
 635-W,&n=22,\\
 560-W,&n=23,\\
 514-W,&n=24,\\
 438-W,&n=25.
 \end{cases}
\]

In the 21-point A1 degree sequence \(6,7,8^9,9^{10}\),

\[
 W=\binom62+\binom72+9\binom82+10\binom92=648.
\]

Thus every such non-B input necessarily has

\[
 \boxed{\quad3n_3+8n_4-2\tau\ge29.\quad}
\]

This is a mixed weighted constraint. If \(n_4=0\), it forces \(n_3\ge10\); if \(n_3=0\), it forces \(n_4\ge4\). It does not assert the disjunction \(n_3\ge10\) or \(n_4\ge4\). At \(\tau=0\), the cases \(n_4=0,1,2,3\) require respectively \(n_3\ge10,7,5,2\), and a positive \(\tau\) increases the required weighted contribution.

The associated finite scalar check is `context/propertyb35-paper/round01/middle/global_private_pair_moments_20261020/CHECK.py`. Its separate report records that the intersection-distribution PSD relaxation is feasible. Neither feasibility nor a distribution witness asserts realization by an actual hypergraph.
