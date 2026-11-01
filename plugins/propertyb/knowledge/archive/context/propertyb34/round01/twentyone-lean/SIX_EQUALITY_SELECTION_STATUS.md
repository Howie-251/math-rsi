# Degree-six equality selection

Source: `formal/Aris4Math/ThirtyFour/TwentyOneSixEquality.lean`.

The written API `TwentyOneSixEquality.select_equality_locks` takes an actual
21-point pair-covering hypergraph with 34 edges, a degree-six point x, all other
degrees at least eight, and the locally classified unit-neighbor set U. The
caller supplies that U consists exactly of degree-eight unit neighbors of x,
that every distinct U-pair has codegree two, and that each edge through x has at
most two U-points. It returns three degree-eight locks u, v, b and an actual edge
through x,u,v,b, with x-b codegree two and u-b/v-b codegrees at most two.

The source derives the degree-eight count at least sixteen, U cardinality
twelve, exceptional degree-eight set cardinality four, exact saturation of all
six edge capacities, and all needed codegree bounds. In particular the outside
codegree bound uses eleven units of the degree-eight vertex's twelve-unit
codegree-excess budget.

The designated sole builder `/root/t34_19_lean` ran the first module build;
`build-six-Equality-r2.log` records one rejected reverse-definition simp argument
in `two_on_every_edge`. The source now uses the explicit edge-count equality
`countX` instead. The builder's
`build-queue-TwentyOneSixEquality-r1.log` records successful checking of the
revised module (1007 jobs; this module 1.3 seconds). The builder reports standard
three-axiom accounting. No Lean execution was performed by this worker. No new
global Property B conclusion is claimed by this conditional selection module.
No cross-model review was run by this worker.

## Additional weighted partition source

`formal/Aris4Math/ThirtyFour/WeightedThreePartition.lean` contains the generic
weighted three-class partition needed for the 24-point matching selection.
Its theorem `exists_three_part_defect_one` assumes symmetric natural-number
weights, zero diagonal, and total weight at each vertex at most five. It returns
a map to `Fin 3` whose internal weight at every vertex is at most one. The
weighted potential update balance is proved explicitly, following the previous
unweighted four-class proof. The first build reported only an unavailable
`Mathlib.Tactic.Omega` import. The import is now the existing
`Lean.Elab.Tactic.Omega`; the revised source and included axiom-output checks
are awaiting the sole builder.

## Additional finite graph obstruction

`formal/Aris4Math/ThirtyFour/FiveVertexClusterBound.lean` contains the generic
graph obstruction for the one-low 23-point branch. `card_le_nine` assumes a
symmetric irreflexive relation with no induced P3, no four-clique, and no four
pairwise nonadjacent points. A maximum independent set has size at most three,
its closed neighborhoods cover the whole domain, and each neighborhood is a
clique of size at most three. The proof concludes that the finite vertex domain
has at most nine members. `exists_forbidden_of_ten` gives the positive
contrapositive interface. The source has been sent to the sole builder;
checking is pending. The actual five-point residual classifier and its caller
remain separate obligations; this generic theorem is not the 23-point branch.
