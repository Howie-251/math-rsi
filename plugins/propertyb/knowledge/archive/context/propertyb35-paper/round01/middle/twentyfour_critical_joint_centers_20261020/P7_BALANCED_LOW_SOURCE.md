# A common low source for the whole remaining P7 branch

Let \(H\) be a simple five-uniform hypergraph on24 vertices with35 edges, point-pair coverage, and degree spectrum \(7^{17}8^7\). Let \(P\) be its seven degree-eight points. Assume that every original edge meets \(P\), and that \(H\) is not two-colorable. No edge-criticality is assumed in the following source selection.

Then there is a12-red/12-blue coloring whose unique monochromatic edge \(G\) contains exactly one point of \(P\). After complementing if necessary, \(G\) is red. In particular it has four degree-seven points and \(d(G)=36\).

This is a source-existence theorem for the whole P7/no-all-seven-edge branch, rather than a coloring theorem or a statement about one P7 inventory.

## 1. The actual family of low edges is large enough

For an original edge \(e\), put \(k_e=|e\cap P|\). By hypothesis \(k_e\ge1\). Let \(I\) be the number of edges contained in \(P\), and \(L\) the number with \(k_e=1\).

If \(I=0\), coloring \(P\) red and its complement blue makes every edge proper. Thus the assumed non-B input has \(I\ge1\).

The seven actual degree-eight points give

\[
 \sum_{e\in H} k_e=56,\qquad
 \sum_{e\in H}(k_e-1)=21.
\]

Among the35 edges, the \(I\) internal edges contribute four each to the second sum. Each of the \(35-L-I\) remaining nonsingleton-trace edges contributes at least one. Therefore

\[
 21\ge4I+(35-L-I),\qquad
 \boxed{L\ge14+3I\ge17.} \tag{1}
\]

Every member of this indexed family is an actual edge of degree type \(7^4 8\), not an arbitrary five-set.

## 2. Apply the existing designated-family source lemma

Use the general [unique-bad-edge-family moment lemma](../../../../../proofs/propertyb35/UNIQUE_BAD_EDGE_FAMILY_MOMENTS.md) on the balanced12/12 color space. An individual five-edge is monochromatic with probability

\[
 p=\frac{2\binom{19}{7}}{\binom{24}{12}}=\frac6{161}.
\]

For completeness, let \(X\) count all monochromatic original edges, \(Y\) those in the family from(1), and \(J\) indicate that exactly one original edge is monochromatic and it lies in that family. Since \(H\) is non-B, \(X\ge1\) at every sample. Pointwise,

\[
 Y\le2(X-1)+J.
\]

If \(X=1\) this is equality; if \(X\ge2\), use \(Y\le X\le2(X-1)\). Hence

\[
 \mathbb P(J=1)\ge Lp-2(35p-1)
 =\frac{6L-98}{161}
 \ge\frac4{161}>0. \tag{2}
\]

There are \(\binom{24}{12}=2704156\) balanced samples. At \(L=17\), (2) guarantees at least67184 actual samples. A sample with \(J=1\) gives the claimed source. All34 other original edges are proper in that same sample.

## 3. A stronger common minimum-blue source

Fix the actual \(G\) obtained above. Among all proper colorings of \(H\setminus\{G\}\) with \(G\) red, minimize the number \(b\) of blue points. This finite family is nonempty by(2), so \(b\le12\). Every blue point has a single-blue private edge; otherwise it could be flipped red while retaining the same unique red bad edge.

Write \(N_j\) for the number of the other34 indexed original edges containing exactly \(j\) blue points. Each point \(g\in G\) must own at least one edge whose only red point is \(g\), or flipping \(g\) blue colors \(H\) properly. These five owners require five distinct \(N_4\) edges. Thus

\[
 \sum_{y\in B}d_H(y)=\sum_{j=1}^4jN_j
 \ge34+3N_4\ge49.
\]

All original degrees are at most eight, so

\[
 \boxed{7\le b\le12.} \tag{3}
\]

The fixed \(G\) and its original degrees have not changed.

## 4. Four actual centers, one blue high-point pool

For a degree-seven \(g\in G\), let \(\mathcal A_g\) be the indexed external four-sets of edges whose unique red point is \(g\), and let \(m_g=|\mathcal A_g|\). Non-B gives \(m_g\ge1\). The other six edges through \(g\) all meet the blue set. Their blue incidences are at least

\[
 4m_g+(6-m_g)=6+3m_g.
\]

On the other hand, by point-pair coverage,

\[
 \sum_{e\ni g}|e\cap B|
 =\sum_{y\in B}\lambda(g,y)
 =b+\kappa_g,\qquad
 0\le\kappa_g\le4d_H(g)-23=5.
\]

Consequently, for all four degree-seven points of this one \(G\),

\[
 \boxed{1\le m_g\le
 \left\lfloor\frac{b-1}{3}\right\rfloor
 \le3.} \tag{4}
\]

When \(b\le9\), all four groups have at most two members. These are constraints in one common source; their individual inventories are not selected independently.

Let \(B_P=B\cap P\). Every edge contains at least one high point. A positive edge whose only red point is a degree-seven \(g\) therefore has a high point among its four blue points:

\[
 \boxed{A\cap B_P\ne\varnothing
 \quad\text{for every }A\in\mathcal A_g
 \text{ and every degree-seven }g\in G.} \tag{5}
\]

The source edge contains one red high point, so \(|B_P|\le6\); (5) and \(m_g\ge1\) give \(|B_P|\ge1\). The at-least-four actual positive groups thus share the same nonempty high-point hitting pool of size at most six. Distinct groups contain distinct original edge indices.

## 5. The repair that remains unproved

Equations(1)–(5) cover the whole P7/no-all-seven branch, including the remaining one- and two-internal-edge cases. They do not eliminate the unique bad edge.

In particular, the blue-minimum normalization does not give a cheap one-direction repair. If \(F_g\) denotes the set of blue points having a single-blue private edge that avoids \(g\), and \(U_g=\bigcup\mathcal A_g\), then the existing common-private-edge accounting gives

\[
 |U_g\cap F_g|\ge4m_g-5.
\]

Thus the private singleton constraints cannot be discarded or assumed to have one common forbidden point. Successful recoloring must use the same actual private edges, either by selecting a different source/initial state or by a genuine bidirectional exchange. The exact necessary-and-sufficient exchange conditions are already in [EXCHANGE_LEMMA.md](../../critical-exchange/EXCHANGE_LEMMA.md). No universal fixed exchange radius is proved here.

The remaining whole-branch obligation is to exploit the four groups in(4), their common high-point pool in(5), and the shared actual private-edge budget to produce a proper coloring. The full-all-seven-edge branch still needs its own low-source selection or compatible exchange; it is not covered by the P7 hypothesis.

## 6. Evidence

[P7_BALANCED_LOW_SOURCE_REVIEW.md](P7_BALANCED_LOW_SOURCE_REVIEW.md) independently checks the source proof and constants, labeled same-family/provisional. [P7_BALANCED_LOW_SOURCE_CHECK.json](P7_BALANCED_LOW_SOURCE_CHECK.json) recomputes the balanced sample counts and the designated-family inequality, with CPU0.000075s. It enumerates no hypergraphs, high-trace families, layouts, or unknown colorings.

The later improvement(3) follows directly from the same source and the actual maximum degree eight. This note does not claim a new coloring branch or a new global lower bound.
