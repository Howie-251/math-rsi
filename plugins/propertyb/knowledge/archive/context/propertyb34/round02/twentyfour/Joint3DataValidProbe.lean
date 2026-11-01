import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3Data
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3Numeric
open scoped BigOperators
open TwentyThreeFiveLowStrictJoint3Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option synthInstance.maxSize 2000
theorem data_valid :
    (∀ T, 0<μ T → T ∈ support) ∧
    (∀ l, Numeric.validProfile (p l) 34) ∧
    (∀ l, (p l).emptyPairCap=none) ∧
    (∀ l j, (positions l j).val+1 ∈ (p l).correctionCenters) ∧
    (∀ l, 0 ≤ gamma l) ∧ (∑ l, gamma l)=1 ∧
    (∀ l j, 0 ≤ beta l j) ∧ (∀ l j, beta l j ≤ gamma l) ∧
    (∀ j q, 0 ≤ delta j q) ∧ (∀ j q, j ∉ R j q) ∧
    (∀ j q, quota j q ≤ (4*available support μ j (R j q)+2-(23-1-(R j q).card))/3) := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3Numeric
