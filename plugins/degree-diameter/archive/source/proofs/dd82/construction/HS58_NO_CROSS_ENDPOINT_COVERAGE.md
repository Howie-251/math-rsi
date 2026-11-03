# HS58: endpoint coverage when the two deleted edges have no cross-edge

Date: 2026-10-12. Let Q be HS50, and let D={xy,zw} be two disjoint
original edges with no other Q edge among their four endpoints P.
Let A consist of added original nonedges, and let eight new vertices
induce H. Assume the complete graph is eight-regular and has diameter
two. Write B_t for old vertex t's new-neighbor set and a_t=d_A(t).

The following necessary condition allows all additions and attachments
to vary. In particular it does not assume that an endpoint's deleted
partner is untouched by A. It is specific to D inducing exactly two
independent edges in Q; it makes no exclusion for adjacent D or for
disjoint D with a Q cross-edge.

## A full endpoint leaves at most one H label uncovered

For t in P, |B_t|=2-a_t. Suppose x is full, meaning |B_x|=2 and a_x=0.
We prove

\[
|V(H)\setminus N_H[B_x]|\le1.                         \tag{1}
\]

Here N_H[B_x] is the union of the closed H-neighborhoods of the two
members of B_x. Set a=a_y and p=|B_y|=2-a. Since x has no additions,
its old neighbors are its retained Q neighbors. All lie outside P:
y was deleted as a neighbor, and the no-cross-edge assumption excludes
z and w. Each such neighbor t has at most one port. If its port is
positive, then |B_t|=1 and a_t=0.

The original pair t,y is nonadjacent in Q, with unique common neighbor
x. Deleting xy destroys that old route. If t's singleton label is not
in B_y, no new common neighbor repairs the pair. Its replacement old
route must then have the form t-q-y, with qy in A and tq in Q: no
added edge touches t. Thus t is a common Q neighbor of x and q.

For each q in N_A(y), Q gives at most one such common neighbor t.
The case q=x is impossible because xy is an original edge, not an
eligible addition. Hence among positive old neighbors of x there are
at most a exceptional vertices whose labels are outside B_y. Denote
their label set by C; then |C|<=a. This bound includes additions
touching other deletion endpoints.

Let R=V(H) minus N_H[B_x]. Direct and H-mediated routes from x cover
no member of R, so the old-mediated routes imply

\[
R\subseteq B_y\cup C,\qquad |R|\le p+a=2.             \tag{2}
\]

Suppose |R|=2. Equality in this capacity bound forces B_y subseteq R,
including the possible case p=0. Thus B_x and B_y are disjoint.
The deleted pair x,y cannot be repaired through a new vertex. It has
no original Q two-step route, because Q has no triangle. Since x has
no added edge, repairing it therefore requires some

\[
q_0\in N_A(y)\cap N_Q(x).
\]

If a=0 no such repair exists, already a contradiction. Otherwise q_0
and x are adjacent in Q and have no common Q neighbor. Consequently
this particular added neighbor q_0 supplies none of the exceptional
vertices counted above. We improve the bound to |C|<=a-1, and (2)
now gives |R|<=p+a-1=1, the final contradiction. Values |R|>=3 were
already excluded by (2), proving (1).

An earlier informal version incorrectly used B_t subseteq B_y before
proving that y avoids A. That shortcut is invalid when y has additions.
The explicit exception count and the consumed q_0 repair above replace
it; no conclusion in this note uses the shortcut.

## Degree-sum condition for every auxiliary bad pair

Let {u,v} be a pair at H-distance greater than two. It needs a common
old neighbor. Vertices outside P have at most one port, while those
in P have at most two. Hence some deletion endpoint has full port set
exactly {u,v}, so (1) applies to it.

The closed H-neighborhoods of u and v are disjoint, because the pair
is neither adjacent nor joined by a two-step H path. Therefore

\[
|N_H[\{u,v\}]|=2+d_H(u)+d_H(v)\ge7,
\qquad d_H(u)+d_H(v)\ge5.                            \tag{3}
\]

This holds for every bad pair, irrespective of how other deletion
endpoints meet additions. The proof did not use a fixed value of |A|;
the application below concerns exactly five additions.

## Actual a5 catalog and construction application

The separately completed a5 auxiliary catalog has 89 raw types.
After the recorded universal-H and adjacent-full-port reductions,
its existing assembly list contains 67 types. Applying only (3) to
those saved representatives leaves **type 3**. Each of the other 66
types has an explicit bad pair of degree sum less than five.

The read-only derived filter source is
[hs58_two_delete_no_cross_filter.py](../../../computations/dd82/construction/hs58_two_delete_no_cross_filter.py),
with full per-type witnesses in
[no_cross_filter.json](../../../computations/dd82/construction/hs58_two_delete_five_add_auxiliary_run/no_cross_filter.json).
It reads existing degree sequences and bad pairs; it generates no
graphs and calls no solver. Raw catalog records and its 67-type
general assembly list are unchanged. The reduction to type 3 concerns
only the no-cross-edge D stratum.

The actual construction uses D={(0,1),(10,11)} in the saved HS
labeling. These edges lie in different pentagons among vertices
0,...,24, with no Q cross-edge between their endpoints. Thus (3)
applies to its whole fixed-D family, with all A and B choices free.
In particular the actual type-54 H has a bad pair with degree sum
2+1=3, and type 14 has bad pairs with degree sum 3+1=4. These are
analytic failures of those fixed-D families, independently of the
candidate BFS counts or the later type-14 checked UNSAT run.

For completeness, type 54 also has a simpler valid obstruction
preceding the general proof above. Its bad graph is K1,3 and H has
only one edge among the three bad leaves. The three required bad
pairs force three full deletion endpoints, so one deleted edge has
both endpoints full, carrying {u,a} and {u,b}. With no Q cross-edge,
their ordinary positive old neighbors have labels in their partner's
port set. Each endpoint can reach the third bad leaf c only if ac
and bc are H edges, requiring two edges among the three bad leaves.
This contradicts the actual type-54 geometry. Unlike the discarded
shortcut, this argument has both endpoints full from the outset.

No exclusion is asserted here for the remaining type 3, for disjoint
D with a Q cross-edge, or for adjacent D. Those are distinct assembly
obligations.
