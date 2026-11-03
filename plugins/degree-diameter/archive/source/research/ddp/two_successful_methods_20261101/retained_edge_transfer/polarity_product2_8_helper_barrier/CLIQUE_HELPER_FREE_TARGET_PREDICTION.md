# Targeted prediction: the natural clique-helper extension also fails at cap31

2026-11-01, before independent paper attack. The230-point calibration
succeeded with a helper clique. The current325-class q2xq8 source is much
larger. Before trying to imitate that clique rule, test the following
specific obstruction. This is a new target set and a restricted helper
model, not a claim that the general cap31 mechanism is excluded.

In the already supported mandatory-edge-preserving product interface,
let r>=0 be the uniform number of original-neighborhood copies per class.
There are M=325 classes, each with r+1 free representatives, so
|F|=(r+1)M. Each f has mandatory degree26 into saturated U, and at most r+1
extra slots. Mandatory neighborhoods of different classes are disjoint.
Allow arbitrary added F--F edges and a nonempty helper batch whose entire
induced helper graph is a clique K_t, at cap Delta=27+r. No helper can meet U.
Helpers may share pins or use repeated classes. No edge is removed.

For helper h, write P_h=N(h) intersect F, p_h=|P_h|, and P=union_g P_g.
The clique costs t-1 slots, so p_h<=Delta+1-t and
|P|<=sum_g p_g<=t(Delta+1-t).

Predict that every free vertex within distance3 of h is in the union of

* P (all helpers' pins, already accessible in at most2 steps),
* N_F(P) (one added free edge after some helper's pin),
* N_F^2(P_h) (two added free edges after h's own pin),
* free representatives of h's own pin classes (a mandatory suffix through U).

These exhaust walks of length<=3: helper--U is forbidden; a mandatory
F--U--F suffix ends in the same base class; a U--F edge is mandatory.
First stepping to another helper leaves only two steps. Multiple helper
steps cannot reach a new free target beyond P.

Every vertex in P spends at least one extra slot on a helper, leaving at
most r F-peer edges. Hence |P union N_F(P)|<=(r+1)|P|. For each f in P_h,
at most r first F peers each have at most r further F peers after excluding
the incoming edge. Immediate backtracking ends in P already counted. Thus
at most r^2 p_h additional vertices arise from two F-peer steps. The same
base class has r+1 representatives, with f already in P, so the mandatory
suffix adds at most r p_h further representatives. Repeated pin classes
and overlaps only lower this upper bound. Consequently predict

    |B_3(h) intersect F| <= (r+1)(|P|+r p_h)
                        <= (r+1)(t+r)(Delta+1-t).

Necessary for D<=3:

    325 <= (t+r)(28+r-t) <= (r+14)^2.

At r4/cap31 the largest right side is324 (t14), so the maximum free
coverage is1620<1625, a shortfall of at least5. This excludes ALL clique
helper batch sizes at cap31 in this exact family, even with arbitrary
added free edges. r0..3 were already excluded more generally by the earlier
650-target barrier; do not register those old exclusions as new results.

The earlier free-edge augmentation note concerns saturated off-centers
forming a matching, which this independent325-center product does not have.
Its algebraic bound happens to resemble this one, but its assumptions and
target set do not establish this clique case. The earlier cap31 all-light
argument also does not cover heavy-row clique helpers. This prediction
must be checked separately, especially the exclusion of the incoming edge
and the partition of all short walks with repeated pins and loops removed.

If supported, stop extrapolating the K5 calibration into any K_t cap31
helper batch. A subsequent cap31 rule must change the helper graph away
from a clique, or change one of the fixed mandatory/source assumptions.
Arbitrary nonclique helper graphs, rewiring, nonuniform copying and other
sources remain open. No8775 source, F graph, BFS, field, solver, Lean or
remote review is requested; one independent paper attack and at most one
tiny scalar comparison within2CPU suffice. No portfolio/Lean increment.
