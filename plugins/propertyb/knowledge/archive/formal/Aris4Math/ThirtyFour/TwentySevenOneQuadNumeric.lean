import Aris4Math.ThirtyFour.TwentySevenOneQuadData
namespace Aris4Math.ThirtyFour.TwentySevenOneQuadNumeric
open scoped BigOperators
open Aris4Math.ThirtyFour.TwentySevenOneQuadData
open Aris4Math.ThirtyThree.RefinedDeletion
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧
    (∑ k : Fin 20, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ∀ j : Fin 4,
      loss i ((positions i j).val+1)=lossAt i j ∧
      (∀ z, 0 ≤ alpha i j z) ∧ (∀ z, j ∉ avoid i j z) ∧
      (∀ z, quota i j z ≤
        (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (avoid i j z))+2-
          (20-1-(avoid i j z).card))/3) ∧
      lossAt i j ≤ (∑ z : Fin 3, (quota i j z : ℚ)*alpha i j z) -
        penaltySum (p i) ((positions i j).val+1)
          (fun z => avoidedPositions (positions i) (avoid i j z)) (alpha i j) := by
  intro i
  fin_cases i <;> simp only [p_eq_computed] <;> unfold Numeric.validProfile <;> decide +kernel
end Aris4Math.ThirtyFour.TwentySevenOneQuadNumeric
#print axioms Aris4Math.ThirtyFour.TwentySevenOneQuadNumeric.certificates
