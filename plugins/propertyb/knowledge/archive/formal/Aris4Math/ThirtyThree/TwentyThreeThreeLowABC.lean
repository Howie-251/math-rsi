import Aris4Math.ThirtyThree.TwentyThreeThreeLowData
namespace Aris4Math.ThirtyThree.TwentyThreeThreeLowNumeric
open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyThreeThreeLowData
open Aris4Math.ThirtyThree.RefinedDeletion
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem abc_exact : ∀ c : Case, ∀ k : Fin 23,
    Numeric.boundA (p c) (k.val+1) = (abc c k).1 ∧
    Numeric.boundB (p c) (k.val+1) = (abc c k).2.1 ∧
    Numeric.boundC (p c) (k.val+1) = (abc c k).2.2 := by
  intro c
  fin_cases c <;> decide +kernel

#print axioms abc_exact
end Aris4Math.ThirtyThree.TwentyThreeThreeLowNumeric
