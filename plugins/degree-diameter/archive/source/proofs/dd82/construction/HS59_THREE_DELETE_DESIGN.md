# HS59 with exactly three deleted old edges

Date: 2026-10-11. **The entire three-edge-deletion family is analytically
impossible.** A complete nine-vertex tree enumeration independently confirms
the small auxiliary-graph classification. Two complete expanded seeds were
also generated and independently checked. No SAT solver was run.

## Target, assumptions, and exact object

Let Q be a Hoffman–Singleton graph on 50 old vertices. Delete exactly three
of its edges, add nine new vertices, and add no old–old edges. Suppose the
expanded graph has maximum degree eight and diameter two. Such a 59-vertex
graph is 8-regular, since a degree-at-most-seven vertex reaches at most
1+7+7·7=57 vertices in two steps.

Let D be the three-edge deleted graph and r_v=d_D(v). Write B_v for the set
of new neighbors of old v, and H for the induced graph on the nine new
vertices. Then

    |B_v|=1+r_v,       sum_v r_v=6,
    sum_v |B_v|=56,    |E(H)|=(72−56)/2=8.

A new vertex a belongs to exactly 8−d_H(a) sets B_v. The invariant object is
the single actual graph [[A',B],[B^T,H]], with the same attachments satisfying
old–old, old–new, and new–new coverage. No controller is assumed in advance.

Call a pair of new vertices *bad in H* if it has neither an H edge nor a
common H neighbor. It must be repaired by a shared old neighbor.

## 1. H must be a tree

The total number of pairs supplied by all old vertices is at most

    sum_v binom(1+r_v,2)
      = 6 + sum_v binom(r_v,2)
      ≤ 6 + binom(3,2) = 9.

The inequality counts intersecting pairs among the three deleted edges; each
pair shares at most one vertex. A separate local bound is essential: for any
fixed new label z, the number of partners supplied through old vertices is at
most

    sum_{v: z∈B_v} (|B_v|−1)
      = sum_{v: z∈B_v} r_v ≤ 6.                    (1)

If H were disconnected, all pairs in different components would be bad.
A component of size a∈{2,...,7} gives a(9−a)≥14 such pairs, contradicting the
nine-pair bound. The only remaining disconnected partition is 1+8: multiple
isolates or other partitions already exceed nine cross-component pairs. But
its isolated vertex has eight bad partners, contradicting (1).

Thus H is connected; with nine vertices and eight edges, it is a tree. This
also checks the proposed disconnected-case reduction without relying on a
numerical tree generator.

## 2. Only a star or a once-subdivided star can occur

In a tree, two distinct length-two paths cannot have the same endpoints.
Writing W(H)=sum_a binom(d_H(a),2), the bad-pair count is exactly

    b(H)=binom(9,2)−8−W(H)=28−W(H).

Since b(H)≤9, we have W(H)≥19. H has positive degrees summing to 16. If all
degrees were at most six, convexity concentrates the seven increments above
the all-one sequence as 5+2, giving

    W(H) ≤ binom(6,2)+binom(3,2)=18.

This is impossible. Hence H has maximum degree seven or eight:

- Degree eight: H=K_{1,8}, with no bad pairs.
- Degree seven: let h be the high vertex. Its seven incident edges leave
  one outside vertex z and one remaining edge; connectivity attaches z to a
  neighbor w of h. Thus H is a star with one edge subdivided. Let S be the
  other six neighbors of h. The bad pairs are exactly {z,s}, s∈S, forming
  K_{1,6}.

This is a self-contained complete classification. The requested enumeration
of all 47 nonisomorphic nine-vertex trees found exactly these two survivors.

## 3. Universal-star H is impossible for every deleted topology

Because Q has girth five, D is a forest and has a leaf u. Let uv be its unique
deleted incident edge. Then r_u=1 and |B_u|=2. Deleting uv destroys its old
adjacency and there was no old two-step replacement, so

    B_u∩B_v ≠ ∅.                                  (2)

For every retained old neighbor x of u, the unique old length-two path
v-u-x was also destroyed. Hence B_x∩B_v≠∅. If x is not a deleted-edge endpoint,
its singleton B_x lies in B_v. If x is a deleted-edge endpoint, it contributes
at most r_x additional labels beyond B_v.

The universal new vertex h has no old neighbors, since d_H(h)=8. Thus B_u
contains only star leaves and N_H(B_u)={h}. All new vertices reachable from
u in at most two steps lie in

    B_u ∪ B_v ∪ {extra labels from special retained neighbors} ∪ {h}.

By (2), |B_u∪B_v|≤r_v+2. The number of reachable new vertices is therefore at
most

    r_v+3 + sum_{x special retained neighbor of u} r_x
      ≤ 3 + (sum_x r_x−r_u)
      = 8,

because v is not a retained neighbor of u, and all terms in the sum are
among deleted-edge endpoints other than u,v. This is fewer than nine,
contradicting diameter two. The same argument covers all four possible
three-edge forest topologies at once.

## 4. Subdivided-star H forces a disjoint-port design

Retain the notation h,w,z,S from Section 2. The six pairs z–S are bad in H.
They must all be supplied through old vertices. The local bound (1) has total
budget exactly six, so equality is forced throughout:

    z∈B_v for every v with r_v>0;
    B_v = {z} ∪ P_v,      |P_v|=r_v;
    the P_v are pairwise disjoint, with disjoint union S.     (3)

Indeed omitting z at a positive-r_v endpoint loses some of the available six
slots; a repeated partner or a partner outside S also wastes a slot. Thus all
six slots must be distinct and must be exactly S. This is a fully explicit
small attachment design, rather than a relaxed pair count.

The new leaf z has total old attachment capacity 8−d_H(z)=7.

### Deleted topology with a branching vertex

If r_c≥2, take two deleted neighbors a,b of c. Every ordinary retained old
neighbor x of c has its singleton in both B_a and B_b, because the old paths
a-c-x and b-c-x were destroyed. By (3), B_a∩B_b={z}; therefore B_x={z}.

There are exactly three nonmatching topologies for D. Their forced incidences
at z exceed its capacity seven:

| Deleted topology | Deleted-edge endpoints already at z | Additional ordinary neighbors forced to z | Total lower bound |
| --- | ---: | ---: | ---: |
| Three-edge star K_{1,3} | 4 | 4 retained neighbors of the center | 8 |
| Three-edge path P4 | 4 | 5 retained neighbors of either internal vertex | 9 |
| Two-edge path plus disjoint edge | 5 | at least 4 retained neighbors of the path center | 9 |

The counts hold for every embedding in Q. For P4, the remote endpoint cannot
be adjacent to the chosen internal vertex, since that would make a triangle;
all five retained neighbors are ordinary. For the two-edge path plus an edge,
at most one endpoint of the separate edge can be adjacent to the path center,
since those two endpoints are adjacent in Q. Hence at least four of the five
retained neighbors are ordinary. The star center's four retained neighbors
are all ordinary by definition of its three deleted edges.

These three cases are impossible.

### Three disjoint deleted edges

Now all six deleted endpoints have r_v=1. By (3), write

    B_v={z,a_v},   with all six a_v distinct and forming S.

Take a deleted edge uv. Every ordinary retained old neighbor of u attaches
to z or a_v, because its singleton must meet B_v. Among the remaining four
deleted endpoints, at most two are retained neighbors of u: u can be adjacent
to at most one endpoint of each of the other deleted edges, by triangle-
freeness of Q. Each such special neighbor adds just its private label a_x.

The direct new neighbors of u are z,a_u. Through a new intermediate it reaches
only w,h, because z is adjacent to w and a_u is adjacent to h in H. Through
ordinary old intermediates it adds at most a_v; through the at-most-two
special old intermediates it adds at most two private labels. Thus u reaches
at most

    2 + 2 + 1 + 2 = 7

new vertices in two steps, fewer than nine. This final topology is impossible.

Sections 3 and 4 exclude every possible H and every three-edge deleted graph.
The endpoint arguments were independently checked by the Petersen-fibers
agent, including the local equality condition (3) and all capacity counts.

## 5. Actual finite outputs and independent expanded-graph checks

[Generator](../../../computations/dd82/construction/hs59_three_delete.py)
uses the already installed NetworkX 3.4.2 `nonisomorphic_trees(9)`. It records
all 47 trees, every edge list, every bad pair, degrees, and wedge counts in
[tree_catalog.json](../../../computations/dd82/construction/hs59_three_delete/tree_catalog.json).
The enumeration took **0.003491 CPU seconds** on one pinned CPU and retained
exactly the star and subdivided star. It also checks b(H)=28−W(H) for every
generated tree. No graph search or SAT solver was launched.

Two complete seeds delete old edges {(0,1),(0,4),(0,25)}, a three-edge star.
The endpoint ports are

    B_0={0,1,2,3}, B_1={0,4}, B_4={0,5}, B_25={0,6}.

For the first seed H has universal vertex 8. For the second H has edges
{8,a}, a=1,...,7, and {7,0}, so the displayed ports realize all six required
new–new repairs. In either seed, the remaining old attachment capacity at
new label 0 is three. Three retained old neighbors of old 0 spend these
slots; the remaining ordinary old vertices fill all other capacities in
increasing label order. This produces a complete explicit graph, with the
fourth retained neighbor visibly unable to join all three deleted leaves
through the required common new label.

The independent BFS checker reads only each saved expanded edge list and
rebuilds the graph. Both seeds have:

| Vertices | Edges | Degrees | Diameter | Bad old–old pairs | Bad old–new pairs | Bad new–new pairs |
| ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 59 | 236 | all 8 | 3 | 15 | 115 | 0 |

Full edges, generating ports, every bad pair, distance, and complete common-
neighbor list are preserved in `star.seed.json`, `star.seed.verification.json`,
`subdivided_star.seed.json`, and `subdivided_star.seed.verification.json` under
[the artifact directory](../../../computations/dd82/construction/hs59_three_delete/).
The failed seeds illustrate the simultaneous-design obstruction; they are
not used as exhaustive evidence and are not valid lower-bound witnesses.

## Scope and next implication

This theorem covers arbitrary embeddings of exactly three deleted HS edges,
with nine added vertices and no new old–old edges. It requires no edge-
transitivity premise, symmetry restriction on B, or SAT completeness claim.
It does not exclude arbitrary order-59 graphs.

Together with the preceding induced-HS, one-deletion, and two-deletion
results, a deletion-only HS order-59 construction must delete at least four
old edges. No global DD82 interval or Lean status changes. This bounded task
has no remaining mathematical design obligation; any further deletion count
changes H and the attachment budgets and is a separate task.

## External construction discussion C4

Gemini read the substantive argument above and found no gap, using the existing Antigravity thread and requested/CLI-selected gemini-3.8-flash-high/high. Raw response: `reviews/dd82/20261011_C4_hs59_three_four.json`. Root independently read the argument and retained exact result scopes. This discussion is provisional corroboration, not a Lean proof or backend model attestation.
