import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000Data
namespace Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000Numeric
open scoped BigOperators
open TwentyOneSevenFive77778Batch000Data
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (21-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 21, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  fin_cases i <;> simp only [p_eq_computed] <;> unfold Numeric.validProfile <;> decide +kernel
end Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000Numeric
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch000Numeric.certificates
