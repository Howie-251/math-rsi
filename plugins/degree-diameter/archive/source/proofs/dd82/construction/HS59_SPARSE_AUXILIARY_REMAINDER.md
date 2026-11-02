# HS59 sparse auxiliary remainder: seven through eleven deletions

Date: 2026-10-11. **New uniform theorem: no successful deletion-only HS59
extension with 7≤t≤11 can have a deleted-degree-seven old vertex.** The proof
uses an exact classification of seven-point dominating sets after removing
one HS vertex. Both the classification and its application were independently
checked by the cyclic-lift agent.

The remaining maximum-deleted-degree-at-most-six family is **open** in this
note. A complete small auxiliary-graph catalog identifies its residual
inputs; necessary budgets are not treated as existence or nonexistence
proofs. No SAT or graph search was started.

## 1. Setup and exact isolated-vertex obligation

Let Q be the 50-vertex Hoffman–Singleton graph. Delete t old edges, add nine
new vertices, and add no old–old edges. Suppose the resulting graph has
maximum degree eight and diameter at most two. It is 8-regular by the
57-vertex radius-two bound for a vertex of degree at most seven.

Write D for the deleted graph, r_x=d_D(x), B_x for the new neighbors of old
x, A'=Q−D, and H for the graph on the nine new vertices. Then

    |B_x|=1+r_x,      sum_x r_x=2t,
    |E(H)|=11−t=m,    |{x:a∈B_x}|=8−d_H(a).

For every isolated new vertex z, its old neighborhood

    S_z={x:z∈B_x}

has size exactly eight and dominates every old vertex in A': an old vertex
outside S_z needs a retained old neighbor in S_z. Also S_z∩S_w is nonempty
for every two isolated new vertices z,w. These are simultaneous conditions
on the actual retained graph and attachments, not merely covering counts.

## 2. Seven-point domination lemma for Q minus one vertex

**Lemma.** Fix c∈V(Q). If T⊂V(Q)\{c}, |T|=7, dominates the induced graph
Q−c in the closed-neighborhood sense, then either

    T=N_Q(c),

or

    T=N_Q(x) for some x at distance two from c.

**Proof.** Write N_Q(c)={l_1,...,l_7} and

    L_i=N_Q(l_i)\{c}.

The seven sets L_i each have six vertices and partition the 42 vertices at
distance two from c. Each L_i is independent. Between any two different
L_i,L_j the old graph is a perfect matching. These facts follow from girth
five and the unique-common-neighbor property: a vertex in L_i has no other
neighbor among the l_j and has exactly one neighbor in each L_j, j≠i.

To dominate l_i after c is removed, T must meet {l_i}∪L_i. These seven cells
are disjoint and |T|=7, so T selects exactly one element from each cell.
Let k be the number of selected l_i. In a cell without its l_i selected,
write q_i for the selected vertex of L_i.

If k<7, consider one of these nonparent-selected cells L_j. It can be
covered only by q_j itself and the unique L_j neighbor of each of the other
6−k selected q_i. Thus six vertices must be covered by at most 7−k slots,
forcing k≤1. Hence k is 0, 1, or 7.

If k=7, then T=N_Q(c).

If k=1, say l_i is selected, each of the other six branches has exactly six
available domination slots for six vertices. Thus all those slots are
distinct. The six selected q_j, j≠i, are pairwise nonadjacent: an adjacency
would duplicate the direct selection of one q_j in its branch. Their unique
common old neighbor cannot be c or any l_j, and cannot lie in a branch L_j
with j≠i, since that would duplicate two domination slots there. It must
lie in L_i. Each q_j has exactly one neighbor in L_i, so all six q_j share
the same neighbor x∈L_i. They are precisely its six neighbors outside l_i,
and T=N_Q(x).

It remains to rule out k=0. Let

    m_v=|T∩({v}∪N_Q(v))|.

Each of the seven branches has exactly seven closed-domination slots:
the selected q_j itself and one neighbor from each of the other six q_i.
They cover six branch vertices, so exactly one vertex has m_v=2 and all
others have m_v=1. Each l_j has m_v=1, and c has m_c=0. Consequently

    sum_v binom(m_v,2)=7.

On the other hand, two nonadjacent vertices of Q have closed neighborhoods
intersecting in one vertex, and adjacent vertices have closed neighborhoods
intersecting in their two endpoints. Double counting gives

    sum_v binom(m_v,2)=binom(7,2)+|E(Q[T])|≥21,

a contradiction. This finishes the classification. ∎

## 3. Uniform exclusion of deleted degree seven

Suppose some old vertex c has r_c=7. Every edge incident to c was deleted,
so c has no retained old neighbors. Decompose

    D = {the seven edges incident to c} ∪ R,
    e=|E(R)|=t−7,       0≤e≤4,       m=|E(H)|=4−e.

Since H has at most four edges on nine vertices, it has an isolated vertex.
For any isolated new vertex z, c must be in S_z, since otherwise the old
isolated vertex c could not reach z in two steps. The other seven elements
of S_z dominate Q−c: they dominate the retained old graph without c, whose
edges form a subgraph of Q−c. The lemma applies.

### 3.1 The open neighborhood of a distance-two vertex is impossible

Suppose S_z={c}∪N_Q(x), where x is at distance two from c. Let r=d_R(x),
so |B_x|=1+r. Every retained old neighbor of x lies in S_z and therefore
has z among its new neighbors. Their union of new neighbors has size at most

    1 + sum_{y∈N_{A'}(x)} r_y.                     (1)

The contribution of the deleted seven-star to the sum is at most one:
x has exactly one neighbor among N_Q(c). The endpoints in N_Q(x) of an
edge of R cannot be both endpoints, because N_Q(x) is independent. Moreover,
the r edges of R incident to x contribute nothing to the sum over retained
neighbors: their opposite endpoints were removed from N_{A'}(x). Hence

    sum_{y∈N_{A'}(x)} r_y ≤1+e−r.                 (2)

Equations (1) and (2) bound new vertices reached through an old intermediate
by 2+e−r. Direct new neighbors contribute at most 1+r. Finally, a graph H
with m edges can add at most m new labels outside B_x via an edge from B_x.
Thus x reaches at most

    (2+e−r)+(1+r)+m =3+e+m=7

new vertices in two steps, fewer than nine. This case is impossible.

It follows that **every isolated new vertex has exactly the same old
neighborhood**:

    S_z={c}∪N_Q(c).                                (3)

### 3.2 t≥8: too many isolated labels on the seven old leaves

Here m≤3, so H has at least 9−2m≥3 isolated vertices. By (3), every one of
the seven old neighbors l_i of c must attach to every isolated new vertex.
Its port size is 2+d_R(l_i), so it must have d_R(l_i)≥1. Therefore

    sum_{i=1}^7 d_R(l_i) ≥7.

The set N_Q(c) is independent, so each edge of R has at most one endpoint
in it. The same sum is at most e≤4, contradiction.

### 3.3 t=7: the missing new neighbor of c cannot be repaired

Now R is empty. Select any isolated new vertex z. Equation (3) forces all
seven old leaves to have two-element ports of the form {z,a_i}.
The center c has eight new neighbors and misses exactly one new vertex y;
y≠z because c∈S_z.

With only four edges, the H-component containing y has at most five vertices.
Thus at least four of the other eight new vertices have no H path of length
at most two from y. Their pairs with y need a common old neighbor.

The old center c is not adjacent to y, and the remaining 42 ordinary old
vertices have singleton ports, so only the seven old leaves can supply such
common neighbors. A port {z,a_i} contains y only when a_i=y, and then covers
only the pair {y,z}. It cannot cover the at-least-four distinct required
pairs. This final contradiction proves the uniform theorem for 7≤t≤11.

## 4. Exact auxiliary catalog for the remaining degree-at-most-six case

The uniform theorem removes all degree-seven deleted graphs. To state the
remainder concretely, every nontrivial component of an H with at most four
edges has at most five vertices. The existing NetworkX graph atlas supplies
all such connected components. Enumerating their multisets with the required
edge sum, then adding isolates, gives exactly 20 auxiliary graphs up to
isomorphism across m=4,3,2,1,0.

For any remaining deleted graph with maximum degree d≤6, choose a degree-d
vertex and remove it. Triangle-freeness gives

    W(D)=sum_x binom(r_x,2)
       ≤ binom(d,2)+binom(t−d,2)+(t−d).

Also W(D)≤t(d−1). These are necessary upper bounds, not claims that the
corresponding degree patterns can be realized inside Q. If b(H) is the
exact number of new pairs without an H path of length at most two, then

    b(H)≤2t+W(D).                                  (4)

The complete catalog evaluates these bounds as follows:

| t | H edges | All auxiliary types | Types surviving (4) after r_x≤6 | W upper bound used |
| ---: | ---: | ---: | ---: | ---: |
| 7 | 4 | 11 | 8 | 16 |
| 8 | 3 | 5 | 5 | 18 |
| 9 | 2 | 2 | 2 | 21 |
| 10 | 1 | 1 | 1 | 27 |
| 11 | 0 | 1 | 1 | 33 |

At t=7 the three removed auxiliary types are K3+K2 plus four isolates,
P3+2K2 plus two isolates, and 4K2 plus one isolate. The eight remaining
four-edge types are:

- K1,4, the five-vertex fork, or P5, each plus four isolates;
- C4 or a triangle with a pendant vertex, each plus five isolates;
- K1,3+K2, P4+K2, or 2P3, each plus three isolates.

For t=8, the five types are K1,3, P4, K3, P3+K2, and 3K2, each padded to
nine vertices by isolates. For t=9 they are P3 or 2K2 with isolates. For t=10
there is one edge and seven isolates; for t=11 H is empty.

[hs59_sparse_auxiliary_catalog.py](../../../computations/dd82/construction/hs59_sparse_auxiliary_catalog.py)
and its [JSON result](../../../computations/dd82/construction/hs59_sparse_auxiliary_catalog.json)
preserve every representative edge list, every bad new pair, all isolate
counts, and the degree bounds. The complete catalog used **0.041209 CPU
seconds** and introduced no new dependency. It is a finite auxiliary
classification, not a search over expanded graphs.

## 5. Precise remaining attachment design and stopping point

For each of the 17 surviving auxiliary representatives, an actual completion
still requires the following objects simultaneously:

1. An embedding of a t-edge deleted graph D in Q with r_x≤6.
2. Port sets B_x of size 1+r_x, with each new label a occurring exactly
   8−d_H(a) times.
3. For every isolated a, its eight-set S_a must dominate Q−D. These sets
   must pairwise intersect.
4. Every old pair losing all retained paths of length at most two must have
   intersecting port sets. This includes each deleted edge and each old
   path broken by a deletion.
5. For each old vertex x, the exact union

       B_x ∪ (union_{y∈N_{Q−D}(x)} B_y) ∪ N_H(B_x)

   must contain all nine new labels. Every bad pair of H must occur together
   in some B_x.

These conditions concern the same D and B. In particular a numerical degree
profile or a new–new pair cover is not an expanded graph. A useful immediate
local consequence of condition 5 is

    sum_{y∈N_{Q−D}(x)} r_y + |N_H(B_x)\B_x| ≥1,

because the direct and old-intermediate slots otherwise total at most eight.
When H is empty (t=11), the deleted-edge endpoints must therefore form a
**total dominating set** in Q−D: every old vertex, including each endpoint,
needs a retained old neighbor with positive deleted degree. This restriction
rules out naive separated-star degree profiles that pass the new–new budget.

No common realization of the surviving conditions has been constructed,
and no contradiction covering all r_x≤6 has been established here. The
budget calculations stop at this exact residual design. There was no
credible complete candidate to justify a new SAT or seed run within this
bounded task; no unstructured solver was launched.

The proven new scope is the entire deleted-degree-seven subfamily for every
7≤t≤11, plus the three auxiliary exclusions at t=7 obtained from that theorem
and (4). It is **not** an exclusion of the whole deletion-only HS59 family,
and it does not change the global DD82 interval or Lean status.

## External discussion C7

Root read the complete proof and C7 read this actual file, accepting the
domination lemma, degree-seven exclusion and precise open remainder. Raw
response: `reviews/dd82/20261011_C7_hs59_degree7_rigidity.json`. The existing
Antigravity thread retained requested/CLI-selected gemini-3.8-flash-high/high.
No solver execution or independent backend attestation is claimed.
