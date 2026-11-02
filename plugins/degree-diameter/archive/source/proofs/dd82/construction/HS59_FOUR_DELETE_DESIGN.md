# HS59 with exactly four deleted old edges

Date: 2026-10-11. Analytic exclusion of the entire stated construction
family, independent of the embedding of the four deleted edges. No SAT run.

Start with a Hoffman–Singleton graph Q on 50 vertices. Delete exactly four
old edges, add nine vertices, and add no old–old edges. Suppose the result
has maximum degree 8 and diameter at most 2. Its order exceeds 57, so it is
8-regular by the radius-two bound at a vertex of degree at most seven.

Write D for the deleted graph, r_x=d_D(x), B_x for the set of new neighbors
of old vertex x, and H for the induced new graph. Then

    |B_x|=1+r_x,     sum r_x=8,     |E(H)|=(72−58)/2=7.

The deleted graph is a forest: it has four edges, while Q has girth five.
Let k be its number of nonisolated vertices and c its number of components
after removing isolates. Thus k=c+4 and 5≤k≤8.

## 1. H has one isolated vertex and one eight-vertex tree

A new pair not reachable within H in two steps must have a common old
neighbor. The maximum number of pairs that old rows can supply is

    sum_x binom(1+r_x,2) = 8 + sum_x binom(r_x,2) ≤ 14.

The last sum counts pairs of deleted edges sharing an endpoint and is at
most binom(4,2)=6. Equality requires all four deleted edges to be pairwise
intersecting; since D is a forest, they form a four-edge star.

H is disconnected because it has nine vertices and only seven edges.
Three or more components create at least 15 cross-component pairs; two
components of sizes at least three create at least 18. Thus the only
possible component sizes are 1+8 or 2+7.

In the 2+7 case, all 14 available old-mediated pair slots are needed just
for cross-component pairs. Equality forces D to be a four-edge star, whose
center has |B_x|=5. All ten pairs in this five-set would have to cross the
two components. This is impossible: among any three elements, two lie in
the same component. Therefore H has an isolated vertex z and a connected
eight-vertex graph with seven edges, which is a tree K.

## 2. The isolated vertex forces a private-port partition

The eight pairs from z to the other new vertices must be covered through
old neighbors. An old neighbor x of z contributes exactly r_x possible
other new labels. The total deleted-degree budget is eight. Consequently
every old vertex with r_x>0 must be adjacent to z, and

    B_x={z} union P_x,     |P_x|=r_x,

where the private sets P_x are pairwise disjoint and partition V(K).
Since z has degree eight, exactly 8−k ordinary old vertices also have
B_x={z}. All other ordinary old rows are singleton labels in K.

Whenever xy is a deleted edge and w is a retained old neighbor of x,
the unique Q-path y-x-w of length two was destroyed. Triangle-freeness
ensures y,w were not adjacent; uniqueness of common neighbors ensures
there is no alternative old path. Therefore B_y intersects B_w.

In particular, if r_x≥2 and w is an ordinary retained neighbor of x,
the singleton B_w must meet the port sets of two distinct deleted
neighbors of x. Their private sets are disjoint, so B_w={z}.

## 3. The deleted graph is a star or a matching

Fix any x with r_x≥2. There is no retained Q-edge from x to another vertex
of its own D-component. Such a vertex has D-distance at most three from x:
a path of length four would use all four deleted edges and force x to be
an endpoint of degree one. A retained edge at distance two or three would
create a triangle or a four-cycle in Q; distance-one edges are deleted.

The component of x uses at least two deleted edges. Every other component
therefore has at most two edges and diameter at most two. The vertex x
has at most one retained neighbor in each such component, since two would
again create a triangle or four-cycle in Q.

There are c−1=k−5 other D-components. Of the 7−r_x retained Q-neighbors
of x, at least

    7−r_x−(k−5) = 12−k−r_x

are ordinary. They all require singleton port z, of which only 8−k are
available. Hence r_x≥4. Every non-leaf vertex of D must therefore have
deleted degree four. With only four edges, D is either the four-edge star
or a four-edge matching.

## 4. Both remaining deleted graphs are impossible

If D is a star with center x and leaves u_1,...,u_4, then k=5. Write
P_{u_i}={p_i}; the four p_i are distinct. Each leaf has six retained old
neighbors, all ordinary. Lost-path coverage puts their singleton labels
in B_x. Consequently the new labels reachable in two steps from u_i
are contained in

    {z,p_i} union P_x union N_K(p_i).

The first two sets contain six vertices. Covering all nine new vertices
requires d_K(p_i)≥3 for each of the four distinct p_i. The four other
vertices of the connected tree K each have degree at least one. Thus
the degree sum is at least 4*3+4*1=16, contradicting the tree's degree
sum 14.

If D is a matching, k=8 and every deleted endpoint u has
B_u={z,p_u}, with all eight labels p_u distinct. For an edge uv of D,
each ordinary retained neighbor of u has singleton label p_v: it must
meet B_v and there are no ordinary z rows left.

Among the six retained neighbors of u, at most three are other deleted
endpoints, at most one from each of the other three deleted edges; two
from the same edge would make a Q-triangle. These add at most three
private labels. Thus all reachable new vertices from u lie among

    {z,p_u,p_v}, at most three other private labels, and N_K(p_u).

Again d_K(p_u)≥3. This holds for all eight labels of K, requiring degree
sum at least 24 instead of 14. Contradiction.

Therefore no target exists in the four-deletion HS59 family. Together
with the induced-HS and one-, two-, three-deletion obstructions, a
deletion-only HS59 construction would have to delete at least five old
edges. This does not exclude arbitrary 59-vertex graphs or constructions
that add old–old edges.

## External construction discussion C4

Gemini read the substantive argument above and found no gap, using the existing Antigravity thread and requested/CLI-selected gemini-3.8-flash-high/high. Raw response: `reviews/dd82/20261011_C4_hs59_three_four.json`. Root independently read the argument and retained exact result scopes. This discussion is provisional corroboration, not a Lean proof or backend model attestation.
