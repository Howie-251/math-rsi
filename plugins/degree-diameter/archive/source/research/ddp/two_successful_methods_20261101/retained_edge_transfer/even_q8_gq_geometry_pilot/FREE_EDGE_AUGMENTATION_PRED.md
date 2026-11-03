# Pre-test prediction: spare-to-spare edges still do not repair the saturated family

2026-11-01. New scope following the independently supported uniform-k fixed-adjacency bound. This permits additional edges BETWEEN existing free vertices, so it is not covered by that theorem. No new q8 graph or copybatch is generated.

## Predicted abstract statement

Use the same delta-regular host H and center code C: disjoint openN, union H minus D, D subset C isolated in C, C_off=C minus D a perfect matching T. Form the uniform-k clone graph, k>=1, with k mandatory full original-source N(c) clones per center, cap Delta=delta+k.

Keep ALL mandatory source and fullN clone edges. Permit arbitrary further edges among existing vertices AND to/between a finite nonempty new helper set B, subject to cap Delta. Old non-D source vertices are saturated, so every extra edge to an existing vertex must meet the free set F=D plus existing clones. Each f in F has delta mandatory old neighbors and at most k extra edges.

Prediction: any such edge-preserving augmentation of diameter<=3 necessarily satisfies

    M=|C_off| <= floor((Delta+k+1)^2/4)
              = floor((delta+2k+1)^2/4).

For balanced q8, M4160/delta81, this excludes k1..23 (cap<=104); first unexcluded k24 gives4225.
For Payne q8, M4032/delta80, it excludes k1..22 (cap<=102); first unexcluded k23 gives4032.
At k1 it recovers the old quadratic threshold and proves the accepted degree82 graph cannot gain ANY additional vertices while preserving all its edges at the same degree cap, EVEN if arbitrary edges among its free existing vertices are also added. This is not global N82 optimality.

## Counting argument to attack

For helper h let p_h=number of neighbors in F and d_h=internal B-degree, so p_h+d_h<=Delta.

A helper-to-old-C_off route of length<=3 has:
- First step to p in F. If p is a clone, its mandatory source routes reach at most its base center and its unique matching-mate center; if p lies in D, they reach none of C_off. The h-p edge uses one of p's k extra slots. Each remaining extra edge can provide at most one new C_off target in the remaining step, since only an existing clone can be directly adjacent to such an old saturated center, and it has exactly one possible C_off source neighbor. Hence this first pin covers at most 2+(k-1)=k+1 targets.
- First step to another helper g. In the remaining two steps, each F-neighbor of g reaches at most one C_off target, by that same old-saturation argument; another helper cannot be adjacent to a saturated C_off center. This contributes at most p_g.

Thus every h reaching all M targets requires

    M <= (k+1)*p_h + sum_{g neighbor_B h} p_g.

Summing over t=|B|>0,

    Mt <= sum_h p_h*(k+1+d_h)
       <= sum_h (Delta-d_h)*(k+1+d_h)
       <= t*floor((Delta+k+1)^2/4).

The last quadratic has vertex d=(Delta-k-1)/2=(delta-1)/2. D pins/diagonal clones and repeated target coverage only decrease usefulness.

Check carefully whether a hidden extra edge to a saturated old center, a two-helper path, or a spare-edge chain evades this count. We must not assume the first F-neighbor has no peer edges for k>=2.

## Targeted validation and decision

An independent paper attack plus one tiny degree-legal toy can suffice: k2 helper h pinned to clone_a which has a peer edge to clone_b gives a new3route to T(b), demonstrating why the previous fixed-adjacency proof cannot simply be reused. At k1 that same two-extra-edge pin would violate cap. Optional exhaustive small aux graphs with one active clone per class and inactive copies may test the path count; <=5CPU total, no oldfield/projection/q8BFS/largegraphs/Lean/solver.

If supported, stop attempts that merely add spare-edge links after uniform saturation throughout the listed ranges. Do not exclude nonuniform clones, removing/modifying mandatory oldedges, joint generation that avoids mandatory fullN saturation, a different code/source, or higher caps. No extra graph/Lean/public novelty count or claim of existing C-review coverage.

