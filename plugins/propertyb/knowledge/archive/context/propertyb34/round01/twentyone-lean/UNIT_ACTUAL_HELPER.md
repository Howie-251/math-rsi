# Actual-input bridge for the degree-six unit-neighbor set

Source: `formal/Aris4Math/ThirtyFour/TwentyOneSixUnitActual.lean`.
Namespace: `Aris4Math.ThirtyFour.TwentyOneSixUnitActual`.

`unit_set_structure_of_not_propertyB` takes an actual
`H : Simple5Hypergraph (Fin 21)`, pair covering, exactly 34 edges,
`¬ PropertyB H`, a degree-six vertex `x`, and a set `U` of at least seven
degree-eight vertices with `H.codegree x u = 1` for each `u ∈ U`. It concludes
that each distinct pair in `U` has codegree two and that every actual edge
through `x` contains at most two members of `U`.

The theorem derives all local classification premises internally. Its
`noB` premise is the intended structural context; the final Property B
dispatcher must discharge the contradiction.

For any distinct `a,b,c ∈ U`, their degrees make them distinct from `x`.
`TwentyOneSixStructure.unit_eight_pair` bounds all three tail pair codegrees
by two, while pair covering bounds them below by one. Subtracting one gives
three actual `Fin 2` inputs. The four-vertex embedding then has exactly the
degree and codegree data required by `TwentyOneSixQuadCoverage.actual6888`.
Its conclusion gives actual quadruple multiplicity zero, and either all tail
codegrees two or tail sum four with all high trace multiplicities zero.

In the latter case, `QuadIncidence.triple_count` gives the common-triple zero
required by `TwentyOneSixUnitSet.TripleResidue`. Any actual edge containing
`x,a,b,c` would give positive quadruple multiplicity by
`TwentyOneFiveLocal.common_quad`, a contradiction. These two conclusions are
exported by `residual_on_three`; the set theorem passes them directly to the
already checked `TwentyOneSixUnitSet.unit_set_structure`.

The unique main Lean executor completed the first serialized regular build:
`build-queue-TwentyOneSixUnitActual-r1.log` reports success (1070 jobs). Both
exports' `#print axioms` output contains only `propext`, `Classical.choice`, and
`Quot.sound`. The helper author inspected the saved output and did not launch
another Lean process. This is an incremental local build, not an
independent-machine reproduction. The module contains no `sorry`, new axioms,
or `native_decide`. This does not finish all degree-six cases, the complete
21-point branch, or T34.
