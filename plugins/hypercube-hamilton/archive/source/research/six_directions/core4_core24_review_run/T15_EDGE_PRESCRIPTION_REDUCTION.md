# An alternative T15 route through one optional edge in an A4 cycle

Date: 2026-11-01. New conditional reduction, independent review pending.
The edge-prescription obligation below is UNPROVED. This document does
not close T15 or any remaining Q6 endpoint instance.

## Exact input and a geometric choice that always exists

Let F be a Q5 T15 input, with minority hole a, forbidden majority holes
x,y, and three other majority holes B={b,c,d}. Two distinct vertices of
one parity in Q5 have distance two or four. At most two majority vertices
are at distance four from BOTH x and y.

To prove this, translate x to 0. If y has weight two, a vertex z of weight
four has distance four from y exactly when its support contains one of
the two y coordinates and all three other coordinates: two choices.
If y has weight four, two four-element subsets of a five-element set
intersect in at least three coordinates, so no weight-four z has distance
four from y. Consequently among the three vertices of B, one has distance
two from at least one of x,y.

Exchange the names of the forbidden vertices if necessary and select
z in B with d(y,z)=2. There are exactly two common short neighbors p,q
of y and z, both of minority parity.

## A sufficient prescription

Adjoin the auxiliary same-parity edge yz to F, obtaining L=F+yz.
Its four holes are a, x, and the two members of B other than z. Thus L
is an A4 input and x is its forbidden majority hole. The established A4
theorem supplies a 31-cycle on Q5-x containing L with short new edges.
What it does NOT guarantee is the following extra condition:

    There exists such a cycle C with yp or yq as an edge.

If this prescription holds, say yp is present, y has exactly the two
cycle edges yz and yp. Delete y and replace the two-edge segment p-y-z
by the short edge pz. The result is a single 30-cycle on Q5-{x,y}.
It retains every edge of F because y,z were original holes, and its only
new replacement edge pz is short. The artificial yz has disappeared.
Thus it proves precisely the T15 conclusion.

For the preprocessed T15 inputs, a is nonadjacent to every member of B,
so neither common neighbor p,q equals a. This is not needed for the
cycle deletion argument, but matters if a later proof uses coverage of
the prescribed-edge endpoints.

## Remaining quantified obligation

A sufficient global lemma would assert the edge prescription for every
A4 matching L with a specified required same-majority-parity distance-two
edge yz and forbidden majority hole x. That is a stronger demand than
the existing A4 theorem and is not assumed true here.

An alternative, weaker sufficient demand is: for every original T15 F,
there exists at least one ordered choice of forbidden endpoint y and
nonforbidden hole z at distance two for which the prescription holds.
The geometry above proves that eligible pairs exist, but not that their
short common-neighbor edges can occur in an A4 extension. The latter
quantifier is the exact unproved step in this alternative route.

This route may handle several of the 23 orbit cores at once. It is
independent of the earlier (2,0) EP0 condition: that condition concerns
a near-perfect local Hamilton path, whereas the present one concerns
an A4 avoided cycle and a required same-parity edge.
