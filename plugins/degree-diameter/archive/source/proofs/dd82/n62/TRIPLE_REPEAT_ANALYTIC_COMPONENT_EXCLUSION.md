# Analytic component exclusion of a triple repeat

## Claim and status

The finite matrix enumeration in Steps 4–5 of
[RECOVERED_REDUCTION.md](RECOVERED_REDUCTION.md) can be replaced by a
short analytic argument. Its last 24-vertex ordered-label case forces
three actual eight-point repeat components, each with original internal
degree 2. The original-graph quotient identity
\(c+2\operatorname{tr}R=17\) then gives a contradiction.

Combined with the analytic reductions in Steps 1–3 of that source, this
proves that the actual repeat matrix of an order-62 degree-8 diameter-2
graph has no entry of weight 3. Fresh independent same-family full-chain
review and Gemini B28 accepted this paper proof; their records are in
reviews/dd82/proof-checker-n62-triple-analytic-20261011 and
reviews/dd82/20261011_B28_n62_analytic_triple_matching_budget.md.
The full new argument is not yet formalized. The quotient trace theorem
used here is already formalized with only the original graph hypotheses.
This does not exclude the whole order-62 graph.

No computation, matrix enumeration, lift classification, Gram-factor
classification, or row-support parity check is required. The archival
script
`context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n62/n62_triple_edge_elimination.py`
was read to identify the finite object; neither it nor its output is a
premise.

## 1. Dependencies and absence of circularity

For an actual candidate with adjacency matrix \(A\), put

\[
B=A^2+A-7I-J.
\]

Regularity, nonnegative integral repeat entries, zero diagonal, row sums
3, and \(AB=BA\) follow directly from the original graph hypotheses.
For distinct vertices,

\[
B_{xy}=|N_G(x)\cap N_G(y)|+A_{xy}-1.
\tag{1}
\]

Let \(c\) count the connected components of the positive support of
\(B\), and let \(R\) be their actual original-adjacency quotient. We use

\[
\boxed{c+2\operatorname{tr}R=17.}
\tag{2}
\]

The precise existing formal theorem is
`DegreeDiameter.n62_repeat_quotient_trace_identity` in
[formal/DegreeDiameter/N62RepeatQuotientTrace.lean](../../../formal/DegreeDiameter/N62RepeatQuotientTrace.lean).
Its hypotheses are only a finite original simple graph, degree at most
8, diameter at most 2, and order 62. In particular it has **no premise
\(B\le2\)**, so applying (2) while assuming a triple repeat is not
circular. Its scope is recorded in
[N62_REPEAT_QUOTIENT_TRACE_HANDOFF.md](../../../formal/N62_REPEAT_QUOTIENT_TRACE_HANDOFF.md).

The analytic derivation is also in Section 3 of
[GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md](GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md):
commutation makes original neighbor counts constant on every actual
repeat component, and the quotient obeys
\(R^2+R=10I+\mathbf1 n^T\). Its eigenvalues other than the principal 8
are the conjugate roots of \(x^2+x-10\), with equal multiplicities.
This gives (2) without any upper bound of 2 on repeat entries. All
quotient diagonal entries are nonnegative original internal degrees.

## 2. The original-graph reduction needed here

Assume \(B_{uv}=3\). Steps 1–3 of
[RECOVERED_REDUCTION.md](RECOVERED_REDUCTION.md) give the following
actual structure before any finite enumeration:

* The pair \(\{u,v\}\) is one whole repeat component.
* The set \(S=N_G(u)\cap N_G(v)\) has four points, its repeat block is
  \(J_4-I_4\), and it is another whole repeat component.
* The five cells \(\{u,v\},S,E,U,V\), of sizes \(2,4,8,24,24\),
  partition the original vertices. No positive repeat entry joins two
  different cells.
* The repeat block on \(E=E^+\sqcup E^-\) is
  \(\begin{psmallmatrix}0&N\\N&0\end{psmallmatrix}\), where \(N\)
  is symmetric, has zero diagonal, and has row sums 3. Its three
  opposite-pair weights sum to 3. The cases with weights
  \((3,0,0)\) and \((2,1,0)\) are excluded directly in Step 3.
  Thus only \(N=J_4-I_4\) remains.

In this remaining case the 24-point set \(V\) consists of two copies
of each ordered type \((p,q)\), for distinct
\(p,q\in\{0,1,2,3\}\). A point of type \((p,q)\) has the two
original neighbors \(e_p^+\) and \(e_q^-\) in \(E\).

Put \(L=A[V]\) and \(Q=B[V]\). If the labels complementary to
\(\{p,q\}\) are \(r,s\), each point of type \((p,q)\) has exactly
one \(L\)-neighbor of type \((r,s)\) and one of type \((s,r)\).
Thus \(L\) has degree 2 and respects the three complementary
unordered-pair blocks.

The \(E,V\) block of \(AB=BA\) gives the repeat marginals

\[
\sum_{z':\,\operatorname{first}(z')=a}Q_{zz'}=1-\delta_{aq},
\qquad
\sum_{z':\,\operatorname{second}(z')=b}Q_{zz'}=1-\delta_{bp}
\tag{3}
\]

for a point \(z\) of type \((p,q)\). Since the entries are
nonnegative integers, (3) makes every entry 0 or 1 and every row sum 3.
Everything in this section is supplied by the source's analytic Steps
1–3; none of its Step 4 matrix counts or Step 5 row-support tables is
used.

## 3. Twin edges force three actual repeat components

Fix the two points \(z,\bar z\) of an ordered type \((p,q)\).
They share the two distinct original neighbors \(e_p^+,e_q^-\).
Therefore (1) gives \(Q_{z\bar z}\ge1\). The marginal bound in (3)
gives \(Q_{z\bar z}\le1\), so

\[
Q_{z\bar z}=1.
\tag{4}
\]

This twin edge uses the first-label total for \(p\) and the
second-label total for \(q\). If \(\{r,s\}\) is complementary to
\(\{p,q\}\), the remaining two repeat neighbors must use first
labels \(r,s\) and second labels \(r,s\), each once. Equal-label
ordered types do not exist. Hence these two neighbors have types
\((r,s)\) and \((s,r)\), one each.

It follows that \(Q\) has no entry between the following three
sets, each of which contains both copies of its four listed types:

\[
\begin{aligned}
W_1&=\{01,10,23,32\}\times\{0,1\},\\
W_2&=\{02,20,13,31\}\times\{0,1\},\\
W_3&=\{03,30,12,21\}\times\{0,1\}.
\end{aligned}
\tag{5}
\]

Here \(pq\) abbreviates \((p,q)\). Each set is connected in the
positive support of \(Q\): the twin edges join the two copies of
any reached type, and the remaining repeat edges connect the four
ordered types as the connected graph \(K_{2,2}\) between a reversed
pair and its complementary reversed pair. More explicitly, from type
\(pq\) one reaches types \(rs\) and \(sr\), and from either of
these one reaches type \(qp\); the twin edges reach both copies of
each type.

The cell \(V\) has no positive repeat entries leaving it. Thus the
three sets in (5) are **three whole connected components of the actual
repeat matrix**, not just blocks in a quotient or unions of unknown
components.

The original adjacency matrix \(L\) also respects (5), and every
point has its two original neighbors inside its own set. Consequently
all three quotient diagonal entries belonging to these components are
exactly 2:

\[
R_{W_iW_i}=2\quad(i=1,2,3),\qquad
\operatorname{tr}R\ge6.
\tag{6}
\]

This argument does not need the copy matchings of \(L\), the identity
\(LQ=QL\), disjointness of \(L\) and \(Q\), or a Gram matrix.

## 4. The trace contradiction

The three components \(W_1,W_2,W_3\), the component \(\{u,v\}\),
and the component \(S\) are pairwise distinct. Their sizes add to
\(24+2+4=30\). The other 32 vertices are nonempty and must contain
at least one further component, since the five just identified are
whole repeat components. Therefore

\[
c\ge6.
\]

Together with (6), this contradicts (2):

\[
17=c+2\operatorname{tr}R\ge6+2\cdot6=18.
\]

The remaining ordered-label case is impossible. The two direct cases
already eliminated in the imported Step 3 exhaust the possibilities
for \(N\), so the triple-repeat hypothesis is impossible:

\[
\boxed{B_{xy}\le2\quad\text{for all distinct original vertices }x,y.}
\]

## 5. Exact dependency replacement

The only imported order-62 facts are the original-graph cell reduction
and direct small-matrix exclusions in the recovered Steps 1–3, together
with the already proved original-input quotient trace identity. The
new implication from the last ordered-label case to the contradiction
is Sections 3–4 above.

No enumeration of the eight lift gauges, no counts of commuting cubic
matrices, no Gram survivor table, and no classification or resolution
of row supports remains in this proof. Existing recovered and reviewed
sources have not been edited. The new finite-label component argument
still needs formalization before it can be used as a Lean theorem.
