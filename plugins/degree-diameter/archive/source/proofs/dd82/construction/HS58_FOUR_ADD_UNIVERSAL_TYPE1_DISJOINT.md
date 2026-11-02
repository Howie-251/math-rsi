# HS58 universal type 1: the disjoint-deletion equality branch

Date: 2026-10-12. This is a pure mathematical closure of the disjoint-D
branch after the equality reduction stated below. It uses no finite
enumeration or SAT result. The equality reduction itself belongs to
the universal-case sections of
[HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md](HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md)
and is an explicit dependency, not a conclusion established in this note.

## Setup and the exact imported equality case

Let Q be HS50, let D be two disjoint original edges, let A be four
added original nonedges, and let M=Q-D+A. The eight new vertices induce
catalog type 1: a star with center c and two incident extra leaf edges.
Four leaves are ordinary, meaning their only H neighbor is c. The
other three leaves are special. Since d_H(c)=7, c has exactly one old
neighbor v.

For each old x write B_x for its new-neighbor set and
p_x=|B_x|=1+r_x-a_x. The equality reduction supplies all of the following:

1. A is a four-edge matching on an eight-element endpoint set W.
2. v does not belong to W.
3. Every endpoint of D belongs to W union {v}.
4. The total incidence of the four ordinary leaf labels among port
   sets of W union {v} is exactly four, one occurrence of each label.

We show that neither v outside the endpoints of D nor v among those
endpoints is possible. In particular this closes all disjoint-D cases
satisfying the stated reduction, without classifying their placements
in Q.

## Two elementary route observations

Every zero-port old vertex x must be adjacent to v in M to reach c
within two steps. Because v is untouched by A, this implies xv is a
retained Q edge.

If xy is a deleted original edge and B_x,B_y are disjoint, its distance
cannot be repaired through a new vertex. Q has no triangle, so it has
no old two-step route using two original edges either. As A is a
matching, no two-step route can use two edges of A. The only remaining
possibilities are

\[
x-a-y\quad\text{with }xa\in A,\ ay\in Q-D,
\qquad
x-b-y\quad\text{with }xb\in Q-D,\ by\in A.       \tag{1}
\]

An unavailable added edge at either endpoint simply removes the
corresponding option. A direct re-addition xy is impossible because A
contains only original nonedges.

## Case 1: v is not a deletion endpoint

All four deletion endpoints form a set P contained in W. Each has
p=1, while the other four vertices Z=W minus P have p=0. Every old
vertex outside W has p=1. In particular B_v={c}. Equality item 4
therefore forces the four ports of P to be the four distinct ordinary
leaf labels.

A zero-port vertex has eight old neighbors and must reach all eight
new vertices through them. Since every old vertex has at most one
port, all eight neighbors must have positive ports. Thus no added
edge can pair two vertices of Z. The matching A consequently pairs
the four vertices of Z bijectively with the four vertices of P.

Now fix x in P. Its own port is an ordinary leaf, whose only H neighbor
is c; its added old neighbor has zero ports. To reach the other six
leaf labels, x must obtain all of them from its six retained Q
neighbors. Each such neighbor supplies at most one leaf label. Hence
none of these neighbors can have zero ports. In particular, no vertex
of P has a Q neighbor in Z, since no deleted edge touches Z.

For either deleted edge xy, the port sets are distinct singletons.
Each added partner in (1) belongs to Z, and the needed original
adjacency to the other endpoint would be a P-Z edge. None exists.
The deleted edge cannot be repaired, a contradiction.

## Case 2: v is a deletion endpoint

Write D={vy,zw}, and put P={y,z,w}. These three vertices lie in W and
have p=1; the other five vertices Z=W minus P have p=0. Vertex v has
two ports. By item 4,

\[
B_v=\{c,\alpha\},\qquad
B_y=\{\beta\},\quad B_z=\{\gamma\},\quad B_w=\{\delta\},
\]

where alpha,beta,gamma,delta are the four distinct ordinary leaves.
Every other old vertex has at most one port. The zero-port observation
gives Z subseteq N_Q(v).

First suppose no edge of A lies inside P. Then each x in P has an
added partner in Z. As in Case 1, x's direct and H-mediated routes
reach only its own ordinary leaf and c, while its added neighbor
supplies no label. Its six retained Q neighbors must supply the other
six leaf labels. Each supplies at most one leaf label, including v:
v's second port is c and only alpha is a leaf. Consequently no vertex
of P has a retained Q neighbor in Z. Since no deleted edge touches Z,
there is no Q edge between P and Z. Applied to the deleted edge zw,
(1) is again impossible.

It remains that A has an edge inside P. It cannot be zw, which is an
original edge. After exchanging z and w if necessary, it is yz.
The remaining vertex w is matched by A to some s in Z.

The deleted edge vy has disjoint port sets, and v has no incident
addition. Its only possible old repair is v-z-y, forcing vz to be
a retained Q edge. For the other deleted edge zw, (1) now gives only
two possibilities:

* yw is a Q edge. Together with the original edges vy,zw and the
  forced edge vz, this creates the four-cycle v-y-w-z-v in Q.
* zs is a Q edge. Since s is in Z, the zero-port observation gives
  vs in Q. Together with vz this creates a triangle v-z-s-v in Q.

HS50 has neither triangles nor four-cycles. Both repairs are impossible,
which is the final contradiction.

The proof closes precisely the stated equality branch with two
disjoint deletions. The equality reduction and the adjacent-deletion
branch are separate inputs to a full universal-type-1 exclusion.
