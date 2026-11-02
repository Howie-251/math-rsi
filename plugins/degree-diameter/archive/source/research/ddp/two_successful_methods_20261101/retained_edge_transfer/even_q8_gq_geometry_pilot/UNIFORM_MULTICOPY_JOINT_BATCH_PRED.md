# Pre-test prediction: the joint-batch quadratic barrier does not need unique ownership

2026-11-01. Same active Goal, same A mechanism. This is a new proposed generalization of the accepted one-copy barrier, not a new graph or published-novel theorem claim. No k2 graph or parameter ladder is generated.

## Fixed scope and predicted conclusion

Let H be the accepted delta-regular filled source with full center code C=O times spread, R=st+1. Its open center neighborhoods are disjoint with union H minus D. On C_off=C minus D, adjacency is the perfect matching T; D has no distance<=2 route to C_off.

Adjoin exactly k full-source-neighborhood clones of EVERY center, k>=1. Set the unchanged cap Delta=delta+k, so every original source vertex outside D is saturated. Keep all existing adjacencies fixed. Only attach a finite nonempty batch B of new vertices to existing free vertices and to one another.

Prediction: for ANY k>=1 and ANY nonempty finite B, diameter<=3 still requires

    M=R(R-1) <= floor((Delta+2)^2/4).

It is not necessary to assume each clone or clone class has only one new-helper owner. Hence both fixed q8 families exclude all such further batches for a larger range:
balanced R65/delta81: k1..45 (Delta<=126), since4160>4096 at126;
Payne R64/delta80: k1..44 (Delta<=124), since4032>3969 at124.
At next degrees127/125 the quadratic bound only ceases to exclude; no existence is claimed.

## Reasoning to attack

Let S_c subset B be helpers adjacent to at least one existing clone whose base center is c. Collapse multiple clone pins at the same helper to one class membership; this only reduces its counted pin load. Let a_h be the number of off-diagonal classes owned in this sense by h, and d_h its internal degree in B. Always a_h+d_h<=Delta, regardless of k, clone multiplicity or available clone spare degrees.

The same exact route classification to a saturated old c in C_off is

    every h in B lies in S_c union N_B[S_T(c)].

Only a directly pinned clone of class c gives the shared-source-neighbor3route, and an own/neighbor helper pin to classT(c) gives the2/3route. D cannot reach c in two old steps; old non-D is saturated. Existing clones have no mutual edges. Extra helpers in the interior cannot end at c, because c is saturated. This argument is independent of k and does not need S_c singleton.

For t=|B|,

    t <= |S_c|+|S_T(c)|+sum_{h in S_T(c)} d_h.

Sum over all M off-diagonal classes. Matching T is a permutation, giving

    M*t <= sum_h a_h*(d_h+2)
         <= sum_h (Delta-d_h)*(d_h+2)
         <= t*floor((Delta+2)^2/4).

The last step is the integer quadratic max over0<=d_h<=Delta. Division by positive t proves the prediction. This even covers t1, though the earlier single-helper R^2 bound can be stronger for that case.

Potential failure modes to inspect are an uncounted route through existing clones, use of an unsaturated old non-D pin, or a missing owner multiplicity cost. Do not treat the conclusion as established before the independent attack.

## Targeted check and resulting decision

An independent finite check may enumerate small arbitrary owner SUBSETS (including empty/multiple owners), arbitrary internal helper graphs, and the exact center-route condition. The earlier singleton-owner toy is not to be rerun. Budget<=15CPU total, no old field/projection/largegraphBFS/Lean or clone production.

If supported, inherit the old route classification and replace only the global count argument; close the stated uniform-k saturated fixed-adjacency batch scope through the listed caps. Do NOT exclude nonuniform copies leaving source pins free, joint generation before saturation, changes between existing vertices, higher cap, a different code, arbitrary degree/diameter graphs, or k beyond the numerical quadratic obstruction.

