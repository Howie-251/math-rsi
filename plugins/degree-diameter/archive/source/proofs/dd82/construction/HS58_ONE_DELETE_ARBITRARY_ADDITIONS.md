# HS58 with at most one old deletion and arbitrary old additions

Date: 2026-10-12. This is a bounded analytic reduction under the active
construction-first Goal. It uses the project formula-derivation workflow.

## Target and exact status

The target is to decide whether eight new vertices can extend an HS50 base
to a maximum-degree-eight, diameter-two graph on 58 vertices,
when at most one original old edge is deleted and arbitrary old nonedges
may be added.

**Complete exclusion of this construction family, with explicit finite
dependencies.** There is no such order-58 graph obtained from an HS50 base
by deleting at most one original old edge and adding arbitrary old edges.
The proof first handles additions meeting the deleted-edge endpoints and
reduces all other additions to an X–Y matching. Matching sizes 0,1,2,3,6
are excluded analytically. Size 4 and the unequal-port-set part of size 5
are excluded by three complete eight-vertex auxiliary enumerations. The
remaining equal-port-set part of size 5 is excluded analytically below.

This is a construction-family exclusion, not a theorem about arbitrary
order-58 graphs or old cores with two or more deleted HS edges. It is a
mathematical and finite-computation result, not a Lean theorem.

The size-six case is reduced both necessarily and sufficiently to a precise
six-color construction obligation. That obligation is then contradicted
by the original HS diameter-two property. No SAT is used. Section 5 states
the separate small-graph enumeration dependencies and their exact scope.

## Invariant object and notation

Q is the 50-vertex, 7-regular Hoffman–Singleton graph. It has no triangles
or four-cycles, and every nonadjacent pair has exactly one common neighbor.
All target vertices have degree eight: a vertex of degree at most seven
can reach at most 1+7+7·7=57 vertices within distance two.

Let L be the eight new vertices and H their induced graph. The final old
edge differences from Q are D (deleted original edges) and A (added original
nonedges). Write r_x=d_D(x), a_x=d_A(x), and B_x⊆L for the new neighbors of
old x. The exact port equation is

    p_x=|B_x|=1+r_x−a_x≥0.

Let K be the final old induced graph. The new vertices within distance two
of an old vertex x are exactly

    B_x ∪ ⋃_{y∈N_K(x)}B_y ∪ N_H(B_x).                    (1)

If p_x=0, x has eight old neighbors, and their port sizes must sum to at
least eight. Also, a pair involving such x must already have old distance
at most two whenever both endpoints are old.

For |D|=1 and |A|=a, summing the degree equations gives

    sum_x p_x=52−2a,          |E(H)|=6+a.                 (2)

All conclusions below apply to arbitrary choices of the deleted HS edge;
no HS edge-transitivity or automorphism assumption is needed.

## 1. No deletion, and additions at deleted-edge endpoints

### No deleted edge

If D is empty, every old vertex has at most one port. An added edge zw
would make both endpoints zero-port. Vertex z has eight old neighbors,
including zero-port w, and therefore at most seven available new-label
incidences. This contradicts the eight required new labels. Thus A is
empty too, and the existing
[induced-HS order-58 exclusion](CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md)
applies.

Henceforth D={uv}. Only u and v can have two ports; all other old vertices
have at most one. Any ordinary old vertex is incident to at most one edge
of A, and such an incidence makes it zero-port.

### Two additions incident to one endpoint are impossible

If a_u=2, then p_u=0. Its eight old neighbors include its two zero-port
addition targets and exclude v, since uv is deleted. Every remaining
neighbor has at most one port. Thus their port sum is at most six, a
contradiction. The same applies to v. Therefore a_u,a_v≤1.

### Exactly one endpoint is touched

Suppose a_u=1 and a_v=0, with added edge uz. Then p_u=1 and p_v=2. Any
additional edge ww' not meeting u or v has two zero-port endpoints. To
reach eight new labels despite its zero-port neighbor w', vertex w must
have the sole two-port vertex v among its old neighbors. The same is true
of w'. As v is untouched by additions, w,w'∈Y=N_Q(v)\{u}.

The unique original old path u−v−w was deleted. Since w has no ports, it
must be repaired within K. The edge ww' cannot repair it: u is not adjacent
to w', as u and w' are distinct neighbors of v in Q. Other matching edges
do not meet w. The only possible repair is u−z−w, requiring zw∈E(Q).
The same reasoning requires zw'∈E(Q). But z has at most one common neighbor
with v in Q, whereas w and w' would be two. Contradiction.

Thus A={uz}. Put B_u={b} and |B_v|=2. Every x∈X=N_Q(u)\{v} is a singleton
port vertex. The lost path v−u−x cannot be replaced using uz, because
neither endpoint v,x equals u or z. Therefore

    B_x⊆B_v       for all six x∈X.                        (3)

At least five of the six vertices y∈Y have their lost u−v−y path unrepaired
within K. If z∈Y, the direct addition uz repairs its pair and no other one,
by triangle-freeness. If z∉Y, the route u−z−y repairs at most one pair,
by uniqueness of a common neighbor of z and v. The remaining five y are
singleton vertices and must have B_y={b}. Including u, the b column has
at least six old incidences, so

    d_H(b)≤2.

Now N_K(u)=X∪{z}, with B_z empty. Equations (1) and (3) bound the new
vertices reachable from u by

    |{b}∪B_v∪N_H(b)|≤1+2+2=5<8.

This excludes the entire one-deletion/one-addition form D={uv}, A={uz},
without needing to assume H is a star.

### Both endpoints are touched

Suppose a_u=a_v=1. Then every old vertex has at most one port. An additional
edge between ordinary vertices would give a zero-port vertex a zero-port
neighbor and at most seven available labels. Therefore the entire addition
set is A={uz,vw}, with distinct ordinary targets z,w. Write B_u={b_u} and
B_v={b_v}.

For the six x∈X, the only added edge able to repair the lost v−u−x route
is vw. It repairs at most one such pair: either x=w directly, or through
a unique original common neighbor of u and w. Hence at least five x have
B_x={b_v}. By the corresponding argument at Y, at least five y have
B_y={b_u}. In particular d_H(b_u)≤2.

All port labels supplied by X therefore lie in {b_v} together with at
most one exceptional singleton label. The added old neighbor z has no
ports. Formula (1) at u gives at most

    1 + 1 + 1 + 2 = 5

reachable new labels, again impossible. This completes every case in which
an addition touches u or v.

## 2. Untouched endpoints force a cross matching

Now a_u=a_v=0. Write P=B_u and T=B_v, both of size two. All additions form
a matching M between ordinary old vertices.

For a matching edge xy, x and y have zero ports. To reach eight new labels,
x needs at least one two-port vertex among its seven original neighbors;
otherwise its added zero-port neighbor y leaves only seven incidences.
Triangle-freeness prevents x from being adjacent in Q to both u and v.
Consequently x∈X∪Y, and likewise y∈X∪Y.

If x∈X, its unique original old path to v was x−u−v. After deletion, its
only possible old repair uses the sole new old edge at x, namely xy,
and then an original edge yv. This forces y∈Y. Thus M is a matching
between X and Y, of some size m≤6.

There are no Q edges within X, within Y, or between X and Y: such edges
would create a triangle or four-cycle through uv. Therefore any matching
between X and Y is a legitimate set of added nonedges.

The old pair uv still has no old route of length at most two, so

    P∩T≠∅.                                               (4)

Every unmatched x∈X is a singleton vertex with B_x⊆T, and every unmatched
y∈Y has B_y⊆P. Only u,v have two ports. Thus old intermediates can repair
at most the two new pairs P and T; H has at most two unordered vertex pairs
at distance greater than two. It has eight vertices and 6+m edges.

## 3. Matching sizes zero through three are excluded

For m=0, H has only six edges and is disconnected. Any disconnected graph
on eight vertices has at least seven pairs between components, contradicting
the two-pair bound.

We use the following small-graph lemma for m=1,2,3.

**Lemma.** An eight-vertex graph with 7, 8, or 9 edges and at most two bad
pairs (distance greater than two, including disconnection) has a universal
vertex.

**Proof.** The graph is connected because disconnection gives at least
seven bad pairs. With seven edges it is a tree. A nonstar tree has an edge
whose removal leaves parts of sizes a,b≥2, a+b=8. The (a−1)(b−1)≥5 pairs
away from that edge's endpoints have distance at least three.

With eight edges, minimum degree at least two would force the cycle C8,
which has more than two bad pairs. Otherwise there is a leaf, whose neighbor
h has degree d≥5, since the leaf has exactly 7−d bad partners. There cannot
be two vertices of degree at least five, since their incident-edge union
would contain at least nine edges. Every leaf consequently meets h. If L
is the number of leaves, degree sum 16 gives L≥d−2. The nonneighbors of h
are not leaves, so there are at least L(7−d) distinct bad leaf pairs. This
exceeds two for d=5 or 6. Thus d=7.

With nine edges, counting edges and two-step witnesses gives
sum_w binom(d(w),2)≥28−9−2=17. If minimum degree were two, degree sum 18
would leave only two increments above all-degree-two, giving at most
binom(4,2)+7=13 such witnesses. Hence there is a leaf and its neighbor has
degree at least five.

If two vertices have degree at least five, they must be adjacent, both
have degree five, and all nine edges meet them. Of the other six vertices,
two meet both centers and two meet only each center. The four cross pairs
of these exclusive leaves are bad. Thus the high-degree vertex h is unique,
all leaves meet it, and degree sum 18 gives L≥d(h)−4.

For d(h)=5, the leaf-pair bound forces L=1. All six other vertices have
degree two. Four of them neighbor h, and two do not. Each of the two
nonneighbors can reach at most two of those four neighbors within two
steps: after deleting h, those four have degree one and the other two have
degree two. Thus there are additional bad pairs beyond the two leaf pairs.
For d(h)=6, the leaf-pair bound forces L=2, and the five other vertices all
have degree two. The unique nonneighbor of h meets two of h's four nonleaf
neighbors; it has distance greater than two to the other two, in addition
to its two bad leaf pairs. Both cases are impossible, so d(h)=7. ∎

Let h be the resulting universal new vertex. Its old attachment column has
size 8−7=1; let s be its unique old neighbor. Every zero-port endpoint of
M must reach h through s, so s must be an old common neighbor of both
endpoints of every matching edge xy.

For a matching pair x∈X,y∈Y, their only common old neighbor is their original
unique Q common neighbor r_xy outside {u,v}∪X∪Y. The added matching edge
creates no additional common neighbor. Distinct matching edges have
distinct r_xy: any such old vertex neighbors exactly one member of X and
exactly one member of Y, by the unique-common-neighbor property with u,v.
Thus m≥2 is incompatible with a single s.

For m=1, H is a star and s=r_xy is outside {u,v}, so h∉P∪T. Formula (1)
at u, the unmatched-X port restriction, and (4) yield at most

    |P∪T|+|N_H(P)|≤3+1=4

new vertices within distance two. This excludes m=1 as well.

## 4. Size six: exact construction obligation and contradiction

Let R be the 36 vertices outside {u,v}∪X∪Y. Each r∈R is nonadjacent to u,v,
so it has exactly one X neighbor and one Y neighbor; its other five Q
neighbors lie in R. Every x∈X and y∈Y are nonadjacent and have a unique
common neighbor in R. These facts identify R bijectively with a 6-by-6
grid, with rows indexed by X, columns by Y, and induced degree five.

For m=6 all X and Y vertices have zero ports, u,v have two each, and all
R vertices have singleton ports. For a row x∈X, its old neighbors are u,
six R vertices, and its zero-port matching partner. To cover eight new
labels, the six R singleton colors must be exactly L\P, each once.
Each column similarly contains exactly L\T.

Counting each color in all six rows and in all six columns forces P=T=C,
a two-element set. The other six labels occur exactly six times in R,
and the two labels in C never occur in R. Thus the degree equations give
degree six in H for each C vertex and degree two for each other new vertex.

An R vertex of color b cannot reach either C label through an old
intermediate: its X,Y neighbors have zero ports and its R neighbors have
colors outside C. Hence b is adjacent in H to both C vertices. Since
every non-C label occurs in R and has H degree two, this forces

    H=K_{2,6}, with the two C vertices on the size-two side.

The remaining old–new coverage at r∈R says precisely that its own color
and the colors of its five R neighbors are all six different labels.
Therefore every grid row, every grid column, and every closed R
neighborhood must contain all six colors once.

This obligation is also sufficient. Given such a coloring, retain Q−uv,
add any perfect matching X–Y, join u and v to both C vertices, join each
R vertex to its color label, and take H=K_{2,6}. All degrees are eight.
The old pair uv is covered through C; the twelve old pairs whose unique
two-step paths used uv are repaired by the X–Y matching. All other old
pairs retain their original routes. Row and column colors cover old–new
pairs at X,Y; the closed-neighborhood colors cover them at R; H covers
the remaining pairs. The resulting explicit definition would have
58 vertices and 232 edges.

However, that coloring cannot exist. Any two distinct R vertices are
adjacent or have a common neighbor in Q. Adjacent vertices cannot share
a color by the closed-R-neighborhood condition. A common neighbor cannot
be u or v. If it belongs to R, its closed neighborhood forbids equal
colors; if it belongs to X or Y, the corresponding row or column forbids
equal colors. Thus **every two R vertices must have different colors**,
requiring 36 colors rather than six. This excludes m=6 for every original
HS edge and every added perfect matching.

The independent actual-instance check is saved in
[HS58_EDGE_K26_ACTUAL_CHECK.md](HS58_EDGE_K26_ACTUAL_CHECK.md). For the
explicit edge (0,1), it verified the 36-vertex grid and classified all
630 R pairs into 90 R edges, 360 pairs with a common R neighbor, 90 same-row
pairs and 90 same-column pairs. No clique or exact-cover search was run.

## 5. The finite auxiliary dependencies

After Sections 1–4, the only cases still needing treatment have:

- Delete a single HS edge uv.
- Add a size-four or size-five matching M⊆X×Y; add no other old edges.
- Matched X,Y vertices have zero ports. Unmatched X singleton ports lie
  in T=B_v, and unmatched Y singleton ports lie in P=B_u, where P,T are
  intersecting two-element subsets of the eight new labels.
- All 36 R vertices have singleton ports. H has ten edges for m=4 or
  eleven edges for m=5. Every new pair other than possibly P and T must
  already have H distance at most two, and each H degree must match its
  old attachment column through d_H(b)+|{x:b∈B_x}|=8.
- All old–new coverage obligations in (1) needing simultaneous realization
  in the same attachment sets and H.

A further exact count supplies necessary conditions for the auxiliary check:
every label outside P∩T must occur on at least m vertices of R. Selected
zero-port rows or columns each need that label, and each R vertex belongs
to only one row and one column. In particular, if P≠T, then 7m≤36; for
m=5, the seven outside labels each occur at least five times and the one
common label occurs in R at most once.

In particular these are necessary degree bounds for a finite auxiliary
check:

    d_H(a)≤6                         if a∈P∩T;
    d_H(a)≤7−m                       if a∈P△T;
    d_H(a)≤8−m                       if a∉P∪T.

The first bound uses the two old incidences from u,v. The second uses at
least m R incidences and one additional incidence from u or v. The third
uses at least m R incidences. Permuting only the eight new labels reduces
the port sets to P=T={0,1}, or P={0,1},T={0,2}. These cover every pair of
intersecting two-element port sets; no old-vertex symmetry is assumed.

The complete finite check uses all 28 possible edges on eight labeled
vertices. It chooses exactly 6+m edges, pruning a branch only when an
endpoint degree would exceed the stated cap or too few undecided edges
remain to reach the target count. At each complete edge set it computes
the actual closed two-ball of every vertex. It accepts precisely when
every missing pair is one of P or T. The three zero-survivor cases below
therefore contain every auxiliary graph of the corresponding original
graph family.

| m | P | T | Degree-bounded H edge sets checked | Survivors |
| ---: | --- | --- | ---: | ---: |
| 4 | {0,1} | {0,1} | 10,350,991 | 0 |
| 4 | {0,1} | {0,2} | 6,721,718 | 0 |
| 5 | {0,1} | {0,2} | 102,256 | 0 |
| 5 | {0,1} | {0,1} | 1,978,650 | 870 |

All four traversals completed within one shared 10-CPU-second budget.
The enumeration reported 0.703368 CPU seconds; process resource accounting
reported 0.501049 user plus 0.204428 system CPU seconds, with exit zero and
no timeout. The actual implementation and results are
[hs58_one_delete_auxiliary.cpp](../../../computations/dd82/construction/hs58_one_delete_auxiliary.cpp),
[runner](../../../computations/dd82/construction/hs58_one_delete_auxiliary.py),
[enumeration.json](../../../computations/dd82/construction/hs58_one_delete_auxiliary_run/enumeration.json),
and [resources.json](../../../computations/dd82/construction/hs58_one_delete_auxiliary_run/resources.json).
The enumerating agent's standalone specification and completeness argument
are in [HS58_ONE_DELETE_AUXILIARY_ENUMERATION.md](HS58_ONE_DELETE_AUXILIARY_ENUMERATION.md).

The source was read against the mathematical conditions: its include/exclude
recursion visits every fixed-cardinality edge subset not already ruled out
by a monotone degree cap; its terminal test forms the union of adjacency
rows for all neighbors and compares missing vertices against the two
allowed-pair masks. Every case's completion flag is true. This executable
finite enumeration, together with the candidate-preserving reduction above,
is the computational dependency for the three zero-survivor rows. It is
not an LRAT certificate or an analytic replacement for those finite cases.

The nonzero row must not be interpreted as an exclusion. Its 870 graphs
satisfy necessary H conditions only. The initial output saved 100 examples;
subsequent relabeling recovered and independently BFS-checked 510 distinct
survivors, not all 870. Neither a complete survivor list nor a classification
of their isomorphism types is needed for the analytic argument in Section 6.
That argument covers every possible H in the nonzero row directly.

## 6. Size five with equal endpoint ports: analytic closure

Now m=5 and P=T=C={a,b}. There is exactly one unmatched row vertex x_0∈X
and one unmatched column vertex y_0∈Y. Their singleton colors lie in C.
Let r_0∈R be their unique grid intersection.

Every matched row and column has all six colors outside C, once each.
Therefore a common color can occur in R only at r_0. Let δ be one if
r_0 has a color in C and zero otherwise. The old attachment incidences
in the two common columns consist exactly of four from u,v, two from
x_0,y_0, and δ from R. Consequently

    d_H(a)+d_H(b)=16−(4+2+δ)=10−δ∈{9,10}.               (5)

### Common degrees and ordinary-color frequencies

Neither common vertex can have H degree six. If c∈C did, let z be its
unique nonneighbor. Removing c from H leaves seven vertices and five
edges, because |E(H)|=11. For every other vertex s of that remaining graph,
the pair z,s is not the exceptional pair {a,b}: if z is the other common
vertex, c has been removed; otherwise z is not common at all. Thus z
would have to reach all six s within two steps in H−c, since z is not
adjacent to c. A seven-vertex graph with only five edges cannot be connected,
giving a contradiction. The existing cap d_H(c)≤6 now gives d_H(c)≤5.
Together with (5), the common degree pairs are only (5,5) and (5,4).

Each of the six ordinary colors, meaning labels outside C, has H degree
at least two. An isolated ordinary label has seven forbidden bad pairs.
If an ordinary label were a leaf, all its seven pairs would need H
distance at most two, forcing its neighbor to be universal of degree
seven. This violates the common cap six and ordinary cap three.

The total H degree is 22. In the common-degree-(5,5) case every ordinary
color therefore has degree two and exactly six old attachments, all in R.
In the (5,4) case five ordinary colors have degree two and six R attachments
each; one ordinary color has degree three and five R attachments. In both
cases every ordinary color occurs at most six times in R.

The five R neighbors of r_0 lie in five different matched rows and five
different matched columns. None is in its own row or column, by HS
triangle-freeness. Two in the same other row or column would give r_0 and
the associated X or Y vertex two common neighbors in Q. Thus the five
R neighbors occupy exactly one cell in each matched row and column.

### Case δ=0: common degrees (5,5)

No R vertex has a common color. Each common label has old capacity three,
of which u and v already use two. Thus x_0 and y_0 have different common
colors; after interchanging row and column names, let their colors be
a and b respectively.

If an ordinary label c is not adjacent to a in H, an R vertex of color c
can reach new a only through old x_0. Indeed, no R vertex is colored a,
y_0 is colored b, matched row/column vertices have no ports, and the
direct H route from c to a is absent. Therefore all six occurrences of c
must occupy the entire unmatched row. Likewise any ordinary color not
adjacent to b must occupy the entire unmatched column.

Each common vertex has degree five but there are six ordinary labels, so
each misses at least one ordinary label. If the two forced labels are
different, they conflict at the row-column intersection. If they are the
same, that color would need to occupy two different six-cell sets whose
union has eleven cells, while its total frequency is six. Both alternatives
are impossible.

### Case δ=1: common degrees (5,4)

Name a,b so that d_H(a)=5 and d_H(b)=4. Their old capacities are three
and four, respectively. Besides the two incidences each from u,v, their
remaining capacities are one for a and two for b. The three remaining
common-colored old vertices are x_0,y_0,r_0.

If r_0 has color a, both x_0 and y_0 have color b. For an ordinary color c
not adjacent to b in H, its occurrence in each of the five matched rows
must be in the unmatched column: there is no R vertex colored b, and only
the two unmatched parents carry b. Its occurrence in each of the five
matched columns must likewise be in the unmatched row. These are ten
different cells, exceeding c's R frequency of at most six. Thus every
ordinary color would have to be adjacent to b, contradicting d_H(b)=4.

It remains that r_0 has color b. The unmatched parents then have one color
a and one color b; take x_0 to have color a and y_0 color b. Any ordinary
color not adjacent to a must have every occurrence in the unmatched row,
since x_0 is the only old vertex other than u,v that supplies a and R
vertices are adjacent to neither u nor v. In each of the five matched
columns that color must occur once. Hence it fills all five noncentral
cells of the unmatched row. At most one ordinary color can have this
property. If ab were an edge of H, degree-five a would miss at least two
of the six ordinary labels. Therefore ab is not an edge.

Vertex b, of degree four and not adjacent to a, consequently misses at
least two ordinary labels. Let c be one of them. In any matched column,
an R vertex of color c can reach b only through its R neighbor r_0:
the column parent has zero ports, the unmatched row parent carries a,
and the only other parent carrying b belongs to the unmatched column.
There are no other R vertices of color b, and the c–b edge of H is absent.
As c occurs once in each matched column, it must occupy all five R
neighbors of r_0, exactly one in each such column. Two different labels
missing b cannot both occupy those five vertices. This is the final
contradiction, closing every size-five equal-port case analytically.

## Conclusion and dependency boundary

The cases cover every final old-edge set with at most one missing HS edge:
Section 1 handles no deletion and additions meeting a deleted endpoint;
Section 2 forces all other additions to be a matching of size at most six;
Sections 3 and 4 exclude sizes 0,1,2,3,6 analytically; Section 5 excludes
size 4 and unequal endpoint ports at size 5 by completed finite auxiliary
enumeration; Section 6 excludes the remaining size-five case analytically.

Thus the stated HS58 family is impossible even when arbitrary old–old
additions are allowed. The all-870 auxiliary classification is not a
dependency, and the partial recovery of survivor examples is not used as
evidence of complete recovery. Independent mathematical reviews helped
check the derivation; the recorded executable and actual completed outputs
are the evidence for the finite cases.

This result does not change the unresolved status of arbitrary order-58
graphs or assert a result for two old deletions. No valid new graph, SAT
certificate, or Lean theorem is claimed.
