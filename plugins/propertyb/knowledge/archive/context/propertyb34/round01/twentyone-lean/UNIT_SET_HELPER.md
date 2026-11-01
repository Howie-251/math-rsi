# Degree-six unit-neighbor structure: checked helper

Source: `formal/Aris4Math/ThirtyFour/TwentyOneSixUnitSet.lean`.

The unique main Lean executor ran the regular build of
`Aris4Math.ThirtyFour.TwentyOneSixUnitSet`; it passed on its first run (1023
jobs, the new module approximately 1.2 seconds). The saved log is
`build-six-UnitSet-r1.log` in this directory. The helper author inspected that
log and the produced `.olean`; the helper author did not start a separate Lean
process. The main executor will include this module in the downstream type and
transitive-axiom audit.

## Mathematical implication

For the actual `H : Simple5Hypergraph (Fin 21)`, let `H.degree x = 6` and let
`U` have at least seven vertices, each satisfying `H.codegree x u = 1`.
Suppose each distinct pair in `U` has codegree one or two. For every ordered
triple of distinct members `a,b,c`, assume either all three pair codegrees are
two, or their sum is four and `tripleCodegree H x a b = 0`.

If a pair `a,b` had codegree one, every member `p` of `U` would have a unit
neighbor: this is immediate for `p=a,b`; otherwise the residual classification
on `p,a,b` forces exactly one of `pa,pb` to be a unit pair. For any distinct
`p,q`, if `pq` is unit choose a third member of `U`; otherwise choose a unit
neighbor of `p`, which is different from `q`. In either case the resulting
triple is not the all-two case, so `tripleCodegree H x p q = 0`.

Thus every actual edge through `x` contains at most one member of `U`.
The existing actual-incidence theorem `Incidence.codegree_capacity` gives

\[
|U|=\sum_{u\in U}\lambda(x,u)\le d(x)=6,
\]

contradicting `|U| ≥ 7`. Hence every distinct `U`-pair has codegree two.
Separately, if no actual edge contains `x` and three distinct members of `U`,
each actual edge through `x` has `|(U ∩ e)| ≤ 2`.

## Exact API and remaining caller obligation

The namespace is `Aris4Math.ThirtyFour.TwentyOneSixUnitSet`.

- `TripleResidue H x a b c` is exactly the ordered disjunction above.
- `no_unit_pair` proves that every prescribed distinct `a,b ∈ U` has
  `H.codegree a b ≠ 1` from the degree, cardinality, unit-incidence, pair-bound,
  and ordered residual premises.
- `unit_set_structure` adds `noFour`, expressed directly as the nonexistence of
  an actual edge containing `x,a,b,c`, and returns both all-pairs codegree two
  and the actual per-edge capacity two.

The finite-set implication does not need degree-eight membership or `x ∉ U`
as separate assumptions. The caller retains those facts when deriving the
local classification premises.

This is a checked conditional structural lemma, not a proof of the complete
21-point case or T34. The main executor still must obtain the residual and
`noFour` premises from the actual quad6888 classification, apply the helper
inside the actual-hypergraph proof, and finish the downstream branch. There
are no `sorry`, new axioms, or `native_decide` in this module. A source scan is
not a substitute for the pending downstream transitive-axiom audit.
