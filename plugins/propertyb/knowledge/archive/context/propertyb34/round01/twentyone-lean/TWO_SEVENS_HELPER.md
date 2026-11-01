# Actual degree-six branch with exactly two degree-seven vertices

The source is `formal/Aris4Math/ThirtyFour/TwentyOneSixTwoSevens.lean`.
Its main declaration is
`Aris4Math.ThirtyFour.TwentyOneSixTwoSevens.propertyB_of_two_sevens`.

The inputs are an actual pair-covering `Simple5Hypergraph (Fin 21)` with 34
edges, distinct vertices `x,y,z` of degrees 6,7,7, and degree at least eight
for every other vertex. The conclusion is `PropertyB H`. No local profile,
probability certificate, or non-Property-B premise is exposed by this theorem.

The actual triple classifier leaves alternatives A and B. In B, any actual
eight-degree unit neighbor of `x` contradicts the `6778` quadruple classifier.
In A, let `L` be the degree-eight set. The actual degree sum gives `|L| ≥ 12`.
Remove `x`'s at most four bad partners, leaving at least eight points. The
actual pair `yz` has exactly two common edges; each contains at most three
members of `L`, since its two displayed seven-degree vertices are outside
`L`. Removing every `L`-point in those two edges therefore leaves at least
two points, directly supplying the final two eight-degree locks.

Both selected points are unit to `x`. Uniqueness of the `xy`- and `xz`-edges
and exclusion of every `yz`-edge give all required common-triple zeros.
The actual `6778` classifier forces both points to be unit to `y,z` as well.
The `688` triple bound gives their remaining pair codegree one or two. The
resulting actual five-vertex embedding meets every hypothesis of
`TwentyOneSixFive67788Local.propertyB_of_five`, concluding Property B.

The unique main Lean executor built the module successfully in
`build-queue-TwentyOneSixTwoSevens-r7.log`. Its exported theorem's
`#print axioms` output contains only `propext`, `Classical.choice`, and
`Quot.sound`. The helper author inspected the saved output and did not launch
a separate Lean process. The initial build encountered tactic elaboration
timeout; the final source uses focused simplification of the five actual
vertices and their relations. The theorem and mathematical route are
unchanged. This is an incremental local build, not independent-machine
reproduction or acceptance of the complete T34 theorem.
