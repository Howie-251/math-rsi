import Aris4Math.General.RS.ProbabilityBound
import Aris4Math.General.RS.SampleLaw
import Aris4Math.General.RS.PilotEstimates

/-! The original arbitrary-finite-vertex 17-uniform pilot, through the same actual
RS probability criterion proved in `ProbabilityBound`. -/
namespace Aris4Math.General.RS

universe u

/-- Every finite simple 17-uniform hypergraph with at most `2^17` edges has
Property B. This is the original target with no extra internal premise. -/
theorem propertyB_seventeen_of_at_most_two_pow : PilotTarget.{u} := by
  intro V _ E hu hm
  apply propertyB_of_rs_bound E 17 (by norm_num) hu
    (by norm_num : (0 : ℝ) < 1/17) (by norm_num : (1/17 : ℝ) ≤ 1)
  simpa using pilot_estimate_actual E hm

end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.propertyB_seventeen_of_at_most_two_pow
