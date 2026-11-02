# Prediction before targeted test: one-copy saturation forbids arbitrary helper batches

2026-11-01 11:02 UTC. This is a new, falsifiable local extension claim, not an accepted new graph or a global degree/diameter bound. The q8 filled sources now have actual mathematical acceptance. Full-product one-copy extensions themselves have not been produced in this experiment.

## Declared fixed scope

Let H be one accepted filled source of degree delta, with full ovoid O and spread, R=st+1. Set C=O times spread, |C|=R^2, and D its R diagonal centers. Every two distinct centers have disjoint open neighborhoods. The induced graph on C is a perfect matching T on C minus D, while D is isolated in C and has no length-2 path to a different center.

Form G by adjoining exactly one immutable full-neighborhood clone x_c for every c in C. Keep all original edges and clone pins. Set the cap Delta=delta+1. All old vertices outside D are saturated. Available existing pins for a new helper batch are therefore only D and the clones, and each can receive at most one further edge. Allow an arbitrary finite batch B of new vertices and arbitrary edges inside B, but no edge deletions or other changes between existing vertices.

## Specific prediction

For |B| at least 2, any such extension with diameter at most 3 must satisfy

    M := |C minus D| = R(R-1) <= max_t t(Delta+2-t)
                                     = floor((Delta+2)^2/4).

For |B|=1, the already accepted single-helper bound requires at least R^2 pins. Thus no nonempty helper batch can extend either q8 one-copy saturated graph at the same cap:

- balanced: R=65, delta=81, Delta=82, M=4160 >1764;
- Payne: R=64, delta=80, Delta=81, M=4032 >1722.

This is strictly stronger than the previous single-helper exclusion and does not assume the new helpers are independent.

## Reasoning to attack independently

Write A_h for off-diagonal clone classes directly pinned to helper h. Each class has only one clone with one spare degree, so ownership is unique if used.

For c in C minus D, a length-at-most-3 route from a new helper h to c can only arise from:
1. h directly pins x_c, giving h-x_c-u-c for a source neighbor u;
2. h or a neighboring helper pins x_T(c), since x_T(c) is adjacent to c.

A D pin cannot reach c in the remaining two steps. No helper can directly pin c because c is saturated. No two distinct center neighborhoods intersect. Paths involving two internal helpers cannot end at saturated c.

If x_c is unused, covering T(c) would force every helper to pin x_T(c) itself, impossible for at least two helpers. Hence all M off-diagonal classes are used.

If h owns c, every other helper except possibly the owner of T(c) must be adjacent to h in B. Therefore every h with |A_h|>0 has internal degree at least |B|-2 and

    |A_h| <= Delta-|B|+2.

Summing over at most |B| owners gives M<=|B|(Delta+2-|B|). If |B|>Delta+2 there can be no active owner, also impossible.

The bound can be attained for this center-route coverage condition alone when an even number t of helper groups is paired, each group has a clone pins, and the internal helper graph is K_t minus the group-pair perfect matching. Then Delta=a+t-2 and M=ta. This does NOT claim full-source all-pairs coverage for such a toy example.

## Targeted test and next decision

Independent agent should attack the exact route classification, unused-class argument, and unique-ownership assumption; use the already accepted incidence/owner matrices only if needed, without repeating field/geometry/BFS of the old sources. One small exhaustive or direct witness calculation may verify the sharp center-route boundary, with <=15 CPU seconds and no giant clone graph or solver queue.

If supported, close only this immutable one-copy, same-cap arbitrary batch scope. Do not close k>=2, a different code, a batch introduced before full saturation, changes to old edges, or a higher degree cap. Next generation must keep some ordinary source pins free, change the clone rule, or choose a new cap; do not launch same-cap joint-helper search.

