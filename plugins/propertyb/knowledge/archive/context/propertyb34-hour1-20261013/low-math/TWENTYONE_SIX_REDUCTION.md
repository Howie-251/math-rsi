# A rigid residual for the 21-point unique-six/no-seven branch

2026-10-13. Partial paper reduction, **not a completed degree-six branch**. This preserves a concrete next input after the completed 20-point and 21-point degree-five candidates.

## Assumptions and target

H is simple, pair-covering, five-uniform, with 21 vertices and 34 edges. Suppose x is its unique degree-six point and all others have degree at least eight. Let L be the eight-degree set, and U={u∈L:λ(x,u)=1}. The invariant is the same conditional-permutation failure upper bound.

The degree sum gives |L|≥16. The codegree excess at x is `4*6-20=4`, so at most four points are nonunit neighbors, yielding |U|≥12.

## Exact local reductions

For u,v∈U, every (6,8,8) profile with λ(u,v)≥3 has a strict witness, so suppose all U-pair codegrees lie in {1,2}. The (6,8,8,8) domain on x plus any three U points consists of 62 labelled profiles. Fifty have strict four-lock witnesses.

Every remaining profile has common-four-point multiplicity zero. Moreover, its three U-pair codegrees are either a permutation of (1,1,2), with **all common triple multiplicities zero**, or (2,2,2). These exact residual properties are checked in `TWENTYONE_SIX_REDUCTION_VERIFIED.json`.

The zero common-four multiplicity implies each edge through x contains at most two points of U. Since all U points occur exactly once among the six x-edges, |U|≤12. Hence |U|=12, and every x-edge contains exactly two U points.

## Eliminate unit pairs inside U

Form the unit graph on U. Every triple induces either a two-edge path (the 1,1,2 residual) or the empty graph. If there is any edge a-b, every other vertex must be adjacent to exactly one of a,b: zero adjacencies gives a forbidden one-edge triple, and two gives a forbidden triangle.

Partition into the side containing a and its vertices adjacent to b, and the side containing b and its vertices adjacent to a. Two vertices on the same side are nonadjacent, since otherwise they form a triangle with the opposite distinguished vertex. Two on opposite sides are adjacent, since otherwise their triple with a or b has exactly one edge. Thus the graph is complete bipartite with both parts nonempty.

Because |U|=12, any pair of vertices can be extended to a three-vertex two-edge path: for two in the same part choose one opposite, and for a cross pair choose a third vertex in a part of size at least two. The corresponding residual has all common triple multiplicities zero, so no edge through x contains this pair. This holds for every pair in U, contradicting the established fact that every x-edge contains two U points.

Consequently the unit graph on U is empty: every U-pair has codegree exactly two.

## The remaining actual equality case

Any still-unhandled H in this particular subbranch must therefore have all of the following:

- Degree sequence `6^1,8^16,9^4`.
- Exactly twelve eight-degree points U have unit codegree with x; every pair within U has codegree two.
- The remaining four eight-degree points have codegree exactly two with x.
- All four nine-degree points have unit codegree with x.
- Each of the six x-incident edges contains exactly two U points.

Indeed, |U|=12 and |L|≥16 force equality in the at-most-four-nonunit bound, so |L|=16 and its four remaining points consume the entire codegree excess four. The degree sum then forces exactly four nine-degree points. This is a necessary actual structure, not an assertion that such an H exists.

## Verification and remaining obligation

`verify_twentyone_six_reduction.py` checks the strict witnesses by independent A/B/C injection counts and exact rational dual arithmetic. The equality-case reduction above is not numerically eliminated and is not marked complete. The next useful question is how the four nonunit eight-degree points interact with the twelve-point double-codegree set U; adding an actual nonunit point may be more informative than more interchangeable unit locks.
