import Aris4Math.ThirtyThree.DoubleLockProfiles
import Aris4Math.ProfileApplication

/-! Actual thirty-three-edge, twenty-two-vertex (6,6) and (6,7) branches.
Both locks are corrected, and actual edge multiplicities realize the new data.
The (7,7) branch is not asserted by this module. -/

namespace Aris4Math.ThirtyThree.TwentyTwo

open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.LinkWeightCertificates Aris4Math.LinkDeletion

def profile66 : Numeric.Profile :=
  ThirtyThree.DoubleLockProfiles.twoProfile 22 6 6 [11,12]

def profile67 : Numeric.Profile :=
  ThirtyThree.DoubleLockProfiles.twoProfile 22 6 7 [11,12]

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem profile66_valid : Numeric.validProfile profile66 33 := by
  unfold Numeric.validProfile
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem profile67_valid : Numeric.validProfile profile67 33 := by
  unfold Numeric.validProfile
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem profile66_value : Numeric.totalBound profile66 = (4155/4199 : ℚ) := by
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem profile67_value : Numeric.totalBound profile67 = (441/442 : ℚ) := by
  decide +kernel

theorem profile66_weight_left : IncidentWeightBound profile66 11 (3/323) := by decide +kernel
theorem profile66_weight_right : IncidentWeightBound profile66 12 (3/323) := by decide +kernel
theorem profile67_weight_left : IncidentWeightBound profile67 11 (3/323) := by decide +kernel
theorem profile67_weight_right : IncidentWeightBound profile67 12 (3/323) := by decide +kernel

/-- The (6,6), codegree-one pair yields a coloring of the actual 33-edge H. -/
theorem six_six_propertyB (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 6) (dy : H.degree y = 6) : PropertyB H := by
  have valid : Numeric.validProfile
      (ThirtyThree.DoubleLockProfiles.twoProfile 22 (H.degree x) (H.degree y) [11,12]) 33 := by
    rw [dx,dy]
    exact profile66_valid
  have real : RealizesProfile H (twoVertices x y hne) (twoPositions 22 (by decide)) profile66 33 := by
    have h := ThirtyThree.DoubleLockProfiles.realizes_two_profile H edges33
      (by decide) x y hne codegree1 [11,12] valid
    simpa only [dx,dy] using h
  apply ProfileApplication.propertyB_of_corrected_profile H
    (twoVertices x y hne) (twoPositions 22 (by decide)) profile66 real rfl
  · intro j _
    fin_cases j
    · apply realized_center_deduction H cover (twoVertices x y hne)
        (twoPositions 22 (by decide)) profile66 real 0 11 1 (3/323) rfl
      · change 1 ≤ (4 * H.degree x - (22-1) + 2) / 3
        simp [dx]
      · norm_num
      · exact profile66_weight_left
      · decide +kernel
    · apply realized_center_deduction H cover (twoVertices x y hne)
        (twoPositions 22 (by decide)) profile66 real 1 12 1 (3/323) rfl
      · change 1 ≤ (4 * H.degree y - (22-1) + 2) / 3
        simp [dy]
      · norm_num
      · exact profile66_weight_right
      · decide +kernel
  · rw [profile66_value]
    norm_num

/-- The (6,7), codegree-one pair yields a coloring after both true link losses. -/
theorem six_seven_propertyB (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 6) (dy : H.degree y = 7) : PropertyB H := by
  have valid : Numeric.validProfile
      (ThirtyThree.DoubleLockProfiles.twoProfile 22 (H.degree x) (H.degree y) [11,12]) 33 := by
    rw [dx,dy]
    exact profile67_valid
  have real : RealizesProfile H (twoVertices x y hne) (twoPositions 22 (by decide)) profile67 33 := by
    have h := ThirtyThree.DoubleLockProfiles.realizes_two_profile H edges33
      (by decide) x y hne codegree1 [11,12] valid
    simpa only [dx,dy] using h
  apply ProfileApplication.propertyB_of_corrected_profile H
    (twoVertices x y hne) (twoPositions 22 (by decide)) profile67 real rfl
  · intro j _
    fin_cases j
    · apply realized_center_deduction H cover (twoVertices x y hne)
        (twoPositions 22 (by decide)) profile67 real 0 11 1 (3/323) rfl
      · change 1 ≤ (4 * H.degree x - (22-1) + 2) / 3
        simp [dx]
      · norm_num
      · exact profile67_weight_left
      · decide +kernel
    · apply realized_center_deduction H cover (twoVertices x y hne)
        (twoPositions 22 (by decide)) profile67 real 1 12 3 (3/323) rfl
      · change 3 ≤ (4 * H.degree y - (22-1) + 2) / 3
        simp [dy]
      · norm_num
      · exact profile67_weight_right
      · decide +kernel
  · rw [profile67_value]
    norm_num

end Aris4Math.ThirtyThree.TwentyTwo

#print axioms Aris4Math.ThirtyThree.TwentyTwo.six_six_propertyB
#print axioms Aris4Math.ThirtyThree.TwentyTwo.six_seven_propertyB
