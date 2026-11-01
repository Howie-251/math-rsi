import Aris4Math.ThirtyFour.TwentyFourSixLowBadData
import Aris4Math.ThirtyFour.CachedRows
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
open scoped BigOperators
open TwentyFourSixLowBadData
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem cached_case_140 : Numeric.validProfile (p 140) 34 ∧ (p 140).emptyPairCap=none ∧
    (∀ j, (positions 140 j).val+1∈(p 140).correctionCenters) ∧
    (∀ j z, 0≤α 140 j z) ∧ (∀ j z, j∉R 140 j z) ∧
    (∀ j z, quota 140 j z ≤
      (4*avoidedCount (p 140) ((positions 140 j).val+1) (avoidedPositions (positions 140) (R 140 j z))+2-
        (24-1-(R 140 j z).card))/3) ∧
    (∀ j, loss 140 j ≤ (∑ z, (quota 140 j z : ℚ)*α 140 j z)-
      penaltySum (p 140) ((positions 140 j).val+1) (fun z => avoidedPositions (positions 140) (R 140 j z)) (α 140 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 140) (k.val+1) true)
      (min (CachedRows.cachedA (p 140) (k.val+1) false) (CachedRows.cachedC (p 140) (k.val+1)-centerLoss (positions 140) (loss 140) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_141 : Numeric.validProfile (p 141) 34 ∧ (p 141).emptyPairCap=none ∧
    (∀ j, (positions 141 j).val+1∈(p 141).correctionCenters) ∧
    (∀ j z, 0≤α 141 j z) ∧ (∀ j z, j∉R 141 j z) ∧
    (∀ j z, quota 141 j z ≤
      (4*avoidedCount (p 141) ((positions 141 j).val+1) (avoidedPositions (positions 141) (R 141 j z))+2-
        (24-1-(R 141 j z).card))/3) ∧
    (∀ j, loss 141 j ≤ (∑ z, (quota 141 j z : ℚ)*α 141 j z)-
      penaltySum (p 141) ((positions 141 j).val+1) (fun z => avoidedPositions (positions 141) (R 141 j z)) (α 141 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 141) (k.val+1) true)
      (min (CachedRows.cachedA (p 141) (k.val+1) false) (CachedRows.cachedC (p 141) (k.val+1)-centerLoss (positions 141) (loss 141) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_142 : Numeric.validProfile (p 142) 34 ∧ (p 142).emptyPairCap=none ∧
    (∀ j, (positions 142 j).val+1∈(p 142).correctionCenters) ∧
    (∀ j z, 0≤α 142 j z) ∧ (∀ j z, j∉R 142 j z) ∧
    (∀ j z, quota 142 j z ≤
      (4*avoidedCount (p 142) ((positions 142 j).val+1) (avoidedPositions (positions 142) (R 142 j z))+2-
        (24-1-(R 142 j z).card))/3) ∧
    (∀ j, loss 142 j ≤ (∑ z, (quota 142 j z : ℚ)*α 142 j z)-
      penaltySum (p 142) ((positions 142 j).val+1) (fun z => avoidedPositions (positions 142) (R 142 j z)) (α 142 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 142) (k.val+1) true)
      (min (CachedRows.cachedA (p 142) (k.val+1) false) (CachedRows.cachedC (p 142) (k.val+1)-centerLoss (positions 142) (loss 142) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_143 : Numeric.validProfile (p 143) 34 ∧ (p 143).emptyPairCap=none ∧
    (∀ j, (positions 143 j).val+1∈(p 143).correctionCenters) ∧
    (∀ j z, 0≤α 143 j z) ∧ (∀ j z, j∉R 143 j z) ∧
    (∀ j z, quota 143 j z ≤
      (4*avoidedCount (p 143) ((positions 143 j).val+1) (avoidedPositions (positions 143) (R 143 j z))+2-
        (24-1-(R 143 j z).card))/3) ∧
    (∀ j, loss 143 j ≤ (∑ z, (quota 143 j z : ℚ)*α 143 j z)-
      penaltySum (p 143) ((positions 143 j).val+1) (fun z => avoidedPositions (positions 143) (R 143 j z)) (α 143 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 143) (k.val+1) true)
      (min (CachedRows.cachedA (p 143) (k.val+1) false) (CachedRows.cachedC (p 143) (k.val+1)-centerLoss (positions 143) (loss 143) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_144 : Numeric.validProfile (p 144) 34 ∧ (p 144).emptyPairCap=none ∧
    (∀ j, (positions 144 j).val+1∈(p 144).correctionCenters) ∧
    (∀ j z, 0≤α 144 j z) ∧ (∀ j z, j∉R 144 j z) ∧
    (∀ j z, quota 144 j z ≤
      (4*avoidedCount (p 144) ((positions 144 j).val+1) (avoidedPositions (positions 144) (R 144 j z))+2-
        (24-1-(R 144 j z).card))/3) ∧
    (∀ j, loss 144 j ≤ (∑ z, (quota 144 j z : ℚ)*α 144 j z)-
      penaltySum (p 144) ((positions 144 j).val+1) (fun z => avoidedPositions (positions 144) (R 144 j z)) (α 144 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 144) (k.val+1) true)
      (min (CachedRows.cachedA (p 144) (k.val+1) false) (CachedRows.cachedC (p 144) (k.val+1)-centerLoss (positions 144) (loss 144) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_145 : Numeric.validProfile (p 145) 34 ∧ (p 145).emptyPairCap=none ∧
    (∀ j, (positions 145 j).val+1∈(p 145).correctionCenters) ∧
    (∀ j z, 0≤α 145 j z) ∧ (∀ j z, j∉R 145 j z) ∧
    (∀ j z, quota 145 j z ≤
      (4*avoidedCount (p 145) ((positions 145 j).val+1) (avoidedPositions (positions 145) (R 145 j z))+2-
        (24-1-(R 145 j z).card))/3) ∧
    (∀ j, loss 145 j ≤ (∑ z, (quota 145 j z : ℚ)*α 145 j z)-
      penaltySum (p 145) ((positions 145 j).val+1) (fun z => avoidedPositions (positions 145) (R 145 j z)) (α 145 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 145) (k.val+1) true)
      (min (CachedRows.cachedA (p 145) (k.val+1) false) (CachedRows.cachedC (p 145) (k.val+1)-centerLoss (positions 145) (loss 145) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_146 : Numeric.validProfile (p 146) 34 ∧ (p 146).emptyPairCap=none ∧
    (∀ j, (positions 146 j).val+1∈(p 146).correctionCenters) ∧
    (∀ j z, 0≤α 146 j z) ∧ (∀ j z, j∉R 146 j z) ∧
    (∀ j z, quota 146 j z ≤
      (4*avoidedCount (p 146) ((positions 146 j).val+1) (avoidedPositions (positions 146) (R 146 j z))+2-
        (24-1-(R 146 j z).card))/3) ∧
    (∀ j, loss 146 j ≤ (∑ z, (quota 146 j z : ℚ)*α 146 j z)-
      penaltySum (p 146) ((positions 146 j).val+1) (fun z => avoidedPositions (positions 146) (R 146 j z)) (α 146 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 146) (k.val+1) true)
      (min (CachedRows.cachedA (p 146) (k.val+1) false) (CachedRows.cachedC (p 146) (k.val+1)-centerLoss (positions 146) (loss 146) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_147 : Numeric.validProfile (p 147) 34 ∧ (p 147).emptyPairCap=none ∧
    (∀ j, (positions 147 j).val+1∈(p 147).correctionCenters) ∧
    (∀ j z, 0≤α 147 j z) ∧ (∀ j z, j∉R 147 j z) ∧
    (∀ j z, quota 147 j z ≤
      (4*avoidedCount (p 147) ((positions 147 j).val+1) (avoidedPositions (positions 147) (R 147 j z))+2-
        (24-1-(R 147 j z).card))/3) ∧
    (∀ j, loss 147 j ≤ (∑ z, (quota 147 j z : ℚ)*α 147 j z)-
      penaltySum (p 147) ((positions 147 j).val+1) (fun z => avoidedPositions (positions 147) (R 147 j z)) (α 147 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 147) (k.val+1) true)
      (min (CachedRows.cachedA (p 147) (k.val+1) false) (CachedRows.cachedC (p 147) (k.val+1)-centerLoss (positions 147) (loss 147) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_148 : Numeric.validProfile (p 148) 34 ∧ (p 148).emptyPairCap=none ∧
    (∀ j, (positions 148 j).val+1∈(p 148).correctionCenters) ∧
    (∀ j z, 0≤α 148 j z) ∧ (∀ j z, j∉R 148 j z) ∧
    (∀ j z, quota 148 j z ≤
      (4*avoidedCount (p 148) ((positions 148 j).val+1) (avoidedPositions (positions 148) (R 148 j z))+2-
        (24-1-(R 148 j z).card))/3) ∧
    (∀ j, loss 148 j ≤ (∑ z, (quota 148 j z : ℚ)*α 148 j z)-
      penaltySum (p 148) ((positions 148 j).val+1) (fun z => avoidedPositions (positions 148) (R 148 j z)) (α 148 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 148) (k.val+1) true)
      (min (CachedRows.cachedA (p 148) (k.val+1) false) (CachedRows.cachedC (p 148) (k.val+1)-centerLoss (positions 148) (loss 148) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
theorem cached_case_149 : Numeric.validProfile (p 149) 34 ∧ (p 149).emptyPairCap=none ∧
    (∀ j, (positions 149 j).val+1∈(p 149).correctionCenters) ∧
    (∀ j z, 0≤α 149 j z) ∧ (∀ j z, j∉R 149 j z) ∧
    (∀ j z, quota 149 j z ≤
      (4*avoidedCount (p 149) ((positions 149 j).val+1) (avoidedPositions (positions 149) (R 149 j z))+2-
        (24-1-(R 149 j z).card))/3) ∧
    (∀ j, loss 149 j ≤ (∑ z, (quota 149 j z : ℚ)*α 149 j z)-
      penaltySum (p 149) ((positions 149 j).val+1) (fun z => avoidedPositions (positions 149) (R 149 j z)) (α 149 j)) ∧
    (∑ k : Fin 24, min (CachedRows.cachedA (p 149) (k.val+1) true)
      (min (CachedRows.cachedA (p 149) (k.val+1) false) (CachedRows.cachedC (p 149) (k.val+1)-centerLoss (positions 149) (loss 149) (k.val+1))))<1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowBadNumeric
