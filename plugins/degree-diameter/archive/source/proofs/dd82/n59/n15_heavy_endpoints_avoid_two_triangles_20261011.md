# N15 alone excludes zero-to-two-triangle heavy nonedges

Status: complete new paper derivation, pending fresh review. This recovers the
relevant old N4 conclusion from an explicit, simpler hypothesis: every
zero-triangle vertex has the actual 2211 matching row. No H5 minimal-root
qualification, K bound, N9, or global t<=2 premise is used.

## Statement

Let G be an original legal graph on59 vertices and let B=A²+A−7I−J be its
actual integer defect matrix. Assume N15 at every zero-triangle vertex:
exactly two entries2 and two entries1, with the equal-weight endpoints adjacent.
If z lies in no triangle and B_zv=2, then v lies in at most one triangle.

The original repeat budget already implies t(v)<=3. Since an edge incident
to z has B=0, zv is a nonedge. The case t(v)=3 has nonedge repeat budget0,
so only t(v)=2 requires proof.

## Root structure for a hypothetical t(v)=2

Put P=N(v), Y=V\(P union {v}), and H=G[P]. The original root bound makes G
8-regular, so |P|=8. There are exactly two edges in H. For q in P,

    B_vq = deg_H(q),

because B on a true edge equals the number of common neighbors.

The nonedge repeat budget is 6−2t(v)=2 and is entirely used by B_vz=2.
For every y in Y,

    |N(y) intersect P| = 1+B_vy.

Thus z has a three-point parent set S subset P, and every other point of Y
has exactly one parent in P. The three parents S are independent: any edge
between them would form a triangle through z.

There exists p in S isolated in H. If the two H edges are disjoint, an
independent set among their four endpoints has size at most2. If they share
an endpoint, their nonisolated part is a three-point path, again with
independence number2. Thus the independent three-point S contains a vertex
outside the nonisolated part.

The eight neighbors of p are v,z, and six ordinary points y in Y\{z}, all
having sole parent p. None of these six y is adjacent to z, because zpy
would be a triangle at z.

## The selected parent p is itself a zero vertex

For any of the six ordinary children y, use AB=BA at (v,y). The left side is

    (AB)_vy = sum_(q in P) B_qy.

On the right, the row of B at v is supported on P with weights deg_H(q)
and on z with weight2. Hence

    (BA)_vy = sum_(q in P) deg_H(q) A_qy + 2 A_zy
            = deg_H(p)
            = 0.

The second equality uses the sole-parent property and A_zy=0. All B entries
are nonnegative, so in particular B_py=0.

Also B_pv=deg_H(p)=0 and B_pz=0 because z lies in no triangle. These are
all neighbors of p. Every incident true edge has B value0, so there is no
triangle through p: a triangle would give a positive common-neighbor count
on each of its incident edges. N15 therefore applies at p.

## Its forced two light endpoints contradict N15

For q in P\{p}, p and q are nonadjacent because p is isolated in H.
Their common neighbors include v. There is no common neighbor in P, as p
has no H neighbor. Among Y, only z can have two parents. Consequently

    B_pq = |N(p) intersect N(q)|−1
          = 1 if q in S\{p}, and0 otherwise.

The two points of S\{p} therefore are two distinct weight-one endpoints
of p's actual B row. N15 gives exactly two such endpoints, so these are
the whole light pair and must be adjacent in G. But S is independent.
This is a contradiction.

It follows that t(v) cannot be2, and hence t(v)<=1.

## Consequences and scope

This lemma applies to every zero-triangle vertex under the stated global
zero-row N15 hypothesis, whether or not it is an extremal or otherwise
qualified root in an inherited H5 argument.

If the entire graph has exactly two intersecting triangles, any vertex
lying in both triangles is adjacent to every other nonzero-triangle vertex.
Its nonedge repeat budget2 can therefore only be supported on zero vertices.
The lemma rules out a single weight-two endpoint; hence it has exactly two
distinct nonedge repeats of weight one. This is a necessary condition,
not yet an exclusion of the two-triangle configurations.

The proof uses no finite enumeration, no short-cycle theorem and no
independently chosen matrix. It does not infer N15 for arbitrary original
graphs. A fresh proof-checker and cross-family review remain before promotion.

