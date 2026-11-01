import Aris4Math.ThirtyThree.TwentyThreeFourLowUnitFacts
namespace Aris4Math.ThirtyThree.TwentyThreeFourLowUnitNumeric
open TwentyThreeFourLowUnitData
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem abc_exact : ∀ c : Config, ∀ k : Fin 23,
    Numeric.boundA (p c) (k.val+1) = (abc c k).1 ∧
    Numeric.boundB (p c) (k.val+1) = (abc c k).2.1 ∧
    Numeric.boundC (p c) (k.val+1) = (abc c k).2.2 := by
  intro c
  fin_cases c <;> decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem weights_exact : ∀ c : Config, ∀ j : Fin 4, ∀ b : Fin 7,
    weights c j b =
      Numeric.pairWeight (p c) ⟨QuadProfiles.executableType (positions c) (slot (family c) j b).1,0⟩
        ⟨QuadProfiles.executableType (positions c) (slot (family c) j b).2,0⟩ ((positions c j).val+1) +
      Numeric.pairWeight (p c) ⟨QuadProfiles.executableType (positions c) (slot (family c) j b).2,0⟩
        ⟨QuadProfiles.executableType (positions c) (slot (family c) j b).1,0⟩ ((positions c j).val+1) := by
  intro c
  fin_cases c <;> decide +kernel

end Aris4Math.ThirtyThree.TwentyThreeFourLowUnitNumeric
#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowUnitNumeric.abc_exact
#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowUnitNumeric.weights_exact
