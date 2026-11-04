# General Q4 inputs obtained by short-edge augmentation

Date: 2026-11-01. These consequences use the already certified N14_4,
A4_4,N10_4,K4_4 from `Q4_CORE_AND_A4_SPLIT.md`, not Q5 A4 or full P6.

## Geometric fact

Any two distinct vertices of the same parity in Q4 have at least six
distinct neighbors: their distance is two or four, giving respectively
two or zero common neighbors among their four neighbors each. Therefore
at most two opposite-parity vertices are nonadjacent to both. Consequently
any two free vertices of one parity and three free vertices of the other
parity contain a short edge between the two sets.

## GQ4-avoid

Let F be any matching of K(Q4) whose holes have counts m and m+2 in the
two parity classes. For any prescribed hole v in the larger class, F
extends to a circle through exactly Q4 minus v, with only short new edges.

For m=0 use N14_4. For m=1 use A4_4. For m>=2 choose two holes in the
smaller class and three holes in the larger class excluding v; the latter
are available because m+1>=3. The geometric fact supplies a short edge
between these free sets. Add it to F, preserving v as free and decreasing
m by one. Repeat to a base case. The base-case circle contains all added
edges, which were short, so it is also the required extension of F.

## GQ4-path

Let F be any matching of K(Q4) with equally many holes in both parity
classes. For any free root r and any opposite-parity vertex y, F extends
to a Hamilton r--y path with only short new edges.

If each class has one hole, use N10_4; if each has two, use K4_4. If each
has m>=3 holes, choose two holes of r's parity distinct from r and three
holes of the other parity. Add a short edge given by the geometric fact.
This preserves r as free and reduces m by one. The target y is allowed
to become covered: N10_4/K4_4 do not require it to remain free. Iterate
to a base case, whose path preserves the original matching. All added
matching edges were short, as required.

## GQ4-cycle

Every matching of K(Q4) with balanced hole counts extends to a Hamilton
circle with only short new edges. If there are no holes, use Fink's
perfect-matching theorem. Otherwise use GQ4-path from a free root to a
short neighbor and add their short edge to close the spanning path.

These general Q4 lemmas are available for the next five-dimensional
auxiliary problems arising from the eight-hole Q6 layer. They do not
themselves establish any whole eight-hole or higher P6 level.
