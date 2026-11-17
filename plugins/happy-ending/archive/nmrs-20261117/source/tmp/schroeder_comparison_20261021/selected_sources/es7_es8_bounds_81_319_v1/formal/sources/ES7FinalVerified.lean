import ES7ClosureExistence
import ES7ClosureData
namespace ES7FinalVerified
open ES8Geometry ES8BalancedGeometry ES7Geometry ES7BalancedEndpoints

/-- Every actual balanced fifty-point configuration has a convex heptagon.
All source clauses and all case coverage are supplied by geometric theorems. -/
theorem balanced50_exclusion : ES7CapacityStage.Balanced50Exclusion := by
  intro c noCap noCup noH
  have noSix := noSix_of_caps_cups c.cup _ noCap noCup
  obtain ⟨d,states,⟨m⟩⟩ := ES7ClosureExistence.exists_frame c noSix noH
  exact ES7ClosureData.impossible m

/-- Maximum cardinality of a planar set avoiding six-caps, six-cups and
convex heptagons is at most forty-nine. -/
theorem balanced49 : ES7Subset.BalancedBound 49 :=
  ES7CapacityStage.balanced_bound_of_50_exclusion balanced50_exclusion

/-- Every set of at least eighty-one planar points in general position
contains seven points in convex position. No emptiness condition is imposed. -/
theorem es7_le_81 (S : Finset Point) (gp : ES7Final.GeneralPosition S) (size : 81≤S.card) :
    HasConvexHeptagon (↑S : Set Point) :=
  ES7CapacityStage.es7_le_81_of_balanced50 balanced50_exclusion S gp size

#print axioms balanced50_exclusion
#print axioms balanced49
#print axioms es7_le_81
#print es7_le_81
end ES7FinalVerified
