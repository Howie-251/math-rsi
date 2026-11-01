import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_120 : Numeric.validProfile (p 120) 34 ∧ (p 120).emptyPairCap=none ∧
    (∀ j, (positions 120 j).val+1∈(p 120).correctionCenters) ∧
    (∀ j z, 0≤α 120 j z) ∧ (∀ j z, j∉R 120 j z) ∧
    (∀ j z, quota 120 j z ≤
      (4*avoidedCount (p 120) ((positions 120 j).val+1) (avoidedPositions (positions 120) (R 120 j z))+2-
        (24-1-(R 120 j z).card))/3) ∧
    (∀ j, loss 120 j ≤ (∑ z, (quota 120 j z : ℚ)*α 120 j z)-
      penaltySum (p 120) ((positions 120 j).val+1) (fun z => avoidedPositions (positions 120) (R 120 j z)) (α 120 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 120) (k.val+1) true)
      (min (CachedRows.cachedA (p 120) (k.val+1) false) (CachedRows.cachedC (p 120) (k.val+1)-centerLoss (positions 120) (loss 120) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_121 : Numeric.validProfile (p 121) 34 ∧ (p 121).emptyPairCap=none ∧
    (∀ j, (positions 121 j).val+1∈(p 121).correctionCenters) ∧
    (∀ j z, 0≤α 121 j z) ∧ (∀ j z, j∉R 121 j z) ∧
    (∀ j z, quota 121 j z ≤
      (4*avoidedCount (p 121) ((positions 121 j).val+1) (avoidedPositions (positions 121) (R 121 j z))+2-
        (24-1-(R 121 j z).card))/3) ∧
    (∀ j, loss 121 j ≤ (∑ z, (quota 121 j z : ℚ)*α 121 j z)-
      penaltySum (p 121) ((positions 121 j).val+1) (fun z => avoidedPositions (positions 121) (R 121 j z)) (α 121 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 121) (k.val+1) true)
      (min (CachedRows.cachedA (p 121) (k.val+1) false) (CachedRows.cachedC (p 121) (k.val+1)-centerLoss (positions 121) (loss 121) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_122 : Numeric.validProfile (p 122) 34 ∧ (p 122).emptyPairCap=none ∧
    (∀ j, (positions 122 j).val+1∈(p 122).correctionCenters) ∧
    (∀ j z, 0≤α 122 j z) ∧ (∀ j z, j∉R 122 j z) ∧
    (∀ j z, quota 122 j z ≤
      (4*avoidedCount (p 122) ((positions 122 j).val+1) (avoidedPositions (positions 122) (R 122 j z))+2-
        (24-1-(R 122 j z).card))/3) ∧
    (∀ j, loss 122 j ≤ (∑ z, (quota 122 j z : ℚ)*α 122 j z)-
      penaltySum (p 122) ((positions 122 j).val+1) (fun z => avoidedPositions (positions 122) (R 122 j z)) (α 122 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 122) (k.val+1) true)
      (min (CachedRows.cachedA (p 122) (k.val+1) false) (CachedRows.cachedC (p 122) (k.val+1)-centerLoss (positions 122) (loss 122) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_123 : Numeric.validProfile (p 123) 34 ∧ (p 123).emptyPairCap=none ∧
    (∀ j, (positions 123 j).val+1∈(p 123).correctionCenters) ∧
    (∀ j z, 0≤α 123 j z) ∧ (∀ j z, j∉R 123 j z) ∧
    (∀ j z, quota 123 j z ≤
      (4*avoidedCount (p 123) ((positions 123 j).val+1) (avoidedPositions (positions 123) (R 123 j z))+2-
        (24-1-(R 123 j z).card))/3) ∧
    (∀ j, loss 123 j ≤ (∑ z, (quota 123 j z : ℚ)*α 123 j z)-
      penaltySum (p 123) ((positions 123 j).val+1) (fun z => avoidedPositions (positions 123) (R 123 j z)) (α 123 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 123) (k.val+1) true)
      (min (CachedRows.cachedA (p 123) (k.val+1) false) (CachedRows.cachedC (p 123) (k.val+1)-centerLoss (positions 123) (loss 123) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_124 : Numeric.validProfile (p 124) 34 ∧ (p 124).emptyPairCap=none ∧
    (∀ j, (positions 124 j).val+1∈(p 124).correctionCenters) ∧
    (∀ j z, 0≤α 124 j z) ∧ (∀ j z, j∉R 124 j z) ∧
    (∀ j z, quota 124 j z ≤
      (4*avoidedCount (p 124) ((positions 124 j).val+1) (avoidedPositions (positions 124) (R 124 j z))+2-
        (24-1-(R 124 j z).card))/3) ∧
    (∀ j, loss 124 j ≤ (∑ z, (quota 124 j z : ℚ)*α 124 j z)-
      penaltySum (p 124) ((positions 124 j).val+1) (fun z => avoidedPositions (positions 124) (R 124 j z)) (α 124 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 124) (k.val+1) true)
      (min (CachedRows.cachedA (p 124) (k.val+1) false) (CachedRows.cachedC (p 124) (k.val+1)-centerLoss (positions 124) (loss 124) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_125 : Numeric.validProfile (p 125) 34 ∧ (p 125).emptyPairCap=none ∧
    (∀ j, (positions 125 j).val+1∈(p 125).correctionCenters) ∧
    (∀ j z, 0≤α 125 j z) ∧ (∀ j z, j∉R 125 j z) ∧
    (∀ j z, quota 125 j z ≤
      (4*avoidedCount (p 125) ((positions 125 j).val+1) (avoidedPositions (positions 125) (R 125 j z))+2-
        (24-1-(R 125 j z).card))/3) ∧
    (∀ j, loss 125 j ≤ (∑ z, (quota 125 j z : ℚ)*α 125 j z)-
      penaltySum (p 125) ((positions 125 j).val+1) (fun z => avoidedPositions (positions 125) (R 125 j z)) (α 125 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 125) (k.val+1) true)
      (min (CachedRows.cachedA (p 125) (k.val+1) false) (CachedRows.cachedC (p 125) (k.val+1)-centerLoss (positions 125) (loss 125) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_126 : Numeric.validProfile (p 126) 34 ∧ (p 126).emptyPairCap=none ∧
    (∀ j, (positions 126 j).val+1∈(p 126).correctionCenters) ∧
    (∀ j z, 0≤α 126 j z) ∧ (∀ j z, j∉R 126 j z) ∧
    (∀ j z, quota 126 j z ≤
      (4*avoidedCount (p 126) ((positions 126 j).val+1) (avoidedPositions (positions 126) (R 126 j z))+2-
        (24-1-(R 126 j z).card))/3) ∧
    (∀ j, loss 126 j ≤ (∑ z, (quota 126 j z : ℚ)*α 126 j z)-
      penaltySum (p 126) ((positions 126 j).val+1) (fun z => avoidedPositions (positions 126) (R 126 j z)) (α 126 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 126) (k.val+1) true)
      (min (CachedRows.cachedA (p 126) (k.val+1) false) (CachedRows.cachedC (p 126) (k.val+1)-centerLoss (positions 126) (loss 126) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_127 : Numeric.validProfile (p 127) 34 ∧ (p 127).emptyPairCap=none ∧
    (∀ j, (positions 127 j).val+1∈(p 127).correctionCenters) ∧
    (∀ j z, 0≤α 127 j z) ∧ (∀ j z, j∉R 127 j z) ∧
    (∀ j z, quota 127 j z ≤
      (4*avoidedCount (p 127) ((positions 127 j).val+1) (avoidedPositions (positions 127) (R 127 j z))+2-
        (24-1-(R 127 j z).card))/3) ∧
    (∀ j, loss 127 j ≤ (∑ z, (quota 127 j z : ℚ)*α 127 j z)-
      penaltySum (p 127) ((positions 127 j).val+1) (fun z => avoidedPositions (positions 127) (R 127 j z)) (α 127 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 127) (k.val+1) true)
      (min (CachedRows.cachedA (p 127) (k.val+1) false) (CachedRows.cachedC (p 127) (k.val+1)-centerLoss (positions 127) (loss 127) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_128 : Numeric.validProfile (p 128) 34 ∧ (p 128).emptyPairCap=none ∧
    (∀ j, (positions 128 j).val+1∈(p 128).correctionCenters) ∧
    (∀ j z, 0≤α 128 j z) ∧ (∀ j z, j∉R 128 j z) ∧
    (∀ j z, quota 128 j z ≤
      (4*avoidedCount (p 128) ((positions 128 j).val+1) (avoidedPositions (positions 128) (R 128 j z))+2-
        (24-1-(R 128 j z).card))/3) ∧
    (∀ j, loss 128 j ≤ (∑ z, (quota 128 j z : ℚ)*α 128 j z)-
      penaltySum (p 128) ((positions 128 j).val+1) (fun z => avoidedPositions (positions 128) (R 128 j z)) (α 128 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 128) (k.val+1) true)
      (min (CachedRows.cachedA (p 128) (k.val+1) false) (CachedRows.cachedC (p 128) (k.val+1)-centerLoss (positions 128) (loss 128) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_129 : Numeric.validProfile (p 129) 34 ∧ (p 129).emptyPairCap=none ∧
    (∀ j, (positions 129 j).val+1∈(p 129).correctionCenters) ∧
    (∀ j z, 0≤α 129 j z) ∧ (∀ j z, j∉R 129 j z) ∧
    (∀ j z, quota 129 j z ≤
      (4*avoidedCount (p 129) ((positions 129 j).val+1) (avoidedPositions (positions 129) (R 129 j z))+2-
        (24-1-(R 129 j z).card))/3) ∧
    (∀ j, loss 129 j ≤ (∑ z, (quota 129 j z : ℚ)*α 129 j z)-
      penaltySum (p 129) ((positions 129 j).val+1) (fun z => avoidedPositions (positions 129) (R 129 j z)) (α 129 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 129) (k.val+1) true)
      (min (CachedRows.cachedA (p 129) (k.val+1) false) (CachedRows.cachedC (p 129) (k.val+1)-centerLoss (positions 129) (loss 129) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
