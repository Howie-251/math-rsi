# T15 in Q5: all six holes in one face, zero required crossings

Date: 2026-11-01. ARIS proof-writer/proof-checker scoped package.
Semantic assurance: **same-family / provisional**. The deterministic finite
checks are separate from this semantic assurance. No global state is changed.

## Exact quantified claim

For every matching F of the complete graph on V(Q5), suppose its uncovered
vertices are exactly {a} union H, where |H|=5 and each member of H has cube
parity opposite to a. For every pair of distinct specified vertices v,w in H,
suppose a coordinate cut Q5=A union B has all six holes in A and no edge of F
crosses that cut. Then a simple cycle exists on exactly V(Q5) minus {v,w},
contains every edge of F, and has only short cube edges outside F.
Thus the cycle has 30 vertices. Required edges of F may be long and may join
vertices of the same parity. The claim includes either parity for a.

This is a theorem for every input satisfying this particular cut condition.
It is not the unrestricted Q5 T15 theorem and does not prove full P6.

## Inputs, symbols, and obligations

Identify the two faces with the same Q4 by deleting the cut coordinate. A
vertex x in A corresponds to bar(x) in B, and x--bar(x) is a short Q5 edge.
Write F_A and F_B for the two restrictions. The zero-crossing hypothesis
implies that F_B is a perfect matching, while F_A has precisely the six holes.

The imported theorem T44_5 is the statement in T44_Q5_CLOSURE_DRAFT.md,
with current PASS provenance in T44_Q5_CLOSURE_REVIEW.json. It says that
four holes of one parity allow omission of any prescribed two holes in a
30-cycle. Its proof and its Q4/Fink dependencies are explicit imports here;
they are not rerun in this package. The import has same-family/provisional
semantic assurance. No Q5 T15 or P6 result is used to prove a local step.

The new independent checker imports no generator or earlier checker. It
reads all four positive path files and both complete opposite-hole circle
tables directly. Q4_T15_CLASSIFICATION.md supplies context and the name of
the triangle condition; its cycle classification is not needed as an
unproved shortcut in the path argument below.

Dependency DAG:

* Complete opposite-hole circle tables, including exhaustive negative
  complements -> perfect-matching root-endpoint bounds.
* Four T15 positive path tables + full matching coverage -> A path bounds.
* Lossless cube automorphisms + complete marked-hole geometry partition ->
  those four residual representatives cover all nonadjacent inputs.
* T44_5 -> adjacent available-hole branch.
* A and B endpoint bounds + two-bridge construction -> residual branch.

All objects are finite. There are no limit interchanges or asymptotic
uniformity assumptions. Bounds are uniform over all complete-graph
matchings of the stated vertex supports.

## 1. Adjacent available-hole branch

If some b in H minus {v,w} is short-adjacent to a, add ab to F. Both are
holes, so this is still a matching. Its four remaining holes are H minus
{b}, all of one parity, and contain v,w. Apply imported T44_5, omitting
exactly v,w. The resulting cycle contains F union {ab}; the edge ab was
short, so relative to the original F every added edge is short as required.

## 2. Lossless residual normalization and complete coverage

Suppose no member of H minus {v,w} is adjacent to a. Translate the common
local labels on both faces by a, putting the root at 0 in A and bar(0) in B.
The five majority holes then have odd local parity, regardless of a's
original local or global parity. Each of the three available holes is a
nonneighbor of 0, hence has Q4 weight 3. Permute coordinates, on both
faces simultaneously, so these three vertices become {7,11,13}. This is
possible because the four weight-3 vertices are the complements of the
four distinct coordinate units; any choice of three can be sent to this
choice. These transformations preserve all short edges and transport any
arbitrary matching bijectively; they also preserve the correspondence of
the two faces and the identities of the two omitted holes.

The omitted pair is now drawn from {1,2,4,8,14}. The permutations preserving
{7,11,13} fix coordinate unit 1 and permute units {2,4,8}. Their four
unordered-pair orbits have representatives

    (1,2), (2,4), (1,14), (2,14).

Independently enumerating all binomial(8,5)*binomial(5,2)=560 marked
geometries at root 0 gives 520 adjacent geometries and 40 residual ones.
The four full coordinate-permutation orbits have sizes 12,12,4,12 and are
disjoint. Every residual geometry belongs to exactly one. Translation
handles every minority root, including the parity-reversed case; there
is no assumption that an arbitrary input was already in a representative.

## 3. Independently checked A path bounds

For each representative pair (v,w), the holes are {0,7,11,13,v,w}. The
remaining ten vertices admit exactly 9!!=945 complete-graph matchings.
The checker generates this entire matching set independently and deletes
one matching for each parsed record. At the end the set is empty. Invalid
mate arrays, duplicate inputs, missing inputs, incomplete records, and
trailing bytes all cause failure.

Each row gives a lower set S of odd endpoints q: every q in S has an
explicit 0--q path on precisely Q4 minus {v,w}. Each path has 14 distinct
vertices, retains all five required matching edges, and has only short
edges outside that matching. Distinct witnesses in a row have distinct
endpoints. No claim that S lists every possible endpoint is required.

Let N={1,2,4,8} and D3={7,11,13,14}. Define the triangle condition by

    {v,w} subset N, N minus {v,w}={p,q}, and pq in F_A.

The deterministic checks establish:

* If the triangle condition fails, S is all six allowed odd endpoints,
  namely ODD minus {v,w}.
* If the triangle condition holds, S contains all four members of D3.
  In particular these endpoints are allowed, since v,w are neighbors.

The 3780 complete matching records give 22260 positive paths. There are
210 triangular records, each with four listed endpoints; all other 3570
records have six listed endpoints. The two families with both omitted
vertices neighboring 0 have histograms {4:105,6:840}; each other family
has {6:945}. The checker also confirms the generation JSON against these
counts, but does not trust the producer's search or its failure behavior.

The triangle condition obstructs a corresponding 14-cycle through 0 in
the older classification. It does not obstruct the endpoint paths used
here: the root 0 has degree one in an A path. Its positive paths are
checked directly, including all 210 records.

## 4. Independently checked B endpoint bounds

For every complete-graph perfect matching P on Q4 and every root r, let
G(P,r) consist of opposite-parity vertices q for which a Hamilton r--q
path contains P and uses only short additional edges. Then

    |G(P,r)| >= 4,
    G(P,r) intersects {q: d_Q4(r,q)=3}.

The package independently checks the full finite basis behind
Q4_PERFECT_ENDPOINT_ABUNDANCE.md, rather than treating the saved 4708
rows as a complete proof by themselves. At root 0, for odd endpoint y,
P(0)=y is necessarily impossible: the mandatory edge 0y would already
exhaust both endpoint degrees, leaving the remaining vertices disconnected.
Otherwise put a=P(0), b=P(y). The four vertices 0,y,a,b are distinct.
Deleting 0,y from a desired Hamilton path and adding the auxiliary edge ab
is equivalent to a 14-cycle containing

    T = P minus {0a,yb} union {ab}

on Q4 minus {0,y}. The reverse removes ab and restores the two endpoint
edges. The auxiliary edge cannot coincide with a retained P edge, and
the 14-vertex path cannot already contain ab: that would isolate its two
endpoints from its other twelve vertices. Thus both constructions give
simple paths/cycles and preserve all original required edges.

The two complete tables with omitted sets {0,1} and {0,7} each contain
135135 distinct valid matchings, exactly 13!!, which proves full coverage.
All 270166 positive circles pass direct support/edge/shortness checks.
For all 104 negatives (51 and 53), the checker exhausts complementary
short perfect matchings disjoint from T. Any required cycle must be such
a union, since T covers each surviving vertex once and a cycle covers it
twice. Every enumerated union has more than one connected component;
therefore the claimed negatives are rigorously impossible.

Coordinate permutations transport the negative tables to all eight odd
endpoints. For every negative T and every oriented edge ab in T, construct
P=T minus {ab} union {0a,yb}. These are all failed endpoint pairs other
than the exceptional trivial case P(0)=y, by the preceding equivalence.
There are 5824 labeled inverse instances and 4708 distinct candidate P.
For each candidate the checker recomputes all eight endpoints by the
forward rule, adds the trivial bad endpoint when present, and agrees with
every saved exact endpoint row. The bad-endpoint histogram is
{1:2072,2:2180,3:36,4:420}; the good distance-3 histogram is
{1:420,2:276,3:2212,4:1800}. These imply the two stated bounds within the
candidate universe. Outside it, only a possible odd partner P(0) can be
bad, giving at least seven good odd endpoints and at least three good
distance-3 endpoints. This proves the bounds for every P, without a
quantifier gap caused by inspecting only the exceptional candidates.
Translation gives every root r.

## 5. Endpoint intersection and exact two-bridge gluing

Apply Section 4 to F_B at root bar(0), in the same local labels. Let G be
its set of good odd local endpoints. If the A record is nontriangular,
|S|=6 and |G|>=4 inside an eight-element universe, so |S intersect G|>=2.
If it is triangular, S contains D3 and G intersects D3, so again their
intersection is nonempty. Choose any q in the intersection and its two
witnessing paths R_A and R_B.

The A path goes from 0_A to q_A and visits exactly A minus {v,w}; the B
path goes from 0_B to q_B and visits all of B. Their supports are disjoint,
and q is odd while 0 is even, so each path has two distinct endpoints.
Add the two short edges

    0_A--0_B and q_A--q_B.

Starting at 0_A, traverse R_A to q_A, cross to q_B, traverse R_B backwards
to 0_B, then cross back to 0_A. This explicitly visits every retained
vertex once and gives one simple cycle, not a disconnected 2-factor.
It has 14+16=30 vertices and omits exactly v,w. Every original matching
edge is internal to a face by hypothesis and is retained by its path.
Every other path edge is short; the two bridges are also short. Undoing
the shared automorphism proves the precise claim above.

## Reproduction and scope boundary

Run D:/anaconda/python.exe
research/six_directions/T15_SAMEFACE_ZERO_CROSSING_check.py from E:/新问题.
The dedicated JSON contains input hashes, every family count, orbit
coverage, the full negative-complement evidence, and the independent
perfect endpoint census. The review records a hash of this proof too.

This closes only the all-six-holes-in-a-coordinate-face, zero-required-
crossing T15 branch, conditional on imported T44_5 for its adjacent
subbranch. The nonadjacent subbranch is established directly from the
independently checked Q4 certificates. Inputs with required crossings,
hole sets in no common coordinate face, the remaining T15 cases, and
full P6 are not resolved here. No global closure ledger is edited.
