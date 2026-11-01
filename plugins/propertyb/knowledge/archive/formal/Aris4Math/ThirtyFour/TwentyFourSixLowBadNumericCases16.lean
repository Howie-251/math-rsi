import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_160 : Numeric.validProfile (p 160) 34 ∧ (p 160).emptyPairCap=none ∧
    (∀ j, (positions 160 j).val+1∈(p 160).correctionCenters) ∧
    (∀ j z, 0≤α 160 j z) ∧ (∀ j z, j∉R 160 j z) ∧
    (∀ j z, quota 160 j z ≤
      (4*avoidedCount (p 160) ((positions 160 j).val+1) (avoidedPositions (positions 160) (R 160 j z))+2-
        (24-1-(R 160 j z).card))/3) ∧
    (∀ j, loss 160 j ≤ (∑ z, (quota 160 j z : ℚ)*α 160 j z)-
      penaltySum (p 160) ((positions 160 j).val+1) (fun z => avoidedPositions (positions 160) (R 160 j z)) (α 160 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 160) (k.val+1) true)
      (min (CachedRows.cachedA (p 160) (k.val+1) false) (CachedRows.cachedC (p 160) (k.val+1)-centerLoss (positions 160) (loss 160) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_161 : Numeric.validProfile (p 161) 34 ∧ (p 161).emptyPairCap=none ∧
    (∀ j, (positions 161 j).val+1∈(p 161).correctionCenters) ∧
    (∀ j z, 0≤α 161 j z) ∧ (∀ j z, j∉R 161 j z) ∧
    (∀ j z, quota 161 j z ≤
      (4*avoidedCount (p 161) ((positions 161 j).val+1) (avoidedPositions (positions 161) (R 161 j z))+2-
        (24-1-(R 161 j z).card))/3) ∧
    (∀ j, loss 161 j ≤ (∑ z, (quota 161 j z : ℚ)*α 161 j z)-
      penaltySum (p 161) ((positions 161 j).val+1) (fun z => avoidedPositions (positions 161) (R 161 j z)) (α 161 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 161) (k.val+1) true)
      (min (CachedRows.cachedA (p 161) (k.val+1) false) (CachedRows.cachedC (p 161) (k.val+1)-centerLoss (positions 161) (loss 161) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_162 : Numeric.validProfile (p 162) 34 ∧ (p 162).emptyPairCap=none ∧
    (∀ j, (positions 162 j).val+1∈(p 162).correctionCenters) ∧
    (∀ j z, 0≤α 162 j z) ∧ (∀ j z, j∉R 162 j z) ∧
    (∀ j z, quota 162 j z ≤
      (4*avoidedCount (p 162) ((positions 162 j).val+1) (avoidedPositions (positions 162) (R 162 j z))+2-
        (24-1-(R 162 j z).card))/3) ∧
    (∀ j, loss 162 j ≤ (∑ z, (quota 162 j z : ℚ)*α 162 j z)-
      penaltySum (p 162) ((positions 162 j).val+1) (fun z => avoidedPositions (positions 162) (R 162 j z)) (α 162 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 162) (k.val+1) true)
      (min (CachedRows.cachedA (p 162) (k.val+1) false) (CachedRows.cachedC (p 162) (k.val+1)-centerLoss (positions 162) (loss 162) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_163 : Numeric.validProfile (p 163) 34 ∧ (p 163).emptyPairCap=none ∧
    (∀ j, (positions 163 j).val+1∈(p 163).correctionCenters) ∧
    (∀ j z, 0≤α 163 j z) ∧ (∀ j z, j∉R 163 j z) ∧
    (∀ j z, quota 163 j z ≤
      (4*avoidedCount (p 163) ((positions 163 j).val+1) (avoidedPositions (positions 163) (R 163 j z))+2-
        (24-1-(R 163 j z).card))/3) ∧
    (∀ j, loss 163 j ≤ (∑ z, (quota 163 j z : ℚ)*α 163 j z)-
      penaltySum (p 163) ((positions 163 j).val+1) (fun z => avoidedPositions (positions 163) (R 163 j z)) (α 163 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 163) (k.val+1) true)
      (min (CachedRows.cachedA (p 163) (k.val+1) false) (CachedRows.cachedC (p 163) (k.val+1)-centerLoss (positions 163) (loss 163) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_164 : Numeric.validProfile (p 164) 34 ∧ (p 164).emptyPairCap=none ∧
    (∀ j, (positions 164 j).val+1∈(p 164).correctionCenters) ∧
    (∀ j z, 0≤α 164 j z) ∧ (∀ j z, j∉R 164 j z) ∧
    (∀ j z, quota 164 j z ≤
      (4*avoidedCount (p 164) ((positions 164 j).val+1) (avoidedPositions (positions 164) (R 164 j z))+2-
        (24-1-(R 164 j z).card))/3) ∧
    (∀ j, loss 164 j ≤ (∑ z, (quota 164 j z : ℚ)*α 164 j z)-
      penaltySum (p 164) ((positions 164 j).val+1) (fun z => avoidedPositions (positions 164) (R 164 j z)) (α 164 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 164) (k.val+1) true)
      (min (CachedRows.cachedA (p 164) (k.val+1) false) (CachedRows.cachedC (p 164) (k.val+1)-centerLoss (positions 164) (loss 164) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_165 : Numeric.validProfile (p 165) 34 ∧ (p 165).emptyPairCap=none ∧
    (∀ j, (positions 165 j).val+1∈(p 165).correctionCenters) ∧
    (∀ j z, 0≤α 165 j z) ∧ (∀ j z, j∉R 165 j z) ∧
    (∀ j z, quota 165 j z ≤
      (4*avoidedCount (p 165) ((positions 165 j).val+1) (avoidedPositions (positions 165) (R 165 j z))+2-
        (24-1-(R 165 j z).card))/3) ∧
    (∀ j, loss 165 j ≤ (∑ z, (quota 165 j z : ℚ)*α 165 j z)-
      penaltySum (p 165) ((positions 165 j).val+1) (fun z => avoidedPositions (positions 165) (R 165 j z)) (α 165 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 165) (k.val+1) true)
      (min (CachedRows.cachedA (p 165) (k.val+1) false) (CachedRows.cachedC (p 165) (k.val+1)-centerLoss (positions 165) (loss 165) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_166 : Numeric.validProfile (p 166) 34 ∧ (p 166).emptyPairCap=none ∧
    (∀ j, (positions 166 j).val+1∈(p 166).correctionCenters) ∧
    (∀ j z, 0≤α 166 j z) ∧ (∀ j z, j∉R 166 j z) ∧
    (∀ j z, quota 166 j z ≤
      (4*avoidedCount (p 166) ((positions 166 j).val+1) (avoidedPositions (positions 166) (R 166 j z))+2-
        (24-1-(R 166 j z).card))/3) ∧
    (∀ j, loss 166 j ≤ (∑ z, (quota 166 j z : ℚ)*α 166 j z)-
      penaltySum (p 166) ((positions 166 j).val+1) (fun z => avoidedPositions (positions 166) (R 166 j z)) (α 166 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 166) (k.val+1) true)
      (min (CachedRows.cachedA (p 166) (k.val+1) false) (CachedRows.cachedC (p 166) (k.val+1)-centerLoss (positions 166) (loss 166) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_167 : Numeric.validProfile (p 167) 34 ∧ (p 167).emptyPairCap=none ∧
    (∀ j, (positions 167 j).val+1∈(p 167).correctionCenters) ∧
    (∀ j z, 0≤α 167 j z) ∧ (∀ j z, j∉R 167 j z) ∧
    (∀ j z, quota 167 j z ≤
      (4*avoidedCount (p 167) ((positions 167 j).val+1) (avoidedPositions (positions 167) (R 167 j z))+2-
        (24-1-(R 167 j z).card))/3) ∧
    (∀ j, loss 167 j ≤ (∑ z, (quota 167 j z : ℚ)*α 167 j z)-
      penaltySum (p 167) ((positions 167 j).val+1) (fun z => avoidedPositions (positions 167) (R 167 j z)) (α 167 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 167) (k.val+1) true)
      (min (CachedRows.cachedA (p 167) (k.val+1) false) (CachedRows.cachedC (p 167) (k.val+1)-centerLoss (positions 167) (loss 167) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_168 : Numeric.validProfile (p 168) 34 ∧ (p 168).emptyPairCap=none ∧
    (∀ j, (positions 168 j).val+1∈(p 168).correctionCenters) ∧
    (∀ j z, 0≤α 168 j z) ∧ (∀ j z, j∉R 168 j z) ∧
    (∀ j z, quota 168 j z ≤
      (4*avoidedCount (p 168) ((positions 168 j).val+1) (avoidedPositions (positions 168) (R 168 j z))+2-
        (24-1-(R 168 j z).card))/3) ∧
    (∀ j, loss 168 j ≤ (∑ z, (quota 168 j z : ℚ)*α 168 j z)-
      penaltySum (p 168) ((positions 168 j).val+1) (fun z => avoidedPositions (positions 168) (R 168 j z)) (α 168 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 168) (k.val+1) true)
      (min (CachedRows.cachedA (p 168) (k.val+1) false) (CachedRows.cachedC (p 168) (k.val+1)-centerLoss (positions 168) (loss 168) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_169 : Numeric.validProfile (p 169) 34 ∧ (p 169).emptyPairCap=none ∧
    (∀ j, (positions 169 j).val+1∈(p 169).correctionCenters) ∧
    (∀ j z, 0≤α 169 j z) ∧ (∀ j z, j∉R 169 j z) ∧
    (∀ j z, quota 169 j z ≤
      (4*avoidedCount (p 169) ((positions 169 j).val+1) (avoidedPositions (positions 169) (R 169 j z))+2-
        (24-1-(R 169 j z).card))/3) ∧
    (∀ j, loss 169 j ≤ (∑ z, (quota 169 j z : ℚ)*α 169 j z)-
      penaltySum (p 169) ((positions 169 j).val+1) (fun z => avoidedPositions (positions 169) (R 169 j z)) (α 169 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 169) (k.val+1) true)
      (min (CachedRows.cachedA (p 169) (k.val+1) false) (CachedRows.cachedC (p 169) (k.val+1)-centerLoss (positions 169) (loss 169) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
