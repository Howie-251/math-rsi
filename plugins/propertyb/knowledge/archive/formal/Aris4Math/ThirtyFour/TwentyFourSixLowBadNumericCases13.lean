import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_130 : Numeric.validProfile (p 130) 34 ∧ (p 130).emptyPairCap=none ∧
    (∀ j, (positions 130 j).val+1∈(p 130).correctionCenters) ∧
    (∀ j z, 0≤α 130 j z) ∧ (∀ j z, j∉R 130 j z) ∧
    (∀ j z, quota 130 j z ≤
      (4*avoidedCount (p 130) ((positions 130 j).val+1) (avoidedPositions (positions 130) (R 130 j z))+2-
        (24-1-(R 130 j z).card))/3) ∧
    (∀ j, loss 130 j ≤ (∑ z, (quota 130 j z : ℚ)*α 130 j z)-
      penaltySum (p 130) ((positions 130 j).val+1) (fun z => avoidedPositions (positions 130) (R 130 j z)) (α 130 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 130) (k.val+1) true)
      (min (CachedRows.cachedA (p 130) (k.val+1) false) (CachedRows.cachedC (p 130) (k.val+1)-centerLoss (positions 130) (loss 130) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_131 : Numeric.validProfile (p 131) 34 ∧ (p 131).emptyPairCap=none ∧
    (∀ j, (positions 131 j).val+1∈(p 131).correctionCenters) ∧
    (∀ j z, 0≤α 131 j z) ∧ (∀ j z, j∉R 131 j z) ∧
    (∀ j z, quota 131 j z ≤
      (4*avoidedCount (p 131) ((positions 131 j).val+1) (avoidedPositions (positions 131) (R 131 j z))+2-
        (24-1-(R 131 j z).card))/3) ∧
    (∀ j, loss 131 j ≤ (∑ z, (quota 131 j z : ℚ)*α 131 j z)-
      penaltySum (p 131) ((positions 131 j).val+1) (fun z => avoidedPositions (positions 131) (R 131 j z)) (α 131 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 131) (k.val+1) true)
      (min (CachedRows.cachedA (p 131) (k.val+1) false) (CachedRows.cachedC (p 131) (k.val+1)-centerLoss (positions 131) (loss 131) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_132 : Numeric.validProfile (p 132) 34 ∧ (p 132).emptyPairCap=none ∧
    (∀ j, (positions 132 j).val+1∈(p 132).correctionCenters) ∧
    (∀ j z, 0≤α 132 j z) ∧ (∀ j z, j∉R 132 j z) ∧
    (∀ j z, quota 132 j z ≤
      (4*avoidedCount (p 132) ((positions 132 j).val+1) (avoidedPositions (positions 132) (R 132 j z))+2-
        (24-1-(R 132 j z).card))/3) ∧
    (∀ j, loss 132 j ≤ (∑ z, (quota 132 j z : ℚ)*α 132 j z)-
      penaltySum (p 132) ((positions 132 j).val+1) (fun z => avoidedPositions (positions 132) (R 132 j z)) (α 132 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 132) (k.val+1) true)
      (min (CachedRows.cachedA (p 132) (k.val+1) false) (CachedRows.cachedC (p 132) (k.val+1)-centerLoss (positions 132) (loss 132) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_133 : Numeric.validProfile (p 133) 34 ∧ (p 133).emptyPairCap=none ∧
    (∀ j, (positions 133 j).val+1∈(p 133).correctionCenters) ∧
    (∀ j z, 0≤α 133 j z) ∧ (∀ j z, j∉R 133 j z) ∧
    (∀ j z, quota 133 j z ≤
      (4*avoidedCount (p 133) ((positions 133 j).val+1) (avoidedPositions (positions 133) (R 133 j z))+2-
        (24-1-(R 133 j z).card))/3) ∧
    (∀ j, loss 133 j ≤ (∑ z, (quota 133 j z : ℚ)*α 133 j z)-
      penaltySum (p 133) ((positions 133 j).val+1) (fun z => avoidedPositions (positions 133) (R 133 j z)) (α 133 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 133) (k.val+1) true)
      (min (CachedRows.cachedA (p 133) (k.val+1) false) (CachedRows.cachedC (p 133) (k.val+1)-centerLoss (positions 133) (loss 133) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_134 : Numeric.validProfile (p 134) 34 ∧ (p 134).emptyPairCap=none ∧
    (∀ j, (positions 134 j).val+1∈(p 134).correctionCenters) ∧
    (∀ j z, 0≤α 134 j z) ∧ (∀ j z, j∉R 134 j z) ∧
    (∀ j z, quota 134 j z ≤
      (4*avoidedCount (p 134) ((positions 134 j).val+1) (avoidedPositions (positions 134) (R 134 j z))+2-
        (24-1-(R 134 j z).card))/3) ∧
    (∀ j, loss 134 j ≤ (∑ z, (quota 134 j z : ℚ)*α 134 j z)-
      penaltySum (p 134) ((positions 134 j).val+1) (fun z => avoidedPositions (positions 134) (R 134 j z)) (α 134 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 134) (k.val+1) true)
      (min (CachedRows.cachedA (p 134) (k.val+1) false) (CachedRows.cachedC (p 134) (k.val+1)-centerLoss (positions 134) (loss 134) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_135 : Numeric.validProfile (p 135) 34 ∧ (p 135).emptyPairCap=none ∧
    (∀ j, (positions 135 j).val+1∈(p 135).correctionCenters) ∧
    (∀ j z, 0≤α 135 j z) ∧ (∀ j z, j∉R 135 j z) ∧
    (∀ j z, quota 135 j z ≤
      (4*avoidedCount (p 135) ((positions 135 j).val+1) (avoidedPositions (positions 135) (R 135 j z))+2-
        (24-1-(R 135 j z).card))/3) ∧
    (∀ j, loss 135 j ≤ (∑ z, (quota 135 j z : ℚ)*α 135 j z)-
      penaltySum (p 135) ((positions 135 j).val+1) (fun z => avoidedPositions (positions 135) (R 135 j z)) (α 135 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 135) (k.val+1) true)
      (min (CachedRows.cachedA (p 135) (k.val+1) false) (CachedRows.cachedC (p 135) (k.val+1)-centerLoss (positions 135) (loss 135) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_136 : Numeric.validProfile (p 136) 34 ∧ (p 136).emptyPairCap=none ∧
    (∀ j, (positions 136 j).val+1∈(p 136).correctionCenters) ∧
    (∀ j z, 0≤α 136 j z) ∧ (∀ j z, j∉R 136 j z) ∧
    (∀ j z, quota 136 j z ≤
      (4*avoidedCount (p 136) ((positions 136 j).val+1) (avoidedPositions (positions 136) (R 136 j z))+2-
        (24-1-(R 136 j z).card))/3) ∧
    (∀ j, loss 136 j ≤ (∑ z, (quota 136 j z : ℚ)*α 136 j z)-
      penaltySum (p 136) ((positions 136 j).val+1) (fun z => avoidedPositions (positions 136) (R 136 j z)) (α 136 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 136) (k.val+1) true)
      (min (CachedRows.cachedA (p 136) (k.val+1) false) (CachedRows.cachedC (p 136) (k.val+1)-centerLoss (positions 136) (loss 136) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_137 : Numeric.validProfile (p 137) 34 ∧ (p 137).emptyPairCap=none ∧
    (∀ j, (positions 137 j).val+1∈(p 137).correctionCenters) ∧
    (∀ j z, 0≤α 137 j z) ∧ (∀ j z, j∉R 137 j z) ∧
    (∀ j z, quota 137 j z ≤
      (4*avoidedCount (p 137) ((positions 137 j).val+1) (avoidedPositions (positions 137) (R 137 j z))+2-
        (24-1-(R 137 j z).card))/3) ∧
    (∀ j, loss 137 j ≤ (∑ z, (quota 137 j z : ℚ)*α 137 j z)-
      penaltySum (p 137) ((positions 137 j).val+1) (fun z => avoidedPositions (positions 137) (R 137 j z)) (α 137 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 137) (k.val+1) true)
      (min (CachedRows.cachedA (p 137) (k.val+1) false) (CachedRows.cachedC (p 137) (k.val+1)-centerLoss (positions 137) (loss 137) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_138 : Numeric.validProfile (p 138) 34 ∧ (p 138).emptyPairCap=none ∧
    (∀ j, (positions 138 j).val+1∈(p 138).correctionCenters) ∧
    (∀ j z, 0≤α 138 j z) ∧ (∀ j z, j∉R 138 j z) ∧
    (∀ j z, quota 138 j z ≤
      (4*avoidedCount (p 138) ((positions 138 j).val+1) (avoidedPositions (positions 138) (R 138 j z))+2-
        (24-1-(R 138 j z).card))/3) ∧
    (∀ j, loss 138 j ≤ (∑ z, (quota 138 j z : ℚ)*α 138 j z)-
      penaltySum (p 138) ((positions 138 j).val+1) (fun z => avoidedPositions (positions 138) (R 138 j z)) (α 138 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 138) (k.val+1) true)
      (min (CachedRows.cachedA (p 138) (k.val+1) false) (CachedRows.cachedC (p 138) (k.val+1)-centerLoss (positions 138) (loss 138) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_139 : Numeric.validProfile (p 139) 34 ∧ (p 139).emptyPairCap=none ∧
    (∀ j, (positions 139 j).val+1∈(p 139).correctionCenters) ∧
    (∀ j z, 0≤α 139 j z) ∧ (∀ j z, j∉R 139 j z) ∧
    (∀ j z, quota 139 j z ≤
      (4*avoidedCount (p 139) ((positions 139 j).val+1) (avoidedPositions (positions 139) (R 139 j z))+2-
        (24-1-(R 139 j z).card))/3) ∧
    (∀ j, loss 139 j ≤ (∑ z, (quota 139 j z : ℚ)*α 139 j z)-
      penaltySum (p 139) ((positions 139 j).val+1) (fun z => avoidedPositions (positions 139) (R 139 j z)) (α 139 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 139) (k.val+1) true)
      (min (CachedRows.cachedA (p 139) (k.val+1) false) (CachedRows.cachedC (p 139) (k.val+1)-centerLoss (positions 139) (loss 139) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
