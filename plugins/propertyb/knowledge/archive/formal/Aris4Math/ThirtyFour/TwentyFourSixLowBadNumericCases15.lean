import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_150 : Numeric.validProfile (p 150) 34 ∧ (p 150).emptyPairCap=none ∧
    (∀ j, (positions 150 j).val+1∈(p 150).correctionCenters) ∧
    (∀ j z, 0≤α 150 j z) ∧ (∀ j z, j∉R 150 j z) ∧
    (∀ j z, quota 150 j z ≤
      (4*avoidedCount (p 150) ((positions 150 j).val+1) (avoidedPositions (positions 150) (R 150 j z))+2-
        (24-1-(R 150 j z).card))/3) ∧
    (∀ j, loss 150 j ≤ (∑ z, (quota 150 j z : ℚ)*α 150 j z)-
      penaltySum (p 150) ((positions 150 j).val+1) (fun z => avoidedPositions (positions 150) (R 150 j z)) (α 150 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 150) (k.val+1) true)
      (min (CachedRows.cachedA (p 150) (k.val+1) false) (CachedRows.cachedC (p 150) (k.val+1)-centerLoss (positions 150) (loss 150) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_151 : Numeric.validProfile (p 151) 34 ∧ (p 151).emptyPairCap=none ∧
    (∀ j, (positions 151 j).val+1∈(p 151).correctionCenters) ∧
    (∀ j z, 0≤α 151 j z) ∧ (∀ j z, j∉R 151 j z) ∧
    (∀ j z, quota 151 j z ≤
      (4*avoidedCount (p 151) ((positions 151 j).val+1) (avoidedPositions (positions 151) (R 151 j z))+2-
        (24-1-(R 151 j z).card))/3) ∧
    (∀ j, loss 151 j ≤ (∑ z, (quota 151 j z : ℚ)*α 151 j z)-
      penaltySum (p 151) ((positions 151 j).val+1) (fun z => avoidedPositions (positions 151) (R 151 j z)) (α 151 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 151) (k.val+1) true)
      (min (CachedRows.cachedA (p 151) (k.val+1) false) (CachedRows.cachedC (p 151) (k.val+1)-centerLoss (positions 151) (loss 151) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_152 : Numeric.validProfile (p 152) 34 ∧ (p 152).emptyPairCap=none ∧
    (∀ j, (positions 152 j).val+1∈(p 152).correctionCenters) ∧
    (∀ j z, 0≤α 152 j z) ∧ (∀ j z, j∉R 152 j z) ∧
    (∀ j z, quota 152 j z ≤
      (4*avoidedCount (p 152) ((positions 152 j).val+1) (avoidedPositions (positions 152) (R 152 j z))+2-
        (24-1-(R 152 j z).card))/3) ∧
    (∀ j, loss 152 j ≤ (∑ z, (quota 152 j z : ℚ)*α 152 j z)-
      penaltySum (p 152) ((positions 152 j).val+1) (fun z => avoidedPositions (positions 152) (R 152 j z)) (α 152 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 152) (k.val+1) true)
      (min (CachedRows.cachedA (p 152) (k.val+1) false) (CachedRows.cachedC (p 152) (k.val+1)-centerLoss (positions 152) (loss 152) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_153 : Numeric.validProfile (p 153) 34 ∧ (p 153).emptyPairCap=none ∧
    (∀ j, (positions 153 j).val+1∈(p 153).correctionCenters) ∧
    (∀ j z, 0≤α 153 j z) ∧ (∀ j z, j∉R 153 j z) ∧
    (∀ j z, quota 153 j z ≤
      (4*avoidedCount (p 153) ((positions 153 j).val+1) (avoidedPositions (positions 153) (R 153 j z))+2-
        (24-1-(R 153 j z).card))/3) ∧
    (∀ j, loss 153 j ≤ (∑ z, (quota 153 j z : ℚ)*α 153 j z)-
      penaltySum (p 153) ((positions 153 j).val+1) (fun z => avoidedPositions (positions 153) (R 153 j z)) (α 153 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 153) (k.val+1) true)
      (min (CachedRows.cachedA (p 153) (k.val+1) false) (CachedRows.cachedC (p 153) (k.val+1)-centerLoss (positions 153) (loss 153) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_154 : Numeric.validProfile (p 154) 34 ∧ (p 154).emptyPairCap=none ∧
    (∀ j, (positions 154 j).val+1∈(p 154).correctionCenters) ∧
    (∀ j z, 0≤α 154 j z) ∧ (∀ j z, j∉R 154 j z) ∧
    (∀ j z, quota 154 j z ≤
      (4*avoidedCount (p 154) ((positions 154 j).val+1) (avoidedPositions (positions 154) (R 154 j z))+2-
        (24-1-(R 154 j z).card))/3) ∧
    (∀ j, loss 154 j ≤ (∑ z, (quota 154 j z : ℚ)*α 154 j z)-
      penaltySum (p 154) ((positions 154 j).val+1) (fun z => avoidedPositions (positions 154) (R 154 j z)) (α 154 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 154) (k.val+1) true)
      (min (CachedRows.cachedA (p 154) (k.val+1) false) (CachedRows.cachedC (p 154) (k.val+1)-centerLoss (positions 154) (loss 154) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_155 : Numeric.validProfile (p 155) 34 ∧ (p 155).emptyPairCap=none ∧
    (∀ j, (positions 155 j).val+1∈(p 155).correctionCenters) ∧
    (∀ j z, 0≤α 155 j z) ∧ (∀ j z, j∉R 155 j z) ∧
    (∀ j z, quota 155 j z ≤
      (4*avoidedCount (p 155) ((positions 155 j).val+1) (avoidedPositions (positions 155) (R 155 j z))+2-
        (24-1-(R 155 j z).card))/3) ∧
    (∀ j, loss 155 j ≤ (∑ z, (quota 155 j z : ℚ)*α 155 j z)-
      penaltySum (p 155) ((positions 155 j).val+1) (fun z => avoidedPositions (positions 155) (R 155 j z)) (α 155 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 155) (k.val+1) true)
      (min (CachedRows.cachedA (p 155) (k.val+1) false) (CachedRows.cachedC (p 155) (k.val+1)-centerLoss (positions 155) (loss 155) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_156 : Numeric.validProfile (p 156) 34 ∧ (p 156).emptyPairCap=none ∧
    (∀ j, (positions 156 j).val+1∈(p 156).correctionCenters) ∧
    (∀ j z, 0≤α 156 j z) ∧ (∀ j z, j∉R 156 j z) ∧
    (∀ j z, quota 156 j z ≤
      (4*avoidedCount (p 156) ((positions 156 j).val+1) (avoidedPositions (positions 156) (R 156 j z))+2-
        (24-1-(R 156 j z).card))/3) ∧
    (∀ j, loss 156 j ≤ (∑ z, (quota 156 j z : ℚ)*α 156 j z)-
      penaltySum (p 156) ((positions 156 j).val+1) (fun z => avoidedPositions (positions 156) (R 156 j z)) (α 156 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 156) (k.val+1) true)
      (min (CachedRows.cachedA (p 156) (k.val+1) false) (CachedRows.cachedC (p 156) (k.val+1)-centerLoss (positions 156) (loss 156) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_157 : Numeric.validProfile (p 157) 34 ∧ (p 157).emptyPairCap=none ∧
    (∀ j, (positions 157 j).val+1∈(p 157).correctionCenters) ∧
    (∀ j z, 0≤α 157 j z) ∧ (∀ j z, j∉R 157 j z) ∧
    (∀ j z, quota 157 j z ≤
      (4*avoidedCount (p 157) ((positions 157 j).val+1) (avoidedPositions (positions 157) (R 157 j z))+2-
        (24-1-(R 157 j z).card))/3) ∧
    (∀ j, loss 157 j ≤ (∑ z, (quota 157 j z : ℚ)*α 157 j z)-
      penaltySum (p 157) ((positions 157 j).val+1) (fun z => avoidedPositions (positions 157) (R 157 j z)) (α 157 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 157) (k.val+1) true)
      (min (CachedRows.cachedA (p 157) (k.val+1) false) (CachedRows.cachedC (p 157) (k.val+1)-centerLoss (positions 157) (loss 157) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_158 : Numeric.validProfile (p 158) 34 ∧ (p 158).emptyPairCap=none ∧
    (∀ j, (positions 158 j).val+1∈(p 158).correctionCenters) ∧
    (∀ j z, 0≤α 158 j z) ∧ (∀ j z, j∉R 158 j z) ∧
    (∀ j z, quota 158 j z ≤
      (4*avoidedCount (p 158) ((positions 158 j).val+1) (avoidedPositions (positions 158) (R 158 j z))+2-
        (24-1-(R 158 j z).card))/3) ∧
    (∀ j, loss 158 j ≤ (∑ z, (quota 158 j z : ℚ)*α 158 j z)-
      penaltySum (p 158) ((positions 158 j).val+1) (fun z => avoidedPositions (positions 158) (R 158 j z)) (α 158 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 158) (k.val+1) true)
      (min (CachedRows.cachedA (p 158) (k.val+1) false) (CachedRows.cachedC (p 158) (k.val+1)-centerLoss (positions 158) (loss 158) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_159 : Numeric.validProfile (p 159) 34 ∧ (p 159).emptyPairCap=none ∧
    (∀ j, (positions 159 j).val+1∈(p 159).correctionCenters) ∧
    (∀ j z, 0≤α 159 j z) ∧ (∀ j z, j∉R 159 j z) ∧
    (∀ j z, quota 159 j z ≤
      (4*avoidedCount (p 159) ((positions 159 j).val+1) (avoidedPositions (positions 159) (R 159 j z))+2-
        (24-1-(R 159 j z).card))/3) ∧
    (∀ j, loss 159 j ≤ (∑ z, (quota 159 j z : ℚ)*α 159 j z)-
      penaltySum (p 159) ((positions 159 j).val+1) (fun z => avoidedPositions (positions 159) (R 159 j z)) (α 159 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 159) (k.val+1) true)
      (min (CachedRows.cachedA (p 159) (k.val+1) false) (CachedRows.cachedC (p 159) (k.val+1)-centerLoss (positions 159) (loss 159) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
