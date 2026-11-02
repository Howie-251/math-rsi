# Paper-only check: cap31 needs a concentrated absolute-A row somewhere

2026-11-01. After the230-point calibration was complete, the separate
`CAP31_ROW_CONCENTRATION_PREDICTION.md` was checked on paper only. **Its
uniqueness premise and stated necessary concentration conclusion are
supported under the same genuine GQ-polarity assumptions as the650-target
barrier.** No additional scalar, subset enumeration, source/polarity build,
graph, BFS, field, Lean, solver, web or paid-review run was made for this
refinement. It is not part of the three existing graphs' C scope.

## The stronger uniqueness premise follows from GQ projection

Let beta and b be distinct absolute vertices of the looped B quotient and
write rho for its polarity. They are not adjacent, so the point beta is not
incident with the line rho(b). The generalized-quadrangle projection axiom
gives exactly one incidence path of length3

    beta -- rho(w) -- v -- rho(b).

Polarity reciprocity changes the middle incidence to w incident rho(v), so
this path is exactly a quotient walk

    beta -- w -- v -- b.

Conversely any such quotient3walk supplies that incidence path. Since beta
and b are distinct absolutes with no edge or common neighbor, a3walk between
them has no loop padding or immediate backtrack; those would shorten it to
an impossible walk of length1 or2. Thus the correspondence has no degenerate
extra paths. In particular there is at most one nonabsolute v adjacent to b
within old distance at most2 of beta. The point-line projection supplies
uniqueness here; absolute-code distance3 alone would not imply it.

Each absolute b has eight nonabsolute B neighbors. Their sets are disjoint,
and65·8=520 is the number of nonabsolute B vertices, so each nonabsolute
vertex has exactly one absolute neighbor. This also follows from the
three-entry/nine-entry absolute-neighborhood partition argument already used
in the barrier.

## A light helper must access every missing based class

Use the same free set F, helpers H, r, cap27+r, p_h and d_h as in
`INDEPENDENT_NOTE.md`. Each free representative has a based class(a,b) in
O_A × O_B. Let s_a(h) count distinct b classes owned by actual pins of h in
A-row a; multiple copies of the same class count once.

Fix h such that every row has s_a(h)<8. Consider a based class(a,b) for which
h has no pin. Its eight old saturated targets are

    (a,v), v in N_B(b) minus {b}.

A pin based in a different absolute-A row cannot reach such a target with
an old suffix of length at most2, because distinct A absolutes have no
one- or two-step factor walk. A pin based in row a but class(a,beta),
beta different from b, covers at most one of these eight targets by such a
suffix, by the uniqueness result above. Repeated clones of a class have
identical mandatory suffix coverage. Since s_a(h)<8, at least one target is
not covered by any old suffix from h's own pins.

That target's unique old C neighbor is(a,b). Indeed in the A coordinate an
absolute can be adjacent to a only through a's own loop, and the B coordinate
v has the unique absolute neighbor b. Any free representative adjacent by a
mandatory edge to the target must therefore be based at(a,b).

The exhaustive short-route classification now forces a representative of
class(a,b) either to be an F-peer of one of h's pins, or a pin of a helper
neighbor of h. The former uses h–f–f'–target; the latter uses
h–g–f'–target. Other first-step types either were already excluded by the
chosen uncovered target, or would need a helper edge into a saturated old
vertex. No fourth step is being borrowed.

Let T_h be the union of all based classes accessible through those two
mechanisms. Each actual pin of h has at most r F-peer edges left after its
h edge, and every actual peer is a representative of one class. Therefore

    |T_h| <= r p_h + sum_{g adjacent h} p_g.

All325 classes are either among h's own distinct based classes or in T_h.
Since the number of own classes is at most p_h, every such light helper
necessarily satisfies

    325 <= (r+1)p_h + sum_{g adjacent h} p_g.             (1)

This is a union upper bound; shared peers, repeated owners and both endpoint
degree costs cannot invalidate its necessity.

## The exact conclusion is existential concentration, not impossibility

If **every** helper is light in all five rows, sum(1) over the nonempty
helper batch. Undirected double counting and p_h+d_h≤27+r give

    325 <= max_d (27+r-d)(r+1+d).

The paper identity

    (27+r-d)(r+1+d) = (r+14)^2 - (d-13)^2

shows the maximum is(r+14)^2, attained at integer d=13 within the allowed
cap range. At r4/cap31 this would require325≤324, a contradiction. Thus any
successful cap31 augmentation in this fixed mandatory-edge-preserving
family must have **at least one helper with at least8 distinct based
classes in one absolute-A row**.

It does not follow that every helper must have a heavy row: the summation
used(1) for all helpers only under the global all-light assumption. It also
does not exclude cap31, establish feasibility of concentrated ownership, or
justify a helper solver or an8-subset enumeration. In particular the proposed
all-light(0,4,5,5,5) ownership profile would be ruled out if it were used by
every helper, but no such controller was constructed or evaluated here.

This conclusion supplies a necessary feature for a future concrete joint
rule. The controlled230-point success explains complementarity in another
small literal product; it is not evidence that this650/325-target interface
can be realized. Root counts, Wiki and frozen artifacts are unchanged.
