# Paper exclusion of the C7-invariant internal-pin S11 rule

This is an independent paper check of the proposed domination argument. No
numerical calculation, graph validation, BFS, solver, symmetry search or
rewiring search was run. The earlier experimental RESULT files are unchanged.

The conclusion applies only to the following fixed model. The accepted source
G has 106 vertices and diameter at most two. Its actual verified C7 action has
eight fixed vertices

    F = {7,17,23,34,46,54,59,105}

and fourteen free orbits of size seven. All free vertices have degree11; the
two degree10 vertices34 and54 are fixed, and every other fixed vertex has
degree11. Choose an invariant pin set S, change only old edges with both
endpoints in S, and add one new vertex z adjacent precisely to S. Require the
result to preserve this C7 while fixing z, have order107, maximum degree11,
and diameter at most two. The only pin sizes considered are10 and11.

## Degree and orbit consequences

Every vertex of any such107-vertex candidate must have degree at least10:
a degree-d root in a graph of maximum degree11 has at most

    1 + d + 10d = 1 + 11d

vertices within distance two, which is at most100 when d<=9.

Since S is invariant and the action has only eight fixed points, S must be
one seven-orbit O together with three fixed points when |S|=10, or four fixed
points when |S|=11. There cannot be two free orbits, and fixed points alone
cannot supply either size.

Let K=S intersect F and let q=|K|, so q is3 or4. A fixed vertex is adjacent
to either every point of O or none. For f in K, changing this bundle adds or
deletes seven neighbors. The other editable old incidences of f are only the
q-1<=3 pairs to other points of K, while z adds one neighbor. Adding a bundle
would therefore give degree at least

    10 + 1 - 3 + 7 = 15 > 11.

Deleting one would give degree at most

    11 + 1 + 3 - 7 = 8 < 10.

Thus all fixed-to-O bundles stay unchanged. Bundles from unselected fixed
vertices were already frozen cross edges.

Write r for the degree of the original induced graph G[O]. A C7-invariant
simple undirected graph on seven points is a union of cyclic-difference rings,
so both its original and final internal degrees are even. Every other old
incidence of a point of O stays unchanged, while z adds one. Its final degree
is therefore

    12 + (r_new - r),

which is even and must lie in[10,11]. Consequently its final degree is10,
r_new=r-2, and r belongs to{2,4,6}. In particular r=0 is already impossible.

For |S|=10 this gives the earlier direct new-root bound

    |B_2(z)| <= 1 + 10 + 7*(10-1) + 3*(11-1) = 104 < 107.

The remaining argument addresses |S|=11, with q=4.

## Closed domination is necessary before any internal rewiring

An old vertex outside S can reach z in at most two steps only through an
original neighbor in S: all edges from S to its complement are frozen.
Selected old vertices are themselves in the closed neighborhood of S.
Therefore the source must satisfy

    N_G[S] = V(G).

This uses closed domination; no additional open-neighbor requirement is
imposed on an already selected vertex.

Let k=|N_G(u) intersect F| for u in O. It is independent of the choice of u
because all fixed vertices are fixed pointwise and O is a transitive orbit.
There are exactly k fixed vertices adjacent to O, each adjacent to all seven
points. Each point of O has11-r-k neighbors outside O and F. Counting their
incidences, with possible repetition only increasing this upper bound, gives

    |N_G[O]| <= 7 + 7*(11-r-k) + k
              = 84 - 7r - 6k.

Any fixed vertex can be adjacent to at most one free seven-orbit, since two
such orbits would already give degree at least14. Thus four fixed points can
cover at most28 free points. Including all eight fixed vertices is a valid
upper bound for the rest of their closed neighborhood, so

    |N_G[K]| <= 28 + 8 = 36.

It follows that

    106 = |N_G[S]| <= |N_G[O]| + |N_G[K]|
                       <= 120 - 7r - 6k.

For r>=4 the right side is at most92. For r=2 and k>=1 it is at most100.
The only numerical possibility left is r=2 and k=0, where the upper bound
is exactly106.

## The only equality case has an unavoidable duplicate outside neighbor

When r=2, a C7-invariant induced graph on O is a seven-cycle: its single
nonzero undirected difference generates the cyclic group of prime order7.
Choose two points u,v at distance three on this cycle. They are not adjacent
and have no common neighbor inside O. The source G has diameter at most two,
so u and v must have a common neighbor outside O. Since k=0, this common
neighbor is not fixed either.

Thus the7*(11-r-k)=63 incidences from O to outside free points cannot all
have distinct endpoints. At least one outside endpoint is counted twice.
The bound for N_G[O] is therefore strict:

    |N_G[O]| <= 7 + 62 = 69,
    |N_G[S]| <= 69 + 36 = 105 < 106.

This contradicts the necessary closed domination. No stronger orbit-counted
loss estimate or additional finite check is needed.

## Disposition and scope

The paper argument supports exclusion of both C7-preserving internal-pin
models with |S|=10 or11 for this source and this actual C7 action. S10 follows
from the new-root two-ball bound; S11 follows from the source closed-domination
count and its strict equality-case obstruction. This is separate from the
earlier numerical MILP UNKNOWN and does not turn that solver result into a
completed solve.

It does not exclude noninvariant pin sets, rewiring that breaks this C7,
changing edges with endpoints outside S, a different source, larger caps,
or other augmentation models. No symmetric pin-set or edge enumeration is
performed or implicitly authorized by this note.
