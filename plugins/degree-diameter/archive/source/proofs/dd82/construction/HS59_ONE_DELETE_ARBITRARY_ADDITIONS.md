# HS59: at most one old deletion, with arbitrary old additions

Date: 2026-10-11. This follows the construction-first Goal and the
project-local formula-derivation workflow. No solver or enumeration is used.

## Target and status

**COHERENT AS STATED.** There is no simple graph G on 59 vertices, of maximum
degree at most eight and diameter at most two, obtained from the
Hoffman–Singleton graph Q on 50 designated old vertices by deleting at most
one original old edge, adding arbitrary edges between old vertices, and
adjoining nine new vertices with arbitrary incident edges.

Deletions and additions mean the final differences from Q, not a sequence of
temporary edits. In particular, an original edge that is deleted and then
restored is retained, and is not counted as both an addition and a deletion.

The new argument excludes every case with at least one added old edge. The
two cases with no added old edges use the already established analytic
exclusions cited below. Thus the statement covers all final old-edge sets
with at most one missing edge of Q, including old-edge supersets of Q.

## Invariant object, assumptions, and notation

Q is 7-regular and triangle-free. Every nonadjacent pair in Q has exactly one
common neighbor. These properties are the only special HS properties used
in the new addition argument.

Every target G is 8-regular: a vertex of degree at most seven has at most
1+7+7·7=57 vertices in its radius-two ball. Write L for the nine new vertices,
H=G[L], and B_x=N_G(x)∩L for the set of new neighbors of old vertex x.

Let D=E(Q)\E(G[Q]) and A=E(G[Q])\E(Q). Put r_x=d_D(x), a_x=d_A(x), and
p_x=|B_x|. The exact degree identities are

    p_x = 1+r_x−a_x ≥ 0,
    |{x : b∈B_x}| = 8−d_H(b)       for every new vertex b.

Let N_old(x) denote the old neighbors of x in G. The set of new vertices
reachable from old x in at most two steps is exactly

    B_x ∪ ⋃_{y∈N_old(x)} B_y ∪ N_H(B_x).                 (1)

In particular, when p_x=0, x has eight old neighbors and can reach only
the union of their port sets B_y. Formula (1) is the invariant coverage
obligation throughout the proof; H is never fixed in advance.

## Derivation map

1. With no deleted edge, any old addition creates a zero-port vertex whose
   eight old neighbors cannot supply all nine new labels.
2. With one deleted edge uv, an addition not incident to u or v is impossible
   by the same count and triangle-freeness of Q.
3. Additions incident to both u and v, or two additions incident to one of
   them, also fail the zero-port count.
4. In the sole remaining form A={uz}, two groups of lost unique old paths
   force a port column of size at least six and at most two labels among
   the retained old neighbors of u. Formula (1) then reaches at most five
   of the nine new vertices.

All these steps are exact necessary conditions, with no relaxation or
approximation.

## Main derivation

### 1. No deleted old edge

Suppose D is empty. Then p_x=1−a_x≤1 at every old vertex. If an old edge is
added, either endpoint z has a_z≥1, hence p_z=0. All eight neighbors of z
are old, and each supplies at most one new label. Thus z reaches at most
eight new vertices in two steps, contrary to |L|=9.

Consequently A must also be empty. This is exactly the induced-HS order-59
case excluded in
[Construction case studies, theorem and k=9 case](CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md).
That analytic result allows arbitrary H and includes empty attachment columns.

### 2. One deleted edge: every addition meets an endpoint

Now let D={uv}. Only u and v can have two new neighbors; they have two
exactly when a_u=0 or a_v=0, respectively. Every other old vertex has at most
one new neighbor.

Suppose zw is an added old edge with z,w outside {u,v}. Nonnegativity of
p_z=1−a_z and p_w=1−a_w gives p_z=p_w=0. Among the eight old neighbors of z,
one is the zero-port vertex w. To supply nine new labels, the other seven
neighbors must include both possible two-port vertices u and v. Otherwise
their port sizes sum to at most eight.

Thus u and v both have two ports and are both adjacent to z. Having two
ports means neither is incident to an addition. Hence zu and zv are edges
of Q, as is uv. This is a triangle in Q, a contradiction. Every old addition
therefore meets {u,v}.

An added edge cannot be uv: uv is an original edge and by assumption is
absent in the final graph. Thus every addition has an endpoint outside
{u,v}, and that endpoint has zero ports.

### 3. One deleted edge: at most one addition

If additions meet both u and v, neither has two ports. All old vertices
then have at most one port. Any ordinary endpoint of an addition has zero
ports and fails to reach nine new vertices through its eight old neighbors.

All additions must therefore meet just one endpoint, say u. Since
p_u=2−a_u≥0, there are at most two. If there are two, p_u=0, and v is the
only two-port vertex. However, uv is absent in G. Each of u's eight old
neighbors consequently has at most one port, again giving at most eight
reachable new vertices.

The only remaining case with an addition is therefore

    D={uv},       A={uz},       z∉{u,v}.

The case A empty is already excluded analytically in
[HS59 with one deleted old edge](HS59_ONE_DELETE_DESIGN.md), for every
choice of uv, without an edge-transitivity assumption.

### 4. The last one-addition configuration

Here B_u={b} for one new vertex b, |B_v|=2, B_z is empty, and every other
old vertex has one port. Since z has eight old neighbors and v is the only
two-port vertex, z must be adjacent to v in order to reach all nine new
vertices. This adjacency is an original edge, so

    z∈N_Q(v)\{u}.

The edge uz is not in Q, both because it is an addition and because Q has
no triangle on u,v,z.

Put W=N_Q(v)\{u,z}. **There are five vertices in W.** For w∈W, the only
original old path of length at most two from u to w is u−v−w, and it is
destroyed by deleting uv. The added edge uz could repair such a path only
through an edge zw. But z and w are both neighbors of v in Q, so zw is
absent by triangle-freeness, and zw is not the added edge either. The pair
u,w must therefore share a new neighbor. Its singleton port is forced to be

    B_w={b}       for all five w∈W.

Together with u itself, these are six distinct old neighbors of b. The new
degree equation gives

    d_H(b)≤2.                                             (2)

Next put X=N_Q(u)\{v}, a set of six vertices. None is z. For x∈X, the
unique original old path from v to x is v−u−x, destroyed by the deletion.
The sole added edge uz cannot appear in a path of length at most two from
v to x: neither endpoint v,x of such a path is u or z. There is also no
direct edge vx. Thus v,x must share a new neighbor, forcing

    B_x⊆B_v       for every x∈X.                           (3)

The final old neighbors of u are exactly X∪{z}. As B_z is empty, (1)–(3)
show that every new vertex within distance two of u lies in

    {b} ∪ B_v ∪ N_H(b).

This set has size at most 1+2+2=5, strictly less than nine. This is the
final contradiction. Together with the previous cases and the two cited
no-addition exclusions, it proves the theorem.

## Interpretation and scope

An HS59 construction cannot evade the one-deletion obstruction merely by
adding old edges. A successful proposal relative to a designated HS base
must delete at least two original HS edges, even if arbitrary old additions
are permitted. The two-deletion case with additions is not addressed here.

The preliminary sketch's W count was six; the correct count is five.
Accordingly the justified bound is d_H(b)≤2. The second group X of six lost
paths closes the proof directly, without the sketch's proposed universal
vertex conclusion for H.

No new computational evidence is needed for this exact argument. It does
not exclude arbitrary order-59 graphs, provide a new lower-bound graph, or
constitute a Lean proof. The global mathematical interval remains
57≤N(8,2)≤61. No unresolved gap remains in the added-edge case analysis;
the two explicitly cited analytic no-addition results are the dependencies
of the combined theorem.
