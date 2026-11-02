# Independent paper attack: complete helper cliques cannot work at cap31

2026-11-01. **The new free-target prediction is supported for the fixed
q2×q8 source and complete uniform r4 copying, with every mandatory edge
retained, arbitrary additional F–F edges, and all new helpers inducing a
nonempty clique.** The strongest possible bound reaches1620 of the1625
free targets. This excludes every helper-clique size at cap31, including
concentrated-row pin assignments. It does not exclude arbitrary nonclique
helper graphs or change the source/copy assumptions.

The prediction was saved first in `CLIQUE_HELPER_FREE_TARGET_PREDICTION.md`.
This check is a paper route classification plus one tiny integer t0..32
calculation, under a2 CPU-second limit. No8775 source, free graph, field,
geometry, BFS, solver, Lean, paid review, old toy or factor-subset enumeration
was constructed or run. The existing230-point calibration is only compared
algebraically, without rerunning it.

## The source assumptions needed here

As established for this specific abstract published interface in
`INDEPENDENT_NOTE.md`, C has325 independent centers, every center has26
mandatory old neighbors, and their neighborhoods partition U of size8450.
Every U vertex has old degree27. After adding r full original-neighborhood
clones per center, U has degree Delta=27+r and is saturated. The free set F
has r+1 representatives per based class and therefore(r+1)325 vertices.
Every free representative has the same26 mandatory U neighbors as its base,
and at most r+1 additional slots. Initially F has no internal edges.

Thus any U–F edge in the final graph is mandatory. In particular a mandatory
two-edge F–U–F walk can end only in the same based class: different classes
have disjoint U neighborhoods. Every such class has exactly r+1 free
representatives, including its original center. These facts apply equally
to centers and all repeated clones. Self-loops were already removed from
the source; the augmentation is a finite simple graph.

The earlier
`../even_q8_gq_geometry_pilot/INDEPENDENT_FREE_EDGE_AUGMENTATION_NOTE.md` was
read as a warning about free-peer routes. Its regular-host/off-center
perfect-matching hypotheses and saturated off-center target set do not hold
here: C is independent and remains free. That older theorem is not being
instantiated or counted again. The proof below targets all F and uses the
new clique assumption.

## Exhaustive classification of short helper-to-free walks

Let all new helpers form K_t, t≥1. For each h let P_h=N(h) intersect F,
p_h=|P_h|, and P=union_g P_g, a set of distinct free vertices. Write Q for
the graph of added edges inside F and N_Q for its open-neighbor operation.
Every helper has t−1 helper neighbors and cannot meet saturated U, so

    p_h <= Delta+1-t.

In particular t≤Delta+1; at cap31 the only possible sizes are1..32.

For a fixed helper h, every free target reachable in at most3 steps lies in

    P union N_Q(P) union N_Q^2(P_h) union classes(P_h).       (1)

Here classes(P_h) means all free representatives of the based classes of
h's own pins. To check(1), enumerate by the first step:

* First step to another helper g: only two edges remain. The endpoint is
  in P (including a further helper step before its pin) or in N_Q(P) (a
  pin followed by one F-peer edge). A step into U is forbidden. A mandatory
  F–U edge cannot end in F within the remaining length.
* First step to f in P_h: one or two F-peer edges end in N_Q(P) or
  N_Q^2(P_h); going through a helper and then its pin ends in P; a
  mandatory F–U–F suffix ends in classes(P_h). A suffix ending in U is
  irrelevant because the target is F.

Shorter walks and immediate backtracks are included. Routes h–f–g–f' with
shared helper pins end in P. There is no omitted helper–U route or extra
U–F edge. No future helper or fourth step is borrowed.

For a clique, all P is already reachable from h in at most2 steps. The
containment itself is only an upper bound and permits generous overlaps;
it is not claimed to characterize every possible extension.

## Pin multiplicity and incoming-peer degree costs

Every vertex of P is adjacent to at least one helper. That actual edge
consumes one of its at most r+1 extra slots, so its Q degree is at most r.
This remains true when several helpers share a pin; sharing reduces the
available peer degree further. Since P is a set, with duplicates removed,

    |P union N_Q(P)| <= (r+1)|P|.                          (2)

Fix f in P_h. It has at most r Q neighbors g. Even if g is not a helper
pin and has all r+1 slots available for Q, the incoming edge g–f spends one
of them. Thus it has at most r other Q neighbors. Immediate backtracking
f–g–f ends in f, already counted in P. Consequently the two-peer term
adds at most r² new endpoints per actual pin, or r²p_h in total. If g also
lies in P or has several helper neighbors this bound only decreases. The
incoming edge cannot be disregarded, but has been explicitly charged at g.

Each pin f's based class contains r+1 representatives and already contains
f in P. Therefore classes(P_h) adds at most rp_h further vertices. Several
pins of one class only produce more overlap; counting r for each remains
a safe upper bound. Combining these observations with(1) and(2) gives

    |B_3(h) intersect F|
      <= (r+1)|P| + r²p_h + rp_h
       = (r+1)(|P|+r p_h).                               (3)

This counts every peer edge's cost at both the first pin and the
intermediate peer. Further global endpoint-slot constraints and overlap
could make the bound smaller; ignoring those extra restrictions cannot
invalidate its necessity. No unique helper owner is assumed.

## The clique-degree bound and the strict five-vertex deficit

Put q=Delta+1-t. Then p_h≤q and
|P|≤sum_g p_g≤tq, regardless of repeated pins. Equation(3) yields

    |B_3(h) intersect F| <= (r+1)(t+r)(Delta+1-t).

Diameter at most3 requires all(r+1)325 F vertices to be reached by every
helper. Since r+1>0 and Delta=27+r, it is necessary that

    325 <= (t+r)(28+r-t).

The exact integer identity is

    (t+r)(28+r-t) = (r+14)^2 - (t-14)^2.

At r4/cap31, the maximum is324 at t14, and the free-vertex coverage bound is
5·324=1620<1625. The sole scalar check inspects t0..32, with t0 marked as a
nonphysical endpoint relaxation, and confirms the same unique maximizer
over allowed t1..32. Sizes greater than32 already violate the helper
clique's degree cap. This closes all nonempty complete helper cliques in
the stated cap31 model.
The one scalar execution exited0 and recorded0.000053 CPU seconds under2;
there were no other experiments.

## Why the successful K5 calibration does not extrapolate

The same counting proof, with base noncenter degree delta0 and mandatory
free degree delta0−1, gives the general necessary condition

    M <= (t+r)(delta0+r+1-t).

For the already actual230-point q2×q2 calibration, delta0=9, M=25 and r0.
It reduces to25≤t(10−t), attained at t5. In that successful case every free
vertex is an actual pin, helper pins partition the25 free vertices and
the clique makes their union accessible in two steps. With r0 there are
no remaining free-peer slots at a pin and no additional representatives
of a class. Thus the free-target count is genuinely tight for the actual
K5 example, without any new experiment here.

The larger product has325 classes and r4, yet its best clique count is324.
Its failure is not merely a failure of balanced-row ownership or of a
particular clique size: the best possible clique/free-slot budget is already
short. The favorable small example calibrates the bound, rather than proving
that all factor products permit the same helper rule.

## Exact terminal scope

This new result excludes complete helper cliques at cap31, with arbitrary
added F–F edges, on the fixed mandatory-edge-preserving uniform-copy source.
Caps27..30 were already excluded for arbitrary helper graphs by the650-target
barrier and are not recorded as new exclusions here. The all-light row
argument is separate and was not needed for this proof.

Nonclique helper graphs, removing or changing mandatory edges, incomplete or
nonuniform copying, different codes or sources remain open. No nonclique
solver, subset enumeration or further construction is started. This is a
paper necessary condition, not a new graph, concrete Lean theorem, global
N(31,3) bound, novelty claim or inherited A/B/C verdict. Root counts, Wiki
and frozen artifacts were not modified. RESULT/TERMINAL record completion.
