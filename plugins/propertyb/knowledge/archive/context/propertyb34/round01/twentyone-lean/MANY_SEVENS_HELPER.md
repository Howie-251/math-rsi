# Degree-six point with three degree-seven points

Source: `formal/Aris4Math/ThirtyFour/TwentyOneSixManySevens.lean`.

## Actual-hypergraph API

The namespace is `Aris4Math.ThirtyFour.TwentyOneSixManySevens`.

- `propertyB_of_six_three_sevens` takes an actual
  `H : Simple5Hypergraph (Fin 21)`, pair covering, exactly 34 edges, four
  distinct vertices `x,y,z,w`, and degrees `6,7,7,7`. It concludes `PropertyB H`.
- `propertyB_of_many_sevens` takes the same hypergraph, pair covering and size,
  a degree-six vertex, and at least three members of the existing
  `TwentyOneFiveStructure.sevens H`. It selects the actual three vertices and
  applies the first theorem.

Neither export asks the caller for a residual classification, high-trace vector,
probability bound, or non-Property-B premise.

## Proof connection

Assuming no Property B, apply `TwentyOneSixStructure.residual_677` to `xyz`,
`xyw`, and `xzw`. Their shared pair values force one of two alternatives.

1. All three pairs from `x` have codegree one, all three remaining pairs have
   codegree two, and both `xyz` and `xyw` have common-triple count one. Obtain
   actual edges for those two triples. They coincide by
   `H.edge_unique_of_codegree_one`, so the actual quadruple count is positive.
   Its pair inventory bounds it by one; therefore it is exactly one.
2. All three pairs from `x` have codegree two, all three remaining pairs have
   codegree one, and the common-triple counts of `xyz`, `xyw`, and `xzw` are
   zero. `QuadIncidence.triple_count` translates these three actual counts into
   the required exact-trace sum equalities.

For each alternative, construct the actual four-vertex embedding and its six
pair codegrees, then call `TwentyOneSixQuadCoverage.actual6777`. Its residual
conclusion is `False`, discharging the original contradiction.

## Verification state

The unique main Lean executor completed the first serialized regular build:
`build-queue-TwentyOneSixManySevens-r1.log` reports success (1069 jobs). Both
public exports were audited by their `#print axioms` commands and depend only
on `propext`, `Classical.choice`, and `Quot.sound`. The helper author inspected
the saved build and axiom output; the helper author did not run another Lean
process. This is an incremental local build, not an independent-machine
reproduction.

This branch does not finish all degree-six cases, the entire 21-point branch,
or T34. The module contains no `sorry`, new axioms, or `native_decide`.
