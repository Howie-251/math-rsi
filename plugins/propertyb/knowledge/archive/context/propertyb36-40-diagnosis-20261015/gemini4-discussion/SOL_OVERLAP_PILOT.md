# Balanced-colouring tree-overlap pilot (18 points, 35 edges)

2026-10-15. Bounded arithmetic/mathematical pilot; no Lean and no whole-hypergraph enumeration. This does not prove the 18-point branch. The existing 35 Lean Goal remains paused.

## Exact tree bound

Let A_e be the event that the five-edge e is monochromatic in a uniformly random balanced 9/9 colouring. Every event has probability 1/34. For distinct edges with intersection size t=0,1,2,3,4, their intersection probabilities, with denominator 24310, are respectively

\[
(70,1,10,55,220)/24310.
\]

These follow directly by counting the 9-subsets containing their union (two same-colour directions), adding the two opposite-colour directions when t=0. The least intersection probability is therefore 1/24310, attained at t=1.

For any tree T on the 35 events,

\[
\Pr(\bigcup_e A_e)\le \sum_e\Pr(A_e)-\sum_{ef\in T}\Pr(A_e\cap A_f).
\]

Proof: root the tree. The root event together with all sets A_child minus A_parent covers the union: along the root-to-active-node path, the first active node is either the root or has an inactive parent. Applying the ordinary union bound to these sets proves the displayed inequality. No independence assumption is used.

Let G_0 have the 35 edges of H as vertices, adjacent when the corresponding hyperedges are disjoint. If G_0 contains a forest with r edges, extend it to a spanning tree in the complete event graph. Its r special tree edges contribute 70/24310 each; the remaining 34-r contribute at least 1/24310 each. Thus

\[
\Pr(\bigcup_e A_e)
\le\frac{35}{34}-\frac{34+69r}{24310}
=1+\frac{681-69r}{24310}.
\]

Consequently **rank r at least 10 suffices**. At r=9 the bound is 2437/2431>1; at r=10 it is 24301/24310<1. Here rank means graph forest rank, equal to 35-c(G_0); the exact sufficient structural obligation is therefore

\[
c(G_0)\le25.
\]

This needs neither a matching of ten pairs nor twenty distinct hyperedges: a forest with ten adjacencies suffices. A readily checked stronger sufficient condition is at least 46 disjoint pairs, since a simple graph of forest rank at most 9 has at most binom(10,2)=45 edges. Indeed for component sizes s_i, sum binom(s_i,2) is at most binom(1+sum(s_i-1),2).

## What elementary incidence arithmetic currently gives

Write N_t for the number of unordered pairs of distinct hyperedges intersecting in t vertices, d_v for vertex degrees, and lambda_uv for codegrees. Then

\[
\sum_{t=0}^4N_t=595,\qquad
\sum_{t=0}^4tN_t=\sum_v\binom{d_v}{2},\qquad
N_2+3N_3+6N_4=\sum_{u<v}\binom{\lambda_{uv}}2.
\]

With 175 incidences on 18 vertices, convexity gives sum binom(d_v,2)>=765; equality has thirteen degrees 10 and five degrees 9. Pair coverage and total codegree 350 on 153 vertex pairs give sum binom(lambda_uv,2)>=241; equality has 44 codegrees 3 and 109 codegrees 2.

These aggregate constraints **do not themselves imply even one disjoint pair**: the nonnegative integer data

\[
(N_0,N_1,N_2,N_3,N_4)=(0,496,28,71,0)
\]

satisfy all three displayed identities with degree moment 765 and codegree moment 241. The degree profile has minimum degree 9. The additional vertexwise identity sum_{u!=v} lambda_uv=4d_v is also numerically compatible with the codegree distribution: a degree-9 vertex requires two incident codegrees 3, and a degree-10 vertex six; the total requirement is 5*2+13*6=88=2*44.

This is only a feasible incidence-moment assignment, **not a constructed hypergraph** and not evidence that such an intersecting H exists. It shows the exact limitation of the first two aggregate moments. Higher consistency, individual-edge constraints, or a structural theorem may still force forest rank ten. No such universal forcing argument has been established by this pilot.

If forest rank is at most nine, there are at least 26 connected components, and at least 17 isolated vertices: a nontrivial component of rank q uses q+1<=2q vertices, so all nontrivial components together use at most 18 vertices. Hence at least 17 hyperedges intersect every other hyperedge. This is a potentially useful precise alternative structural branch. Pair coverage and minimum degree eight alone do not exclude it, as the actual example below shows; any exclusion must use additional residual-branch structure.

## Stronger weighted version available

Keeping every intersection type, give an event pair excess weight (69,0,9,54,219) when t=(0,1,2,3,4). Any forest F with total excess weight greater than 681 can be extended to a tree and gives a strict bound below one. Thus failure to force ten disjointness-forest edges does not invalidate the full tree method: large intersections can help. Four independent forest edges of type t=4, for example, already have weight 876. A proof must supply the weighted forest from actual H; the numerical condition alone is conditional.

## Actual minimum-degree-eight counterexample to a universal rank claim

The parent supplied the following construction, checked directly in this pilot. Take outer vertices Z/17Z and one centre infinity. Let the 35 outer four-blocks be all 17 translates of A={0,1,4,6}, all 17 translates of B={0,1,7,8}, and C={0,1,2,3}. Adjoin infinity to each block to make the five-edges.

The two translation orbits are disjoint and each has size 17; C is in neither orbit. The degrees are thirteen 8s, four 9s, and centre degree 35. Every vertex pair is covered: the undirected differences of A and B together cover distances 1,...,8 on Z/17Z, and every outer vertex occurs in eight or nine blocks. Direct codegree counts are 82 pairs of codegree 1, 37 of codegree 2, 14 of codegree 3, 3 of codegree 4, 13 of codegree 8, and 4 of codegree 9; their total is 153 and weighted sum 350.

All hyperedges contain infinity, so the disjointness graph has rank zero. Thus pair coverage and minimum degree eight **cannot universally guarantee the desired forest rank**. This hypergraph is easily two-coloured by giving the centre one colour and every outer vertex the other. It is not an obstruction to Property B. Nor does it disprove a rank claim with additional residual-branch hypotheses: some degree-eight/nine pairs here have codegree at least three and may already be discharged by favourable double-lock estimates. A usable claim for the four residual types must explicitly incorporate the fact that every available low-degree pair is unfavourable, or otherwise exclude this star family. The minimum-degree-nine case remains open in this pilot.

## Scope

Checked: the five common-denominator probabilities, the elementary tree deduction, the exact ten-edge threshold, the component/isolated-edge alternatives, the incidence-moment arithmetic, and the explicit star construction above. Not checked or proved: a residual-branch rank-ten/weighted-forest guarantee, an extremal non-Property-B hypergraph, or the full 18-point Property B statement. This same-family pilot is provisional mathematical assistance, not a designated cross-family review.
