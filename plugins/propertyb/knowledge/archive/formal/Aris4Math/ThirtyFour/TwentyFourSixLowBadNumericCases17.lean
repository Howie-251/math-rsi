import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_170 : Numeric.validProfile (p 170) 34 ∧ (p 170).emptyPairCap=none ∧
    (∀ j, (positions 170 j).val+1∈(p 170).correctionCenters) ∧
    (∀ j z, 0≤α 170 j z) ∧ (∀ j z, j∉R 170 j z) ∧
    (∀ j z, quota 170 j z ≤
      (4*avoidedCount (p 170) ((positions 170 j).val+1) (avoidedPositions (positions 170) (R 170 j z))+2-
        (24-1-(R 170 j z).card))/3) ∧
    (∀ j, loss 170 j ≤ (∑ z, (quota 170 j z : ℚ)*α 170 j z)-
      penaltySum (p 170) ((positions 170 j).val+1) (fun z => avoidedPositions (positions 170) (R 170 j z)) (α 170 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 170) (k.val+1) true)
      (min (CachedRows.cachedA (p 170) (k.val+1) false) (CachedRows.cachedC (p 170) (k.val+1)-centerLoss (positions 170) (loss 170) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_171 : Numeric.validProfile (p 171) 34 ∧ (p 171).emptyPairCap=none ∧
    (∀ j, (positions 171 j).val+1∈(p 171).correctionCenters) ∧
    (∀ j z, 0≤α 171 j z) ∧ (∀ j z, j∉R 171 j z) ∧
    (∀ j z, quota 171 j z ≤
      (4*avoidedCount (p 171) ((positions 171 j).val+1) (avoidedPositions (positions 171) (R 171 j z))+2-
        (24-1-(R 171 j z).card))/3) ∧
    (∀ j, loss 171 j ≤ (∑ z, (quota 171 j z : ℚ)*α 171 j z)-
      penaltySum (p 171) ((positions 171 j).val+1) (fun z => avoidedPositions (positions 171) (R 171 j z)) (α 171 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 171) (k.val+1) true)
      (min (CachedRows.cachedA (p 171) (k.val+1) false) (CachedRows.cachedC (p 171) (k.val+1)-centerLoss (positions 171) (loss 171) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_172 : Numeric.validProfile (p 172) 34 ∧ (p 172).emptyPairCap=none ∧
    (∀ j, (positions 172 j).val+1∈(p 172).correctionCenters) ∧
    (∀ j z, 0≤α 172 j z) ∧ (∀ j z, j∉R 172 j z) ∧
    (∀ j z, quota 172 j z ≤
      (4*avoidedCount (p 172) ((positions 172 j).val+1) (avoidedPositions (positions 172) (R 172 j z))+2-
        (24-1-(R 172 j z).card))/3) ∧
    (∀ j, loss 172 j ≤ (∑ z, (quota 172 j z : ℚ)*α 172 j z)-
      penaltySum (p 172) ((positions 172 j).val+1) (fun z => avoidedPositions (positions 172) (R 172 j z)) (α 172 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 172) (k.val+1) true)
      (min (CachedRows.cachedA (p 172) (k.val+1) false) (CachedRows.cachedC (p 172) (k.val+1)-centerLoss (positions 172) (loss 172) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_173 : Numeric.validProfile (p 173) 34 ∧ (p 173).emptyPairCap=none ∧
    (∀ j, (positions 173 j).val+1∈(p 173).correctionCenters) ∧
    (∀ j z, 0≤α 173 j z) ∧ (∀ j z, j∉R 173 j z) ∧
    (∀ j z, quota 173 j z ≤
      (4*avoidedCount (p 173) ((positions 173 j).val+1) (avoidedPositions (positions 173) (R 173 j z))+2-
        (24-1-(R 173 j z).card))/3) ∧
    (∀ j, loss 173 j ≤ (∑ z, (quota 173 j z : ℚ)*α 173 j z)-
      penaltySum (p 173) ((positions 173 j).val+1) (fun z => avoidedPositions (positions 173) (R 173 j z)) (α 173 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 173) (k.val+1) true)
      (min (CachedRows.cachedA (p 173) (k.val+1) false) (CachedRows.cachedC (p 173) (k.val+1)-centerLoss (positions 173) (loss 173) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_174 : Numeric.validProfile (p 174) 34 ∧ (p 174).emptyPairCap=none ∧
    (∀ j, (positions 174 j).val+1∈(p 174).correctionCenters) ∧
    (∀ j z, 0≤α 174 j z) ∧ (∀ j z, j∉R 174 j z) ∧
    (∀ j z, quota 174 j z ≤
      (4*avoidedCount (p 174) ((positions 174 j).val+1) (avoidedPositions (positions 174) (R 174 j z))+2-
        (24-1-(R 174 j z).card))/3) ∧
    (∀ j, loss 174 j ≤ (∑ z, (quota 174 j z : ℚ)*α 174 j z)-
      penaltySum (p 174) ((positions 174 j).val+1) (fun z => avoidedPositions (positions 174) (R 174 j z)) (α 174 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 174) (k.val+1) true)
      (min (CachedRows.cachedA (p 174) (k.val+1) false) (CachedRows.cachedC (p 174) (k.val+1)-centerLoss (positions 174) (loss 174) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_175 : Numeric.validProfile (p 175) 34 ∧ (p 175).emptyPairCap=none ∧
    (∀ j, (positions 175 j).val+1∈(p 175).correctionCenters) ∧
    (∀ j z, 0≤α 175 j z) ∧ (∀ j z, j∉R 175 j z) ∧
    (∀ j z, quota 175 j z ≤
      (4*avoidedCount (p 175) ((positions 175 j).val+1) (avoidedPositions (positions 175) (R 175 j z))+2-
        (24-1-(R 175 j z).card))/3) ∧
    (∀ j, loss 175 j ≤ (∑ z, (quota 175 j z : ℚ)*α 175 j z)-
      penaltySum (p 175) ((positions 175 j).val+1) (fun z => avoidedPositions (positions 175) (R 175 j z)) (α 175 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 175) (k.val+1) true)
      (min (CachedRows.cachedA (p 175) (k.val+1) false) (CachedRows.cachedC (p 175) (k.val+1)-centerLoss (positions 175) (loss 175) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_176 : Numeric.validProfile (p 176) 34 ∧ (p 176).emptyPairCap=none ∧
    (∀ j, (positions 176 j).val+1∈(p 176).correctionCenters) ∧
    (∀ j z, 0≤α 176 j z) ∧ (∀ j z, j∉R 176 j z) ∧
    (∀ j z, quota 176 j z ≤
      (4*avoidedCount (p 176) ((positions 176 j).val+1) (avoidedPositions (positions 176) (R 176 j z))+2-
        (24-1-(R 176 j z).card))/3) ∧
    (∀ j, loss 176 j ≤ (∑ z, (quota 176 j z : ℚ)*α 176 j z)-
      penaltySum (p 176) ((positions 176 j).val+1) (fun z => avoidedPositions (positions 176) (R 176 j z)) (α 176 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 176) (k.val+1) true)
      (min (CachedRows.cachedA (p 176) (k.val+1) false) (CachedRows.cachedC (p 176) (k.val+1)-centerLoss (positions 176) (loss 176) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_177 : Numeric.validProfile (p 177) 34 ∧ (p 177).emptyPairCap=none ∧
    (∀ j, (positions 177 j).val+1∈(p 177).correctionCenters) ∧
    (∀ j z, 0≤α 177 j z) ∧ (∀ j z, j∉R 177 j z) ∧
    (∀ j z, quota 177 j z ≤
      (4*avoidedCount (p 177) ((positions 177 j).val+1) (avoidedPositions (positions 177) (R 177 j z))+2-
        (24-1-(R 177 j z).card))/3) ∧
    (∀ j, loss 177 j ≤ (∑ z, (quota 177 j z : ℚ)*α 177 j z)-
      penaltySum (p 177) ((positions 177 j).val+1) (fun z => avoidedPositions (positions 177) (R 177 j z)) (α 177 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 177) (k.val+1) true)
      (min (CachedRows.cachedA (p 177) (k.val+1) false) (CachedRows.cachedC (p 177) (k.val+1)-centerLoss (positions 177) (loss 177) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_178 : Numeric.validProfile (p 178) 34 ∧ (p 178).emptyPairCap=none ∧
    (∀ j, (positions 178 j).val+1∈(p 178).correctionCenters) ∧
    (∀ j z, 0≤α 178 j z) ∧ (∀ j z, j∉R 178 j z) ∧
    (∀ j z, quota 178 j z ≤
      (4*avoidedCount (p 178) ((positions 178 j).val+1) (avoidedPositions (positions 178) (R 178 j z))+2-
        (24-1-(R 178 j z).card))/3) ∧
    (∀ j, loss 178 j ≤ (∑ z, (quota 178 j z : ℚ)*α 178 j z)-
      penaltySum (p 178) ((positions 178 j).val+1) (fun z => avoidedPositions (positions 178) (R 178 j z)) (α 178 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 178) (k.val+1) true)
      (min (CachedRows.cachedA (p 178) (k.val+1) false) (CachedRows.cachedC (p 178) (k.val+1)-centerLoss (positions 178) (loss 178) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_179 : Numeric.validProfile (p 179) 34 ∧ (p 179).emptyPairCap=none ∧
    (∀ j, (positions 179 j).val+1∈(p 179).correctionCenters) ∧
    (∀ j z, 0≤α 179 j z) ∧ (∀ j z, j∉R 179 j z) ∧
    (∀ j z, quota 179 j z ≤
      (4*avoidedCount (p 179) ((positions 179 j).val+1) (avoidedPositions (positions 179) (R 179 j z))+2-
        (24-1-(R 179 j z).card))/3) ∧
    (∀ j, loss 179 j ≤ (∑ z, (quota 179 j z : ℚ)*α 179 j z)-
      penaltySum (p 179) ((positions 179 j).val+1) (fun z => avoidedPositions (positions 179) (R 179 j z)) (α 179 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 179) (k.val+1) true)
      (min (CachedRows.cachedA (p 179) (k.val+1) false) (CachedRows.cachedC (p 179) (k.val+1)-centerLoss (positions 179) (loss 179) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
